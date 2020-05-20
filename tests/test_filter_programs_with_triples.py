import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter


db = json.loads(Path("tests/snapshots/simple_db.json").read_text())


def test_exclude_taxons():

    # The taxon "variable/assignment/single" is featured by assignment.py and collatz_print.py. In
    # collatz_print.py, it appears after a taxon "io/standard/print". Consequently, it should be excluded
    # from the results, along with the programs which import it: fizzbuzz.py and is_even.py.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({("variable/assignment/single", "after", "io/standard/print")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # "operator/arithmetic/addition" and "operator/arithmetic/multiplication" are both featured on
    # the same line of collatz_print.py, and indirectly by fizzbuzz.py and is_even.py. Therefore,
    # excluding this taxon keeps only assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons(
        {("operator/arithmetic/addition", "equals", "operator/arithmetic/multiplication")}
    )
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # "test/equality" is inside "subroutine/function" in is_even.py, which is not imported anywhere.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({("test/equality", "inside", "subroutine/function")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "assignment.py", "fizzbuzz.py"}

    # "call/function/builtin/range" is not inside "flow/conditional" anywhere.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons([("call/function/builtin/range", "inside", "flow/conditional")])
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {
        "is_even.py",
        "fizzbuzz.py",
        "assignment.py",
        "collatz_print.py",
    }


def test_include_taxons():

    # The taxon "variable/assignment/single" is featured by assignment.py and collatz_print.py. In
    # collatz_print.py, it appears after a taxon "io/standard/print". Consequently, it should be included
    # in the results, but not the programs which import it: fizzbuzz.py and is_even.py.
    dbf = ProgramFilter(db)
    dbf.include_taxons({("variable/assignment/single", "after", "io/standard/print")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py"}

    # "operator/arithmetic/modulo" and "type/number/integer/literal" are both featured on
    # the same line in all programs except assignment.py
    dbf = ProgramFilter(db)
    dbf.include_taxons({("operator/arithmetic/modulo", "equals", "type/number/integer/literal")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "is_even.py", "fizzbuzz.py"}

    # The same with "x == y" instead of "equals"
    dbf = ProgramFilter(db)
    dbf.include_taxons({("operator/arithmetic/modulo", "equals", "type/number/integer/literal")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "is_even.py", "fizzbuzz.py"}

    # "test/equality" is inside "subroutine/function" in is_even.py, which is not imported anywhere.
    dbf = ProgramFilter(db)
    dbf.include_taxons({("test/equality", "inside", "subroutine/function")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"is_even.py"}

    # "test/equality" is inside "subroutine/function" in is_even.py and inside
    # "subroutine/procedure" in collatz_print.py. Both will be included.
    dbf = ProgramFilter(db)
    taxons = dbf.preprocess_taxons([("test/equality", "inside", "subroutine/.*")])
    print(taxons)
    assert taxons == [
        ("test/equality", "inside", "subroutine/argument/arg"),
        ("test/equality", "inside", "subroutine/function"),
        ("test/equality", "inside", "subroutine/predicate"),
        ("test/equality", "inside", "subroutine/procedure"),
    ]
    dbf.include_taxons(taxons)
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "is_even.py"}

    # "call/function/builtin/range" is not inside "flow/conditional" anywhere.
    dbf = ProgramFilter(db)
    dbf.include_taxons([("call/function/builtin/range", "inside", "flow/conditional")])
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == set()

    # "type/number/integer/literal" appears twice on the same line in fizzbuzz.py and
    # collatz_print.py
    dbf = ProgramFilter(db)
    dbf.include_taxons([("type/number/integer/literal", "is", "type/number/integer/literal")])
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"fizzbuzz.py", "collatz_print.py"}

    # "call/function/builtin/print" may appear several times in the same program, but never
    # on the same line.
    dbf = ProgramFilter(db)
    dbf.include_taxons([("call/function/builtin/print", "is", "call/function/builtin/print")])
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == set()


def test_impart_taxons():

    # Imparting a triple doesn't make much sense. Currently, it comes down to imparting the two
    # taxons, and ignoring the predicate.
    dbf = ProgramFilter(db)
    dbf.impart_taxons({("operator/arithmetic/modulo", "equals", "type/number/integer")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {
        "assignment.py",
        "collatz_print.py",
        "fizzbuzz.py",
        "is_even.py",
    }
    print(dbf.imparted_knowledge)
    assert dbf.imparted_knowledge == {
        "operator",
        "operator/arithmetic",
        "operator/arithmetic/modulo",
        "type",
        "type/number",
        "type/number/integer",
    }


def test_negate_triple():
    # "io/standard/print" and "flow/loop/exit/late" are both featured by collatz_print.py and
    # fizzbuzz.py. In collatz_print.py the print statements are both inside and outside the loop,
    # but in fizzbuzz.py, all print statement are inside the loop. Consequently, the unique print
    # statement not inside a loop is featured by collatz_print.py only. Note that assignment.py
    # and is_even.py are not included in the result, since they don't feature (at least directly)
    # the two taxons.
    dbf = ProgramFilter(db)
    dbf.include_taxons({("io/standard/print", "not inside", "flow/loop/exit/late")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py"}
    # For the excluding filter, as usual, the importations are taken into account. collatz_print.py
    # is excluded for featuring a print statement inside a loop, and fizzbuzz.py and is_even.py are
    # excluded for importing collatz_print.py. The only remaining program is assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({("io/standard/print", "not inside", "flow/loop/exit/late")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}
    # The not operator can appear anywhere, even if it's not syntactically correct.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({("io/standard/print", "inside not", "flow/loop/exit/late")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}
    # It can be replaced by a "!" symbol, and of course the other normalization rules still apply.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({("io/standard/print", "!(y1 ≤ x1 ≤ x2 ≤ y1)", "flow/loop/exit/late")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}


def test_negate_taxon():
    # Keep all programs which feature a subroutine definition (i.e., collatz_print.py and
    # is_even.py) or no assignment (i.e., fizzbuzz.py and is_even.py). The result is the union of
    # these sets.
    dbf = ProgramFilter(db)
    dbf.include_taxons(
        ["subroutine/function", "subroutine/procedure", "!variable/assignment/single"]
    )
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "is_even.py", "fizzbuzz.py"}
    # Negating a taxon dont't make previously excluded programs reenter in the result
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"is_even.py"})
    dbf.include_taxons(
        ["subroutine/function", "subroutine/procedure", "!variable/assignment/single"]
    )
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "fizzbuzz.py"}


if __name__ == "__main__":
    pytest.main(["-qq", "tests/test_filter_programs_with_triples.py"])
