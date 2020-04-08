import json
from pathlib import Path

import pytest

import context
from suggest_programs import ProgramProcessor, compute_taxon_cost_zeno, compute_taxon_cost_length
from paroxython.make_db import Database


def test_run():
    db = json.loads(Path("snapshots/simple_db.json").read_text())
    pp = ProgramProcessor(db)
    syllabus = """
    January :
        + assignment.py
        + unknown_program.py
    February :
        + [mandatory] is_even.py
    # EOF: no program below is studied yet
    March :
        either + collatz_print.py or + fizzbuzz.py
    """

    pp.init_old_programs(syllabus, "tests/data/simple/")
    print("\n".join(sorted(pp.old_program_names)))
    print()
    assert pp.old_program_names == {
        "tests/data/simple/assignment.py",
        "tests/data/simple/is_even.py",
    }

    pp.init_old_taxons()
    print("\n".join(sorted(pp.old_taxons)))
    print()
    assert pp.old_taxons.__contains__("variable")
    assert pp.old_taxons.__contains__("variable/assignment")
    assert pp.old_taxons.__contains__("variable/assignment/single")
    assert not pp.old_taxons.__contains__("variable/assignment/conditional")

    for taxon_name in sorted(db["taxons"]):
        taxon_cost = pp.compute_taxon_depth_range(taxon_name)
        print(taxon_cost, taxon_name)

    assert (2, 4) == pp.compute_taxon_depth_range("variable/assignment/conditional/verbose")
    assert (2, 3) == pp.compute_taxon_depth_range("variable/assignment/conditional")
    assert (0, 0) == pp.compute_taxon_depth_range("variable/assignment")  # already known
    assert (0, 0) == pp.compute_taxon_depth_range("variable")  # already known
    assert (0, 4) == pp.compute_taxon_depth_range("foo/bar/bizz/buzz")  # all segments are new


def test_compute_taxon_cost_length():
    assert compute_taxon_cost_length(3, 5) == 2


def test_compute_taxon_cost_zeno():
    assert compute_taxon_cost_zeno(0, 0) == 0
    assert compute_taxon_cost_zeno(42, 42) == 0
    assert compute_taxon_cost_zeno(0, 1) == 1 / 2
    assert compute_taxon_cost_zeno(0, 2) == 1 / 2 + 1 / 4
    assert compute_taxon_cost_zeno(0, 3) == 1 / 2 + 1 / 4 + 1 / 8
    assert compute_taxon_cost_zeno(1, 4) == 1 / 4 + 1 / 8 + 1 / 16
