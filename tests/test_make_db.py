import json
from pathlib import Path

import pytest

import context
from paroxython.make_db import make_database, to_json


def test_make_db():
    dirty_fields = ["timestamp"]
    sanitize = lambda d: {k: ("ignored" if k in dirty_fields else d[k]) for k in d}
    db = make_database(["tests/data/programs"])
    result = json.loads(to_json(db), object_hook=sanitize)
    print(to_json(result))
    expected = json.loads(Path("tests/data/programs/test_db.json").read_text())
    assert result == expected
