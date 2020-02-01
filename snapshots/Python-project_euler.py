# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return sum([e for e in range(3, n) if e % 3 == 0 or e % 5 == 0]) # binary_operator:Mod, boolean_operator:Or, call_argument:, call_argument:3, call_argument:n, comparison_operator:Eq, composition, comprehension:List, comprehension_for_count:1, divisibility_test:3, divisibility_test:5, filtered_comprehension, function_call:range, function_call:sum, function_tail_call:sum, int_literal, literal:Num, range:3:n, return, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_returning_something:solution (-> +8)
    sum = 0 # assignment, assignment_lhs_identifier:sum, assignment_rhs_atom:0, int_literal, literal:Num
    terms = (n - 1) // 3 # assignment, assignment_lhs_identifier:terms, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:n, binary_operator:FloorDiv, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    sum += ((terms) * (6 + (terms - 1) * 3)) // 2 # assignment_lhs_identifier:sum, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:6, assignment_rhs_atom:terms, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, increment_variable:sum:1, increment_variable:sum:2, increment_variable:sum:3, increment_variable:sum:6, increment_variable:sum:terms, int_literal, literal:Num, suggest_constant_definition, update_variable:sum:1, update_variable:sum:2, update_variable:sum:3, update_variable:sum:6, update_variable:sum:terms
    terms = (n - 1) // 5 # assignment, assignment_lhs_identifier:terms, assignment_rhs_atom:1, assignment_rhs_atom:5, assignment_rhs_atom:n, binary_operator:FloorDiv, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    sum += ((terms) * (10 + (terms - 1) * 5)) // 2 # assignment_lhs_identifier:sum, assignment_rhs_atom:1, assignment_rhs_atom:10, assignment_rhs_atom:2, assignment_rhs_atom:5, assignment_rhs_atom:terms, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, increment_variable:sum:1, increment_variable:sum:10, increment_variable:sum:2, increment_variable:sum:5, increment_variable:sum:terms, int_literal, literal:Num, suggest_constant_definition, update_variable:sum:1, update_variable:sum:10, update_variable:sum:2, update_variable:sum:5, update_variable:sum:terms
    terms = (n - 1) // 15 # assignment, assignment_lhs_identifier:terms, assignment_rhs_atom:1, assignment_rhs_atom:15, assignment_rhs_atom:n, binary_operator:FloorDiv, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    sum -= ((terms) * (30 + (terms - 1) * 15)) // 2 # assignment_lhs_identifier:sum, assignment_rhs_atom:1, assignment_rhs_atom:15, assignment_rhs_atom:2, assignment_rhs_atom:30, assignment_rhs_atom:terms, augmented_assignment:Sub, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, decrement_variable:sum:1, decrement_variable:sum:15, decrement_variable:sum:2, decrement_variable:sum:30, decrement_variable:sum:terms, int_literal, literal:Num, suggest_constant_definition, update_variable:sum:1, update_variable:sum:15, update_variable:sum:2, update_variable:sum:30, update_variable:sum:terms
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +32), function_returning_something:solution (-> +32)
    sum = 0 # assignment, assignment_lhs_identifier:sum, assignment_rhs_atom:0, int_literal, literal:Num
    num = 0 # assignment, assignment_lhs_identifier:num, assignment_rhs_atom:0, int_literal, literal:Num
    while 1: # int_literal, literal:Num, while (-> +28)
        num += 3 # assignment_lhs_identifier:num, assignment_rhs_atom:3, augmented_assignment:Add, increment_variable:num:3, int_literal, literal:Num, suggest_constant_definition, update_variable:num:3
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, increment_variable:sum:num, update_variable:sum:num
        num += 2 # assignment_lhs_identifier:num, assignment_rhs_atom:2, augmented_assignment:Add, increment_variable:num:2, int_literal, literal:Num, update_variable:num:2
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, increment_variable:sum:num, update_variable:sum:num
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:num:1, int_literal, literal:Num, update_variable:num:1
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, increment_variable:sum:num, update_variable:sum:num
        num += 3 # assignment_lhs_identifier:num, assignment_rhs_atom:3, augmented_assignment:Add, increment_variable:num:3, int_literal, literal:Num, suggest_constant_definition, update_variable:num:3
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, increment_variable:sum:num, update_variable:sum:num
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:num:1, int_literal, literal:Num, update_variable:num:1
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, increment_variable:sum:num, update_variable:sum:num
        num += 2 # assignment_lhs_identifier:num, assignment_rhs_atom:2, augmented_assignment:Add, increment_variable:num:2, int_literal, literal:Num, update_variable:num:2
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, increment_variable:sum:num, update_variable:sum:num
        num += 3 # assignment_lhs_identifier:num, assignment_rhs_atom:3, augmented_assignment:Add, increment_variable:num:3, int_literal, literal:Num, suggest_constant_definition, update_variable:num:3
        if num >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:n, if_test_atom:num
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_atom:num, augmented_assignment:Add, increment_variable:sum:num, update_variable:sum:num
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +22), function_returning_something:solution (-> +22)
    xmulti = [] # assignment, assignment_lhs_identifier:xmulti, literal:List
    zmulti = [] # assignment, assignment_lhs_identifier:zmulti, literal:List
    z = 3 # assignment, assignment_lhs_identifier:z, assignment_rhs_atom:3, int_literal, literal:Num, suggest_constant_definition
    x = 5 # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:5, int_literal, literal:Num, suggest_constant_definition
    temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, int_literal, literal:Num
    while True: # infinite_while, literal:True, while (-> +7)
        result = z * temp # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:temp, assignment_rhs_atom:z, binary_operator:Mult
        if result < n: # comparison_operator:Lt, if (-> +5), if_test_atom:n, if_test_atom:result
            zmulti.append(result) # call_argument:result, if_then_branch (-> +1), method_call, method_call_name:append, method_call_object:zmulti, update_variable:zmulti:result
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:temp:1, int_literal, literal:Num, update_variable:temp:1
        else:
            temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, if_else_branch (-> +1), int_literal, literal:Num
            break
    while True: # infinite_while, literal:True, while (-> +6)
        result = x * temp # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:temp, assignment_rhs_atom:x, binary_operator:Mult
        if result < n: # comparison_operator:Lt, if (-> +4), if_test_atom:n, if_test_atom:result
            xmulti.append(result) # call_argument:result, if_then_branch (-> +1), method_call, method_call_name:append, method_call_object:xmulti, update_variable:xmulti:result
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:temp:1, int_literal, literal:Num, update_variable:temp:1
        else:
            break # if_else_branch
    collection = list(set(xmulti + zmulti)) # assignment, assignment_lhs_identifier:collection, assignment_rhs_atom:xmulti, assignment_rhs_atom:zmulti, binary_operator:Add, call_argument:, composition, function_call:list, function_call:set
    return sum(collection) # call_argument:collection, function_call:sum, function_tail_call:sum, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0]) # binary_operator:Mod, boolean_operator:Or, call_argument:, call_argument:n, comparison_operator:Eq, composition, comprehension:List, comprehension_for_count:1, divisibility_test:3, divisibility_test:5, filtered_comprehension, function_call:range, function_call:sum, function_tail_call:sum, int_literal, literal:Num, range:n, return, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol6.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +9), function_returning_something:solution (-> +9)
    a = 3 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:3, int_literal, literal:Num, suggest_constant_definition
    result = 0 # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:0, int_literal, literal:Num
    while a < n: # comparison_operator:Lt, while (-> +5)
        if a % 3 == 0 or a % 5 == 0: # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, divisibility_test:3, divisibility_test:5, if (-> +3), if_test_atom:0, if_test_atom:3, if_test_atom:5, if_test_atom:a, int_literal, literal:Num, suggest_constant_definition
            result += a # assignment_lhs_identifier:result, assignment_rhs_atom:a, augmented_assignment:Add, if_then_branch, increment_variable:result:a, update_variable:result:a
        elif a % 15 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:15, if (-> +1), if_test_atom:0, if_test_atom:15, if_test_atom:a, int_literal, literal:Num, suggest_constant_definition
            result -= a # assignment_lhs_identifier:result, assignment_rhs_atom:a, augmented_assignment:Sub, decrement_variable:result:a, if_elif_branch, update_variable:result:a
        a += 1 # assignment_lhs_identifier:a, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:a:1, int_literal, literal:Num, update_variable:a:1
    return result # return:result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol7.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_something:solution (-> +7)
    result = 0 # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(n): # accumulate_elements:result (-> +4), call_argument:n, for:i (-> +4), for_range:n (-> +4), function_call:range, range:n
        if i % 3 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:3, if (-> +3), if_test_atom:0, if_test_atom:3, if_test_atom:i, int_literal, literal:Num, suggest_constant_definition
            result += i # assignment_lhs_identifier:result, assignment_rhs_atom:i, augmented_assignment:Add, if_then_branch, increment_variable:result:i, update_variable:result:i
        elif i % 5 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:5, if (-> +1), if_test_atom:0, if_test_atom:5, if_test_atom:i, int_literal, literal:Num, suggest_constant_definition
            result += i # assignment_lhs_identifier:result, assignment_rhs_atom:i, augmented_assignment:Add, if_elif_branch, increment_variable:result:i, update_variable:result:i
    return result # return:result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_returning_something:solution (-> +8)
    i = 1 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:1, int_literal, literal:Num
    j = 2 # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:2, int_literal, literal:Num
    sum = 0 # assignment, assignment_lhs_identifier:sum, assignment_rhs_atom:0, int_literal, literal:Num
    while j <= n: # comparison_operator:LtE, while (-> +3)
        if j % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:j, int_literal, literal:Num
            sum += j # assignment_lhs_identifier:sum, assignment_rhs_atom:j, augmented_assignment:Add, if_then_branch, increment_variable:sum:j, update_variable:sum:j
        i, j = j, i + j # assignment, assignment_lhs_identifier:i, assignment_lhs_identifier:j, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, increment_variable:i:j, increment_variable:j:i, update_variable:i:j, update_variable:j:i
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_something:solution (-> +7)
    ls = [] # assignment, assignment_lhs_identifier:ls, literal:List
    a, b = 0, 1 # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:0, assignment_rhs_atom:1, int_literal, literal:Num, literal:Tuple
    while b <= n: # comparison_operator:LtE, while (-> +3)
        if b % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:b, int_literal, literal:Num
            ls.append(b) # call_argument:b, if_then_branch, method_call, method_call_name:append, method_call_object:ls, update_variable:ls:b
        a, b = b, a + b # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, increment_variable:a:b, increment_variable:b:a, update_variable:a:b, update_variable:b:a
    return ls # return:ls

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +9), function_returning_something:solution (-> +9)
    if n <= 1: # comparison_operator:LtE, if (-> +1), if_test_atom:1, if_test_atom:n, int_literal, literal:Num
        return 0 # if_then_branch, int_literal, literal:Num, return:0
    a = 0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, int_literal, literal:Num
    b = 2 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:2, int_literal, literal:Num
    count = 0 # assignment, assignment_lhs_identifier:count, assignment_rhs_atom:0, int_literal, literal:Num
    while 4 * b + a <= n: # binary_operator:Add, binary_operator:Mult, comparison_operator:LtE, int_literal, literal:Num, suggest_constant_definition, while (-> +2)
        a, b = b, 4 * b + a # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:4, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, binary_operator:Mult, increment_variable:a:4, increment_variable:a:b, increment_variable:b:4, increment_variable:b:a, int_literal, literal:Num, suggest_constant_definition, update_variable:a:4, update_variable:a:b, update_variable:b:4, update_variable:b:a
        count += a # assignment_lhs_identifier:count, assignment_rhs_atom:a, augmented_assignment:Add, increment_variable:count:a, update_variable:count:a
    return count + b # binary_operator:Add, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol4.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
from decimal import Decimal, getcontext # import:decimal:Decimal, import:decimal:getcontext, import_module:decimal, import_name:Decimal, import_name:getcontext
def solution(n): # function:solution (-> +12), function_returning_something:solution (-> +12)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    getcontext().prec = 100 # assignment, assignment_rhs_atom:100, function_call:getcontext, int_literal, literal:Num, suggest_constant_definition
    phi = (Decimal(5) ** Decimal(0.5) + 1) / Decimal(2) # assignment, assignment_lhs_identifier:phi, assignment_rhs_atom:0.5, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:5, binary_operator:Add, binary_operator:Div, binary_operator:Pow, call_argument:0.5, call_argument:2, call_argument:5, float_literal, function_call:Decimal, int_literal, literal:Num, suggest_constant_definition
    index = (math.floor(math.log(n * (phi + 2), phi) - 1) // 3) * 3 + 2 # assignment, assignment_lhs_identifier:index, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:math, assignment_rhs_atom:n, assignment_rhs_atom:phi, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:phi, composition, int_literal, literal:Num, method_call, method_call_name:floor, method_call_name:log, suggest_constant_definition
    num = Decimal(round(phi ** Decimal(index + 1))) / (phi + 2) # assignment, assignment_lhs_identifier:num, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:index, assignment_rhs_atom:phi, binary_operator:Add, binary_operator:Div, binary_operator:Pow, call_argument:, composition, function_call:Decimal, function_call:round, int_literal, literal:Num
    sum = num // 2 # assignment, assignment_lhs_identifier:sum, assignment_rhs_atom:2, assignment_rhs_atom:num, binary_operator:FloorDiv, int_literal, literal:Num
    return int(sum) # call_argument:sum, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +12), function_returning_something:solution (-> +12)
    a = [0, 1] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, assignment_rhs_atom:1, int_literal, literal:List, literal:Num
    i = 0 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:0, int_literal, literal:Num
    while a[i] <= n: # comparison_operator:LtE, index, while (-> +4)
        a.append(a[i] + a[i + 1]) # binary_operator:Add, call_argument:, index, index_arithmetic, int_literal, literal:Num, method_call, method_call_name:append, method_call_object:a, update_variable:a:
        if a[i + 2] > n: # binary_operator:Add, comparison_operator:Gt, if (-> +1), if_test_atom:2, if_test_atom:a, if_test_atom:i, if_test_atom:n, index, index_arithmetic, int_literal, literal:Num
            break # if_then_branch
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
    sum = 0 # assignment, assignment_lhs_identifier:sum, assignment_rhs_atom:0, int_literal, literal:Num
    for j in range(len(a) - 1): # accumulate_elements:sum (-> +2), binary_operator:Sub, call_argument:, call_argument:a, composition, for:j (-> +2), for_range:_ (-> +2), function_call:len, function_call:range, int_literal, literal:Num, range:_
        if a[j] % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:a, if_test_atom:j, index, int_literal, literal:Num
            sum += a[j] # assignment_lhs_identifier:sum, assignment_rhs_atom:a, assignment_rhs_atom:j, augmented_assignment:Add, if_then_branch, increment_variable:sum:a, increment_variable:sum:j, index, update_variable:sum:a, update_variable:sum:j
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol1.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def isprime(no): # function:isprime (-> +9), function_returning_something:isprime (-> +9)
    if no == 2: # comparison_operator:Eq, if (-> +3), if_test_atom:2, if_test_atom:no, int_literal, literal:Num
        return True # if_then_branch, literal:True, return:True
    elif no % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:no, int_literal, literal:Num
        return False # if_elif_branch, literal:False, return:False
    sq = int(math.sqrt(no)) + 1 # assignment, assignment_lhs_identifier:sq, assignment_rhs_atom:1, assignment_rhs_atom:math, assignment_rhs_atom:no, binary_operator:Add, call_argument:, call_argument:no, composition, function_call:int, int_literal, literal:Num, method_call, method_call_name:sqrt
    for i in range(3, sq, 2): # call_argument:2, call_argument:3, call_argument:sq, for:i (-> +2), for_range:3:sq:2 (-> +2), function_call:range, int_literal, literal:Num, range:3:sq:2, suggest_constant_definition, universal_quantifier (-> +3)
        if no % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:no, int_literal, literal:Num
            return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def solution(n): # function:solution (-> +24), function_returning_something:solution (-> +24)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    maxNumber = 0 # assignment, assignment_lhs_identifier:maxNumber, assignment_rhs_atom:0, int_literal, literal:Num
    if isprime(n): # call_argument:n, function_call:isprime, if (-> +16), if_test_atom:n
        return n # if_then_branch, return:n
    else:
        while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +1), if_else_branch (-> +13), int_literal, literal:Num, while (-> +1)
            n = n / 2 # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, int_literal, literal:Num, suggest_augmented_assignment, update_variable:n:2
        if isprime(n): # call_argument:n, function_call:isprime, if (-> +11), if_test_atom:n, nested_if:1 (-> +11)
            return int(n) # call_argument:n, function_call:int, function_tail_call:int, if_then_branch, return
        else:
            n1 = int(math.sqrt(n)) + 1 # assignment, assignment_lhs_identifier:n1, assignment_rhs_atom:1, assignment_rhs_atom:math, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:n, composition, function_call:int, if_else_branch (-> +8), int_literal, literal:Num, method_call, method_call_name:sqrt
            for i in range(3, n1, 2): # call_argument:2, call_argument:3, call_argument:n1, for:i (-> +6), for_range:3:n1:2 (-> +6), function_call:range, int_literal, literal:Num, range:3:n1:2, suggest_constant_definition
                if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +5), if_test_atom:0, if_test_atom:i, if_test_atom:n, int_literal, literal:Num, nested_if:2 (-> +5)
                    if isprime(n / i): # binary_operator:Div, call_argument:, function_call:isprime, if (-> +4), if_test_atom:i, if_test_atom:n, if_then_branch (-> +4), nested_if:3 (-> +4)
                        maxNumber = n / i # assignment, assignment_lhs_identifier:maxNumber, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, if_then_branch (-> +1)
                        break
                    elif isprime(i): # call_argument:i, function_call:isprime, if (-> +1), if_test_atom:i, nested_if:3 (-> +1)
                        maxNumber = i # assignment, assignment_lhs_identifier:maxNumber, assignment_rhs_atom:i, if_elif_branch
            return maxNumber # return:maxNumber

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +16), function_returning_something:solution (-> +16)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    prime = 1 # assignment, assignment_lhs_identifier:prime, assignment_rhs_atom:1, int_literal, literal:Num
    i = 2 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:2, int_literal, literal:Num
    while i * i <= n: # binary_operator:Mult, comparison_operator:LtE, evolve_state (-> +4), while (-> +4)
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +2)
            prime = i # assignment, assignment_lhs_identifier:prime, assignment_rhs_atom:i
            n //= i # assignment_lhs_identifier:n, assignment_rhs_atom:i, augmented_assignment:FloorDiv, update_variable:n:i
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
    if n > 1: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:n, int_literal, literal:Num
        prime = n # assignment, assignment_lhs_identifier:prime, assignment_rhs_atom:n, if_then_branch
    return int(prime) # call_argument:prime, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n: int) -> int: # function:solution (-> +18), function_returning_something:solution (-> +18)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int
    except (TypeError, ValueError): # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    i = 2 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:2, int_literal, literal:Num
    ans = 0 # assignment, assignment_lhs_identifier:ans, assignment_rhs_atom:0, int_literal, literal:Num
    if n == 2: # comparison_operator:Eq, if (-> +1), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        return 2 # if_then_branch, int_literal, literal:Num, return:2
    while n > 2: # comparison_operator:Gt, evolve_state (-> +6), int_literal, literal:Num, while (-> +6)
        while n % i != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test, evolve_state (-> +1), int_literal, literal:Num, while (-> +1)
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
        ans = i # assignment, assignment_lhs_identifier:ans, assignment_rhs_atom:i
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +1)
            n = n / i # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, suggest_augmented_assignment, update_variable:n:i
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
    return int(ans) # call_argument:ans, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_04/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_returning_something:solution (-> +8)
    for number in range(n - 1, 10000, -1): # binary_operator:Sub, call_argument:, call_argument:-1, call_argument:10000, find_first_element (-> +6), for:number (-> +7), for_range:_:10000:-1 (-> +7), function_call:range, int_literal, literal:Num, range:_:10000:-1, suggest_constant_definition
        strNumber = str(number) # assignment, assignment_lhs_identifier:strNumber, assignment_rhs_atom:number, call_argument:number, function_call:str
        if strNumber == strNumber[::-1]: # comparison_operator:Eq, if (-> +5), if_test_atom:-1, if_test_atom:strNumber, int_literal, literal:Num, slice_step
            divisor = 999 # assignment, assignment_lhs_identifier:divisor, assignment_rhs_atom:999, if_then_branch (-> +4), int_literal, literal:Num, suggest_constant_definition
            while divisor != 99: # comparison_operator:NotEq, evolve_state (-> +3), int_literal, literal:Num, suggest_constant_definition, while (-> +3)
                if (number % divisor == 0) and (len(str(int(number / divisor))) == 3): # binary_operator:Div, binary_operator:Mod, boolean_operator:And, call_argument:, comparison_operator:Eq, composition, divisibility_test, function_call:int, function_call:len, function_call:str, if (-> +1), if_test_atom:0, if_test_atom:3, if_test_atom:divisor, if_test_atom:number, int_literal, literal:Num, nested_if:1 (-> +1), suggest_constant_definition
                    return number # if_then_branch, return:number
                divisor -= 1 # assignment_lhs_identifier:divisor, assignment_rhs_atom:1, augmented_assignment:Sub, decrement_variable:divisor:1, int_literal, literal:Num, update_variable:divisor:1

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_04/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_something:solution (-> +7)
    answer = 0 # assignment, assignment_lhs_identifier:answer, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(999, 99, -1): # accumulate_elements:answer (-> +4), call_argument:-1, call_argument:99, call_argument:999, for:i (-> +4), for_range:999:99:-1 (-> +4), function_call:range, int_literal, literal:Num, range:999:99:-1, square_nested_for (-> +4), suggest_constant_definition
        for j in range(999, 99, -1): # accumulate_elements:answer (-> +3), call_argument:-1, call_argument:99, call_argument:999, for:j (-> +3), for_range:999:99:-1 (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), range:999:99:-1, suggest_constant_definition
            t = str(i * j) # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Mult, call_argument:, function_call:str
            if t == t[::-1] and i * j < n: # binary_operator:Mult, boolean_operator:And, comparison_operator:Eq, comparison_operator:Lt, if (-> +1), if_test_atom:-1, if_test_atom:i, if_test_atom:j, if_test_atom:n, if_test_atom:t, int_literal, literal:Num, slice_step
                answer = max(answer, i * j) # assignment, assignment_lhs_identifier:answer, assignment_rhs_atom:answer, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Mult, call_argument:, call_argument:answer, function_call:max, if_then_branch, update_variable:answer:i, update_variable:answer:j
    return answer # return:answer

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_05/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +18), function_returning_something:solution (-> +18)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    i = 0 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:0, int_literal, literal:Num
    while 1: # int_literal, literal:Num, while (-> +10)
        i += n * (n - 1) # assignment_lhs_identifier:i, assignment_rhs_atom:1, assignment_rhs_atom:n, augmented_assignment:Add, binary_operator:Mult, binary_operator:Sub, increment_variable:i:1, increment_variable:i:n, int_literal, literal:Num, update_variable:i:1, update_variable:i:n
        nfound = 0 # assignment, assignment_lhs_identifier:nfound, assignment_rhs_atom:0, int_literal, literal:Num
        for j in range(2, n): # call_argument:2, call_argument:n, for:j (-> +3), for_range:2:n (-> +3), function_call:range, int_literal, literal:Num, range:2:n
            if i % j != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test, if (-> +2), if_test_atom:0, if_test_atom:i, if_test_atom:j, int_literal, literal:Num
                nfound = 1 # assignment, assignment_lhs_identifier:nfound, assignment_rhs_atom:1, if_then_branch (-> +1), int_literal, literal:Num
                break
        if nfound == 0: # comparison_operator:Eq, if (-> +3), if_test_atom:0, if_test_atom:nfound, int_literal, literal:Num
            if i == 0: # comparison_operator:Eq, if (-> +1), if_test_atom:0, if_test_atom:i, if_then_branch (-> +2), int_literal, literal:Num, nested_if:1 (-> +1)
                i = 1 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:1, if_then_branch, int_literal, literal:Num
            return i # return:i

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_05/sol2.py
# ----------------------------------------------------------------------------------------
def gcd(x, y): # function:gcd (-> +1), function_returning_something:gcd (-> +1), recursive_function:gcd (-> +1), tail_recursive_function:gcd (-> +1)
    return x if y == 0 else gcd(y, x % y) # binary_operator:Mod, call_argument:, call_argument:y, comparison_operator:Eq, conditional_expression, function_call:gcd, function_tail_call:gcd, int_literal, literal:Num, return
def lcm(x, y): # function:lcm (-> +1), function_returning_something:lcm (-> +1)
    return (x * y) // gcd(x, y) # binary_operator:FloorDiv, binary_operator:Mult, call_argument:x, call_argument:y, function_call:gcd, return
def solution(n): # function:solution (-> +4), function_returning_something:solution (-> +4)
    g = 1 # assignment, assignment_lhs_identifier:g, assignment_rhs_atom:1, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:g (-> +1), binary_operator:Add, call_argument:, call_argument:1, for:i (-> +1), for_range:1:_ (-> +1), function_call:range, int_literal, literal:Num, range:1:_
        g = lcm(g, i) # assignment, assignment_lhs_identifier:g, assignment_rhs_atom:g, assignment_rhs_atom:i, call_argument:g, call_argument:i, function_call:lcm, update_variable:g:i
    return g # return:g

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_something:solution (-> +7)
    suma = 0 # assignment, assignment_lhs_identifier:suma, assignment_rhs_atom:0, int_literal, literal:Num
    sumb = 0 # assignment, assignment_lhs_identifier:sumb, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:suma (-> +2), accumulate_elements:sumb (-> +2), binary_operator:Add, call_argument:, call_argument:1, for:i (-> +2), for_range:1:_ (-> +2), function_call:range, int_literal, literal:Num, range:1:_
        suma += i ** 2 # assignment_lhs_identifier:suma, assignment_rhs_atom:2, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Pow, increment_variable:suma:2, increment_variable:suma:i, int_literal, literal:Num, update_variable:suma:2, update_variable:suma:i
        sumb += i # assignment_lhs_identifier:sumb, assignment_rhs_atom:i, augmented_assignment:Add, increment_variable:sumb:i, update_variable:sumb:i
    sum = sumb ** 2 - suma # assignment, assignment_lhs_identifier:sum, assignment_rhs_atom:2, assignment_rhs_atom:suma, assignment_rhs_atom:sumb, binary_operator:Pow, binary_operator:Sub, int_literal, literal:Num
    return sum # return:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +4), function_returning_something:solution (-> +4)
    suma = n * (n + 1) / 2 # assignment, assignment_lhs_identifier:suma, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, int_literal, literal:Num
    suma **= 2 # assignment_lhs_identifier:suma, assignment_rhs_atom:2, augmented_assignment:Pow, int_literal, literal:Num, update_variable:suma:2
    sumb = n * (n + 1) * (2 * n + 1) / 6 # assignment, assignment_lhs_identifier:sumb, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, int_literal, literal:Num, suggest_constant_definition
    return int(suma - sumb) # binary_operator:Sub, call_argument:, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol3.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def solution(n): # function:solution (-> +3), function_returning_something:solution (-> +3)
    sum_of_squares = sum([i * i for i in range(1, n + 1)]) # assignment, assignment_lhs_identifier:sum_of_squares, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:1, composition, comprehension:List, comprehension_for_count:1, function_call:range, function_call:sum, int_literal, literal:Num, range:1:_
    square_of_sum = int(math.pow(sum(range(1, n + 1)), 2)) # assignment, assignment_lhs_identifier:square_of_sum, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:math, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:1, call_argument:2, composition, function_call:int, function_call:range, function_call:sum, int_literal, literal:Num, method_call, method_call_name:pow, range:1:_
    return square_of_sum - sum_of_squares # binary_operator:Sub, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +3), function_returning_something:solution (-> +3)
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6 # assignment, assignment_lhs_identifier:sum_of_squares, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, int_literal, literal:Num, suggest_constant_definition
    square_of_sum = (n * (n + 1) / 2) ** 2 # assignment, assignment_lhs_identifier:square_of_sum, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Pow, int_literal, literal:Num
    return int(square_of_sum - sum_of_squares) # binary_operator:Sub, call_argument:, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt
def isprime(n): # function:isprime (-> +10), function_returning_something:isprime (-> +10)
    if n == 2: # comparison_operator:Eq, if (-> +8), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        return True # if_then_branch, literal:True, return:True
    elif n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +6), if_test_atom:0, if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        return False # if_elif_branch, literal:False, return:False
    else:
        sq = int(sqrt(n)) + 1 # assignment, assignment_lhs_identifier:sq, assignment_rhs_atom:1, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:n, composition, function_call:int, function_call:sqrt, if_else_branch (-> +3), int_literal, literal:Num
        for i in range(3, sq, 2): # call_argument:2, call_argument:3, call_argument:sq, for:i (-> +2), for_range:3:sq:2 (-> +2), function_call:range, int_literal, literal:Num, range:3:sq:2, suggest_constant_definition
            if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:n, int_literal, literal:Num, nested_if:1 (-> +1)
                return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def solution(n): # function:solution (-> +11), function_returning_something:solution (-> +11)
    i = 0 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:0, int_literal, literal:Num
    j = 1 # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:1, int_literal, literal:Num
    while i != n and j < 3: # boolean_operator:And, comparison_operator:Lt, comparison_operator:NotEq, evolve_state (-> +3), int_literal, literal:Num, suggest_constant_definition, while (-> +3)
        j += 1 # assignment_lhs_identifier:j, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:j:1, int_literal, literal:Num, update_variable:j:1
        if isprime(j): # call_argument:j, function_call:isprime, if (-> +1), if_test_atom:j
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
    while i != n: # comparison_operator:NotEq, while (-> +3)
        j += 2 # assignment_lhs_identifier:j, assignment_rhs_atom:2, augmented_assignment:Add, increment_variable:j:2, int_literal, literal:Num, update_variable:j:2
        if isprime(j): # call_argument:j, function_call:isprime, if (-> +1), if_test_atom:j
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
    return j # return:j

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol2.py
# ----------------------------------------------------------------------------------------
def isprime(number): # function:isprime (-> +4), function_returning_something:isprime (-> +4)
    for i in range(2, int(number ** 0.5) + 1): # binary_operator:Add, binary_operator:Pow, call_argument:, call_argument:2, composition, float_literal, for:i (-> +2), for_range:2:_ (-> +2), function_call:int, function_call:range, int_literal, literal:Num, range:2:_, suggest_constant_definition, universal_quantifier (-> +3)
        if number % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:number, int_literal, literal:Num
            return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def solution(n): # function:solution (-> +15), function_returning_something:solution (-> +15)
    try: # try (-> +3), try_except:TypeError (-> +3), try_except:ValueError (-> +3), try_raise:TypeError (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int
    except (TypeError, ValueError) as e: # except:TypeError, except:ValueError
        raise TypeError("Parameter n must be int or passive of cast to int.") # call_argument:, function_call:TypeError, literal:Str, raise:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    primes = [] # assignment, assignment_lhs_identifier:primes, literal:List
    num = 2 # assignment, assignment_lhs_identifier:num, assignment_rhs_atom:2, int_literal, literal:Num
    while len(primes) < n: # call_argument:primes, comparison_operator:Lt, evolve_state (-> +5), function_call:len, while (-> +5)
        if isprime(num): # call_argument:num, function_call:isprime, if (-> +4), if_test_atom:num
            primes.append(num) # call_argument:num, if_then_branch (-> +1), method_call, method_call_name:append, method_call_object:primes, update_variable:primes:num
            num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:num:1, int_literal, literal:Num, update_variable:num:1
        else:
            num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, if_else_branch, increment_variable:num:1, int_literal, literal:Num, update_variable:num:1
    return primes[len(primes) - 1] # binary_operator:Sub, call_argument:primes, function_call:len, index, index_arithmetic, int_literal, literal:Num, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol3.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
import itertools # import:itertools, import_module:itertools
def primeCheck(number): # function:primeCheck (-> +3), function_returning_something:primeCheck (-> +3)
    if number % 2 == 0 and number > 2: # binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:number, int_literal, literal:Num
        return False # if_then_branch, literal:False, return:False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # binary_operator:Add, binary_operator:Mod, call_argument:, call_argument:2, call_argument:3, call_argument:number, composition, comprehension:Generator, comprehension_for_count:1, function_call:all, function_call:int, function_call:range, function_tail_call:all, int_literal, literal:Num, method_call, method_call_name:sqrt, range:3:_:2, return, suggest_constant_definition
def prime_generator(): # function:prime_generator (-> +5), generator:prime_generator (-> +5)
    num = 2 # assignment, assignment_lhs_identifier:num, assignment_rhs_atom:2, int_literal, literal:Num
    while True: # infinite_while, literal:True, while (-> +3)
        if primeCheck(num): # call_argument:num, function_call:primeCheck, if (-> +1), if_test_atom:num
            yield num # if_then_branch, yield:num
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:num:1, int_literal, literal:Num, update_variable:num:1
def solution(n): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return next(itertools.islice(prime_generator(), n - 1, n)) # binary_operator:Sub, call_argument:, call_argument:n, composition, function_call:next, function_call:prime_generator, function_tail_call:next, int_literal, literal:Num, method_call, method_call_name:islice, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol1.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys
N = """73167176531330624919225119674426574742355349194934\ # assignment, assignment_lhs_identifier:N
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
def solution(n): # function:solution (-> +8), function_returning_something:solution (-> +8)
    LargestProduct = -sys.maxsize - 1 # assignment, assignment_lhs_identifier:LargestProduct, assignment_rhs_atom:1, assignment_rhs_atom:sys, binary_operator:Sub, int_literal, literal:Num, unary_operator:USub
    for i in range(len(n) - 12): # accumulate_elements:product (-> +5), binary_operator:Sub, call_argument:, call_argument:n, composition, for:i (-> +5), for_range:13 (-> +5), for_range:_ (-> +5), function_call:len, function_call:range, int_literal, literal:Num, range:_, suggest_constant_definition
        product = 1 # assignment, assignment_lhs_identifier:product, assignment_rhs_atom:1, int_literal, literal:Num
        for j in range(13): # accumulate_elements:product (-> +1), call_argument:13, for:j (-> +1), for_range:13 (-> +1), function_call:range, int_literal, literal:Num, nested_for:1 (-> +1), range:13, suggest_constant_definition
            product *= int(n[i + j]) # assignment_lhs_identifier:product, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:n, augmented_assignment:Mult, binary_operator:Add, call_argument:, function_call:int, index, index_arithmetic, update_variable:product:i, update_variable:product:j, update_variable:product:n
        if product > LargestProduct: # comparison_operator:Gt, if (-> +1), if_test_atom:LargestProduct, if_test_atom:product
            LargestProduct = product # assignment, assignment_lhs_identifier:LargestProduct, assignment_rhs_atom:product, if_then_branch
    return LargestProduct # return:LargestProduct

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol2.py
# ----------------------------------------------------------------------------------------
from functools import reduce # import:functools:reduce, import_module:functools, import_name:reduce
N = ( # assignment, assignment_lhs_identifier:N
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
def solution(n): # function:solution (-> +4), function_returning_something:solution (-> +4)
    return max( # composition, function_call:max, function_tail_call:max, return
        [
            reduce(lambda x, y: int(x) * int(y), n[i : i + 13]) # binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:x, call_argument:y, composition, comprehension:List, comprehension_for_count:1, function_call:int, function_call:reduce, int_literal, lambda_function, literal:Num, slice, suggest_constant_definition
            for i in range(len(n) - 12) # binary_operator:Sub, call_argument:, call_argument:n, composition, function_call:len, function_call:range, int_literal, literal:Num, range:_, suggest_constant_definition
        ]
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol3.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys
N = """73167176531330624919225119674426574742355349194934\ # assignment, assignment_lhs_identifier:N
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
def streval(s: str) -> int: # function:streval (-> +4), function_returning_something:streval (-> +4)
    ret = 1 # assignment, assignment_lhs_identifier:ret, assignment_rhs_atom:1, int_literal, literal:Num
    for it in s: # accumulate_elements:ret (-> +1), for:it (-> +1), for_each (-> +1)
        ret *= int(it) # assignment_lhs_identifier:ret, assignment_rhs_atom:it, augmented_assignment:Mult, call_argument:it, function_call:int, update_variable:ret:it
    return ret # return:ret
def solution(n: str) -> int: # function:solution (-> +12), function_returning_something:solution (-> +12)
    LargestProduct = -sys.maxsize - 1 # assignment, assignment_lhs_identifier:LargestProduct, assignment_rhs_atom:1, assignment_rhs_atom:sys, binary_operator:Sub, int_literal, literal:Num, unary_operator:USub
    substr = n[:13] # assignment, assignment_lhs_identifier:substr, assignment_rhs_atom:13, assignment_rhs_atom:n, int_literal, literal:Num, slice, suggest_constant_definition
    cur_index = 13 # assignment, assignment_lhs_identifier:cur_index, assignment_rhs_atom:13, int_literal, literal:Num, suggest_constant_definition
    while cur_index < len(n) - 13: # binary_operator:Sub, call_argument:n, comparison_operator:Lt, function_call:len, int_literal, literal:Num, suggest_constant_definition, while (-> +7)
        if int(n[cur_index]) >= int(substr[0]): # call_argument:, comparison_operator:GtE, function_call:int, if (-> +6), if_test_atom:0, if_test_atom:cur_index, if_test_atom:n, if_test_atom:substr, index, int_literal, literal:Num
            substr = substr[1:] + n[cur_index] # assignment, assignment_lhs_identifier:substr, assignment_rhs_atom:1, assignment_rhs_atom:cur_index, assignment_rhs_atom:n, assignment_rhs_atom:substr, binary_operator:Add, if_then_branch (-> +1), increment_variable:substr:1, increment_variable:substr:cur_index, increment_variable:substr:n, index, int_literal, literal:Num, slice, update_variable:substr:1, update_variable:substr:cur_index, update_variable:substr:n
            cur_index += 1 # assignment_lhs_identifier:cur_index, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:cur_index:1, int_literal, literal:Num, update_variable:cur_index:1
        else:
            LargestProduct = max(LargestProduct, streval(substr)) # assignment, assignment_lhs_identifier:LargestProduct, assignment_rhs_atom:LargestProduct, assignment_rhs_atom:substr, call_argument:, call_argument:LargestProduct, call_argument:substr, composition, function_call:max, function_call:streval, if_else_branch (-> +2), update_variable:LargestProduct:substr
            substr = n[cur_index : cur_index + 13] # assignment, assignment_lhs_identifier:substr, assignment_rhs_atom:13, assignment_rhs_atom:cur_index, assignment_rhs_atom:n, binary_operator:Add, int_literal, literal:Num, slice, suggest_constant_definition
            cur_index += 13 # assignment_lhs_identifier:cur_index, assignment_rhs_atom:13, augmented_assignment:Add, increment_variable:cur_index:13, int_literal, literal:Num, suggest_constant_definition, update_variable:cur_index:13
    return LargestProduct # return:LargestProduct

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +7), function_returning_something:solution (-> +7)
    for a in range(300): # call_argument:300, for:a (-> +6), for_range:300 (-> +6), for_range:400 (-> +6), for_range:500 (-> +6), function_call:range, int_literal, literal:Num, range:300, suggest_constant_definition
        for b in range(400): # call_argument:400, for:b (-> +5), for_range:400 (-> +5), for_range:500 (-> +5), function_call:range, int_literal, literal:Num, nested_for:1 (-> +5), range:400, suggest_constant_definition
            for c in range(500): # call_argument:500, for:c (-> +4), for_range:500 (-> +4), function_call:range, int_literal, literal:Num, nested_for:2 (-> +4), range:500, suggest_constant_definition
                if a < b < c: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +3), if_test_atom:a, if_test_atom:b, if_test_atom:c
                    if (a ** 2) + (b ** 2) == (c ** 2): # binary_operator:Add, binary_operator:Pow, comparison_operator:Eq, if (-> +2), if_test_atom:2, if_test_atom:a, if_test_atom:b, if_test_atom:c, if_then_branch (-> +2), int_literal, literal:Num, nested_if:1 (-> +2)
                        if (a + b + c) == 1000: # binary_operator:Add, comparison_operator:Eq, if (-> +1), if_test_atom:1000, if_test_atom:a, if_test_atom:b, if_test_atom:c, if_then_branch (-> +1), int_literal, literal:Num, nested_if:2 (-> +1), suggest_constant_definition
                            return a * b * c # binary_operator:Mult, if_then_branch, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +10), function_returning_something:solution (-> +10)
    product = -1 # assignment, assignment_lhs_identifier:product, assignment_rhs_atom:-1, int_literal, literal:Num
    d = 0 # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:0, int_literal, literal:Num
    for a in range(1, n // 3): # binary_operator:FloorDiv, call_argument:, call_argument:1, for:a (-> +6), for_range:1:_ (-> +6), function_call:range, int_literal, literal:Num, range:1:_, suggest_constant_definition
        b = (n * n - 2 * a * n) // (2 * n - 2 * a) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:2, assignment_rhs_atom:a, assignment_rhs_atom:n, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num
        c = n - a - b # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:n, binary_operator:Sub
        if c * c == (a * a + b * b): # binary_operator:Add, binary_operator:Mult, comparison_operator:Eq, if (-> +3), if_test_atom:a, if_test_atom:b, if_test_atom:c
            d = a * b * c # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:c, binary_operator:Mult, if_then_branch (-> +2)
            if d >= product: # comparison_operator:GtE, if (-> +1), if_test_atom:d, if_test_atom:product, nested_if:1 (-> +1)
                product = d # assignment, assignment_lhs_identifier:product, assignment_rhs_atom:d, if_then_branch
    return product # return:product

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol3.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +7), function_returning_something:solution (-> +7)
    return [ # return
        a * b * c # binary_operator:Mult, comprehension:List, comprehension_for_count:3, index
        for a in range(1, 999) # call_argument:1, call_argument:999, function_call:range, int_literal, literal:Num, range:1:999, suggest_constant_definition
        for b in range(a, 999) # call_argument:999, call_argument:a, function_call:range, int_literal, literal:Num, range:a:999, suggest_constant_definition
        for c in range(b, 999) # call_argument:999, call_argument:b, function_call:range, int_literal, literal:Num, range:b:999, suggest_constant_definition
        if (a * a + b * b == c * c) and (a + b + c == 1000) # binary_operator:Add, binary_operator:Mult, boolean_operator:And, comparison_operator:Eq, filtered_comprehension, int_literal, literal:Num, suggest_constant_definition
    ][0] # int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt
def is_prime(n): # function:is_prime (-> +4), function_returning_something:is_prime (-> +4)
    for i in range(2, int(sqrt(n)) + 1): # binary_operator:Add, call_argument:, call_argument:2, call_argument:n, composition, for:i (-> +2), for_range:2:_ (-> +2), function_call:int, function_call:range, function_call:sqrt, int_literal, literal:Num, range:2:_, universal_quantifier (-> +3)
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:n, int_literal, literal:Num
            return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def sum_of_primes(n): # function:sum_of_primes (-> +8), function_returning_something:sum_of_primes (-> +8)
    if n > 2: # comparison_operator:Gt, if (-> +3), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        sumOfPrimes = 2 # assignment, assignment_lhs_identifier:sumOfPrimes, assignment_rhs_atom:2, if_then_branch, int_literal, literal:Num
    else:
        return 0 # if_else_branch, int_literal, literal:Num, return:0
    for i in range(3, n, 2): # accumulate_elements:sumOfPrimes (-> +2), call_argument:2, call_argument:3, call_argument:n, for:i (-> +2), for_range:3:n:2 (-> +2), function_call:range, int_literal, literal:Num, range:3:n:2, suggest_constant_definition
        if is_prime(i): # call_argument:i, function_call:is_prime, if (-> +1), if_test_atom:i
            sumOfPrimes += i # assignment_lhs_identifier:sumOfPrimes, assignment_rhs_atom:i, augmented_assignment:Add, if_then_branch, increment_variable:sumOfPrimes:i, update_variable:sumOfPrimes:i
    return sumOfPrimes # return:sumOfPrimes
def solution(n): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return sum_of_primes(n) # call_argument:n, function_call:sum_of_primes, function_tail_call:sum_of_primes, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol2.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
from itertools import takewhile # import:itertools:takewhile, import_module:itertools, import_name:takewhile
def primeCheck(number): # function:primeCheck (-> +3), function_returning_something:primeCheck (-> +3)
    if number % 2 == 0 and number > 2: # binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, divisibility_test:2, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:number, int_literal, literal:Num
        return False # if_then_branch, literal:False, return:False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # binary_operator:Add, binary_operator:Mod, call_argument:, call_argument:2, call_argument:3, call_argument:number, composition, comprehension:Generator, comprehension_for_count:1, function_call:all, function_call:int, function_call:range, function_tail_call:all, int_literal, literal:Num, method_call, method_call_name:sqrt, range:3:_:2, return, suggest_constant_definition
def prime_generator(): # function:prime_generator (-> +5), generator:prime_generator (-> +5)
    num = 2 # assignment, assignment_lhs_identifier:num, assignment_rhs_atom:2, int_literal, literal:Num
    while True: # infinite_while, literal:True, while (-> +3)
        if primeCheck(num): # call_argument:num, function_call:primeCheck, if (-> +1), if_test_atom:num
            yield num # if_then_branch, yield:num
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:num:1, int_literal, literal:Num, update_variable:num:1
def solution(n): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return sum(takewhile(lambda x: x < n, prime_generator())) # call_argument:, comparison_operator:Lt, composition, function_call:prime_generator, function_call:sum, function_call:takewhile, function_tail_call:sum, lambda_function, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol3.py
# ----------------------------------------------------------------------------------------
def prime_sum(n: int) -> int: # function:prime_sum (-> +12), function_returning_something:prime_sum (-> +12)
    list_ = [0 for i in range(n + 1)] # assignment, assignment_lhs_identifier:list_, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Add, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num, range:_
    list_[0] = 1 # assignment, assignment_lhs_identifier:list_, assignment_rhs_atom:1, index, int_literal, literal:Num
    list_[1] = 1 # assignment, assignment_lhs_identifier:list_, assignment_rhs_atom:1, index, int_literal, literal:Num
    for i in range(2, int(n ** 0.5) + 1): # binary_operator:Add, binary_operator:Pow, call_argument:, call_argument:2, composition, float_literal, for:i (-> +3), for_range:2:_ (-> +3), for_range:_:_:i (-> +3), function_call:int, function_call:range, int_literal, literal:Num, range:2:_, suggest_constant_definition
        if list_[i] == 0: # comparison_operator:Eq, if (-> +2), if_test_atom:0, if_test_atom:i, if_test_atom:list_, index, int_literal, literal:Num
            for j in range(i * i, n + 1, i): # binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:i, for:j (-> +1), for_range:_:_:i (-> +1), function_call:range, if_then_branch (-> +1), int_literal, literal:Num, nested_for:1 (-> +1), range:_:_:i
                list_[j] = 1 # assignment, assignment_lhs_identifier:list_, assignment_rhs_atom:1, index, int_literal, literal:Num
    s = 0 # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(n): # accumulate_elements:s (-> +2), call_argument:n, for:i (-> +2), for_range:n (-> +2), function_call:range, range:n
        if list_[i] == 0: # comparison_operator:Eq, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:list_, index, int_literal, literal:Num
            s += i # assignment_lhs_identifier:s, assignment_rhs_atom:i, augmented_assignment:Add, if_then_branch, increment_variable:s:i, update_variable:s:i
    return s # return:s

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_11/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def largest_product(grid): # function:largest_product (-> +27), function_returning_something:largest_product (-> +27)
    nColumns = len(grid[0]) # assignment, assignment_lhs_identifier:nColumns, assignment_rhs_atom:0, assignment_rhs_atom:grid, call_argument:, function_call:len, index, int_literal, literal:Num
    nRows = len(grid) # assignment, assignment_lhs_identifier:nRows, assignment_rhs_atom:grid, call_argument:grid, function_call:len
    largest = 0 # assignment, assignment_lhs_identifier:largest, assignment_rhs_atom:0, int_literal, literal:Num
    lrDiagProduct = 0 # assignment, assignment_lhs_identifier:lrDiagProduct, assignment_rhs_atom:0, int_literal, literal:Num
    rlDiagProduct = 0 # assignment, assignment_lhs_identifier:rlDiagProduct, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(nColumns): # call_argument:nColumns, for:i (-> +20), for_range:_ (-> +20), for_range:nColumns (-> +20), function_call:range, range:nColumns
        for j in range(nRows - 3): # binary_operator:Sub, call_argument:, for:j (-> +19), for_range:_ (-> +19), function_call:range, int_literal, literal:Num, nested_for:1 (-> +19), range:_, suggest_constant_definition
            vertProduct = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i] # assignment, assignment_lhs_identifier:vertProduct, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
            horzProduct = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3] # assignment, assignment_lhs_identifier:horzProduct, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
            if i < nColumns - 3: # binary_operator:Sub, comparison_operator:Lt, if (-> +5), if_test_atom:3, if_test_atom:i, if_test_atom:nColumns, int_literal, literal:Num, suggest_constant_definition
                lrDiagProduct = ( # assignment, assignment_lhs_identifier:lrDiagProduct, if_then_branch (-> +4)
                    grid[i][j] # assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Mult, index
                    * grid[i + 1][j + 1] # assignment_rhs_atom:1, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, index, index_arithmetic, int_literal, literal:Num
                    * grid[i + 2][j + 2] # assignment_rhs_atom:2, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num
                    * grid[i + 3][j + 3] # assignment_rhs_atom:3, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                )
            if i > 2: # comparison_operator:Gt, if (-> +5), if_test_atom:2, if_test_atom:i, int_literal, literal:Num
                rlDiagProduct = ( # assignment, assignment_lhs_identifier:rlDiagProduct, if_then_branch (-> +4)
                    grid[i][j] # assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Mult, index
                    * grid[i - 1][j + 1] # assignment_rhs_atom:1, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num
                    * grid[i - 2][j + 2] # assignment_rhs_atom:2, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num
                    * grid[i - 3][j + 3] # assignment_rhs_atom:3, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                )
            maxProduct = max(vertProduct, horzProduct, lrDiagProduct, rlDiagProduct) # assignment, assignment_lhs_identifier:maxProduct, assignment_rhs_atom:horzProduct, assignment_rhs_atom:lrDiagProduct, assignment_rhs_atom:rlDiagProduct, assignment_rhs_atom:vertProduct, call_argument:horzProduct, call_argument:lrDiagProduct, call_argument:rlDiagProduct, call_argument:vertProduct, function_call:max
            if maxProduct > largest: # comparison_operator:Gt, if (-> +1), if_test_atom:largest, if_test_atom:maxProduct
                largest = maxProduct # assignment, assignment_lhs_identifier:largest, assignment_rhs_atom:maxProduct, if_then_branch
    return largest # return:largest
def solution(): # function:solution (-> +6), function_returning_something:solution (-> +6)
    grid = [] # assignment, assignment_lhs_identifier:grid, literal:List
    with open(os.path.dirname(__file__) + "/grid.txt") as file: # binary_operator:Add, call_argument:, call_argument:__file__, composition, function_call:open, literal:Str, method_call, method_call_name:dirname
        for line in file: # for:line (-> +1), for_each (-> +1)
            grid.append(line.strip("\n").split(" ")) # call_argument:, composition, literal:Str, method_call, method_call_name:append, method_call_name:split, method_call_name:strip, method_call_object:grid, method_call_object:line, method_chaining, update_variable:grid:, update_variable:line:
    grid = [[int(i) for i in grid[j]] for j in range(len(grid))] # assignment, assignment_lhs_identifier:grid, assignment_rhs_atom:grid, assignment_rhs_atom:i, assignment_rhs_atom:j, call_argument:, call_argument:grid, call_argument:i, composition, comprehension:List, comprehension_for_count:1, function_call:int, function_call:len, function_call:range, index, range:_, update_variable:grid:i, update_variable:grid:j
    return largest_product(grid) # call_argument:grid, function_call:largest_product, function_tail_call:largest_product, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_11/sol2.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +26), function_returning_something:solution (-> +26)
    with open(os.path.dirname(__file__) + "/grid.txt") as f: # binary_operator:Add, call_argument:, call_argument:__file__, composition, function_call:open, literal:Str, method_call, method_call_name:dirname
        l = [] # assignment, assignment_lhs_identifier:l, literal:List
        for i in range(20): # call_argument:20, for:i (-> +1), for_range:20 (-> +1), function_call:range, int_literal, literal:Num, range:20, suggest_constant_definition
            l.append([int(x) for x in f.readline().split()]) # call_argument:, call_argument:x, composition, comprehension:List, comprehension_for_count:1, function_call:int, method_call, method_call_name:append, method_call_name:readline, method_call_name:split, method_call_object:f, method_call_object:l, method_chaining, update_variable:f:, update_variable:f:x, update_variable:l:, update_variable:l:x
        maximum = 0 # assignment, assignment_lhs_identifier:maximum, assignment_rhs_atom:0, int_literal, literal:Num
        for i in range(20): # call_argument:20, for:i (-> +4), for_range:17 (-> +4), for_range:20 (-> +4), function_call:range, int_literal, literal:Num, range:20, suggest_constant_definition
            for j in range(17): # call_argument:17, for:j (-> +3), for_range:17 (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), range:17, suggest_constant_definition
                temp = l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3] # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:l, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1), if_test_atom:maximum, if_test_atom:temp
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_atom:temp, if_then_branch
        for i in range(17): # call_argument:17, for:i (-> +4), for_range:17 (-> +4), for_range:20 (-> +4), function_call:range, int_literal, literal:Num, range:17, suggest_constant_definition
            for j in range(20): # call_argument:20, for:j (-> +3), for_range:20 (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), range:20, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j] # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:l, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1), if_test_atom:maximum, if_test_atom:temp
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_atom:temp, if_then_branch
        for i in range(17): # call_argument:17, for:i (-> +4), for_range:17 (-> +4), function_call:range, int_literal, literal:Num, range:17, square_nested_for (-> +4), suggest_constant_definition
            for j in range(17): # call_argument:17, for:j (-> +3), for_range:17 (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), range:17, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3] # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:l, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1), if_test_atom:maximum, if_test_atom:temp
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_atom:temp, if_then_branch
        for i in range(17): # call_argument:17, for:i (-> +4), for_range:17 (-> +4), for_range:3:20 (-> +4), function_call:range, int_literal, literal:Num, range:17, suggest_constant_definition
            for j in range(3, 20): # call_argument:20, call_argument:3, for:j (-> +3), for_range:3:20 (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), range:3:20, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3] # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:l, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1), if_test_atom:maximum, if_test_atom:temp
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_atom:temp, if_then_branch
        return maximum # return:maximum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_12/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt
def count_divisors(n): # function:count_divisors (-> +7), function_returning_something:count_divisors (-> +7)
    nDivisors = 0 # assignment, assignment_lhs_identifier:nDivisors, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(1, int(sqrt(n)) + 1): # binary_operator:Add, call_argument:, call_argument:1, call_argument:n, composition, for:i (-> +2), for_range:1:_ (-> +2), function_call:int, function_call:range, function_call:sqrt, int_literal, literal:Num, range:1:_
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:i, if_test_atom:n, int_literal, literal:Num
            nDivisors += 2 # assignment_lhs_identifier:nDivisors, assignment_rhs_atom:2, augmented_assignment:Add, if_then_branch, increment_variable:nDivisors:2, int_literal, literal:Num, update_variable:nDivisors:2
    if n ** 0.5 == int(n ** 0.5): # binary_operator:Pow, call_argument:, comparison_operator:Eq, float_literal, function_call:int, if (-> +1), if_test_atom:0.5, if_test_atom:n, literal:Num, suggest_constant_definition
        nDivisors -= 1 # assignment_lhs_identifier:nDivisors, assignment_rhs_atom:1, augmented_assignment:Sub, decrement_variable:nDivisors:1, if_then_branch, int_literal, literal:Num, update_variable:nDivisors:1
    return nDivisors # return:nDivisors
def solution(): # function:solution (-> +8), function_returning_something:solution (-> +8)
    tNum = 1 # assignment, assignment_lhs_identifier:tNum, assignment_rhs_atom:1, int_literal, literal:Num
    i = 1 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:1, int_literal, literal:Num
    while True: # infinite_while, literal:True, while (-> +4)
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
        tNum += i # assignment_lhs_identifier:tNum, assignment_rhs_atom:i, augmented_assignment:Add, increment_variable:tNum:i, update_variable:tNum:i
        if count_divisors(tNum) > 500: # call_argument:tNum, comparison_operator:Gt, function_call:count_divisors, if (-> +1), if_test_atom:500, if_test_atom:tNum, int_literal, literal:Num, suggest_constant_definition
            break # if_then_branch
    return tNum # return:tNum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_12/sol2.py
# ----------------------------------------------------------------------------------------
def triangle_number_generator(): # function:triangle_number_generator (-> +2), generator:triangle_number_generator (-> +2)
    for n in range(1, 1000000): # call_argument:1, call_argument:1000000, for:n (-> +1), for_range:1:1000000 (-> +1), function_call:range, int_literal, literal:Num, range:1:1000000, suggest_constant_definition
        yield n * (n + 1) // 2 # binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, int_literal, literal:Num, yield
def count_divisors(n): # function:count_divisors (-> +1), function_returning_something:count_divisors (-> +1)
    return sum([2 for i in range(1, int(n ** 0.5) + 1) if n % i == 0 and i * i != n]) # binary_operator:Add, binary_operator:Mod, binary_operator:Mult, binary_operator:Pow, boolean_operator:And, call_argument:, call_argument:1, comparison_operator:Eq, comparison_operator:NotEq, composition, comprehension:List, comprehension_for_count:1, divisibility_test, filtered_comprehension, float_literal, function_call:int, function_call:range, function_call:sum, function_tail_call:sum, int_literal, literal:Num, range:1:_, return, suggest_constant_definition
def solution(): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return next(i for i in triangle_number_generator() if count_divisors(i) > 500) # call_argument:, call_argument:i, comparison_operator:Gt, composition, comprehension:Generator, comprehension_for_count:1, filtered_comprehension, function_call:count_divisors, function_call:next, function_call:triangle_number_generator, function_tail_call:next, int_literal, literal:Num, return, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_13/sol1.py
# ----------------------------------------------------------------------------------------
def solution(array): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return str(sum(array))[:10] # call_argument:, call_argument:array, composition, function_call:str, function_call:sum, int_literal, literal:Num, return, slice, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_14/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +16), function_returning_something:solution (-> +16)
    largest_number = 0 # assignment, assignment_lhs_identifier:largest_number, assignment_rhs_atom:0, int_literal, literal:Num
    pre_counter = 0 # assignment, assignment_lhs_identifier:pre_counter, assignment_rhs_atom:0, int_literal, literal:Num
    for input1 in range(n): # call_argument:n, for:input1 (-> +12), for_range:n (-> +12), function_call:range, range:n
        counter = 1 # assignment, assignment_lhs_identifier:counter, assignment_rhs_atom:1, int_literal, literal:Num
        number = input1 # assignment, assignment_lhs_identifier:number, assignment_rhs_atom:input1
        while number > 1: # comparison_operator:Gt, evolve_state (-> +6), int_literal, literal:Num, while (-> +6)
            if number % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +5), if_test_atom:0, if_test_atom:2, if_test_atom:number, int_literal, literal:Num
                number /= 2 # assignment_lhs_identifier:number, assignment_rhs_atom:2, augmented_assignment:Div, if_then_branch (-> +1), int_literal, literal:Num, update_variable:number:2
                counter += 1 # assignment_lhs_identifier:counter, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:counter:1, int_literal, literal:Num, update_variable:counter:1
            else:
                number = (3 * number) + 1 # assignment, assignment_lhs_identifier:number, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:number, binary_operator:Add, binary_operator:Mult, if_else_branch (-> +1), increment_variable:number:1, increment_variable:number:3, int_literal, literal:Num, suggest_constant_definition, update_variable:number:1, update_variable:number:3
                counter += 1 # assignment_lhs_identifier:counter, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:counter:1, int_literal, literal:Num, update_variable:counter:1
        if counter > pre_counter: # comparison_operator:Gt, if (-> +2), if_test_atom:counter, if_test_atom:pre_counter
            largest_number = input1 # assignment, assignment_lhs_identifier:largest_number, assignment_rhs_atom:input1, if_then_branch (-> +1)
            pre_counter = counter # assignment, assignment_lhs_identifier:pre_counter, assignment_rhs_atom:counter
    return {"counter": pre_counter, "largest_number": largest_number} # literal:Str, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_14/sol2.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function:collatz_sequence (-> +8), function_returning_something:collatz_sequence (-> +8)
    sequence = [n] # assignment, assignment_lhs_identifier:sequence, assignment_rhs_atom:n
    while n != 1: # comparison_operator:NotEq, evolve_state (-> +5), int_literal, literal:Num, while (-> +5)
        if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:0, if_test_atom:2, if_test_atom:n, int_literal, literal:Num
            n //= 2 # assignment_lhs_identifier:n, assignment_rhs_atom:2, augmented_assignment:FloorDiv, if_then_branch, int_literal, literal:Num, update_variable:n:2
        else:
            n = 3 * n + 1 # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, if_else_branch, increment_variable:n:1, increment_variable:n:3, int_literal, literal:Num, suggest_constant_definition, update_variable:n:1, update_variable:n:3
        sequence.append(n) # call_argument:n, method_call, method_call_name:append, method_call_object:sequence, update_variable:sequence:n
    return sequence # return:sequence
def solution(n): # function:solution (-> +2), function_returning_something:solution (-> +2)
    result = max([(len(collatz_sequence(i)), i) for i in range(1, n)]) # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:n, call_argument:, call_argument:1, call_argument:i, call_argument:n, composition, comprehension:List, comprehension_for_count:1, function_call:collatz_sequence, function_call:len, function_call:max, function_call:range, int_literal, literal:Num, range:1:n
    return {"counter": result[0], "largest_number": result[1]} # index, int_literal, literal:Num, literal:Str, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_15/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial # import:math:factorial, import_module:math, import_name:factorial
def lattice_paths(n): # function:lattice_paths (-> +3), function_returning_something:lattice_paths (-> +3)
    n = 2 * n # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Mult, int_literal, literal:Num, update_variable:n:2
    k = n / 2 # assignment, assignment_lhs_identifier:k, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, int_literal, literal:Num
    return int(factorial(n) / (factorial(k) * factorial(n - k))) # binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:k, call_argument:n, composition, function_call:factorial, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_16/sol1.py
# ----------------------------------------------------------------------------------------
def solution(power): # function:solution (-> +7), function_returning_something:solution (-> +7)
    num = 2 ** power # assignment, assignment_lhs_identifier:num, assignment_rhs_atom:2, assignment_rhs_atom:power, binary_operator:Pow, int_literal, literal:Num
    string_num = str(num) # assignment, assignment_lhs_identifier:string_num, assignment_rhs_atom:num, call_argument:num, function_call:str
    list_num = list(string_num) # assignment, assignment_lhs_identifier:list_num, assignment_rhs_atom:string_num, call_argument:string_num, function_call:list
    sum_of_num = 0 # assignment, assignment_lhs_identifier:sum_of_num, assignment_rhs_atom:0, int_literal, literal:Num
    for i in list_num: # accumulate_elements:sum_of_num (-> +1), for:i (-> +1), for_each (-> +1)
        sum_of_num += int(i) # assignment_lhs_identifier:sum_of_num, assignment_rhs_atom:i, augmented_assignment:Add, call_argument:i, function_call:int, increment_variable:sum_of_num:i, update_variable:sum_of_num:i
    return sum_of_num # return:sum_of_num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_16/sol2.py
# ----------------------------------------------------------------------------------------
def solution(power): # function:solution (-> +5), function_returning_something:solution (-> +5)
    n = 2 ** power # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:power, binary_operator:Pow, int_literal, literal:Num
    r = 0 # assignment, assignment_lhs_identifier:r, assignment_rhs_atom:0, int_literal, literal:Num
    while n: # while (-> +1)
        r, n = r + n % 10, n // 10 # assignment, assignment_lhs_identifier:n, assignment_lhs_identifier:r, assignment_rhs_atom:10, assignment_rhs_atom:n, assignment_rhs_atom:r, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mod, increment_variable:n:10, increment_variable:n:r, increment_variable:r:10, increment_variable:r:n, int_literal, literal:Num, suggest_constant_definition, update_variable:n:10, update_variable:n:r, update_variable:r:10, update_variable:r:n
    return r # return:r

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_17/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +17), function_returning_something:solution (-> +17)
    ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # assignment, assignment_lhs_identifier:ones_counts, assignment_rhs_atom:0, assignment_rhs_atom:3, assignment_rhs_atom:4, assignment_rhs_atom:5, assignment_rhs_atom:6, assignment_rhs_atom:7, assignment_rhs_atom:8, assignment_rhs_atom:9, int_literal, literal:List, literal:Num, suggest_constant_definition
    tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6] # assignment, assignment_lhs_identifier:tens_counts, assignment_rhs_atom:0, assignment_rhs_atom:5, assignment_rhs_atom:6, assignment_rhs_atom:7, int_literal, literal:List, literal:Num, suggest_constant_definition
    count = 0 # assignment, assignment_lhs_identifier:count, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:count (-> +12), binary_operator:Add, call_argument:, call_argument:1, for:i (-> +12), for_range:1:_ (-> +12), function_call:range, int_literal, literal:Num, range:1:_
        if i < 1000: # comparison_operator:Lt, if (-> +11), if_test_atom:1000, if_test_atom:i, int_literal, literal:Num, suggest_constant_definition
            if i >= 100: # comparison_operator:GtE, if (-> +3), if_test_atom:100, if_test_atom:i, if_then_branch (-> +8), int_literal, literal:Num, nested_if:1 (-> +3), suggest_constant_definition
                count += ones_counts[i // 100] + 7 # assignment_lhs_identifier:count, assignment_rhs_atom:100, assignment_rhs_atom:7, assignment_rhs_atom:i, assignment_rhs_atom:ones_counts, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, if_then_branch (-> +2), increment_variable:count:100, increment_variable:count:7, increment_variable:count:i, increment_variable:count:ones_counts, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition, update_variable:count:100, update_variable:count:7, update_variable:count:i, update_variable:count:ones_counts
                if i % 100 != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test:100, if (-> +1), if_test_atom:0, if_test_atom:100, if_test_atom:i, int_literal, literal:Num, nested_if:2 (-> +1), suggest_constant_definition
                    count += 3 # assignment_lhs_identifier:count, assignment_rhs_atom:3, augmented_assignment:Add, if_then_branch, increment_variable:count:3, int_literal, literal:Num, suggest_constant_definition, update_variable:count:3
            if 0 < i % 100 < 20: # binary_operator:Mod, chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +4), if_test_atom:0, if_test_atom:100, if_test_atom:20, if_test_atom:i, int_literal, literal:Num, nested_if:1 (-> +4), suggest_constant_definition
                count += ones_counts[i % 100] # assignment_lhs_identifier:count, assignment_rhs_atom:100, assignment_rhs_atom:i, assignment_rhs_atom:ones_counts, augmented_assignment:Add, binary_operator:Mod, if_then_branch, increment_variable:count:100, increment_variable:count:i, increment_variable:count:ones_counts, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition, update_variable:count:100, update_variable:count:i, update_variable:count:ones_counts
            else:
                count += ones_counts[i % 10] # assignment_lhs_identifier:count, assignment_rhs_atom:10, assignment_rhs_atom:i, assignment_rhs_atom:ones_counts, augmented_assignment:Add, binary_operator:Mod, if_else_branch (-> +1), increment_variable:count:10, increment_variable:count:i, increment_variable:count:ones_counts, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition, update_variable:count:10, update_variable:count:i, update_variable:count:ones_counts
                count += tens_counts[(i % 100 - i % 10) // 10] # assignment_lhs_identifier:count, assignment_rhs_atom:10, assignment_rhs_atom:100, assignment_rhs_atom:i, assignment_rhs_atom:tens_counts, augmented_assignment:Add, binary_operator:FloorDiv, binary_operator:Mod, binary_operator:Sub, increment_variable:count:10, increment_variable:count:100, increment_variable:count:i, increment_variable:count:tens_counts, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition, update_variable:count:10, update_variable:count:100, update_variable:count:i, update_variable:count:tens_counts
        else:
            count += ones_counts[i // 1000] + 8 # assignment_lhs_identifier:count, assignment_rhs_atom:1000, assignment_rhs_atom:8, assignment_rhs_atom:i, assignment_rhs_atom:ones_counts, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, if_else_branch, increment_variable:count:1000, increment_variable:count:8, increment_variable:count:i, increment_variable:count:ones_counts, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition, update_variable:count:1000, update_variable:count:8, update_variable:count:i, update_variable:count:ones_counts
    return count # return:count

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_18/solution.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +17), function_returning_something:solution (-> +17)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, assignment_lhs_identifier:script_dir, assignment_rhs_atom:__file__, assignment_rhs_atom:os, call_argument:, call_argument:__file__, composition, method_call, method_call_name:dirname, method_call_name:realpath
    triangle = os.path.join(script_dir, "triangle.txt") # assignment, assignment_lhs_identifier:triangle, assignment_rhs_atom:os, assignment_rhs_atom:script_dir, call_argument:, call_argument:script_dir, literal:Str, method_call, method_call_name:join
    with open(triangle, "r") as f: # call_argument:, call_argument:triangle, function_call:open, literal:Str
        triangle = f.readlines() # assignment, assignment_lhs_identifier:triangle, assignment_rhs_atom:f, method_call, method_call_name:readlines
    a = [[int(y) for y in x.rstrip("\r\n").split(" ")] for x in triangle] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:triangle, assignment_rhs_atom:x, assignment_rhs_atom:y, call_argument:, call_argument:y, comprehension:List, comprehension_for_count:1, function_call:int, literal:Str, method_call, method_call_name:rstrip, method_call_name:split, method_call_object:x, method_chaining
    for i in range(1, len(a)): # call_argument:, call_argument:1, call_argument:a, composition, for:i (-> +10), for_range:1:_ (-> +10), for_range:_ (-> +10), function_call:len, function_call:range, int_literal, literal:Num, range:1:_
        for j in range(len(a[i])): # call_argument:, composition, for:j (-> +9), for_indexes (-> +9), for_range:_ (-> +9), function_call:len, function_call:range, index, nested_for:1 (-> +9), range:_
            if j != len(a[i - 1]): # binary_operator:Sub, call_argument:, comparison_operator:NotEq, function_call:len, if (-> +3), if_test_atom:1, if_test_atom:a, if_test_atom:i, if_test_atom:j, index, index_arithmetic, int_literal, literal:Num, suggest_conditional_expression (-> +3)
                number1 = a[i - 1][j] # assignment, assignment_lhs_identifier:number1, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
            else:
                number1 = 0 # assignment, assignment_lhs_identifier:number1, assignment_rhs_atom:0, if_else_branch, int_literal, literal:Num
            if j > 0: # comparison_operator:Gt, if (-> +3), if_test_atom:0, if_test_atom:j, int_literal, literal:Num, suggest_conditional_expression (-> +3)
                number2 = a[i - 1][j - 1] # assignment, assignment_lhs_identifier:number2, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
            else:
                number2 = 0 # assignment, assignment_lhs_identifier:number2, assignment_rhs_atom:0, if_else_branch, int_literal, literal:Num
            a[i][j] += max(number1, number2) # assignment_rhs_atom:number1, assignment_rhs_atom:number2, augmented_assignment:Add, call_argument:number1, call_argument:number2, function_call:max, index
    return max(a[-1]) # call_argument:, function_call:max, function_tail_call:max, index, int_literal, literal:Num, negative_index:-1, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_19/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +24), function_returning_something:solution (-> +24)
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # assignment, assignment_lhs_identifier:days_per_month, assignment_rhs_atom:28, assignment_rhs_atom:30, assignment_rhs_atom:31, int_literal, literal:List, literal:Num, suggest_constant_definition
    day = 6 # assignment, assignment_lhs_identifier:day, assignment_rhs_atom:6, int_literal, literal:Num, suggest_constant_definition
    month = 1 # assignment, assignment_lhs_identifier:month, assignment_rhs_atom:1, int_literal, literal:Num
    year = 1901 # assignment, assignment_lhs_identifier:year, assignment_rhs_atom:1901, int_literal, literal:Num, suggest_constant_definition
    sundays = 0 # assignment, assignment_lhs_identifier:sundays, assignment_rhs_atom:0, int_literal, literal:Num
    while year < 2001: # comparison_operator:Lt, evolve_state (-> +17), int_literal, literal:Num, suggest_constant_definition, while (-> +17)
        day += 7 # assignment_lhs_identifier:day, assignment_rhs_atom:7, augmented_assignment:Add, increment_variable:day:7, int_literal, literal:Num, suggest_constant_definition, update_variable:day:7
        if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0): # binary_operator:Mod, boolean_operator:And, boolean_operator:Or, comparison_operator:Eq, divisibility_test:100, divisibility_test:4, divisibility_test:400, if (-> +10), if_test_atom:0, if_test_atom:100, if_test_atom:4, if_test_atom:400, if_test_atom:year, int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
            if day > days_per_month[month - 1] and month != 2: # binary_operator:Sub, boolean_operator:And, comparison_operator:Gt, comparison_operator:NotEq, if (-> +5), if_test_atom:1, if_test_atom:2, if_test_atom:day, if_test_atom:days_per_month, if_test_atom:month, if_then_branch (-> +5), index, index_arithmetic, int_literal, literal:Num, nested_if:1 (-> +5)
                month += 1 # assignment_lhs_identifier:month, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch (-> +1), increment_variable:month:1, int_literal, literal:Num, update_variable:month:1
                day = day - days_per_month[month - 2] # assignment, assignment_lhs_identifier:day, assignment_rhs_atom:2, assignment_rhs_atom:day, assignment_rhs_atom:days_per_month, assignment_rhs_atom:month, binary_operator:Sub, decrement_variable:day:2, decrement_variable:day:days_per_month, decrement_variable:day:month, index, index_arithmetic, int_literal, literal:Num, suggest_augmented_assignment, update_variable:day:2, update_variable:day:days_per_month, update_variable:day:month
            elif day > 29 and month == 2: # boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, if (-> +2), if_test_atom:2, if_test_atom:29, if_test_atom:day, if_test_atom:month, int_literal, literal:Num, nested_if:1 (-> +2), suggest_constant_definition
                month += 1 # assignment_lhs_identifier:month, assignment_rhs_atom:1, augmented_assignment:Add, if_elif_branch (-> +1), increment_variable:month:1, int_literal, literal:Num, update_variable:month:1
                day = day - 29 # assignment, assignment_lhs_identifier:day, assignment_rhs_atom:29, assignment_rhs_atom:day, binary_operator:Sub, decrement_variable:day:29, int_literal, literal:Num, suggest_augmented_assignment, suggest_constant_definition, update_variable:day:29
        else:
            if day > days_per_month[month - 1]: # binary_operator:Sub, comparison_operator:Gt, if (-> +2), if_test_atom:1, if_test_atom:day, if_test_atom:days_per_month, if_test_atom:month, index, index_arithmetic, int_literal, literal:Num
                month += 1 # assignment_lhs_identifier:month, assignment_rhs_atom:1, augmented_assignment:Add, if_elif_branch (-> +1), increment_variable:month:1, int_literal, literal:Num, update_variable:month:1
                day = day - days_per_month[month - 2] # assignment, assignment_lhs_identifier:day, assignment_rhs_atom:2, assignment_rhs_atom:day, assignment_rhs_atom:days_per_month, assignment_rhs_atom:month, binary_operator:Sub, decrement_variable:day:2, decrement_variable:day:days_per_month, decrement_variable:day:month, index, index_arithmetic, int_literal, literal:Num, suggest_augmented_assignment, update_variable:day:2, update_variable:day:days_per_month, update_variable:day:month
        if month > 12: # comparison_operator:Gt, if (-> +2), if_test_atom:12, if_test_atom:month, int_literal, literal:Num, suggest_constant_definition
            year += 1 # assignment_lhs_identifier:year, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch (-> +1), increment_variable:year:1, int_literal, literal:Num, update_variable:year:1
            month = 1 # assignment, assignment_lhs_identifier:month, assignment_rhs_atom:1, int_literal, literal:Num
        if year < 2001 and day == 1: # boolean_operator:And, comparison_operator:Eq, comparison_operator:Lt, if (-> +1), if_test_atom:1, if_test_atom:2001, if_test_atom:day, if_test_atom:year, int_literal, literal:Num, suggest_constant_definition
            sundays += 1 # assignment_lhs_identifier:sundays, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment_variable:sundays:1, int_literal, literal:Num, update_variable:sundays:1
    return sundays # return:sundays

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol1.py
# ----------------------------------------------------------------------------------------
def factorial(n): # function:factorial (-> +4), function_returning_something:factorial (-> +4)
    fact = 1 # assignment, assignment_lhs_identifier:fact, assignment_rhs_atom:1, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:fact (-> +1), binary_operator:Add, call_argument:, call_argument:1, for:i (-> +1), for_range:1:_ (-> +1), function_call:range, int_literal, literal:Num, range:1:_
        fact *= i # assignment_lhs_identifier:fact, assignment_rhs_atom:i, augmented_assignment:Mult, update_variable:fact:i
    return fact # return:fact
def split_and_add(number): # function:split_and_add (-> +6), function_returning_something:split_and_add (-> +6)
    sum_of_digits = 0 # assignment, assignment_lhs_identifier:sum_of_digits, assignment_rhs_atom:0, int_literal, literal:Num
    while number > 0: # comparison_operator:Gt, evolve_state (-> +3), int_literal, literal:Num, while (-> +3)
        last_digit = number % 10 # assignment, assignment_lhs_identifier:last_digit, assignment_rhs_atom:10, assignment_rhs_atom:number, binary_operator:Mod, int_literal, literal:Num, suggest_constant_definition
        sum_of_digits += last_digit # assignment_lhs_identifier:sum_of_digits, assignment_rhs_atom:last_digit, augmented_assignment:Add, increment_variable:sum_of_digits:last_digit, update_variable:sum_of_digits:last_digit
        number = number // 10 # assignment, assignment_lhs_identifier:number, assignment_rhs_atom:10, assignment_rhs_atom:number, binary_operator:FloorDiv, int_literal, literal:Num, suggest_augmented_assignment, suggest_constant_definition, update_variable:number:10
    return sum_of_digits # return:sum_of_digits
def solution(n): # function:solution (-> +3), function_returning_something:solution (-> +3)
    f = factorial(n) # assignment, assignment_lhs_identifier:f, assignment_rhs_atom:n, call_argument:n, function_call:factorial
    result = split_and_add(f) # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:f, call_argument:f, function_call:split_and_add
    return result # return:result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol2.py
# ----------------------------------------------------------------------------------------
from math import factorial # import:math:factorial, import_module:math, import_name:factorial
def solution(n): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return sum([int(x) for x in str(factorial(n))]) # call_argument:, call_argument:n, call_argument:x, composition, comprehension:List, comprehension_for_count:1, function_call:factorial, function_call:int, function_call:str, function_call:sum, function_tail_call:sum, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol3.py
# ----------------------------------------------------------------------------------------
from math import factorial # import:math:factorial, import_module:math, import_name:factorial
def solution(n): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return sum(map(int, str(factorial(n)))) # call_argument:, call_argument:int, call_argument:n, composition, function_call:factorial, function_call:map, function_call:str, function_call:sum, function_tail_call:sum, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_something:solution (-> +7)
    fact = 1 # assignment, assignment_lhs_identifier:fact, assignment_rhs_atom:1, int_literal, literal:Num
    result = 0 # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:fact (-> +1), binary_operator:Add, call_argument:, call_argument:1, for:i (-> +1), for_range:1:_ (-> +1), function_call:range, int_literal, literal:Num, range:1:_
        fact *= i # assignment_lhs_identifier:fact, assignment_rhs_atom:i, augmented_assignment:Mult, update_variable:fact:i
    for j in str(fact): # accumulate_elements:result (-> +1), call_argument:fact, for:j (-> +1), function_call:str
        result += int(j) # assignment_lhs_identifier:result, assignment_rhs_atom:j, augmented_assignment:Add, call_argument:j, function_call:int, increment_variable:result:j, update_variable:result:j
    return result # return:result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_21/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt
def sum_of_divisors(n): # function:sum_of_divisors (-> +7), function_returning_something:sum_of_divisors (-> +7)
    total = 0 # assignment, assignment_lhs_identifier:total, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(1, int(sqrt(n) + 1)): # accumulate_elements:total (-> +4), binary_operator:Add, call_argument:, call_argument:1, call_argument:n, composition, for:i (-> +4), for_range:1:_ (-> +4), function_call:int, function_call:range, function_call:sqrt, int_literal, literal:Num, range:1:_
        if n % i == 0 and i != sqrt(n): # binary_operator:Mod, boolean_operator:And, call_argument:n, comparison_operator:Eq, comparison_operator:NotEq, divisibility_test, function_call:sqrt, if (-> +3), if_test_atom:0, if_test_atom:i, if_test_atom:n, int_literal, literal:Num
            total += i + n // i # assignment_lhs_identifier:total, assignment_rhs_atom:i, assignment_rhs_atom:n, augmented_assignment:Add, binary_operator:Add, binary_operator:FloorDiv, if_then_branch, increment_variable:total:i, increment_variable:total:n, update_variable:total:i, update_variable:total:n
        elif i == sqrt(n): # call_argument:n, comparison_operator:Eq, function_call:sqrt, if (-> +1), if_test_atom:i, if_test_atom:n
            total += i # assignment_lhs_identifier:total, assignment_rhs_atom:i, augmented_assignment:Add, if_elif_branch, increment_variable:total:i, update_variable:total:i
    return total - n # binary_operator:Sub, return
def solution(n): # function:solution (-> +8), function_returning_something:solution (-> +8)
    total = sum( # assignment, assignment_lhs_identifier:total, composition, function_call:sum
        [
            i # assignment_rhs_atom:i, call_argument:, comprehension:List, comprehension_for_count:1
            for i in range(1, n) # assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:n, call_argument:1, call_argument:n, function_call:range, int_literal, literal:Num, range:1:n
            if sum_of_divisors(sum_of_divisors(i)) == i and sum_of_divisors(i) != i # assignment_rhs_atom:i, boolean_operator:And, call_argument:, call_argument:i, comparison_operator:Eq, comparison_operator:NotEq, composition, filtered_comprehension, function_call:sum_of_divisors
        ]
    )
    return total # return:total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_22/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +12), function_returning_something:solution (-> +12)
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator:Add, call_argument:, call_argument:__file__, composition, function_call:open, literal:Str, method_call, method_call_name:dirname
        names = str(file.readlines()[0]) # assignment, assignment_lhs_identifier:names, assignment_rhs_atom:0, assignment_rhs_atom:file, call_argument:, composition, function_call:str, index, int_literal, literal:Num, method_call, method_call_name:readlines, method_call_object:file
        names = names.replace('"', "").split(",") # assignment, assignment_lhs_identifier:names, assignment_rhs_atom:names, call_argument:, literal:Str, method_call, method_call_name:replace, method_call_name:split, method_call_object:names, method_chaining
    names.sort() # method_call, method_call_name:sort, method_call_object:names
    name_score = 0 # assignment, assignment_lhs_identifier:name_score, assignment_rhs_atom:0, int_literal, literal:Num
    total_score = 0 # assignment, assignment_lhs_identifier:total_score, assignment_rhs_atom:0, int_literal, literal:Num
    for i, name in enumerate(names): # call_argument:names, for:i:name (-> +4), for_indexes_elements (-> +4), function_call:enumerate
        for letter in name: # accumulate_elements:name_score (-> +1), for:letter (-> +1), for_each (-> +1), nested_for:1 (-> +1)
            name_score += ord(letter) - 64 # assignment_lhs_identifier:name_score, assignment_rhs_atom:64, assignment_rhs_atom:letter, augmented_assignment:Add, binary_operator:Sub, call_argument:letter, function_call:ord, increment_variable:name_score:64, increment_variable:name_score:letter, int_literal, literal:Num, suggest_constant_definition, update_variable:name_score:64, update_variable:name_score:letter
        total_score += (i + 1) * name_score # assignment_lhs_identifier:total_score, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:name_score, augmented_assignment:Add, binary_operator:Add, binary_operator:Mult, increment_variable:total_score:1, increment_variable:total_score:i, increment_variable:total_score:name_score, int_literal, literal:Num, update_variable:total_score:1, update_variable:total_score:i, update_variable:total_score:name_score
        name_score = 0 # assignment, assignment_lhs_identifier:name_score, assignment_rhs_atom:0, int_literal, literal:Num
    return total_score # return:total_score

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_22/sol2.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +12), function_returning_something:solution (-> +12)
    total_sum = 0 # assignment, assignment_lhs_identifier:total_sum, assignment_rhs_atom:0, int_literal, literal:Num
    temp_sum = 0 # assignment, assignment_lhs_identifier:temp_sum, assignment_rhs_atom:0, int_literal, literal:Num
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator:Add, call_argument:, call_argument:__file__, composition, function_call:open, literal:Str, method_call, method_call_name:dirname
        name = str(file.readlines()[0]) # assignment, assignment_lhs_identifier:name, assignment_rhs_atom:0, assignment_rhs_atom:file, call_argument:, composition, function_call:str, index, int_literal, literal:Num, method_call, method_call_name:readlines, method_call_object:file
        name = name.replace('"', "").split(",") # assignment, assignment_lhs_identifier:name, assignment_rhs_atom:name, call_argument:, literal:Str, method_call, method_call_name:replace, method_call_name:split, method_call_object:name, method_chaining
    name.sort() # method_call, method_call_name:sort, method_call_object:name
    for i in range(len(name)): # accumulate_elements:total_sum (-> +4), call_argument:, call_argument:name, composition, for:i (-> +4), for_indexes (-> +4), for_range:_ (-> +4), function_call:len, function_call:range, range:_
        for j in name[i]: # accumulate_elements:temp_sum (-> +1), for:j (-> +1), index, nested_for:1 (-> +1)
            temp_sum += ord(j) - ord("A") + 1 # assignment_lhs_identifier:temp_sum, assignment_rhs_atom:1, assignment_rhs_atom:j, augmented_assignment:Add, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:j, function_call:ord, increment_variable:temp_sum:1, increment_variable:temp_sum:j, int_literal, literal:Num, literal:Str, update_variable:temp_sum:1, update_variable:temp_sum:j
        total_sum += (i + 1) * temp_sum # assignment_lhs_identifier:total_sum, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:temp_sum, augmented_assignment:Add, binary_operator:Add, binary_operator:Mult, increment_variable:total_sum:1, increment_variable:total_sum:i, increment_variable:total_sum:temp_sum, int_literal, literal:Num, update_variable:total_sum:1, update_variable:total_sum:i, update_variable:total_sum:temp_sum
        temp_sum = 0 # assignment, assignment_lhs_identifier:temp_sum, assignment_rhs_atom:0, int_literal, literal:Num
    return total_sum # return:total_sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_23/sol1.py
# ----------------------------------------------------------------------------------------
def solution(limit=28123): # function:solution (-> +13), function_returning_something:solution (-> +13), function_with_default_positional_arguments:solution (-> +13), int_literal, literal:Num
    sumDivs = [1] * (limit + 1) # assignment, assignment_lhs_identifier:sumDivs, assignment_rhs_atom:1, assignment_rhs_atom:limit, binary_operator:Add, binary_operator:Mult, int_literal, literal:List, literal:Num
    for i in range(2, int(limit ** 0.5) + 1): # accumulate_elements:sumDivs (-> +3), binary_operator:Add, binary_operator:Pow, call_argument:, call_argument:2, composition, float_literal, for:i (-> +3), for_range:2:_ (-> +3), for_range:_:_ (-> +3), function_call:int, function_call:range, int_literal, literal:Num, range:2:_, suggest_constant_definition
        sumDivs[i * i] += i # assignment_lhs_identifier:sumDivs, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Mult, increment_variable:sumDivs:i, index, index_arithmetic, update_variable:sumDivs:i
        for k in range(i + 1, limit // i + 1): # accumulate_elements:sumDivs (-> +1), binary_operator:Add, binary_operator:FloorDiv, call_argument:, for:k (-> +1), for_range:_:_ (-> +1), function_call:range, int_literal, literal:Num, nested_for:1 (-> +1), range:_:_
            sumDivs[k * i] += k + i # assignment_lhs_identifier:sumDivs, assignment_rhs_atom:i, assignment_rhs_atom:k, augmented_assignment:Add, binary_operator:Add, binary_operator:Mult, increment_variable:sumDivs:i, increment_variable:sumDivs:k, index, index_arithmetic, update_variable:sumDivs:i, update_variable:sumDivs:k
    abundants = set() # assignment, assignment_lhs_identifier:abundants, function_call:set
    res = 0 # assignment, assignment_lhs_identifier:res, assignment_rhs_atom:0, int_literal, literal:Num
    for n in range(1, limit + 1): # accumulate_elements:abundants (-> +4), accumulate_elements:res (-> +4), binary_operator:Add, call_argument:, call_argument:1, for:n (-> +4), for_range:1:_ (-> +4), function_call:range, int_literal, literal:Num, range:1:_
        if sumDivs[n] > n: # comparison_operator:Gt, if (-> +1), if_test_atom:n, if_test_atom:sumDivs, index
            abundants.add(n) # call_argument:n, if_then_branch, method_call, method_call_name:add, method_call_object:abundants, update_variable:abundants:n
        if not any((n - a in abundants) for a in abundants): # binary_operator:Sub, call_argument:, comparison_operator:In, comprehension:Generator, comprehension_for_count:1, function_call:any, if (-> +1), if_test_atom:a, if_test_atom:abundants, if_test_atom:n, unary_operator:Not
            res += n # assignment_lhs_identifier:res, assignment_rhs_atom:n, augmented_assignment:Add, if_then_branch, increment_variable:res:n, update_variable:res:n
    return res # return:res

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_234/sol1.py
# ----------------------------------------------------------------------------------------
def fib(a, b, n): # function:fib (-> +13), function_returning_something:fib (-> +13)
    if n == 1: # comparison_operator:Eq, if (-> +5), if_test_atom:1, if_test_atom:n, int_literal, literal:Num
        return a # if_then_branch, return:a
    elif n == 2: # comparison_operator:Eq, if (-> +3), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        return b # if_elif_branch, return:b
    elif n == 3: # comparison_operator:Eq, if (-> +1), if_test_atom:3, if_test_atom:n, int_literal, literal:Num, suggest_constant_definition
        return str(a) + str(b) # binary_operator:Add, call_argument:a, call_argument:b, function_call:str, if_elif_branch, return
    temp = 0 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:0, int_literal, literal:Num
    for x in range(2, n): # call_argument:2, call_argument:n, for:x (-> +4), for_range:2:n (-> +4), function_call:range, int_literal, literal:Num, range:2:n
        c = str(a) + str(b) # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, call_argument:a, call_argument:b, function_call:str
        temp = b # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:b
        b = c # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:c
        a = temp # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:temp
    return c # return:c
def solution(n): # function:solution (-> +11), function_returning_something:solution (-> +11)
    semidivisible = [] # assignment, assignment_lhs_identifier:semidivisible, literal:List
    for x in range(n): # call_argument:n, for:x (-> +8), for_range:n (-> +8), function_call:range, range:n
        l = [i for i in input().split()] # assignment, assignment_lhs_identifier:l, assignment_rhs_atom:i, comprehension:List, comprehension_for_count:1, function_call:input, method_call, method_call_name:split
        c2 = 1 # assignment, assignment_lhs_identifier:c2, assignment_rhs_atom:1, int_literal, literal:Num
        while 1: # int_literal, literal:Num, while (-> +4)
            if len(fib(l[0], l[1], c2)) < int(l[2]): # call_argument:, call_argument:c2, comparison_operator:Lt, composition, function_call:fib, function_call:int, function_call:len, if (-> +3), if_test_atom:0, if_test_atom:1, if_test_atom:2, if_test_atom:c2, if_test_atom:l, index, int_literal, literal:Num
                c2 += 1 # assignment_lhs_identifier:c2, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment_variable:c2:1, int_literal, literal:Num, update_variable:c2:1
            else:
                break # if_else_branch
        semidivisible.append(fib(l[0], l[1], c2 + 1)[int(l[2]) - 1]) # binary_operator:Add, binary_operator:Sub, call_argument:, composition, function_call:fib, function_call:int, index, index_arithmetic, int_literal, literal:Num, method_call, method_call_name:append, method_call_object:semidivisible, update_variable:semidivisible:
    return semidivisible # return:semidivisible

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_24/sol1.py
# ----------------------------------------------------------------------------------------
from itertools import permutations # import:itertools:permutations, import_module:itertools, import_name:permutations
def solution(): # function:solution (-> +2), function_returning_something:solution (-> +2)
    result = list(map("".join, permutations("0123456789"))) # assignment, assignment_lhs_identifier:result, call_argument:, composition, function_call:list, function_call:map, function_call:permutations, literal:Str
    return result[999999] # index, int_literal, literal:Num, return, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol1.py
# ----------------------------------------------------------------------------------------
def fibonacci(n): # function:fibonacci (-> +9), function_returning_something:fibonacci (-> +9)
    if n == 1 or type(n) is not int: # boolean_operator:Or, call_argument:n, comparison_operator:Eq, comparison_operator:IsNot, function_call:type, if (-> +8), if_test_atom:1, if_test_atom:int, if_test_atom:n, int_literal, literal:Num
        return 0 # if_then_branch, int_literal, literal:Num, return:0
    elif n == 2: # comparison_operator:Eq, if (-> +6), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        return 1 # if_elif_branch, int_literal, literal:Num, return:1
    else:
        sequence = [0, 1] # assignment, assignment_lhs_identifier:sequence, assignment_rhs_atom:0, assignment_rhs_atom:1, if_else_branch (-> +3), int_literal, literal:List, literal:Num
        for i in range(2, n + 1): # binary_operator:Add, call_argument:, call_argument:2, for:i (-> +1), for_range:2:_ (-> +1), function_call:range, int_literal, literal:Num, range:2:_
            sequence.append(sequence[i - 1] + sequence[i - 2]) # binary_operator:Add, binary_operator:Sub, call_argument:, index, index_arithmetic, int_literal, literal:Num, method_call, method_call_name:append, method_call_object:sequence, update_variable:sequence:
        return sequence[n] # index, return
def fibonacci_digits_index(n): # function:fibonacci_digits_index (-> +6), function_returning_something:fibonacci_digits_index (-> +6)
    digits = 0 # assignment, assignment_lhs_identifier:digits, assignment_rhs_atom:0, int_literal, literal:Num
    index = 2 # assignment, assignment_lhs_identifier:index, assignment_rhs_atom:2, int_literal, literal:Num
    while digits < n: # comparison_operator:Lt, while (-> +2)
        index += 1 # assignment_lhs_identifier:index, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:index:1, int_literal, literal:Num, update_variable:index:1
        digits = len(str(fibonacci(index))) # assignment, assignment_lhs_identifier:digits, assignment_rhs_atom:index, call_argument:, call_argument:index, composition, function_call:fibonacci, function_call:len, function_call:str
    return index # return:index
def solution(n): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return fibonacci_digits_index(n) # call_argument:n, function_call:fibonacci_digits_index, function_tail_call:fibonacci_digits_index, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol2.py
# ----------------------------------------------------------------------------------------
def fibonacci_generator(): # function:fibonacci_generator (-> +4), generator:fibonacci_generator (-> +4)
    a, b = 0, 1 # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:0, assignment_rhs_atom:1, int_literal, literal:Num, literal:Tuple
    while True: # infinite_while, literal:True, while (-> +2)
        a, b = b, a + b # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, increment_variable:a:b, increment_variable:b:a, update_variable:a:b, update_variable:b:a
        yield b # yield:b
def solution(n): # function:solution (-> +5), function_returning_something:solution (-> +5)
    answer = 1 # assignment, assignment_lhs_identifier:answer, assignment_rhs_atom:1, int_literal, literal:Num
    gen = fibonacci_generator() # assignment, assignment_lhs_identifier:gen, function_call:fibonacci_generator
    while len(str(next(gen))) < n: # call_argument:, call_argument:gen, comparison_operator:Lt, composition, function_call:len, function_call:next, function_call:str, while (-> +1)
        answer += 1 # assignment_lhs_identifier:answer, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:answer:1, int_literal, literal:Num, update_variable:answer:1
    return answer + 1 # binary_operator:Add, int_literal, literal:Num, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +12), function_returning_something:solution (-> +12)
    f1, f2 = 1, 1 # assignment, assignment_lhs_identifier:f1, assignment_lhs_identifier:f2, assignment_rhs_atom:1, int_literal, literal:Num, literal:Tuple
    index = 2 # assignment, assignment_lhs_identifier:index, assignment_rhs_atom:2, int_literal, literal:Num
    while True: # infinite_while, literal:True, while (-> +8)
        i = 0 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:0, int_literal, literal:Num
        f = f1 + f2 # assignment, assignment_lhs_identifier:f, assignment_rhs_atom:f1, assignment_rhs_atom:f2, binary_operator:Add
        f1, f2 = f2, f # assignment, assignment_lhs_identifier:f1, assignment_lhs_identifier:f2, assignment_rhs_atom:f, assignment_rhs_atom:f2, update_variable:f2:f
        index += 1 # assignment_lhs_identifier:index, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:index:1, int_literal, literal:Num, update_variable:index:1
        for j in str(f): # call_argument:f, for:j (-> +1), function_call:str
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
        if i == n: # comparison_operator:Eq, if (-> +1), if_test_atom:i, if_test_atom:n
            break # if_then_branch
    return index # return:index

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_27/problem_27_sol1.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math
def is_prime(k: int) -> bool: # function:is_prime (-> +9), function_returning_something:is_prime (-> +9)
    if k < 2 or k % 2 == 0: # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, comparison_operator:Lt, divisibility_test:2, if (-> +7), if_test_atom:0, if_test_atom:2, if_test_atom:k, int_literal, literal:Num
        return False # if_then_branch, literal:False, return:False
    elif k == 2: # comparison_operator:Eq, if (-> +5), if_test_atom:2, if_test_atom:k, int_literal, literal:Num
        return True # if_elif_branch, literal:True, return:True
    else:
        for x in range(3, int(math.sqrt(k) + 1), 2): # binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:k, composition, for:x (-> +2), for_range:3:_:2 (-> +2), function_call:int, function_call:range, if_else_branch (-> +2), int_literal, literal:Num, method_call, method_call_name:sqrt, range:3:_:2, suggest_constant_definition
            if k % x == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), if_test_atom:0, if_test_atom:k, if_test_atom:x, int_literal, literal:Num, nested_if:1 (-> +1)
                return False # if_then_branch, literal:False, return:False
    return True # literal:True, return:True
def solution(a_limit: int, b_limit: int) -> int: # function:solution (-> +13), function_returning_something:solution (-> +13)
    longest = [0, 0, 0] # assignment, assignment_lhs_identifier:longest, assignment_rhs_atom:0, int_literal, literal:List, literal:Num
    for a in range((a_limit * -1) + 1, a_limit): # binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:a_limit, for:a (-> +9), for_range:2:b_limit (-> +9), for_range:_:a_limit (-> +9), function_call:range, int_literal, literal:Num, range:_:a_limit
        for b in range(2, b_limit): # call_argument:2, call_argument:b_limit, for:b (-> +8), for_range:2:b_limit (-> +8), function_call:range, int_literal, literal:Num, nested_for:1 (-> +8), range:2:b_limit
            if is_prime(b): # call_argument:b, function_call:is_prime, if (-> +7), if_test_atom:b
                count = 0 # assignment, assignment_lhs_identifier:count, assignment_rhs_atom:0, if_then_branch (-> +6), int_literal, literal:Num
                n = 0 # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:0, int_literal, literal:Num
                while is_prime((n ** 2) + (a * n) + b): # binary_operator:Add, binary_operator:Mult, binary_operator:Pow, call_argument:, function_call:is_prime, int_literal, literal:Num, while (-> +2)
                    count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:count:1, int_literal, literal:Num, update_variable:count:1
                    n += 1 # assignment_lhs_identifier:n, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:n:1, int_literal, literal:Num, update_variable:n:1
                if count > longest[0]: # comparison_operator:Gt, if (-> +1), if_test_atom:0, if_test_atom:count, if_test_atom:longest, index, int_literal, literal:Num, nested_if:1 (-> +1)
                    longest = [count, a, b] # assignment, assignment_lhs_identifier:longest, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:count, if_then_branch
    ans = longest[1] * longest[2] # assignment, assignment_lhs_identifier:ans, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:longest, binary_operator:Mult, index, int_literal, literal:Num
    return ans # return:ans

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_28/sol1.py
# ----------------------------------------------------------------------------------------
from math import ceil # import:math:ceil, import_module:math, import_name:ceil
def diagonal_sum(n): # function:diagonal_sum (-> +6), function_returning_something:diagonal_sum (-> +6)
    total = 1 # assignment, assignment_lhs_identifier:total, assignment_rhs_atom:1, int_literal, literal:Num
    for i in range(1, int(ceil(n / 2.0))): # binary_operator:Div, call_argument:, call_argument:1, composition, float_literal, for:i (-> +3), for_range:1:_ (-> +3), function_call:ceil, function_call:int, function_call:range, int_literal, literal:Num, range:1:_, suggest_constant_definition
        odd = 2 * i + 1 # assignment, assignment_lhs_identifier:odd, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:i, binary_operator:Add, binary_operator:Mult, int_literal, literal:Num
        even = 2 * i # assignment, assignment_lhs_identifier:even, assignment_rhs_atom:2, assignment_rhs_atom:i, binary_operator:Mult, int_literal, literal:Num
        total = total + 4 * odd ** 2 - 6 * even # assignment, assignment_lhs_identifier:total, assignment_rhs_atom:2, assignment_rhs_atom:4, assignment_rhs_atom:6, assignment_rhs_atom:even, assignment_rhs_atom:odd, assignment_rhs_atom:total, binary_operator:Add, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, increment_variable:total:2, increment_variable:total:4, increment_variable:total:6, increment_variable:total:even, increment_variable:total:odd, int_literal, literal:Num, suggest_constant_definition, update_variable:total:2, update_variable:total:4, update_variable:total:6, update_variable:total:even, update_variable:total:odd
    return total # return:total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_29/solution.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_returning_something:solution (-> +8)
    collectPowers = set() # assignment, assignment_lhs_identifier:collectPowers, function_call:set
    currentPow = 0 # assignment, assignment_lhs_identifier:currentPow, assignment_rhs_atom:0, int_literal, literal:Num
    N = n + 1 # assignment, assignment_lhs_identifier:N, assignment_rhs_atom:1, assignment_rhs_atom:n, binary_operator:Add, int_literal, literal:Num
    for a in range(2, N): # call_argument:2, call_argument:N, for:a (-> +3), for_range:2:N (-> +3), function_call:range, int_literal, literal:Num, range:2:N, square_nested_for (-> +3)
        for b in range(2, N): # call_argument:2, call_argument:N, for:b (-> +2), for_range:2:N (-> +2), function_call:range, int_literal, literal:Num, nested_for:1 (-> +2), range:2:N
            currentPow = a ** b # assignment, assignment_lhs_identifier:currentPow, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Pow
            collectPowers.add(currentPow) # call_argument:currentPow, method_call, method_call_name:add, method_call_object:collectPowers, update_variable:collectPowers:currentPow
    return len(collectPowers) # call_argument:collectPowers, function_call:len, function_tail_call:len, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_31/sol1.py
# ----------------------------------------------------------------------------------------
def one_pence(): # function:one_pence (-> +1), function_returning_something:one_pence (-> +1)
    return 1 # int_literal, literal:Num, return:1
def two_pence(x): # body_recursive_function:two_pence (-> +1), function:two_pence (-> +1), function_returning_something:two_pence (-> +1), recursive_function:two_pence (-> +1)
    return 0 if x < 0 else two_pence(x - 2) + one_pence() # binary_operator:Add, binary_operator:Sub, call_argument:, comparison_operator:Lt, conditional_expression, function_call:one_pence, function_call:two_pence, int_literal, literal:Num, return
def five_pence(x): # body_recursive_function:five_pence (-> +1), function:five_pence (-> +1), function_returning_something:five_pence (-> +1), recursive_function:five_pence (-> +1)
    return 0 if x < 0 else five_pence(x - 5) + two_pence(x) # binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:five_pence, function_call:two_pence, int_literal, literal:Num, return, suggest_constant_definition
def ten_pence(x): # body_recursive_function:ten_pence (-> +1), function:ten_pence (-> +1), function_returning_something:ten_pence (-> +1), recursive_function:ten_pence (-> +1)
    return 0 if x < 0 else ten_pence(x - 10) + five_pence(x) # binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:five_pence, function_call:ten_pence, int_literal, literal:Num, return, suggest_constant_definition
def twenty_pence(x): # body_recursive_function:twenty_pence (-> +1), function:twenty_pence (-> +1), function_returning_something:twenty_pence (-> +1), recursive_function:twenty_pence (-> +1)
    return 0 if x < 0 else twenty_pence(x - 20) + ten_pence(x) # binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:ten_pence, function_call:twenty_pence, int_literal, literal:Num, return, suggest_constant_definition
def fifty_pence(x): # body_recursive_function:fifty_pence (-> +1), function:fifty_pence (-> +1), function_returning_something:fifty_pence (-> +1), recursive_function:fifty_pence (-> +1)
    return 0 if x < 0 else fifty_pence(x - 50) + twenty_pence(x) # binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:fifty_pence, function_call:twenty_pence, int_literal, literal:Num, return, suggest_constant_definition
def one_pound(x): # body_recursive_function:one_pound (-> +1), function:one_pound (-> +1), function_returning_something:one_pound (-> +1), recursive_function:one_pound (-> +1)
    return 0 if x < 0 else one_pound(x - 100) + fifty_pence(x) # binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:fifty_pence, function_call:one_pound, int_literal, literal:Num, return, suggest_constant_definition
def two_pound(x): # body_recursive_function:two_pound (-> +1), function:two_pound (-> +1), function_returning_something:two_pound (-> +1), recursive_function:two_pound (-> +1)
    return 0 if x < 0 else two_pound(x - 200) + one_pound(x) # binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:x, comparison_operator:Lt, conditional_expression, function_call:one_pound, function_call:two_pound, int_literal, literal:Num, return, suggest_constant_definition
def solution(n): # function:solution (-> +1), function_returning_something:solution (-> +1)
    return two_pound(n) # call_argument:n, function_call:two_pound, function_tail_call:two_pound, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_32/sol32.py
# ----------------------------------------------------------------------------------------
import itertools # import:itertools, import_module:itertools
def isCombinationValid(combination): # function:isCombinationValid (-> +6), function_returning_something:isCombinationValid (-> +6)
    return ( # boolean_operator:Or, return
        int("".join(combination[0:2])) * int("".join(combination[2:5])) # binary_operator:Mult, call_argument:, composition, function_call:int, int_literal, literal:Num, literal:Str, method_call, method_call_name:join, slice, suggest_constant_definition
        == int("".join(combination[5:9])) # call_argument:, comparison_operator:Eq, composition, function_call:int, int_literal, literal:Num, literal:Str, method_call, method_call_name:join, slice, suggest_constant_definition
    ) or (
        int("".join(combination[0])) * int("".join(combination[1:5])) # binary_operator:Mult, call_argument:, composition, function_call:int, index, int_literal, literal:Num, literal:Str, method_call, method_call_name:join, slice, suggest_constant_definition
        == int("".join(combination[5:9])) # call_argument:, comparison_operator:Eq, composition, function_call:int, int_literal, literal:Num, literal:Str, method_call, method_call_name:join, slice, suggest_constant_definition
    )
def solution(): # function:solution (-> +6), function_returning_something:solution (-> +6)
    return sum( # composition, function_call:sum, function_tail_call:sum, return
        set( # call_argument:, composition, function_call:set
            [
                int("".join(pandigital[5:9])) # call_argument:, composition, comprehension:List, comprehension_for_count:1, function_call:int, int_literal, literal:Num, literal:Str, method_call, method_call_name:join, slice, suggest_constant_definition
                for pandigital in itertools.permutations("123456789") # call_argument:, literal:Str, method_call, method_call_name:permutations
                if isCombinationValid(pandigital) # call_argument:pandigital, filtered_comprehension, function_call:isCombinationValid
            ]
        )
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_33/sol1.py
# ----------------------------------------------------------------------------------------
def isDigitCancelling(num, den): # function:isDigitCancelling (-> +4), function_returning_something:isDigitCancelling (-> +4)
    if num != den: # comparison_operator:NotEq, if (-> +3), if_test_atom:den, if_test_atom:num
        if num % 10 == den // 10: # binary_operator:FloorDiv, binary_operator:Mod, comparison_operator:Eq, divisibility_test:10, if (-> +2), if_test_atom:10, if_test_atom:den, if_test_atom:num, if_then_branch (-> +2), int_literal, literal:Num, nested_if:1 (-> +2), suggest_constant_definition
            if (num // 10) / (den % 10) == num / den: # binary_operator:Div, binary_operator:FloorDiv, binary_operator:Mod, comparison_operator:Eq, if (-> +1), if_test_atom:10, if_test_atom:den, if_test_atom:num, if_then_branch (-> +1), int_literal, literal:Num, nested_if:2 (-> +1), suggest_constant_definition
                return True # if_then_branch, literal:True, return:True
def solve(digit_len: int) -> str: # function:solve (-> +13), function_returning_something:solve (-> +13)
    solutions = [] # assignment, assignment_lhs_identifier:solutions, literal:List
    den = 11 # assignment, assignment_lhs_identifier:den, assignment_rhs_atom:11, int_literal, literal:Num, suggest_constant_definition
    last_digit = int("1" + "0" * digit_len) # assignment, assignment_lhs_identifier:last_digit, assignment_rhs_atom:digit_len, binary_operator:Add, binary_operator:Mult, call_argument:, function_call:int, literal:Str
    for num in range(den, last_digit): # accumulate_elements:solutions (-> +7), call_argument:den, call_argument:last_digit, for:num (-> +7), for_range:den:last_digit (-> +7), function_call:range, range:den:last_digit
        while den <= 99: # comparison_operator:LtE, evolve_state (-> +4), int_literal, literal:Num, suggest_constant_definition, while (-> +4)
            if (num != den) and (num % 10 == den // 10) and (den % 10 != 0): # binary_operator:FloorDiv, binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:NotEq, divisibility_test:10, if (-> +2), if_test_atom:0, if_test_atom:10, if_test_atom:den, if_test_atom:num, int_literal, literal:Num, suggest_constant_definition
                if isDigitCancelling(num, den): # call_argument:den, call_argument:num, function_call:isDigitCancelling, if (-> +1), if_test_atom:den, if_test_atom:num, if_then_branch (-> +1), nested_if:1 (-> +1)
                    solutions.append("{}/{}".format(num, den)) # call_argument:, call_argument:den, call_argument:num, composition, if_then_branch, literal:Str, method_call, method_call_name:append, method_call_name:format, method_call_object:solutions, update_variable:solutions:, update_variable:solutions:den, update_variable:solutions:num
            den += 1 # assignment_lhs_identifier:den, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:den:1, int_literal, literal:Num, update_variable:den:1
        num += 1 # assignment_lhs_identifier:num, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:num:1, int_literal, literal:Num, update_variable:num:1
        den = 10 # assignment, assignment_lhs_identifier:den, assignment_rhs_atom:10, int_literal, literal:Num, suggest_constant_definition
    solutions = " , ".join(solutions) # assignment, assignment_lhs_identifier:solutions, assignment_rhs_atom:solutions, call_argument:solutions, literal:Str, method_call, method_call_name:join
    return solutions # return:solutions

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_36/sol1.py
# ----------------------------------------------------------------------------------------
def is_palindrome(n): # function:is_palindrome (-> +5), function_returning_something:is_palindrome (-> +5)
    n = str(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:str
    if n == n[::-1]: # comparison_operator:Eq, if (-> +3), if_test_atom:-1, if_test_atom:n, int_literal, literal:Num, slice_step, suggest_condition_return (-> +3)
        return True # if_then_branch, literal:True, return:True
    else:
        return False # if_else_branch, literal:False, return:False
def solution(n): # function:solution (-> +5), function_returning_something:solution (-> +5)
    total = 0 # assignment, assignment_lhs_identifier:total, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(1, n): # accumulate_elements:total (-> +2), call_argument:1, call_argument:n, for:i (-> +2), for_range:1:n (-> +2), function_call:range, int_literal, literal:Num, range:1:n
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]): # boolean_operator:And, call_argument:, call_argument:i, composition, function_call:bin, function_call:is_palindrome, if (-> +1), if_test_atom:1, if_test_atom:i, index, int_literal, literal:Num, literal:Str, method_call, method_call_name:split
            total += i # assignment_lhs_identifier:total, assignment_rhs_atom:i, augmented_assignment:Add, if_then_branch, increment_variable:total:i, update_variable:total:i
    return total # return:total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_40/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +14), function_returning_something:solution (-> +14)
    constant = [] # assignment, assignment_lhs_identifier:constant, literal:List
    i = 1 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:1, int_literal, literal:Num
    while len(constant) < 1e6: # call_argument:constant, comparison_operator:Lt, evolve_state (-> +2), float_literal, function_call:len, literal:Num, suggest_constant_definition, while (-> +2)
        constant.append(str(i)) # call_argument:, call_argument:i, composition, function_call:str, method_call, method_call_name:append, method_call_object:constant, update_variable:constant:, update_variable:constant:i
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
    constant = "".join(constant) # assignment, assignment_lhs_identifier:constant, assignment_rhs_atom:constant, call_argument:constant, literal:Str, method_call, method_call_name:join
    return ( # return
        int(constant[0]) # binary_operator:Mult, call_argument:, function_call:int, index, int_literal, literal:Num
        * int(constant[9]) # call_argument:, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[99]) # binary_operator:Mult, call_argument:, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[999]) # binary_operator:Mult, call_argument:, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[9999]) # binary_operator:Mult, call_argument:, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[99999]) # binary_operator:Mult, call_argument:, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[999999]) # binary_operator:Mult, call_argument:, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_42/solution42.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
TRIANGULAR_NUMBERS = [int(0.5 * n * (n + 1)) for n in range(1, 101)] # assignment, assignment_lhs_identifier:TRIANGULAR_NUMBERS, assignment_rhs_atom:0.5, assignment_rhs_atom:1, assignment_rhs_atom:101, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:1, call_argument:101, comprehension:List, comprehension_for_count:1, float_literal, function_call:int, function_call:range, int_literal, literal:Num, range:1:101
def solution(): # function:solution (-> +13), function_returning_something:solution (-> +13)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, assignment_lhs_identifier:script_dir, assignment_rhs_atom:__file__, assignment_rhs_atom:os, call_argument:, call_argument:__file__, composition, method_call, method_call_name:dirname, method_call_name:realpath
    wordsFilePath = os.path.join(script_dir, "words.txt") # assignment, assignment_lhs_identifier:wordsFilePath, assignment_rhs_atom:os, assignment_rhs_atom:script_dir, call_argument:, call_argument:script_dir, literal:Str, method_call, method_call_name:join
    words = "" # assignment, assignment_lhs_identifier:words, literal:Str
    with open(wordsFilePath, "r") as f: # call_argument:, call_argument:wordsFilePath, function_call:open, literal:Str
        words = f.readline() # assignment, assignment_lhs_identifier:words, assignment_rhs_atom:f, method_call, method_call_name:readline
    words = list(map(lambda word: word.strip('"'), words.strip("\r\n").split(","))) # assignment, assignment_lhs_identifier:words, assignment_rhs_atom:word, assignment_rhs_atom:words, call_argument:, composition, function_call:list, function_call:map, lambda_function, literal:Str, method_call, method_call_name:split, method_call_name:strip, method_call_object:words, method_chaining, update_variable:words:word
    words = list( # assignment, assignment_lhs_identifier:words, composition, decrement_variable:words:64, decrement_variable:words:TRIANGULAR_NUMBERS, decrement_variable:words:word, decrement_variable:words:x, function_call:list, update_variable:words:64, update_variable:words:TRIANGULAR_NUMBERS, update_variable:words:word, update_variable:words:x
        filter( # call_argument:, composition, function_call:filter
            lambda word: word in TRIANGULAR_NUMBERS, # assignment_rhs_atom:TRIANGULAR_NUMBERS, assignment_rhs_atom:word, call_argument:, comparison_operator:In, lambda_function
            map(lambda word: sum(map(lambda x: ord(x) - 64, word)), words), # assignment_rhs_atom:64, assignment_rhs_atom:word, assignment_rhs_atom:words, assignment_rhs_atom:x, binary_operator:Sub, call_argument:, call_argument:word, call_argument:words, call_argument:x, composition, function_call:map, function_call:ord, function_call:sum, int_literal, lambda_function, literal:Num, suggest_constant_definition
        )
    )
    return len(words) # call_argument:words, function_call:len, function_tail_call:len, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_48/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +4), function_returning_something:solution (-> +4)
    total = 0 # assignment, assignment_lhs_identifier:total, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(1, 1001): # accumulate_elements:total (-> +1), call_argument:1, call_argument:1001, for:i (-> +1), for_range:1:1001 (-> +1), function_call:range, int_literal, literal:Num, range:1:1001, suggest_constant_definition
        total += i ** i # assignment_lhs_identifier:total, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Pow, increment_variable:total:i, update_variable:total:i
    return str(total)[-10:] # call_argument:total, function_call:str, int_literal, literal:Num, return, slice, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_52/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +12), function_returning_something:solution (-> +12)
    i = 1 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:1, int_literal, literal:Num
    while True: # infinite_while, literal:True, while (-> +10)
        if ( # if (-> +8)
            sorted(list(str(i))) # call_argument:, call_argument:i, chained_comparison:5, chained_equalities:5, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:i
            == sorted(list(str(2 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:2, if_test_atom:i, int_literal, literal:Num
            == sorted(list(str(3 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:3, if_test_atom:i, int_literal, literal:Num, suggest_constant_definition
            == sorted(list(str(4 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:4, if_test_atom:i, int_literal, literal:Num, suggest_constant_definition
            == sorted(list(str(5 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:5, if_test_atom:i, int_literal, literal:Num, suggest_constant_definition
            == sorted(list(str(6 * i))) # binary_operator:Mult, call_argument:, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, if_test_atom:6, if_test_atom:i, int_literal, literal:Num, suggest_constant_definition
        ):
            return i # if_then_branch, return:i
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_53/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial # import:math:factorial, import_module:math, import_name:factorial
def combinations(n, r): # function:combinations (-> +1), function_returning_something:combinations (-> +1)
    return factorial(n) / (factorial(r) * factorial(n - r)) # binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:n, call_argument:r, function_call:factorial, return
def solution(): # function:solution (-> +6), function_returning_something:solution (-> +6)
    total = 0 # assignment, assignment_lhs_identifier:total, assignment_rhs_atom:0, int_literal, literal:Num
    for i in range(1, 101): # call_argument:1, call_argument:101, for:i (-> +3), for_range:1:101 (-> +3), for_range:1:_ (-> +3), function_call:range, int_literal, literal:Num, range:1:101, suggest_constant_definition
        for j in range(1, i + 1): # binary_operator:Add, call_argument:, call_argument:1, for:j (-> +2), for_range:1:_ (-> +2), function_call:range, int_literal, literal:Num, nested_for:1 (-> +2), range:1:_
            if combinations(i, j) > 1e6: # call_argument:i, call_argument:j, comparison_operator:Gt, float_literal, function_call:combinations, if (-> +1), if_test_atom:1000000.0, if_test_atom:i, if_test_atom:j, literal:Num, suggest_constant_definition
                total += 1 # assignment_lhs_identifier:total, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment_variable:total:1, int_literal, literal:Num, update_variable:total:1
    return total # return:total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_551/sol1.py
# ----------------------------------------------------------------------------------------
ks = [k for k in range(2, 20 + 1)] # assignment, assignment_lhs_identifier:ks, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:20, assignment_rhs_atom:k, binary_operator:Add, call_argument:, call_argument:2, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num, range:2:_
base = [10 ** k for k in range(ks[-1] + 1)] # assignment, assignment_lhs_identifier:base, assignment_rhs_atom:-1, assignment_rhs_atom:1, assignment_rhs_atom:10, assignment_rhs_atom:k, assignment_rhs_atom:ks, binary_operator:Add, binary_operator:Pow, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, index, int_literal, literal:Num, negative_index:-1, range:_
memo = {} # assignment, assignment_lhs_identifier:memo, literal:Dict
def next_term(a_i, k, i, n): # body_recursive_function:next_term (-> +50), function:next_term (-> +50), function_returning_something:next_term (-> +50), recursive_function:next_term (-> +50)
    ds_b = 0 # assignment, assignment_lhs_identifier:ds_b, assignment_rhs_atom:0, int_literal, literal:Num
    for j in range(k, len(a_i)): # accumulate_elements:ds_b (-> +1), call_argument:, call_argument:a_i, call_argument:k, composition, for:j (-> +1), for_range:k:_ (-> +1), function_call:len, function_call:range, range:k:_
        ds_b += a_i[j] # assignment_lhs_identifier:ds_b, assignment_rhs_atom:a_i, assignment_rhs_atom:j, augmented_assignment:Add, increment_variable:ds_b:a_i, increment_variable:ds_b:j, index, update_variable:ds_b:a_i, update_variable:ds_b:j
    c = 0 # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:0, int_literal, literal:Num
    for j in range(min(len(a_i), k)): # accumulate_elements:c (-> +1), call_argument:, call_argument:a_i, call_argument:k, composition, for:j (-> +1), for_range:_ (-> +1), function_call:len, function_call:min, function_call:range, range:_
        c += a_i[j] * base[j] # assignment_lhs_identifier:c, assignment_rhs_atom:a_i, assignment_rhs_atom:base, assignment_rhs_atom:j, augmented_assignment:Add, binary_operator:Mult, increment_variable:c:a_i, increment_variable:c:base, increment_variable:c:j, index, update_variable:c:a_i, update_variable:c:base, update_variable:c:j
    diff, dn = 0, 0 # assignment, assignment_lhs_identifier:diff, assignment_lhs_identifier:dn, assignment_rhs_atom:0, int_literal, literal:Num, literal:Tuple
    max_dn = n - i # assignment, assignment_lhs_identifier:max_dn, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Sub
    sub_memo = memo.get(ds_b) # assignment, assignment_lhs_identifier:sub_memo, assignment_rhs_atom:ds_b, assignment_rhs_atom:memo, call_argument:ds_b, method_call, method_call_name:get
    if sub_memo != None: # comparison_operator:NotEq, if (-> +19), if_test_atom:None, if_test_atom:sub_memo, literal:None
        jumps = sub_memo.get(c) # assignment, assignment_lhs_identifier:jumps, assignment_rhs_atom:c, assignment_rhs_atom:sub_memo, call_argument:c, if_then_branch (-> +15), method_call, method_call_name:get
        if jumps != None and len(jumps) > 0: # boolean_operator:And, call_argument:jumps, comparison_operator:Gt, comparison_operator:NotEq, function_call:len, if (-> +14), if_test_atom:0, if_test_atom:None, if_test_atom:jumps, int_literal, literal:None, literal:Num, nested_if:1 (-> +14)
            max_jump = -1 # assignment, assignment_lhs_identifier:max_jump, assignment_rhs_atom:-1, if_then_branch (-> +11), int_literal, literal:Num
            for _k in range(len(jumps) - 1, -1, -1): # binary_operator:Sub, call_argument:, call_argument:-1, call_argument:jumps, composition, for:_k (-> +3), for_range:_:-1:-1 (-> +3), function_call:len, function_call:range, int_literal, literal:Num, range:_:-1:-1
                if jumps[_k][2] <= k and jumps[_k][1] <= max_dn: # boolean_operator:And, comparison_operator:LtE, if (-> +2), if_test_atom:1, if_test_atom:2, if_test_atom:_k, if_test_atom:jumps, if_test_atom:k, if_test_atom:max_dn, index, int_literal, literal:Num, nested_if:2 (-> +2)
                    max_jump = _k # assignment, assignment_lhs_identifier:max_jump, assignment_rhs_atom:_k, if_then_branch (-> +1)
                    break
            if max_jump >= 0: # comparison_operator:GtE, if (-> +6), if_test_atom:0, if_test_atom:max_jump, int_literal, literal:Num, nested_if:2 (-> +6)
                diff, dn, _kk = jumps[max_jump] # assignment, assignment_lhs_identifier:_kk, assignment_lhs_identifier:diff, assignment_lhs_identifier:dn, assignment_rhs_atom:jumps, assignment_rhs_atom:max_jump, if_then_branch (-> +5), index
                new_c = diff + c # assignment, assignment_lhs_identifier:new_c, assignment_rhs_atom:c, assignment_rhs_atom:diff, binary_operator:Add
                for j in range(min(k, len(a_i))): # call_argument:, call_argument:a_i, call_argument:k, composition, for:j (-> +1), for_range:_ (-> +1), function_call:len, function_call:min, function_call:range, range:_
                    new_c, a_i[j] = divmod(new_c, 10) # assignment, assignment_lhs_identifier:a_i, assignment_lhs_identifier:new_c, assignment_rhs_atom:10, assignment_rhs_atom:new_c, call_argument:10, call_argument:new_c, function_call:divmod, index, int_literal, literal:Num, suggest_constant_definition, update_variable:new_c:10
                if new_c > 0: # comparison_operator:Gt, if (-> +1), if_test_atom:0, if_test_atom:new_c, int_literal, literal:Num, nested_if:3 (-> +1)
                    add(a_i, k, new_c) # call_argument:a_i, call_argument:k, call_argument:new_c, function_call:add, if_then_branch
        else:
            sub_memo[c] = [] # assignment, assignment_lhs_identifier:sub_memo, if_else_branch, index, literal:List
    else:
        sub_memo = {c: []} # assignment, assignment_lhs_identifier:sub_memo, assignment_rhs_atom:c, if_else_branch (-> +1), literal:List
        memo[ds_b] = sub_memo # assignment, assignment_lhs_identifier:memo, assignment_rhs_atom:sub_memo, index
    if dn >= max_dn or c + diff >= base[k]: # binary_operator:Add, boolean_operator:Or, comparison_operator:GtE, if (-> +1), if_test_atom:base, if_test_atom:c, if_test_atom:diff, if_test_atom:dn, if_test_atom:k, if_test_atom:max_dn, index
        return diff, dn # if_then_branch, return
    if k > ks[0]: # comparison_operator:Gt, if (-> +10), if_test_atom:0, if_test_atom:k, if_test_atom:ks, index, int_literal, literal:Num
        while True: # if_then_branch (-> +5), infinite_while, literal:True, while (-> +5)
            _diff, terms_jumped = next_term(a_i, k - 1, i + dn, n) # assignment, assignment_lhs_identifier:_diff, assignment_lhs_identifier:terms_jumped, assignment_rhs_atom:1, assignment_rhs_atom:a_i, assignment_rhs_atom:dn, assignment_rhs_atom:i, assignment_rhs_atom:k, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Sub, call_argument:, call_argument:a_i, call_argument:n, function_call:next_term, int_literal, literal:Num
            diff += _diff # assignment_lhs_identifier:diff, assignment_rhs_atom:_diff, augmented_assignment:Add, increment_variable:diff:_diff, update_variable:diff:_diff
            dn += terms_jumped # assignment_lhs_identifier:dn, assignment_rhs_atom:terms_jumped, augmented_assignment:Add, increment_variable:dn:terms_jumped, update_variable:dn:terms_jumped
            if dn >= max_dn or c + diff >= base[k]: # binary_operator:Add, boolean_operator:Or, comparison_operator:GtE, if (-> +1), if_test_atom:base, if_test_atom:c, if_test_atom:diff, if_test_atom:dn, if_test_atom:k, if_test_atom:max_dn, index, nested_if:1 (-> +1)
                break # if_then_branch
    else:
        _diff, terms_jumped = compute(a_i, k, i + dn, n) # assignment, assignment_lhs_identifier:_diff, assignment_lhs_identifier:terms_jumped, assignment_rhs_atom:a_i, assignment_rhs_atom:dn, assignment_rhs_atom:i, assignment_rhs_atom:k, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:a_i, call_argument:k, call_argument:n, function_call:compute, if_else_branch (-> +2)
        diff += _diff # assignment_lhs_identifier:diff, assignment_rhs_atom:_diff, augmented_assignment:Add, increment_variable:diff:_diff, update_variable:diff:_diff
        dn += terms_jumped # assignment_lhs_identifier:dn, assignment_rhs_atom:terms_jumped, augmented_assignment:Add, increment_variable:dn:terms_jumped, update_variable:dn:terms_jumped
    jumps = sub_memo[c] # assignment, assignment_lhs_identifier:jumps, assignment_rhs_atom:c, assignment_rhs_atom:sub_memo, index
    j = 0 # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:0, int_literal, literal:Num
    while j < len(jumps): # call_argument:jumps, comparison_operator:Lt, function_call:len, while (-> +3)
        if jumps[j][1] > dn: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:dn, if_test_atom:j, if_test_atom:jumps, index, int_literal, literal:Num
            break # if_then_branch
        j += 1 # assignment_lhs_identifier:j, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:j:1, int_literal, literal:Num, update_variable:j:1
    sub_memo[c].insert(j, (diff, dn, k)) # call_argument:, call_argument:j, index, method_call, method_call_name:insert
    return (diff, dn) # return
def compute(a_i, k, i, n): # function:compute (-> +25), function_returning_something:compute (-> +25)
    if i >= n: # comparison_operator:GtE, if (-> +1), if_test_atom:i, if_test_atom:n
        return 0, i # if_then_branch, int_literal, literal:Num, return
    if k > len(a_i): # call_argument:a_i, comparison_operator:Gt, function_call:len, if (-> +1), if_test_atom:a_i, if_test_atom:k
        a_i.extend([0 for _ in range(k - len(a_i))]) # binary_operator:Sub, call_argument:, call_argument:a_i, composition, comprehension:List, comprehension_for_count:1, function_call:len, function_call:range, if_then_branch, int_literal, literal:Num, method_call, method_call_name:extend, method_call_object:a_i, range:_, update_variable:a_i:, update_variable:a_i:a_i
    start_i = i # assignment, assignment_lhs_identifier:start_i, assignment_rhs_atom:i
    ds_b, ds_c, diff = 0, 0, 0 # assignment, assignment_lhs_identifier:diff, assignment_lhs_identifier:ds_b, assignment_lhs_identifier:ds_c, assignment_rhs_atom:0, int_literal, literal:Num, literal:Tuple
    for j in range(len(a_i)): # accumulate_elements:ds_b (-> +4), accumulate_elements:ds_c (-> +4), call_argument:, call_argument:a_i, composition, for:j (-> +4), for_indexes (-> +4), for_range:_ (-> +4), function_call:len, function_call:range, range:_
        if j >= k: # comparison_operator:GtE, if (-> +3), if_test_atom:j, if_test_atom:k
            ds_b += a_i[j] # assignment_lhs_identifier:ds_b, assignment_rhs_atom:a_i, assignment_rhs_atom:j, augmented_assignment:Add, if_then_branch, increment_variable:ds_b:a_i, increment_variable:ds_b:j, index, update_variable:ds_b:a_i, update_variable:ds_b:j
        else:
            ds_c += a_i[j] # assignment_lhs_identifier:ds_c, assignment_rhs_atom:a_i, assignment_rhs_atom:j, augmented_assignment:Add, if_else_branch, increment_variable:ds_c:a_i, increment_variable:ds_c:j, index, update_variable:ds_c:a_i, update_variable:ds_c:j
    while i < n: # comparison_operator:Lt, while (-> +10)
        i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, increment_variable:i:1, int_literal, literal:Num, update_variable:i:1
        addend = ds_c + ds_b # assignment, assignment_lhs_identifier:addend, assignment_rhs_atom:ds_b, assignment_rhs_atom:ds_c, binary_operator:Add
        diff += addend # assignment_lhs_identifier:diff, assignment_rhs_atom:addend, augmented_assignment:Add, increment_variable:diff:addend, update_variable:diff:addend
        ds_c = 0 # assignment, assignment_lhs_identifier:ds_c, assignment_rhs_atom:0, int_literal, literal:Num
        for j in range(k): # accumulate_elements:ds_c (-> +3), call_argument:k, for:j (-> +3), for_range:k (-> +3), function_call:range, range:k
            s = a_i[j] + addend # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:a_i, assignment_rhs_atom:addend, assignment_rhs_atom:j, binary_operator:Add, index
            addend, a_i[j] = divmod(s, 10) # assignment, assignment_lhs_identifier:a_i, assignment_lhs_identifier:addend, assignment_rhs_atom:10, assignment_rhs_atom:s, call_argument:10, call_argument:s, function_call:divmod, index, int_literal, literal:Num, suggest_constant_definition
            ds_c += a_i[j] # assignment_lhs_identifier:ds_c, assignment_rhs_atom:a_i, assignment_rhs_atom:j, augmented_assignment:Add, increment_variable:ds_c:a_i, increment_variable:ds_c:j, index, update_variable:ds_c:a_i, update_variable:ds_c:j
        if addend > 0: # comparison_operator:Gt, if (-> +1), if_test_atom:0, if_test_atom:addend, int_literal, literal:Num
            break # if_then_branch
    if addend > 0: # comparison_operator:Gt, if (-> +1), if_test_atom:0, if_test_atom:addend, int_literal, literal:Num
        add(a_i, k, addend) # call_argument:a_i, call_argument:addend, call_argument:k, function_call:add, if_then_branch
    return diff, i - start_i # binary_operator:Sub, return
def add(digits, k, addend): # function:add (-> +13), function_returning_nothing:add (-> +13)
    for j in range(k, len(digits)): # call_argument:, call_argument:digits, call_argument:k, composition, for:j (-> +9), for_range:k:_ (-> +9), function_call:len, function_call:range, range:k:_
        s = digits[j] + addend # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:addend, assignment_rhs_atom:digits, assignment_rhs_atom:j, binary_operator:Add, index
        if s >= 10: # comparison_operator:GtE, if (-> +5), if_test_atom:10, if_test_atom:s, int_literal, literal:Num, suggest_constant_definition
            quotient, digits[j] = divmod(s, 10) # assignment, assignment_lhs_identifier:digits, assignment_lhs_identifier:quotient, assignment_rhs_atom:10, assignment_rhs_atom:s, call_argument:10, call_argument:s, function_call:divmod, if_then_branch (-> +1), index, int_literal, literal:Num, suggest_constant_definition
            addend = addend // 10 + quotient # assignment, assignment_lhs_identifier:addend, assignment_rhs_atom:10, assignment_rhs_atom:addend, assignment_rhs_atom:quotient, binary_operator:Add, binary_operator:FloorDiv, increment_variable:addend:10, increment_variable:addend:quotient, int_literal, literal:Num, suggest_constant_definition, update_variable:addend:10, update_variable:addend:quotient
        else:
            digits[j] = s # assignment, assignment_lhs_identifier:digits, assignment_rhs_atom:s, if_else_branch (-> +1), index
            addend = addend // 10 # assignment, assignment_lhs_identifier:addend, assignment_rhs_atom:10, assignment_rhs_atom:addend, binary_operator:FloorDiv, int_literal, literal:Num, suggest_augmented_assignment, suggest_constant_definition, update_variable:addend:10
        if addend == 0: # comparison_operator:Eq, if (-> +1), if_test_atom:0, if_test_atom:addend, int_literal, literal:Num
            break # if_then_branch
    while addend > 0: # comparison_operator:Gt, int_literal, literal:Num, while (-> +2)
        addend, digit = divmod(addend, 10) # assignment, assignment_lhs_identifier:addend, assignment_lhs_identifier:digit, assignment_rhs_atom:10, assignment_rhs_atom:addend, call_argument:10, call_argument:addend, function_call:divmod, int_literal, literal:Num, suggest_constant_definition, update_variable:addend:10
        digits.append(digit) # call_argument:digit, method_call, method_call_name:append, method_call_object:digits, update_variable:digits:digit
def solution(n): # function:solution (-> +12), function_returning_something:solution (-> +12)
    digits = [1] # assignment, assignment_lhs_identifier:digits, assignment_rhs_atom:1, int_literal, literal:List, literal:Num
    i = 1 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:1, int_literal, literal:Num
    dn = 0 # assignment, assignment_lhs_identifier:dn, assignment_rhs_atom:0, int_literal, literal:Num
    while True: # infinite_while, literal:True, while (-> +4)
        diff, terms_jumped = next_term(digits, 20, i + dn, n) # assignment, assignment_lhs_identifier:diff, assignment_lhs_identifier:terms_jumped, assignment_rhs_atom:20, assignment_rhs_atom:digits, assignment_rhs_atom:dn, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Add, call_argument:, call_argument:20, call_argument:digits, call_argument:n, function_call:next_term, int_literal, literal:Num, suggest_constant_definition
        dn += terms_jumped # assignment_lhs_identifier:dn, assignment_rhs_atom:terms_jumped, augmented_assignment:Add, increment_variable:dn:terms_jumped, update_variable:dn:terms_jumped
        if dn == n - i: # binary_operator:Sub, comparison_operator:Eq, if (-> +1), if_test_atom:dn, if_test_atom:i, if_test_atom:n
            break # if_then_branch
    a_n = 0 # assignment, assignment_lhs_identifier:a_n, assignment_rhs_atom:0, int_literal, literal:Num
    for j in range(len(digits)): # accumulate_elements:a_n (-> +1), call_argument:, call_argument:digits, composition, for:j (-> +1), for_indexes (-> +1), for_range:_ (-> +1), function_call:len, function_call:range, range:_
        a_n += digits[j] * 10 ** j # assignment_lhs_identifier:a_n, assignment_rhs_atom:10, assignment_rhs_atom:digits, assignment_rhs_atom:j, augmented_assignment:Add, binary_operator:Mult, binary_operator:Pow, increment_variable:a_n:10, increment_variable:a_n:digits, increment_variable:a_n:j, index, int_literal, literal:Num, suggest_constant_definition, update_variable:a_n:10, update_variable:a_n:digits, update_variable:a_n:j
    return a_n # return:a_n

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_56/sol1.py
# ----------------------------------------------------------------------------------------
def maximum_digital_sum(a: int, b: int) -> int: # function:maximum_digital_sum (-> +5), function_returning_something:maximum_digital_sum (-> +5)
    return max( # composition, function_call:max, function_tail_call:max, return
        [
            sum([int(x) for x in str(base ** power)]) # binary_operator:Pow, call_argument:, call_argument:x, composition, comprehension:List, comprehension_for_count:1, comprehension_for_count:2, function_call:int, function_call:str, function_call:sum
            for base in range(a) # call_argument:a, function_call:range, range:a
            for power in range(b) # call_argument:b, function_call:range, range:b
        ]
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_67/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
def solution(): # function:solution (-> +18), function_returning_something:solution (-> +18)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, assignment_lhs_identifier:script_dir, assignment_rhs_atom:__file__, assignment_rhs_atom:os, call_argument:, call_argument:__file__, composition, method_call, method_call_name:dirname, method_call_name:realpath
    triangle = os.path.join(script_dir, "triangle.txt") # assignment, assignment_lhs_identifier:triangle, assignment_rhs_atom:os, assignment_rhs_atom:script_dir, call_argument:, call_argument:script_dir, literal:Str, method_call, method_call_name:join
    with open(triangle, "r") as f: # call_argument:, call_argument:triangle, function_call:open, literal:Str
        triangle = f.readlines() # assignment, assignment_lhs_identifier:triangle, assignment_rhs_atom:f, method_call, method_call_name:readlines
    a = map(lambda x: x.rstrip("\r\n").split(" "), triangle) # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:triangle, assignment_rhs_atom:x, call_argument:, call_argument:triangle, composition, function_call:map, lambda_function, literal:Str, method_call, method_call_name:rstrip, method_call_name:split, method_call_object:x, method_chaining
    a = list(map(lambda x: list(map(lambda y: int(y), x)), a)) # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:a, assignment_rhs_atom:x, assignment_rhs_atom:y, call_argument:, call_argument:a, call_argument:x, call_argument:y, composition, function_call:int, function_call:list, function_call:map, lambda_function, update_variable:a:x, update_variable:a:y
    for i in range(1, len(a)): # call_argument:, call_argument:1, call_argument:a, composition, for:i (-> +10), for_range:1:_ (-> +10), for_range:_ (-> +10), function_call:len, function_call:range, int_literal, literal:Num, range:1:_
        for j in range(len(a[i])): # call_argument:, composition, for:j (-> +9), for_indexes (-> +9), for_range:_ (-> +9), function_call:len, function_call:range, index, nested_for:1 (-> +9), range:_
            if j != len(a[i - 1]): # binary_operator:Sub, call_argument:, comparison_operator:NotEq, function_call:len, if (-> +3), if_test_atom:1, if_test_atom:a, if_test_atom:i, if_test_atom:j, index, index_arithmetic, int_literal, literal:Num, suggest_conditional_expression (-> +3)
                number1 = a[i - 1][j] # assignment, assignment_lhs_identifier:number1, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
            else:
                number1 = 0 # assignment, assignment_lhs_identifier:number1, assignment_rhs_atom:0, if_else_branch, int_literal, literal:Num
            if j > 0: # comparison_operator:Gt, if (-> +3), if_test_atom:0, if_test_atom:j, int_literal, literal:Num, suggest_conditional_expression (-> +3)
                number2 = a[i - 1][j - 1] # assignment, assignment_lhs_identifier:number2, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:j, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
            else:
                number2 = 0 # assignment, assignment_lhs_identifier:number2, assignment_rhs_atom:0, if_else_branch, int_literal, literal:Num
            a[i][j] += max(number1, number2) # assignment_rhs_atom:number1, assignment_rhs_atom:number2, augmented_assignment:Add, call_argument:number1, call_argument:number2, function_call:max, index
    return max(a[-1]) # call_argument:, function_call:max, function_tail_call:max, index, int_literal, literal:Num, negative_index:-1, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_76/sol1.py
# ----------------------------------------------------------------------------------------
def partition(m): # function:partition (-> +9), function_returning_something:partition (-> +9)
    memo = [[0 for _ in range(m)] for _ in range(m + 1)] # assignment, assignment_lhs_identifier:memo, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:_, assignment_rhs_atom:m, binary_operator:Add, call_argument:, call_argument:m, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num, range:_, range:m
    for i in range(m + 1): # binary_operator:Add, call_argument:, for:i (-> +1), for_range:_ (-> +1), function_call:range, int_literal, literal:Num, range:_
        memo[i][0] = 1 # assignment, assignment_rhs_atom:1, index, int_literal, literal:Num
    for n in range(m + 1): # binary_operator:Add, call_argument:, for:n (-> +4), for_range:1:m (-> +4), for_range:_ (-> +4), function_call:range, int_literal, literal:Num, range:_
        for k in range(1, m): # call_argument:1, call_argument:m, for:k (-> +3), for_range:1:m (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), range:1:m
            memo[n][k] += memo[n][k - 1] # assignment_rhs_atom:1, assignment_rhs_atom:k, assignment_rhs_atom:memo, assignment_rhs_atom:n, augmented_assignment:Add, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num
            if n > k: # comparison_operator:Gt, if (-> +1), if_test_atom:k, if_test_atom:n
                memo[n][k] += memo[n - k - 1][k] # assignment_rhs_atom:1, assignment_rhs_atom:k, assignment_rhs_atom:memo, assignment_rhs_atom:n, augmented_assignment:Add, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
    return memo[m][m - 1] - 1 # binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, return

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_99/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os
from math import log10 # import:math:log10, import_module:math, import_name:log10
def find_largest(data_file: str = "base_exp.txt") -> int: # function:find_largest (-> +6), function_returning_something:find_largest (-> +6), function_with_default_positional_arguments:find_largest (-> +6), literal:Str
    largest = [0, 0] # assignment, assignment_lhs_identifier:largest, assignment_rhs_atom:0, int_literal, literal:List, literal:Num
    for i, line in enumerate(open(os.path.join(os.path.dirname(__file__), data_file))): # call_argument:, call_argument:__file__, call_argument:data_file, composition, for:i:line (-> +3), for_indexes_elements (-> +3), function_call:enumerate, function_call:open, method_call, method_call_name:dirname, method_call_name:join
        a, x = list(map(int, line.split(","))) # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:x, assignment_rhs_atom:int, assignment_rhs_atom:line, call_argument:, call_argument:int, composition, function_call:list, function_call:map, literal:Str, method_call, method_call_name:split
        if x * log10(a) > largest[0]: # binary_operator:Mult, call_argument:a, comparison_operator:Gt, function_call:log10, if (-> +1), if_test_atom:0, if_test_atom:a, if_test_atom:largest, if_test_atom:x, index, int_literal, literal:Num
            largest = [x * log10(a), i + 1] # assignment, assignment_lhs_identifier:largest, assignment_rhs_atom:1, assignment_rhs_atom:a, assignment_rhs_atom:i, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, call_argument:a, function_call:log10, if_then_branch, int_literal, literal:Num
    return largest[1] # index, int_literal, literal:Num, return
