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
    dbf.exclude_taxons({("after", "variable/assignment/single", "io/standard/print")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # "operator/arithmetic/addition" and "operator/arithmetic/multiplication" are both featured on
    # the same line of collatz_print.py, and indirectly by fizzbuzz.py and is_even.py. Therefore,
    # excluding this taxon keeps only assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons(
        {("equals", "operator/arithmetic/addition", "operator/arithmetic/multiplication")}
    )
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # "test/equality" is inside "subroutine/function" in is_even.py, which is not imported anywhere.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({("inside", "test/equality", "subroutine/function")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "assignment.py", "fizzbuzz.py"}

    # "call/function/builtin/range" is not inside "flow/conditional" anywhere.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons([("inside", "call/function/builtin/range", "flow/conditional")])
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
    dbf.include_taxons({("after", "variable/assignment/single", "io/standard/print")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py"}

    # "operator/arithmetic/modulo" and "type/number/integer/literal" are both featured on
    # the same line in all programs except assignment.py
    dbf = ProgramFilter(db)
    dbf.include_taxons({("equals", "operator/arithmetic/modulo", "type/number/integer/literal")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "is_even.py", "fizzbuzz.py"}

    # The same with "x == y" instead of "equals"
    dbf = ProgramFilter(db)
    dbf.include_taxons({("equals", "operator/arithmetic/modulo", "type/number/integer/literal")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "is_even.py", "fizzbuzz.py"}

    # "test/equality" is inside "subroutine/function" in is_even.py, which is not imported anywhere.
    dbf = ProgramFilter(db)
    dbf.include_taxons({("inside", "test/equality", "subroutine/function")})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"is_even.py"}

    # "test/equality" is inside "subroutine/function" in is_even.py and inside
    # "subroutine/procedure" in collatz_print.py. Both will be included.
    dbf = ProgramFilter(db)
    taxons = dbf.preprocess_taxons([("inside", "test/equality", "subroutine/.*")])
    print(taxons)
    assert taxons == [
        ("inside", "test/equality", "subroutine/argument/arg"),
        ("inside", "test/equality", "subroutine/function"),
        ("inside", "test/equality", "subroutine/predicate"),
        ("inside", "test/equality", "subroutine/procedure"),
    ]
    dbf.include_taxons(taxons)
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "is_even.py"}

    # "call/function/builtin/range" is not inside "flow/conditional" anywhere.
    dbf = ProgramFilter(db)
    dbf.include_taxons([("inside", "call/function/builtin/range", "flow/conditional")])
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == set()


def test_impart_taxons():

    # Imparting a triple doesn't make much sense. Currently, it comes down to imparting the two
    # taxons, and ignoring the predicate.
    dbf = ProgramFilter(db)
    dbf.impart_taxons({("equals", "operator/arithmetic/modulo", "type/number/integer")})
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


if __name__ == "__main__":
    pytest.main(["-qq", "tests/test_filter_programs_with_triples.py"])
