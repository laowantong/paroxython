import json
from collections import Counter as C
from pathlib import Path

import pytest

import context
from make_snapshot import make_snapshot
from paroxython.label_programs import ProgramLabeller
from paroxython.map_taxonomy import Taxonomy
from paroxython.span import Span
from paroxython.user_types import Label, Program

t = Taxonomy(Path("tests/data/dummy/taxonomy.tsv"))
S = lambda i, j: Span([i, j])  # shortcut for Span([i, j])


def test_initial_values():
    print(t.literal_label_names)
    assert t.literal_label_names == {
        "literal:Set": ["call/function/builtin/casting/set", "type/set"],
        "if": ["control_flow/conditional"],
        "if_else": ["control_flow/conditional/else"],
        "method_call:difference_update": ["type/set"],
    }
    assert t.compiled_label_names[0][1] == "test/inequality"


def test_get_taxon_name_list():
    assert t.get_taxon_name_list("if") == ["control_flow/conditional"]
    assert t.get_taxon_name_list("comparison_operator:Gt") == ["test/inequality"]
    assert t.get_taxon_name_list("label_with_no_corresponding_taxon") == []


def test_to_taxons():
    labels = [
        Label("if", [S(1, 1), S(1, 1), S(2, 5)]),
        Label("comparison_operator:Lt", [S(1, 1), S(3, 3), S(2, 2)]),
    ]
    assert t.to_taxons(labels) == [
        ("control_flow/conditional", C({S(1, 1): 2, S(2, 5): 1})),
        ("test/inequality", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]


def test_deduplicated_taxons():
    assert t.deduplicated_taxons([]) == []
    taxons = [
        ("control_flow/conditional", C({S(1, 1): 2, S(2, 5): 1})),
        ("control_flow/conditional/else", C({S(1, 1): 1, S(2, 5): 1})),
        ("test/inequality", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]
    result = t.deduplicated_taxons(taxons)
    print(result)
    assert result == [
        ("control_flow/conditional", C({S(1, 1): 1})),
        ("control_flow/conditional/else", C({S(1, 1): 1, S(2, 5): 1})),
        ("test/inequality", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]


def test_deduplicated_taxons_with_deletion():
    taxons = [
        ("control_flow", C({S(1, 1): 2, S(2, 5): 1})),
        ("control_flow/conditional", C({S(1, 1): 2, S(2, 5): 1})),
        ("control_flow/conditional/else", C({S(1, 1): 2, S(2, 5): 1})),
    ]
    result = t.deduplicated_taxons(taxons)
    print(result)
    assert result == [
        ("control_flow/conditional/else", C({S(1, 1): 2, S(2, 5): 1})),
    ]
    taxons = [
        ("control_flow", C({S(1, 1): 2, S(2, 5): 2})),
        ("control_flow/conditional", C({S(1, 1): 2, S(2, 5): 1})),
        ("control_flow/conditional/else", C({S(1, 1): 2, S(2, 5): 1})),
    ]
    result = t.deduplicated_taxons(taxons)
    print(result)
    assert result == [
        ("control_flow", C({S(2, 5): 1})),
        ("control_flow/conditional/else", C({S(1, 1): 2, S(2, 5): 1})),
    ]
    taxons = [
        ("control_flow", C({S(1, 1): 2, S(2, 5): 2})),
        ("control_flow/conditional", C({S(1, 1): 1, S(2, 5): 1})),
        ("control_flow/loop", C({S(1, 1): 1, S(2, 5): 1})),
    ]
    result = t.deduplicated_taxons(taxons)
    print(result)
    assert result == [
        ("control_flow/conditional", C({S(1, 1): 1, S(2, 5): 1})),
        ("control_flow/loop", C({S(1, 1): 1, S(2, 5): 1})),
    ]


def test_call():
    programs = [
        Program(
            name="algo1",
            labels=[
                Label("if", [S(1, 1), S(1, 1), S(2, 5)]),
                Label("if_else", [S(1, 1), S(2, 5)]),
                Label("comparison_operator:Lt", [S(1, 1), S(3, 3), S(2, 2)]),
            ],
            taxons=[],
            addition={},
            deletion={},
        ),
        Program(
            name="algo2",
            labels=[
                Label("method_call:difference_update", [S(1, 1), S(1, 1), S(2, 5)]),
                Label("literal:Set", [S(1, 1), S(2, 5)]),
            ],
            taxons=[],
            addition={},
            deletion={},
        ),
    ]
    result = {program.name: t.to_taxons(program.labels) for program in programs}
    print(result)
    assert result == {
        "algo1": [
            ("control_flow/conditional", C({S(1, 1): 1})),
            ("control_flow/conditional/else", C({S(1, 1): 1, S(2, 5): 1})),
            ("test/inequality", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
        ],
        "algo2": [
            ("call/function/builtin/casting/set", C({S(1, 1): 1, S(2, 5): 1})),
            ("type/set", C({S(1, 1): 3, S(2, 5): 2})),
        ],
    }


def test_snapshot_simple_taxons(capsys):
    taxonomy = Taxonomy()
    acc = {}
    labeller = ProgramLabeller(Path("tests/data/simple"))
    programs = labeller.list_labelled_programs()
    for program in programs:
        taxons = taxonomy.to_taxons(program.labels)
        acc[program.name] = {
            name: " ".join(map(str, sorted(set(spans)))) for (name, spans) in taxons
        }
    result = json.dumps(acc, indent=2)
    make_snapshot(Path("tests/snapshots/simple_taxons.json"), result, capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
