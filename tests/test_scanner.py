import pytest

import context
from scanner import Scanner

scan = Scanner("tests/data/programs")


def test_generate_tagged_source_codes():
    result = list(scan.generate_tagged_source_codes())
    expected = [
        "# ----------------------------------------------------------------------------------------\n"
        "# tests/data/programs/assignment.py\n"
        "# ----------------------------------------------------------------------------------------",
        "a = b # assignment, global_variable_definition\n",
        "# ----------------------------------------------------------------------------------------\n"
        "# tests/data/programs/function_definition.py\n"
        "# ----------------------------------------------------------------------------------------",
        "def succ(n): # function_definition:succ (-> +1)\n"
        "    return n + 1 # binary_operator:Add, literal:Num\n",
        "# ----------------------------------------------------------------------------------------\n"
        "# tests/data/programs/loop.py\n"
        "# ----------------------------------------------------------------------------------------",
        "while input(): # function_call:input\n"
        '    print("foobar") # function_call:print, literal:Str\n',
    ]
    assert result == expected


def test_generate_lists_of_tags():
    result = list(scan.generate_lists_of_tags())
    expected = [
        (
            "tests/data/programs/assignment.py",
            {"assignment": [(1, 1)], "global_variable_definition": [(1, 1)]},
        ),
        (
            "tests/data/programs/function_definition.py",
            {
                "binary_operator:Add": [(2, 2)],
                "function_definition:succ": [(1, 2)],
                "literal:Num": [(2, 2)],
            },
        ),
        (
            "tests/data/programs/loop.py",
            {
                "function_call:input": [(1, 1)],
                "function_call:print": [(2, 2)],
                "literal:Str": [(2, 2)],
            },
        ),
    ]
    for (rk, rv), (ek, ev) in zip(result, expected):
        assert rk == ek
        for (label, spans) in rv.items():
            assert ev[label] == [span.to_couple() for span in spans]


pytest.main(args=["-q"])
