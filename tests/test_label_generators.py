from pathlib import Path

import pytest

import context
from paroxython.label_generators import (
    generate_labeled_sources,
    generate_programs_labels,
)
from paroxython.program_generator import generate_programs

programs = list(generate_programs("tests/data/programs"))


def test_generate_labeled_sources():
    result = generate_labeled_sources(programs)

    assert "assignment.py" in next(result)
    assert next(result).strip() == "a = b # assignment, global_variable_definition"

    assert "function_definition.py" in next(result)
    assert next(result).strip() == "\n".join(
        [
            "def succ(n): # function_definition:succ (-> +1)",
            "    return n + 1 # binary_operator:Add, literal:Num",
        ]
    )

    assert "loop.py" in next(result)
    assert next(result).strip() == "\n".join(
        [
            "while input(): # function_call:input",
            '    print("foobar") # function_call:print, literal:Str',
        ]
    )


def test_generate_programs_labels():
    result = list(generate_programs_labels(programs))
    expected = [
        (
            Path("tests/data/programs/assignment.py"),
            {"assignment": [(1, 1)], "global_variable_definition": [(1, 1)]},
        ),
        (
            Path("tests/data/programs/function_definition.py"),
            {
                "binary_operator:Add": [(2, 2)],
                "function_definition:succ": [(1, 2)],
                "literal:Num": [(2, 2)],
            },
        ),
        (
            Path("tests/data/programs/loop.py"),
            {
                "function_call:input": [(1, 1)],
                "function_call:print": [(2, 2)],
                "literal:Str": [(2, 2)],
            },
        ),
    ]
    for (rk, rv), (ek, ev) in zip(result, expected):
        assert rk == ek
        for (label, spans) in rv:
            assert ev[label] == [span.to_couple() for span in spans]


pytest.main(args=["-q"])
