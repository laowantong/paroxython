from pathlib import Path

import pytest

import context


from paroxython.recommend_programs import Recommendations
from make_snapshot import make_snapshot


def test_recommend_program(capsys):
    rec = Recommendations(Path("tests/data/dummy/pipe.py"))
    rec.run_pipeline()
    print(rec.recommended_programs)
    assert rec.recommended_programs == {
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
    assert [p["filtered_out"] for p in rec.processes] == [
        ["prg8.py"],
        ["prg7.py", "prg9.py"],
        ["prg4.py", "prg5.py", "prg6.py"],
        ["prg1.py"],
    ]
    costs = {taxon: rec.taxon_cost(taxon) for taxon in rec.recommended_programs["prg2.py"]}
    print(costs)
    assert costs == {
        "O/N/P": 0,
        "Y/T/Q": 384,
        "Y": 0,
        "X/S/M/L/R/D": 0,
        "O": 0,
        "O/C/H/B": 0,
        "X/S/M": 0,
        "X/S/M/L/R": 0,
        "Y/T": 256,
        "O/C": 0,
        "X/G": 256,
        "X/S/M/L/V": 0,
        "O/C/H/B/I": 32,
    }
    text = rec.get_markdown(toc_group_limit=1)  # for coverage testing
    text = rec.get_markdown(span_column_width=10)
    make_snapshot(Path("tests/data/dummy/recommendations.md"), text, capsys)
    rec.dump(text)  # for coverage testing
