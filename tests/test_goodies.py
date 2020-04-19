import pytest

import context
from paroxython.goodies import title_to_slug_factory, add_line_numbers, enumeration_to_html_factory


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


def test_enumeration_to_html():
    enumeration_to_html = enumeration_to_html_factory()
    assert enumeration_to_html("") == ""
    enumeration_to_html = enumeration_to_html_factory(30)
    assert enumeration_to_html("1, 2, 3, 4, 5-6, 7, 8, 9") == "1, 2, 3, 4, 5-6, 7, 8, 9"
    enumeration_to_html = enumeration_to_html_factory(7)
    print(enumeration_to_html("1, 2, 3, 4, 5-6, 7, 8, 9"))
    assert (
        enumeration_to_html("1, 2, 3, 4, 5-6, 7, 8, 9")
        == "<details><summary>1,</summary>2, 3,<br>4, 5-6,<br>7, 8, 9</details>"
    )
