import pytest

import context
from scanner import Scanner


def test_scan():
    scan = Scanner("tests/data/programs")
    result = list(scan.generate_tagged_source_codes())
    expected = [
        "# ----------------------------------------------------------------------------------------\n"
        "# tests/data/programs/assignment.py\n"
        "# ----------------------------------------------------------------------------------------",
        "a = b # assignment, global_variable_definition\n",
        "# ----------------------------------------------------------------------------------------\n"
        "# tests/data/programs/function_definition.py\n"
        "# ----------------------------------------------------------------------------------------",
        "def succ(n): # function_definition:succ (-> +1)\n"
        "    return n + 1 # binary_operator:Add, literal:Num\n",
        "# ----------------------------------------------------------------------------------------\n"
        "# tests/data/programs/loop.py\n"
        "# ----------------------------------------------------------------------------------------",
        "while input(): # function_call:input\n"
        '    print("foobar") # function_call:print, literal:Str\n',
    ]
    assert result == expected


pytest.main(args=["-q"])
