import pytest

import context
from paroxython.program_generator import generate_programs


def test_generate_programs():
    result = generate_programs("tests/data/programs")

    program = next(result)
    assert program.path.name == "assignment.py"
    assert program.source == "a = b"

    program = next(result)
    assert program.path.name == "function_definition.py"
    assert program.source == "def succ(n):\n    return a + b + 1"

    program = next(result)
    assert program.path.name == "loop.py"
    assert program.source == 'while input():\n    print("foobar")'


pytest.main(args=["-q"])
