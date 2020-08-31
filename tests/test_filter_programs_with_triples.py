import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter
from paroxython.compare_spans import compare_spans

db = json.loads(Path("examples/mini/programs_db.json").read_text())
dbf = ProgramFilter(db)

triple_data = [
    (
        (
            "var/assignment/explicit/single",  # featured by assignment.py and collatz.py
            compare_spans["after"],  # but after
            "call/subroutine/builtin/print",  # this taxon in collatz.py only.
        ),
        {"collatz.py"},
    ),
    (
        (
            "operator/arithmetic/addition",  # this taxon is featured by collatz.py only
            compare_spans["equals"],  # and on the same line
            "operator/arithmetic/multiplication",  # as that taxon
        ),
        {"collatz.py"},
    ),
    (
        (
            "call/subroutine/builtin/range",  # this taxon is featured by fizzbuzz.py only
            compare_spans["inside"],  # but not inside of
            "flow/conditional",  # that taxon
        ),
        set(),
    ),
    (
        (
            "operator/arithmetic/modulo",  # featured by all programs except assignment.py
            compare_spans["equals"],  # and always on the same line
            "type/number/integer/literal",  # as that taxon
        ),
        {"collatz.py", "is_even.py", "fizzbuzz.py"},
    ),
    (
        (
            "condition/equality$",  # featured by all programs except assignment.py
            compare_spans["inside"],  # but only inside
            "def",  # def/subroutine/function or def/subroutine/procedure in two of them
        ),
        {"collatz.py", "is_even.py"},
    ),
    (
        (
            "call",  # featured by collatz.py and fizzbuzz.py
            compare_spans["inside"],  # but only inside
            "flow/conditional",  # a conditional in fizzbuzz.py
        ),
        {"fizzbuzz.py"},
    ),
]


@pytest.mark.parametrize("triple, expected_programs", triple_data)
def test_programs_of_triple(triple, expected_programs):
    programs = dbf.programs_of_triple(*triple)
    print(programs)
    assert programs == expected_programs


negated_triple_data = [
    (
        (
            "var/assignment/explicit/single",  # featured by assignment.py and collatz.py
            compare_spans["after"],  # but after
            "call/subroutine/builtin/print",  # this taxon in collatz.py only.
        ),
        {"assignment.py"},
    ),
    (
        (
            "operator/arithmetic/addition",  # this taxon is featured by collatz.py only
            compare_spans["equals"],  # and on the same line
            "operator/arithmetic/multiplication",  # as that taxon
        ),
        set(),
    ),
    (
        (
            "call/subroutine/builtin/range",  # this taxon is featured by fizzbuzz.py only
            compare_spans["inside"],  # but not inside of
            "flow/conditional",  # that taxon
        ),
        {"fizzbuzz.py"},
    ),
    (
        (
            "flow/conditional",  # this taxon is featured by collatz.py and fizzbuzz.py
            compare_spans["contains"],  # but it never contains
            "call/subroutine/builtin/range",  # that taxon
        ),
        {"collatz.py", "fizzbuzz.py"},  # distinct from the previous result!
    ),
    (
        (
            "operator/arithmetic/modulo",  # featured by all programs except assignment.py
            compare_spans["equals"],  # and always on the same line
            "type/number/integer/literal",  # as that taxon
        ),
        set(),
    ),
    (
        (
            "condition/equality$",  # featured by all programs except assignment.py
            compare_spans["inside"],  # but only inside
            "def",  # def/subroutine/function or def/subroutine/procedure in two of them
        ),
        {"fizzbuzz.py"},
    ),
    (
        (
            "call",  # featured by collatz.py and fizzbuzz.py
            compare_spans["inside"],  # in collatz, the two print() are not inside the conditional
            "flow/conditional",  # in fizzbuzz, although print() is inside, range() is not
        ),
        {"fizzbuzz.py", "collatz.py"},
    ),
]


@pytest.mark.parametrize("triple, expected_programs", negated_triple_data)
def test_programs_of_negated_triple(triple, expected_programs):
    programs = dbf.programs_of_negated_triple(*triple)
    print(programs)
    assert programs == expected_programs


def test_iterate_on_spans():
    call = lambda *args: list(dbf.iterate_on_spans(*args))
    result = call(
        {"a1": [1], "b1": [2, 3], "c1": [4, 5, 6], "a2": [7], "b2": [8, 9]},
        # The two following arguments are normally of type set,
        # but they are given here as lists to avoid hash randomization.
        ["a1", "b1", "c1"],
        ["a2", "b2"],
    )
    print(result)
    assert result == [
        (1, 7),  # a1 x a2
        (1, 8),  # a1 x b2
        (1, 9),  # |
        (2, 7),  # b1 x a2
        (3, 7),  # |
        (2, 8),  # b2 x b2
        (2, 9),  # |
        (3, 8),  # |
        (3, 9),  # |
        (4, 7),  # c1 x a2
        (5, 7),  # |
        (6, 7),  # |
        (4, 8),  # c1 x b1
        (4, 9),  # |
        (5, 8),  # |
        (5, 9),  # |
        (6, 8),  # |
        (6, 9),  # |
    ]
    result = call({"a1": [1], "b1": [2, 3], "c1": [1, 2, 3]}, ["a1", "b1", "c1"], ["a1", "b1"])
    print(result)
    assert result == [
        # (1, 1) skip diagonal for a1 x a1
        (1, 2),
        (1, 3),
        (2, 1),
        (3, 1),
        # (2, 2) skip diagonal for b1 x b1
        (2, 3),
        (3, 2),
        # (3, 3) skip diagonal for b1 x b1
        (1, 1),
        (2, 1),
        (3, 1),
        (1, 2),
        (1, 3),
        (2, 2),  # don't skip diagonal for b1 x c1
        (2, 3),
        (3, 2),
        (3, 3),  # don't skip diagonal for b1 x c1
    ]


if __name__ == "__main__":
    pytest.main(["-qq", "tests/test_filter_programs_with_triples.py"])
