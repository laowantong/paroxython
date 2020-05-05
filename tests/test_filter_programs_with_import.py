import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter


db = json.loads(Path("tests/snapshots/simple_db.json").read_text())


def test_init():
    dbf = ProgramFilter(db)
    print(dbf.selected_programs)
    assert set(dbf.selected_programs.keys()) == {
        "assignment.py",
        "collatz_print.py",
        "fizzbuzz.py",
        "is_even.py",
    }


def test_programs_of_taxons():
    dbf = ProgramFilter(db)
    taxons = {"variable/assignment/single"}

    # The taxon "variable/assignment/single" is featured by assignment.py and collatz_print.py.
    # This corresponds to follow=False. It is indirectly featured by fizzbuzz.py (which imports
    # collatz_print.py) and by is_even.py (which imports fizzbuzz.py). Their addition corresponds
    # to follow=True.

    programs = dbf.programs_of_taxons(taxons, follow=False)
    print(set(programs))
    assert set(programs) == {"assignment.py", "collatz_print.py"}

    programs = dbf.programs_of_taxons(taxons, follow=True)
    print(set(programs))
    assert set(programs) == {
        "assignment.py",
        "collatz_print.py",
        "fizzbuzz.py",
        "is_even.py",
    }


def test_exclude_taxons():

    # The taxon "variable/assignment/single" is featured by assignment.py and collatz_print.py. It
    # is indirectly featured by fizzbuzz.py (which imports collatz_print.py) and by is_even.py
    # (which imports fizzbuzz.py). Therefore, excluding this taxon excludes all four programs.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({"variable/assignment/single"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == set()

    # "operator/arithmetic/addition" is featured by collatz_print.py, and indirectly by fizzbuzz.py
    # and is_even.py. Therefore, excluding this taxon keeps only assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({"io/standard/print"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # "flow/conditional" is featured by collatz_print.py, fizzbuzz.py, and indirectly by
    # is_even.py. Therefore, excluding this taxon keeps only assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({"flow/conditional"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # "type/sequence/string/literal" is featured by fizzbuzz.py, and indirectly by is_even.py.
    # Therefore, excluding this taxon keeps only assignment.py and collatz_print.py
    dbf = ProgramFilter(db)
    dbf.exclude_taxons({"type/sequence/string/literal"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py", "collatz_print.py"}


def test_include_taxons():

    # The taxon "variable/assignment/single" is directly featured by assignment.py and
    # collatz_print.py, but only indirectly by the other programs, which therefore cannot be
    # included in the result. Note that this behavior contrasts with that of exclude_taxons.
    dbf = ProgramFilter(db)
    dbf.include_taxons({"variable/assignment/single"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py", "collatz_print.py"}

    # "operator/arithmetic/addition" is directly featured by collatz_print.py only. Therefore,
    # including this taxon keeps only collatz_print.py.
    dbf = ProgramFilter(db)
    dbf.include_taxons({"operator/arithmetic/addition"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py"}

    # "flow/conditional" is featured by collatz_print.py, fizzbuzz.py, and indirectly by
    # is_even.py. Therefore, including this taxon keeps only the former two.
    dbf = ProgramFilter(db)
    dbf.include_taxons({"flow/conditional"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py", "fizzbuzz.py"}

    # "type/sequence/string/literal" is directly featured by fizzbuzz.py only. Therefore, including
    # this taxon keeps only fizzbuzz.py
    dbf = ProgramFilter(db)
    dbf.include_taxons({"type/sequence/string/literal"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"fizzbuzz.py"}


def test_impart_taxons():

    # Imparting a knowledge decreases the learning cost of the corresponding taxons, but has no
    # effect whatsoever on the selected programs.
    dbf = ProgramFilter(db)
    dbf.impart_taxons({"flow/conditional"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {
        "assignment.py",
        "collatz_print.py",
        "fizzbuzz.py",
        "is_even.py",
    }


def test_exclude_programs():

    # The program collatz_print.py is imported by fizzbuzz.py, and indirectly by is_even.py.
    # Excluding the former excludes the two latter too.
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"collatz_print.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # The program fizzbuzz.py is imported by is_even.py. Excluding the former excludes both.
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"fizzbuzz.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py", "collatz_print.py"}

    # The program is_even.py is not imported. Excluding it has no other effect on the selection.
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"is_even.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {
        "assignment.py",
        "collatz_print.py",
        "fizzbuzz.py",
    }


def test_include_programs():

    # The program collatz_print.py is self-contained. Including it has no other effect on the
    # selection.
    dbf = ProgramFilter(db)
    dbf.include_programs({"collatz_print.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz_print.py"}

    # The program fizzbuzz.py imports collatz_print.py. Including the former includes both.
    dbf = ProgramFilter(db)
    dbf.include_programs({"fizzbuzz.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"fizzbuzz.py", "collatz_print.py"}

    # The program is_even.py import collatz_print.py, which imports collatz_print.py. Including the
    # former includes the three of them.
    dbf = ProgramFilter(db)
    dbf.include_programs({"is_even.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {
        "is_even.py",
        "collatz_print.py",
        "fizzbuzz.py",
    }


def test_impart_programs():

    # The program collatz_print.py is self-contained. Imparting it excludes it from the selection,
    # but has no other effect.
    dbf = ProgramFilter(db)
    dbf.impart_programs({"collatz_print.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {
        "assignment.py",
        "fizzbuzz.py",
        "is_even.py",
    }

    # The program fizzbuzz.py imports collatz_print.py. Imparting the former implies that the
    # latter has already been studied, and must be excluded from the selection.
    dbf = ProgramFilter(db)
    dbf.impart_programs({"fizzbuzz.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py", "is_even.py"}

    # The program is_even.py imports collatz_print.py, which imports collatz_print.py. Imparting
    # the former excludes the three of them from the selection.
    dbf = ProgramFilter(db)
    dbf.impart_programs({"is_even.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
