# ----------------------------------------------------------------------------------------
# assignment.py
# ----------------------------------------------------------------------------------------
a = b # assignment
      # assignment_lhs_identifier:a
      # assignment_rhs_atom:b
      # flat_style
      # global_scope:a
      # imperative_style
      # loaded_variable:b
      # node:Assign
      # node:Name
      # one_liner_style
      # scope:a
      # single_assignment:a
      # variety:1
      # whole_span:1

# ----------------------------------------------------------------------------------------
# collatz.py
# ----------------------------------------------------------------------------------------
def print_collatz(n): # added_block_label (-> +7)
                      # function:print_collatz (-> +7)
                      # function_line_count:8 (-> +7)
                      # function_parameter:n
                      # function_parameter_flavor:arg
                      # function_returning_nothing:print_collatz (-> +7)
                      # local_scope:n (-> +7)
                      # node:FunctionDef (-> +7)
                      # node:arg
                      # procedural_style (-> +7)
                      # scope:n (-> +7)
                      # variety:4 (-> +7)
                      # whole_span:8 (-> +7)
    while n != 1: # comparison_operator:NotEq
                  # literal:1
                  # loaded_variable:n
                  # loop:while (-> +5)
                  # loop_with_late_exit:while (-> +5)
                  # node:Compare
                  # node:Name
                  # node:Num
                  # node:While (-> +5)
                  # suggest_constant_definition
        print(n) # argument:n
                 # external_free_call:print
                 # free_call:print
                 # free_call_without_result:print
                 # loaded_variable:n
                 # node:Call
                 # node:Expr
                 # node:Name
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
                       # loaded_variable:n
                       # modulo_operator
                       # node:BinOp
                       # node:Compare
                       # node:If (-> +3)
                       # node:Name
                       # node:Num
                       # verbose_conditional_assignment (-> +3)
            n = n // 2 # assignment:FloorDiv
                       # assignment_lhs_identifier:n
                       # assignment_rhs_atom:2
                       # assignment_rhs_atom:n
                       # augmented_assignment_unpythonic
                       # if_then_branch
                       # literal:2
                       # loaded_variable:n
                       # node:Assign
                       # node:BinOp
                       # node:Name
                       # node:Num
                       # single_assignment:n
                       # update:n:2
                       # update_by_assignment:n:2
                       # update_by_assignment_with:FloorDiv
                       # update_with:FloorDiv
        else: # unknown_label
            n = 3 * n + 1 # addition_operator
                          # assignment:Add
                          # assignment_lhs_identifier:n
                          # assignment_rhs_atom:1
                          # assignment_rhs_atom:3
                          # assignment_rhs_atom:n
                          # binary_operator:Add
                          # binary_operator:Mult
                          # if_else_branch
                          # literal:1
                          # literal:3
                          # loaded_variable:n
                          # magic_number:3
                          # multiplication_operator
                          # node:Assign
                          # node:BinOp
                          # node:Name
                          # node:Num
                          # single_assignment:n
                          # update:n:1
                          # update:n:3
                          # update_by_assignment:n:1
                          # update_by_assignment:n:3
                          # update_by_assignment_with:Add
                          # update_with:Add
    print(n) # argument:n
             # external_free_call:print
             # free_call:print
             # free_call_without_result:print
             # loaded_variable:n
             # node:Call
             # node:Expr
             # node:Name

# ----------------------------------------------------------------------------------------
# fizzbuzz.py
# ----------------------------------------------------------------------------------------
import collatz # global_scope:i (-> +9)
               # imperative_style (-> +9)
               # import_internally:collatz
               # import_module_internally:collatz
               # node:Import
               # scope:i (-> +9)
               # variety:3 (-> +9)
               # whole_span:10 (-> +9)
for i in range(1, 101): # argument:1
                        # argument:101
                        # external_free_call:range
                        # for:i (-> +8)
                        # for_range:1:101 (-> +8)
                        # free_call:range
                        # iteration_variable:i
                        # literal:1
                        # literal:101
                        # loop:for (-> +8)
                        # loop_with_late_exit:for (-> +8)
                        # magic_number:101
                        # node:Call
                        # node:For (-> +8)
                        # node:Name
                        # node:Num
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
                    # loaded_variable:i
                    # magic_number:15
                    # modulo_operator
                    # node:BinOp
                    # node:Compare
                    # node:If (-> +7)
                    # node:Name
                    # node:Num
        print("FizzBuzz") # argument:
                          # external_free_call:print
                          # free_call:print
                          # free_call_without_result:print
                          # if_then_branch
                          # literal:Str
                          # node:Call
                          # node:Expr
                          # node:Name
                          # node:Str
    elif i % 3 == 0: # binary_operator:Mod
                     # comparison_operator:Eq
                     # divisibility_test:3
                     # if (-> +5)
                     # if_test_atom:0
                     # if_test_atom:3
                     # if_test_atom:i
                     # literal:0
                     # literal:3
                     # loaded_variable:i
                     # magic_number:3
                     # modulo_operator
                     # node:BinOp
                     # node:Compare
                     # node:If (-> +5)
                     # node:Name
                     # node:Num
        print("Fizz") # argument:
                      # external_free_call:print
                      # free_call:print
                      # free_call_without_result:print
                      # if_elif_branch
                      # literal:Str
                      # node:Call
                      # node:Expr
                      # node:Name
                      # node:Str
    elif i % 5 == 0: # binary_operator:Mod
                     # comparison_operator:Eq
                     # divisibility_test:5
                     # if (-> +3)
                     # if_test_atom:0
                     # if_test_atom:5
                     # if_test_atom:i
                     # literal:0
                     # literal:5
                     # loaded_variable:i
                     # magic_number:5
                     # modulo_operator
                     # node:BinOp
                     # node:Compare
                     # node:If (-> +3)
                     # node:Name
                     # node:Num
        print("Buzz") # argument:
                      # external_free_call:print
                      # free_call:print
                      # free_call_without_result:print
                      # if_elif_branch
                      # literal:Str
                      # node:Call
                      # node:Expr
                      # node:Name
                      # node:Str
    else: # 
        print(i) # argument:i
                 # external_free_call:print
                 # free_call:print
                 # free_call_without_result:print
                 # if_else_branch
                 # loaded_variable:i
                 # node:Call
                 # node:Expr
                 # node:Name

# ----------------------------------------------------------------------------------------
# is_even.py
# ----------------------------------------------------------------------------------------
import fizzbuzz # functional_style (-> +2)
                # import_internally:fizzbuzz
                # import_module_internally:fizzbuzz
                # node:Import
                # one_liner_style (-> +2)
                # variety:2 (-> +2)
                # whole_span:3 (-> +2)
def is_even(n): # function:is_even (-> +1)
                # function_line_count:2 (-> +1)
                # function_parameter:n
                # function_parameter_flavor:arg
                # function_returning_something:is_even (-> +1)
                # local_scope:n (-> +1)
                # node:FunctionDef (-> +1)
                # node:arg
                # pure_function:is_even (-> +1)
                # scope:n (-> +1)
    return n % 2 == 0 # binary_operator:Mod
                      # comparison_operator:Eq
                      # divisibility_test:2
                      # literal:0
                      # literal:2
                      # loaded_variable:n
                      # modulo_operator
                      # node:BinOp
                      # node:Compare
                      # node:Name
                      # node:Num
                      # node:Return
                      # return
