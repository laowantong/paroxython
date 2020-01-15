from collections import defaultdict
from unicodedata import normalize

import pytest
import regex  # type: ignore
import sqlparse

import context
from paroxython.parse_program import ProgramParser
from paroxython.user_types import Program
from paroxython.preprocess_source import (
    cleanup_factory,
    centrifugate_hints,
    collect_hints,
    remove_hints,
)


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


def reformat_sql(match):
    string = sqlparse.format(
        match.group(1),
        reindent=True,
        keyword_case="upper",
        identifier_case="lower",
        indent_width=2,
    ).replace("\n\n", "\n")
    return f"```sql\n{string}\n```"


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
    text = regex.sub(r"(?ms)^```sql\n(.+?)\n```", reformat_sql, text)
    construct_path.write_text(text)


def extract_examples(construct_path):
    text = construct_path.read_text()
    rex = r"""(?msx)
        ^\#{4}\s+Construct\s+`(.+?)` # capture the label's name
        .+?\#{5}\s+Example # ensure the next code is in the Example section
        .+?```python\n+(.+?)\n``` # capture the source
        .+?\#{5}\s+Matches.+?^\|:--\|:--\| # ensure the table is in the Matches section
        (\n\|\s`(?P<LABELS>[^\|]+)`\s\|\s(?P<LINES>[^\|]+)\s\|)+ # capture the expected results
    """
    return regex.finditer(rex, text)


parse = ProgramParser()
reformat_file(parse.ref_path)
examples = []
for match in extract_examples(parse.ref_path):
    label_name = match.group(1)
    source = match.group(2)
    source = regex.sub(r"(?m)^.{1,4}", "", source)
    source = centrifugate_hints(source)
    (addition, deletion) = collect_hints(source)
    source = remove_hints(source)
    actual_results = dict(parse(Program(source=source, addition=addition, deletion=deletion)))
    expected_results = list(zip(match.captures("LABELS"), match.captures("LINES")))
    examples.append((label_name, actual_results, expected_results))


@pytest.mark.parametrize("label_name, actual_results, expected_results", examples)
def test_example(label_name, actual_results, expected_results):
    keys = set(actual_results.keys())
    for (expected_label_name, expected_spans) in expected_results:
        assert expected_label_name in keys
        actual_spans = ", ".join(map(str, actual_results[expected_label_name]))
        assert actual_spans == expected_spans
        keys.discard(expected_label_name)
    n = len(label_name)
    for expected_label_name in keys:
        if expected_label_name.partition(":")[0] == label_name:
            actual_spans = ", ".join(map(str, actual_results[expected_label_name]))
            message = f"{expected_label_name} unexpectedly appears on {actual_spans}"
            assert not expected_label_name[n:], message


def test_at_least_one_example_is_provided_for_each_construct():
    expected = set(parse.constructs)
    actual_results = {label_name.partition(":")[0] for (label_name, _, _) in examples}
    assert actual_results.issuperset(expected)


def test_malformed_example():
    source = "if foo():\nbar() # wrong indentation"
    result = parse(Program(source=source))
    assert result == [("ast_construction:IndentationError", [])]
