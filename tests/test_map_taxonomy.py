import json
from collections import Counter as C
from pathlib import Path

import pytest

import context
from make_snapshot import make_snapshot
from paroxython.goodies import couple_to_string
from paroxython.label_programs import ProgramLabeller
from paroxython.map_taxonomy import Taxonomy
from paroxython.user_types import Label, Program, Span

t = Taxonomy(Path("tests/data/dummy/taxonomy.tsv"))
S = lambda i, j: Span(i, j)  # shortcut for Span(i, j)


def test_initial_values():
    print(t.literal_label_names)
    assert t.literal_label_names == {
        "literal:Set": ["call/function/builtin/casting/set", "type/non_sequence/set"],
        "if": ["flow/conditional"],
        "if_else": ["flow/conditional/else"],
        "free_call:list": ["type/sequence/list"],
        "member_call:difference_update": ["type/non_sequence/set"],
    }
    print(t.compiled_label_names)
    assert t.compiled_label_names[0][1] == "call/function/builtin/casting/\\1"
    assert t.compiled_label_names[1][1] == "test/inequality"


def test_get_taxon_name_list():
    assert t.get_taxon_name_list("if") == ["flow/conditional"]
    assert t.get_taxon_name_list("comparison_operator:Gt") == ["test/inequality"]
    assert t.get_taxon_name_list("label_with_no_corresponding_taxon") == []
    assert t.get_taxon_name_list("free_call:list") == [
        "type/sequence/list",
        "call/function/builtin/casting/list",
    ]


def test_to_taxons():
    labels = [
        Label("if", [S(1, 1), S(1, 1), S(2, 5)]),
        Label("comparison_operator:Lt", [S(1, 1), S(3, 3), S(2, 2)]),
    ]
    assert t.to_taxons(labels) == [
        ("flow/conditional", C({S(1, 1): 2, S(2, 5): 1})),
        ("test/inequality", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]


def test_deduplicated_taxons():
    assert t.deduplicated_taxons([]) == []
    taxons = [
        ("flow/conditional", C({S(1, 1): 2, S(2, 5): 1})),
        ("flow/conditional/else", C({S(1, 1): 1, S(2, 5): 1})),
        ("test/inequality", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]
    result = t.deduplicated_taxons(taxons)
    print(result)
    assert result == [
        ("flow/conditional", C({S(1, 1): 1})),
        ("flow/conditional/else", C({S(1, 1): 1, S(2, 5): 1})),
        ("test/inequality", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]


def test_deduplicated_taxons_with_deletion():
    taxons = [
        ("flow", C({S(1, 1): 2, S(2, 5): 1})),
        ("flow/conditional", C({S(1, 1): 2, S(2, 5): 1})),
        ("flow/conditional/else", C({S(1, 1): 2, S(2, 5): 1})),
    ]
    result = t.deduplicated_taxons(taxons)
    print(result)
    assert result == [
        ("flow/conditional/else", C({S(1, 1): 2, S(2, 5): 1})),
    ]
    taxons = [
        ("flow", C({S(1, 1): 2, S(2, 5): 2})),
        ("flow/conditional", C({S(1, 1): 2, S(2, 5): 1})),
        ("flow/conditional/else", C({S(1, 1): 2, S(2, 5): 1})),
    ]
    result = t.deduplicated_taxons(taxons)
    print(result)
    assert result == [
        ("flow", C({S(2, 5): 1})),
        ("flow/conditional/else", C({S(1, 1): 2, S(2, 5): 1})),
    ]
    taxons = [
        ("flow", C({S(1, 1): 2, S(2, 5): 2})),
        ("flow/conditional", C({S(1, 1): 1, S(2, 5): 1})),
        ("flow/loop", C({S(1, 1): 1, S(2, 5): 1})),
    ]
    result = t.deduplicated_taxons(taxons)
    print(result)
    assert result == [
        ("flow/conditional", C({S(1, 1): 1, S(2, 5): 1})),
        ("flow/loop", C({S(1, 1): 1, S(2, 5): 1})),
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
                Label("member_call:difference_update", [S(1, 1), S(1, 1), S(2, 5)]),
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
            ("flow/conditional", C({S(1, 1): 1})),
            ("flow/conditional/else", C({S(1, 1): 1, S(2, 5): 1})),
            ("test/inequality", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
        ],
        "algo2": [
            ("call/function/builtin/casting/set", C({S(1, 1): 1, S(2, 5): 1})),
            ("type/non_sequence/set", C({S(1, 1): 3, S(2, 5): 2})),
        ],
    }


def test_snapshot_simple_taxons(capsys):
    taxonomy = Taxonomy()
    acc = {}
    labeller = ProgramLabeller()
    labeller.label_programs(Path("tests/data/simple"))
    for program in labeller.programs:
        taxons = taxonomy.to_taxons(program.labels)
        acc[program.name] = {
            name: " ".join(map(couple_to_string, sorted(set(spans)))) for (name, spans) in taxons
        }
    result = json.dumps(acc, indent=2)
    make_snapshot(Path("tests/snapshots/simple_taxons.json"), result, capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
