from collections import Counter as C

import pytest

import context
from paroxython.span import Span
from paroxython.taxonomy import Taxonomy, Taxon, ProgramTaxons
from paroxython.label_generators import Label, ProgramLabels

t = Taxonomy("tests/data/test_taxonomy.tsv")
S = lambda i, j: Span([i, j])  # shorten Span([i, j])
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
    labels = [
        Label("if", [S(1, 1), S(1, 1), S(2, 5)]),
        Label("comparison_operator:Lt", [S(1, 1), S(3, 3), S(2, 2)]),
    ]
    assert t.to_taxons(labels) == [
        Taxon("control_flow/conditional/", C({S(1, 1): 2, S(2, 5): 1})),
        Taxon("test/inequality/", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]


def test_deduplicated_taxons():
    taxons = [
        Taxon("control_flow/conditional/", C({S(1, 1): 2, S(2, 5): 1})),
        Taxon("control_flow/conditional/else/", C({S(1, 1): 1, S(2, 5): 1})),
        Taxon("test/inequality/", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]
    assert t.deduplicated_taxons(taxons) == [
        Taxon("control_flow/conditional/", C({S(1, 1): 1})),
        Taxon("control_flow/conditional/else/", C({S(1, 1): 1, S(2, 5): 1})),
        Taxon("test/inequality/", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
    ]


def test_call():
    programs_labels = [
        ProgramLabels(
            "algo1",
            [
                Label("if", [S(1, 1), S(1, 1), S(2, 5)]),
                Label("if_else", [S(1, 1), S(2, 5)]),
                Label("comparison_operator:Lt", [S(1, 1), S(3, 3), S(2, 2)]),
            ],
        ),
        ProgramLabels(
            "algo2",
            [
                Label("method_call:difference_update", [S(1, 1), S(1, 1), S(2, 5)]),
                Label("literal:Set", [S(1, 1), S(2, 5)]),
            ],
        ),
    ]
    result = list(t(programs_labels))
    assert result[0] == ProgramTaxons(
        "algo1",
        [
            Taxon("control_flow/conditional/", C({S(1, 1): 1})),
            Taxon("control_flow/conditional/else/", C({S(1, 1): 1, S(2, 5): 1})),
            Taxon("test/inequality/", C({S(2, 2): 1, S(3, 3): 1, S(1, 1): 1})),
        ],
    )
    assert result[1] == ProgramTaxons(
        "algo2",
        [
            Taxon("call/function/builtin/casting/set/", C({S(1, 1): 1, S(2, 5): 1})),
            Taxon("type/set/", C({S(1, 1): 3, S(2, 5): 2})),
        ],
    )
