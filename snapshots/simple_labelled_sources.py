# ----------------------------------------------------------------------------------------
# tests/data/simple/assignment.py
# ----------------------------------------------------------------------------------------
a = b # assignment
      # assignment_lhs_identifier:a
      # assignment_rhs_atom:b
      # lines_of_code:1
      # single_assignment:a

# ----------------------------------------------------------------------------------------
# tests/data/simple/collatz_print.py
# ----------------------------------------------------------------------------------------
def print_collatz(n): # added_block_label (-> +7)
                      # function:print_collatz (-> +7)
                      # function_argument:n
                      # function_argument_flavor:arg
                      # function_returning_nothing:print_collatz (-> +7)
                      # lines_of_code:8 (-> +7)
    while n != 1: # comparison_operator:NotEq
                  # literal:1
                  # loop:while (-> +5)
                  # suggest_constant_definition
                  # while (-> +5)
        print(n) # call_argument:n
                 # function_call:print
                 # function_call_without_result:print
        if n % 2 == 0: # added_label_on_line_4
                       # binary_operator:Mod
                       # comparison_operator:Eq
                       # divisibility_test:2
                       # if (-> +3)
                       # if_test_atom:0
                       # if_test_atom:2
                       # if_test_atom:n
                       # literal:0
                       # literal:2
                       # suggest_conditional_expression (-> +3)
            n = n // 2 # assignment:FloorDiv
                       # assignment_lhs_identifier:n
                       # assignment_rhs_atom:2
                       # assignment_rhs_atom:n
                       # if_then_branch
                       # literal:2
                       # single_assignment:n
                       # suggest_augmented_assignment
                       # update:n:2
                       # update_by_assignment:n:2
                       # update_by_assignment_with:FloorDiv
                       # update_with:FloorDiv
        else: # unknown_label
            n = 3 * n + 1 # assignment:Add
                          # assignment_lhs_identifier:n
                          # assignment_rhs_atom:1
                          # assignment_rhs_atom:3
                          # assignment_rhs_atom:n
                          # binary_operator:Add
                          # binary_operator:Mult
                          # if_else_branch
                          # literal:1
                          # literal:3
                          # single_assignment:n
                          # suggest_constant_definition
                          # update:n:1
                          # update:n:3
                          # update_by_assignment:n:1
                          # update_by_assignment:n:3
                          # update_by_assignment_with:Add
                          # update_with:Add
    print(n) # call_argument:n
             # function_call:print
             # function_call_without_result:print

# ----------------------------------------------------------------------------------------
# tests/data/simple/fizzbuzz.py
# ----------------------------------------------------------------------------------------
for i in range(1, 101): # call_argument:1
                        # call_argument:101
                        # for:i (-> +8)
                        # for_range:1:101 (-> +8)
                        # function_call:range
                        # lines_of_code:9 (-> +8)
                        # literal:1
                        # literal:101
                        # loop:for (-> +8)
                        # range:1:101
    if i % 15 == 0: # binary_operator:Mod
                    # comparison_operator:Eq
                    # divisibility_test:15
                    # if (-> +7)
                    # if_test_atom:0
                    # if_test_atom:15
                    # if_test_atom:i
                    # literal:0
                    # literal:15
                    # suggest_constant_definition
        print("FizzBuzz") # call_argument:
                          # function_call:print
                          # function_call_without_result:print
                          # if_then_branch
                          # literal:Str
    elif i % 3 == 0: # binary_operator:Mod
                     # comparison_operator:Eq
                     # divisibility_test:3
                     # if (-> +5)
                     # if_test_atom:0
                     # if_test_atom:3
                     # if_test_atom:i
                     # literal:0
                     # literal:3
                     # suggest_constant_definition
        print("Fizz") # call_argument:
                      # function_call:print
                      # function_call_without_result:print
                      # if_elif_branch
                      # literal:Str
    elif i % 5 == 0: # binary_operator:Mod
                     # comparison_operator:Eq
                     # divisibility_test:5
                     # if (-> +3)
                     # if_test_atom:0
                     # if_test_atom:5
                     # if_test_atom:i
                     # literal:0
                     # literal:5
                     # suggest_constant_definition
        print("Buzz") # call_argument:
                      # function_call:print
                      # function_call_without_result:print
                      # if_elif_branch
                      # literal:Str
    else: # 
        print(i) # call_argument:i
                 # function_call:print
                 # if_else_branch

# ----------------------------------------------------------------------------------------
# tests/data/simple/is_even.py
# ----------------------------------------------------------------------------------------
def is_even(n): # function:is_even (-> +1)
                # function_argument:n
                # function_argument_flavor:arg
                # function_returning_something:is_even (-> +1)
                # lines_of_code:2 (-> +1)
    return n % 2 == 0 # binary_operator:Mod
                      # comparison_operator:Eq
                      # divisibility_test:2
                      # literal:0
                      # literal:2
                      # return
