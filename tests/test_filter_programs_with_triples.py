import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter
from paroxython.normalize_predicate import normalize_predicate
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


def _test_exclude_taxons():

    dbf = ProgramFilter(db)
    dbf.exclude_taxons(
        dbf.preprocess_taxons([("variable/assignment/single", "after", "io/standard/print")])
    )
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # "operator/arithmetic/addition" and "operator/arithmetic/multiplication" are both featured on
    # the same line of collatz.py, and indirectly by fizzbuzz.py and is_even.py. Therefore,
    # excluding this taxon keeps only assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons(
        dbf.preprocess_taxons(
            [("operator/arithmetic/addition", "equals", "operator/arithmetic/multiplication")]
        )
    )
    print(programs)
    assert programs == {"assignment.py"}

    # "test/equality" is inside "subroutine/function" in is_even.py, which is not imported anywhere.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons(dbf.programs_of_triple("test/equality", "inside", "subroutine/function"))
    print(programs)
    assert programs == {"collatz.py", "assignment.py", "fizzbuzz.py"}

    # "call/function/builtin/range" is not inside "flow/conditional" anywhere.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons(
        dbf.programs_of_triple("call/function/builtin/range", "inside", "flow/conditional")
    )
    print(programs)
    assert programs == {
        "is_even.py",
        "fizzbuzz.py",
        "assignment.py",
        "collatz.py",
    }


def _test_include_taxons():

    # The taxon "variable/assignment/single" is featured by assignment.py and collatz.py. In
    # collatz.py, it appears after a taxon "io/standard/print". Consequently, it should be included
    # in the results, but not the programs which import it: fizzbuzz.py and is_even.py.
    dbf = ProgramFilter(db)
    dbf.include_taxons(
        dbf.programs_of_triple("variable/assignment/single", "after", "io/standard/print")
    )
    print(programs)
    assert programs == {"collatz.py"}

    # "operator/arithmetic/modulo" and "type/number/integer/literal" are both featured on
    # the same line in all programs except assignment.py
    dbf = ProgramFilter(db)
    dbf.include_taxons(
        dbf.preprocess_taxons(
            [("operator/arithmetic/modulo", "equals", "type/number/integer/literal")]
        )
    )
    print(programs)
    assert programs == {"collatz.py", "is_even.py", "fizzbuzz.py"}

    # The same with "x == y" instead of "equals"
    dbf = ProgramFilter(db)
    dbf.include_taxons(
        dbf.preprocess_taxons(
            [("operator/arithmetic/modulo", "x == y", "type/number/integer/literal")]
        )
    )
    print(programs)
    assert programs == {"collatz.py", "is_even.py", "fizzbuzz.py"}

    # "test/equality" is inside "subroutine/function" in is_even.py, which is not imported anywhere.
    dbf = ProgramFilter(db)
    dbf.include_taxons(dbf.programs_of_triple("test/equality", "inside", "subroutine/function"))
    print(programs)
    assert programs == {"is_even.py"}

    # "test/equality" is inside "subroutine/function" in is_even.py and inside
    # "subroutine/procedure" in collatz.py. Both will be included.
    dbf = ProgramFilter(db)
    taxons = dbf.programs_of_triple("test/equality$", "inside", "subroutine")
    print(taxons)
    assert [(taxon.name_1, taxon.name_2) for taxon in taxons] == [
        ("test/equality", "subroutine/argument/arg"),
        ("test/equality", "subroutine/function"),
        ("test/equality", "subroutine/predicate"),
        ("test/equality", "subroutine/procedure"),
    ]
    dbf.include_taxons(taxons)
    print(programs)
    assert programs == {"collatz.py", "is_even.py"}

    # "call/function/builtin/range" is not inside "flow/conditional" anywhere.
    dbf = ProgramFilter(db)
    dbf.include_taxons(
        dbf.programs_of_triple("call/function/builtin/range", "inside", "flow/conditional")
    )
    print(programs)
    assert programs == set()

    # "call/function/builtin/print" may appear several times in the same program, but never
    # on the same line.
    dbf = ProgramFilter(db)
    dbf.include_taxons(
        dbf.preprocess_taxons(
            [("call/function/builtin/print", "is", "call/function/builtin/print")]
        )
    )
    print(programs)
    assert programs == set()

    # "type/number/integer/literal" appears twice on the same line in fizzbuzz.py and
    # collatz.py
    dbf = ProgramFilter(db)
    dbf.include_taxons(
        dbf.preprocess_taxons(
            [("type/number/integer/literal$", "is", "type/number/integer/literal$")]
        )
    )
    print(programs)
    assert programs == {"fizzbuzz.py", "collatz.py"}


def _test_programs_of_triple_positive():
    # "io/standard/print" and "flow/loop/exit/late" are both featured by collatz.py and
    # fizzbuzz.py. In collatz.py the print statements are both inside and outside the loop,
    # but in fizzbuzz.py, all print statement are inside the loop. Consequently, the unique print
    # statement not inside a loop is featured by collatz.py only. Note that assignment.py
    # and is_even.py are not included in the result, since they don't feature (at least directly)
    # the two taxons.
    dbf = ProgramFilter(db)
    programs = dbf.programs_of_triple(
        "io/standard/print", compare_spans["not inside"], "flow/loop/exit/late"
    )
    print(programs)
    assert programs == {"collatz.py"}
    # For the excluding filter, as usual, the importations are taken into account. collatz.py
    # is excluded for featuring a print statement inside a loop, and fizzbuzz.py and is_even.py are
    # excluded for importing collatz.py. The only remaining program is assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons(
        dbf.programs_of_triple(
            "io/standard/print", compare_spans["not inside"], "flow/loop/exit/late"
        )
    )
    print(programs)
    assert programs == {"assignment.py"}
    # The not operator can appear anywhere, even if it's not syntactically correct.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons(
        dbf.programs_of_triple("io/standard/print", "inside not", "flow/loop/exit/late")
    )
    print(programs)
    assert programs == {"assignment.py"}
    # It can be replaced by a "!" symbol, and of course the other normalization rules still apply.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons(
        dbf.preprocess_taxons(
            [("io/standard/print", "!(y1 ≤ x1 ≤ x2 ≤ y1)", "flow/loop/exit/late")]
        )
    )
    print(programs)
    assert programs == {"assignment.py"}


def _test_negate_taxon():
    # Keep all programs which feature a subroutine definition (i.e., collatz.py and
    # is_even.py) or no assignment (i.e., fizzbuzz.py and is_even.py). The result is the union of
    # these sets.
    dbf = ProgramFilter(db)
    dbf.include_taxons(dbf.programs_of_triple("subroutine", "!variable/assignment/single"))
    print(programs)
    assert programs == {"collatz.py", "is_even.py", "fizzbuzz.py"}
    # Negating a taxon don't make previously excluded programs reenter in the result
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"is_even.py"})
    dbf.include_taxons(
        dbf.preprocess_taxons(
            ["subroutine/function", "subroutine/procedure", "not variable/assignment/single"]
        )
    )
    print(programs)
    assert programs == {"collatz.py", "fizzbuzz.py"}


if __name__ == "__main__":
    pytest.main(["-qq", "tests/test_filter_programs_with_triples.py"])
