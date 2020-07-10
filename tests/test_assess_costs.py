import json
from pathlib import Path

import pytest

import context
from paroxython.assess_costs import (
    LearningCostAssessor,
    range_to_cost_linear,
    range_to_cost_zeno,
)


def test_range_to_cost_zeno():
    assert range_to_cost_zeno(0, 0) == 0
    assert range_to_cost_zeno(42, 42) == 0
    assert range_to_cost_zeno(0, 1) == (1 / 2)
    assert range_to_cost_zeno(0, 2) == (1 / 2 + 1 / 4)
    assert range_to_cost_zeno(0, 3) == (1 / 2 + 1 / 4 + 1 / 8)
    assert range_to_cost_zeno(1, 4) == (1 / 4 + 1 / 8 + 1 / 16)


def test_range_to_cost_linear():
    assert range_to_cost_linear(3, 5) == 2


def test_taxon_cost():
    assess = LearningCostAssessor(None, "linear")
    imparted_knowledge = {"O", "O/J", "X", "X/S", "X/S/M", "X/S/M/L"}
    assess.set_imparted_knowledge(imparted_knowledge)
    assert assess.taxon_cost("O") == 0
    assert assess.taxon_cost("O/C") == 1
    assert assess.taxon_cost("O/C/F") == 2
    assert assess.taxon_cost("O/C/F/U") == 3
    assert assess.taxon_cost("O/J") == 0
    assert assess.taxon_cost("O/N") == 1
    assert assess.taxon_cost("O/N/P") == 2
    assert assess.taxon_cost("X") == 0
    assert assess.taxon_cost("X/S") == 0
    assert assess.taxon_cost("X/S/M") == 0
    assert assess.taxon_cost("X/S/M/L") == 0
    assert assess.taxon_cost("X/S/M/L/R") == 1
    assert assess.taxon_cost("X/S/M/L/R/D") == 2
    assert assess.taxon_cost("X/S/M/L/R/D/A") == 3
    assert assess.taxon_cost("Y") == 1
    assert assess.taxon_cost("Y/E") == 2
    assert assess.taxon_cost("Y/T") == 2
    assert assess.taxon_cost("Y/T/Q") == 3
    assert assess.taxon_cost("") == 1  # weird, but unspecified


def test_get_sorted_recommandations():
    db = json.loads(Path("examples/dummy/programs_db.json").read_text())
    assess = LearningCostAssessor(db["programs"], "zeno")
    imparted_knowledge = {"O", "O/J", "X", "X/S", "X/S/M", "X/S/M/L"}
    assess.set_imparted_knowledge(imparted_knowledge)
    result = assess(db["programs"].keys())
    print(result)
    assert result == [
        (2.8671875, "prg5.py"),
        (3.1328125, "prg8.py"),
        (3.328125, "prg1.py"),
        (3.7578125, "prg4.py"),
        (3.9375, "prg3.py"),
        (4.015625, "prg2.py"),
        (4.296875, "prg7.py"),
        (4.7421875, "prg6.py"),
        (4.90625, "prg9.py"),
    ]


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
