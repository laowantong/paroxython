import pytest

import context
from paroxython import program_generator


def test_generate_programs():
    result = program_generator.generate_programs("tests/data/programs")

    (path, program) = next(result)
    assert path.name == "assignment.py"
    assert program == "a = b"

    (path, program) = next(result)
    assert path.name == "function_definition.py"
    assert program == "def succ(n):\n    return n + 1"

    (path, program) = next(result)
    assert path.name == "loop.py"
    assert program == 'while input():\n    print("foobar")'


pytest.main(args=["-q"])
