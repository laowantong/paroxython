import json
from collections import Counter as c
from pathlib import Path

import pytest

from make_snapshot import make_snapshot

import context
from paroxython.goodies import couple_to_string
from paroxython.label_programs import labelled_programs
from paroxython.map_taxonomy import Taxonomy, deduplicated_taxa, is_literal
from paroxython.user_types import Label, Program, Span

t = Taxonomy(Path("examples/mini/taxonomy.tsv"))
S = lambda i, j: Span(i, j)  # shortcut for Span(i, j)


def test_initial_values():
    print(t.literal_labels)
    assert t.literal_labels == {
        "literal:Set": ["call/subroutine/builtin/casting/set", "type/non_sequence/set"],
        "if": ["flow/conditional"],
        "if_else": ["flow/conditional/else"],
        "free_call:list": ["type/sequence/list"],
        "member_call_method:difference_update": ["type/non_sequence/set"],
    }
    print(t.compiled_labels)
    assert t.compiled_labels[0][1] == "call/subroutine/builtin/casting/\\1"
    assert t.compiled_labels[1][1] == "condition/inequality"


def test_get_taxon_name_list():
    assert t.get_taxon_name_list("if") == ["flow/conditional"]
    assert t.get_taxon_name_list("comparison_operator:Gt") == ["condition/inequality"]
    assert t.get_taxon_name_list("label_with_no_corresponding_taxon") == []
    assert t.get_taxon_name_list("free_call:list") == [
        "type/sequence/list",
        "call/subroutine/builtin/casting/list",
    ]
    assert t.get_taxon_name_list("looks/like/a/taxon") == ["looks/like/a/taxon"]


def test_is_literal():
    assert is_literal("external_free_call:print")
    assert is_literal("assignment_rhs_atom:1.5")
    assert is_literal("looks/like/a/taxon")
    assert not is_literal("whole_span:.+")
    assert not is_literal("(assignment_rhs_atom:1.5)")


def test_to_taxa():
    labels = [
        Label("if", [S(1, 1), S(1, 1), S(2, 5)]),
        Label("comparison_operator:Lt", [S(1, 1), S(3, 3), S(2, 2)]),
    ]
    assert t.to_taxa(labels) == [
        ("condition/inequality", c({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
        ("flow/conditional", c({S(1, 1): 2, S(2, 5): 1})),
    ]


def test_deduplicated_taxa():
    assert deduplicated_taxa([]) == []
    taxa = [
        ("flow/conditional", c({S(1, 1): 2, S(2, 5): 1})),
        ("flow/conditional/else", c({S(1, 1): 1, S(2, 5): 1})),
        ("condition/inequality", c({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]
    result = deduplicated_taxa(taxa)
    print(result)
    assert result == [
        ("flow/conditional", c({S(1, 1): 1})),
        ("flow/conditional/else", c({S(1, 1): 1, S(2, 5): 1})),
        ("condition/inequality", c({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]


def test_deduplicated_taxa_with_deletion():
    taxa = [
        ("flow", c({S(1, 1): 2, S(2, 5): 1})),
        ("flow/conditional", c({S(1, 1): 2, S(2, 5): 1})),
        ("flow/conditional/else", c({S(1, 1): 2, S(2, 5): 1})),
    ]
    result = deduplicated_taxa(taxa)
    print(result)
    assert result == [
        ("flow/conditional/else", c({S(1, 1): 2, S(2, 5): 1})),
    ]
    taxa = [
        ("flow", c({S(1, 1): 2, S(2, 5): 2})),
        ("flow/conditional", c({S(1, 1): 2, S(2, 5): 1})),
        ("flow/conditional/else", c({S(1, 1): 2, S(2, 5): 1})),
    ]
    result = deduplicated_taxa(taxa)
    print(result)
    assert result == [
        ("flow", c({S(2, 5): 1})),
        ("flow/conditional/else", c({S(1, 1): 2, S(2, 5): 1})),
    ]
    taxa = [
        ("flow", c({S(1, 1): 2, S(2, 5): 2})),
        ("flow/conditional", c({S(1, 1): 1, S(2, 5): 1})),
        ("flow/loop", c({S(1, 1): 1, S(2, 5): 1})),
    ]
    result = deduplicated_taxa(taxa)
    print(result)
    assert result == [
        ("flow/conditional", c({S(1, 1): 1, S(2, 5): 1})),
        ("flow/loop", c({S(1, 1): 1, S(2, 5): 1})),
    ]


def test_call():
    programs = [
        Program(
            path="algo1",
            labels=[
                Label("if", [S(1, 1), S(1, 1), S(2, 5)]),
                Label("if_else", [S(1, 1), S(2, 5)]),
                Label("comparison_operator:Lt", [S(1, 1), S(3, 3), S(2, 2)]),
            ],
            taxa=[],
            addition={},
            deletion={},
        ),
        Program(
            path="algo2",
            labels=[
                Label("member_call_method:difference_update", [S(1, 1), S(1, 1), S(2, 5)]),
                Label("literal:Set", [S(1, 1), S(2, 5)]),
            ],
            taxa=[],
            addition={},
            deletion={},
        ),
    ]
    result = {program.path: t.to_taxa(program.labels) for program in programs}
    print(result)
    assert result == {
        "algo1": [
            ("condition/inequality", c({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
            ("flow/conditional", c({S(1, 1): 1})),
            ("flow/conditional/else", c({S(1, 1): 1, S(2, 5): 1})),
        ],
        "algo2": [
            ("call/subroutine/builtin/casting/set", c({S(1, 1): 1, S(2, 5): 1})),
            ("type/non_sequence/set", c({S(1, 1): 3, S(2, 5): 2})),
        ],
    }


def test_snapshot_mini_taxa(capsys):
    taxonomy = Taxonomy()
    acc = {}
    programs = labelled_programs(Path("examples/mini/programs"))
    for program in programs:
        taxa = taxonomy.to_taxa(program.labels)
        acc[program.path] = {
            name: " ".join(map(couple_to_string, sorted(set(spans)))) for (name, spans) in taxa
        }
    result = json.dumps(acc, indent=2)
    make_snapshot(Path("examples/mini/taxa.json"), result, capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
