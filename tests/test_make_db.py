import json
from pathlib import Path

import pytest

import context
from paroxython.make_db import make_database


def test_make_db():
    dirty_fields = ["timestamp"]
    sanitize = lambda d: {k: ("ignored" if k in dirty_fields else d[k]) for k in d}
    result = json.loads(make_database(["tests/data/programs"]), object_hook=sanitize)
    expected = json.loads(Path("tests/data/programs/test_db.json").read_text())
    assert result == expected


pytest.main(args=["-q"])
