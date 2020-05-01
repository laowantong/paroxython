from pathlib import Path

import pytest

import context
from make_snapshot import make_snapshot
from paroxython.make_db import Database


def test_snapshot_simple_db(capsys):
    db = Database(Path("tests/data/simple"), ignore_timestamps=True)
    make_snapshot(Path("tests/snapshots/simple_db.json"), db.get_json(), capsys)
    db.write_json(Path("tests/snapshots/simple_db.json"))


def test_sqlite_simple_db(capsys):
    db = Database(Path("tests/data/simple"))
    db.write_sqlite(Path("tests/snapshots/simple_db.sqlite"))


def test_snapshot_programming_idioms_db(capsys):
    db = Database(Path("tests/data/sanity"), ignore_timestamps=True)
    make_snapshot(Path("tests/snapshots/sanity_db.json"), db.get_json(), capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
