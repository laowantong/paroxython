import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter


db = json.loads(Path("examples/dummy/programs_db.json").read_text())


def test_init():
    dbf = ProgramFilter(db)
    print(dbf.selected_programs)
    assert dbf.selected_programs == db["programs"].keys()
    assert not dbf.imparted_knowledge


def test_programs_of_taxa():
    dbf = ProgramFilter(db)
    taxa = {"X/S/M/L/R/D/A", "X/S/M/L/R/D", "non_existing_taxon"}
    programs = dbf.programs_of_taxa(taxa, follow=False)
    print(sorted(programs))
    for (db_program, db_program_data) in db["programs"].items():
        if taxa.intersection(db_program_data["taxa"]):
            assert db_program in programs
        else:
            assert db_program not in programs


def test_taxa_of_programs():
    dbf = ProgramFilter(db)
    programs = {"prg8.py", "prg9.py", "non_existing_program"}
    taxa = dbf.taxa_of_programs(programs)
    prg8_taxa = set(dbf.db_programs["prg8.py"]["taxa"])
    prg9_taxa = set(dbf.db_programs["prg9.py"]["taxa"])
    print(sorted(taxa))
    assert taxa == prg8_taxa | prg9_taxa


def test_taxa_of_pattern():
    dbf = ProgramFilter(db)
    names = ["X/S/M", "O(?!/C)", "Y/E$", "non_matching_pattern"]
    taxa = set().union(*(dbf.taxa_of_pattern(name) for name in names))
    print(sorted(taxa))
    assert sorted(taxa) == [
        "O",
        "O/J",
        "O/N",
        "O/N/P",
        "X/S/M",
        "X/S/M/L",
        "X/S/M/L/R",
        "X/S/M/L/R/D",
        "X/S/M/L/R/D/A",
        "X/S/M/L/V",
        "Y/E",
    ]


def test_impart_taxa():
    dbf = ProgramFilter(db)
    taxa = ["O/J", "X/S/M/L", "non/existing/taxon"]
    dbf.impart_taxa(taxa)
    print(sorted(dbf.imparted_knowledge))
    assert dbf.imparted_knowledge == {
        "O",
        "O/J",
        "X",
        "X/S",
        "X/S/M",
        "X/S/M/L",
        "non",
        "non/existing",
        "non/existing/taxon",
    }


def test_programs_of_pattern():
    dbf = ProgramFilter(db)
    names = [r"prg[1-3]\.py", r"prg[7-9]\.py", "non_matching_pattern"]
    programs = set().union(*(dbf.programs_of_pattern(name) for name in names))
    print(sorted(programs))
    assert sorted(programs) == ["prg1.py", "prg2.py", "prg3.py", "prg7.py", "prg8.py", "prg9.py"]


def test_exclude_programs():
    dbf = ProgramFilter(db)
    programs = {"prg1.py", "prg2.py", "non_existing_program"}
    dbf.exclude_programs(programs, follow=True)
    print(sorted(dbf.selected_programs))
    assert dbf.selected_programs == set(db["programs"]) - set(programs)


def test_include_programs():
    dbf = ProgramFilter(db)
    programs = {"prg1.py", "prg2.py", "non_existing_program"}
    dbf.include_programs(programs)
    print(sorted(dbf.selected_programs))
    assert dbf.selected_programs == {"prg1.py", "prg2.py"}


if __name__ == "__main__":
    pytest.main(["-qq", "tests/test_filter_programs.py"])
