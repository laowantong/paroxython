import json
from pathlib import Path

import pytest

import context
from make_snapshot import make_snapshot
from paroxython.make_db import make_database, to_json


def test_snapshot_simple_db(capsys):
    dirty_fields = ["timestamp"]
    sanitize = lambda d: {k: ("ignored" if k in dirty_fields else d[k]) for k in d}
    db = make_database(["tests/data/simple"])
    result = to_json(json.loads(to_json(db), object_hook=sanitize))
    make_snapshot("snapshots/simple_db.json", result, capsys)
