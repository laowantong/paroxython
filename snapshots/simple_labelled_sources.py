# ----------------------------------------------------------------------------------------
# tests/data/simple/assignment.py
# ----------------------------------------------------------------------------------------
a = b # assignment
      # assignment_lhs_identifier:a
      # assignment_rhs_identifier:b

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
                       # if_test_id:n
                       # int_literal
                       # literal:Num
                       # suggest_conditional_expression (-> +3)
            n = n // 2 # assignment
                       # assignment_lhs_identifier:n
                       # assignment_rhs_identifier:n
                       # if_then_branch
                       # int_literal
                       # suggest_augmented_assignment
        else: # unknown_label
            n = 3 * n + 1 # assignment
                          # assignment_lhs_identifier:n
                          # assignment_rhs_identifier:n
                          # binary_operator:Add
                          # binary_operator:Mult
                          # if_else_branch
                          # int_literal
                          # literal:Num
                          # suggest_constant_definition
    print(n) # call_argument:n
             # function_call:print

# ----------------------------------------------------------------------------------------
# tests/data/simple/function_definition.py
# ----------------------------------------------------------------------------------------
def succ(n): # function:succ (-> +1)
             # function_returning_something:succ (-> +1)
    return a + b + 1 # binary_operator:Add
                     # int_literal
                     # literal:Num
                     # return

# ----------------------------------------------------------------------------------------
# tests/data/simple/loop.py
# ----------------------------------------------------------------------------------------
while input(): # function_call:input
               # while (-> +1)
    print("foobar") # call_argument:
                    # function_call:print
                    # literal:Str
