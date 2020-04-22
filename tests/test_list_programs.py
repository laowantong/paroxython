from pathlib import Path
import pytest

import context
from paroxython.list_programs import list_programs


def test_list_programs():
    result = iter(list_programs(Path("tests/data/simple")))

    program = next(result)
    assert program.name == "assignment.py"
    assert program.source == "a = b"

    program = next(result)
    assert program.name == "collatz_print.py"
    assert program.source.startswith("def print_collatz(n):")

    program = next(result)
    assert program.name == "fizzbuzz.py"
    assert program.source.startswith("import collatz_print")

    program = next(result)
    assert program.name == "is_even.py"
    assert program.source.__contains__("def is_even(n):\n    return n % 2 == 0")


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
