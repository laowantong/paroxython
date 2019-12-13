import pytest
import json
from pathlib import Path

import context
from paroxython import make_db


def test_make_db():
    f = lambda d: {k: "ignored" for (k, v) in d.items() if k != "timestamp"}
    result = make_db.make_database(["tests/data/programs"])
    expected = Path("tests/data/programs/db.json").read_text()
    assert json.loads(result, object_hook=f) == json.loads(expected, object_hook=f)


pytest.main(args=["-q"])
