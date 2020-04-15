import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter, depths_to_cost_length, depths_to_cost_zeno


def test_depths_to_cost_zeno():
    assert depths_to_cost_zeno(0, 0) == 0
    assert depths_to_cost_zeno(42, 42) == 0
    assert depths_to_cost_zeno(0, 1) == int(1024 * (1 / 2))
    assert depths_to_cost_zeno(0, 2) == int(1024 * (1 / 2 + 1 / 4))
    assert depths_to_cost_zeno(0, 3) == int(1024 * (1 / 2 + 1 / 4 + 1 / 8))
    assert depths_to_cost_zeno(1, 4) == int(1024 * (1 / 4 + 1 / 8 + 1 / 16))


def test_depths_to_cost_length():
    assert depths_to_cost_length(3, 5) == 2000


db = json.loads(Path("tests/data/dummy/db.json").read_text())


def test_init():
    dbf = ProgramFilter(db)
    print(dbf.recommended_programs)
    assert dbf.recommended_programs == set(db["programs"])
    assert not dbf.imparted_knowledge


def test_programs_of_taxons():
    dbf = ProgramFilter(db)
    taxons = {"X/S/M/L/R/D/A", "X/S/M/L/R/D", "non_existing_taxon"}
    programs = dbf.programs_of_taxons(taxons)
    print(sorted(programs))
    for (db_program, db_program_data) in db["programs"].items():
        if taxons.intersection(db_program_data["taxons"]):
            assert db_program in programs
        else:
            assert db_program not in programs


def test_taxons_of_program():
    dbf = ProgramFilter(db)
    program = "prg8.py"
    taxons = dbf.taxons_of_program(program)
    print(sorted(taxons))
    assert taxons == set(db["programs"][program]["taxons"])
    program = "non_existing_program"
    taxons = dbf.taxons_of_program(program)
    print(sorted(taxons))
    assert taxons == set()


def test_taxons_of_programs():
    dbf = ProgramFilter(db)
    programs = ["prg8.py", "prg9.py", "non_existing_program"]
    taxons = dbf.taxons_of_programs(programs)
    prg8_taxons = dbf.taxons_of_program("prg8.py")
    prg9_taxons = dbf.taxons_of_program("prg9.py")
    print(sorted(taxons))
    assert taxons == prg8_taxons | prg9_taxons


def test_patterns_to_taxons():
    dbf = ProgramFilter(db)
    patterns = ["X/S/M.*", "O(?!/C).*", "non_matching_pattern"]
    taxons = dbf.patterns_to_taxons(patterns)
    print(sorted(taxons))
    assert taxons == {
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
    }


def test_impart_taxons():
    dbf = ProgramFilter(db)
    taxons = ["O/J", "X/S/M/L", "non_existing_taxon"]
    dbf.impart_taxons(taxons)
    print(sorted(dbf.imparted_knowledge))
    assert dbf.imparted_knowledge == {"O", "O/J", "X", "X/S", "X/S/M", "X/S/M/L"}


def test_exclude_taxons():
    dbf = ProgramFilter(db)
    taxons = ["O/J", "X/S/M/L", "non_existing_taxon"]
    dbf.exclude_taxons(taxons)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs == {"prg2.py", "prg5.py"}
    for taxon in taxons:
        assert taxon not in db["programs"]["prg2.py"]["taxons"]
        assert taxon not in db["programs"]["prg5.py"]["taxons"]


def test_include_taxons():
    dbf = ProgramFilter(db)
    taxons = ["O/J", "X/S/M/L", "non_existing_taxon"]
    dbf.include_taxons(taxons)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs == {
        "prg1.py",
        "prg3.py",
        "prg4.py",
        "prg6.py",
        "prg7.py",
        "prg8.py",
        "prg9.py",
    }


def test_patterns_to_programs():
    dbf = ProgramFilter(db)
    patterns = ["prg[1-3]", "prg[7-9]", "non_matching_pattern"]
    programs = dbf.patterns_to_programs(patterns)
    print(sorted(programs))
    assert programs == {"prg1.py", "prg2.py", "prg3.py", "prg7.py", "prg8.py", "prg9.py"}


def test_impart_programs():
    dbf = ProgramFilter(db)
    programs = ["prg1.py", "prg2.py", "non_existing_program"]
    dbf.impart_programs(programs)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs == set(db["programs"]) - set(programs)
    print(sorted(dbf.imparted_knowledge))
    assert set(db["taxons"]) - dbf.imparted_knowledge == {
        "O/C/F",
        "O/C/F/U",
        "X/S/M/L/R/D/A",
        "Y/E",
    }


def test_exclude_programs():
    dbf = ProgramFilter(db)
    programs = ["prg1.py", "prg2.py", "non_existing_program"]
    dbf.exclude_programs(programs)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs == set(db["programs"]) - set(programs)


def test_include_programs():
    dbf = ProgramFilter(db)
    programs = ["prg1.py", "prg2.py", "non_existing_program"]
    dbf.include_programs(programs)
    print(sorted(dbf.recommended_programs))
    assert dbf.recommended_programs == {"prg1.py", "prg2.py"}


def test_compute_taxon_cost():
    dbf = ProgramFilter(db)
    dbf.imparted_knowledge = {"O", "O/J", "X", "X/S", "X/S/M", "X/S/M/L"}
    dbf.set_cost_computation_strategy("length")
    taxon_costs = {taxon: dbf.compute_taxon_cost(taxon) for taxon in db["taxons"]}
    print(taxon_costs)
    assert taxon_costs == {
        "O": 0000,
        "O/C": 1000,
        "O/C/F": 2000,
        "O/C/F/U": 3000,
        "O/C/H": 2000,
        "O/C/H/B": 3000,
        "O/C/H/B/I": 4000,
        "O/J": 0000,
        "O/N": 1000,
        "O/N/P": 2000,
        "X": 0000,
        "X/G": 1000,
        "X/K": 1000,
        "X/S": 0000,
        "X/S/M": 0000,
        "X/S/M/L": 0000,
        "X/S/M/L/R": 1000,
        "X/S/M/L/R/D": 2000,
        "X/S/M/L/R/D/A": 3000,
        "X/S/M/L/V": 1000,
        "X/W": 1000,
        "Y": 1000,
        "Y/E": 2000,
        "Y/T": 2000,
        "Y/T/Q": 3000,
    }


def test_get_sorted_recommandations():
    dbf = ProgramFilter(db)
    programs = ["prg1.py", "prg2.py", "non_existing_program"]
    dbf.impart_programs(programs)
    dbf.set_cost_computation_strategy("zeno")
    sorted_recommendations = dbf.get_sorted_recommendations()
    print(sorted_recommendations)
    assert sorted_recommendations == [
        (136, "prg5.py"),
        (200, "prg4.py"),
        (384, "prg9.py"),
        (448, "prg3.py"),
        (448, "prg7.py"),
        (456, "prg8.py"),
        (584, "prg6.py"),
    ]


def test_get_markdown():
    dbf = ProgramFilter(db)
    programs = ["prg1.py", "prg2.py", "non_existing_program"]
    dbf.impart_programs(programs)
    dbf.set_cost_computation_strategy("length")
    text = dbf.get_markdown(section_group_limit=2)
    print(text)
    assert "2 programs of learning cost 2000" in text
    assert "3 programs of learning cost 3000" in text
    assert "9 programs initially" in text
    assert "7 programs remaining" in text
