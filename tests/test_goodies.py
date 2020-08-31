import pytest

import context
from paroxython.goodies import (
    add_line_numbers,
    cost_bucket,
    couple_to_string,
    enumeration_to_txt_factory,
    title_to_slug_factory,
)
from paroxython.user_types import Span


def test_non_ascii_title_to_slug_factory():
    titles_and_slugs = [
        ("Partie 1. Fantine", "partie-1-fantine"),
        ("Livre 1. Un juste", "livre-1-un-juste"),
        ("M. Myriel", "m-myriel"),
        ("M. Myriel devient monseigneur Bienvenu", "m-myriel-devient-monseigneur-bienvenu"),
        ("A bon évêque dur évêché", "a-bon-eveque-dur-eveche"),
        ("Les œuvres semblables aux paroles", "les-uvres-semblables-aux-paroles"),
        (
            "Que monseigneur Bienvenu faisait durer trop longtemps ses soutanes",
            "que-monseigneur-bienvenu-faisait-durer-trop-longtemps-ses-soutanes",
        ),
        ("Par qui il faisait garder sa maison", "par-qui-il-faisait-garder-sa-maison"),
        ("Cravatte", "cravatte"),
        ("Philosophie après boire", "philosophie-apres-boire"),
        ("Le frère raconté par la sœur", "le-frere-raconte-par-la-sur"),
        (
            "L'évêque en présence d'une lumière inconnue",
            "leveque-en-presence-dune-lumiere-inconnue",
        ),
        ("Une restriction", "une-restriction"),
        ("Solitude de monseigneur Bienvenu", "solitude-de-monseigneur-bienvenu"),
        ("Ce qu'il croyait", "ce-quil-croyait"),
        ("Ce qu'il pensait", "ce-quil-pensait"),
    ]
    title_to_slug = title_to_slug_factory()
    for (title, slug) in titles_and_slugs:
        assert title_to_slug(title) == slug


def test_duplicate_title_to_slug_factory():
    titles_and_slugs = [
        ("foobar", "foobar"),
        ("foo", "foo"),
        ("bar", "bar"),
        ("foobar", "foobar-1"),
        ("foobar", "foobar-2"),
        ("foo", "foo-1"),
        ("foo", "foo-2"),
        ("foobar", "foobar-3"),
        ("foo-2", "foo-2-1"),
        ("foo-2", "foo-2-2"),
        ("foo", "foo-3"),
    ]
    title_to_slug = title_to_slug_factory()
    for (title, slug) in titles_and_slugs:
        assert title_to_slug(title, deduplicate=True) == slug


def test_enumeration_to_txt():
    enumeration_to_txt = enumeration_to_txt_factory()
    assert enumeration_to_txt("") == ""
    enumeration_to_txt = enumeration_to_txt_factory(30)
    assert enumeration_to_txt("1, 2, 3, 4, 5-6, 7, 8, 9") == "1, 2, 3, 4, 5-6, 7, 8, 9"
    enumeration_to_txt = enumeration_to_txt_factory(7)
    print(enumeration_to_txt("1, 2, 3, 4, 5-6, 7, 8, 9"))
    assert (
        enumeration_to_txt("1, 2, 3, 4, 5-6, 7, 8, 9")
        == "<details><summary>1,</summary>2, 3,<br>4, 5-6,<br>7, 8, 9</details>"
    )


def test_cost_bucket():
    values = [i / 8 for i in range(20)]
    result = list(zip(values, map(cost_bucket, values)))
    print(result)
    assert result == [
        (0.0, "0"),
        (0.125, "in ]0, 0.25["),
        (0.25, "in [0.25, 0.5["),
        (0.375, "in [0.25, 0.5["),
        (0.5, "in [0.5, 1["),
        (0.625, "in [0.5, 1["),
        (0.75, "in [0.5, 1["),
        (0.875, "in [0.5, 1["),
        (1.0, "in [1, 2["),
        (1.125, "in [1, 2["),
        (1.25, "in [1, 2["),
        (1.375, "in [1, 2["),
        (1.5, "in [1, 2["),
        (1.625, "in [1, 2["),
        (1.75, "in [1, 2["),
        (1.875, "in [1, 2["),
        (2.0, "in [2, 4["),
        (2.125, "in [2, 4["),
        (2.25, "in [2, 4["),
        (2.375, "in [2, 4["),
    ]


def test_add_line_numbers():
    result = add_line_numbers("\n".join(map(str, range(15))))
    print(result)
    assert (
        result
        == "1   0\n2   1\n3   2\n4   3\n5   4\n6   5\n7   6\n8   7\n9   8\n10  9\n11  10\n12  11\n13  12\n14  13\n15  14"
    )
    assert add_line_numbers("") == ""


def test_couple_to_string():
    assert couple_to_string((12, 15)) == "12-15"
    assert couple_to_string((12, 12)) == "12"
    assert couple_to_string(Span(12, 15)) == "12-15"


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
