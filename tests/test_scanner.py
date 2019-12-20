import pytest

import context
from paroxython.scanner import Scanner

scan = Scanner("tests/data/programs")


def test_generate_tagged_source_codes():
    result = list(scan.generate_tagged_source_codes())
    expected = [
        "# ----------------------------------------------------------------------------------------\n"
        "# tests/data/programs/assignment.py\n"
        "# ----------------------------------------------------------------------------------------",
        "a = b # assignment, global_variable_definition\n",
        "# ----------------------------------------------------------------------------------------\n"
        "# tests/data/programs/function_definition.py\n"
        "# ----------------------------------------------------------------------------------------",
        "def succ(n): # function:succ (-> +1)\n"
        "    return a + b + 1 # binary_operator:Add, literal:Num\n",
        "# ----------------------------------------------------------------------------------------\n"
        "# tests/data/programs/loop.py\n"
        "# ----------------------------------------------------------------------------------------",
        "while input(): # function_call:input\n"
        '    print("foobar") # function_call:print, literal:Str\n',
    ]
    for (result_row, expected_row) in zip(result, expected):
        assert result_row == expected_row


pytest.main(args=["-q"])
