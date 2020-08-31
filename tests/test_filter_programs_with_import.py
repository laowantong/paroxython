import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter


db = json.loads(Path("examples/mini/programs_db.json").read_text())


def test_init():
    dbf = ProgramFilter(db)
    print(dbf.selected_programs)
    assert dbf.selected_programs == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }


def test_taxa_of_programs():
    dbf = ProgramFilter(db)
    # collatz is imported by fizzbuzz
    subset_taxa = dbf.taxa_of_programs({"collatz.py"}, follow=False)
    subset_taxa = set(filter(lambda x: not x.startswith("meta/"), subset_taxa))
    print(sorted(subset_taxa))
    print()
    # when following the importations...
    superset_taxa = dbf.taxa_of_programs({"fizzbuzz.py"}, follow=True)
    superset_taxa = set(filter(lambda x: not x.startswith("meta/"), superset_taxa))
    print(sorted(superset_taxa))
    # in addition to its own taxa, fizzbuzz features all those of collatz...
    assert superset_taxa.issuperset(subset_taxa)
    assert len(superset_taxa - subset_taxa) > 0
    # when not following the importations...
    own_taxa = dbf.taxa_of_programs({"fizzbuzz.py"}, follow=False)
    own_taxa = set(filter(lambda x: not x.startswith("meta/"), own_taxa))
    print(sorted(own_taxa))
    assert superset_taxa.issuperset(own_taxa)
    assert len(superset_taxa - own_taxa) > 0


def test_programs_of_taxa():
    dbf = ProgramFilter(db)
    taxa = {"var/assignment/explicit/single"}

    # The taxon "var/assignment/explicit/single" is featured by assignment.py and collatz.py.
    # This corresponds to follow=False. It is indirectly featured by fizzbuzz.py (which imports
    # collatz.py) and by is_even.py (which imports fizzbuzz.py). Their addition corresponds
    # to follow=True.

    programs = dbf.programs_of_taxa(taxa)
    print(set(programs))
    assert set(programs) == {"assignment.py", "collatz.py"}

    programs = dbf.programs_of_taxa(taxa, follow=True)
    print(set(programs))
    assert set(programs) == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }


def test_exclude_taxa():

    # The taxon "var/assignment/explicit/single" is featured by assignment.py and collatz.py. It
    # is indirectly featured by fizzbuzz.py (which imports collatz.py) and by is_even.py
    # (which imports fizzbuzz.py). Therefore, excluding this taxon excludes all four programs.
    dbf = ProgramFilter(db)
    dbf.exclude_programs(dbf.programs_of_taxa({"var/assignment/explicit/single"}), follow=True)
    print(dbf.selected_programs)
    assert dbf.selected_programs == set()

    # "operator/arithmetic/addition" is featured by collatz.py, and indirectly by fizzbuzz.py
    # and is_even.py. Therefore, excluding this taxon keeps only assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_programs(dbf.programs_of_taxa({"call/subroutine/builtin/print"}), follow=True)
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"assignment.py"}

    # "flow/conditional" is featured by collatz.py, fizzbuzz.py, and indirectly by
    # is_even.py. Therefore, excluding this taxon keeps only assignment.py.
    dbf = ProgramFilter(db)
    dbf.exclude_programs(dbf.programs_of_taxa({"flow/conditional"}), follow=True)
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"assignment.py"}

    # "type/sequence/string/literal" is featured by fizzbuzz.py, and indirectly by is_even.py.
    # Therefore, excluding this taxon keeps only assignment.py and collatz.py
    dbf = ProgramFilter(db)
    dbf.exclude_programs(dbf.programs_of_taxa({"type/sequence/string/literal"}), follow=True)
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"assignment.py", "collatz.py"}


def test_include_taxa():

    # The taxon "var/assignment/explicit/single" is directly featured by assignment.py and
    # collatz.py, but only indirectly by the other programs, which therefore cannot be
    # included in the result. Note that this behavior contrasts with that of exclude_taxa.
    dbf = ProgramFilter(db)
    dbf.include_programs(dbf.programs_of_taxa({"var/assignment/explicit/single"}))
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"assignment.py", "collatz.py"}

    # "operator/arithmetic/addition" is directly featured by collatz.py only. Therefore,
    # including this taxon keeps only collatz.py.
    dbf = ProgramFilter(db)
    dbf.include_programs(dbf.programs_of_taxa({"operator/arithmetic/addition"}))
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"collatz.py"}

    # "flow/conditional" is featured by collatz.py, fizzbuzz.py, and indirectly by
    # is_even.py. Therefore, including this taxon keeps only the former two.
    dbf = ProgramFilter(db)
    dbf.include_programs(dbf.programs_of_taxa({"flow/conditional"}))
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"collatz.py", "fizzbuzz.py"}

    # "type/sequence/string/literal" is directly featured by fizzbuzz.py only. Therefore, including
    # this taxon keeps only fizzbuzz.py
    dbf = ProgramFilter(db)
    dbf.include_programs(dbf.programs_of_taxa({"type/sequence/string/literal"}))
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"fizzbuzz.py"}


def test_impart_taxa():

    # Imparting a knowledge decreases the learning cost of the corresponding taxa, but has no
    # effect whatsoever on the selected programs.
    dbf = ProgramFilter(db)
    dbf.impart_taxa({"flow/conditional"})
    print(dbf.selected_programs)
    assert dbf.selected_programs == {
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
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"assignment.py"}

    # The program fizzbuzz.py is imported by is_even.py. Excluding the former excludes both.
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"fizzbuzz.py"}, follow=True)
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"assignment.py", "collatz.py"}

    # The program is_even.py is not imported. Excluding it has no other effect on the selection.
    dbf = ProgramFilter(db)
    dbf.exclude_programs({"is_even.py"}, follow=True)
    print(dbf.selected_programs)
    assert dbf.selected_programs == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
    }


def test_include_programs():

    # The program collatz.py is self-contained. Including it has no other effect on the
    # selection.
    dbf = ProgramFilter(db)
    dbf.include_programs({"collatz.py"})
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"collatz.py"}

    # Including a program does not include the programs it imports.
    dbf = ProgramFilter(db)
    dbf.include_programs({"fizzbuzz.py"})
    print(dbf.selected_programs)
    assert dbf.selected_programs == {"fizzbuzz.py"}


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
