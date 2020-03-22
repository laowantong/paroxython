import json
from pathlib import Path

import pytest

import context
from suggest_programs import ProgramProcessor
from paroxython.make_db import Database


def test_run():
    db = json.loads(Path("snapshots/simple_db.json").read_text())
    pp = ProgramProcessor(db)
    syllabus = """
    January :
        + assignment.py
        + unknown_program.py
    February :
        + is_even.py
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
        taxon_cost = pp.calculate_taxon_cost(taxon_name)
        print(taxon_cost, taxon_name)
    assert 2 == pp.calculate_taxon_cost("variable/assignment/conditional/verbose/")
    assert 1 == pp.calculate_taxon_cost("variable/assignment/conditional/")
    assert 0 == pp.calculate_taxon_cost("variable/assignment/")
    assert 0 == pp.calculate_taxon_cost("variable/")
