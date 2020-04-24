from pathlib import Path
import pytest
import regex  # type: ignore

import context
from make_snapshot import make_snapshot
from paroxython.list_programs import list_programs
from paroxython.parse_program import ProgramParser
from paroxython.preprocess_source import (
    centrifugate_hints,
    collect_hints,
    remove_hints,
)
from paroxython.user_types import Program
from helpers.reformat_spec import reformat_spec


def extract_examples(feature_path):
    text = feature_path.read_text()
    rex = r"""(?msx)
        ^\#{4}\s+Feature\s+`(.+?)` # capture the label's pattern
        .+?\#{5}\s+Example # ensure the next code is in the Example section
        .+?```python\n+(.+?)\n``` # capture the source
        .+?\#{5}\s+Matches.+?^\|:--\|:--\| # ensure the table is in the Matches section
        (\n\|\s`(?P<LABELS>[^\|]+)`\s\|\s(?P<LINES>[^\|]+)\s\|)+ # capture the expected results
    """
    return regex.finditer(rex, text)


parse = ProgramParser()
reformat_spec(parse.spec_path)
examples = []
for match in extract_examples(parse.spec_path):
    label_name = match.group(1)
    source = match.group(2)
    source = regex.sub(r"(?m)^.{1,4}", "", source)
    source = centrifugate_hints(source)
    (addition, deletion) = collect_hints(source)
    source = remove_hints(source)
    actual_results = dict(
        parse(Program(source=source, labels=[], addition=addition, deletion=deletion))
    )
    expected_results = list(zip(match.captures("LABELS"), match.captures("LINES")))
    examples.append((label_name, actual_results, expected_results))


@pytest.mark.parametrize("label_name, actual_results, expected_results", examples)
def test_example(label_name, actual_results, expected_results):
    keys = set(actual_results.keys())
    print(actual_results)
    for (expected_label_name, expected_spans) in expected_results:
        assert expected_label_name in keys
        actual_spans = ", ".join(map(str, actual_results[expected_label_name]))
        assert actual_spans == expected_spans
        keys.discard(expected_label_name)
    for expected_label_name in keys:
        expected_name_prefix = expected_label_name.partition(":")[0]
        if regex.fullmatch(label_name, expected_name_prefix):
            actual_spans = ", ".join(map(str, actual_results[expected_label_name]))
            message = f"{expected_label_name} unexpectedly appears on {actual_spans}"
            raise AssertionError(message)


def test_at_least_one_example_is_provided_for_each_feature():
    expected = set(parse.features)
    actual_results = {label_name.partition(":")[0] for (label_name, _, _) in examples}
    assert actual_results.issuperset(expected)


def test_malformed_example():
    source = "if foo():\nbar() # wrong indentation"
    result = parse(Program(source=source, labels=[], addition={}, deletion={}))
    print(result)
    assert result[0].name in (
        "ast_construction:IndentationError",  # under Python 3.7 ast standard library
        "ast_construction:SyntaxError",  # under Python 3.7 with typed_ast.ast3 library
    )


def test_label_presence(capsys):
    all_names = set()
    present_names = set()
    result = []
    for program in list_programs(Path("tests/data/simple/")):
        labels = parse(
            Program(source=program.source, labels=[], addition={}, deletion={}),
            yield_failed_matches=True,
        )
        for (name, spans) in labels:
            all_names.add(name)
            if spans:
                present_names.add(name)
                result.append(name + f" / {program.name} / " + ", ".join(map(str, spans)))
    present = "\n- ".join(sorted(result))
    absent = "\n- ".join(sorted(all_names - present_names))
    text = f"# Present labels\n\n- {present}\n\n# Absent labels\n\n- {absent}\n"
    make_snapshot(Path("tests/snapshots/simple_labels.md"), text, capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
