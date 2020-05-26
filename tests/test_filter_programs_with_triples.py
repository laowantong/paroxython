import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter
from paroxython.compare_spans import compare_spans

db = json.loads(Path("examples/mini/programs_db.json").read_text())


def test_programs_of_triple():
    dbf = ProgramFilter(db)

    programs = dbf.programs_of_triple(
        "variable/assignment/single",  # featured by assignment.py and collatz.py
        compare_spans["after"],  # but after
        "io/standard/print",  # this taxon in collatz.py only.
    )
    print(programs)
    assert programs == {"collatz.py"}

    programs = dbf.programs_of_triple(
        "operator/arithmetic/addition",  # this taxon is featured by collatz.py only
        compare_spans["equals"],  # and on the same line
        "operator/arithmetic/multiplication",  # as that taxon
    )
    print(programs)
    assert programs == {"collatz.py"}

    programs = dbf.programs_of_triple(
        "call/function/builtin/range",  # this taxon is featured by fizzbuzz.py only
        compare_spans["inside"],  # but not inside of
        "flow/conditional",  # that taxon
    )
    print(programs)
    assert programs == set()

    programs = dbf.programs_of_triple(
        "operator/arithmetic/modulo",  # featured by all programs except assignment.py
        compare_spans["equals"],  # and always on the same line
        "type/number/integer/literal",  # as that taxon
    )
    print(programs)
    assert programs == {"collatz.py", "is_even.py", "fizzbuzz.py"}

    programs = dbf.programs_of_triple(
        "test/equality$",  # featured by all programs except assignment.py
        compare_spans["inside"],  # but only inside
        "subroutine",  # subroutine/function or subroutine/procedure in two of them
    )
    print(programs)
    assert programs == {"collatz.py", "is_even.py"}

    programs = dbf.programs_of_triple(
        "call",  # featured by collatz.py and fizzbuzz.py
        compare_spans["inside"],  # but only inside
        "flow/conditional",  # a conditional in fizzbuzz.py
    )
    print(programs)
    assert programs == {"fizzbuzz.py"}


def test_iterate_on_spans():
    call = lambda *args: list(ProgramFilter._iterate_on_spans(*args))
    result = call(
        {"a1": [1], "b1": [2, 3], "c1": [4, 5, 6], "a2": [7], "b2": [8, 9]},
        ["a1", "b1", "c1"],  # normally a set is expected...
        ["a2", "b2"],  # but force a list to defeat hash randomization.
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
