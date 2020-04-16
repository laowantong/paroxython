from pathlib import Path
import pytest

import context
from paroxython.list_programs import list_programs


def test_list_programs():
    result = iter(list_programs(Path("tests/data/simple")))

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
