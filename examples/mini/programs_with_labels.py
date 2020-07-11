# ----------------------------------------------------------------------------------------
# assignment.py
# ----------------------------------------------------------------------------------------
a = b # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:b, node:Assign, node:Name, single_assignment:a, whole_span:1

# ----------------------------------------------------------------------------------------
# collatz.py
# ----------------------------------------------------------------------------------------
def print_collatz(n): # added_block_label (-> +7), function:print_collatz (-> +7), function_argument:n, function_argument_flavor:arg, function_returning_nothing:print_collatz (-> +7), node:FunctionDef (-> +7), node:arg, whole_span:8 (-> +7)
    while n != 1: # comparison_operator:NotEq, literal:1, loop:while (-> +5), loop_with_late_exit:while (-> +5), node:Compare, node:Name, node:Num, node:While (-> +5), suggest_constant_definition
        print(n) # call_argument:n, external_free_call:print, free_call:print, free_call_without_result:print, node:Call, node:Expr, node:Name
        if n % 2 == 0: # added_label_on_line_4, binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:0, if_test_atom:2, if_test_atom:n, literal:0, literal:2, modulo_operator, node:BinOp, node:Compare, node:If (-> +3), node:Name, node:Num, verbose_conditional_assignment (-> +3)
            n = n // 2 # assignment:FloorDiv, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, if_then_branch, literal:2, node:Assign, node:BinOp, node:Name, node:Num, single_assignment:n, suggest_augmented_assignment, update:n:2, update_by_assignment:n:2, update_by_assignment_with:FloorDiv, update_with:FloorDiv
        else: # unknown_label
            n = 3 * n + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:n, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, if_else_branch, literal:1, literal:3, multiplication_operator, node:Assign, node:BinOp, node:Name, node:Num, single_assignment:n, suggest_constant_definition, update:n:1, update:n:3, update_by_assignment:n:1, update_by_assignment:n:3, update_by_assignment_with:Add, update_with:Add
    print(n) # call_argument:n, external_free_call:print, free_call:print, free_call_without_result:print, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# fizzbuzz.py
# ----------------------------------------------------------------------------------------
import collatz # import_internally:collatz, import_module_internally:collatz, node:Import, whole_span:10 (-> +9)
for i in range(1, 101): # call_argument:1, call_argument:101, external_free_call:range, for:i (-> +8), for_range:1:101 (-> +8), free_call:range, literal:1, literal:101, loop:for (-> +8), loop_with_late_exit:for (-> +8), node:Call, node:For (-> +8), node:Name, node:Num, range:1:101
    if i % 15 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:15, if (-> +7), if_test_atom:0, if_test_atom:15, if_test_atom:i, literal:0, literal:15, modulo_operator, node:BinOp, node:Compare, node:If (-> +7), node:Name, node:Num, suggest_constant_definition
        print("FizzBuzz") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, node:Call, node:Expr, node:Name, node:Str
    elif i % 3 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:3, if (-> +5), if_test_atom:0, if_test_atom:3, if_test_atom:i, literal:0, literal:3, modulo_operator, node:BinOp, node:Compare, node:If (-> +5), node:Name, node:Num, suggest_constant_definition
        print("Fizz") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_elif_branch, literal:Str, node:Call, node:Expr, node:Name, node:Str
    elif i % 5 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:5, if (-> +3), if_test_atom:0, if_test_atom:5, if_test_atom:i, literal:0, literal:5, modulo_operator, node:BinOp, node:Compare, node:If (-> +3), node:Name, node:Num, suggest_constant_definition
        print("Buzz") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_elif_branch, literal:Str, node:Call, node:Expr, node:Name, node:Str
    else:
        print(i) # call_argument:i, external_free_call:print, free_call:print, free_call_without_result:print, if_else_branch, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# is_even.py
# ----------------------------------------------------------------------------------------
import fizzbuzz # import_internally:fizzbuzz, import_module_internally:fizzbuzz, node:Import, whole_span:3 (-> +2)
def is_even(n): # function:is_even (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:is_even (-> +1), node:FunctionDef (-> +1), node:arg
    return n % 2 == 0 # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, literal:0, literal:2, modulo_operator, node:BinOp, node:Compare, node:Name, node:Num, node:Return, return
