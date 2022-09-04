from pathlib import Path
import pytest
import regex  # type: ignore

from make_snapshot import make_snapshot

import context
from paroxython.goodies import couple_to_string
from paroxython.list_programs import list_programs
from paroxython.parse_program import ProgramParser, get_bindings
from paroxython.preprocess_source import (
    centrifugate_hints,
    collect_hints,
    remove_hints,
)
from paroxython.user_types import Program, Span
from helpers.reformat_spec import reformat_spec


def extract_examples(spec_path):
    text = spec_path.read_text()
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
    program = Program(source=source, labels=[], taxa=[], addition=addition, deletion=deletion)
    actual_results = dict(parse(program))
    expected_results = list(zip(match.captures("LABELS"), match.captures("LINES")))
    examples.append((label_name, actual_results, expected_results))


@pytest.mark.parametrize("label_name, actual_results, expected_results", examples)
def test_example(label_name, actual_results, expected_results):
    keys = set(actual_results.keys())
    for (expected_label_name, expected_spans) in expected_results:
        expected_spans = expected_spans.split(" / ")
        if keys == {"ast_construction:SyntaxError"}:
            assert "SyntaxError" in expected_spans
            continue
        assert expected_label_name in keys
        actual_spans = ", ".join(map(couple_to_string, actual_results[expected_label_name]))
        assert actual_spans in expected_spans
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
    result = parse(Program(source=source, labels=[], taxa=[], addition={}, deletion={}))
    print(result)
    assert result[0].name == "ast_construction:IndentationError"


def test_empty_example():
    source = ""
    result = parse(Program(source=source, labels=[], taxa=[], addition={}, deletion={}))
    print(result)
    assert result[0].name == "ast_construction:EmptyProgramError"


def test_label_presence(capsys):
    all_names = set()
    present_names = set()
    result = []
    for program in list_programs(Path("examples/mini/programs/")):
        labels = parse(
            Program(source=program.source, labels=[], taxa=[], addition={}, deletion={}),
            yield_failed_matches=True,
        )
        for (name, spans) in labels:
            all_names.add(name)
            if spans:
                present_names.add(name)
                result.append(
                    name + f" / {program.path} / " + ", ".join(map(couple_to_string, spans))
                )
    present = "\n- ".join(sorted(result))
    absent = "\n- ".join(sorted(all_names - present_names))
    text = f"# Present labels\n\n- {present}\n\n# Absent labels\n\n- {absent}\n"
    make_snapshot(Path("examples/mini/labels.md"), text, capsys)


label_captures = [
    {  # 0 SUFFIX and 1 POS
        "name": "null_operation",
        "captures": {"POS": ["4:1-3-1-5-1-"]},
        "expected": [("null_operation", Span(start=4, end=4, path="1-3-1-5-1-"))],
    },
    {  # 1 empty SUFFIX and 1 POS
        "name": "divisibility_test",
        "captures": {"POS": ["15:3-5-1-2-1-0-"], "SUFFIX": []},
        "expected": [("divisibility_test", Span(start=15, end=15, path="3-5-1-2-1-0-"))],
    },
    {  # 0 SUFFIX and n POS, with n > 1
        "name": "while",
        "captures": {"POS": ["11:2-", "16:2-1-4-2-1-2-"]},
        "expected": [("while", Span(start=11, end=16, path="2-"))],
    },
    {  # 1 empty SUFFIX and n POS, with n > 1
        "name": "foobar",
        "captures": {"POS": ["11:2-", "16:2-1-4-2-1-2-"]},
        "expected": [("foobar", Span(start=11, end=16, path="2-"))],
    },
    {  # 1 SUFFIX and 1 POS
        "name": "literal",
        "captures": {"POS": ["16:3-5-1-2-1-1-1-0-"], "SUFFIX": ["False"]},
        "expected": [("literal:False", Span(start=16, end=16, path="3-5-1-2-1-1-1-0-"))],
    },
    {  # 1 SUFFIX and n POS, with n > 1
        "name": "for",
        "captures": {"POS": ["1:1-", "5:1-0-", "10:1-2-3-2-"], "SUFFIX": ["i"]},
        "expected": [("for:i", Span(start=1, end=10, path="1-"))],
    },
    {  # n SUFFIX and 1 POS, with n > 1
        "name": "import_module",
        "captures": {"POS": ["1:1-"], "SUFFIX": ["m1", "m2", "m3"]},
        "expected": [
            ("import_module:m1", Span(start=1, end=1, path="1-")),
            ("import_module:m2", Span(start=1, end=1, path="1-")),
            ("import_module:m3", Span(start=1, end=1, path="1-")),
        ],
    },
    {  # n SUFFIX and n POS, with n > 1
        "name": "if_test_atom",
        "captures": {
            "POS": ["31:5-2-1-0-0-0-", "31:5-2-1-0-0-2-1-1-", "31:5-2-1-0-2-1-"],
            "SUFFIX": ["b", "a", "greatest"],
        },
        "expected": [
            ("if_test_atom:b", Span(start=31, end=31, path="5-2-1-0-0-0-")),
            ("if_test_atom:a", Span(start=31, end=31, path="5-2-1-0-0-2-1-1-")),
            ("if_test_atom:greatest", Span(start=31, end=31, path="5-2-1-0-2-1-")),
        ],
    },
    {  # n SUFFIX and more POS, with n > 1
        "name": "function_decorator",
        "captures": {
            "POS": ["1:1-", "1:1-2-1-", "2:1-2-2-", "3:1-2-3-", "5:1-5-1-"],
            "SUFFIX": ["bizz", "foo", "bar"],
        },
        "expected": [
            ("function_decorator:bizz", Span(start=1, end=5, path="1-")),
            ("function_decorator:foo", Span(start=1, end=5, path="1-")),
            ("function_decorator:bar", Span(start=1, end=5, path="1-")),
        ],
    },
]
label_captures = (d.values() for d in label_captures)


@pytest.mark.parametrize("name, captures, expected", label_captures)
def test_get_bindings(name, captures, expected):
    print(name)
    result = list(get_bindings(name, captures))
    print(result)
    assert result == expected


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
