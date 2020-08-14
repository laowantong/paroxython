from pathlib import Path
from collections import Counter

import pytest

from make_snapshot import make_snapshot

import context
from paroxython.make_db import TagDatabase, prepared_labels, prepared_taxa
from paroxython.user_types import Span


def test_snapshot_mini_db(capsys):
    db = TagDatabase(Path("examples/mini/programs"), ignore_timestamps=True)
    make_snapshot(Path("examples/mini/programs_db.json"), db.get_json(), capsys)
    db.write_sqlite(Path("examples/mini/programs_db.sqlite"))


def test_snapshot_programming_idioms_db(capsys):
    db = TagDatabase(Path("examples/idioms/programs"), ignore_timestamps=True)
    make_snapshot(Path("examples/idioms/programs_db.json"), db.get_json(), capsys)


def test_prepared_labels():
    labels = [
        (
            "name_1",
            [
                Span(start=1, end=2, path="foo"),
                Span(start=1, end=2, path="foo"),
                Span(start=1, end=2, path="bar"),
            ],
        ),
        ("name_2", [Span(start=2, end=4, path="fizz"), Span(start=6, end=7, path="buzz")]),
        ("name_3", [Span(start=5, end=5, path="foobar")]),
    ]
    result = prepared_labels(labels)
    print(result)
    assert result == {
        "name_1": [(1, 2), (1, 2)],
        "name_2": [(2, 4), (6, 7)],
        "name_3": [(5, 5)],
    }


def test_prepared_taxa():
    taxa = [
        (
            "name_1",
            Counter({Span(start=1, end=2, path="foo"): 2, Span(start=1, end=2, path="bar"): 1}),
        ),
        (
            "name_2",
            Counter({Span(start=2, end=4, path="fizz"): 1, Span(start=6, end=7, path="buzz"): 1}),
        ),
        ("name_3", Counter({Span(start=5, end=5, path="foobar"): 1})),
    ]
    result = prepared_taxa(taxa)
    print(result)
    assert result == {
        "name_1": [(1, 2), (1, 2)],
        "name_2": [(2, 4), (6, 7)],
        "name_3": [(5, 5)],
    }


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
