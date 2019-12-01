import pytest
import regex
from md_toc import build_toc

import context
from paroxython import parser


def reformat_file(construct_path):
    text = construct_path.read_text()
    toc = build_toc(construct_path, keep_header_levels=4, no_list_coherence=True)
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


parse = parser.Parser()
reformat_file(parse.ref_path)
examples = []
for match in extract_examples(parse.ref_path):
    label_name = match.group(1)
    source = match.group(2)
    results = zip(match.captures("LABELS"), match.captures("LINES"))
    examples.append((label_name, source, results))
pytest.main(args=["-q"])


@pytest.mark.parametrize("label_name, source, results", examples)
def test_example(label_name, source, results):
    source = regex.sub(r"(?m)^.{4}", "", source)
    actual = dict(parse(source))
    keys = set(actual.keys())
    for (label_name, expected_spots) in results:
        assert label_name in keys
        actual_spots = ", ".join(map(str, actual[label_name]))
        assert actual_spots == expected_spots


def test_at_least_one_example_is_provided_for_each_construct():
    expected = set(parse.constructs)
    actual = set(label_name.partition(":")[0] for (label_name, _, _) in examples)
    assert actual == expected

