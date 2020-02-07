# ----------------------------------------------------------------------------------------
# tests/data/simple/assignment.py
# ----------------------------------------------------------------------------------------
a = b # assignment
      # assignment_lhs_identifier:a
      # assignment_rhs_atom:b

# ----------------------------------------------------------------------------------------
# tests/data/simple/collatz_print.py
# ----------------------------------------------------------------------------------------
def print_collatz(n): # added_block_label (-> +7)
                      # function:print_collatz (-> +7)
                      # function_returning_nothing:print_collatz (-> +7)
    while n != 1: # comparison_operator:NotEq
                  # evolve_state (-> +5)
                  # int_literal
                  # literal:Num
                  # suggest_constant_definition
                  # while (-> +5)
        print(n) # call_argument:n
                 # function_call:print
        if n % 2 == 0: # added_label_on_line_4
                       # binary_operator:Mod
                       # comparison_operator:Eq
                       # divisibility_test:2
                       # if (-> +3)
                       # if_test_atom:0
                       # if_test_atom:2
                       # if_test_atom:n
                       # int_literal
                       # literal:Num
                       # suggest_conditional_expression (-> +3)
            n = n // 2 # assignment
                       # assignment_lhs_identifier:n
                       # assignment_rhs_atom:2
                       # assignment_rhs_atom:n
                       # if_then_branch
                       # int_literal
                       # suggest_augmented_assignment
                       # variable_update:n:2
                       # variable_update_by_assignment:n:2
        else: # unknown_label
            n = 3 * n + 1 # assignment
                          # assignment_lhs_identifier:n
                          # assignment_rhs_atom:1
                          # assignment_rhs_atom:3
                          # assignment_rhs_atom:n
                          # binary_operator:Add
                          # binary_operator:Mult
                          # if_else_branch
                          # increment_variable:n:1
                          # increment_variable:n:3
                          # int_literal
                          # literal:Num
                          # suggest_constant_definition
                          # variable_update:n:1
                          # variable_update:n:3
                          # variable_update_by_assignment:n:1
                          # variable_update_by_assignment:n:3
    print(n) # call_argument:n
             # function_call:print

# ----------------------------------------------------------------------------------------
# tests/data/simple/fizzbuzz.py
# ----------------------------------------------------------------------------------------
for i in range(1, 101): # call_argument:1
                        # call_argument:101
                        # for:i (-> +8)
                        # for_range:1:101 (-> +8)
                        # function_call:range
                        # int_literal
                        # literal:Num
                        # range:1:101
    if i % 15 == 0: # binary_operator:Mod
                    # comparison_operator:Eq
                    # divisibility_test:15
                    # if (-> +7)
                    # if_test_atom:0
                    # if_test_atom:15
                    # if_test_atom:i
                    # int_literal
                    # literal:Num
                    # suggest_constant_definition
        print("FizzBuzz") # call_argument:
                          # function_call:print
                          # if_then_branch
                          # literal:Str
    elif i % 3 == 0: # binary_operator:Mod
                     # comparison_operator:Eq
                     # divisibility_test:3
                     # if (-> +5)
                     # if_test_atom:0
                     # if_test_atom:3
                     # if_test_atom:i
                     # int_literal
                     # literal:Num
                     # suggest_constant_definition
        print("Fizz") # call_argument:
                      # function_call:print
                      # if_elif_branch
                      # literal:Str
    elif i % 5 == 0: # binary_operator:Mod
                     # comparison_operator:Eq
                     # divisibility_test:5
                     # if (-> +3)
                     # if_test_atom:0
                     # if_test_atom:5
                     # if_test_atom:i
                     # int_literal
                     # literal:Num
                     # suggest_constant_definition
        print("Buzz") # call_argument:
                      # function_call:print
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
                # function_returning_something:is_even (-> +1)
    return n % 2 == 0 # binary_operator:Mod
                      # comparison_operator:Eq
                      # divisibility_test:2
                      # int_literal
                      # literal:Num
                      # return
