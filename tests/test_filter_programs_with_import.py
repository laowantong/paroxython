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
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }


def test_taxons_of_programs():
    dbf = ProgramFilter(db)
    # collatz is imported by fizzbuzz
    subset_taxons = dbf.taxons_of_programs({"collatz.py"}, follow=False)
    subset_taxons = set(filter(lambda x: not x.startswith("metadata/"), subset_taxons))
    print(sorted(subset_taxons))
    print()
    # when following the importations...
    superset_taxons = dbf.taxons_of_programs({"fizzbuzz.py"}, follow=True)
    superset_taxons = set(filter(lambda x: not x.startswith("metadata/"), superset_taxons))
    print(sorted(superset_taxons))
    # in addition to its own taxons, fizzbuzz features all those of collatz...
    assert superset_taxons.issuperset(subset_taxons)
    assert len(superset_taxons - subset_taxons) > 0
    # when not following the importations...
    own_taxons = dbf.taxons_of_programs({"fizzbuzz.py"}, follow=False)
    own_taxons = set(filter(lambda x: not x.startswith("metadata/"), own_taxons))
    print(sorted(own_taxons))
    assert superset_taxons.issuperset(own_taxons)
    assert len(superset_taxons - own_taxons) > 0


def test_programs_of_taxons():
    dbf = ProgramFilter(db)
    taxons = {"variable/assignment/single"}

    # The taxon "variable/assignment/single" is featured by assignment.py and collatz.py.
    # This corresponds to follow=False. It is indirectly featured by fizzbuzz.py (which imports
    # collatz.py) and by is_even.py (which imports fizzbuzz.py). Their addition corresponds
    # to follow=True.

    programs = dbf.programs_of_taxons(taxons)
    print(set(programs))
    assert set(programs) == {"assignment.py", "collatz.py"}

    programs = dbf.programs_of_taxons(taxons, follow=True)
    print(set(programs))
    assert set(programs) == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }


def test_exclude_taxons():

    # The taxon "variable/assignment/single" is featured by assignment.py and collatz.py. It
    # is indirectly featured by fizzbuzz.py (which imports collatz.py) and by is_even.py
    # (which imports fizzbuzz.py). Therefore, excluding this taxon excludes all four programs.
    dbf = ProgramFilter(db)
    dbf.exclude_programs(dbf.programs_of_taxons({"variable/assignment/single"}), follow=True)
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == set()

    # "operator/arithmetic/addition" is featured by collatz.py, and indirectly by fizzbuzz.py
    # and is_even.py. Therefore, excluding this taxon keeps only assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_programs(dbf.programs_of_taxons({"io/standard/print"}), follow=True)
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # "flow/conditional" is featured by collatz.py, fizzbuzz.py, and indirectly by
    # is_even.py. Therefore, excluding this taxon keeps only assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_programs(dbf.programs_of_taxons({"flow/conditional"}), follow=True)
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # "type/sequence/string/literal" is featured by fizzbuzz.py, and indirectly by is_even.py.
    # Therefore, excluding this taxon keeps only assignment.py and collatz.py
    dbf = ProgramFilter(db)
    dbf.exclude_programs(dbf.programs_of_taxons({"type/sequence/string/literal"}), follow=True)
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py", "collatz.py"}


def test_include_taxons():

    # The taxon "variable/assignment/single" is directly featured by assignment.py and
    # collatz.py, but only indirectly by the other programs, which therefore cannot be
    # included in the result. Note that this behavior contrasts with that of exclude_taxons.
    dbf = ProgramFilter(db)
    dbf.include_programs(dbf.programs_of_taxons({"variable/assignment/single"}))
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py", "collatz.py"}

    # "operator/arithmetic/addition" is directly featured by collatz.py only. Therefore,
    # including this taxon keeps only collatz.py.
    dbf = ProgramFilter(db)
    dbf.include_programs(dbf.programs_of_taxons({"operator/arithmetic/addition"}))
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz.py"}

    # "flow/conditional" is featured by collatz.py, fizzbuzz.py, and indirectly by
    # is_even.py. Therefore, including this taxon keeps only the former two.
    dbf = ProgramFilter(db)
    dbf.include_programs(dbf.programs_of_taxons({"flow/conditional"}))
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz.py", "fizzbuzz.py"}

    # "type/sequence/string/literal" is directly featured by fizzbuzz.py only. Therefore, including
    # this taxon keeps only fizzbuzz.py
    dbf = ProgramFilter(db)
    dbf.include_programs(dbf.programs_of_taxons({"type/sequence/string/literal"}))
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
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }


def test_exclude_programs():

    # The program collatz.py is imported by fizzbuzz.py, and indirectly by is_even.py.
    # Excluding the former excludes the two latter too.
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"collatz.py"}, follow=True)
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py"}

    # The program fizzbuzz.py is imported by is_even.py. Excluding the former excludes both.
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"fizzbuzz.py"}, follow=True)
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"assignment.py", "collatz.py"}

    # The program is_even.py is not imported. Excluding it has no other effect on the selection.
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"is_even.py"}, follow=True)
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
    }


def test_include_programs():

    # The program collatz.py is self-contained. Including it has no other effect on the
    # selection.
    dbf = ProgramFilter(db)
    dbf.include_programs({"collatz.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"collatz.py"}

    # Including a program does not include the programs it imports.
    dbf = ProgramFilter(db)
    dbf.include_programs({"fizzbuzz.py"})
    print(set(dbf.selected_programs.keys()))
    assert set(dbf.selected_programs.keys()) == {"fizzbuzz.py"}


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
