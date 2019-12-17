import json
from pathlib import Path

import pytest

import context
from make_db import make_database


def test_make_db():
    f = lambda d: {k: "ignored" for (k, v) in d.items() if k != "timestamp"}
    result = make_database(["tests/data/programs"])
    expected = Path("tests/data/programs/test_db.json").read_text()
    assert json.loads(result, object_hook=f) == json.loads(expected, object_hook=f)


pytest.main(args=["-q"])
