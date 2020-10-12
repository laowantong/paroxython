from pathlib import Path
import pytest

import context
from paroxython.list_programs import list_programs


def test_list_programs():
    result = iter(list_programs(Path("examples/mini/programs/")))

    program = next(result)
    assert program.path == "assignment.py"
    assert program.source == "a = b"

    program = next(result)
    assert program.path == "collatz.py"
    assert program.source.startswith("def print_collatz(n):")

    program = next(result)
    assert program.path == "fizzbuzz.py"
    assert program.source.startswith("import collatz")

    program = next(result)
    assert program.path == "is_even.py"
    assert program.source.__contains__("def is_even(n):\n    return n % 2 == 0")


if __name__ == "__main__":
    pytest.main(["-qq", __import__("sys").argv[0]])
