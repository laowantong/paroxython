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
        "# tests/data/programs/collatz_print.py\n"
        "# ----------------------------------------------------------------------------------------",
        "def print_collatz(n): # added_block_label (-> +7), function:print_collatz (-> +7)\n"
        "    while n != 1: # comparison_operator:NotEq, evolve_state (-> +5), literal:Num\n"
        "        print(n) # function_call:print\n"
        "        if n % 2 == 0: # added_label_on_line_4, binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_else (-> +3), literal:Num, suggest_conditional_expression (-> +3)\n"
        "            n = n // 2 # assignment, suggest_augmented_assignment\n"
        "        else: # if\n"
        "            n = 3 * n + 1 # assignment, binary_operator:Add, binary_operator:Mult, literal:Num, suggest_constant_definition\n"
        "    print(n) # function_call:print\n",
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
