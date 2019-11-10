import md_toc
import pytest
import regex

from context import paroxython


def reformat_file(trait_path):
    """ Update TOC and vertical spaces in the definition file. """
    with open("traits.md") as f:
        text = f.read()
    toc = md_toc.build_toc("traits.md", keep_header_levels=5, no_list_coherence=True)
    text = regex.sub(r"(?ms).*?^(?=# )", fr"{toc}\n\n", text, count=1)
    text = regex.sub(r"(?m)\s+^(#+ .+)\s+", fr"\n\n\1\n\n", text)
    with open("traits.md", "w") as f:
        f.write(text)


reformat_file("traits.md")


def extract_examples(trait_path):
    with open(trait_path) as f:
        text = f.read()
    rex = r"""(?msx)
        ^\#{5}\s+`(.+?)` # capture the label
        .+?
        \#{6}\s+Example # ensure the next code is in the Example section
        .+?
        ```python\n+(.+?)\n``` # capture the source-code
        .+?
        \#{6}\s+Matches # ensure the next results are in the Example section
        .+?
        ```markdown\n+(.+?)\n``` # capture the expected results
    """
    return regex.findall(rex, text)


examples = extract_examples("traits.md")


@pytest.mark.parametrize("label, source, results", examples)
def test_example(label, source, results):
    source = regex.sub(r"(?m)^.{4}", "", source)
    results = (line.partition(": ")[0::2] for line in results.split("\n"))
    actual = set(parse(source).items())
    for (label, expected) in results:
        assert (label, expected) in actual


def test_at_least_one_example_is_provided_for_each_trait():
    expected = set(parse.traits)
    actual = set(label.partition("-")[0] for (label, _, _) in examples)
    assert actual == expected


parse = paroxython.Parser("traits.md")
pytest.main(args=["-q"])
