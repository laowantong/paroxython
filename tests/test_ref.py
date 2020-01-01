from collections import defaultdict
from unicodedata import normalize

import pytest
import regex  # type: ignore

import context
from paroxython.source_parser import SourceParser


def generate_toc(text):
    slug_counts = defaultdict(int)
    for match in regex.finditer(r"(?m)^(#{1,4}) (.+)", text):
        (hashtags, title) = match.groups()
        offset = "  " * (len(hashtags) - 1) + "- "
        slug = normalize("NFD", title.lower()).encode("ASCII", "ignore").decode("ASCII")
        slug = slug.replace(" ", "-")
        slug = regex.sub(r"[^\w-]", "", slug)
        slug = f"{slug}-{slug_counts[slug]}"
        slug = slug.rstrip("-0")
        slug_counts[slug] += 1
        yield f"{offset}[{title}](#{slug})"


def reformat_file(construct_path):
    text = construct_path.read_text()
    toc = "\n".join(generate_toc(text))
    rule = "-" * 80 + "\n"
    text = regex.sub(r"(?m)^---+\n", "", text)
    text = regex.sub(r"(?m)^ +```", "```", text)
    text = regex.sub(r"(?ms).*?^(?=# )", fr"{toc}\n\n", text, count=1)
    text = regex.sub(r"(?m)\s+^(#+ .+)\s+", fr"\n\n\1\n\n", text)
    text = regex.sub(r"(?ms)^(\| Label \| .+?)(^\#{1,3} )", fr"\1{rule}\n\2", text)
    text = regex.sub(r"(?=\n\#{4} )", fr"\n{rule}", text)
    construct_path.write_text(text)


def extract_examples(construct_path):
    text = construct_path.read_text()
    rex = r"""(?msx)
        ^\#{4}\s+Construct\s+`(.+?)` # capture the label's name
        .+?\#{5}\s+Example # ensure the next code is in the Example section
        .+?```python\n+(.+?)\n``` # capture the source-code
        .+?\#{5}\s+Matches.+?^\|:--\|:--\| # ensure the table is in the Matches section
        (\n\|\s`(?P<LABELS>[^\|]+)`\s\|\s(?P<LINES>[^\|]+)\s\|)+ # capture the expected results
    """
    return regex.finditer(rex, text)


parse = SourceParser()
reformat_file(parse.ref_path)
examples = []
for match in extract_examples(parse.ref_path):
    label_name = match.group(1)
    source = match.group(2)
    results = list(zip(match.captures("LABELS"), match.captures("LINES")))
    examples.append((label_name, source, results))


@pytest.mark.parametrize("label_name, source, results", examples)
def test_example(label_name, source, results):
    source = regex.sub(r"(?m)^.{1,4}", "", source)
    actual = dict(parse(source))
    keys = set(actual.keys())
    for (expected_label_name, expected_spans) in results:
        assert expected_label_name in keys
        actual_spans = ", ".join(map(str, actual[expected_label_name]))
        assert actual_spans == expected_spans
        keys.discard(expected_label_name)
    n = len(label_name)
    for expected_label_name in keys:
        if expected_label_name.partition(":")[0] == label_name:
            actual_spans = ", ".join(map(str, actual[expected_label_name]))
            message = f"{expected_label_name} unexpectedly appears on {actual_spans}"
            assert not expected_label_name[n:], message


def test_at_least_one_example_is_provided_for_each_construct():
    expected = set(parse.constructs)
    actual = {label_name.partition(":")[0] for (label_name, _, _) in examples}
    assert actual == expected


def test_malformed_example():
    source = "if foo():\nbar() # wrong indentation"
    with pytest.raises(StopIteration):
        next(parse(source))


def test_failed_matches():
    source = "a = 42"
    actual = dict(parse(source, yield_failed_matches=True))
    print(actual)
    assert actual.pop("assignment")[0].to_couple() == (1, 1)
    assert actual.pop("global_variable_definition")[0].to_couple() == (1, 1)
    assert actual.pop("literal:Num")[0].to_couple() == (1, 1)
    assert actual.pop("suggest_constant_definition")[0].to_couple() == (1, 1)
    for spans in actual.values():
        assert not spans


pytest.main(args=["-q"])
