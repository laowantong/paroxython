import pytest

import context
from paroxython.generate_programs import generate_programs


def test_generate_programs():
    result = generate_programs("tests/data/simple")

    program = next(result)
    assert program.path.name == "assignment.py"
    assert program.source == "a = b"

    program = next(result)
    assert program.path.name == "collatz_print.py"
    assert program.source.startswith("def print_collatz(n):")

    program = next(result)
    assert program.path.name == "fizzbuzz.py"
    assert program.source.startswith("for i in range(1, 101):")

    program = next(result)
    assert program.path.name == "is_even.py"
    assert program.source == "def is_even(n):\n    return n % 2 == 0"
