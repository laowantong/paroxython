import pytest
from collections import Counter

import context
from paroxython import taxonomy
from paroxython import span

t = taxonomy.Taxonomy("tests/data/test_taxonomy.tsv")
S = lambda i, j: span.Span([i, j])  # shorten Span([i, j])
pytest.main(args=["-q"])


def test_initial_values():
    assert t.literal_label_names == {
        "if": ["control_flow/conditional/"],
        "if_else": ["control_flow/conditional/else/"],
        "method_call:difference_update": ["type/set/"],
        "literal:Set": ["type/set/", "call/function/builtin/casting/set/"],
    }
    assert t.compiled_label_names[0][1] == "test/inequality/"


def test_get_taxon_name_list():
    assert t.get_taxon_name_list("if") == ["control_flow/conditional/"]
    assert t.get_taxon_name_list("comparison_operator:Gt") == ["test/inequality/"]
    assert t.get_taxon_name_list("label_with_no_corresponding_taxon") == []


def test_to_taxons():
    labels = {
        "if": [S(1, 1), S(1, 1), S(2, 5)],
        "comparison_operator:Lt": [S(1, 1), S(3, 3), S(2, 2)],
    }
    assert t.to_taxons(labels) == [
        ("control_flow/conditional/", Counter({S(1, 1): 2, S(2, 5): 1})),
        ("test/inequality/", Counter({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]


def test_deduplicated_taxons():
    taxons = [
        ("control_flow/conditional/", Counter({S(1, 1): 2, S(2, 5): 1})),
        ("control_flow/conditional/else/", Counter({S(1, 1): 1, S(2, 5): 1})),
        ("test/inequality/", Counter({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]
    assert t.deduplicated_taxons(taxons) == [
        ("control_flow/conditional/", Counter({S(1, 1): 1})),
        ("control_flow/conditional/else/", Counter({S(1, 1): 1, S(2, 5): 1})),
        ("test/inequality/", Counter({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]


def test_call():
    paths_and_labels = {
        "algo1": {
            "if": [S(1, 1), S(1, 1), S(2, 5)],
            "if_else": [S(1, 1), S(2, 5)],
            "comparison_operator:Lt": [S(1, 1), S(3, 3), S(2, 2)],
        },
        "algo2": {
            "method_call:difference_update": [S(1, 1), S(1, 1), S(2, 5)],
            "literal:Set": [S(1, 1), S(2, 5)],
        },
    }
    result = list(t(paths_and_labels.items()))
    assert result[0] == (
        "algo1",
        [
            ("control_flow/conditional/", Counter({S(1, 1): 1})),
            ("control_flow/conditional/else/", Counter({S(1, 1): 1, S(2, 5): 1})),
            ("test/inequality/", Counter({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
        ],
    )
    assert result[1] == (
        "algo2",
        [
            ("call/function/builtin/casting/set/", Counter({S(1, 1): 1, S(2, 5): 1})),
            ("type/set/", Counter({S(1, 1): 3, S(2, 5): 2})),
        ],
    )
