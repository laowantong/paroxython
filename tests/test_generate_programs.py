import pytest

import context
from paroxython.generate_programs import generate_programs


def test_generate_programs():
    result = generate_programs("tests/data/programs")

    program = next(result)
    assert program.path.name == "assignment.py"
    assert program.source == "a = b"

    program = next(result)
    assert program.path.name == "collatz_print.py"
    assert program.source.startswith("def print_collatz(n):")

    program = next(result)
    assert program.path.name == "function_definition.py"
    assert program.source == "def succ(n):\n    return a + b + 1"

    program = next(result)
    assert program.path.name == "loop.py"
    assert program.source == 'while input():\n    print("foobar")'
