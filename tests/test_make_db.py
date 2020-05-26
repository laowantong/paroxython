from pathlib import Path

import pytest

import context
from make_snapshot import make_snapshot
from paroxython.make_db import Database


def test_snapshot_mini_db(capsys):
    db = Database(Path("examples/mini/programs"))
    make_snapshot(Path("examples/mini/programs_db.json"), db.get_json(), capsys)
    db.write_sqlite(Path("examples/mini/programs_db.sqlite"))


def test_snapshot_programming_idioms_db(capsys):
    db = Database(Path("examples/idioms/programs"))
    make_snapshot(Path("examples/idioms/programs_db.json"), db.get_json(), capsys)


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
