import pytest
import regex
from md_toc import build_toc

import context
from paroxython import parser


def reformat_file(construct_path):
    text = construct_path.read_text()
    toc = build_toc(construct_path, keep_header_levels=5, no_list_coherence=True)
    rule = "-" * 80 + "\n"
    text = regex.sub(r"(?m)^---+\n", "", text)
    text = regex.sub(r"(?m)^ +```", "```", text)
    text = regex.sub(r"(?ms).*?^(?=# )", fr"{toc}\n\n", text, count=1)
    text = regex.sub(r"(?m)\s+^(#+ .+)\s+", fr"\n\n\1\n\n", text)
    text = regex.sub(r"(?ms)(```markdown.+?```.+?)(^\#{1,4} )", fr"\1{rule}\n\2", text)
    text = regex.sub(r"(?=\n\#{5} )", fr"\n{rule}", text)
    construct_path.write_text(text)


def extract_examples(construct_path):
    text = construct_path.read_text()
    rex = r"""(?msx)
        ^\#{5}\s+Construct\s+`(.+?)` # capture the label
        .+?\#{6}\s+Example # ensure the next code is in the Example section
        .+?```python\n+(.+?)\n``` # capture the source-code
        .+?\#{6}\s+Matches # ensure the next results are in the Example section
        .+?```markdown\n+(.+?)\n``` # capture the expected results
    """
    return regex.findall(rex, text)


parse = parser.Parser()
reformat_file(parse.ref_path)
examples = extract_examples(parse.ref_path)
pytest.main(args=["-q"])


@pytest.mark.parametrize("label, source, results", examples)
def test_example(label, source, results):
    source = regex.sub(r"(?m)^.{4}", "", source)
    results = (line.partition(": ")[0::2] for line in results.split("\n"))
    actual = dict(parse(source))
    for (label, expected) in results:
        keys = list(actual.keys())
        assert label in keys
        actual_label = ", ".join(actual[label])
        assert actual_label == expected


def test_at_least_one_example_is_provided_for_each_construct():
    expected = set(parse.constructs)
    actual = set(label.partition("=")[0] for (label, _, _) in examples)
    assert actual == expected

