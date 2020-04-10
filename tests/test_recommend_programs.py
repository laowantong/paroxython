import json
from pathlib import Path

import pytest

import context
from make_db import Database
from recommend_programs import (
    ProgramAdvisor,
    DatabaseFilter,
    depths_to_cost_length,
    depths_to_cost_zeno,
    get_prefixes_of_taxon_names,
    get_studied_programs_from_syllabus,
)


def test_depths_to_cost_length():
    assert depths_to_cost_length(3, 5) == 2


def test_depths_to_cost_zeno():
    assert depths_to_cost_zeno(0, 0) == 0
    assert depths_to_cost_zeno(42, 42) == 0
    assert depths_to_cost_zeno(0, 1) == 1 / 2
    assert depths_to_cost_zeno(0, 2) == 1 / 2 + 1 / 4
    assert depths_to_cost_zeno(0, 3) == 1 / 2 + 1 / 4 + 1 / 8
    assert depths_to_cost_zeno(1, 4) == 1 / 4 + 1 / 8 + 1 / 16


SYLLABUS = """
January :
    + assignment.py
    + unknown_program.py
February :
    + [mandatory] is_even.py
# EOF: no program below is studied yet
March :
    either + collatz_print.py or + fizzbuzz.py
"""
PATH_PREFIX = "tests/data/simple/"


def test_get_studied_programs_from_syllabus():
    result = get_studied_programs_from_syllabus(SYLLABUS, PATH_PREFIX)
    print(result)
    assert result == {
        "tests/data/simple/assignment.py",
        "tests/data/simple/unknown_program.py",
        "tests/data/simple/is_even.py",
    }


DB = json.loads(Path("snapshots/simple_db.json").read_text())


def test_run():
    advisor = ProgramAdvisor(DatabaseFilter(DB))

    advisor.init_old_programs(syllabus=SYLLABUS, path_prefix=PATH_PREFIX)
    print("\n".join(sorted(advisor.old_program_names)))
    assert advisor.old_program_names == {
        "tests/data/simple/assignment.py",
        "tests/data/simple/is_even.py",
    }
    print("\n".join(sorted(advisor.old_taxon_names)))
    print()
    assert advisor.old_taxon_names.__contains__("variable")
    assert advisor.old_taxon_names.__contains__("variable/assignment")
    assert advisor.old_taxon_names.__contains__("variable/assignment/single")
    assert not advisor.old_taxon_names.__contains__("variable/assignment/conditional")

    advisor.set_cost_computation_strategy("zeno")

    assert advisor.compute_taxon_cost("variable/assignment/conditional/verbose") == 1 / 8 + 1 / 16
    assert advisor.compute_taxon_cost("variable/assignment/conditional") == 1 / 8
    assert advisor.compute_taxon_cost("variable/assignment") == 0
    assert advisor.compute_taxon_cost("variable") == 0
    assert advisor.compute_taxon_cost("foo/bar/bizz/buzz") == 1 / 2 + 1 / 4 + 1 / 8 + 1 / 16

    assert advisor.compute_program_cost("tests/data/simple/collatz_print.py") == 4.4375

    advisor.set_cost_computation_strategy("length")

    assert advisor.compute_taxon_cost("variable/assignment/conditional/verbose") == 2
    assert advisor.compute_taxon_cost("variable/assignment/conditional") == 1
    assert advisor.compute_taxon_cost("variable/assignment") == 0
    assert advisor.compute_taxon_cost("variable") == 0
    assert advisor.compute_taxon_cost("foo/bar/bizz/buzz") == 4

    assert advisor.compute_program_cost("tests/data/simple/collatz_print.py") == 17

    recommendations = advisor.get_recommendations()
    print(recommendations)
    assert "4 programs initially" in recommendations
    assert "2 programs remaining" in recommendations
