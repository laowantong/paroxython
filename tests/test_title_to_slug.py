import pytest

import context
from paroxython.title_to_slug import title_converter


def test_non_ascii_titles():
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
    title_to_slug = title_converter()
    for (title, slug) in titles_and_slugs:
        assert title_to_slug(title) == slug


def test_duplicate_titles():
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
    title_to_slug = title_converter()
    for (title, slug) in titles_and_slugs:
        assert title_to_slug(title, deduplicate=True) == slug
