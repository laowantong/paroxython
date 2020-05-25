from typed_ast.ast3 import literal_eval
import json
from pathlib import Path

import pytest

import context
from make_snapshot import make_snapshot

from paroxython.recommend_programs import Recommendations


def test_recommend_program(capsys):
    rec = Recommendations(
        commands=literal_eval(Path("tests/data/dummy/pipe.py").read_text()),
        db=json.loads(Path("tests/data/dummy/db.json").read_text()),
        base_path=Path("tests/data/dummy/"),
    )
    rec.run_pipeline()
    print(rec.selected_programs)
    assert rec.selected_programs == {
        "prg2.py": [
            "O/N/P",
            "Y/T/Q",
            "Y",
            "X/S/M/L/R/D",
            "O",
            "O/C/H/B",
            "X/S/M",
            "X/S/M/L/R",
            "Y/T",
            "O/C",
            "X/G",
            "X/S/M/L/V",
            "O/C/H/B/I",
        ],
        "prg3.py": [
            "O/N/P",
            "X/K",
            "Y/T",
            "X/S/M/L/V",
            "O/C/H/B",
            "X/S/M/L/R",
            "O/J",
            "X/S/M",
            "O/C/F/U",
            "O/C/H",
            "X/S",
            "Y",
            "O",
            "X/S/M/L",
            "Y/E",
        ],
    }
    assert [p["filtered_out"] for p in rec.commands] == [
        ["prg8.py"],
        ["prg7.py", "prg9.py"],
        ["prg4.py", "prg5.py", "prg6.py"],
        ["prg1.py"],
    ]
    costs = {taxon: rec.taxon_cost(taxon) for taxon in rec.selected_programs["prg2.py"]}
    print(costs)
    assert costs == {
        "O/N/P": 0,
        "Y/T/Q": 0.375,
        "Y": 0,
        "X/S/M/L/R/D": 0,
        "O": 0,
        "O/C/H/B": 0,
        "X/S/M": 0,
        "X/S/M/L/R": 0,
        "Y/T": 0.25,
        "O/C": 0,
        "X/G": 0.25,
        "X/S/M/L/V": 0,
        "O/C/H/B/I": 0.03125,
    }
    text = rec.get_markdown(span_column_width=10)
    make_snapshot(Path("tests/data/dummy/recommendations.md"), text, capsys)


def test_recommend_programming_idioms(capsys):
    path = Path("tests/snapshots/programming_idioms_db.json")
    rec = Recommendations(db=json.loads(path.read_text()))
    rec.run_pipeline()
    output_path = path.parent / "programming_idioms_recommendations.md"
    rec.get_markdown()  # for coverage
    make_snapshot(
        output_path,
        rec.get_markdown(sorting_strategy="lexicographic", grouping_strategy="no_group"),
        capsys,
    )


def test_recommend_simple_programs():
    db = json.loads(Path("tests/snapshots/simple_db.json").read_text())
    proper_taxons = {}
    for program in ["assignment.py", "collatz.py", "fizzbuzz.py", "is_even.py"]:
        proper_taxons[program] = set(db["programs"][program]["taxons"])

    rec = Recommendations(db)  # Warning: initialization modifies the db by side-effect.
    # The taxons of some programs are now augmented with the taxons of those they import,
    # associated with an empty list of spans. Exception: metadata taxons are not imported.
    original = proper_taxons["fizzbuzz.py"] | proper_taxons["collatz.py"]
    assert all(
        taxon.startswith("metadata")
        for taxon in original.difference(db["programs"]["fizzbuzz.py"]["taxons"])
    )

    commands = [
        {
            "operation": "exclude",
            "source": [
                "assignment.py",
                "fizzbuzz.py",  # imported by is_even.py, consequently excluded
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"collatz.py"}
    assert not rec.imparted_knowledge

    # A command excluding a sequence is equivalent to a sequence of excluding commands
    commands = [
        {"operation": "exclude", "source": ["assignment.py",],},
        {"operation": "exclude", "source": ["fizzbuzz.py",],},
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"collatz.py"}
    assert not rec.imparted_knowledge

    commands = [{"operation": "include", "source": ["this_program_does_not_exist.py",],}]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert not rec.selected_programs.keys()
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "source": [
                "assignment.py",
                "fizzbuzz.py",  # imported by is_even.py, which nevertheless will not be included
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"assignment.py", "fizzbuzz.py"}
    assert not rec.imparted_knowledge

    # A command including a sequence is not equivalent to a sequence of including commands
    commands = [
        {"operation": "include", "source": ["assignment.py",],},
        {"operation": "include", "source": ["fizzbuzz.py",],},
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert not rec.selected_programs.keys()
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "impart",
            "source": [
                "assignment.py",  # exclude it, and impart its taxons
                "fizzbuzz.py",  # idem, but ignore its imports or exports
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"collatz.py", "is_even.py"}
    assert proper_taxons["assignment.py"].issubset(rec.imparted_knowledge)
    assert proper_taxons["fizzbuzz.py"].issubset(rec.imparted_knowledge)
    assert not proper_taxons["is_even.py"].issubset(rec.imparted_knowledge)
    assert not proper_taxons["collatz.py"].issubset(rec.imparted_knowledge)

    commands = [
        {
            "operation": "exclude",
            "source": [
                "variable/assignment/single",  # featured directly by assignment.py
                # and collatz.py, which is imported by fizzbuzz.py and is_even.py
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert not rec.selected_programs.keys()
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "source": [
                "flow/conditional/else/if",  # featured directly by fizzbuzz.py,
                # which is imported by is_even.py
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"assignment.py", "collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "source": [
                "flow/conditional/else/if",  # Although not recommended, it is possible to mix
                "assignment.py",  # taxons and programs (ending with ".py") in a same command.
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "source": [
                "variable/assignment/single",  # featured by assignment.py and collatz.py
                # Although the latter is imported by both fizzbuzz.py and is_even.py, they are
                # not included in the result
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"assignment.py", "collatz.py"}
    assert not rec.imparted_knowledge

    commands = [{"operation": "include", "source": ["this_taxon_does_not_exist",],}]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert not rec.selected_programs.keys()
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "source": [
                ("variable/assignment", "inside", "flow/loop"),  # featured by collatz.py only
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "exclude",
            "source": [
                ("variable/assignment", "inside", "flow/loop"),  # featured by collatz.py,
                # and indirectly by fizzbuzz.py and is_even.py
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"assignment.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "source": [
                ("variable/assignment", "not inside", "flow/loop"),  # Must read as:
                # Include all programs featuring an assignment, except those where this assignment
                # is inside a loop. Hence, this includes assignment.py, even if it does not feature
                # a loop.
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {"assignment.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "source": [
                ("variable/assignment", "inside", "metadata/program"),  # This comes down to
                # including all programs featuring an assignment.
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    print(rec.selected_programs.keys())
    assert rec.selected_programs.keys() == {"assignment.py", "collatz.py"}
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "include",
            "source": [
                ("variable/assignment", "not inside", "metadata/program"),  # This comes down to
                # exclude all programs either featuring or not featuring an assignment!
            ],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    print(rec.selected_programs.keys())
    assert not rec.selected_programs.keys()
    assert not rec.imparted_knowledge

    commands = [
        {
            "operation": "impart",  # Imparting triples is currently not supported (ignored).
            "source": [("variable/assignment", "inside", "flow/loop"),],
        }
    ]
    rec = Recommendations(db, commands=commands)
    rec.run_pipeline()
    assert rec.selected_programs.keys() == {
        "assignment.py",
        "collatz.py",
        "fizzbuzz.py",
        "is_even.py",
    }
    assert not rec.imparted_knowledge


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
