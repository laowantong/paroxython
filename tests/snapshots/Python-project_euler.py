# ----------------------------------------------------------------------------------------
# problem_01/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return sum([e for e in range(3, n) if e % 3 == 0 or e % 5 == 0]) # binary_operator:Mod, boolean_operator:Or, call_argument:, call_argument:3, call_argument:n, comparison_operator:Eq, composition, comprehension:List, comprehension_for_count:1, divisibility_test:3, divisibility_test:5, filtered_comprehension, function_call:range, function_call:sum, function_tail_call:sum, literal:0, literal:3, literal:5, modulo_operator, range:3:n, return, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# problem_01/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +8)
    sum = 0 # assignment:0, assignment_lhs_identifier:sum, assignment_rhs_atom:0, literal:0, single_assignment:sum
    terms = (n - 1) // 3 # assignment:FloorDiv, assignment_lhs_identifier:terms, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:n, binary_operator:FloorDiv, binary_operator:Sub, literal:1, literal:3, single_assignment:terms, suggest_constant_definition
    sum += ((terms) * (6 + (terms - 1) * 3)) // 2 # addition_operator, assignment_lhs_identifier:sum, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:6, assignment_rhs_atom:terms, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, literal:1, literal:2, literal:3, literal:6, multiplication_operator, suggest_constant_definition, update:sum:1, update:sum:2, update:sum:3, update:sum:6, update:sum:terms, update_by_augmented_assignment:sum:1, update_by_augmented_assignment:sum:2, update_by_augmented_assignment:sum:3, update_by_augmented_assignment:sum:6, update_by_augmented_assignment:sum:terms, update_by_augmented_assignment_with:Add, update_with:Add
    terms = (n - 1) // 5 # assignment:FloorDiv, assignment_lhs_identifier:terms, assignment_rhs_atom:1, assignment_rhs_atom:5, assignment_rhs_atom:n, binary_operator:FloorDiv, binary_operator:Sub, literal:1, literal:5, single_assignment:terms, suggest_constant_definition
    sum += ((terms) * (10 + (terms - 1) * 5)) // 2 # addition_operator, assignment_lhs_identifier:sum, assignment_rhs_atom:1, assignment_rhs_atom:10, assignment_rhs_atom:2, assignment_rhs_atom:5, assignment_rhs_atom:terms, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, literal:1, literal:10, literal:2, literal:5, multiplication_operator, suggest_constant_definition, update:sum:1, update:sum:10, update:sum:2, update:sum:5, update:sum:terms, update_by_augmented_assignment:sum:1, update_by_augmented_assignment:sum:10, update_by_augmented_assignment:sum:2, update_by_augmented_assignment:sum:5, update_by_augmented_assignment:sum:terms, update_by_augmented_assignment_with:Add, update_with:Add
    terms = (n - 1) // 15 # assignment:FloorDiv, assignment_lhs_identifier:terms, assignment_rhs_atom:1, assignment_rhs_atom:15, assignment_rhs_atom:n, binary_operator:FloorDiv, binary_operator:Sub, literal:1, literal:15, single_assignment:terms, suggest_constant_definition
    sum -= ((terms) * (30 + (terms - 1) * 15)) // 2 # addition_operator, assignment_lhs_identifier:sum, assignment_rhs_atom:1, assignment_rhs_atom:15, assignment_rhs_atom:2, assignment_rhs_atom:30, assignment_rhs_atom:terms, augmented_assignment:Sub, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, literal:1, literal:15, literal:2, literal:30, multiplication_operator, suggest_constant_definition, update:sum:1, update:sum:15, update:sum:2, update:sum:30, update:sum:terms, update_by_augmented_assignment:sum:1, update_by_augmented_assignment:sum:15, update_by_augmented_assignment:sum:2, update_by_augmented_assignment:sum:30, update_by_augmented_assignment:sum:terms, update_by_augmented_assignment_with:Sub, update_with:Sub
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# problem_01/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +32), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +32)
    sum = 0 # assignment:0, assignment_lhs_identifier:sum, assignment_rhs_atom:0, literal:0, single_assignment:sum
    num = 0 # assignment:0, assignment_lhs_identifier:num, assignment_rhs_atom:0, literal:0, single_assignment:num
    while 1: # infinite_while (-> +28), literal:1, loop:while (-> +28), loop_with_early_exit:while:break (-> +28), while (-> +28)
        num += 3 # assignment_lhs_identifier:num, assignment_rhs_atom:3, augmented_assignment:Add, literal:3, suggest_constant_definition, update:num:3, update_by_augmented_assignment:num:3, update_by_augmented_assignment_with:Add, update_with:Add
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num, if_without_else (-> +1)
            break # break, if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, update:sum:num, update_by_augmented_assignment:sum:num, update_by_augmented_assignment_with:Add, update_with:Add
        num += 2 # assignment_lhs_identifier:num, assignment_rhs_atom:2, augmented_assignment:Add, literal:2, update:num:2, update_by_augmented_assignment:num:2, update_by_augmented_assignment_with:Add, update_with:Add
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num, if_without_else (-> +1)
            break # break, if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, update:sum:num, update_by_augmented_assignment:sum:num, update_by_augmented_assignment_with:Add, update_with:Add
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment:num, literal:1, update:num:1, update_by_augmented_assignment:num:1, update_by_augmented_assignment_with:Add, update_with:Add
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num, if_without_else (-> +1)
            break # break, if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, update:sum:num, update_by_augmented_assignment:sum:num, update_by_augmented_assignment_with:Add, update_with:Add
        num += 3 # assignment_lhs_identifier:num, assignment_rhs_atom:3, augmented_assignment:Add, literal:3, suggest_constant_definition, update:num:3, update_by_augmented_assignment:num:3, update_by_augmented_assignment_with:Add, update_with:Add
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num, if_without_else (-> +1)
            break # break, if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, update:sum:num, update_by_augmented_assignment:sum:num, update_by_augmented_assignment_with:Add, update_with:Add
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment:num, literal:1, update:num:1, update_by_augmented_assignment:num:1, update_by_augmented_assignment_with:Add, update_with:Add
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num, if_without_else (-> +1)
            break # break, if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, update:sum:num, update_by_augmented_assignment:sum:num, update_by_augmented_assignment_with:Add, update_with:Add
        num += 2 # assignment_lhs_identifier:num, assignment_rhs_atom:2, augmented_assignment:Add, literal:2, update:num:2, update_by_augmented_assignment:num:2, update_by_augmented_assignment_with:Add, update_with:Add
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num, if_without_else (-> +1)
            break # break, if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, update:sum:num, update_by_augmented_assignment:sum:num, update_by_augmented_assignment_with:Add, update_with:Add
        num += 3 # assignment_lhs_identifier:num, assignment_rhs_atom:3, augmented_assignment:Add, literal:3, suggest_constant_definition, update:num:3, update_by_augmented_assignment:num:3, update_by_augmented_assignment_with:Add, update_with:Add
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num, if_without_else (-> +1)
            break # break, if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, update:sum:num, update_by_augmented_assignment:sum:num, update_by_augmented_assignment_with:Add, update_with:Add
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# problem_01/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +22), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +22)
    xmulti = [] # assignment, assignment_lhs_identifier:xmulti, empty_literal:List, literal:List, single_assignment:xmulti
    zmulti = [] # assignment, assignment_lhs_identifier:zmulti, empty_literal:List, literal:List, single_assignment:zmulti
    z = 3 # assignment:3, assignment_lhs_identifier:z, assignment_rhs_atom:3, literal:3, single_assignment:z, suggest_constant_definition
    x = 5 # assignment:5, assignment_lhs_identifier:x, assignment_rhs_atom:5, literal:5, single_assignment:x, suggest_constant_definition
    temp = 1 # assignment:1, assignment_lhs_identifier:temp, assignment_rhs_atom:1, literal:1, single_assignment:temp
    while True: # infinite_while (-> +7), literal:True, loop:while (-> +7), loop_with_early_exit:while:break (-> +7), while (-> +7)
        result = z * temp # assignment:Mult, assignment_lhs_identifier:result, assignment_rhs_atom:temp, assignment_rhs_atom:z, binary_operator:Mult, multiplication_operator, single_assignment:result
        if result < n: # comparison_operator:Lt, if (-> +5), if_test_atom:n, if_test_atom:result
            zmulti.append(result) # call_argument:result, if_then_branch (-> +1), method_call:append, method_call_object:zmulti, method_call_without_result:append, update:zmulti:result, update_by_method_call:zmulti:result, update_by_method_call_with:append, update_with:append
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, increment:temp, literal:1, update:temp:1, update_by_augmented_assignment:temp:1, update_by_augmented_assignment_with:Add, update_with:Add
        else:
            temp = 1 # assignment:1, assignment_lhs_identifier:temp, assignment_rhs_atom:1, if_else_branch (-> +1), literal:1, single_assignment:temp
            break # break
    while True: # count_states:temp (-> +6), infinite_while (-> +6), literal:True, loop:while (-> +6), loop_with_early_exit:while:break (-> +6), while (-> +6)
        result = x * temp # assignment:Mult, assignment_lhs_identifier:result, assignment_rhs_atom:temp, assignment_rhs_atom:x, binary_operator:Mult, multiplication_operator, single_assignment:result
        if result < n: # comparison_operator:Lt, if (-> +4), if_test_atom:n, if_test_atom:result
            xmulti.append(result) # call_argument:result, if_then_branch (-> +1), method_call:append, method_call_object:xmulti, method_call_without_result:append, update:xmulti:result, update_by_method_call:xmulti:result, update_by_method_call_with:append, update_with:append
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, increment:temp, literal:1, update:temp:1, update_by_augmented_assignment:temp:1, update_by_augmented_assignment_with:Add, update_with:Add
        else:
            break # break, if_else_branch
    collection = list(set(xmulti + zmulti)) # addition_operator, assignment:list, assignment_lhs_identifier:collection, assignment_rhs_atom:xmulti, assignment_rhs_atom:zmulti, binary_operator:Add, call_argument:, composition, function_call:list, function_call:set, single_assignment:collection
    return sum(collection) # call_argument:collection, function_call:sum, function_tail_call:sum, return

# ----------------------------------------------------------------------------------------
# problem_01/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0]) # binary_operator:Mod, boolean_operator:Or, call_argument:, call_argument:n, comparison_operator:Eq, composition, comprehension:List, comprehension_for_count:1, divisibility_test:3, divisibility_test:5, filtered_comprehension, function_call:range, function_call:sum, function_tail_call:sum, literal:0, literal:3, literal:5, modulo_operator, range:n, return, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# problem_01/sol6.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +9), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +9)
    a = 3 # assignment:3, assignment_lhs_identifier:a, assignment_rhs_atom:3, literal:3, single_assignment:a, suggest_constant_definition
    result = 0 # assignment:0, assignment_lhs_identifier:result, assignment_rhs_atom:0, literal:0, single_assignment:result
    while a < n: # comparison_operator:Lt, count_states:a (-> +5), loop:while (-> +5), while (-> +5)
        if a % 3 == 0 or a % 5 == 0: # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, divisibility_test:3, divisibility_test:5, if (-> +3), if_test_atom:0, if_test_atom:3, if_test_atom:5, if_test_atom:a, literal:0, literal:3, literal:5, modulo_operator, suggest_constant_definition
            result += a # assignment_lhs_identifier:result, assignment_rhs_atom:a, augmented_assignment:Add, if_then_branch, update:result:a, update_by_augmented_assignment:result:a, update_by_augmented_assignment_with:Add, update_with:Add
        elif a % 15 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:15, if (-> +1), if_test_atom:0, if_test_atom:15, if_test_atom:a, literal:0, literal:15, modulo_operator, suggest_constant_definition
            result -= a # assignment_lhs_identifier:result, assignment_rhs_atom:a, augmented_assignment:Sub, if_elif_branch, update:result:a, update_by_augmented_assignment:result:a, update_by_augmented_assignment_with:Sub, update_with:Sub
        a += 1 # assignment_lhs_identifier:a, assignment_rhs_atom:1, augmented_assignment:Add, increment:a, literal:1, update:a:1, update_by_augmented_assignment:a:1, update_by_augmented_assignment_with:Add, update_with:Add
    return result # return:result

# ----------------------------------------------------------------------------------------
# problem_01/sol7.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +7)
    result = 0 # assignment:0, assignment_lhs_identifier:result, assignment_rhs_atom:0, literal:0, single_assignment:result
    for i in range(n): # accumulate_elements:Add (-> +4), accumulate_some_elements:Add (-> +4), call_argument:n, for:i (-> +4), for_range:n (-> +4), function_call:range, loop:for (-> +4), range:n
        if i % 3 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:3, if (-> +3), if_test_atom:0, if_test_atom:3, if_test_atom:i, literal:0, literal:3, modulo_operator, suggest_constant_definition
            result += i # assignment_lhs_identifier:result, assignment_rhs_atom:i, augmented_assignment:Add, if_then_branch, update:result:i, update_by_augmented_assignment:result:i, update_by_augmented_assignment_with:Add, update_with:Add
        elif i % 5 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:5, if (-> +1), if_test_atom:0, if_test_atom:5, if_test_atom:i, literal:0, literal:5, modulo_operator, suggest_constant_definition
            result += i # assignment_lhs_identifier:result, assignment_rhs_atom:i, augmented_assignment:Add, if_elif_branch, update:result:i, update_by_augmented_assignment:result:i, update_by_augmented_assignment_with:Add, update_with:Add
    return result # return:result

# ----------------------------------------------------------------------------------------
# problem_02/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +8)
    i = 1 # assignment:1, assignment_lhs_identifier:i, assignment_rhs_atom:1, literal:1, single_assignment:i
    j = 2 # assignment:2, assignment_lhs_identifier:j, assignment_rhs_atom:2, literal:2, single_assignment:j
    sum = 0 # assignment:0, assignment_lhs_identifier:sum, assignment_rhs_atom:0, literal:0, single_assignment:sum
    while j <= n: # comparison_operator:LtE, loop:while (-> +3), while (-> +3)
        if j % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:j, if_without_else (-> +1), literal:0, literal:2, modulo_operator
            sum += j # assignment_lhs_identifier:sum, assignment_rhs_atom:j, augmented_assignment:Add, if_then_branch, update:sum:j, update_by_augmented_assignment:sum:j, update_by_augmented_assignment_with:Add, update_with:Add
        i, j = j, i + j # addition_operator, assignment, assignment_lhs_identifier:i, assignment_lhs_identifier:j, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, parallel_assignment:2, slide, update:i:j, update:j:i, update_by_assignment:i:j, update_by_assignment:j:i, update_by_assignment_with, update_with
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# problem_02/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +7)
    ls = [] # assignment, assignment_lhs_identifier:ls, empty_literal:List, literal:List, single_assignment:ls
    a, b = 0, 1 # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:0, assignment_rhs_atom:1, literal:0, literal:1, literal:Tuple, parallel_assignment:2
    while b <= n: # comparison_operator:LtE, loop:while (-> +3), while (-> +3)
        if b % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:b, if_without_else (-> +1), literal:0, literal:2, modulo_operator
            ls.append(b) # call_argument:b, if_then_branch, method_call:append, method_call_object:ls, method_call_without_result:append, update:ls:b, update_by_method_call:ls:b, update_by_method_call_with:append, update_with:append
        a, b = b, a + b # addition_operator, assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, parallel_assignment:2, slide, update:a:b, update:b:a, update_by_assignment:a:b, update_by_assignment:b:a, update_by_assignment_with, update_with
    return ls # return:ls

# ----------------------------------------------------------------------------------------
# problem_02/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +9), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +9)
    if n <= 1: # comparison_operator:LtE, if (-> +1), if_guard (-> +1), if_test_atom:1, if_test_atom:n, if_without_else (-> +1), literal:1
        return 0 # if_then_branch, literal:0, return:0
    a = 0 # assignment:0, assignment_lhs_identifier:a, assignment_rhs_atom:0, literal:0, single_assignment:a
    b = 2 # assignment:2, assignment_lhs_identifier:b, assignment_rhs_atom:2, literal:2, single_assignment:b
    count = 0 # assignment:0, assignment_lhs_identifier:count, assignment_rhs_atom:0, literal:0, single_assignment:count
    while 4 * b + a <= n: # addition_operator, binary_operator:Add, binary_operator:Mult, comparison_operator:LtE, literal:4, loop:while (-> +2), multiplication_operator, suggest_constant_definition, while (-> +2)
        a, b = b, 4 * b + a # addition_operator, assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:4, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, binary_operator:Mult, literal:4, multiplication_operator, parallel_assignment:2, slide, suggest_constant_definition, update:a:4, update:a:b, update:b:4, update:b:a, update_by_assignment:a:4, update_by_assignment:a:b, update_by_assignment:b:4, update_by_assignment:b:a, update_by_assignment_with, update_with
        count += a # assignment_lhs_identifier:count, assignment_rhs_atom:a, augmented_assignment:Add, update:count:a, update_by_augmented_assignment:count:a, update_by_augmented_assignment_with:Add, update_with:Add
    return count + b # addition_operator, binary_operator:Add, return

# ----------------------------------------------------------------------------------------
# problem_02/sol4.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
from decimal import Decimal, getcontext # import:decimal:Decimal, import:decimal:getcontext, import_module:decimal, import_name:Decimal, import_name:getcontext
def solution(n): # function:solution (-> +12), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +12)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int, single_assignment:n
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    getcontext().prec = 100 # assignment:100, assignment_rhs_atom:100, function_call:getcontext, function_call_without_arguments:getcontext, literal:100, suggest_constant_definition
    phi = (Decimal(5) ** Decimal(0.5) + 1) / Decimal(2) # addition_operator, assignment:Div, assignment_lhs_identifier:phi, assignment_rhs_atom:0.5, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:5, binary_operator:Add, binary_operator:Div, binary_operator:Pow, call_argument:0.5, call_argument:2, call_argument:5, function_call:Decimal, literal:0.5, literal:1, literal:2, literal:5, single_assignment:phi, suggest_constant_definition
    index = (math.floor(math.log(n * (phi + 2), phi) - 1) // 3) * 3 + 2 # addition_operator, assignment:Add, assignment_lhs_identifier:index, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:math, assignment_rhs_atom:n, assignment_rhs_atom:phi, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:phi, composition, literal:1, literal:2, literal:3, method_call:floor, method_call:log, multiplication_operator, single_assignment:index, suggest_constant_definition
    num = Decimal(round(phi ** Decimal(index + 1))) / (phi + 2) # addition_operator, assignment:Div, assignment_lhs_identifier:num, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:index, assignment_rhs_atom:phi, binary_operator:Add, binary_operator:Div, binary_operator:Pow, call_argument:, composition, function_call:Decimal, function_call:round, literal:1, literal:2, single_assignment:num
    sum = num // 2 # assignment:FloorDiv, assignment_lhs_identifier:sum, assignment_rhs_atom:2, assignment_rhs_atom:num, binary_operator:FloorDiv, literal:2, single_assignment:sum
    return int(sum) # call_argument:sum, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# problem_02/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +12), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +12)
    a = [0, 1] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, assignment_rhs_atom:1, literal:0, literal:1, literal:List, single_assignment:a
    i = 0 # assignment:0, assignment_lhs_identifier:i, assignment_rhs_atom:0, literal:0, single_assignment:i
    while a[i] <= n: # comparison_operator:LtE, count_states:i (-> +4), index:i, loop:while (-> +4), loop_with_early_exit:while:break (-> +4), while (-> +4)
        a.append(a[i] + a[i + 1]) # addition_operator, binary_operator:Add, call_argument:, index:_, index:i, index_arithmetic, literal:1, method_call:append, method_call_object:a, method_call_without_result:append
        if a[i + 2] > n: # addition_operator, binary_operator:Add, comparison_operator:Gt, if (-> +1), if_test_atom:2, if_test_atom:a, if_test_atom:i, if_test_atom:n, if_without_else (-> +1), index:_, index_arithmetic, literal:2
            break # break, if_then_branch
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
    sum = 0 # assignment:0, assignment_lhs_identifier:sum, assignment_rhs_atom:0, literal:0, single_assignment:sum
    for j in range(len(a) - 1): # accumulate_elements:Add (-> +2), accumulate_some_elements:Add (-> +2), binary_operator:Sub, call_argument:, call_argument:a, composition, for:j (-> +2), for_range:_ (-> +2), function_call:len, function_call:range, literal:1, loop:for (-> +2), range:_
        if a[j] % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:a, if_test_atom:j, if_without_else (-> +1), index:j, literal:0, literal:2, modulo_operator
            sum += a[j] # assignment_lhs_identifier:sum, assignment_rhs_atom:a, assignment_rhs_atom:j, augmented_assignment:Add, if_then_branch, index:j, update:sum:a, update:sum:j, update_by_augmented_assignment:sum:a, update_by_augmented_assignment:sum:j, update_by_augmented_assignment_with:Add, update_with:Add
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# problem_03/sol1.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def isprime(no): # function:isprime (-> +9), function_argument:no, function_argument_flavor:arg, function_returning_something:isprime (-> +9)
    if no == 2: # comparison_operator:Eq, if (-> +3), if_test_atom:2, if_test_atom:no, literal:2
        return True # if_then_branch, literal:True, return:True
    elif no % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:no, literal:0, literal:2, modulo_operator
        return False # if_elif_branch, literal:False, return:False
    sq = int(math.sqrt(no)) + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:sq, assignment_rhs_atom:1, assignment_rhs_atom:math, assignment_rhs_atom:no, binary_operator:Add, call_argument:, call_argument:no, composition, function_call:int, literal:1, method_call:sqrt, single_assignment:sq
    for i in range(3, sq, 2): # call_argument:2, call_argument:3, call_argument:sq, for:i (-> +2), for_range:3:sq:2 (-> +2), function_call:range, literal:2, literal:3, loop:for (-> +2), loop_with_early_exit:for:return (-> +2), range:3:sq:2, suggest_constant_definition, universal_quantification:i (-> +2)
        if no % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:no, if_without_else (-> +1), literal:0, modulo_operator
            return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def solution(n): # function:solution (-> +24), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +24)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int, single_assignment:n
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    maxNumber = 0 # assignment:0, assignment_lhs_identifier:maxNumber, assignment_rhs_atom:0, literal:0, single_assignment:maxNumber
    if isprime(n): # call_argument:n, function_call:isprime, if (-> +16), if_test_atom:n
        return n # if_then_branch, return:n
    else:
        while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if_else_branch (-> +13), literal:0, literal:2, loop:while (-> +1), modulo_operator, while (-> +1)
            n = n / 2 # assignment:Div, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, literal:2, single_assignment:n, suggest_augmented_assignment, update:n:2, update_by_assignment:n:2, update_by_assignment_with:Div, update_with:Div
        if isprime(n): # call_argument:n, function_call:isprime, if (-> +11), if_test_atom:n, nested_if:1 (-> +11)
            return int(n) # call_argument:n, function_call:int, function_tail_call:int, if_then_branch, return
        else:
            n1 = int(math.sqrt(n)) + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:n1, assignment_rhs_atom:1, assignment_rhs_atom:math, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:n, composition, function_call:int, if_else_branch (-> +8), literal:1, method_call:sqrt, single_assignment:n1
            for i in range(3, n1, 2): # call_argument:2, call_argument:3, call_argument:n1, for:i (-> +6), for_range:3:n1:2 (-> +6), function_call:range, literal:2, literal:3, loop:for (-> +6), loop_with_early_exit:for:break (-> +6), range:3:n1:2, suggest_constant_definition
                if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +5), if_test_atom:0, if_test_atom:i, if_test_atom:n, if_without_else (-> +5), literal:0, modulo_operator, nested_if:2 (-> +5)
                    if isprime(n / i): # binary_operator:Div, call_argument:, function_call:isprime, if (-> +4), if_test_atom:i, if_test_atom:n, if_then_branch (-> +4), nested_if:3 (-> +4)
                        maxNumber = n / i # assignment:Div, assignment_lhs_identifier:maxNumber, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, if_then_branch (-> +1), single_assignment:maxNumber
                        break # break
                    elif isprime(i): # call_argument:i, function_call:isprime, if (-> +1), if_test_atom:i, nested_if:3 (-> +1)
                        maxNumber = i # assignment, assignment_lhs_identifier:maxNumber, assignment_rhs_atom:i, if_elif_branch, single_assignment:maxNumber
            return maxNumber # return:maxNumber

# ----------------------------------------------------------------------------------------
# problem_03/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +16), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +16)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int, single_assignment:n
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    prime = 1 # assignment:1, assignment_lhs_identifier:prime, assignment_rhs_atom:1, literal:1, single_assignment:prime
    i = 2 # assignment:2, assignment_lhs_identifier:i, assignment_rhs_atom:2, literal:2, single_assignment:i
    while i * i <= n: # binary_operator:Mult, comparison_operator:LtE, count_states:i (-> +4), loop:while (-> +4), multiplication_operator, while (-> +4)
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, literal:0, loop:while (-> +2), modulo_operator, while (-> +2)
            prime = i # assignment, assignment_lhs_identifier:prime, assignment_rhs_atom:i, single_assignment:prime
            n //= i # assignment_lhs_identifier:n, assignment_rhs_atom:i, augmented_assignment:FloorDiv, update:n:i, update_by_augmented_assignment:n:i, update_by_augmented_assignment_with:FloorDiv, update_with:FloorDiv
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
    if n > 1: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:n, if_without_else (-> +1), literal:1
        prime = n # assignment, assignment_lhs_identifier:prime, assignment_rhs_atom:n, if_then_branch, single_assignment:prime
    return int(prime) # call_argument:prime, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# problem_03/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n: int) -> int: # function:solution (-> +18), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +18)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int, single_assignment:n
    except (TypeError, ValueError): # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    i = 2 # assignment:2, assignment_lhs_identifier:i, assignment_rhs_atom:2, literal:2, single_assignment:i
    ans = 0 # assignment:0, assignment_lhs_identifier:ans, assignment_rhs_atom:0, literal:0, single_assignment:ans
    if n == 2: # comparison_operator:Eq, if (-> +1), if_guard (-> +1), if_test_atom:2, if_test_atom:n, if_without_else (-> +1), literal:2
        return 2 # if_then_branch, literal:2, return:2
    while n > 2: # comparison_operator:Gt, literal:2, loop:while (-> +6), while (-> +6)
        while n % i != 0: # binary_operator:Mod, comparison_operator:NotEq, count_states:i (-> +1), divisibility_test, literal:0, loop:while (-> +1), modulo_operator, while (-> +1)
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
        ans = i # assignment, assignment_lhs_identifier:ans, assignment_rhs_atom:i, single_assignment:ans
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, literal:0, loop:while (-> +1), modulo_operator, while (-> +1)
            n = n / i # assignment:Div, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, single_assignment:n, suggest_augmented_assignment, update:n:i, update_by_assignment:n:i, update_by_assignment_with:Div, update_with:Div
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
    return int(ans) # call_argument:ans, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# problem_04/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +8)
    for number in range(n - 1, 10000, -1): # binary_operator:Sub, call_argument:, call_argument:-1, call_argument:10000, find_first_element:number (-> +7), for:number (-> +7), for_range:_:10000:-1 (-> +7), function_call:range, literal:-1, literal:1, literal:10000, loop:for (-> +7), range:_:10000:-1, suggest_constant_definition
        strNumber = str(number) # assignment:str, assignment_lhs_identifier:strNumber, assignment_rhs_atom:number, call_argument:number, function_call:str, single_assignment:strNumber
        if strNumber == strNumber[::-1]: # comparison_operator:Eq, if (-> +5), if_test_atom:-1, if_test_atom:strNumber, if_without_else (-> +5), literal:-1, slice:::-1, slice_lower:, slice_step:-1, slice_upper:
            divisor = 999 # assignment:999, assignment_lhs_identifier:divisor, assignment_rhs_atom:999, if_then_branch (-> +4), literal:999, single_assignment:divisor, suggest_constant_definition
            while divisor != 99: # comparison_operator:NotEq, literal:99, loop:while (-> +3), loop_with_early_exit:while:return (-> +3), suggest_constant_definition, while (-> +3)
                if (number % divisor == 0) and (len(str(int(number / divisor))) == 3): # binary_operator:Div, binary_operator:Mod, boolean_operator:And, call_argument:, comparison_operator:Eq, composition, divisibility_test, function_call:int, function_call:len, function_call:str, if (-> +1), if_test_atom:0, if_test_atom:3, if_test_atom:divisor, if_test_atom:number, if_without_else (-> +1), literal:0, literal:3, modulo_operator, nested_if:1 (-> +1), suggest_constant_definition
                    return number # if_then_branch, return:number
                divisor -= 1 # assignment_lhs_identifier:divisor, assignment_rhs_atom:1, augmented_assignment:Sub, literal:1, update:divisor:1, update_by_augmented_assignment:divisor:1, update_by_augmented_assignment_with:Sub, update_with:Sub

# ----------------------------------------------------------------------------------------
# problem_04/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +7)
    answer = 0 # assignment:0, assignment_lhs_identifier:answer, assignment_rhs_atom:0, literal:0, single_assignment:answer
    for i in range(999, 99, -1): # accumulate_elements:max (-> +4), accumulate_some_elements:max (-> +4), call_argument:-1, call_argument:99, call_argument:999, for:i (-> +4), for_range:999:99:-1 (-> +4), function_call:range, literal:-1, literal:99, literal:999, loop:for (-> +4), range:999:99:-1, square_nested_for (-> +4), suggest_constant_definition
        for j in range(999, 99, -1): # accumulate_all_elements:max (-> +3), accumulate_elements:max (-> +3), call_argument:-1, call_argument:99, call_argument:999, for:j (-> +3), for_range:999:99:-1 (-> +3), function_call:range, literal:-1, literal:99, literal:999, loop:for (-> +3), nested_for:1 (-> +3), range:999:99:-1, suggest_constant_definition
            t = str(i * j) # assignment:str, assignment_lhs_identifier:t, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Mult, call_argument:, function_call:str, multiplication_operator, single_assignment:t
            if t == t[::-1] and i * j < n: # binary_operator:Mult, boolean_operator:And, comparison_operator:Eq, comparison_operator:Lt, if (-> +1), if_test_atom:-1, if_test_atom:i, if_test_atom:j, if_test_atom:n, if_test_atom:t, if_without_else (-> +1), literal:-1, multiplication_operator, slice:::-1, slice_lower:, slice_step:-1, slice_upper:
                answer = max(answer, i * j) # assignment:max, assignment_lhs_identifier:answer, assignment_rhs_atom:answer, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Mult, call_argument:, call_argument:answer, function_call:max, if_then_branch, multiplication_operator, single_assignment:answer, update:answer:i, update:answer:j, update_by_assignment:answer:i, update_by_assignment:answer:j, update_by_assignment_with:max, update_with:max
    return answer # return:answer

# ----------------------------------------------------------------------------------------
# problem_05/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +18), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +18)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int, single_assignment:n
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    i = 0 # assignment:0, assignment_lhs_identifier:i, assignment_rhs_atom:0, literal:0, single_assignment:i
    while 1: # infinite_while (-> +10), literal:1, loop:while (-> +10), loop_with_early_exit:while:return (-> +10), while (-> +10)
        i += n * (n - 1) # assignment_lhs_identifier:i, assignment_rhs_atom:1, assignment_rhs_atom:n, augmented_assignment:Add, binary_operator:Mult, binary_operator:Sub, literal:1, multiplication_operator, update:i:1, update:i:n, update_by_augmented_assignment:i:1, update_by_augmented_assignment:i:n, update_by_augmented_assignment_with:Add, update_with:Add
        nfound = 0 # assignment:0, assignment_lhs_identifier:nfound, assignment_rhs_atom:0, literal:0, single_assignment:nfound
        for j in range(2, n): # call_argument:2, call_argument:n, for:j (-> +3), for_range:2:n (-> +3), function_call:range, literal:2, loop:for (-> +3), loop_with_early_exit:for:break (-> +3), range:2:n
            if i % j != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test, if (-> +2), if_test_atom:0, if_test_atom:i, if_test_atom:j, if_without_else (-> +2), literal:0, modulo_operator
                nfound = 1 # assignment:1, assignment_lhs_identifier:nfound, assignment_rhs_atom:1, if_then_branch (-> +1), literal:1, single_assignment:nfound
                break # break
        if nfound == 0: # comparison_operator:Eq, if (-> +3), if_test_atom:0, if_test_atom:nfound, if_without_else (-> +3), literal:0
            if i == 0: # comparison_operator:Eq, if (-> +1), if_test_atom:0, if_test_atom:i, if_then_branch (-> +2), if_without_else (-> +1), literal:0, nested_if:1 (-> +1)
                i = 1 # assignment:1, assignment_lhs_identifier:i, assignment_rhs_atom:1, if_then_branch, literal:1, single_assignment:i
            return i # return:i

# ----------------------------------------------------------------------------------------
# problem_05/sol2.py
# ----------------------------------------------------------------------------------------
def gcd(x, y): # function:gcd (-> +1), function_argument:x, function_argument:y, function_argument_flavor:arg, function_returning_something:gcd (-> +1), recursive_function:gcd (-> +1), tail_recursive_function:gcd (-> +1)
    return x if y == 0 else gcd(y, x % y) # binary_operator:Mod, call_argument:, call_argument:y, comparison_operator:Eq, conditional_expression, function_call:gcd, function_tail_call:gcd, literal:0, modulo_operator, return
def lcm(x, y): # function:lcm (-> +1), function_argument:x, function_argument:y, function_argument_flavor:arg, function_returning_something:lcm (-> +1)
    return (x * y) // gcd(x, y) # binary_operator:FloorDiv, binary_operator:Mult, call_argument:x, call_argument:y, function_call:gcd, multiplication_operator, return
def solution(n): # function:solution (-> +4), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +4)
    g = 1 # assignment:1, assignment_lhs_identifier:g, assignment_rhs_atom:1, literal:1, single_assignment:g
    for i in range(1, n + 1): # accumulate_all_elements:lcm (-> +1), accumulate_elements:lcm (-> +1), addition_operator, binary_operator:Add, call_argument:, call_argument:1, for:i (-> +1), for_range:1:_ (-> +1), function_call:range, literal:1, loop:for (-> +1), range:1:_
        g = lcm(g, i) # assignment:lcm, assignment_lhs_identifier:g, assignment_rhs_atom:g, assignment_rhs_atom:i, call_argument:g, call_argument:i, function_call:lcm, single_assignment:g, update:g:i, update_by_assignment:g:i, update_by_assignment_with:lcm, update_with:lcm
    return g # return:g

# ----------------------------------------------------------------------------------------
# problem_06/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +7)
    suma = 0 # assignment:0, assignment_lhs_identifier:suma, assignment_rhs_atom:0, literal:0, single_assignment:suma
    sumb = 0 # assignment:0, assignment_lhs_identifier:sumb, assignment_rhs_atom:0, literal:0, single_assignment:sumb
    for i in range(1, n + 1): # accumulate_all_elements:Add (-> +2), accumulate_elements:Add (-> +2), addition_operator, binary_operator:Add, call_argument:, call_argument:1, for:i (-> +2), for_range:1:_ (-> +2), function_call:range, literal:1, loop:for (-> +2), range:1:_
        suma += i ** 2 # assignment_lhs_identifier:suma, assignment_rhs_atom:2, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Pow, literal:2, update:suma:2, update:suma:i, update_by_augmented_assignment:suma:2, update_by_augmented_assignment:suma:i, update_by_augmented_assignment_with:Add, update_with:Add
        sumb += i # assignment_lhs_identifier:sumb, assignment_rhs_atom:i, augmented_assignment:Add, update:sumb:i, update_by_augmented_assignment:sumb:i, update_by_augmented_assignment_with:Add, update_with:Add
    sum = sumb ** 2 - suma # assignment:Sub, assignment_lhs_identifier:sum, assignment_rhs_atom:2, assignment_rhs_atom:suma, assignment_rhs_atom:sumb, binary_operator:Pow, binary_operator:Sub, literal:2, single_assignment:sum
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# problem_06/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +4), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +4)
    suma = n * (n + 1) / 2 # addition_operator, assignment:Div, assignment_lhs_identifier:suma, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, literal:1, literal:2, multiplication_operator, single_assignment:suma
    suma **= 2 # assignment_lhs_identifier:suma, assignment_rhs_atom:2, augmented_assignment:Pow, literal:2, update:suma:2, update_by_augmented_assignment:suma:2, update_by_augmented_assignment_with:Pow, update_with:Pow
    sumb = n * (n + 1) * (2 * n + 1) / 6 # addition_operator, assignment:Div, assignment_lhs_identifier:sumb, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, literal:1, literal:2, literal:6, multiplication_operator, single_assignment:sumb, suggest_constant_definition
    return int(suma - sumb) # binary_operator:Sub, call_argument:, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# problem_06/sol3.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def solution(n): # function:solution (-> +3), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +3)
    sum_of_squares = sum([i * i for i in range(1, n + 1)]) # addition_operator, assignment:sum, assignment_lhs_identifier:sum_of_squares, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:1, composition, comprehension:List, comprehension_for_count:1, function_call:range, function_call:sum, literal:1, multiplication_operator, range:1:_, single_assignment:sum_of_squares
    square_of_sum = int(math.pow(sum(range(1, n + 1)), 2)) # addition_operator, assignment:int, assignment_lhs_identifier:square_of_sum, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:math, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:1, call_argument:2, composition, function_call:int, function_call:range, function_call:sum, literal:1, literal:2, method_call:pow, range:1:_, single_assignment:square_of_sum
    return square_of_sum - sum_of_squares # binary_operator:Sub, return

# ----------------------------------------------------------------------------------------
# problem_06/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +3), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +3)
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6 # addition_operator, assignment:Div, assignment_lhs_identifier:sum_of_squares, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, literal:1, literal:2, literal:6, multiplication_operator, single_assignment:sum_of_squares, suggest_constant_definition
    square_of_sum = (n * (n + 1) / 2) ** 2 # addition_operator, assignment:Pow, assignment_lhs_identifier:square_of_sum, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Pow, literal:1, literal:2, multiplication_operator, single_assignment:square_of_sum
    return int(square_of_sum - sum_of_squares) # binary_operator:Sub, call_argument:, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# problem_07/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt
def isprime(n): # function:isprime (-> +10), function_argument:n, function_argument_flavor:arg, function_returning_something:isprime (-> +10)
    if n == 2: # comparison_operator:Eq, if (-> +8), if_test_atom:2, if_test_atom:n, literal:2
        return True # if_then_branch, literal:True, return:True
    elif n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +6), if_test_atom:0, if_test_atom:2, if_test_atom:n, literal:0, literal:2, modulo_operator
        return False # if_elif_branch, literal:False, return:False
    else:
        sq = int(sqrt(n)) + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:sq, assignment_rhs_atom:1, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:n, composition, function_call:int, function_call:sqrt, if_else_branch (-> +3), literal:1, single_assignment:sq
        for i in range(3, sq, 2): # call_argument:2, call_argument:3, call_argument:sq, for:i (-> +2), for_range:3:sq:2 (-> +2), function_call:range, literal:2, literal:3, loop:for (-> +2), loop_with_early_exit:for:return (-> +2), range:3:sq:2, suggest_constant_definition, universal_quantification:i (-> +2)
            if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:n, if_without_else (-> +1), literal:0, modulo_operator, nested_if:1 (-> +1)
                return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def solution(n): # function:solution (-> +11), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +11)
    i = 0 # assignment:0, assignment_lhs_identifier:i, assignment_rhs_atom:0, literal:0, single_assignment:i
    j = 1 # assignment:1, assignment_lhs_identifier:j, assignment_rhs_atom:1, literal:1, single_assignment:j
    while i != n and j < 3: # boolean_operator:And, comparison_operator:Lt, comparison_operator:NotEq, count_states:i (-> +3), count_states:j (-> +3), literal:3, loop:while (-> +3), suggest_constant_definition, while (-> +3)
        j += 1 # assignment_lhs_identifier:j, assignment_rhs_atom:1, augmented_assignment:Add, increment:j, literal:1, update:j:1, update_by_augmented_assignment:j:1, update_by_augmented_assignment_with:Add, update_with:Add
        if isprime(j): # call_argument:j, function_call:isprime, if (-> +1), if_test_atom:j, if_without_else (-> +1)
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
    while i != n: # comparison_operator:NotEq, count_states:i (-> +3), loop:while (-> +3), while (-> +3)
        j += 2 # assignment_lhs_identifier:j, assignment_rhs_atom:2, augmented_assignment:Add, literal:2, update:j:2, update_by_augmented_assignment:j:2, update_by_augmented_assignment_with:Add, update_with:Add
        if isprime(j): # call_argument:j, function_call:isprime, if (-> +1), if_test_atom:j, if_without_else (-> +1)
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
    return j # return:j

# ----------------------------------------------------------------------------------------
# problem_07/sol2.py
# ----------------------------------------------------------------------------------------
def isprime(number): # function:isprime (-> +4), function_argument:number, function_argument_flavor:arg, function_returning_something:isprime (-> +4)
    for i in range(2, int(number ** 0.5) + 1): # addition_operator, binary_operator:Add, binary_operator:Pow, call_argument:, call_argument:2, composition, for:i (-> +2), for_range:2:_ (-> +2), function_call:int, function_call:range, literal:0.5, literal:1, literal:2, loop:for (-> +2), loop_with_early_exit:for:return (-> +2), range:2:_, suggest_constant_definition, universal_quantification:i (-> +2)
        if number % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:number, if_without_else (-> +1), literal:0, modulo_operator
            return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def solution(n): # function:solution (-> +15), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +15)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int, single_assignment:n
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    primes = [] # assignment, assignment_lhs_identifier:primes, empty_literal:List, literal:List, single_assignment:primes
    num = 2 # assignment:2, assignment_lhs_identifier:num, assignment_rhs_atom:2, literal:2, single_assignment:num
    while len(primes) < n: # call_argument:primes, comparison_operator:Lt, function_call:len, loop:while (-> +5), while (-> +5)
        if isprime(num): # call_argument:num, function_call:isprime, if (-> +4), if_test_atom:num
            primes.append(num) # call_argument:num, if_then_branch (-> +1), method_call:append, method_call_object:primes, method_call_without_result:append, update:primes:num, update_by_method_call:primes:num, update_by_method_call_with:append, update_with:append
            num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment:num, literal:1, update:num:1, update_by_augmented_assignment:num:1, update_by_augmented_assignment_with:Add, update_with:Add
        else:
            num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, if_else_branch, increment:num, literal:1, update:num:1, update_by_augmented_assignment:num:1, update_by_augmented_assignment_with:Add, update_with:Add
    return primes[len(primes) - 1] # binary_operator:Sub, call_argument:primes, function_call:len, index:_, index_arithmetic, literal:1, return

# ----------------------------------------------------------------------------------------
# problem_07/sol3.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
import itertools # import:itertools, import_module:itertools
def primeCheck(number): # function:primeCheck (-> +3), function_argument:number, function_argument_flavor:arg, function_returning_something:primeCheck (-> +3)
    if number % 2 == 0 and number > 2: # binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, divisibility_test:2, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:number, if_without_else (-> +1), literal:0, literal:2, modulo_operator
        return False # if_then_branch, literal:False, return:False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # addition_operator, binary_operator:Add, binary_operator:Mod, call_argument:, call_argument:2, call_argument:3, call_argument:number, composition, comprehension:Generator, comprehension_for_count:1, function_call:all, function_call:int, function_call:range, function_tail_call:all, literal:1, literal:2, literal:3, method_call:sqrt, modulo_operator, range:3:_:2, return, suggest_constant_definition
def prime_generator(): # function:prime_generator (-> +5), function_without_arguments:prime_generator (-> +5), generator:prime_generator (-> +5)
    num = 2 # assignment:2, assignment_lhs_identifier:num, assignment_rhs_atom:2, literal:2, single_assignment:num
    while True: # count_states:num (-> +3), infinite_while (-> +3), literal:True, loop:while (-> +3), while (-> +3)
        if primeCheck(num): # call_argument:num, function_call:primeCheck, if (-> +1), if_test_atom:num, if_without_else (-> +1)
            yield num # if_then_branch, yield:num
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment:num, literal:1, update:num:1, update_by_augmented_assignment:num:1, update_by_augmented_assignment_with:Add, update_with:Add
def solution(n): # function:solution (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return next(itertools.islice(prime_generator(), n - 1, n)) # binary_operator:Sub, call_argument:, call_argument:n, composition, function_call:next, function_call:prime_generator, function_call_without_arguments:prime_generator, function_tail_call:next, literal:1, method_call:islice, return

# ----------------------------------------------------------------------------------------
# problem_08/sol1.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys
N = """73167176531330624919225119674426574742355349194934\ # assignment, assignment_lhs_identifier:N, single_assignment:N
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450""" # literal:Str
def solution(n): # function:solution (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +8)
    LargestProduct = -sys.maxsize - 1 # assignment:Sub, assignment_lhs_identifier:LargestProduct, assignment_rhs_atom:1, assignment_rhs_atom:sys, binary_operator:Sub, literal:1, single_assignment:LargestProduct, unary_operator:USub
    for i in range(len(n) - 12): # accumulate_all_elements:Mult (-> +5), accumulate_elements:Mult (-> +5), binary_operator:Sub, call_argument:, call_argument:n, composition, for:i (-> +5), for_range:13 (-> +5), for_range:_ (-> +5), function_call:len, function_call:range, literal:12, loop:for (-> +5), range:_, suggest_constant_definition
        product = 1 # assignment:1, assignment_lhs_identifier:product, assignment_rhs_atom:1, literal:1, single_assignment:product
        for j in range(13): # accumulate_all_elements:Mult (-> +1), accumulate_elements:Mult (-> +1), call_argument:13, for:j (-> +1), for_range:13 (-> +1), function_call:range, literal:13, loop:for (-> +1), nested_for:1 (-> +1), range:13, suggest_constant_definition
            product *= int(n[i + j]) # addition_operator, assignment_lhs_identifier:product, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:n, augmented_assignment:Mult, binary_operator:Add, call_argument:, function_call:int, index:_, index_arithmetic, update:product:i, update:product:j, update:product:n, update_by_augmented_assignment:product:i, update_by_augmented_assignment:product:j, update_by_augmented_assignment:product:n, update_by_augmented_assignment_with:Mult, update_with:Mult
        if product > LargestProduct: # comparison_operator:Gt, if (-> +1), if_test_atom:LargestProduct, if_test_atom:product, if_without_else (-> +1)
            LargestProduct = product # assignment, assignment_lhs_identifier:LargestProduct, assignment_rhs_atom:product, if_then_branch, single_assignment:LargestProduct
    return LargestProduct # return:LargestProduct

# ----------------------------------------------------------------------------------------
# problem_08/sol2.py
# ----------------------------------------------------------------------------------------
from functools import reduce # import:functools:reduce, import_module:functools, import_name:reduce
N = ( # assignment, assignment_lhs_identifier:N, single_assignment:N
    "73167176531330624919225119674426574742355349194934" # literal:Str
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)
def solution(n): # function:solution (-> +4), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +4)
    return max( # composition, function_call:max, function_tail_call:max, return
        [
            reduce(lambda x, y: int(x) * int(y), n[i : i + 13]) # addition_operator, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:x, call_argument:y, composition, comprehension:List, comprehension_for_count:1, function_argument:x, function_argument:y, function_argument_flavor:arg, function_call:int, function_call:reduce, lambda_function, literal:13, multiplication_operator, slice:i:_:, slice_lower:i, slice_step:, slice_upper:_, suggest_constant_definition
            for i in range(len(n) - 12) # binary_operator:Sub, call_argument:, call_argument:n, composition, function_call:len, function_call:range, literal:12, range:_, suggest_constant_definition
        ]
    )

# ----------------------------------------------------------------------------------------
# problem_08/sol3.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys
N = """73167176531330624919225119674426574742355349194934\ # assignment, assignment_lhs_identifier:N, single_assignment:N
96983520312774506326239578318016984801869478851843\
85861560789112949495459501737958331952853208805511\
12540698747158523863050715693290963295227443043557\
66896648950445244523161731856403098711121722383113\
62229893423380308135336276614282806444486645238749\
30358907296290491560440772390713810515859307960866\
70172427121883998797908792274921901699720888093776\
65727333001053367881220235421809751254540594752243\
52584907711670556013604839586446706324415722155397\
53697817977846174064955149290862569321978468622482\
83972241375657056057490261407972968652414535100474\
82166370484403199890008895243450658541227588666881\
16427171479924442928230863465674813919123162824586\
17866458359124566529476545682848912883142607690042\
24219022671055626321111109370544217506941658960408\
07198403850962455444362981230987879927244284909188\
84580156166097919133875499200524063689912560717606\
05886116467109405077541002256983155200055935729725\
71636269561882670428252483600823257530420752963450""" # literal:Str
def streval(s: str) -> int: # function:streval (-> +4), function_argument:s, function_argument_flavor:arg, function_returning_something:streval (-> +4)
    ret = 1 # assignment:1, assignment_lhs_identifier:ret, assignment_rhs_atom:1, literal:1, single_assignment:ret
    for it in s: # accumulate_all_elements:Mult (-> +1), accumulate_elements:Mult (-> +1), for:it (-> +1), for_each (-> +1), loop:for (-> +1)
        ret *= int(it) # assignment_lhs_identifier:ret, assignment_rhs_atom:it, augmented_assignment:Mult, call_argument:it, function_call:int, update:ret:it, update_by_augmented_assignment:ret:it, update_by_augmented_assignment_with:Mult, update_with:Mult
    return ret # return:ret
def solution(n: str) -> int: # function:solution (-> +12), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +12)
    LargestProduct = -sys.maxsize - 1 # assignment:Sub, assignment_lhs_identifier:LargestProduct, assignment_rhs_atom:1, assignment_rhs_atom:sys, binary_operator:Sub, literal:1, single_assignment:LargestProduct, unary_operator:USub
    substr = n[:13] # assignment, assignment_lhs_identifier:substr, assignment_rhs_atom:13, assignment_rhs_atom:n, literal:13, single_assignment:substr, slice::13:, slice_lower:, slice_step:, slice_upper:13, suggest_constant_definition
    cur_index = 13 # assignment:13, assignment_lhs_identifier:cur_index, assignment_rhs_atom:13, literal:13, single_assignment:cur_index, suggest_constant_definition
    while cur_index < len(n) - 13: # binary_operator:Sub, call_argument:n, comparison_operator:Lt, function_call:len, literal:13, loop:while (-> +7), suggest_constant_definition, while (-> +7)
        if int(n[cur_index]) >= int(substr[0]): # call_argument:, comparison_operator:GtE, function_call:int, if (-> +6), if_test_atom:0, if_test_atom:cur_index, if_test_atom:n, if_test_atom:substr, index:0, index:cur_index, literal:0
            substr = substr[1:] + n[cur_index] # addition_operator, assignment:Add, assignment_lhs_identifier:substr, assignment_rhs_atom:1, assignment_rhs_atom:cur_index, assignment_rhs_atom:n, assignment_rhs_atom:substr, binary_operator:Add, if_then_branch (-> +1), index:cur_index, literal:1, single_assignment:substr, slice:1::, slice_lower:1, slice_step:, slice_upper:, update:substr:1, update:substr:cur_index, update:substr:n, update_by_assignment:substr:1, update_by_assignment:substr:cur_index, update_by_assignment:substr:n, update_by_assignment_with:Add, update_with:Add
            cur_index += 1 # assignment_lhs_identifier:cur_index, assignment_rhs_atom:1, augmented_assignment:Add, increment:cur_index, literal:1, update:cur_index:1, update_by_augmented_assignment:cur_index:1, update_by_augmented_assignment_with:Add, update_with:Add
        else:
            LargestProduct = max(LargestProduct, streval(substr)) # assignment:max, assignment_lhs_identifier:LargestProduct, assignment_rhs_atom:LargestProduct, assignment_rhs_atom:substr, call_argument:, call_argument:LargestProduct, call_argument:substr, composition, function_call:max, function_call:streval, if_else_branch (-> +2), single_assignment:LargestProduct, update:LargestProduct:substr, update_by_assignment:LargestProduct:substr, update_by_assignment_with:max, update_with:max
            substr = n[cur_index : cur_index + 13] # addition_operator, assignment, assignment_lhs_identifier:substr, assignment_rhs_atom:13, assignment_rhs_atom:cur_index, assignment_rhs_atom:n, binary_operator:Add, literal:13, single_assignment:substr, slice:cur_index:_:, slice_lower:cur_index, slice_step:, slice_upper:_, suggest_constant_definition
            cur_index += 13 # assignment_lhs_identifier:cur_index, assignment_rhs_atom:13, augmented_assignment:Add, increment:cur_index, literal:13, suggest_constant_definition, update:cur_index:13, update_by_augmented_assignment:cur_index:13, update_by_augmented_assignment_with:Add, update_with:Add
    return LargestProduct # return:LargestProduct

# ----------------------------------------------------------------------------------------
# problem_09/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +7), function_returning_something:solution (-> +7), function_without_arguments:solution (-> +7)
    for a in range(300): # call_argument:300, for:a (-> +6), for_range:300 (-> +6), for_range:400 (-> +6), for_range:500 (-> +6), function_call:range, literal:300, loop:for (-> +6), range:300, suggest_constant_definition
        for b in range(400): # call_argument:400, for:b (-> +5), for_range:400 (-> +5), for_range:500 (-> +5), function_call:range, literal:400, loop:for (-> +5), nested_for:1 (-> +5), range:400, suggest_constant_definition
            for c in range(500): # call_argument:500, for:c (-> +4), for_range:500 (-> +4), function_call:range, literal:500, loop:for (-> +4), loop_with_early_exit:for:return (-> +4), nested_for:2 (-> +4), range:500, suggest_constant_definition
                if a < b < c: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +3), if_test_atom:a, if_test_atom:b, if_test_atom:c, if_without_else (-> +3)
                    if (a ** 2) + (b ** 2) == (c ** 2): # addition_operator, binary_operator:Add, binary_operator:Pow, comparison_operator:Eq, if (-> +2), if_test_atom:2, if_test_atom:a, if_test_atom:b, if_test_atom:c, if_then_branch (-> +2), if_without_else (-> +2), literal:2, nested_if:1 (-> +2)
                        if (a + b + c) == 1000: # addition_operator, binary_operator:Add, comparison_operator:Eq, if (-> +1), if_test_atom:1000, if_test_atom:a, if_test_atom:b, if_test_atom:c, if_then_branch (-> +1), if_without_else (-> +1), literal:1000, nested_if:2 (-> +1), suggest_constant_definition
                            return a * b * c # binary_operator:Mult, if_then_branch, multiplication_operator, return

# ----------------------------------------------------------------------------------------
# problem_09/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +10), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +10)
    product = -1 # assignment:-1, assignment_lhs_identifier:product, assignment_rhs_atom:-1, literal:-1, single_assignment:product
    d = 0 # assignment:0, assignment_lhs_identifier:d, assignment_rhs_atom:0, literal:0, single_assignment:d
    for a in range(1, n // 3): # binary_operator:FloorDiv, call_argument:, call_argument:1, for:a (-> +6), for_range:1:_ (-> +6), function_call:range, literal:1, literal:3, loop:for (-> +6), range:1:_, suggest_constant_definition
        b = (n * n - 2 * a * n) // (2 * n - 2 * a) # assignment:FloorDiv, assignment_lhs_identifier:b, assignment_rhs_atom:2, assignment_rhs_atom:a, assignment_rhs_atom:n, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, literal:2, multiplication_operator, single_assignment:b
        c = n - a - b # assignment:Sub, assignment_lhs_identifier:c, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:n, binary_operator:Sub, single_assignment:c
        if c * c == (a * a + b * b): # addition_operator, binary_operator:Add, binary_operator:Mult, comparison_operator:Eq, if (-> +3), if_test_atom:a, if_test_atom:b, if_test_atom:c, if_without_else (-> +3), multiplication_operator
            d = a * b * c # assignment:Mult, assignment_lhs_identifier:d, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:c, binary_operator:Mult, if_then_branch (-> +2), multiplication_operator, single_assignment:d
            if d >= product: # comparison_operator:GtE, if (-> +1), if_test_atom:d, if_test_atom:product, if_without_else (-> +1), nested_if:1 (-> +1)
                product = d # assignment, assignment_lhs_identifier:product, assignment_rhs_atom:d, if_then_branch, single_assignment:product
    return product # return:product

# ----------------------------------------------------------------------------------------
# problem_09/sol3.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +7), function_returning_something:solution (-> +7), function_without_arguments:solution (-> +7)
    return [ # return
        a * b * c # binary_operator:Mult, comprehension:List, comprehension_for_count:3, index:0, multiplication_operator
        for a in range(1, 999) # call_argument:1, call_argument:999, function_call:range, literal:1, literal:999, range:1:999, suggest_constant_definition
        for b in range(a, 999) # call_argument:999, call_argument:a, function_call:range, literal:999, range:a:999, suggest_constant_definition
        for c in range(b, 999) # call_argument:999, call_argument:b, function_call:range, literal:999, range:b:999, suggest_constant_definition
        if (a * a + b * b == c * c) and (a + b + c == 1000) # addition_operator, binary_operator:Add, binary_operator:Mult, boolean_operator:And, comparison_operator:Eq, filtered_comprehension, literal:1000, multiplication_operator, suggest_constant_definition
    ][0] # literal:0

# ----------------------------------------------------------------------------------------
# problem_10/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt
def is_prime(n): # function:is_prime (-> +4), function_argument:n, function_argument_flavor:arg, function_returning_something:is_prime (-> +4)
    for i in range(2, int(sqrt(n)) + 1): # addition_operator, binary_operator:Add, call_argument:, call_argument:2, call_argument:n, composition, for:i (-> +2), for_range:2:_ (-> +2), function_call:int, function_call:range, function_call:sqrt, literal:1, literal:2, loop:for (-> +2), loop_with_early_exit:for:return (-> +2), range:2:_, universal_quantification:i (-> +2)
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:n, if_without_else (-> +1), literal:0, modulo_operator
            return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def sum_of_primes(n): # function:sum_of_primes (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:sum_of_primes (-> +8)
    if n > 2: # comparison_operator:Gt, if (-> +3), if_test_atom:2, if_test_atom:n, literal:2
        sumOfPrimes = 2 # assignment:2, assignment_lhs_identifier:sumOfPrimes, assignment_rhs_atom:2, if_then_branch, literal:2, single_assignment:sumOfPrimes
    else:
        return 0 # if_else_branch, literal:0, return:0
    for i in range(3, n, 2): # accumulate_elements:Add (-> +2), accumulate_some_elements:Add (-> +2), call_argument:2, call_argument:3, call_argument:n, for:i (-> +2), for_range:3:n:2 (-> +2), function_call:range, literal:2, literal:3, loop:for (-> +2), range:3:n:2, suggest_constant_definition
        if is_prime(i): # call_argument:i, function_call:is_prime, if (-> +1), if_test_atom:i, if_without_else (-> +1)
            sumOfPrimes += i # assignment_lhs_identifier:sumOfPrimes, assignment_rhs_atom:i, augmented_assignment:Add, if_then_branch, update:sumOfPrimes:i, update_by_augmented_assignment:sumOfPrimes:i, update_by_augmented_assignment_with:Add, update_with:Add
    return sumOfPrimes # return:sumOfPrimes
def solution(n): # function:solution (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return sum_of_primes(n) # call_argument:n, function_call:sum_of_primes, function_tail_call:sum_of_primes, return

# ----------------------------------------------------------------------------------------
# problem_10/sol2.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
from itertools import takewhile # import:itertools:takewhile, import_module:itertools, import_name:takewhile
def primeCheck(number): # function:primeCheck (-> +3), function_argument:number, function_argument_flavor:arg, function_returning_something:primeCheck (-> +3)
    if number % 2 == 0 and number > 2: # binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, divisibility_test:2, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:number, if_without_else (-> +1), literal:0, literal:2, modulo_operator
        return False # if_then_branch, literal:False, return:False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # addition_operator, binary_operator:Add, binary_operator:Mod, call_argument:, call_argument:2, call_argument:3, call_argument:number, composition, comprehension:Generator, comprehension_for_count:1, function_call:all, function_call:int, function_call:range, function_tail_call:all, literal:1, literal:2, literal:3, method_call:sqrt, modulo_operator, range:3:_:2, return, suggest_constant_definition
def prime_generator(): # function:prime_generator (-> +5), function_without_arguments:prime_generator (-> +5), generator:prime_generator (-> +5)
    num = 2 # assignment:2, assignment_lhs_identifier:num, assignment_rhs_atom:2, literal:2, single_assignment:num
    while True: # count_states:num (-> +3), infinite_while (-> +3), literal:True, loop:while (-> +3), while (-> +3)
        if primeCheck(num): # call_argument:num, function_call:primeCheck, if (-> +1), if_test_atom:num, if_without_else (-> +1)
            yield num # if_then_branch, yield:num
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment:num, literal:1, update:num:1, update_by_augmented_assignment:num:1, update_by_augmented_assignment_with:Add, update_with:Add
def solution(n): # function:solution (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return sum(takewhile(lambda x: x < n, prime_generator())) # call_argument:, comparison_operator:Lt, composition, function_argument:x, function_argument_flavor:arg, function_call:prime_generator, function_call:sum, function_call:takewhile, function_call_without_arguments:prime_generator, function_tail_call:sum, lambda_function, return

# ----------------------------------------------------------------------------------------
# problem_10/sol3.py
# ----------------------------------------------------------------------------------------
def prime_sum(n: int) -> int: # function:prime_sum (-> +12), function_argument:n, function_argument_flavor:arg, function_returning_something:prime_sum (-> +12)
    list_ = [0 for i in range(n + 1)] # addition_operator, assignment, assignment_lhs_identifier:list_, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Add, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, literal:0, literal:1, range:_, single_assignment:list_
    list_[0] = 1 # assignment:1, assignment_lhs_identifier:list_, assignment_rhs_atom:1, index:0, literal:0, literal:1
    list_[1] = 1 # assignment:1, assignment_lhs_identifier:list_, assignment_rhs_atom:1, index:1, literal:1
    for i in range(2, int(n ** 0.5) + 1): # addition_operator, binary_operator:Add, binary_operator:Pow, call_argument:, call_argument:2, composition, for:i (-> +3), for_range:2:_ (-> +3), for_range:_:_:i (-> +3), function_call:int, function_call:range, literal:0.5, literal:1, literal:2, loop:for (-> +3), range:2:_, suggest_constant_definition
        if list_[i] == 0: # comparison_operator:Eq, if (-> +2), if_test_atom:0, if_test_atom:i, if_test_atom:list_, if_without_else (-> +2), index:i, literal:0
            for j in range(i * i, n + 1, i): # addition_operator, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:i, for:j (-> +1), for_range:_:_:i (-> +1), function_call:range, if_then_branch (-> +1), literal:1, loop:for (-> +1), multiplication_operator, nested_for:1 (-> +1), range:_:_:i
                list_[j] = 1 # assignment:1, assignment_lhs_identifier:list_, assignment_rhs_atom:1, index:j, literal:1
    s = 0 # assignment:0, assignment_lhs_identifier:s, assignment_rhs_atom:0, literal:0, single_assignment:s
    for i in range(n): # accumulate_elements:Add (-> +2), accumulate_some_elements:Add (-> +2), call_argument:n, for:i (-> +2), for_range:n (-> +2), function_call:range, loop:for (-> +2), range:n
        if list_[i] == 0: # comparison_operator:Eq, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:list_, if_without_else (-> +1), index:i, literal:0
            s += i # assignment_lhs_identifier:s, assignment_rhs_atom:i, augmented_assignment:Add, if_then_branch, update:s:i, update_by_augmented_assignment:s:i, update_by_augmented_assignment_with:Add, update_with:Add
    return s # return:s

# ----------------------------------------------------------------------------------------
# problem_11/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def largest_product(grid): # function:largest_product (-> +27), function_argument:grid, function_argument_flavor:arg, function_returning_something:largest_product (-> +27)
    nColumns = len(grid[0]) # assignment:len, assignment_lhs_identifier:nColumns, assignment_rhs_atom:0, assignment_rhs_atom:grid, call_argument:, function_call:len, index:0, literal:0, single_assignment:nColumns
    nRows = len(grid) # assignment:len, assignment_lhs_identifier:nRows, assignment_rhs_atom:grid, call_argument:grid, function_call:len, single_assignment:nRows
    largest = 0 # assignment:0, assignment_lhs_identifier:largest, assignment_rhs_atom:0, literal:0, single_assignment:largest
    lrDiagProduct = 0 # assignment:0, assignment_lhs_identifier:lrDiagProduct, assignment_rhs_atom:0, literal:0, single_assignment:lrDiagProduct
    rlDiagProduct = 0 # assignment:0, assignment_lhs_identifier:rlDiagProduct, assignment_rhs_atom:0, literal:0, single_assignment:rlDiagProduct
    for i in range(nColumns): # call_argument:nColumns, for:i (-> +20), for_range:_ (-> +20), for_range:nColumns (-> +20), function_call:range, loop:for (-> +20), range:nColumns
        for j in range(nRows - 3): # binary_operator:Sub, call_argument:, for:j (-> +19), for_range:_ (-> +19), function_call:range, literal:3, loop:for (-> +19), nested_for:1 (-> +19), range:_, suggest_constant_definition
            vertProduct = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i] # addition_operator, assignment:Mult, assignment_lhs_identifier:vertProduct, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, index:_, index:i, index:j, index_arithmetic, literal:1, literal:2, literal:3, multiplication_operator, nested_index:2, single_assignment:vertProduct, suggest_constant_definition
            horzProduct = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3] # addition_operator, assignment:Mult, assignment_lhs_identifier:horzProduct, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, index:_, index:i, index:j, index_arithmetic, literal:1, literal:2, literal:3, multiplication_operator, nested_index:2, single_assignment:horzProduct, suggest_constant_definition
            if i < nColumns - 3: # binary_operator:Sub, comparison_operator:Lt, if (-> +5), if_test_atom:3, if_test_atom:i, if_test_atom:nColumns, if_without_else (-> +5), literal:3, suggest_constant_definition
                lrDiagProduct = ( # assignment:Mult, assignment_lhs_identifier:lrDiagProduct, if_then_branch (-> +4), single_assignment:lrDiagProduct
                    grid[i][j] # assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Mult, index:i, index:j, multiplication_operator, nested_index:2
                    * grid[i + 1][j + 1] # addition_operator, assignment_rhs_atom:1, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, index:_, index_arithmetic, literal:1, nested_index:2
                    * grid[i + 2][j + 2] # addition_operator, assignment_rhs_atom:2, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, index:_, index_arithmetic, literal:2, multiplication_operator, nested_index:2
                    * grid[i + 3][j + 3] # addition_operator, assignment_rhs_atom:3, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, index:_, index_arithmetic, literal:3, multiplication_operator, nested_index:2, suggest_constant_definition
                )
            if i > 2: # comparison_operator:Gt, if (-> +5), if_test_atom:2, if_test_atom:i, if_without_else (-> +5), literal:2
                rlDiagProduct = ( # assignment:Mult, assignment_lhs_identifier:rlDiagProduct, if_then_branch (-> +4), single_assignment:rlDiagProduct
                    grid[i][j] # assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Mult, index:i, index:j, multiplication_operator, nested_index:2
                    * grid[i - 1][j + 1] # addition_operator, assignment_rhs_atom:1, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Sub, index:_, index_arithmetic, literal:1, nested_index:2
                    * grid[i - 2][j + 2] # addition_operator, assignment_rhs_atom:2, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index:_, index_arithmetic, literal:2, multiplication_operator, nested_index:2
                    * grid[i - 3][j + 3] # addition_operator, assignment_rhs_atom:3, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index:_, index_arithmetic, literal:3, multiplication_operator, nested_index:2, suggest_constant_definition
                )
            maxProduct = max(vertProduct, horzProduct, lrDiagProduct, rlDiagProduct) # assignment:max, assignment_lhs_identifier:maxProduct, assignment_rhs_atom:horzProduct, assignment_rhs_atom:lrDiagProduct, assignment_rhs_atom:rlDiagProduct, assignment_rhs_atom:vertProduct, call_argument:horzProduct, call_argument:lrDiagProduct, call_argument:rlDiagProduct, call_argument:vertProduct, function_call:max, single_assignment:maxProduct
            if maxProduct > largest: # comparison_operator:Gt, if (-> +1), if_test_atom:largest, if_test_atom:maxProduct, if_without_else (-> +1)
                largest = maxProduct # assignment, assignment_lhs_identifier:largest, assignment_rhs_atom:maxProduct, if_then_branch, single_assignment:largest
    return largest # return:largest
def solution(): # function:solution (-> +6), function_returning_something:solution (-> +6), function_without_arguments:solution (-> +6)
    grid = [] # assignment, assignment_lhs_identifier:grid, empty_literal:List, literal:List, single_assignment:grid
    with open(os.path.dirname(__file__) + "/grid.txt") as file: # binary_operator:Add, call_argument:, call_argument:__file__, composition, concatenation_operator:Str, function_call:open, literal:Str, method_call:dirname
        for line in file: # for:line (-> +1), for_each (-> +1), loop:for (-> +1)
            grid.append(line.strip("\n").split(" ")) # call_argument:, composition, literal:Str, method_call:append, method_call:split, method_call:strip, method_call_object:grid, method_call_object:line, method_call_without_result:append, method_chaining
    grid = [[int(i) for i in grid[j]] for j in range(len(grid))] # assignment, assignment_lhs_identifier:grid, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, call_argument:, call_argument:grid, call_argument:i, composition, comprehension:List, comprehension_for_count:1, function_call:int, function_call:len, function_call:range, index:j, range:_, single_assignment:grid, update:grid:i, update:grid:j, update_by_assignment:grid:i, update_by_assignment:grid:j, update_by_assignment_with, update_with
    return largest_product(grid) # call_argument:grid, function_call:largest_product, function_tail_call:largest_product, return

# ----------------------------------------------------------------------------------------
# problem_11/sol2.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +26), function_returning_something:solution (-> +26), function_without_arguments:solution (-> +26)
    with open(os.path.dirname(__file__) + "/grid.txt") as f: # binary_operator:Add, call_argument:, call_argument:__file__, composition, concatenation_operator:Str, function_call:open, literal:Str, method_call:dirname
        l = [] # assignment, assignment_lhs_identifier:l, empty_literal:List, literal:List, single_assignment:l
        for i in range(20): # call_argument:20, for:i (-> +1), for_range:20 (-> +1), function_call:range, literal:20, loop:for (-> +1), range:20, suggest_constant_definition
            l.append([int(x) for x in f.readline().split()]) # call_argument:, call_argument:x, composition, comprehension:List, comprehension_for_count:1, function_call:int, method_call:append, method_call:readline, method_call:split, method_call_object:f, method_call_object:l, method_call_without_result:append, method_chaining, update:f:x, update:l:x, update_by_method_call:f:x, update_by_method_call:l:x, update_by_method_call_with:append, update_with:append
        maximum = 0 # assignment:0, assignment_lhs_identifier:maximum, assignment_rhs_atom:0, literal:0, single_assignment:maximum
        for i in range(20): # call_argument:20, for:i (-> +4), for_range:17 (-> +4), for_range:20 (-> +4), function_call:range, literal:20, loop:for (-> +4), range:20, suggest_constant_definition
            for j in range(17): # call_argument:17, for:j (-> +3), for_range:17 (-> +3), function_call:range, literal:17, loop:for (-> +3), nested_for:1 (-> +3), range:17, suggest_constant_definition
                temp = l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3] # addition_operator, assignment:Mult, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:l, binary_operator:Add, binary_operator:Mult, index:_, index:i, index:j, index_arithmetic, literal:1, literal:2, literal:3, multiplication_operator, nested_index:2, single_assignment:temp, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1), if_test_atom:maximum, if_test_atom:temp, if_without_else (-> +1)
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_atom:temp, if_then_branch, single_assignment:maximum
        for i in range(17): # call_argument:17, for:i (-> +4), for_range:17 (-> +4), for_range:20 (-> +4), function_call:range, literal:17, loop:for (-> +4), range:17, suggest_constant_definition
            for j in range(20): # call_argument:20, for:j (-> +3), for_range:20 (-> +3), function_call:range, literal:20, loop:for (-> +3), nested_for:1 (-> +3), range:20, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j] # addition_operator, assignment:Mult, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:l, binary_operator:Add, binary_operator:Mult, index:_, index:i, index:j, index_arithmetic, literal:1, literal:2, literal:3, multiplication_operator, nested_index:2, single_assignment:temp, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1), if_test_atom:maximum, if_test_atom:temp, if_without_else (-> +1)
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_atom:temp, if_then_branch, single_assignment:maximum
        for i in range(17): # call_argument:17, for:i (-> +4), for_range:17 (-> +4), function_call:range, literal:17, loop:for (-> +4), range:17, square_nested_for (-> +4), suggest_constant_definition
            for j in range(17): # call_argument:17, for:j (-> +3), for_range:17 (-> +3), function_call:range, literal:17, loop:for (-> +3), nested_for:1 (-> +3), range:17, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3] # addition_operator, assignment:Mult, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:l, binary_operator:Add, binary_operator:Mult, index:_, index:i, index:j, index_arithmetic, literal:1, literal:2, literal:3, multiplication_operator, nested_index:2, single_assignment:temp, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1), if_test_atom:maximum, if_test_atom:temp, if_without_else (-> +1)
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_atom:temp, if_then_branch, single_assignment:maximum
        for i in range(17): # call_argument:17, for:i (-> +4), for_range:17 (-> +4), for_range:3:20 (-> +4), function_call:range, literal:17, loop:for (-> +4), range:17, suggest_constant_definition
            for j in range(3, 20): # call_argument:20, call_argument:3, for:j (-> +3), for_range:3:20 (-> +3), function_call:range, literal:20, literal:3, loop:for (-> +3), nested_for:1 (-> +3), range:3:20, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3] # addition_operator, assignment:Mult, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:l, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index:_, index:i, index:j, index_arithmetic, literal:1, literal:2, literal:3, multiplication_operator, nested_index:2, single_assignment:temp, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1), if_test_atom:maximum, if_test_atom:temp, if_without_else (-> +1)
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_atom:temp, if_then_branch, single_assignment:maximum
        return maximum # return:maximum

# ----------------------------------------------------------------------------------------
# problem_12/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt
def count_divisors(n): # function:count_divisors (-> +7), function_argument:n, function_argument_flavor:arg, function_returning_something:count_divisors (-> +7)
    nDivisors = 0 # assignment:0, assignment_lhs_identifier:nDivisors, assignment_rhs_atom:0, literal:0, single_assignment:nDivisors
    for i in range(1, int(sqrt(n)) + 1): # addition_operator, binary_operator:Add, call_argument:, call_argument:1, call_argument:n, composition, for:i (-> +2), for_range:1:_ (-> +2), function_call:int, function_call:range, function_call:sqrt, literal:1, loop:for (-> +2), range:1:_
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:n, if_without_else (-> +1), literal:0, modulo_operator
            nDivisors += 2 # assignment_lhs_identifier:nDivisors, assignment_rhs_atom:2, augmented_assignment:Add, if_then_branch, literal:2, update:nDivisors:2, update_by_augmented_assignment:nDivisors:2, update_by_augmented_assignment_with:Add, update_with:Add
    if n ** 0.5 == int(n ** 0.5): # binary_operator:Pow, call_argument:, comparison_operator:Eq, function_call:int, if (-> +1), if_test_atom:0.5, if_test_atom:n, if_without_else (-> +1), literal:0.5, suggest_constant_definition
        nDivisors -= 1 # assignment_lhs_identifier:nDivisors, assignment_rhs_atom:1, augmented_assignment:Sub, if_then_branch, literal:1, update:nDivisors:1, update_by_augmented_assignment:nDivisors:1, update_by_augmented_assignment_with:Sub, update_with:Sub
    return nDivisors # return:nDivisors
def solution(): # function:solution (-> +8), function_returning_something:solution (-> +8), function_without_arguments:solution (-> +8)
    tNum = 1 # assignment:1, assignment_lhs_identifier:tNum, assignment_rhs_atom:1, literal:1, single_assignment:tNum
    i = 1 # assignment:1, assignment_lhs_identifier:i, assignment_rhs_atom:1, literal:1, single_assignment:i
    while True: # count_states:i (-> +4), infinite_while (-> +4), literal:True, loop:while (-> +4), loop_with_early_exit:while:break (-> +4), while (-> +4)
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
        tNum += i # assignment_lhs_identifier:tNum, assignment_rhs_atom:i, augmented_assignment:Add, update:tNum:i, update_by_augmented_assignment:tNum:i, update_by_augmented_assignment_with:Add, update_with:Add
        if count_divisors(tNum) > 500: # call_argument:tNum, comparison_operator:Gt, function_call:count_divisors, if (-> +1), if_test_atom:500, if_test_atom:tNum, if_without_else (-> +1), literal:500, suggest_constant_definition
            break # break, if_then_branch
    return tNum # return:tNum

# ----------------------------------------------------------------------------------------
# problem_12/sol2.py
# ----------------------------------------------------------------------------------------
def triangle_number_generator(): # function:triangle_number_generator (-> +2), function_without_arguments:triangle_number_generator (-> +2), generator:triangle_number_generator (-> +2)
    for n in range(1, 1000000): # call_argument:1, call_argument:1000000, for:n (-> +1), for_range:1:1000000 (-> +1), function_call:range, literal:1, literal:1000000, loop:for (-> +1), range:1:1000000, suggest_constant_definition
        yield n * (n + 1) // 2 # addition_operator, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, literal:1, literal:2, multiplication_operator, yield
def count_divisors(n): # function:count_divisors (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:count_divisors (-> +1)
    return sum([2 for i in range(1, int(n ** 0.5) + 1) if n % i == 0 and i * i != n]) # addition_operator, binary_operator:Add, binary_operator:Mod, binary_operator:Mult, binary_operator:Pow, boolean_operator:And, call_argument:, call_argument:1, comparison_operator:Eq, comparison_operator:NotEq, composition, comprehension:List, comprehension_for_count:1, divisibility_test, filtered_comprehension, function_call:int, function_call:range, function_call:sum, function_tail_call:sum, literal:0, literal:0.5, literal:1, literal:2, modulo_operator, multiplication_operator, range:1:_, return, suggest_constant_definition
def solution(): # function:solution (-> +1), function_returning_something:solution (-> +1), function_without_arguments:solution (-> +1)
    return next(i for i in triangle_number_generator() if count_divisors(i) > 500) # call_argument:, call_argument:i, comparison_operator:Gt, composition, comprehension:Generator, comprehension_for_count:1, filtered_comprehension, function_call:count_divisors, function_call:next, function_call:triangle_number_generator, function_call_without_arguments:triangle_number_generator, function_tail_call:next, literal:500, return, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# problem_13/sol1.py
# ----------------------------------------------------------------------------------------
def solution(array): # function:solution (-> +1), function_argument:array, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return str(sum(array))[:10] # call_argument:, call_argument:array, composition, function_call:str, function_call:sum, literal:10, return, slice::10:, slice_lower:, slice_step:, slice_upper:10, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# problem_14/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +16), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +16)
    largest_number = 0 # assignment:0, assignment_lhs_identifier:largest_number, assignment_rhs_atom:0, literal:0, single_assignment:largest_number
    pre_counter = 0 # assignment:0, assignment_lhs_identifier:pre_counter, assignment_rhs_atom:0, literal:0, single_assignment:pre_counter
    for input1 in range(n): # call_argument:n, for:input1 (-> +12), for_range:n (-> +12), function_call:range, loop:for (-> +12), range:n
        counter = 1 # assignment:1, assignment_lhs_identifier:counter, assignment_rhs_atom:1, literal:1, single_assignment:counter
        number = input1 # assignment, assignment_lhs_identifier:number, assignment_rhs_atom:input1, single_assignment:number
        while number > 1: # comparison_operator:Gt, literal:1, loop:while (-> +6), while (-> +6)
            if number % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +5), if_test_atom:0, if_test_atom:2, if_test_atom:number, literal:0, literal:2, modulo_operator
                number /= 2 # assignment_lhs_identifier:number, assignment_rhs_atom:2, augmented_assignment:Div, if_then_branch (-> +1), literal:2, update:number:2, update_by_augmented_assignment:number:2, update_by_augmented_assignment_with:Div, update_with:Div
                counter += 1 # assignment_lhs_identifier:counter, assignment_rhs_atom:1, augmented_assignment:Add, increment:counter, literal:1, update:counter:1, update_by_augmented_assignment:counter:1, update_by_augmented_assignment_with:Add, update_with:Add
            else:
                number = (3 * number) + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:number, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:number, binary_operator:Add, binary_operator:Mult, if_else_branch (-> +1), literal:1, literal:3, multiplication_operator, single_assignment:number, suggest_constant_definition, update:number:1, update:number:3, update_by_assignment:number:1, update_by_assignment:number:3, update_by_assignment_with:Add, update_with:Add
                counter += 1 # assignment_lhs_identifier:counter, assignment_rhs_atom:1, augmented_assignment:Add, increment:counter, literal:1, update:counter:1, update_by_augmented_assignment:counter:1, update_by_augmented_assignment_with:Add, update_with:Add
        if counter > pre_counter: # comparison_operator:Gt, if (-> +2), if_test_atom:counter, if_test_atom:pre_counter, if_without_else (-> +2)
            largest_number = input1 # assignment, assignment_lhs_identifier:largest_number, assignment_rhs_atom:input1, if_then_branch (-> +1), single_assignment:largest_number
            pre_counter = counter # assignment, assignment_lhs_identifier:pre_counter, assignment_rhs_atom:counter, single_assignment:pre_counter
    return {"counter": pre_counter, "largest_number": largest_number} # literal:Str, return

# ----------------------------------------------------------------------------------------
# problem_14/sol2.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function:collatz_sequence (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:collatz_sequence (-> +8)
    sequence = [n] # assignment, assignment_lhs_identifier:sequence, assignment_rhs_atom:n, single_assignment:sequence
    while n != 1: # comparison_operator:NotEq, literal:1, loop:while (-> +5), while (-> +5)
        if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:0, if_test_atom:2, if_test_atom:n, literal:0, literal:2, modulo_operator
            n //= 2 # assignment_lhs_identifier:n, assignment_rhs_atom:2, augmented_assignment:FloorDiv, if_then_branch, literal:2, update:n:2, update_by_augmented_assignment:n:2, update_by_augmented_assignment_with:FloorDiv, update_with:FloorDiv
        else:
            n = 3 * n + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:n, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, if_else_branch, literal:1, literal:3, multiplication_operator, single_assignment:n, suggest_constant_definition, update:n:1, update:n:3, update_by_assignment:n:1, update_by_assignment:n:3, update_by_assignment_with:Add, update_with:Add
        sequence.append(n) # call_argument:n, method_call:append, method_call_object:sequence, method_call_without_result:append, update:sequence:n, update_by_method_call:sequence:n, update_by_method_call_with:append, update_with:append
    return sequence # return:sequence
def solution(n): # function:solution (-> +2), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +2)
    result = max([(len(collatz_sequence(i)), i) for i in range(1, n)]) # assignment:max, assignment_lhs_identifier:result, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:n, call_argument:, call_argument:1, call_argument:i, call_argument:n, composition, comprehension:List, comprehension_for_count:1, function_call:collatz_sequence, function_call:len, function_call:max, function_call:range, literal:1, range:1:n, single_assignment:result
    return {"counter": result[0], "largest_number": result[1]} # index:0, index:1, literal:0, literal:1, literal:Str, return

# ----------------------------------------------------------------------------------------
# problem_15/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial # import:math:factorial, import_module:math, import_name:factorial
def lattice_paths(n): # function:lattice_paths (-> +3), function_argument:n, function_argument_flavor:arg, function_returning_something:lattice_paths (-> +3)
    n = 2 * n # assignment:Mult, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Mult, literal:2, multiplication_operator, single_assignment:n, update:n:2, update_by_assignment:n:2, update_by_assignment_with:Mult, update_with:Mult
    k = n / 2 # assignment:Div, assignment_lhs_identifier:k, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, literal:2, single_assignment:k
    return int(factorial(n) / (factorial(k) * factorial(n - k))) # binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:k, call_argument:n, composition, function_call:factorial, function_call:int, function_tail_call:int, multiplication_operator, return

# ----------------------------------------------------------------------------------------
# problem_16/sol1.py
# ----------------------------------------------------------------------------------------
def solution(power): # function:solution (-> +7), function_argument:power, function_argument_flavor:arg, function_returning_something:solution (-> +7)
    num = 2 ** power # assignment:Pow, assignment_lhs_identifier:num, assignment_rhs_atom:2, assignment_rhs_atom:power, binary_operator:Pow, literal:2, single_assignment:num
    string_num = str(num) # assignment:str, assignment_lhs_identifier:string_num, assignment_rhs_atom:num, call_argument:num, function_call:str, single_assignment:string_num
    list_num = list(string_num) # assignment:list, assignment_lhs_identifier:list_num, assignment_rhs_atom:string_num, call_argument:string_num, function_call:list, single_assignment:list_num
    sum_of_num = 0 # assignment:0, assignment_lhs_identifier:sum_of_num, assignment_rhs_atom:0, literal:0, single_assignment:sum_of_num
    for i in list_num: # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), for:i (-> +1), for_each (-> +1), loop:for (-> +1)
        sum_of_num += int(i) # assignment_lhs_identifier:sum_of_num, assignment_rhs_atom:i, augmented_assignment:Add, call_argument:i, function_call:int, update:sum_of_num:i, update_by_augmented_assignment:sum_of_num:i, update_by_augmented_assignment_with:Add, update_with:Add
    return sum_of_num # return:sum_of_num

# ----------------------------------------------------------------------------------------
# problem_16/sol2.py
# ----------------------------------------------------------------------------------------
def solution(power): # function:solution (-> +5), function_argument:power, function_argument_flavor:arg, function_returning_something:solution (-> +5)
    n = 2 ** power # assignment:Pow, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:power, binary_operator:Pow, literal:2, single_assignment:n
    r = 0 # assignment:0, assignment_lhs_identifier:r, assignment_rhs_atom:0, literal:0, single_assignment:r
    while n: # loop:while (-> +1), while (-> +1)
        r, n = r + n % 10, n // 10 # addition_operator, assignment, assignment_lhs_identifier:n, assignment_lhs_identifier:r, assignment_rhs_atom:10, assignment_rhs_atom:n, assignment_rhs_atom:r, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mod, literal:10, modulo_operator, parallel_assignment:2, suggest_constant_definition, update:n:10, update:n:r, update:r:10, update:r:n, update_by_assignment:n:10, update_by_assignment:n:r, update_by_assignment:r:10, update_by_assignment:r:n, update_by_assignment_with, update_with
    return r # return:r

# ----------------------------------------------------------------------------------------
# problem_17/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +17), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +17)
    ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # assignment, assignment_lhs_identifier:ones_counts, assignment_rhs_atom:0, assignment_rhs_atom:3, assignment_rhs_atom:4, assignment_rhs_atom:5, assignment_rhs_atom:6, assignment_rhs_atom:7, assignment_rhs_atom:8, assignment_rhs_atom:9, literal:0, literal:3, literal:4, literal:5, literal:6, literal:7, literal:8, literal:9, literal:List, single_assignment:ones_counts, suggest_constant_definition
    tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6] # assignment, assignment_lhs_identifier:tens_counts, assignment_rhs_atom:0, assignment_rhs_atom:5, assignment_rhs_atom:6, assignment_rhs_atom:7, literal:0, literal:5, literal:6, literal:7, literal:List, single_assignment:tens_counts, suggest_constant_definition
    count = 0 # assignment:0, assignment_lhs_identifier:count, assignment_rhs_atom:0, literal:0, single_assignment:count
    for i in range(1, n + 1): # accumulate_elements:Add (-> +12), accumulate_some_elements:Add (-> +12), addition_operator, binary_operator:Add, call_argument:, call_argument:1, for:i (-> +12), for_range:1:_ (-> +12), function_call:range, literal:1, loop:for (-> +12), range:1:_
        if i < 1000: # comparison_operator:Lt, if (-> +11), if_test_atom:1000, if_test_atom:i, literal:1000, suggest_constant_definition
            if i >= 100: # comparison_operator:GtE, if (-> +3), if_test_atom:100, if_test_atom:i, if_then_branch (-> +8), if_without_else (-> +3), literal:100, nested_if:1 (-> +3), suggest_constant_definition
                count += ones_counts[i // 100] + 7 # addition_operator, assignment_lhs_identifier:count, assignment_rhs_atom:100, assignment_rhs_atom:7, assignment_rhs_atom:i, assignment_rhs_atom:ones_counts, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, if_then_branch (-> +2), index:_, index_arithmetic, literal:100, literal:7, suggest_constant_definition, update:count:100, update:count:7, update:count:i, update:count:ones_counts, update_by_augmented_assignment:count:100, update_by_augmented_assignment:count:7, update_by_augmented_assignment:count:i, update_by_augmented_assignment:count:ones_counts, update_by_augmented_assignment_with:Add, update_with:Add
                if i % 100 != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test:100, if (-> +1), if_test_atom:0, if_test_atom:100, if_test_atom:i, if_without_else (-> +1), literal:0, literal:100, modulo_operator, nested_if:2 (-> +1), suggest_constant_definition
                    count += 3 # assignment_lhs_identifier:count, assignment_rhs_atom:3, augmented_assignment:Add, if_then_branch, literal:3, suggest_constant_definition, update:count:3, update_by_augmented_assignment:count:3, update_by_augmented_assignment_with:Add, update_with:Add
            if 0 < i % 100 < 20: # binary_operator:Mod, chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +4), if_test_atom:0, if_test_atom:100, if_test_atom:20, if_test_atom:i, literal:0, literal:100, literal:20, modulo_operator, nested_if:1 (-> +4), suggest_constant_definition, yoda_comparison:Lt
                count += ones_counts[i % 100] # assignment_lhs_identifier:count, assignment_rhs_atom:100, assignment_rhs_atom:i, assignment_rhs_atom:ones_counts, augmented_assignment:Add, binary_operator:Mod, if_then_branch, index:_, index_arithmetic, literal:100, modulo_operator, suggest_constant_definition, update:count:100, update:count:i, update:count:ones_counts, update_by_augmented_assignment:count:100, update_by_augmented_assignment:count:i, update_by_augmented_assignment:count:ones_counts, update_by_augmented_assignment_with:Add, update_with:Add
            else:
                count += ones_counts[i % 10] # assignment_lhs_identifier:count, assignment_rhs_atom:10, assignment_rhs_atom:i, assignment_rhs_atom:ones_counts, augmented_assignment:Add, binary_operator:Mod, if_else_branch (-> +1), index:_, index_arithmetic, literal:10, modulo_operator, suggest_constant_definition, update:count:10, update:count:i, update:count:ones_counts, update_by_augmented_assignment:count:10, update_by_augmented_assignment:count:i, update_by_augmented_assignment:count:ones_counts, update_by_augmented_assignment_with:Add, update_with:Add
                count += tens_counts[(i % 100 - i % 10) // 10] # assignment_lhs_identifier:count, assignment_rhs_atom:10, assignment_rhs_atom:100, assignment_rhs_atom:i, assignment_rhs_atom:tens_counts, augmented_assignment:Add, binary_operator:FloorDiv, binary_operator:Mod, binary_operator:Sub, index:_, index_arithmetic, literal:10, literal:100, modulo_operator, suggest_constant_definition, update:count:10, update:count:100, update:count:i, update:count:tens_counts, update_by_augmented_assignment:count:10, update_by_augmented_assignment:count:100, update_by_augmented_assignment:count:i, update_by_augmented_assignment:count:tens_counts, update_by_augmented_assignment_with:Add, update_with:Add
        else:
            count += ones_counts[i // 1000] + 8 # addition_operator, assignment_lhs_identifier:count, assignment_rhs_atom:1000, assignment_rhs_atom:8, assignment_rhs_atom:i, assignment_rhs_atom:ones_counts, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, if_else_branch, index:_, index_arithmetic, literal:1000, literal:8, suggest_constant_definition, update:count:1000, update:count:8, update:count:i, update:count:ones_counts, update_by_augmented_assignment:count:1000, update_by_augmented_assignment:count:8, update_by_augmented_assignment:count:i, update_by_augmented_assignment:count:ones_counts, update_by_augmented_assignment_with:Add, update_with:Add
    return count # return:count

# ----------------------------------------------------------------------------------------
# problem_18/solution.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +17), function_returning_something:solution (-> +17), function_without_arguments:solution (-> +17)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment:dirname, assignment_lhs_identifier:script_dir, assignment_rhs_atom:__file__, assignment_rhs_atom:os, call_argument:, call_argument:__file__, composition, method_call:dirname, method_call:realpath, single_assignment:script_dir
    triangle = os.path.join(script_dir, "triangle.txt") # assignment:join, assignment_lhs_identifier:triangle, assignment_rhs_atom:os, assignment_rhs_atom:script_dir, call_argument:, call_argument:script_dir, literal:Str, method_call:join, single_assignment:triangle
    with open(triangle, "r") as f: # call_argument:, call_argument:triangle, function_call:open, literal:Str
        triangle = f.readlines() # assignment:readlines, assignment_lhs_identifier:triangle, assignment_rhs_atom:f, method_call:readlines, single_assignment:triangle
    a = [[int(y) for y in x.rstrip("\r\n").split(" ")] for x in triangle] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:triangle, assignment_rhs_atom:x, assignment_rhs_atom:y, call_argument:, call_argument:y, comprehension:List, comprehension_for_count:1, function_call:int, literal:Str, method_call:rstrip, method_call:split, method_call_object:x, method_chaining, single_assignment:a
    for i in range(1, len(a)): # call_argument:, call_argument:1, call_argument:a, composition, for:i (-> +10), for_range:1:_ (-> +10), for_range:_ (-> +10), function_call:len, function_call:range, literal:1, loop:for (-> +10), range:1:_
        for j in range(len(a[i])): # call_argument:, composition, for:j (-> +9), for_indexes (-> +9), for_range:_ (-> +9), function_call:len, function_call:range, index:i, loop:for (-> +9), nested_for:1 (-> +9), range:_
            if j != len(a[i - 1]): # binary_operator:Sub, call_argument:, comparison_operator:NotEq, function_call:len, if (-> +3), if_test_atom:1, if_test_atom:a, if_test_atom:i, if_test_atom:j, index:_, index_arithmetic, literal:1, verbose_conditional_assignment (-> +3)
                number1 = a[i - 1][j] # assignment, assignment_lhs_identifier:number1, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Sub, if_then_branch, index:_, index:j, index_arithmetic, literal:1, nested_index:2, single_assignment:number1
            else:
                number1 = 0 # assignment:0, assignment_lhs_identifier:number1, assignment_rhs_atom:0, if_else_branch, literal:0, single_assignment:number1
            if j > 0: # comparison_operator:Gt, if (-> +3), if_test_atom:0, if_test_atom:j, literal:0, verbose_conditional_assignment (-> +3)
                number2 = a[i - 1][j - 1] # assignment, assignment_lhs_identifier:number2, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Sub, if_then_branch, index:_, index_arithmetic, literal:1, nested_index:2, single_assignment:number2
            else:
                number2 = 0 # assignment:0, assignment_lhs_identifier:number2, assignment_rhs_atom:0, if_else_branch, literal:0, single_assignment:number2
            a[i][j] += max(number1, number2) # assignment_rhs_atom:number1, assignment_rhs_atom:number2, augmented_assignment:Add, call_argument:number1, call_argument:number2, function_call:max, index:i, index:j, nested_index:2, subscript_augmented_assignment:Add
    return max(a[-1]) # call_argument:, function_call:max, function_tail_call:max, index:-1, literal:-1, negative_index:-1, return

# ----------------------------------------------------------------------------------------
# problem_19/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +24), function_returning_something:solution (-> +24), function_without_arguments:solution (-> +24)
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # assignment, assignment_lhs_identifier:days_per_month, assignment_rhs_atom:28, assignment_rhs_atom:30, assignment_rhs_atom:31, literal:28, literal:30, literal:31, literal:List, single_assignment:days_per_month, suggest_constant_definition
    day = 6 # assignment:6, assignment_lhs_identifier:day, assignment_rhs_atom:6, literal:6, single_assignment:day, suggest_constant_definition
    month = 1 # assignment:1, assignment_lhs_identifier:month, assignment_rhs_atom:1, literal:1, single_assignment:month
    year = 1901 # assignment:1901, assignment_lhs_identifier:year, assignment_rhs_atom:1901, literal:1901, single_assignment:year, suggest_constant_definition
    sundays = 0 # assignment:0, assignment_lhs_identifier:sundays, assignment_rhs_atom:0, literal:0, single_assignment:sundays
    while year < 2001: # comparison_operator:Lt, count_states:sundays (-> +17), count_states:year (-> +17), literal:2001, loop:while (-> +17), suggest_constant_definition, while (-> +17)
        day += 7 # assignment_lhs_identifier:day, assignment_rhs_atom:7, augmented_assignment:Add, literal:7, suggest_constant_definition, update:day:7, update_by_augmented_assignment:day:7, update_by_augmented_assignment_with:Add, update_with:Add
        if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0): # binary_operator:Mod, boolean_operator:And, boolean_operator:Or, comparison_operator:Eq, divisibility_test:100, divisibility_test:4, divisibility_test:400, if (-> +10), if_test_atom:0, if_test_atom:100, if_test_atom:4, if_test_atom:400, if_test_atom:year, literal:0, literal:100, literal:4, literal:400, modulo_operator, suggest_constant_definition, unary_operator:Not
            if day > days_per_month[month - 1] and month != 2: # binary_operator:Sub, boolean_operator:And, comparison_operator:Gt, comparison_operator:NotEq, if (-> +5), if_test_atom:1, if_test_atom:2, if_test_atom:day, if_test_atom:days_per_month, if_test_atom:month, if_then_branch (-> +5), index:_, index_arithmetic, literal:1, literal:2, nested_if:1 (-> +5)
                month += 1 # assignment_lhs_identifier:month, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch (-> +1), increment:month, literal:1, update:month:1, update_by_augmented_assignment:month:1, update_by_augmented_assignment_with:Add, update_with:Add
                day = day - days_per_month[month - 2] # assignment:Sub, assignment_lhs_identifier:day, assignment_rhs_atom:2, assignment_rhs_atom:day, assignment_rhs_atom:days_per_month, assignment_rhs_atom:month, binary_operator:Sub, index:_, index_arithmetic, literal:2, single_assignment:day, suggest_augmented_assignment, update:day:2, update:day:days_per_month, update:day:month, update_by_assignment:day:2, update_by_assignment:day:days_per_month, update_by_assignment:day:month, update_by_assignment_with:Sub, update_with:Sub
            elif day > 29 and month == 2: # boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, if (-> +2), if_test_atom:2, if_test_atom:29, if_test_atom:day, if_test_atom:month, literal:2, literal:29, nested_if:1 (-> +2), suggest_constant_definition
                month += 1 # assignment_lhs_identifier:month, assignment_rhs_atom:1, augmented_assignment:Add, if_elif_branch (-> +1), increment:month, literal:1, update:month:1, update_by_augmented_assignment:month:1, update_by_augmented_assignment_with:Add, update_with:Add
                day = day - 29 # assignment:Sub, assignment_lhs_identifier:day, assignment_rhs_atom:29, assignment_rhs_atom:day, binary_operator:Sub, literal:29, single_assignment:day, suggest_augmented_assignment, suggest_constant_definition, update:day:29, update_by_assignment:day:29, update_by_assignment_with:Sub, update_with:Sub
        else:
            if day > days_per_month[month - 1]: # binary_operator:Sub, comparison_operator:Gt, if (-> +2), if_test_atom:1, if_test_atom:day, if_test_atom:days_per_month, if_test_atom:month, index:_, index_arithmetic, literal:1
                month += 1 # assignment_lhs_identifier:month, assignment_rhs_atom:1, augmented_assignment:Add, if_elif_branch (-> +1), increment:month, literal:1, update:month:1, update_by_augmented_assignment:month:1, update_by_augmented_assignment_with:Add, update_with:Add
                day = day - days_per_month[month - 2] # assignment:Sub, assignment_lhs_identifier:day, assignment_rhs_atom:2, assignment_rhs_atom:day, assignment_rhs_atom:days_per_month, assignment_rhs_atom:month, binary_operator:Sub, index:_, index_arithmetic, literal:2, single_assignment:day, suggest_augmented_assignment, update:day:2, update:day:days_per_month, update:day:month, update_by_assignment:day:2, update_by_assignment:day:days_per_month, update_by_assignment:day:month, update_by_assignment_with:Sub, update_with:Sub
        if month > 12: # comparison_operator:Gt, if (-> +2), if_test_atom:12, if_test_atom:month, if_without_else (-> +2), literal:12, suggest_constant_definition
            year += 1 # assignment_lhs_identifier:year, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch (-> +1), increment:year, literal:1, update:year:1, update_by_augmented_assignment:year:1, update_by_augmented_assignment_with:Add, update_with:Add
            month = 1 # assignment:1, assignment_lhs_identifier:month, assignment_rhs_atom:1, literal:1, single_assignment:month
        if year < 2001 and day == 1: # boolean_operator:And, comparison_operator:Eq, comparison_operator:Lt, if (-> +1), if_test_atom:1, if_test_atom:2001, if_test_atom:day, if_test_atom:year, if_without_else (-> +1), literal:1, literal:2001, suggest_constant_definition
            sundays += 1 # assignment_lhs_identifier:sundays, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment:sundays, literal:1, update:sundays:1, update_by_augmented_assignment:sundays:1, update_by_augmented_assignment_with:Add, update_with:Add
    return sundays # return:sundays

# ----------------------------------------------------------------------------------------
# problem_20/sol1.py
# ----------------------------------------------------------------------------------------
def factorial(n): # function:factorial (-> +4), function_argument:n, function_argument_flavor:arg, function_returning_something:factorial (-> +4)
    fact = 1 # assignment:1, assignment_lhs_identifier:fact, assignment_rhs_atom:1, literal:1, single_assignment:fact
    for i in range(1, n + 1): # accumulate_all_elements:Mult (-> +1), accumulate_elements:Mult (-> +1), addition_operator, binary_operator:Add, call_argument:, call_argument:1, for:i (-> +1), for_range:1:_ (-> +1), function_call:range, literal:1, loop:for (-> +1), range:1:_
        fact *= i # assignment_lhs_identifier:fact, assignment_rhs_atom:i, augmented_assignment:Mult, update:fact:i, update_by_augmented_assignment:fact:i, update_by_augmented_assignment_with:Mult, update_with:Mult
    return fact # return:fact
def split_and_add(number): # function:split_and_add (-> +6), function_argument:number, function_argument_flavor:arg, function_returning_something:split_and_add (-> +6)
    sum_of_digits = 0 # assignment:0, assignment_lhs_identifier:sum_of_digits, assignment_rhs_atom:0, literal:0, single_assignment:sum_of_digits
    while number > 0: # comparison_operator:Gt, literal:0, loop:while (-> +3), while (-> +3)
        last_digit = number % 10 # assignment:Mod, assignment_lhs_identifier:last_digit, assignment_rhs_atom:10, assignment_rhs_atom:number, binary_operator:Mod, literal:10, modulo_operator, single_assignment:last_digit, suggest_constant_definition
        sum_of_digits += last_digit # assignment_lhs_identifier:sum_of_digits, assignment_rhs_atom:last_digit, augmented_assignment:Add, update:sum_of_digits:last_digit, update_by_augmented_assignment:sum_of_digits:last_digit, update_by_augmented_assignment_with:Add, update_with:Add
        number = number // 10 # assignment:FloorDiv, assignment_lhs_identifier:number, assignment_rhs_atom:10, assignment_rhs_atom:number, binary_operator:FloorDiv, literal:10, single_assignment:number, suggest_augmented_assignment, suggest_constant_definition, update:number:10, update_by_assignment:number:10, update_by_assignment_with:FloorDiv, update_with:FloorDiv
    return sum_of_digits # return:sum_of_digits
def solution(n): # function:solution (-> +3), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +3)
    f = factorial(n) # assignment:factorial, assignment_lhs_identifier:f, assignment_rhs_atom:n, call_argument:n, function_call:factorial, single_assignment:f
    result = split_and_add(f) # assignment:split_and_add, assignment_lhs_identifier:result, assignment_rhs_atom:f, call_argument:f, function_call:split_and_add, single_assignment:result
    return result # return:result

# ----------------------------------------------------------------------------------------
# problem_20/sol2.py
# ----------------------------------------------------------------------------------------
from math import factorial # import:math:factorial, import_module:math, import_name:factorial
def solution(n): # function:solution (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return sum([int(x) for x in str(factorial(n))]) # call_argument:, call_argument:n, call_argument:x, composition, comprehension:List, comprehension_for_count:1, function_call:factorial, function_call:int, function_call:str, function_call:sum, function_tail_call:sum, return

# ----------------------------------------------------------------------------------------
# problem_20/sol3.py
# ----------------------------------------------------------------------------------------
from math import factorial # import:math:factorial, import_module:math, import_name:factorial
def solution(n): # function:solution (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return sum(map(int, str(factorial(n)))) # call_argument:, call_argument:int, call_argument:n, composition, function_call:factorial, function_call:map, function_call:str, function_call:sum, function_tail_call:sum, return

# ----------------------------------------------------------------------------------------
# problem_20/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +7)
    fact = 1 # assignment:1, assignment_lhs_identifier:fact, assignment_rhs_atom:1, literal:1, single_assignment:fact
    result = 0 # assignment:0, assignment_lhs_identifier:result, assignment_rhs_atom:0, literal:0, single_assignment:result
    for i in range(1, n + 1): # accumulate_all_elements:Mult (-> +1), accumulate_elements:Mult (-> +1), addition_operator, binary_operator:Add, call_argument:, call_argument:1, for:i (-> +1), for_range:1:_ (-> +1), function_call:range, literal:1, loop:for (-> +1), range:1:_
        fact *= i # assignment_lhs_identifier:fact, assignment_rhs_atom:i, augmented_assignment:Mult, update:fact:i, update_by_augmented_assignment:fact:i, update_by_augmented_assignment_with:Mult, update_with:Mult
    for j in str(fact): # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), call_argument:fact, for:j (-> +1), function_call:str, loop:for (-> +1)
        result += int(j) # assignment_lhs_identifier:result, assignment_rhs_atom:j, augmented_assignment:Add, call_argument:j, function_call:int, update:result:j, update_by_augmented_assignment:result:j, update_by_augmented_assignment_with:Add, update_with:Add
    return result # return:result

# ----------------------------------------------------------------------------------------
# problem_21/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt
def sum_of_divisors(n): # function:sum_of_divisors (-> +7), function_argument:n, function_argument_flavor:arg, function_returning_something:sum_of_divisors (-> +7)
    total = 0 # assignment:0, assignment_lhs_identifier:total, assignment_rhs_atom:0, literal:0, single_assignment:total
    for i in range(1, int(sqrt(n) + 1)): # accumulate_elements:Add (-> +4), accumulate_some_elements:Add (-> +4), addition_operator, binary_operator:Add, call_argument:, call_argument:1, call_argument:n, composition, for:i (-> +4), for_range:1:_ (-> +4), function_call:int, function_call:range, function_call:sqrt, literal:1, loop:for (-> +4), range:1:_
        if n % i == 0 and i != sqrt(n): # binary_operator:Mod, boolean_operator:And, call_argument:n, comparison_operator:Eq, comparison_operator:NotEq, divisibility_test, function_call:sqrt, if (-> +3), if_test_atom:0, if_test_atom:i, if_test_atom:n, literal:0, modulo_operator
            total += i + n // i # addition_operator, assignment_lhs_identifier:total, assignment_rhs_atom:i, assignment_rhs_atom:n, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, if_then_branch, update:total:i, update:total:n, update_by_augmented_assignment:total:i, update_by_augmented_assignment:total:n, update_by_augmented_assignment_with:Add, update_with:Add
        elif i == sqrt(n): # call_argument:n, comparison_operator:Eq, function_call:sqrt, if (-> +1), if_test_atom:i, if_test_atom:n
            total += i # assignment_lhs_identifier:total, assignment_rhs_atom:i, augmented_assignment:Add, if_elif_branch, update:total:i, update_by_augmented_assignment:total:i, update_by_augmented_assignment_with:Add, update_with:Add
    return total - n # binary_operator:Sub, return
def solution(n): # function:solution (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +8)
    total = sum( # assignment:sum, assignment_lhs_identifier:total, composition, function_call:sum, single_assignment:total
        [
            i # assignment_rhs_atom:i, call_argument:, comprehension:List, comprehension_for_count:1
            for i in range(1, n) # assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:n, call_argument:1, call_argument:n, function_call:range, literal:1, range:1:n
            if sum_of_divisors(sum_of_divisors(i)) == i and sum_of_divisors(i) != i # assignment_rhs_atom:i, boolean_operator:And, call_argument:, call_argument:i, comparison_operator:Eq, comparison_operator:NotEq, composition, filtered_comprehension, function_call:sum_of_divisors
        ]
    )
    return total # return:total

# ----------------------------------------------------------------------------------------
# problem_22/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +12), function_returning_something:solution (-> +12), function_without_arguments:solution (-> +12)
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator:Add, call_argument:, call_argument:__file__, composition, concatenation_operator:Str, function_call:open, literal:Str, method_call:dirname
        names = str(file.readlines()[0]) # assignment:str, assignment_lhs_identifier:names, assignment_rhs_atom:0, assignment_rhs_atom:file, call_argument:, composition, function_call:str, index:0, literal:0, method_call:readlines, method_call_object:file, single_assignment:names
        names = names.replace('"', "").split(",") # assignment:split, assignment_lhs_identifier:names, assignment_rhs_atom:names, call_argument:, empty_literal:Str, literal:Str, method_call:replace, method_call:split, method_call_object:names, method_chaining, single_assignment:names
    names.sort() # method_call:sort, method_call_object:names, method_call_without_result:sort
    name_score = 0 # assignment:0, assignment_lhs_identifier:name_score, assignment_rhs_atom:0, literal:0, single_assignment:name_score
    total_score = 0 # assignment:0, assignment_lhs_identifier:total_score, assignment_rhs_atom:0, literal:0, single_assignment:total_score
    for i, name in enumerate(names): # accumulate_all_elements:Add, accumulate_elements:Add, call_argument:names, for:i, for_indexes_elements (-> +4), function_call:enumerate, loop:for
        for letter in name: # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), for:letter (-> +1), for_each (-> +1), loop:for (-> +1), nested_for:1 (-> +1)
            name_score += ord(letter) - 64 # assignment_lhs_identifier:name_score, assignment_rhs_atom:64, assignment_rhs_atom:letter, augmented_assignment:Add, binary_operator:Sub, call_argument:letter, function_call:ord, literal:64, suggest_constant_definition, update:name_score:64, update:name_score:letter, update_by_augmented_assignment:name_score:64, update_by_augmented_assignment:name_score:letter, update_by_augmented_assignment_with:Add, update_with:Add
        total_score += (i + 1) * name_score # addition_operator, assignment_lhs_identifier:total_score, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:name_score, augmented_assignment:Add, binary_operator:Add, binary_operator:Mult, literal:1, multiplication_operator, update:total_score:1, update:total_score:i, update:total_score:name_score, update_by_augmented_assignment:total_score:1, update_by_augmented_assignment:total_score:i, update_by_augmented_assignment:total_score:name_score, update_by_augmented_assignment_with:Add, update_with:Add
        name_score = 0 # assignment:0, assignment_lhs_identifier:name_score, assignment_rhs_atom:0, for:name, literal:0, loop:for, nested_for:1, single_assignment:name_score
    return total_score # return:total_score

# ----------------------------------------------------------------------------------------
# problem_22/sol2.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +12), function_returning_something:solution (-> +12), function_without_arguments:solution (-> +12)
    total_sum = 0 # assignment:0, assignment_lhs_identifier:total_sum, assignment_rhs_atom:0, literal:0, single_assignment:total_sum
    temp_sum = 0 # assignment:0, assignment_lhs_identifier:temp_sum, assignment_rhs_atom:0, literal:0, single_assignment:temp_sum
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator:Add, call_argument:, call_argument:__file__, composition, concatenation_operator:Str, function_call:open, literal:Str, method_call:dirname
        name = str(file.readlines()[0]) # assignment:str, assignment_lhs_identifier:name, assignment_rhs_atom:0, assignment_rhs_atom:file, call_argument:, composition, function_call:str, index:0, literal:0, method_call:readlines, method_call_object:file, single_assignment:name
        name = name.replace('"', "").split(",") # assignment:split, assignment_lhs_identifier:name, assignment_rhs_atom:name, call_argument:, empty_literal:Str, literal:Str, method_call:replace, method_call:split, method_call_object:name, method_chaining, single_assignment:name
    name.sort() # method_call:sort, method_call_object:name, method_call_without_result:sort
    for i in range(len(name)): # accumulate_all_elements:Add (-> +4), accumulate_elements:Add (-> +4), call_argument:, call_argument:name, composition, for:i (-> +4), for_indexes (-> +4), for_range:_ (-> +4), function_call:len, function_call:range, loop:for (-> +4), range:_
        for j in name[i]: # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), for:j (-> +1), index:i, loop:for (-> +1), nested_for:1 (-> +1)
            temp_sum += ord(j) - ord("A") + 1 # addition_operator, assignment_lhs_identifier:temp_sum, assignment_rhs_atom:1, assignment_rhs_atom:j, augmented_assignment:Add, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:j, function_call:ord, literal:1, literal:Str, update:temp_sum:1, update:temp_sum:j, update_by_augmented_assignment:temp_sum:1, update_by_augmented_assignment:temp_sum:j, update_by_augmented_assignment_with:Add, update_with:Add
        total_sum += (i + 1) * temp_sum # addition_operator, assignment_lhs_identifier:total_sum, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:temp_sum, augmented_assignment:Add, binary_operator:Add, binary_operator:Mult, literal:1, multiplication_operator, update:total_sum:1, update:total_sum:i, update:total_sum:temp_sum, update_by_augmented_assignment:total_sum:1, update_by_augmented_assignment:total_sum:i, update_by_augmented_assignment:total_sum:temp_sum, update_by_augmented_assignment_with:Add, update_with:Add
        temp_sum = 0 # assignment:0, assignment_lhs_identifier:temp_sum, assignment_rhs_atom:0, literal:0, single_assignment:temp_sum
    return total_sum # return:total_sum

# ----------------------------------------------------------------------------------------
# problem_23/sol1.py
# ----------------------------------------------------------------------------------------
def solution(limit=28123): # function:solution (-> +13), function_argument:limit, function_argument_flavor:arg, function_returning_something:solution (-> +13), literal:28123
    sumDivs = [1] * (limit + 1) # addition_operator, assignment:Mult, assignment_lhs_identifier:sumDivs, assignment_rhs_atom:1, assignment_rhs_atom:limit, binary_operator:Add, binary_operator:Mult, literal:1, literal:List, replication_operator:List, single_assignment:sumDivs
    for i in range(2, int(limit ** 0.5) + 1): # accumulate_all_elements:Add (-> +3), accumulate_elements:Add (-> +3), addition_operator, binary_operator:Add, binary_operator:Pow, call_argument:, call_argument:2, composition, for:i (-> +3), for_range:2:_ (-> +3), for_range:_:_ (-> +3), function_call:int, function_call:range, literal:0.5, literal:1, literal:2, loop:for (-> +3), range:2:_, suggest_constant_definition
        sumDivs[i * i] += i # assignment_lhs_identifier:sumDivs, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Mult, index:_, index_arithmetic, multiplication_operator, subscript_augmented_assignment:Add, update:sumDivs:i, update_by_augmented_assignment:sumDivs:i, update_by_augmented_assignment_with:Add, update_with:Add
        for k in range(i + 1, limit // i + 1): # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), addition_operator, binary_operator:Add, binary_operator:FloorDiv, call_argument:, for:k (-> +1), for_range:_:_ (-> +1), function_call:range, literal:1, loop:for (-> +1), nested_for:1 (-> +1), range:_:_
            sumDivs[k * i] += k + i # addition_operator, assignment_lhs_identifier:sumDivs, assignment_rhs_atom:i, assignment_rhs_atom:k, augmented_assignment:Add, binary_operator:Add, binary_operator:Mult, index:_, index_arithmetic, multiplication_operator, subscript_augmented_assignment:Add, update:sumDivs:i, update:sumDivs:k, update_by_augmented_assignment:sumDivs:i, update_by_augmented_assignment:sumDivs:k, update_by_augmented_assignment_with:Add, update_with:Add
    abundants = set() # assignment:set, assignment_lhs_identifier:abundants, function_call:set, function_call_without_arguments:set, single_assignment:abundants
    res = 0 # assignment:0, assignment_lhs_identifier:res, assignment_rhs_atom:0, literal:0, single_assignment:res
    for n in range(1, limit + 1): # accumulate_elements:Add (-> +4), accumulate_elements:add (-> +4), accumulate_some_elements:Add (-> +4), accumulate_some_elements:add (-> +4), addition_operator, binary_operator:Add, call_argument:, call_argument:1, for:n (-> +4), for_range:1:_ (-> +4), function_call:range, literal:1, loop:for (-> +4), range:1:_
        if sumDivs[n] > n: # comparison_operator:Gt, if (-> +1), if_test_atom:n, if_test_atom:sumDivs, if_without_else (-> +1), index:n
            abundants.add(n) # call_argument:n, if_then_branch, method_call:add, method_call_object:abundants, method_call_without_result:add, update:abundants:n, update_by_method_call:abundants:n, update_by_method_call_with:add, update_with:add
        if not any((n - a in abundants) for a in abundants): # binary_operator:Sub, call_argument:, comparison_operator:In, comprehension:Generator, comprehension_for_count:1, function_call:any, if (-> +1), if_test_atom:a, if_test_atom:abundants, if_test_atom:n, if_without_else (-> +1), unary_operator:Not
            res += n # assignment_lhs_identifier:res, assignment_rhs_atom:n, augmented_assignment:Add, if_then_branch, update:res:n, update_by_augmented_assignment:res:n, update_by_augmented_assignment_with:Add, update_with:Add
    return res # return:res

# ----------------------------------------------------------------------------------------
# problem_234/sol1.py
# ----------------------------------------------------------------------------------------
def fib(a, b, n): # function:fib (-> +13), function_argument:a, function_argument:b, function_argument:n, function_argument_flavor:arg, function_returning_something:fib (-> +13)
    if n == 1: # comparison_operator:Eq, if (-> +5), if_test_atom:1, if_test_atom:n, literal:1
        return a # if_then_branch, return:a
    elif n == 2: # comparison_operator:Eq, if (-> +3), if_test_atom:2, if_test_atom:n, literal:2
        return b # if_elif_branch, return:b
    elif n == 3: # comparison_operator:Eq, if (-> +1), if_test_atom:3, if_test_atom:n, literal:3, suggest_constant_definition
        return str(a) + str(b) # addition_operator, binary_operator:Add, call_argument:a, call_argument:b, function_call:str, if_elif_branch, return
    temp = 0 # assignment:0, assignment_lhs_identifier:temp, assignment_rhs_atom:0, literal:0, single_assignment:temp
    for x in range(2, n): # call_argument:2, call_argument:n, for:x (-> +4), for_range:2:n (-> +4), function_call:range, literal:2, loop:for (-> +4), range:2:n
        c = str(a) + str(b) # addition_operator, assignment:Add, assignment_lhs_identifier:c, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, call_argument:a, call_argument:b, function_call:str, single_assignment:c
        temp = b # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:b, single_assignment:temp
        b = c # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:c, single_assignment:b
        a = temp # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:temp, single_assignment:a
    return c # return:c
def solution(n): # function:solution (-> +11), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +11)
    semidivisible = [] # assignment, assignment_lhs_identifier:semidivisible, empty_literal:List, literal:List, single_assignment:semidivisible
    for x in range(n): # call_argument:n, for:x (-> +8), for_range:n (-> +8), function_call:range, loop:for (-> +8), range:n
        l = [i for i in input().split()] # assignment, assignment_lhs_identifier:l, assignment_rhs_atom:i, comprehension:List, comprehension_for_count:1, function_call:input, function_call_without_arguments:input, method_call:split, single_assignment:l
        c2 = 1 # assignment:1, assignment_lhs_identifier:c2, assignment_rhs_atom:1, literal:1, single_assignment:c2
        while 1: # count_states:c2 (-> +4), infinite_while (-> +4), literal:1, loop:while (-> +4), loop_with_early_exit:while:break (-> +4), while (-> +4)
            if len(fib(l[0], l[1], c2)) < int(l[2]): # call_argument:, call_argument:c2, comparison_operator:Lt, composition, function_call:fib, function_call:int, function_call:len, if (-> +3), if_test_atom:0, if_test_atom:1, if_test_atom:2, if_test_atom:c2, if_test_atom:l, index:0, index:1, index:2, literal:0, literal:1, literal:2
                c2 += 1 # assignment_lhs_identifier:c2, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment:c2, literal:1, update:c2:1, update_by_augmented_assignment:c2:1, update_by_augmented_assignment_with:Add, update_with:Add
            else:
                break # break, if_else_branch
        semidivisible.append(fib(l[0], l[1], c2 + 1)[int(l[2]) - 1]) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, composition, function_call:fib, function_call:int, index:0, index:1, index:2, index:_, index_arithmetic, literal:0, literal:1, literal:2, method_call:append, method_call_object:semidivisible, method_call_without_result:append, nested_index:4
    return semidivisible # return:semidivisible

# ----------------------------------------------------------------------------------------
# problem_24/sol1.py
# ----------------------------------------------------------------------------------------
from itertools import permutations # import:itertools:permutations, import_module:itertools, import_name:permutations
def solution(): # function:solution (-> +2), function_returning_something:solution (-> +2), function_without_arguments:solution (-> +2)
    result = list(map("".join, permutations("0123456789"))) # assignment:list, assignment_lhs_identifier:result, call_argument:, composition, empty_literal:Str, function_call:list, function_call:map, function_call:permutations, literal:Str, single_assignment:result
    return result[999999] # index:999999, literal:999999, return, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# problem_25/sol1.py
# ----------------------------------------------------------------------------------------
def fibonacci(n): # function:fibonacci (-> +9), function_argument:n, function_argument_flavor:arg, function_returning_something:fibonacci (-> +9)
    if n == 1 or type(n) is not int: # boolean_operator:Or, call_argument:n, comparison_operator:Eq, comparison_operator:IsNot, function_call:type, if (-> +8), if_test_atom:1, if_test_atom:int, if_test_atom:n, literal:1
        return 0 # if_then_branch, literal:0, return:0
    elif n == 2: # comparison_operator:Eq, if (-> +6), if_test_atom:2, if_test_atom:n, literal:2
        return 1 # if_elif_branch, literal:1, return:1
    else:
        sequence = [0, 1] # assignment, assignment_lhs_identifier:sequence, assignment_rhs_atom:0, assignment_rhs_atom:1, if_else_branch (-> +3), literal:0, literal:1, literal:List, single_assignment:sequence
        for i in range(2, n + 1): # addition_operator, binary_operator:Add, call_argument:, call_argument:2, for:i (-> +1), for_range:2:_ (-> +1), function_call:range, literal:1, literal:2, loop:for (-> +1), range:2:_
            sequence.append(sequence[i - 1] + sequence[i - 2]) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, index:_, index_arithmetic, literal:1, literal:2, method_call:append, method_call_object:sequence, method_call_without_result:append
        return sequence[n] # index:n, return
def fibonacci_digits_index(n): # function:fibonacci_digits_index (-> +6), function_argument:n, function_argument_flavor:arg, function_returning_something:fibonacci_digits_index (-> +6)
    digits = 0 # assignment:0, assignment_lhs_identifier:digits, assignment_rhs_atom:0, literal:0, single_assignment:digits
    index = 2 # assignment:2, assignment_lhs_identifier:index, assignment_rhs_atom:2, literal:2, single_assignment:index
    while digits < n: # comparison_operator:Lt, count_states:index (-> +2), loop:while (-> +2), while (-> +2)
        index += 1 # assignment_lhs_identifier:index, assignment_rhs_atom:1, augmented_assignment:Add, increment:index, literal:1, update:index:1, update_by_augmented_assignment:index:1, update_by_augmented_assignment_with:Add, update_with:Add
        digits = len(str(fibonacci(index))) # assignment:len, assignment_lhs_identifier:digits, assignment_rhs_atom:index, call_argument:, call_argument:index, composition, function_call:fibonacci, function_call:len, function_call:str, single_assignment:digits
    return index # return:index
def solution(n): # function:solution (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return fibonacci_digits_index(n) # call_argument:n, function_call:fibonacci_digits_index, function_tail_call:fibonacci_digits_index, return

# ----------------------------------------------------------------------------------------
# problem_25/sol2.py
# ----------------------------------------------------------------------------------------
def fibonacci_generator(): # function:fibonacci_generator (-> +4), function_without_arguments:fibonacci_generator (-> +4), generator:fibonacci_generator (-> +4)
    a, b = 0, 1 # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:0, assignment_rhs_atom:1, literal:0, literal:1, literal:Tuple, parallel_assignment:2
    while True: # infinite_while (-> +2), literal:True, loop:while (-> +2), while (-> +2)
        a, b = b, a + b # addition_operator, assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, parallel_assignment:2, slide, update:a:b, update:b:a, update_by_assignment:a:b, update_by_assignment:b:a, update_by_assignment_with, update_with
        yield b # yield:b
def solution(n): # function:solution (-> +5), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +5)
    answer = 1 # assignment:1, assignment_lhs_identifier:answer, assignment_rhs_atom:1, literal:1, single_assignment:answer
    gen = fibonacci_generator() # assignment:fibonacci_generator, assignment_lhs_identifier:gen, function_call:fibonacci_generator, function_call_without_arguments:fibonacci_generator, single_assignment:gen
    while len(str(next(gen))) < n: # call_argument:, call_argument:gen, comparison_operator:Lt, composition, count_states:answer (-> +1), function_call:len, function_call:next, function_call:str, loop:while (-> +1), while (-> +1)
        answer += 1 # assignment_lhs_identifier:answer, assignment_rhs_atom:1, augmented_assignment:Add, increment:answer, literal:1, update:answer:1, update_by_augmented_assignment:answer:1, update_by_augmented_assignment_with:Add, update_with:Add
    return answer + 1 # addition_operator, binary_operator:Add, literal:1, return

# ----------------------------------------------------------------------------------------
# problem_25/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +12), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +12)
    f1, f2 = 1, 1 # assignment, assignment_lhs_identifier:f1, assignment_lhs_identifier:f2, assignment_rhs_atom:1, literal:1, literal:Tuple, parallel_assignment:2
    index = 2 # assignment:2, assignment_lhs_identifier:index, assignment_rhs_atom:2, literal:2, single_assignment:index
    while True: # count_states:index (-> +8), infinite_while (-> +8), literal:True, loop:while (-> +8), loop_with_early_exit:while:break (-> +8), while (-> +8)
        i = 0 # assignment:0, assignment_lhs_identifier:i, assignment_rhs_atom:0, literal:0, single_assignment:i
        f = f1 + f2 # addition_operator, assignment:Add, assignment_lhs_identifier:f, assignment_rhs_atom:f1, assignment_rhs_atom:f2, binary_operator:Add, single_assignment:f
        f1, f2 = f2, f # assignment, assignment_lhs_identifier:f1, assignment_lhs_identifier:f2, assignment_rhs_atom:f, assignment_rhs_atom:f2, parallel_assignment:2, slide, update:f2:f, update_by_assignment:f2:f, update_by_assignment_with, update_with
        index += 1 # assignment_lhs_identifier:index, assignment_rhs_atom:1, augmented_assignment:Add, increment:index, literal:1, update:index:1, update_by_augmented_assignment:index:1, update_by_augmented_assignment_with:Add, update_with:Add
        for j in str(f): # call_argument:f, count_elements:i (-> +1), for:j (-> +1), function_call:str, loop:for (-> +1)
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
        if i == n: # comparison_operator:Eq, if (-> +1), if_test_atom:i, if_test_atom:n, if_without_else (-> +1)
            break # break, if_then_branch
    return index # return:index

# ----------------------------------------------------------------------------------------
# problem_27/problem_27_sol1.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def is_prime(k: int) -> bool: # function:is_prime (-> +9), function_argument:k, function_argument_flavor:arg, function_returning_something:is_prime (-> +9)
    if k < 2 or k % 2 == 0: # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, comparison_operator:Lt, divisibility_test:2, if (-> +7), if_test_atom:0, if_test_atom:2, if_test_atom:k, literal:0, literal:2, modulo_operator
        return False # if_then_branch, literal:False, return:False
    elif k == 2: # comparison_operator:Eq, if (-> +5), if_test_atom:2, if_test_atom:k, literal:2
        return True # if_elif_branch, literal:True, return:True
    else:
        for x in range(3, int(math.sqrt(k) + 1), 2): # addition_operator, binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:k, composition, for:x (-> +2), for_range:3:_:2 (-> +2), function_call:int, function_call:range, if_else_branch (-> +2), literal:1, literal:2, literal:3, loop:for (-> +2), loop_with_early_exit:for:return (-> +2), method_call:sqrt, range:3:_:2, suggest_constant_definition, universal_quantification:x (-> +2)
            if k % x == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:k, if_test_atom:x, if_without_else (-> +1), literal:0, modulo_operator, nested_if:1 (-> +1)
                return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def solution(a_limit: int, b_limit: int) -> int: # function:solution (-> +13), function_argument:a_limit, function_argument:b_limit, function_argument_flavor:arg, function_returning_something:solution (-> +13)
    longest = [0, 0, 0] # assignment, assignment_lhs_identifier:longest, assignment_rhs_atom:0, literal:0, literal:List, single_assignment:longest
    for a in range((a_limit * -1) + 1, a_limit): # addition_operator, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:a_limit, for:a (-> +9), for_range:2:b_limit (-> +9), for_range:_:a_limit (-> +9), function_call:range, literal:-1, literal:1, loop:for (-> +9), multiplication_operator, range:_:a_limit
        for b in range(2, b_limit): # call_argument:2, call_argument:b_limit, for:b (-> +8), for_range:2:b_limit (-> +8), function_call:range, literal:2, loop:for (-> +8), nested_for:1 (-> +8), range:2:b_limit
            if is_prime(b): # call_argument:b, function_call:is_prime, if (-> +7), if_test_atom:b, if_without_else (-> +7)
                count = 0 # assignment:0, assignment_lhs_identifier:count, assignment_rhs_atom:0, if_then_branch (-> +6), literal:0, single_assignment:count
                n = 0 # assignment:0, assignment_lhs_identifier:n, assignment_rhs_atom:0, literal:0, single_assignment:n
                while is_prime((n ** 2) + (a * n) + b): # addition_operator, binary_operator:Add, binary_operator:Mult, binary_operator:Pow, call_argument:, count_states:count (-> +2), count_states:n (-> +2), function_call:is_prime, literal:2, loop:while (-> +2), multiplication_operator, while (-> +2)
                    count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment:Add, increment:count, literal:1, update:count:1, update_by_augmented_assignment:count:1, update_by_augmented_assignment_with:Add, update_with:Add
                    n += 1 # assignment_lhs_identifier:n, assignment_rhs_atom:1, augmented_assignment:Add, increment:n, literal:1, update:n:1, update_by_augmented_assignment:n:1, update_by_augmented_assignment_with:Add, update_with:Add
                if count > longest[0]: # comparison_operator:Gt, if (-> +1), if_test_atom:0, if_test_atom:count, if_test_atom:longest, if_without_else (-> +1), index:0, literal:0, nested_if:1 (-> +1)
                    longest = [count, a, b] # assignment, assignment_lhs_identifier:longest, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:count, if_then_branch, single_assignment:longest
    ans = longest[1] * longest[2] # assignment:Mult, assignment_lhs_identifier:ans, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:longest, binary_operator:Mult, index:1, index:2, literal:1, literal:2, multiplication_operator, single_assignment:ans
    return ans # return:ans

# ----------------------------------------------------------------------------------------
# problem_28/sol1.py
# ----------------------------------------------------------------------------------------
from math import ceil # import:math:ceil, import_module:math, import_name:ceil
def diagonal_sum(n): # function:diagonal_sum (-> +6), function_argument:n, function_argument_flavor:arg, function_returning_something:diagonal_sum (-> +6)
    total = 1 # assignment:1, assignment_lhs_identifier:total, assignment_rhs_atom:1, literal:1, single_assignment:total
    for i in range(1, int(ceil(n / 2.0))): # binary_operator:Div, call_argument:, call_argument:1, composition, for:i (-> +3), for_range:1:_ (-> +3), function_call:ceil, function_call:int, function_call:range, literal:1, literal:2.0, loop:for (-> +3), range:1:_, suggest_constant_definition
        odd = 2 * i + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:odd, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:i, binary_operator:Add, binary_operator:Mult, literal:1, literal:2, multiplication_operator, single_assignment:odd
        even = 2 * i # assignment:Mult, assignment_lhs_identifier:even, assignment_rhs_atom:2, assignment_rhs_atom:i, binary_operator:Mult, literal:2, multiplication_operator, single_assignment:even
        total = total + 4 * odd ** 2 - 6 * even # addition_operator, assignment:Sub, assignment_lhs_identifier:total, assignment_rhs_atom:2, assignment_rhs_atom:4, assignment_rhs_atom:6, assignment_rhs_atom:even, assignment_rhs_atom:odd, assignment_rhs_atom:total, binary_operator:Add, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, literal:2, literal:4, literal:6, multiplication_operator, single_assignment:total, suggest_constant_definition, update:total:2, update:total:4, update:total:6, update:total:even, update:total:odd, update_by_assignment:total:2, update_by_assignment:total:4, update_by_assignment:total:6, update_by_assignment:total:even, update_by_assignment:total:odd, update_by_assignment_with:Sub, update_with:Sub
    return total # return:total

# ----------------------------------------------------------------------------------------
# problem_29/solution.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +8)
    collectPowers = set() # assignment:set, assignment_lhs_identifier:collectPowers, function_call:set, function_call_without_arguments:set, single_assignment:collectPowers
    currentPow = 0 # assignment:0, assignment_lhs_identifier:currentPow, assignment_rhs_atom:0, literal:0, single_assignment:currentPow
    N = n + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:N, assignment_rhs_atom:1, assignment_rhs_atom:n, binary_operator:Add, literal:1, single_assignment:N
    for a in range(2, N): # call_argument:2, call_argument:N, for:a (-> +3), for_range:2:N (-> +3), function_call:range, literal:2, loop:for (-> +3), range:2:N, square_nested_for (-> +3)
        for b in range(2, N): # call_argument:2, call_argument:N, for:b (-> +2), for_range:2:N (-> +2), function_call:range, literal:2, loop:for (-> +2), nested_for:1 (-> +2), range:2:N
            currentPow = a ** b # assignment:Pow, assignment_lhs_identifier:currentPow, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Pow, single_assignment:currentPow
            collectPowers.add(currentPow) # call_argument:currentPow, method_call:add, method_call_object:collectPowers, method_call_without_result:add, update:collectPowers:currentPow, update_by_method_call:collectPowers:currentPow, update_by_method_call_with:add, update_with:add
    return len(collectPowers) # call_argument:collectPowers, function_call:len, function_tail_call:len, return

# ----------------------------------------------------------------------------------------
# problem_31/sol1.py
# ----------------------------------------------------------------------------------------
def one_pence(): # function:one_pence (-> +1), function_returning_something:one_pence (-> +1), function_without_arguments:one_pence (-> +1)
    return 1 # literal:1, return:1
def two_pence(x): # body_recursive_function:two_pence (-> +1), function:two_pence (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:two_pence (-> +1), recursive_function:two_pence (-> +1)
    return 0 if x < 0 else two_pence(x - 2) + one_pence() # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, comparison_operator:Lt, conditional_expression, function_call:one_pence, function_call:two_pence, function_call_without_arguments:one_pence, literal:0, literal:2, return
def five_pence(x): # body_recursive_function:five_pence (-> +1), function:five_pence (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:five_pence (-> +1), recursive_function:five_pence (-> +1)
    return 0 if x < 0 else five_pence(x - 5) + two_pence(x) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:five_pence, function_call:two_pence, literal:0, literal:5, return, suggest_constant_definition
def ten_pence(x): # body_recursive_function:ten_pence (-> +1), function:ten_pence (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:ten_pence (-> +1), recursive_function:ten_pence (-> +1)
    return 0 if x < 0 else ten_pence(x - 10) + five_pence(x) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:five_pence, function_call:ten_pence, literal:0, literal:10, return, suggest_constant_definition
def twenty_pence(x): # body_recursive_function:twenty_pence (-> +1), function:twenty_pence (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:twenty_pence (-> +1), recursive_function:twenty_pence (-> +1)
    return 0 if x < 0 else twenty_pence(x - 20) + ten_pence(x) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:ten_pence, function_call:twenty_pence, literal:0, literal:20, return, suggest_constant_definition
def fifty_pence(x): # body_recursive_function:fifty_pence (-> +1), function:fifty_pence (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:fifty_pence (-> +1), recursive_function:fifty_pence (-> +1)
    return 0 if x < 0 else fifty_pence(x - 50) + twenty_pence(x) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:fifty_pence, function_call:twenty_pence, literal:0, literal:50, return, suggest_constant_definition
def one_pound(x): # body_recursive_function:one_pound (-> +1), function:one_pound (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:one_pound (-> +1), recursive_function:one_pound (-> +1)
    return 0 if x < 0 else one_pound(x - 100) + fifty_pence(x) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:fifty_pence, function_call:one_pound, literal:0, literal:100, return, suggest_constant_definition
def two_pound(x): # body_recursive_function:two_pound (-> +1), function:two_pound (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:two_pound (-> +1), recursive_function:two_pound (-> +1)
    return 0 if x < 0 else two_pound(x - 200) + one_pound(x) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:one_pound, function_call:two_pound, literal:0, literal:200, return, suggest_constant_definition
def solution(n): # function:solution (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +1)
    return two_pound(n) # call_argument:n, function_call:two_pound, function_tail_call:two_pound, return

# ----------------------------------------------------------------------------------------
# problem_32/sol32.py
# ----------------------------------------------------------------------------------------
import itertools # import:itertools, import_module:itertools
def isCombinationValid(combination): # function:isCombinationValid (-> +6), function_argument:combination, function_argument_flavor:arg, function_returning_something:isCombinationValid (-> +6)
    return ( # boolean_operator:Or, return
        int("".join(combination[0:2])) * int("".join(combination[2:5])) # binary_operator:Mult, call_argument:, composition, empty_literal:Str, function_call:int, literal:0, literal:2, literal:5, literal:Str, method_call:join, multiplication_operator, slice:0:2:, slice:2:5:, slice_lower:0, slice_lower:2, slice_step:, slice_upper:2, slice_upper:5, suggest_constant_definition
        == int("".join(combination[5:9])) # call_argument:, comparison_operator:Eq, composition, empty_literal:Str, function_call:int, literal:5, literal:9, literal:Str, method_call:join, slice:5:9:, slice_lower:5, slice_step:, slice_upper:9, suggest_constant_definition
    ) or (
        int("".join(combination[0])) * int("".join(combination[1:5])) # binary_operator:Mult, call_argument:, composition, empty_literal:Str, function_call:int, index:0, literal:0, literal:1, literal:5, literal:Str, method_call:join, multiplication_operator, slice:1:5:, slice_lower:1, slice_step:, slice_upper:5, suggest_constant_definition
        == int("".join(combination[5:9])) # call_argument:, comparison_operator:Eq, composition, empty_literal:Str, function_call:int, literal:5, literal:9, literal:Str, method_call:join, slice:5:9:, slice_lower:5, slice_step:, slice_upper:9, suggest_constant_definition
    )
def solution(): # function:solution (-> +6), function_returning_something:solution (-> +6), function_without_arguments:solution (-> +6)
    return sum( # composition, function_call:sum, function_tail_call:sum, return
        set( # call_argument:, composition, function_call:set
            [
                int("".join(pandigital[5:9])) # call_argument:, composition, comprehension:List, comprehension_for_count:1, empty_literal:Str, function_call:int, literal:5, literal:9, literal:Str, method_call:join, slice:5:9:, slice_lower:5, slice_step:, slice_upper:9, suggest_constant_definition
                for pandigital in itertools.permutations("123456789") # call_argument:, literal:Str, method_call:permutations
                if isCombinationValid(pandigital) # call_argument:pandigital, filtered_comprehension, function_call:isCombinationValid
            ]
        )
    )

# ----------------------------------------------------------------------------------------
# problem_33/sol1.py
# ----------------------------------------------------------------------------------------
def isDigitCancelling(num, den): # function:isDigitCancelling (-> +4), function_argument:den, function_argument:num, function_argument_flavor:arg, function_returning_something:isDigitCancelling (-> +4)
    if num != den: # comparison_operator:NotEq, if (-> +3), if_test_atom:den, if_test_atom:num, if_without_else (-> +3)
        if num % 10 == den // 10: # binary_operator:FloorDiv, binary_operator:Mod, comparison_operator:Eq, divisibility_test:10, if (-> +2), if_test_atom:10, if_test_atom:den, if_test_atom:num, if_then_branch (-> +2), if_without_else (-> +2), literal:10, modulo_operator, nested_if:1 (-> +2), suggest_constant_definition
            if (num // 10) / (den % 10) == num / den: # binary_operator:Div, binary_operator:FloorDiv, binary_operator:Mod, comparison_operator:Eq, if (-> +1), if_test_atom:10, if_test_atom:den, if_test_atom:num, if_then_branch (-> +1), if_without_else (-> +1), literal:10, modulo_operator, nested_if:2 (-> +1), suggest_constant_definition
                return True # if_then_branch, literal:True, return:True
def solve(digit_len: int) -> str: # function:solve (-> +13), function_argument:digit_len, function_argument_flavor:arg, function_returning_something:solve (-> +13)
    solutions = [] # assignment, assignment_lhs_identifier:solutions, empty_literal:List, literal:List, single_assignment:solutions
    den = 11 # assignment:11, assignment_lhs_identifier:den, assignment_rhs_atom:11, literal:11, single_assignment:den, suggest_constant_definition
    last_digit = int("1" + "0" * digit_len) # assignment:int, assignment_lhs_identifier:last_digit, assignment_rhs_atom:digit_len, binary_operator:Add, binary_operator:Mult, call_argument:, concatenation_operator:Str, function_call:int, literal:Str, replication_operator:Str, single_assignment:last_digit
    for num in range(den, last_digit): # accumulate_elements:append (-> +7), accumulate_some_elements:append (-> +7), call_argument:den, call_argument:last_digit, count_elements:num (-> +7), for:num (-> +7), for_range:den:last_digit (-> +7), function_call:range, loop:for (-> +7), range:den:last_digit
        while den <= 99: # comparison_operator:LtE, count_states:den (-> +4), literal:99, loop:while (-> +4), suggest_constant_definition, while (-> +4)
            if (num != den) and (num % 10 == den // 10) and (den % 10 != 0): # binary_operator:FloorDiv, binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:NotEq, divisibility_test:10, if (-> +2), if_test_atom:0, if_test_atom:10, if_test_atom:den, if_test_atom:num, if_without_else (-> +2), literal:0, literal:10, modulo_operator, suggest_constant_definition
                if isDigitCancelling(num, den): # call_argument:den, call_argument:num, function_call:isDigitCancelling, if (-> +1), if_test_atom:den, if_test_atom:num, if_then_branch (-> +1), if_without_else (-> +1), nested_if:1 (-> +1)
                    solutions.append("{}/{}".format(num, den)) # call_argument:, call_argument:den, call_argument:num, composition, if_then_branch, literal:Str, method_call:append, method_call:format, method_call_object:solutions, method_call_without_result:append, update:solutions:den, update:solutions:num, update_by_method_call:solutions:den, update_by_method_call:solutions:num, update_by_method_call_with:append, update_with:append
            den += 1 # assignment_lhs_identifier:den, assignment_rhs_atom:1, augmented_assignment:Add, increment:den, literal:1, update:den:1, update_by_augmented_assignment:den:1, update_by_augmented_assignment_with:Add, update_with:Add
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment:num, literal:1, update:num:1, update_by_augmented_assignment:num:1, update_by_augmented_assignment_with:Add, update_with:Add
        den = 10 # assignment:10, assignment_lhs_identifier:den, assignment_rhs_atom:10, literal:10, single_assignment:den, suggest_constant_definition
    solutions = " , ".join(solutions) # assignment:join, assignment_lhs_identifier:solutions, assignment_rhs_atom:solutions, call_argument:solutions, literal:Str, method_call:join, single_assignment:solutions
    return solutions # return:solutions

# ----------------------------------------------------------------------------------------
# problem_36/sol1.py
# ----------------------------------------------------------------------------------------
def is_palindrome(n): # function:is_palindrome (-> +5), function_argument:n, function_argument_flavor:arg, function_returning_something:is_palindrome (-> +5)
    n = str(n) # assignment:str, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:str, single_assignment:n
    if n == n[::-1]: # comparison_operator:Eq, if (-> +3), if_test_atom:-1, if_test_atom:n, literal:-1, slice:::-1, slice_lower:, slice_step:-1, slice_upper:, suggest_condition_return (-> +3)
        return True # if_then_branch, literal:True, return:True
    else:
        return False # if_else_branch, literal:False, return:False
def solution(n): # function:solution (-> +5), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +5)
    total = 0 # assignment:0, assignment_lhs_identifier:total, assignment_rhs_atom:0, literal:0, single_assignment:total
    for i in range(1, n): # accumulate_elements:Add (-> +2), accumulate_some_elements:Add (-> +2), call_argument:1, call_argument:n, for:i (-> +2), for_range:1:n (-> +2), function_call:range, literal:1, loop:for (-> +2), range:1:n
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]): # boolean_operator:And, call_argument:, call_argument:i, composition, function_call:bin, function_call:is_palindrome, if (-> +1), if_test_atom:1, if_test_atom:i, if_without_else (-> +1), index:1, literal:1, literal:Str, method_call:split
            total += i # assignment_lhs_identifier:total, assignment_rhs_atom:i, augmented_assignment:Add, if_then_branch, update:total:i, update_by_augmented_assignment:total:i, update_by_augmented_assignment_with:Add, update_with:Add
    return total # return:total

# ----------------------------------------------------------------------------------------
# problem_40/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +14), function_returning_something:solution (-> +14), function_without_arguments:solution (-> +14)
    constant = [] # assignment, assignment_lhs_identifier:constant, empty_literal:List, literal:List, single_assignment:constant
    i = 1 # assignment:1, assignment_lhs_identifier:i, assignment_rhs_atom:1, literal:1, single_assignment:i
    while len(constant) < 1e6: # call_argument:constant, comparison_operator:Lt, count_states:i (-> +2), function_call:len, literal:1000000.0, loop:while (-> +2), suggest_constant_definition, while (-> +2)
        constant.append(str(i)) # call_argument:, call_argument:i, composition, function_call:str, method_call:append, method_call_object:constant, method_call_without_result:append, update:constant:i, update_by_method_call:constant:i, update_by_method_call_with:append, update_with:append
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
    constant = "".join(constant) # assignment:join, assignment_lhs_identifier:constant, assignment_rhs_atom:constant, call_argument:constant, empty_literal:Str, literal:Str, method_call:join, single_assignment:constant
    return ( # return
        int(constant[0]) # binary_operator:Mult, call_argument:, function_call:int, index:0, literal:0, multiplication_operator
        * int(constant[9]) # call_argument:, function_call:int, index:9, literal:9, suggest_constant_definition
        * int(constant[99]) # binary_operator:Mult, call_argument:, function_call:int, index:99, literal:99, multiplication_operator, suggest_constant_definition
        * int(constant[999]) # binary_operator:Mult, call_argument:, function_call:int, index:999, literal:999, multiplication_operator, suggest_constant_definition
        * int(constant[9999]) # binary_operator:Mult, call_argument:, function_call:int, index:9999, literal:9999, multiplication_operator, suggest_constant_definition
        * int(constant[99999]) # binary_operator:Mult, call_argument:, function_call:int, index:99999, literal:99999, multiplication_operator, suggest_constant_definition
        * int(constant[999999]) # binary_operator:Mult, call_argument:, function_call:int, index:999999, literal:999999, multiplication_operator, suggest_constant_definition
    )

# ----------------------------------------------------------------------------------------
# problem_42/solution42.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
TRIANGULAR_NUMBERS = [int(0.5 * n * (n + 1)) for n in range(1, 101)] # addition_operator, assignment, assignment_lhs_identifier:TRIANGULAR_NUMBERS, assignment_rhs_atom:0.5, assignment_rhs_atom:1, assignment_rhs_atom:101, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:1, call_argument:101, comprehension:List, comprehension_for_count:1, function_call:int, function_call:range, literal:0.5, literal:1, literal:101, multiplication_operator, range:1:101, single_assignment:TRIANGULAR_NUMBERS
def solution(): # function:solution (-> +13), function_returning_something:solution (-> +13), function_without_arguments:solution (-> +13)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment:dirname, assignment_lhs_identifier:script_dir, assignment_rhs_atom:__file__, assignment_rhs_atom:os, call_argument:, call_argument:__file__, composition, method_call:dirname, method_call:realpath, single_assignment:script_dir
    wordsFilePath = os.path.join(script_dir, "words.txt") # assignment:join, assignment_lhs_identifier:wordsFilePath, assignment_rhs_atom:os, assignment_rhs_atom:script_dir, call_argument:, call_argument:script_dir, literal:Str, method_call:join, single_assignment:wordsFilePath
    words = "" # assignment, assignment_lhs_identifier:words, empty_literal:Str, literal:Str, single_assignment:words
    with open(wordsFilePath, "r") as f: # call_argument:, call_argument:wordsFilePath, function_call:open, literal:Str
        words = f.readline() # assignment:readline, assignment_lhs_identifier:words, assignment_rhs_atom:f, method_call:readline, single_assignment:words
    words = list(map(lambda word: word.strip('"'), words.strip("\r\n").split(","))) # assignment:list, assignment_lhs_identifier:words, assignment_rhs_atom:word, assignment_rhs_atom:words, call_argument:, composition, function_argument:word, function_argument_flavor:arg, function_call:list, function_call:map, lambda_function, literal:Str, method_call:split, method_call:strip, method_call_object:words, method_chaining, single_assignment:words, update:words:word, update_by_assignment:words:word, update_by_assignment_with:list, update_with:list
    words = list( # assignment:list, assignment_lhs_identifier:words, composition, function_call:list, single_assignment:words, update:words:64, update:words:TRIANGULAR_NUMBERS, update:words:word, update:words:x, update_by_assignment:words:64, update_by_assignment:words:TRIANGULAR_NUMBERS, update_by_assignment:words:word, update_by_assignment:words:x, update_by_assignment_with:list, update_with:list
        filter( # call_argument:, composition, function_call:filter
            lambda word: word in TRIANGULAR_NUMBERS, # assignment_rhs_atom:TRIANGULAR_NUMBERS, assignment_rhs_atom:word, call_argument:, comparison_operator:In, function_argument:word, function_argument_flavor:arg, lambda_function
            map(lambda word: sum(map(lambda x: ord(x) - 64, word)), words), # assignment_rhs_atom:64, assignment_rhs_atom:word, assignment_rhs_atom:words, assignment_rhs_atom:x, binary_operator:Sub, call_argument:, call_argument:word, call_argument:words, call_argument:x, composition, function_argument:word, function_argument:x, function_argument_flavor:arg, function_call:map, function_call:ord, function_call:sum, lambda_function, literal:64, suggest_constant_definition
        )
    )
    return len(words) # call_argument:words, function_call:len, function_tail_call:len, return

# ----------------------------------------------------------------------------------------
# problem_48/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +4), function_returning_something:solution (-> +4), function_without_arguments:solution (-> +4)
    total = 0 # assignment:0, assignment_lhs_identifier:total, assignment_rhs_atom:0, literal:0, single_assignment:total
    for i in range(1, 1001): # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), call_argument:1, call_argument:1001, for:i (-> +1), for_range:1:1001 (-> +1), function_call:range, literal:1, literal:1001, loop:for (-> +1), range:1:1001, suggest_constant_definition
        total += i ** i # assignment_lhs_identifier:total, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Pow, update:total:i, update_by_augmented_assignment:total:i, update_by_augmented_assignment_with:Add, update_with:Add
    return str(total)[-10:] # call_argument:total, function_call:str, literal:-10, return, slice:-10::, slice_lower:-10, slice_step:, slice_upper:, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# problem_52/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +12), function_returning_something:solution (-> +12), function_without_arguments:solution (-> +12)
    i = 1 # assignment:1, assignment_lhs_identifier:i, assignment_rhs_atom:1, literal:1, single_assignment:i
    while True: # count_states:i (-> +10), infinite_while (-> +10), literal:True, loop:while (-> +10), loop_with_early_exit:while:return (-> +10), while (-> +10)
        if ( # if (-> +8)
            sorted(list(str(i))) # call_argument:, call_argument:i, chained_comparison:5, chained_equalities:5, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:i
            == sorted(list(str(2 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:2, if_test_atom:i, literal:2, multiplication_operator
            == sorted(list(str(3 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:3, if_test_atom:i, literal:3, multiplication_operator, suggest_constant_definition
            == sorted(list(str(4 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:4, if_test_atom:i, literal:4, multiplication_operator, suggest_constant_definition
            == sorted(list(str(5 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:5, if_test_atom:i, literal:5, multiplication_operator, suggest_constant_definition
            == sorted(list(str(6 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:6, if_test_atom:i, literal:6, multiplication_operator, suggest_constant_definition
        ):
            return i # if_then_branch, return:i
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add

# ----------------------------------------------------------------------------------------
# problem_53/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial # import:math:factorial, import_module:math, import_name:factorial
def combinations(n, r): # function:combinations (-> +1), function_argument:n, function_argument:r, function_argument_flavor:arg, function_returning_something:combinations (-> +1)
    return factorial(n) / (factorial(r) * factorial(n - r)) # binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:n, call_argument:r, function_call:factorial, multiplication_operator, return
def solution(): # function:solution (-> +6), function_returning_something:solution (-> +6), function_without_arguments:solution (-> +6)
    total = 0 # assignment:0, assignment_lhs_identifier:total, assignment_rhs_atom:0, literal:0, single_assignment:total
    for i in range(1, 101): # call_argument:1, call_argument:101, count_elements:total (-> +3), for:i (-> +3), for_range:1:101 (-> +3), for_range:1:_ (-> +3), function_call:range, literal:1, literal:101, loop:for (-> +3), range:1:101, suggest_constant_definition
        for j in range(1, i + 1): # addition_operator, binary_operator:Add, call_argument:, call_argument:1, for:j (-> +2), for_range:1:_ (-> +2), function_call:range, literal:1, loop:for (-> +2), nested_for:1 (-> +2), range:1:_
            if combinations(i, j) > 1e6: # call_argument:i, call_argument:j, comparison_operator:Gt, function_call:combinations, if (-> +1), if_test_atom:1000000.0, if_test_atom:i, if_test_atom:j, if_without_else (-> +1), literal:1000000.0, suggest_constant_definition
                total += 1 # assignment_lhs_identifier:total, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment:total, literal:1, update:total:1, update_by_augmented_assignment:total:1, update_by_augmented_assignment_with:Add, update_with:Add
    return total # return:total

# ----------------------------------------------------------------------------------------
# problem_551/sol1.py
# ----------------------------------------------------------------------------------------
ks = [k for k in range(2, 20 + 1)] # addition_operator, assignment, assignment_lhs_identifier:ks, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:20, assignment_rhs_atom:k, binary_operator:Add, call_argument:, call_argument:2, comprehension:List, comprehension_for_count:1, function_call:range, literal:1, literal:2, literal:20, range:2:_, single_assignment:ks
base = [10 ** k for k in range(ks[-1] + 1)] # addition_operator, assignment, assignment_lhs_identifier:base, assignment_rhs_atom:-1, assignment_rhs_atom:1, assignment_rhs_atom:10, assignment_rhs_atom:k, assignment_rhs_atom:ks, binary_operator:Add, binary_operator:Pow, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, index:-1, literal:-1, literal:1, literal:10, negative_index:-1, range:_, single_assignment:base
memo = {} # assignment, assignment_lhs_identifier:memo, empty_literal:Dict, literal:Dict, single_assignment:memo
def next_term(a_i, k, i, n): # body_recursive_function:next_term (-> +50), function:next_term (-> +50), function_argument:a_i, function_argument:i, function_argument:k, function_argument:n, function_argument_flavor:arg, function_returning_something:next_term (-> +50), recursive_function:next_term (-> +50)
    ds_b = 0 # assignment:0, assignment_lhs_identifier:ds_b, assignment_rhs_atom:0, literal:0, single_assignment:ds_b
    for j in range(k, len(a_i)): # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), call_argument:, call_argument:a_i, call_argument:k, composition, for:j (-> +1), for_range:k:_ (-> +1), function_call:len, function_call:range, loop:for (-> +1), range:k:_
        ds_b += a_i[j] # assignment_lhs_identifier:ds_b, assignment_rhs_atom:a_i, assignment_rhs_atom:j, augmented_assignment:Add, index:j, update:ds_b:a_i, update:ds_b:j, update_by_augmented_assignment:ds_b:a_i, update_by_augmented_assignment:ds_b:j, update_by_augmented_assignment_with:Add, update_with:Add
    c = 0 # assignment:0, assignment_lhs_identifier:c, assignment_rhs_atom:0, literal:0, single_assignment:c
    for j in range(min(len(a_i), k)): # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), call_argument:, call_argument:a_i, call_argument:k, composition, for:j (-> +1), for_range:_ (-> +1), function_call:len, function_call:min, function_call:range, loop:for (-> +1), range:_
        c += a_i[j] * base[j] # assignment_lhs_identifier:c, assignment_rhs_atom:a_i, assignment_rhs_atom:base, assignment_rhs_atom:j, augmented_assignment:Add, binary_operator:Mult, index:j, multiplication_operator, update:c:a_i, update:c:base, update:c:j, update_by_augmented_assignment:c:a_i, update_by_augmented_assignment:c:base, update_by_augmented_assignment:c:j, update_by_augmented_assignment_with:Add, update_with:Add
    diff, dn = 0, 0 # assignment, assignment_lhs_identifier:diff, assignment_lhs_identifier:dn, assignment_rhs_atom:0, literal:0, literal:Tuple, parallel_assignment:2
    max_dn = n - i # assignment:Sub, assignment_lhs_identifier:max_dn, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Sub, single_assignment:max_dn
    sub_memo = memo.get(ds_b) # assignment:get, assignment_lhs_identifier:sub_memo, assignment_rhs_atom:ds_b, assignment_rhs_atom:memo, call_argument:ds_b, method_call:get, single_assignment:sub_memo
    if sub_memo != None: # comparison_operator:NotEq, if (-> +19), if_test_atom:None, if_test_atom:sub_memo, literal:None
        jumps = sub_memo.get(c) # assignment:get, assignment_lhs_identifier:jumps, assignment_rhs_atom:c, assignment_rhs_atom:sub_memo, call_argument:c, if_then_branch (-> +15), method_call:get, single_assignment:jumps
        if jumps != None and len(jumps) > 0: # boolean_operator:And, call_argument:jumps, comparison_operator:Gt, comparison_operator:NotEq, function_call:len, if (-> +14), if_test_atom:0, if_test_atom:None, if_test_atom:jumps, literal:0, literal:None, nested_if:1 (-> +14)
            max_jump = -1 # assignment:-1, assignment_lhs_identifier:max_jump, assignment_rhs_atom:-1, if_then_branch (-> +11), literal:-1, single_assignment:max_jump
            for _k in range(len(jumps) - 1, -1, -1): # binary_operator:Sub, call_argument:, call_argument:-1, call_argument:jumps, composition, for:_k (-> +3), for_range:_:-1:-1 (-> +3), function_call:len, function_call:range, literal:-1, literal:1, loop:for (-> +3), loop_with_early_exit:for:break (-> +3), range:_:-1:-1
                if jumps[_k][2] <= k and jumps[_k][1] <= max_dn: # boolean_operator:And, comparison_operator:LtE, if (-> +2), if_test_atom:1, if_test_atom:2, if_test_atom:_k, if_test_atom:jumps, if_test_atom:k, if_test_atom:max_dn, if_without_else (-> +2), index:1, index:2, index:_k, literal:1, literal:2, nested_if:2 (-> +2), nested_index:2
                    max_jump = _k # assignment, assignment_lhs_identifier:max_jump, assignment_rhs_atom:_k, if_then_branch (-> +1), single_assignment:max_jump
                    break # break
            if max_jump >= 0: # comparison_operator:GtE, if (-> +6), if_test_atom:0, if_test_atom:max_jump, if_without_else (-> +6), literal:0, nested_if:2 (-> +6)
                diff, dn, _kk = jumps[max_jump] # assignment, assignment_lhs_identifier:_kk, assignment_lhs_identifier:diff, assignment_lhs_identifier:dn, assignment_rhs_atom:jumps, assignment_rhs_atom:max_jump, if_then_branch (-> +5), index:max_jump, parallel_assignment:3
                new_c = diff + c # addition_operator, assignment:Add, assignment_lhs_identifier:new_c, assignment_rhs_atom:c, assignment_rhs_atom:diff, binary_operator:Add, single_assignment:new_c
                for j in range(min(k, len(a_i))): # call_argument:, call_argument:a_i, call_argument:k, composition, for:j (-> +1), for_range:_ (-> +1), function_call:len, function_call:min, function_call:range, loop:for (-> +1), range:_
                    new_c, a_i[j] = divmod(new_c, 10) # assignment:divmod, assignment_lhs_identifier:a_i, assignment_lhs_identifier:new_c, assignment_rhs_atom:10, assignment_rhs_atom:new_c, call_argument:10, call_argument:new_c, function_call:divmod, index:j, literal:10, parallel_assignment:2, suggest_constant_definition, update:new_c:10, update_by_assignment:new_c:10, update_by_assignment_with:divmod, update_with:divmod
                if new_c > 0: # comparison_operator:Gt, if (-> +1), if_test_atom:0, if_test_atom:new_c, if_without_else (-> +1), literal:0, nested_if:3 (-> +1)
                    add(a_i, k, new_c) # call_argument:a_i, call_argument:k, call_argument:new_c, function_call:add, function_call_without_result:add, if_then_branch
        else:
            sub_memo[c] = [] # assignment, assignment_lhs_identifier:sub_memo, empty_literal:List, if_else_branch, index:c, literal:List
    else:
        sub_memo = {c: []} # assignment, assignment_lhs_identifier:sub_memo, assignment_rhs_atom:c, empty_literal:List, if_else_branch (-> +1), literal:List, single_assignment:sub_memo
        memo[ds_b] = sub_memo # assignment, assignment_lhs_identifier:memo, assignment_rhs_atom:sub_memo, index:ds_b
    if dn >= max_dn or c + diff >= base[k]: # addition_operator, binary_operator:Add, boolean_operator:Or, comparison_operator:GtE, if (-> +1), if_guard (-> +1), if_test_atom:base, if_test_atom:c, if_test_atom:diff, if_test_atom:dn, if_test_atom:k, if_test_atom:max_dn, if_without_else (-> +1), index:k
        return diff, dn # if_then_branch, return
    if k > ks[0]: # comparison_operator:Gt, if (-> +10), if_test_atom:0, if_test_atom:k, if_test_atom:ks, index:0, literal:0
        while True: # if_then_branch (-> +5), infinite_while (-> +5), literal:True, loop:while (-> +5), loop_with_early_exit:while:break (-> +5), while (-> +5)
            _diff, terms_jumped = next_term(a_i, k - 1, i + dn, n) # addition_operator, assignment:next_term, assignment_lhs_identifier:_diff, assignment_lhs_identifier:terms_jumped, assignment_rhs_atom:1, assignment_rhs_atom:a_i, assignment_rhs_atom:dn, assignment_rhs_atom:i, assignment_rhs_atom:k, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:a_i, call_argument:n, function_call:next_term, literal:1, parallel_assignment:2
            diff += _diff # assignment_lhs_identifier:diff, assignment_rhs_atom:_diff, augmented_assignment:Add, update:diff:_diff, update_by_augmented_assignment:diff:_diff, update_by_augmented_assignment_with:Add, update_with:Add
            dn += terms_jumped # assignment_lhs_identifier:dn, assignment_rhs_atom:terms_jumped, augmented_assignment:Add, update:dn:terms_jumped, update_by_augmented_assignment:dn:terms_jumped, update_by_augmented_assignment_with:Add, update_with:Add
            if dn >= max_dn or c + diff >= base[k]: # addition_operator, binary_operator:Add, boolean_operator:Or, comparison_operator:GtE, if (-> +1), if_test_atom:base, if_test_atom:c, if_test_atom:diff, if_test_atom:dn, if_test_atom:k, if_test_atom:max_dn, if_without_else (-> +1), index:k, nested_if:1 (-> +1)
                break # break, if_then_branch
    else:
        _diff, terms_jumped = compute(a_i, k, i + dn, n) # addition_operator, assignment:compute, assignment_lhs_identifier:_diff, assignment_lhs_identifier:terms_jumped, assignment_rhs_atom:a_i, assignment_rhs_atom:dn, assignment_rhs_atom:i, assignment_rhs_atom:k, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:a_i, call_argument:k, call_argument:n, function_call:compute, if_else_branch (-> +2), parallel_assignment:2
        diff += _diff # assignment_lhs_identifier:diff, assignment_rhs_atom:_diff, augmented_assignment:Add, update:diff:_diff, update_by_augmented_assignment:diff:_diff, update_by_augmented_assignment_with:Add, update_with:Add
        dn += terms_jumped # assignment_lhs_identifier:dn, assignment_rhs_atom:terms_jumped, augmented_assignment:Add, update:dn:terms_jumped, update_by_augmented_assignment:dn:terms_jumped, update_by_augmented_assignment_with:Add, update_with:Add
    jumps = sub_memo[c] # assignment, assignment_lhs_identifier:jumps, assignment_rhs_atom:c, assignment_rhs_atom:sub_memo, index:c, single_assignment:jumps
    j = 0 # assignment:0, assignment_lhs_identifier:j, assignment_rhs_atom:0, literal:0, single_assignment:j
    while j < len(jumps): # call_argument:jumps, comparison_operator:Lt, count_states:j (-> +3), function_call:len, loop:while (-> +3), loop_with_early_exit:while:break (-> +3), while (-> +3)
        if jumps[j][1] > dn: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:dn, if_test_atom:j, if_test_atom:jumps, if_without_else (-> +1), index:1, index:j, literal:1, nested_index:2
            break # break, if_then_branch
        j += 1 # assignment_lhs_identifier:j, assignment_rhs_atom:1, augmented_assignment:Add, increment:j, literal:1, update:j:1, update_by_augmented_assignment:j:1, update_by_augmented_assignment_with:Add, update_with:Add
    sub_memo[c].insert(j, (diff, dn, k)) # call_argument:, call_argument:j, index:c, method_call:insert, method_call_without_result:insert
    return (diff, dn) # return
def compute(a_i, k, i, n): # function:compute (-> +25), function_argument:a_i, function_argument:i, function_argument:k, function_argument:n, function_argument_flavor:arg, function_returning_something:compute (-> +25)
    if i >= n: # comparison_operator:GtE, if (-> +1), if_guard (-> +1), if_test_atom:i, if_test_atom:n, if_without_else (-> +1)
        return 0, i # if_then_branch, literal:0, return
    if k > len(a_i): # call_argument:a_i, comparison_operator:Gt, function_call:len, if (-> +1), if_test_atom:a_i, if_test_atom:k, if_without_else (-> +1)
        a_i.extend([0 for _ in range(k - len(a_i))]) # binary_operator:Sub, call_argument:, call_argument:a_i, composition, comprehension:List, comprehension_for_count:1, function_call:len, function_call:range, if_then_branch, literal:0, method_call:extend, method_call_object:a_i, method_call_without_result:extend, range:_, update:a_i:a_i, update_by_method_call:a_i:a_i, update_by_method_call_with:extend, update_with:extend
    start_i = i # assignment, assignment_lhs_identifier:start_i, assignment_rhs_atom:i, single_assignment:start_i
    ds_b, ds_c, diff = 0, 0, 0 # assignment, assignment_lhs_identifier:diff, assignment_lhs_identifier:ds_b, assignment_lhs_identifier:ds_c, assignment_rhs_atom:0, literal:0, literal:Tuple, parallel_assignment:3
    for j in range(len(a_i)): # accumulate_elements:Add (-> +4), accumulate_some_elements:Add (-> +4), call_argument:, call_argument:a_i, composition, for:j (-> +4), for_indexes (-> +4), for_range:_ (-> +4), function_call:len, function_call:range, loop:for (-> +4), range:_
        if j >= k: # comparison_operator:GtE, if (-> +3), if_test_atom:j, if_test_atom:k
            ds_b += a_i[j] # assignment_lhs_identifier:ds_b, assignment_rhs_atom:a_i, assignment_rhs_atom:j, augmented_assignment:Add, if_then_branch, index:j, update:ds_b:a_i, update:ds_b:j, update_by_augmented_assignment:ds_b:a_i, update_by_augmented_assignment:ds_b:j, update_by_augmented_assignment_with:Add, update_with:Add
        else:
            ds_c += a_i[j] # assignment_lhs_identifier:ds_c, assignment_rhs_atom:a_i, assignment_rhs_atom:j, augmented_assignment:Add, if_else_branch, index:j, update:ds_c:a_i, update:ds_c:j, update_by_augmented_assignment:ds_c:a_i, update_by_augmented_assignment:ds_c:j, update_by_augmented_assignment_with:Add, update_with:Add
    while i < n: # comparison_operator:Lt, count_states:i (-> +10), loop:while (-> +10), loop_with_early_exit:while:break (-> +10), while (-> +10)
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
        addend = ds_c + ds_b # addition_operator, assignment:Add, assignment_lhs_identifier:addend, assignment_rhs_atom:ds_b, assignment_rhs_atom:ds_c, binary_operator:Add, single_assignment:addend
        diff += addend # assignment_lhs_identifier:diff, assignment_rhs_atom:addend, augmented_assignment:Add, update:diff:addend, update_by_augmented_assignment:diff:addend, update_by_augmented_assignment_with:Add, update_with:Add
        ds_c = 0 # assignment:0, assignment_lhs_identifier:ds_c, assignment_rhs_atom:0, literal:0, single_assignment:ds_c
        for j in range(k): # accumulate_all_elements:Add (-> +3), accumulate_elements:Add (-> +3), call_argument:k, for:j (-> +3), for_range:k (-> +3), function_call:range, loop:for (-> +3), range:k
            s = a_i[j] + addend # addition_operator, assignment:Add, assignment_lhs_identifier:s, assignment_rhs_atom:a_i, assignment_rhs_atom:addend, assignment_rhs_atom:j, binary_operator:Add, index:j, single_assignment:s
            addend, a_i[j] = divmod(s, 10) # assignment:divmod, assignment_lhs_identifier:a_i, assignment_lhs_identifier:addend, assignment_rhs_atom:10, assignment_rhs_atom:s, call_argument:10, call_argument:s, function_call:divmod, index:j, literal:10, parallel_assignment:2, suggest_constant_definition
            ds_c += a_i[j] # assignment_lhs_identifier:ds_c, assignment_rhs_atom:a_i, assignment_rhs_atom:j, augmented_assignment:Add, index:j, update:ds_c:a_i, update:ds_c:j, update_by_augmented_assignment:ds_c:a_i, update_by_augmented_assignment:ds_c:j, update_by_augmented_assignment_with:Add, update_with:Add
        if addend > 0: # comparison_operator:Gt, if (-> +1), if_test_atom:0, if_test_atom:addend, if_without_else (-> +1), literal:0
            break # break, if_then_branch
    if addend > 0: # comparison_operator:Gt, if (-> +1), if_test_atom:0, if_test_atom:addend, if_without_else (-> +1), literal:0
        add(a_i, k, addend) # call_argument:a_i, call_argument:addend, call_argument:k, function_call:add, function_call_without_result:add, if_then_branch
    return diff, i - start_i # binary_operator:Sub, return
def add(digits, k, addend): # function:add (-> +13), function_argument:addend, function_argument:digits, function_argument:k, function_argument_flavor:arg, function_returning_nothing:add (-> +13)
    for j in range(k, len(digits)): # call_argument:, call_argument:digits, call_argument:k, composition, for:j (-> +9), for_range:k:_ (-> +9), function_call:len, function_call:range, loop:for (-> +9), loop_with_early_exit:for:break (-> +9), range:k:_
        s = digits[j] + addend # addition_operator, assignment:Add, assignment_lhs_identifier:s, assignment_rhs_atom:addend, assignment_rhs_atom:digits, assignment_rhs_atom:j, binary_operator:Add, index:j, single_assignment:s
        if s >= 10: # comparison_operator:GtE, if (-> +5), if_test_atom:10, if_test_atom:s, literal:10, suggest_constant_definition
            quotient, digits[j] = divmod(s, 10) # assignment:divmod, assignment_lhs_identifier:digits, assignment_lhs_identifier:quotient, assignment_rhs_atom:10, assignment_rhs_atom:s, call_argument:10, call_argument:s, function_call:divmod, if_then_branch (-> +1), index:j, literal:10, parallel_assignment:2, suggest_constant_definition
            addend = addend // 10 + quotient # addition_operator, assignment:Add, assignment_lhs_identifier:addend, assignment_rhs_atom:10, assignment_rhs_atom:addend, assignment_rhs_atom:quotient, binary_operator:Add, binary_operator:FloorDiv, literal:10, single_assignment:addend, suggest_constant_definition, update:addend:10, update:addend:quotient, update_by_assignment:addend:10, update_by_assignment:addend:quotient, update_by_assignment_with:Add, update_with:Add
        else:
            digits[j] = s # assignment, assignment_lhs_identifier:digits, assignment_rhs_atom:s, if_else_branch (-> +1), index:j
            addend = addend // 10 # assignment:FloorDiv, assignment_lhs_identifier:addend, assignment_rhs_atom:10, assignment_rhs_atom:addend, binary_operator:FloorDiv, literal:10, single_assignment:addend, suggest_augmented_assignment, suggest_constant_definition, update:addend:10, update_by_assignment:addend:10, update_by_assignment_with:FloorDiv, update_with:FloorDiv
        if addend == 0: # comparison_operator:Eq, if (-> +1), if_test_atom:0, if_test_atom:addend, if_without_else (-> +1), literal:0
            break # break, if_then_branch
    while addend > 0: # comparison_operator:Gt, literal:0, loop:while (-> +2), while (-> +2)
        addend, digit = divmod(addend, 10) # assignment:divmod, assignment_lhs_identifier:addend, assignment_lhs_identifier:digit, assignment_rhs_atom:10, assignment_rhs_atom:addend, call_argument:10, call_argument:addend, function_call:divmod, literal:10, parallel_assignment:2, suggest_constant_definition, update:addend:10, update_by_assignment:addend:10, update_by_assignment_with:divmod, update_with:divmod
        digits.append(digit) # call_argument:digit, method_call:append, method_call_object:digits, method_call_without_result:append, update:digits:digit, update_by_method_call:digits:digit, update_by_method_call_with:append, update_with:append
def solution(n): # function:solution (-> +12), function_argument:n, function_argument_flavor:arg, function_returning_something:solution (-> +12)
    digits = [1] # assignment, assignment_lhs_identifier:digits, assignment_rhs_atom:1, literal:1, literal:List, single_assignment:digits
    i = 1 # assignment:1, assignment_lhs_identifier:i, assignment_rhs_atom:1, literal:1, single_assignment:i
    dn = 0 # assignment:0, assignment_lhs_identifier:dn, assignment_rhs_atom:0, literal:0, single_assignment:dn
    while True: # infinite_while (-> +4), literal:True, loop:while (-> +4), loop_with_early_exit:while:break (-> +4), while (-> +4)
        diff, terms_jumped = next_term(digits, 20, i + dn, n) # addition_operator, assignment:next_term, assignment_lhs_identifier:diff, assignment_lhs_identifier:terms_jumped, assignment_rhs_atom:20, assignment_rhs_atom:digits, assignment_rhs_atom:dn, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:20, call_argument:digits, call_argument:n, function_call:next_term, literal:20, parallel_assignment:2, suggest_constant_definition
        dn += terms_jumped # assignment_lhs_identifier:dn, assignment_rhs_atom:terms_jumped, augmented_assignment:Add, update:dn:terms_jumped, update_by_augmented_assignment:dn:terms_jumped, update_by_augmented_assignment_with:Add, update_with:Add
        if dn == n - i: # binary_operator:Sub, comparison_operator:Eq, if (-> +1), if_test_atom:dn, if_test_atom:i, if_test_atom:n, if_without_else (-> +1)
            break # break, if_then_branch
    a_n = 0 # assignment:0, assignment_lhs_identifier:a_n, assignment_rhs_atom:0, literal:0, single_assignment:a_n
    for j in range(len(digits)): # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), call_argument:, call_argument:digits, composition, for:j (-> +1), for_indexes (-> +1), for_range:_ (-> +1), function_call:len, function_call:range, loop:for (-> +1), range:_
        a_n += digits[j] * 10 ** j # assignment_lhs_identifier:a_n, assignment_rhs_atom:10, assignment_rhs_atom:digits, assignment_rhs_atom:j, augmented_assignment:Add, binary_operator:Mult, binary_operator:Pow, index:j, literal:10, multiplication_operator, suggest_constant_definition, update:a_n:10, update:a_n:digits, update:a_n:j, update_by_augmented_assignment:a_n:10, update_by_augmented_assignment:a_n:digits, update_by_augmented_assignment:a_n:j, update_by_augmented_assignment_with:Add, update_with:Add
    return a_n # return:a_n

# ----------------------------------------------------------------------------------------
# problem_56/sol1.py
# ----------------------------------------------------------------------------------------
def maximum_digital_sum(a: int, b: int) -> int: # function:maximum_digital_sum (-> +5), function_argument:a, function_argument:b, function_argument_flavor:arg, function_returning_something:maximum_digital_sum (-> +5)
    return max( # composition, function_call:max, function_tail_call:max, return
        [
            sum([int(x) for x in str(base ** power)]) # binary_operator:Pow, call_argument:, call_argument:x, composition, comprehension:List, comprehension_for_count:1, comprehension_for_count:2, function_call:int, function_call:str, function_call:sum
            for base in range(a) # call_argument:a, function_call:range, range:a
            for power in range(b) # call_argument:b, function_call:range, range:b
        ]
    )

# ----------------------------------------------------------------------------------------
# problem_67/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +18), function_returning_something:solution (-> +18), function_without_arguments:solution (-> +18)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment:dirname, assignment_lhs_identifier:script_dir, assignment_rhs_atom:__file__, assignment_rhs_atom:os, call_argument:, call_argument:__file__, composition, method_call:dirname, method_call:realpath, single_assignment:script_dir
    triangle = os.path.join(script_dir, "triangle.txt") # assignment:join, assignment_lhs_identifier:triangle, assignment_rhs_atom:os, assignment_rhs_atom:script_dir, call_argument:, call_argument:script_dir, literal:Str, method_call:join, single_assignment:triangle
    with open(triangle, "r") as f: # call_argument:, call_argument:triangle, function_call:open, literal:Str
        triangle = f.readlines() # assignment:readlines, assignment_lhs_identifier:triangle, assignment_rhs_atom:f, method_call:readlines, single_assignment:triangle
    a = map(lambda x: x.rstrip("\r\n").split(" "), triangle) # assignment:map, assignment_lhs_identifier:a, assignment_rhs_atom:triangle, assignment_rhs_atom:x, call_argument:, call_argument:triangle, composition, function_argument:x, function_argument_flavor:arg, function_call:map, lambda_function, literal:Str, method_call:rstrip, method_call:split, method_call_object:x, method_chaining, single_assignment:a
    a = list(map(lambda x: list(map(lambda y: int(y), x)), a)) # assignment:list, assignment_lhs_identifier:a, assignment_rhs_atom:a, assignment_rhs_atom:x, assignment_rhs_atom:y, call_argument:, call_argument:a, call_argument:x, call_argument:y, composition, function_argument:x, function_argument:y, function_argument_flavor:arg, function_call:int, function_call:list, function_call:map, lambda_function, single_assignment:a, update:a:x, update:a:y, update_by_assignment:a:x, update_by_assignment:a:y, update_by_assignment_with:list, update_with:list
    for i in range(1, len(a)): # call_argument:, call_argument:1, call_argument:a, composition, for:i (-> +10), for_range:1:_ (-> +10), for_range:_ (-> +10), function_call:len, function_call:range, literal:1, loop:for (-> +10), range:1:_
        for j in range(len(a[i])): # call_argument:, composition, for:j (-> +9), for_indexes (-> +9), for_range:_ (-> +9), function_call:len, function_call:range, index:i, loop:for (-> +9), nested_for:1 (-> +9), range:_
            if j != len(a[i - 1]): # binary_operator:Sub, call_argument:, comparison_operator:NotEq, function_call:len, if (-> +3), if_test_atom:1, if_test_atom:a, if_test_atom:i, if_test_atom:j, index:_, index_arithmetic, literal:1, verbose_conditional_assignment (-> +3)
                number1 = a[i - 1][j] # assignment, assignment_lhs_identifier:number1, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Sub, if_then_branch, index:_, index:j, index_arithmetic, literal:1, nested_index:2, single_assignment:number1
            else:
                number1 = 0 # assignment:0, assignment_lhs_identifier:number1, assignment_rhs_atom:0, if_else_branch, literal:0, single_assignment:number1
            if j > 0: # comparison_operator:Gt, if (-> +3), if_test_atom:0, if_test_atom:j, literal:0, verbose_conditional_assignment (-> +3)
                number2 = a[i - 1][j - 1] # assignment, assignment_lhs_identifier:number2, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Sub, if_then_branch, index:_, index_arithmetic, literal:1, nested_index:2, single_assignment:number2
            else:
                number2 = 0 # assignment:0, assignment_lhs_identifier:number2, assignment_rhs_atom:0, if_else_branch, literal:0, single_assignment:number2
            a[i][j] += max(number1, number2) # assignment_rhs_atom:number1, assignment_rhs_atom:number2, augmented_assignment:Add, call_argument:number1, call_argument:number2, function_call:max, index:i, index:j, nested_index:2, subscript_augmented_assignment:Add
    return max(a[-1]) # call_argument:, function_call:max, function_tail_call:max, index:-1, literal:-1, negative_index:-1, return

# ----------------------------------------------------------------------------------------
# problem_76/sol1.py
# ----------------------------------------------------------------------------------------
def partition(m): # function:partition (-> +9), function_argument:m, function_argument_flavor:arg, function_returning_something:partition (-> +9)
    memo = [[0 for _ in range(m)] for _ in range(m + 1)] # addition_operator, assignment, assignment_lhs_identifier:memo, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:_, assignment_rhs_atom:m, binary_operator:Add, call_argument:, call_argument:m, comprehension:List, comprehension_for_count:1, function_call:range, literal:0, literal:1, range:_, range:m, single_assignment:memo
    for i in range(m + 1): # addition_operator, binary_operator:Add, call_argument:, for:i (-> +1), for_range:_ (-> +1), function_call:range, literal:1, loop:for (-> +1), range:_
        memo[i][0] = 1 # assignment:1, assignment_rhs_atom:1, index:0, index:i, literal:0, literal:1, nested_index:2
    for n in range(m + 1): # addition_operator, binary_operator:Add, call_argument:, for:n (-> +4), for_range:1:m (-> +4), for_range:_ (-> +4), function_call:range, literal:1, loop:for (-> +4), range:_
        for k in range(1, m): # call_argument:1, call_argument:m, for:k (-> +3), for_range:1:m (-> +3), function_call:range, literal:1, loop:for (-> +3), nested_for:1 (-> +3), range:1:m
            memo[n][k] += memo[n][k - 1] # assignment_rhs_atom:1, assignment_rhs_atom:k, assignment_rhs_atom:memo, assignment_rhs_atom:n, augmented_assignment:Add, binary_operator:Sub, index:_, index:k, index:n, index_arithmetic, literal:1, nested_index:2, subscript_augmented_assignment:Add
            if n > k: # comparison_operator:Gt, if (-> +1), if_test_atom:k, if_test_atom:n, if_without_else (-> +1)
                memo[n][k] += memo[n - k - 1][k] # assignment_rhs_atom:1, assignment_rhs_atom:k, assignment_rhs_atom:memo, assignment_rhs_atom:n, augmented_assignment:Add, binary_operator:Sub, if_then_branch, index:_, index:k, index:n, index_arithmetic, literal:1, nested_index:2, subscript_augmented_assignment:Add
    return memo[m][m - 1] - 1 # binary_operator:Sub, index:_, index:m, index_arithmetic, literal:1, nested_index:2, return

# ----------------------------------------------------------------------------------------
# problem_99/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
from math import log10 # import:math:log10, import_module:math, import_name:log10
def find_largest(data_file: str = "base_exp.txt") -> int: # function:find_largest (-> +6), function_argument:data_file, function_argument_flavor:arg, function_returning_something:find_largest (-> +6), literal:Str
    largest = [0, 0] # assignment, assignment_lhs_identifier:largest, assignment_rhs_atom:0, literal:0, literal:List, single_assignment:largest
    for i, line in enumerate(open(os.path.join(os.path.dirname(__file__), data_file))): # call_argument:, call_argument:__file__, call_argument:data_file, composition, for:i, for_indexes_elements (-> +3), function_call:enumerate, function_call:open, loop:for, method_call:dirname, method_call:join
        a, x = list(map(int, line.split(","))) # assignment:list, assignment_lhs_identifier:a, assignment_lhs_identifier:x, assignment_rhs_atom:int, assignment_rhs_atom:line, call_argument:, call_argument:int, composition, function_call:list, function_call:map, literal:Str, method_call:split, parallel_assignment:2
        if x * log10(a) > largest[0]: # binary_operator:Mult, call_argument:a, comparison_operator:Gt, function_call:log10, if (-> +1), if_test_atom:0, if_test_atom:a, if_test_atom:largest, if_test_atom:x, if_without_else (-> +1), index:0, literal:0, multiplication_operator
            largest = [x * log10(a), i + 1] # addition_operator, assignment, assignment_lhs_identifier:largest, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, call_argument:a, for:line, function_call:log10, if_then_branch, literal:1, loop:for, multiplication_operator, nested_for:1, single_assignment:largest
    return largest[1] # index:1, literal:1, return
