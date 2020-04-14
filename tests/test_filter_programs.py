import json
from pathlib import Path

import pytest

import context
from paroxython.filter_programs import ProgramFilter, depths_to_cost_length, depths_to_cost_zeno


def test_depths_to_cost_zeno():
    assert depths_to_cost_zeno(0, 0) == 0
    assert depths_to_cost_zeno(42, 42) == 0
    assert depths_to_cost_zeno(0, 1) == 1 / 2
    assert depths_to_cost_zeno(0, 2) == 1 / 2 + 1 / 4
    assert depths_to_cost_zeno(0, 3) == 1 / 2 + 1 / 4 + 1 / 8
    assert depths_to_cost_zeno(1, 4) == 1 / 4 + 1 / 8 + 1 / 16


def test_depths_to_cost_length():
    assert depths_to_cost_length(3, 5) == 2


db = json.loads(Path("tests/data/dummy_db.json").read_text())


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


def test_compute_taxon_cost_with_length_strategy():
    dbf = ProgramFilter(db)
    dbf.imparted_knowledge = {"O", "O/J", "X", "X/S", "X/S/M", "X/S/M/L"}
    dbf.set_cost_computation_strategy("length")
    taxon_costs = {taxon: dbf.compute_taxon_cost(taxon) for taxon in db["taxons"]}
    print(taxon_costs)
    assert taxon_costs == {
        "O": 0.0,
        "O/C": 1.0,
        "O/C/F": 2.0,
        "O/C/F/U": 3.0,
        "O/C/H": 2.0,
        "O/C/H/B": 3.0,
        "O/C/H/B/I": 4.0,
        "O/J": 0.0,
        "O/N": 1.0,
        "O/N/P": 2.0,
        "X": 0.0,
        "X/G": 1.0,
        "X/K": 1.0,
        "X/S": 0.0,
        "X/S/M": 0.0,
        "X/S/M/L": 0.0,
        "X/S/M/L/R": 1.0,
        "X/S/M/L/R/D": 2.0,
        "X/S/M/L/R/D/A": 3.0,
        "X/S/M/L/V": 1.0,
        "X/W": 1.0,
        "Y": 1.0,
        "Y/E": 2.0,
        "Y/T": 2.0,
        "Y/T/Q": 3.0,
    }


def test_compute_taxon_cost_with_zeno_strategy():
    dbf = ProgramFilter(db)
    dbf.imparted_knowledge = {"O", "O/J", "X", "X/S", "X/S/M", "X/S/M/L"}
    dbf.set_cost_computation_strategy("zeno")
    taxon_costs = {taxon: dbf.compute_taxon_cost(taxon) for taxon in db["taxons"]}
    print(taxon_costs)
    assert taxon_costs == {
        "O": 0,
        "O/C": 0.25,
        "O/C/F": 0.375,
        "O/C/F/U": 0.4375,
        "O/C/H": 0.375,
        "O/C/H/B": 0.4375,
        "O/C/H/B/I": 0.46875,
        "O/J": 0,
        "O/N": 0.25,
        "O/N/P": 0.375,
        "X": 0,
        "X/G": 0.25,
        "X/K": 0.25,
        "X/S": 0,
        "X/S/M": 0,
        "X/S/M/L": 0,
        "X/S/M/L/R": 0.03125,
        "X/S/M/L/R/D": 0.046875,
        "X/S/M/L/R/D/A": 0.0546875,
        "X/S/M/L/V": 0.03125,
        "X/W": 0.25,
        "Y": 0.5,
        "Y/E": 0.75,
        "Y/T": 0.75,
        "Y/T/Q": 0.875,
    }


def test_get_sorted_recommandations():
    dbf = ProgramFilter(db)
    programs = ["prg1.py", "prg2.py", "non_existing_program"]
    dbf.impart_programs(programs)
    dbf.set_cost_computation_strategy("zeno")
    sorted_recommendations = dbf.get_sorted_recommendations()
    print(sorted_recommendations)
    assert sorted_recommendations == [
        (0.1328125, "prg5.py"),
        (0.1953125, "prg4.py"),
        (0.375, "prg9.py"),
        (0.4375, "prg3.py"),
        (0.4375, "prg7.py"),
        (0.4453125, "prg8.py"),
        (0.5703125, "prg6.py"),
    ]


def test_get_markdown():
    dbf = ProgramFilter(db)
    programs = ["prg1.py", "prg2.py", "non_existing_program"]
    dbf.impart_programs(programs)
    dbf.set_cost_computation_strategy("length")
    text = dbf.get_markdown(section_group_limit=2)
    print(text)
    assert "2 programs of cost 2" in text
    assert "3 programs of cost 3" in text
    assert "9 programs initially" in text
    assert "7 programs remaining" in text
