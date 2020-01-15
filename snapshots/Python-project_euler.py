# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return sum([e for e in range(3, n) if e % 3 == 0 or e % 5 == 0]) # binary_operator:Mod, boolean_operator:Or, call_parameter:n, comparison_operator:Eq, composition, comprehension:List, comprehension_for_count:1, divisibility_test:3, divisibility_test:5, filtered_comprehension, function_call:range, function_call:sum, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_returning_a_value:solution (-> +8)
    sum = 0 # assignment, assignment_lhs_identifier:sum, int_literal, literal:Num
    terms = (n - 1) // 3 # assignment, assignment_lhs_identifier:terms, assignment_rhs_identifier:n, binary_operator:FloorDiv, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    sum += ((terms) * (6 + (terms - 1) * 3)) // 2 # assignment_lhs_identifier:sum, assignment_rhs_identifier:terms, augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    terms = (n - 1) // 5 # assignment, assignment_lhs_identifier:terms, assignment_rhs_identifier:n, binary_operator:FloorDiv, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    sum += ((terms) * (10 + (terms - 1) * 5)) // 2 # assignment_lhs_identifier:sum, assignment_rhs_identifier:terms, augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    terms = (n - 1) // 15 # assignment, assignment_lhs_identifier:terms, assignment_rhs_identifier:n, binary_operator:FloorDiv, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    sum -= ((terms) * (30 + (terms - 1) * 15)) // 2 # assignment_lhs_identifier:sum, assignment_rhs_identifier:terms, augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +32), function_returning_a_value:solution (-> +32)
    sum = 0 # assignment, assignment_lhs_identifier:sum, int_literal, literal:Num
    num = 0 # assignment, assignment_lhs_identifier:num, int_literal, literal:Num
    while 1: # int_literal, literal:Num, while (-> +28)
        num += 3 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num, suggest_constant_definition
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_identifier:num, augmented_assignment
        num += 2 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_identifier:num, augmented_assignment
        num += 1 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_identifier:num, augmented_assignment
        num += 3 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num, suggest_constant_definition
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_identifier:num, augmented_assignment
        num += 1 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_identifier:num, augmented_assignment
        num += 2 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_identifier:num, augmented_assignment
        num += 3 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num, suggest_constant_definition
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break # if_then_branch
        sum += num # assignment_lhs_identifier:sum, assignment_rhs_identifier:num, augmented_assignment
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +22), function_returning_a_value:solution (-> +22)
    xmulti = [] # assignment, assignment_lhs_identifier:xmulti, literal:List
    zmulti = [] # assignment, assignment_lhs_identifier:zmulti, literal:List
    z = 3 # assignment, assignment_lhs_identifier:z, int_literal, literal:Num, suggest_constant_definition
    x = 5 # assignment, assignment_lhs_identifier:x, int_literal, literal:Num, suggest_constant_definition
    temp = 1 # assignment, assignment_lhs_identifier:temp, int_literal, literal:Num
    while True: # literal:True, while (-> +7)
        result = z * temp # assignment, assignment_lhs_identifier:result, assignment_rhs_identifier:temp, assignment_rhs_identifier:z, binary_operator:Mult
        if result < n: # comparison_operator:Lt, if (-> +5)
            zmulti.append(result) # call_parameter:result, if_then_branch (-> +1), method_call:append, method_call_object:zmulti
            temp += 1 # assignment_lhs_identifier:temp, augmented_assignment, int_literal, literal:Num
        else:
            temp = 1 # assignment, assignment_lhs_identifier:temp, if_else_branch (-> +1), int_literal, literal:Num
            break
    while True: # literal:True, while (-> +6)
        result = x * temp # assignment, assignment_lhs_identifier:result, assignment_rhs_identifier:temp, assignment_rhs_identifier:x, binary_operator:Mult
        if result < n: # comparison_operator:Lt, if (-> +4)
            xmulti.append(result) # call_parameter:result, if_then_branch (-> +1), method_call:append, method_call_object:xmulti
            temp += 1 # assignment_lhs_identifier:temp, augmented_assignment, int_literal, literal:Num
        else:
            break # if_else_branch
    collection = list(set(xmulti + zmulti)) # assignment, assignment_lhs_identifier:collection, assignment_rhs_identifier:list, assignment_rhs_identifier:set, assignment_rhs_identifier:xmulti, assignment_rhs_identifier:zmulti, binary_operator:Add, composition, function_call:list, function_call:set
    return sum(collection) # call_parameter:collection, function_call:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0]) # binary_operator:Mod, boolean_operator:Or, call_parameter:n, comparison_operator:Eq, composition, comprehension:List, comprehension_for_count:1, divisibility_test:3, divisibility_test:5, filtered_comprehension, function_call:range, function_call:sum, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol6.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +9), function_returning_a_value:solution (-> +9)
    a = 3 # assignment, assignment_lhs_identifier:a, int_literal, literal:Num, suggest_constant_definition
    result = 0 # assignment, assignment_lhs_identifier:result, int_literal, literal:Num
    while a < n: # comparison_operator:Lt, while (-> +5)
        if a % 3 == 0 or a % 5 == 0: # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, divisibility_test:3, divisibility_test:5, if (-> +3), int_literal, literal:Num, suggest_constant_definition
            result += a # assignment_lhs_identifier:result, assignment_rhs_identifier:a, augmented_assignment, if_then_branch
        elif a % 15 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:15, if (-> +1), int_literal, literal:Num, suggest_constant_definition
            result -= a # assignment_lhs_identifier:result, assignment_rhs_identifier:a, augmented_assignment, if_elif_branch
        a += 1 # assignment_lhs_identifier:a, augmented_assignment, int_literal, literal:Num
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol7.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_a_value:solution (-> +7)
    result = 0 # assignment, assignment_lhs_identifier:result, int_literal, literal:Num
    for i in range(n): # accumulate_elements:1 (-> +4), call_parameter:n, for:i (-> +4), for_range_stop (-> +4), function_call:range
        if i % 3 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:3, if (-> +3), int_literal, literal:Num, suggest_constant_definition
            result += i # assignment_lhs_identifier:result, assignment_rhs_identifier:i, augmented_assignment, if_then_branch
        elif i % 5 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:5, if (-> +1), int_literal, literal:Num, suggest_constant_definition
            result += i # assignment_lhs_identifier:result, assignment_rhs_identifier:i, augmented_assignment, if_elif_branch
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_returning_a_value:solution (-> +8)
    i = 1 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    j = 2 # assignment, assignment_lhs_identifier:j, int_literal, literal:Num
    sum = 0 # assignment, assignment_lhs_identifier:sum, int_literal, literal:Num
    while j <= n: # comparison_operator:LtE, while (-> +3)
        if j % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), int_literal, literal:Num
            sum += j # assignment_lhs_identifier:sum, assignment_rhs_identifier:j, augmented_assignment, if_then_branch
        i, j = j, i + j # assignment, assignment_lhs_identifier:i, assignment_lhs_identifier:j, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Add
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_a_value:solution (-> +7)
    ls = [] # assignment, assignment_lhs_identifier:ls, literal:List
    a, b = 0, 1 # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, int_literal, literal:Num, literal:Tuple
    while b <= n: # comparison_operator:LtE, while (-> +3)
        if b % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), int_literal, literal:Num
            ls.append(b) # call_parameter:b, if_then_branch, method_call:append, method_call_object:ls
        a, b = b, a + b # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_identifier:a, assignment_rhs_identifier:b, binary_operator:Add
    return ls

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +9), function_returning_a_value:solution (-> +9)
    if n <= 1: # comparison_operator:LtE, if (-> +1), int_literal, literal:Num
        return 0 # if_then_branch, int_literal, literal:Num
    a = 0 # assignment, assignment_lhs_identifier:a, int_literal, literal:Num
    b = 2 # assignment, assignment_lhs_identifier:b, int_literal, literal:Num
    count = 0 # assignment, assignment_lhs_identifier:count, int_literal, literal:Num
    while 4 * b + a <= n: # binary_operator:Add, binary_operator:Mult, comparison_operator:LtE, int_literal, literal:Num, suggest_constant_definition, while (-> +2)
        a, b = b, 4 * b + a # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_identifier:a, assignment_rhs_identifier:b, binary_operator:Add, binary_operator:Mult, int_literal, literal:Num, suggest_constant_definition
        count += a # assignment_lhs_identifier:count, assignment_rhs_identifier:a, augmented_assignment
    return count + b # binary_operator:Add

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol4.py
# ----------------------------------------------------------------------------------------
import math # import:math
from decimal import Decimal, getcontext # import_from:decimal
def solution(n): # function:solution (-> +12), function_returning_a_value:solution (-> +12)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:int, assignment_rhs_identifier:n, call_parameter:n, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    getcontext().prec = 100 # assignment, function_call:getcontext, int_literal, literal:Num, suggest_constant_definition
    phi = (Decimal(5) ** Decimal(0.5) + 1) / Decimal(2) # assignment, assignment_lhs_identifier:phi, assignment_rhs_identifier:Decimal, binary_operator:Add, binary_operator:Div, binary_operator:Pow, float_literal, function_call:Decimal, int_literal, literal:Num, suggest_constant_definition
    index = (math.floor(math.log(n * (phi + 2), phi) - 1) // 3) * 3 + 2 # assignment, assignment_lhs_identifier:index, assignment_rhs_identifier:math, assignment_rhs_identifier:n, assignment_rhs_identifier:phi, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, call_parameter:phi, composition, int_literal, literal:Num, method_call:floor, method_call:log, suggest_constant_definition
    num = Decimal(round(phi ** Decimal(index + 1))) / (phi + 2) # assignment, assignment_lhs_identifier:num, assignment_rhs_identifier:Decimal, assignment_rhs_identifier:index, assignment_rhs_identifier:phi, assignment_rhs_identifier:round, binary_operator:Add, binary_operator:Div, binary_operator:Pow, composition, function_call:Decimal, function_call:round, int_literal, literal:Num
    sum = num // 2 # assignment, assignment_lhs_identifier:sum, assignment_rhs_identifier:num, binary_operator:FloorDiv, int_literal, literal:Num
    return int(sum) # call_parameter:sum, function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +12), function_returning_a_value:solution (-> +12)
    a = [0, 1] # assignment, assignment_lhs_identifier:a, int_literal, literal:List, literal:Num
    i = 0 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    while a[i] <= n: # comparison_operator:LtE, index, while (-> +4)
        a.append(a[i] + a[i + 1]) # binary_operator:Add, index, index_arithmetic, int_literal, literal:Num, method_call:append, method_call_object:a
        if a[i + 2] > n: # binary_operator:Add, comparison_operator:Gt, if (-> +1), index, index_arithmetic, int_literal, literal:Num
            break # if_then_branch
        i += 1 # assignment_lhs_identifier:i, augmented_assignment, int_literal, literal:Num
    sum = 0 # assignment, assignment_lhs_identifier:sum, int_literal, literal:Num
    for j in range(len(a) - 1): # accumulate_elements:1 (-> +2), binary_operator:Sub, call_parameter:a, composition, for:j (-> +2), for_range_stop (-> +2), function_call:len, function_call:range, int_literal, literal:Num
        if a[j] % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), index, int_literal, literal:Num
            sum += a[j] # assignment_lhs_identifier:sum, assignment_rhs_identifier:a, assignment_rhs_identifier:j, augmented_assignment, if_then_branch, index
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol1.py
# ----------------------------------------------------------------------------------------
import math # import:math
def isprime(no): # function:isprime (-> +9), function_returning_a_value:isprime (-> +9)
    if no == 2: # comparison_operator:Eq, if (-> +3), int_literal, literal:Num
        return True # if_then_branch, literal:True
    elif no % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), int_literal, literal:Num
        return False # if_elif_branch, literal:False
    sq = int(math.sqrt(no)) + 1 # assignment, assignment_lhs_identifier:sq, assignment_rhs_identifier:int, assignment_rhs_identifier:math, assignment_rhs_identifier:no, binary_operator:Add, call_parameter:no, composition, function_call:int, int_literal, literal:Num, method_call:sqrt
    for i in range(3, sq, 2): # call_parameter:sq, for:i (-> +2), for_range_step:2 (-> +2), function_call:range, int_literal, literal:Num, suggest_constant_definition, universal_quantifier (-> +3)
        if no % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), int_literal, literal:Num
            return False # if_then_branch, literal:False
    return True # literal:True
def solution(n): # function:solution (-> +24), function_returning_a_value:solution (-> +24)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:int, assignment_rhs_identifier:n, call_parameter:n, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    maxNumber = 0 # assignment, assignment_lhs_identifier:maxNumber, int_literal, literal:Num
    if isprime(n): # call_parameter:n, function_call:isprime, if (-> +16)
        return n # if_then_branch
    else:
        while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +1), if_else_branch (-> +13), int_literal, literal:Num, while (-> +1)
            n = n / 2 # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:n, binary_operator:Div, int_literal, literal:Num, suggest_augmented_assignment
        if isprime(n): # call_parameter:n, function_call:isprime, if (-> +11), nested_if:1 (-> +11)
            return int(n) # call_parameter:n, function_call:int, if_then_branch
        else:
            n1 = int(math.sqrt(n)) + 1 # assignment, assignment_lhs_identifier:n1, assignment_rhs_identifier:int, assignment_rhs_identifier:math, assignment_rhs_identifier:n, binary_operator:Add, call_parameter:n, composition, function_call:int, if_else_branch (-> +8), int_literal, literal:Num, method_call:sqrt
            for i in range(3, n1, 2): # call_parameter:n1, for:i (-> +6), for_range_step:2 (-> +6), function_call:range, int_literal, literal:Num, suggest_constant_definition
                if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +5), int_literal, literal:Num, nested_if:2 (-> +5)
                    if isprime(n / i): # binary_operator:Div, function_call:isprime, if (-> +4), if_then_branch (-> +4), nested_if:3 (-> +4)
                        maxNumber = n / i # assignment, assignment_lhs_identifier:maxNumber, assignment_rhs_identifier:i, assignment_rhs_identifier:n, binary_operator:Div, if_then_branch (-> +1)
                        break
                    elif isprime(i): # call_parameter:i, function_call:isprime, if (-> +1), nested_if:3 (-> +1)
                        maxNumber = i # assignment, assignment_lhs_identifier:maxNumber, assignment_rhs_identifier:i, if_elif_branch
            return maxNumber

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +16), function_returning_a_value:solution (-> +16)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:int, assignment_rhs_identifier:n, call_parameter:n, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    prime = 1 # assignment, assignment_lhs_identifier:prime, int_literal, literal:Num
    i = 2 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    while i * i <= n: # binary_operator:Mult, comparison_operator:LtE, evolve_state (-> +4), while (-> +4)
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +2)
            prime = i # assignment, assignment_lhs_identifier:prime, assignment_rhs_identifier:i
            n //= i # assignment_lhs_identifier:n, assignment_rhs_identifier:i, augmented_assignment
        i += 1 # assignment_lhs_identifier:i, augmented_assignment, int_literal, literal:Num
    if n > 1: # comparison_operator:Gt, if (-> +1), int_literal, literal:Num
        prime = n # assignment, assignment_lhs_identifier:prime, assignment_rhs_identifier:n, if_then_branch
    return int(prime) # call_parameter:prime, function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n: int) -> int: # function:solution, function_returning_a_value:solution
    try: # catch_exception (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:int, assignment_rhs_identifier:n, call_parameter:n, function_call:int
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    i = 2 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    ans = 0 # assignment, assignment_lhs_identifier:ans, int_literal, literal:Num
    if n == 2: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
        return 2 # if_then_branch, int_literal, literal:Num
    while n > 2: # comparison_operator:Gt, evolve_state (-> +6), int_literal, literal:Num, while (-> +6)
        while n % i != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test, evolve_state (-> +1), int_literal, literal:Num, while (-> +1)
            i += 1 # assignment_lhs_identifier:i, augmented_assignment, int_literal, literal:Num
        ans = i # assignment, assignment_lhs_identifier:ans, assignment_rhs_identifier:i
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +1)
            n = n / i # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:i, assignment_rhs_identifier:n, binary_operator:Div, suggest_augmented_assignment
        i += 1 # assignment_lhs_identifier:i, augmented_assignment, int_literal, literal:Num
    return int(ans) # call_parameter:ans, function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_04/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_returning_a_value:solution (-> +8)
    for number in range(n - 1, 10000, -1): # binary_operator:Sub, find_first_element (-> +6), for:number (-> +7), for_range_step:-1 (-> +7), function_call:range, int_literal, literal:Num, suggest_constant_definition
        strNumber = str(number) # assignment, assignment_lhs_identifier:strNumber, assignment_rhs_identifier:number, assignment_rhs_identifier:str, call_parameter:number, function_call:str
        if strNumber == strNumber[::-1]: # comparison_operator:Eq, if (-> +5), int_literal, literal:Num, slice_step
            divisor = 999 # assignment, assignment_lhs_identifier:divisor, if_then_branch (-> +4), int_literal, literal:Num, suggest_constant_definition
            while divisor != 99: # comparison_operator:NotEq, evolve_state (-> +3), int_literal, literal:Num, suggest_constant_definition, while (-> +3)
                if (number % divisor == 0) and (len(str(int(number / divisor))) == 3): # binary_operator:Div, binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, composition, divisibility_test, function_call:int, function_call:len, function_call:str, if (-> +1), int_literal, literal:Num, nested_if:1 (-> +1), suggest_constant_definition
                    return number # if_then_branch
                divisor -= 1 # assignment_lhs_identifier:divisor, augmented_assignment, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_04/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_a_value:solution (-> +7)
    answer = 0 # assignment, assignment_lhs_identifier:answer, int_literal, literal:Num
    for i in range(999, 99, -1): # accumulate_elements:1 (-> +4), for:i (-> +4), for_range_step:-1 (-> +4), function_call:range, int_literal, literal:Num, square_nested_for (-> +4), suggest_constant_definition
        for j in range(999, 99, -1): # accumulate_elements:1 (-> +3), for:j (-> +3), for_range_step:-1 (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), suggest_constant_definition
            t = str(i * j) # assignment, assignment_lhs_identifier:t, assignment_rhs_identifier:i, assignment_rhs_identifier:j, assignment_rhs_identifier:str, binary_operator:Mult, function_call:str
            if t == t[::-1] and i * j < n: # binary_operator:Mult, boolean_operator:And, comparison_operator:Eq, comparison_operator:Lt, if (-> +1), int_literal, literal:Num, slice_step
                answer = max(answer, i * j) # assignment, assignment_lhs_identifier:answer, assignment_rhs_identifier:answer, assignment_rhs_identifier:i, assignment_rhs_identifier:j, assignment_rhs_identifier:max, binary_operator:Mult, call_parameter:answer, function_call:max, if_then_branch
    return answer

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_05/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +18), function_returning_a_value:solution (-> +18)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:int, assignment_rhs_identifier:n, call_parameter:n, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    i = 0 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    while 1: # int_literal, literal:Num, while (-> +10)
        i += n * (n - 1) # assignment_lhs_identifier:i, assignment_rhs_identifier:n, augmented_assignment, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num
        nfound = 0 # assignment, assignment_lhs_identifier:nfound, int_literal, literal:Num
        for j in range(2, n): # call_parameter:n, for:j (-> +3), for_range_start (-> +3), function_call:range, int_literal, literal:Num
            if i % j != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test, if (-> +2), int_literal, literal:Num
                nfound = 1 # assignment, assignment_lhs_identifier:nfound, if_then_branch (-> +1), int_literal, literal:Num
                break
        if nfound == 0: # comparison_operator:Eq, if (-> +3), int_literal, literal:Num
            if i == 0: # comparison_operator:Eq, if (-> +1), if_then_branch (-> +2), int_literal, literal:Num, nested_if:1 (-> +1)
                i = 1 # assignment, assignment_lhs_identifier:i, if_then_branch, int_literal, literal:Num
            return i

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_05/sol2.py
# ----------------------------------------------------------------------------------------
def gcd(x, y): # function:gcd (-> +1), function_returning_a_value:gcd (-> +1), recursive_function:gcd (-> +1)
    return x if y == 0 else gcd(y, x % y) # binary_operator:Mod, call_parameter:y, comparison_operator:Eq, conditional_expression, function_call:gcd, int_literal, literal:Num
def lcm(x, y): # function:lcm (-> +1), function_returning_a_value:lcm (-> +1)
    return (x * y) // gcd(x, y) # binary_operator:FloorDiv, binary_operator:Mult, call_parameter:x, call_parameter:y, function_call:gcd
def solution(n): # function:solution (-> +4), function_returning_a_value:solution (-> +4)
    g = 1 # assignment, assignment_lhs_identifier:g, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:1 (-> +1), binary_operator:Add, for:i (-> +1), for_range_start (-> +1), function_call:range, int_literal, literal:Num
        g = lcm(g, i) # assignment, assignment_lhs_identifier:g, assignment_rhs_identifier:g, assignment_rhs_identifier:i, assignment_rhs_identifier:lcm, call_parameter:g, call_parameter:i, function_call:lcm
    return g

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_a_value:solution (-> +7)
    suma = 0 # assignment, assignment_lhs_identifier:suma, int_literal, literal:Num
    sumb = 0 # assignment, assignment_lhs_identifier:sumb, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:1 (-> +2), binary_operator:Add, for:i (-> +2), for_range_start (-> +2), function_call:range, int_literal, literal:Num
        suma += i ** 2 # assignment_lhs_identifier:suma, assignment_rhs_identifier:i, augmented_assignment, binary_operator:Pow, int_literal, literal:Num
        sumb += i # assignment_lhs_identifier:sumb, assignment_rhs_identifier:i, augmented_assignment
    sum = sumb ** 2 - suma # assignment, assignment_lhs_identifier:sum, assignment_rhs_identifier:suma, assignment_rhs_identifier:sumb, binary_operator:Pow, binary_operator:Sub, int_literal, literal:Num
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +4), function_returning_a_value:solution (-> +4)
    suma = n * (n + 1) / 2 # assignment, assignment_lhs_identifier:suma, assignment_rhs_identifier:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, int_literal, literal:Num
    suma **= 2 # assignment_lhs_identifier:suma, augmented_assignment, int_literal, literal:Num
    sumb = n * (n + 1) * (2 * n + 1) / 6 # assignment, assignment_lhs_identifier:sumb, assignment_rhs_identifier:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, int_literal, literal:Num, suggest_constant_definition
    return int(suma - sumb) # binary_operator:Sub, function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol3.py
# ----------------------------------------------------------------------------------------
import math # import:math
def solution(n): # function:solution (-> +3), function_returning_a_value:solution (-> +3)
    sum_of_squares = sum([i * i for i in range(1, n + 1)]) # assignment, assignment_lhs_identifier:sum_of_squares, assignment_rhs_identifier:i, assignment_rhs_identifier:n, assignment_rhs_identifier:range, assignment_rhs_identifier:sum, binary_operator:Add, binary_operator:Mult, composition, comprehension:List, comprehension_for_count:1, function_call:range, function_call:sum, int_literal, literal:Num
    square_of_sum = int(math.pow(sum(range(1, n + 1)), 2)) # assignment, assignment_lhs_identifier:square_of_sum, assignment_rhs_identifier:int, assignment_rhs_identifier:math, assignment_rhs_identifier:n, assignment_rhs_identifier:range, assignment_rhs_identifier:sum, binary_operator:Add, composition, function_call:int, function_call:range, function_call:sum, int_literal, literal:Num, method_call:pow
    return square_of_sum - sum_of_squares # binary_operator:Sub

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +3), function_returning_a_value:solution (-> +3)
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6 # assignment, assignment_lhs_identifier:sum_of_squares, assignment_rhs_identifier:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, int_literal, literal:Num, suggest_constant_definition
    square_of_sum = (n * (n + 1) / 2) ** 2 # assignment, assignment_lhs_identifier:square_of_sum, assignment_rhs_identifier:n, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Pow, int_literal, literal:Num
    return int(square_of_sum - sum_of_squares) # binary_operator:Sub, function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import_from:math
def isprime(n): # function:isprime (-> +10), function_returning_a_value:isprime (-> +10)
    if n == 2: # comparison_operator:Eq, if (-> +8), int_literal, literal:Num
        return True # if_then_branch, literal:True
    elif n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +6), int_literal, literal:Num
        return False # if_elif_branch, literal:False
    else:
        sq = int(sqrt(n)) + 1 # assignment, assignment_lhs_identifier:sq, assignment_rhs_identifier:int, assignment_rhs_identifier:n, assignment_rhs_identifier:sqrt, binary_operator:Add, call_parameter:n, composition, function_call:int, function_call:sqrt, if_else_branch (-> +3), int_literal, literal:Num
        for i in range(3, sq, 2): # call_parameter:sq, for:i (-> +2), for_range_step:2 (-> +2), function_call:range, int_literal, literal:Num, suggest_constant_definition
            if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), int_literal, literal:Num, nested_if:1 (-> +1)
                return False # if_then_branch, literal:False
    return True # literal:True
def solution(n): # function:solution (-> +11), function_returning_a_value:solution (-> +11)
    i = 0 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    j = 1 # assignment, assignment_lhs_identifier:j, int_literal, literal:Num
    while i != n and j < 3: # boolean_operator:And, comparison_operator:Lt, comparison_operator:NotEq, evolve_state (-> +3), int_literal, literal:Num, suggest_constant_definition, while (-> +3)
        j += 1 # assignment_lhs_identifier:j, augmented_assignment, int_literal, literal:Num
        if isprime(j): # call_parameter:j, function_call:isprime, if (-> +1)
            i += 1 # assignment_lhs_identifier:i, augmented_assignment, if_then_branch, int_literal, literal:Num
    while i != n: # comparison_operator:NotEq, while (-> +3)
        j += 2 # assignment_lhs_identifier:j, augmented_assignment, int_literal, literal:Num
        if isprime(j): # call_parameter:j, function_call:isprime, if (-> +1)
            i += 1 # assignment_lhs_identifier:i, augmented_assignment, if_then_branch, int_literal, literal:Num
    return j

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol2.py
# ----------------------------------------------------------------------------------------
def isprime(number): # function:isprime (-> +4), function_returning_a_value:isprime (-> +4)
    for i in range(2, int(number ** 0.5) + 1): # binary_operator:Add, binary_operator:Pow, composition, float_literal, for:i (-> +2), for_range_start (-> +2), function_call:int, function_call:range, int_literal, literal:Num, suggest_constant_definition, universal_quantifier (-> +3)
        if number % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), int_literal, literal:Num
            return False # if_then_branch, literal:False
    return True # literal:True
def solution(n): # function:solution (-> +15), function_returning_a_value:solution (-> +15)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:int, assignment_rhs_identifier:n, call_parameter:n, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), int_literal, literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    primes = [] # assignment, assignment_lhs_identifier:primes, literal:List
    num = 2 # assignment, assignment_lhs_identifier:num, int_literal, literal:Num
    while len(primes) < n: # call_parameter:primes, comparison_operator:Lt, function_call:len, while (-> +5)
        if isprime(num): # call_parameter:num, function_call:isprime, if (-> +4)
            primes.append(num) # call_parameter:num, if_then_branch (-> +1), method_call:append, method_call_object:primes
            num += 1 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num
        else:
            num += 1 # assignment_lhs_identifier:num, augmented_assignment, if_else_branch, int_literal, literal:Num
    return primes[len(primes) - 1] # binary_operator:Sub, call_parameter:primes, function_call:len, index, index_arithmetic, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol3.py
# ----------------------------------------------------------------------------------------
import math # import:math
import itertools # import:itertools
def primeCheck(number): # function:primeCheck (-> +3), function_returning_a_value:primeCheck (-> +3)
    if number % 2 == 0 and number > 2: # binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, divisibility_test:2, if (-> +1), int_literal, literal:Num
        return False # if_then_branch, literal:False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # binary_operator:Add, binary_operator:Mod, call_parameter:number, composition, comprehension:Generator, comprehension_for_count:1, function_call:all, function_call:int, function_call:range, int_literal, literal:Num, method_call:sqrt, suggest_constant_definition
def prime_generator(): # function:prime_generator (-> +5), generator:prime_generator (-> +5), procedure:prime_generator (-> +5)
    num = 2 # assignment, assignment_lhs_identifier:num, int_literal, literal:Num
    while True: # literal:True, while (-> +3)
        if primeCheck(num): # call_parameter:num, function_call:primeCheck, if (-> +1)
            yield num # if_then_branch
        num += 1 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num
def solution(n): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return next(itertools.islice(prime_generator(), n - 1, n)) # binary_operator:Sub, call_parameter:n, composition, function_call:next, function_call:prime_generator, int_literal, literal:Num, method_call:islice

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol1.py
# ----------------------------------------------------------------------------------------
import sys # import:sys
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
def solution(n): # function:solution (-> +8), function_returning_a_value:solution (-> +8)
    LargestProduct = -sys.maxsize - 1 # assignment, assignment_lhs_identifier:LargestProduct, assignment_rhs_identifier:sys, binary_operator:Sub, int_literal, literal:Num, unary_operator:USub
    for i in range(len(n) - 12): # accumulate_elements:1 (-> +5), binary_operator:Sub, call_parameter:n, composition, for:i (-> +5), for_range_stop (-> +5), function_call:len, function_call:range, int_literal, literal:Num, suggest_constant_definition
        product = 1 # assignment, assignment_lhs_identifier:product, int_literal, literal:Num
        for j in range(13): # accumulate_elements:1 (-> +1), for:j (-> +1), for_range_stop (-> +1), function_call:range, int_literal, literal:Num, nested_for:1 (-> +1), suggest_constant_definition
            product *= int(n[i + j]) # assignment_lhs_identifier:product, assignment_rhs_identifier:i, assignment_rhs_identifier:int, assignment_rhs_identifier:j, assignment_rhs_identifier:n, augmented_assignment, binary_operator:Add, function_call:int, index, index_arithmetic
        if product > LargestProduct: # comparison_operator:Gt, if (-> +1)
            LargestProduct = product # assignment, assignment_lhs_identifier:LargestProduct, assignment_rhs_identifier:product, if_then_branch
    return LargestProduct

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol2.py
# ----------------------------------------------------------------------------------------
from functools import reduce # import_from:functools
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
def solution(n): # function:solution (-> +4), function_returning_a_value:solution (-> +4)
    return max( # composition, function_call:max
        [
            reduce(lambda x, y: int(x) * int(y), n[i : i + 13]) # binary_operator:Add, binary_operator:Mult, call_parameter:x, call_parameter:y, composition, comprehension:List, comprehension_for_count:1, function_call:int, function_call:reduce, int_literal, lambda_function, literal:Num, slice, suggest_constant_definition
            for i in range(len(n) - 12) # binary_operator:Sub, call_parameter:n, composition, function_call:len, function_call:range, int_literal, literal:Num, suggest_constant_definition
        ]
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol3.py
# ----------------------------------------------------------------------------------------
import sys # import:sys
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
def streval(s: str) -> int: # function:streval, function_returning_a_value:streval
    ret = 1 # assignment, assignment_lhs_identifier:ret, int_literal, literal:Num
    for it in s: # accumulate_elements:1 (-> +1), for:it (-> +1), for_each (-> +1)
        ret *= int(it) # assignment_lhs_identifier:ret, assignment_rhs_identifier:int, assignment_rhs_identifier:it, augmented_assignment, call_parameter:it, function_call:int
    return ret
def solution(n: str) -> int: # function:solution, function_returning_a_value:solution
    LargestProduct = -sys.maxsize - 1 # assignment, assignment_lhs_identifier:LargestProduct, assignment_rhs_identifier:sys, binary_operator:Sub, int_literal, literal:Num, unary_operator:USub
    substr = n[:13] # assignment, assignment_lhs_identifier:substr, assignment_rhs_identifier:n, int_literal, literal:Num, slice, suggest_constant_definition
    cur_index = 13 # assignment, assignment_lhs_identifier:cur_index, int_literal, literal:Num, suggest_constant_definition
    while cur_index < len(n) - 13: # binary_operator:Sub, call_parameter:n, comparison_operator:Lt, function_call:len, int_literal, literal:Num, suggest_constant_definition, while (-> +7)
        if int(n[cur_index]) >= int(substr[0]): # comparison_operator:GtE, function_call:int, if (-> +6), index, int_literal, literal:Num
            substr = substr[1:] + n[cur_index] # assignment, assignment_lhs_identifier:substr, assignment_rhs_identifier:cur_index, assignment_rhs_identifier:n, assignment_rhs_identifier:substr, binary_operator:Add, if_then_branch (-> +1), index, int_literal, literal:Num, slice
            cur_index += 1 # assignment_lhs_identifier:cur_index, augmented_assignment, int_literal, literal:Num
        else:
            LargestProduct = max(LargestProduct, streval(substr)) # assignment, assignment_lhs_identifier:LargestProduct, assignment_rhs_identifier:LargestProduct, assignment_rhs_identifier:max, assignment_rhs_identifier:streval, assignment_rhs_identifier:substr, call_parameter:LargestProduct, call_parameter:substr, composition, function_call:max, function_call:streval, if_else_branch (-> +2)
            substr = n[cur_index : cur_index + 13] # assignment, assignment_lhs_identifier:substr, assignment_rhs_identifier:cur_index, assignment_rhs_identifier:n, binary_operator:Add, int_literal, literal:Num, slice, suggest_constant_definition
            cur_index += 13 # assignment_lhs_identifier:cur_index, augmented_assignment, int_literal, literal:Num, suggest_constant_definition
    return LargestProduct

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +7), function_returning_a_value:solution (-> +7)
    for a in range(300): # for:a (-> +6), for_range_stop (-> +6), function_call:range, int_literal, literal:Num, suggest_constant_definition
        for b in range(400): # for:b (-> +5), for_range_stop (-> +5), function_call:range, int_literal, literal:Num, nested_for:1 (-> +5), suggest_constant_definition
            for c in range(500): # for:c (-> +4), for_range_stop (-> +4), function_call:range, int_literal, literal:Num, nested_for:2 (-> +4), suggest_constant_definition
                if a < b < c: # chained_comparison:2, comparison_operator:Lt, if (-> +3)
                    if (a ** 2) + (b ** 2) == (c ** 2): # binary_operator:Add, binary_operator:Pow, comparison_operator:Eq, if (-> +2), if_then_branch (-> +2), int_literal, literal:Num, nested_if:1 (-> +2)
                        if (a + b + c) == 1000: # binary_operator:Add, comparison_operator:Eq, if (-> +1), if_then_branch (-> +1), int_literal, literal:Num, nested_if:2 (-> +1), suggest_constant_definition
                            return a * b * c # binary_operator:Mult, if_then_branch

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +10), function_returning_a_value:solution (-> +10)
    product = -1 # assignment, assignment_lhs_identifier:product, int_literal, literal:Num
    d = 0 # assignment, assignment_lhs_identifier:d, int_literal, literal:Num
    for a in range(1, n // 3): # binary_operator:FloorDiv, for:a (-> +6), for_range_start (-> +6), function_call:range, int_literal, literal:Num, suggest_constant_definition
        b = (n * n - 2 * a * n) // (2 * n - 2 * a) # assignment, assignment_lhs_identifier:b, assignment_rhs_identifier:a, assignment_rhs_identifier:n, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num
        c = n - a - b # assignment, assignment_lhs_identifier:c, assignment_rhs_identifier:a, assignment_rhs_identifier:b, assignment_rhs_identifier:n, binary_operator:Sub
        if c * c == (a * a + b * b): # binary_operator:Add, binary_operator:Mult, comparison_operator:Eq, if (-> +3)
            d = a * b * c # assignment, assignment_lhs_identifier:d, assignment_rhs_identifier:a, assignment_rhs_identifier:b, assignment_rhs_identifier:c, binary_operator:Mult, if_then_branch (-> +2)
            if d >= product: # comparison_operator:GtE, if (-> +1), nested_if:1 (-> +1)
                product = d # assignment, assignment_lhs_identifier:product, assignment_rhs_identifier:d, if_then_branch
    return product

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol3.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +7), function_returning_a_value:solution (-> +7)
    return [
        a * b * c # binary_operator:Mult, comprehension:List, comprehension_for_count:3, index
        for a in range(1, 999) # function_call:range, int_literal, literal:Num, suggest_constant_definition
        for b in range(a, 999) # call_parameter:a, function_call:range, int_literal, literal:Num, suggest_constant_definition
        for c in range(b, 999) # call_parameter:b, function_call:range, int_literal, literal:Num, suggest_constant_definition
        if (a * a + b * b == c * c) and (a + b + c == 1000) # binary_operator:Add, binary_operator:Mult, boolean_operator:And, comparison_operator:Eq, filtered_comprehension, int_literal, literal:Num, suggest_constant_definition
    ][0] # int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import_from:math
def is_prime(n): # function:is_prime (-> +4), function_returning_a_value:is_prime (-> +4)
    for i in range(2, int(sqrt(n)) + 1): # binary_operator:Add, call_parameter:n, composition, for:i (-> +2), for_range_start (-> +2), function_call:int, function_call:range, function_call:sqrt, int_literal, literal:Num, universal_quantifier (-> +3)
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), int_literal, literal:Num
            return False # if_then_branch, literal:False
    return True # literal:True
def sum_of_primes(n): # function:sum_of_primes (-> +8), function_returning_a_value:sum_of_primes (-> +8)
    if n > 2: # comparison_operator:Gt, if (-> +3), int_literal, literal:Num
        sumOfPrimes = 2 # assignment, assignment_lhs_identifier:sumOfPrimes, if_then_branch, int_literal, literal:Num
    else:
        return 0 # if_else_branch, int_literal, literal:Num
    for i in range(3, n, 2): # accumulate_elements:1 (-> +2), call_parameter:n, for:i (-> +2), for_range_step:2 (-> +2), function_call:range, int_literal, literal:Num, suggest_constant_definition
        if is_prime(i): # call_parameter:i, function_call:is_prime, if (-> +1)
            sumOfPrimes += i # assignment_lhs_identifier:sumOfPrimes, assignment_rhs_identifier:i, augmented_assignment, if_then_branch
    return sumOfPrimes
def solution(n): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return sum_of_primes(n) # call_parameter:n, function_call:sum_of_primes

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol2.py
# ----------------------------------------------------------------------------------------
import math # import:math
from itertools import takewhile # import_from:itertools
def primeCheck(number): # function:primeCheck (-> +3), function_returning_a_value:primeCheck (-> +3)
    if number % 2 == 0 and number > 2: # binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, divisibility_test:2, if (-> +1), int_literal, literal:Num
        return False # if_then_branch, literal:False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # binary_operator:Add, binary_operator:Mod, call_parameter:number, composition, comprehension:Generator, comprehension_for_count:1, function_call:all, function_call:int, function_call:range, int_literal, literal:Num, method_call:sqrt, suggest_constant_definition
def prime_generator(): # function:prime_generator (-> +5), generator:prime_generator (-> +5), procedure:prime_generator (-> +5)
    num = 2 # assignment, assignment_lhs_identifier:num, int_literal, literal:Num
    while True: # literal:True, while (-> +3)
        if primeCheck(num): # call_parameter:num, function_call:primeCheck, if (-> +1)
            yield num # if_then_branch
        num += 1 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num
def solution(n): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return sum(takewhile(lambda x: x < n, prime_generator())) # comparison_operator:Lt, composition, function_call:prime_generator, function_call:sum, function_call:takewhile, lambda_function

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol3.py
# ----------------------------------------------------------------------------------------
def prime_sum(n: int) -> int: # function:prime_sum, function_returning_a_value:prime_sum
    list_ = [0 for i in range(n + 1)] # assignment, assignment_lhs_identifier:list_, assignment_rhs_identifier:i, assignment_rhs_identifier:n, assignment_rhs_identifier:range, binary_operator:Add, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num
    list_[0] = 1 # assignment, assignment_lhs_identifier:list_, index, int_literal, literal:Num
    list_[1] = 1 # assignment, assignment_lhs_identifier:list_, index, int_literal, literal:Num
    for i in range(2, int(n ** 0.5) + 1): # binary_operator:Add, binary_operator:Pow, composition, float_literal, for:i (-> +3), for_range_start (-> +3), function_call:int, function_call:range, int_literal, literal:Num, suggest_constant_definition
        if list_[i] == 0: # comparison_operator:Eq, if (-> +2), index, int_literal, literal:Num
            for j in range(i * i, n + 1, i): # binary_operator:Add, binary_operator:Mult, call_parameter:i, for:j (-> +1), for_range_step (-> +1), function_call:range, if_then_branch (-> +1), int_literal, literal:Num, nested_for:1 (-> +1)
                list_[j] = 1 # assignment, assignment_lhs_identifier:list_, index, int_literal, literal:Num
    s = 0 # assignment, assignment_lhs_identifier:s, int_literal, literal:Num
    for i in range(n): # accumulate_elements:1 (-> +2), call_parameter:n, for:i (-> +2), for_range_stop (-> +2), function_call:range
        if list_[i] == 0: # comparison_operator:Eq, if (-> +1), index, int_literal, literal:Num
            s += i # assignment_lhs_identifier:s, assignment_rhs_identifier:i, augmented_assignment, if_then_branch
    return s

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_11/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os
def largest_product(grid): # function:largest_product (-> +27), function_returning_a_value:largest_product (-> +27)
    nColumns = len(grid[0]) # assignment, assignment_lhs_identifier:nColumns, assignment_rhs_identifier:grid, assignment_rhs_identifier:len, function_call:len, index, int_literal, literal:Num
    nRows = len(grid) # assignment, assignment_lhs_identifier:nRows, assignment_rhs_identifier:grid, assignment_rhs_identifier:len, call_parameter:grid, function_call:len
    largest = 0 # assignment, assignment_lhs_identifier:largest, int_literal, literal:Num
    lrDiagProduct = 0 # assignment, assignment_lhs_identifier:lrDiagProduct, int_literal, literal:Num
    rlDiagProduct = 0 # assignment, assignment_lhs_identifier:rlDiagProduct, int_literal, literal:Num
    for i in range(nColumns): # call_parameter:nColumns, for:i (-> +20), for_range_stop (-> +20), function_call:range
        for j in range(nRows - 3): # binary_operator:Sub, for:j (-> +19), for_range_stop (-> +19), function_call:range, int_literal, literal:Num, nested_for:1 (-> +19), suggest_constant_definition
            vertProduct = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i] # assignment, assignment_lhs_identifier:vertProduct, assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
            horzProduct = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3] # assignment, assignment_lhs_identifier:horzProduct, assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
            if i < nColumns - 3: # binary_operator:Sub, comparison_operator:Lt, if (-> +5), int_literal, literal:Num, suggest_constant_definition
                lrDiagProduct = ( # assignment, assignment_lhs_identifier:lrDiagProduct, if_then_branch (-> +4)
                    grid[i][j] # assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Mult, index
                    * grid[i + 1][j + 1] # assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Add, index, index_arithmetic, int_literal, literal:Num
                    * grid[i + 2][j + 2] # assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num
                    * grid[i + 3][j + 3] # assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                )
            if i > 2: # comparison_operator:Gt, if (-> +5), int_literal, literal:Num
                rlDiagProduct = ( # assignment, assignment_lhs_identifier:rlDiagProduct, if_then_branch (-> +4)
                    grid[i][j] # assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Mult, index
                    * grid[i - 1][j + 1] # assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Add, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num
                    * grid[i - 2][j + 2] # assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num
                    * grid[i - 3][j + 3] # assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                )
            maxProduct = max(vertProduct, horzProduct, lrDiagProduct, rlDiagProduct) # assignment, assignment_lhs_identifier:maxProduct, assignment_rhs_identifier:horzProduct, assignment_rhs_identifier:lrDiagProduct, assignment_rhs_identifier:max, assignment_rhs_identifier:rlDiagProduct, assignment_rhs_identifier:vertProduct, call_parameter:horzProduct, call_parameter:lrDiagProduct, call_parameter:rlDiagProduct, call_parameter:vertProduct, function_call:max
            if maxProduct > largest: # comparison_operator:Gt, if (-> +1)
                largest = maxProduct # assignment, assignment_lhs_identifier:largest, assignment_rhs_identifier:maxProduct, if_then_branch
    return largest
def solution(): # function:solution (-> +6), function_returning_a_value:solution (-> +6)
    grid = [] # assignment, assignment_lhs_identifier:grid, literal:List
    with open(os.path.dirname(__file__) + "/grid.txt") as file: # binary_operator:Add, call_parameter:__file__, composition, function_call:open, literal:Str, method_call:dirname
        for line in file: # for:line (-> +1), for_each (-> +1)
            grid.append(line.strip("\n").split(" ")) # composition, literal:Str, method_call:append, method_call:split, method_call:strip, method_call_object:grid, method_call_object:line, method_chaining
    grid = [[int(i) for i in grid[j]] for j in range(len(grid))] # assignment, assignment_lhs_identifier:grid, assignment_rhs_identifier:grid, assignment_rhs_identifier:i, assignment_rhs_identifier:int, assignment_rhs_identifier:j, assignment_rhs_identifier:len, assignment_rhs_identifier:range, call_parameter:grid, call_parameter:i, composition, comprehension:List, comprehension_for_count:1, function_call:int, function_call:len, function_call:range, index
    return largest_product(grid) # call_parameter:grid, function_call:largest_product

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_11/sol2.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +26), function_returning_a_value:solution (-> +26)
    with open(os.path.dirname(__file__) + "/grid.txt") as f: # binary_operator:Add, call_parameter:__file__, composition, function_call:open, literal:Str, method_call:dirname
        l = [] # assignment, assignment_lhs_identifier:l, literal:List
        for i in range(20): # for:i (-> +1), for_range_stop (-> +1), function_call:range, int_literal, literal:Num, suggest_constant_definition
            l.append([int(x) for x in f.readline().split()]) # call_parameter:x, composition, comprehension:List, comprehension_for_count:1, function_call:int, method_call:append, method_call:readline, method_call:split, method_call_object:f, method_call_object:l, method_chaining
        maximum = 0 # assignment, assignment_lhs_identifier:maximum, int_literal, literal:Num
        for i in range(20): # for:i (-> +4), for_range_stop (-> +4), function_call:range, int_literal, literal:Num, suggest_constant_definition
            for j in range(17): # for:j (-> +3), for_range_stop (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), suggest_constant_definition
                temp = l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3] # assignment, assignment_lhs_identifier:temp, assignment_rhs_identifier:i, assignment_rhs_identifier:j, assignment_rhs_identifier:l, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1)
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_identifier:temp, if_then_branch
        for i in range(17): # for:i (-> +4), for_range_stop (-> +4), function_call:range, int_literal, literal:Num, suggest_constant_definition
            for j in range(20): # for:j (-> +3), for_range_stop (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), suggest_constant_definition
                temp = l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j] # assignment, assignment_lhs_identifier:temp, assignment_rhs_identifier:i, assignment_rhs_identifier:j, assignment_rhs_identifier:l, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1)
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_identifier:temp, if_then_branch
        for i in range(17): # for:i (-> +4), for_range_stop (-> +4), function_call:range, int_literal, literal:Num, square_nested_for (-> +4), suggest_constant_definition
            for j in range(17): # for:j (-> +3), for_range_stop (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), suggest_constant_definition
                temp = l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3] # assignment, assignment_lhs_identifier:temp, assignment_rhs_identifier:i, assignment_rhs_identifier:j, assignment_rhs_identifier:l, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1)
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_identifier:temp, if_then_branch
        for i in range(17): # for:i (-> +4), for_range_stop (-> +4), function_call:range, int_literal, literal:Num, suggest_constant_definition
            for j in range(3, 20): # for:j (-> +3), for_range_start (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3), suggest_constant_definition
                temp = l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3] # assignment, assignment_lhs_identifier:temp, assignment_rhs_identifier:i, assignment_rhs_identifier:j, assignment_rhs_identifier:l, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1)
                    maximum = temp # assignment, assignment_lhs_identifier:maximum, assignment_rhs_identifier:temp, if_then_branch
        return maximum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_12/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import_from:math
def count_divisors(n): # function:count_divisors (-> +7), function_returning_a_value:count_divisors (-> +7)
    nDivisors = 0 # assignment, assignment_lhs_identifier:nDivisors, int_literal, literal:Num
    for i in range(1, int(sqrt(n)) + 1): # binary_operator:Add, call_parameter:n, composition, for:i (-> +2), for_range_start (-> +2), function_call:int, function_call:range, function_call:sqrt, int_literal, literal:Num
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), int_literal, literal:Num
            nDivisors += 2 # assignment_lhs_identifier:nDivisors, augmented_assignment, if_then_branch, int_literal, literal:Num
    if n ** 0.5 == int(n ** 0.5): # binary_operator:Pow, comparison_operator:Eq, float_literal, function_call:int, if (-> +1), literal:Num, suggest_constant_definition
        nDivisors -= 1 # assignment_lhs_identifier:nDivisors, augmented_assignment, if_then_branch, int_literal, literal:Num
    return nDivisors
def solution(): # function:solution (-> +8), function_returning_a_value:solution (-> +8)
    tNum = 1 # assignment, assignment_lhs_identifier:tNum, int_literal, literal:Num
    i = 1 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    while True: # literal:True, while (-> +4)
        i += 1 # assignment_lhs_identifier:i, augmented_assignment, int_literal, literal:Num
        tNum += i # assignment_lhs_identifier:tNum, assignment_rhs_identifier:i, augmented_assignment
        if count_divisors(tNum) > 500: # call_parameter:tNum, comparison_operator:Gt, function_call:count_divisors, if (-> +1), int_literal, literal:Num, suggest_constant_definition
            break # if_then_branch
    return tNum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_12/sol2.py
# ----------------------------------------------------------------------------------------
def triangle_number_generator(): # function:triangle_number_generator (-> +2), generator:triangle_number_generator (-> +2), procedure:triangle_number_generator (-> +2)
    for n in range(1, 1000000): # for:n (-> +1), for_range_start (-> +1), function_call:range, int_literal, literal:Num, suggest_constant_definition
        yield n * (n + 1) // 2 # binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, int_literal, literal:Num
def count_divisors(n): # function:count_divisors (-> +1), function_returning_a_value:count_divisors (-> +1)
    return sum([2 for i in range(1, int(n ** 0.5) + 1) if n % i == 0 and i * i != n]) # binary_operator:Add, binary_operator:Mod, binary_operator:Mult, binary_operator:Pow, boolean_operator:And, comparison_operator:Eq, comparison_operator:NotEq, composition, comprehension:List, comprehension_for_count:1, divisibility_test, filtered_comprehension, float_literal, function_call:int, function_call:range, function_call:sum, int_literal, literal:Num, suggest_constant_definition
def solution(): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return next(i for i in triangle_number_generator() if count_divisors(i) > 500) # call_parameter:i, comparison_operator:Gt, composition, comprehension:Generator, comprehension_for_count:1, filtered_comprehension, function_call:count_divisors, function_call:next, function_call:triangle_number_generator, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_13/sol1.py
# ----------------------------------------------------------------------------------------
def solution(array): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return str(sum(array))[:10] # call_parameter:array, composition, function_call:str, function_call:sum, int_literal, literal:Num, slice, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_14/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +16), function_returning_a_value:solution (-> +16)
    largest_number = 0 # assignment, assignment_lhs_identifier:largest_number, int_literal, literal:Num
    pre_counter = 0 # assignment, assignment_lhs_identifier:pre_counter, int_literal, literal:Num
    for input1 in range(n): # call_parameter:n, for:input1 (-> +12), for_range_stop (-> +12), function_call:range
        counter = 1 # assignment, assignment_lhs_identifier:counter, int_literal, literal:Num
        number = input1 # assignment, assignment_lhs_identifier:number, assignment_rhs_identifier:input1
        while number > 1: # comparison_operator:Gt, evolve_state (-> +6), int_literal, literal:Num, while (-> +6)
            if number % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +5), int_literal, literal:Num
                number /= 2 # assignment_lhs_identifier:number, augmented_assignment, if_then_branch (-> +1), int_literal, literal:Num
                counter += 1 # assignment_lhs_identifier:counter, augmented_assignment, int_literal, literal:Num
            else:
                number = (3 * number) + 1 # assignment, assignment_lhs_identifier:number, assignment_rhs_identifier:number, binary_operator:Add, binary_operator:Mult, if_else_branch (-> +1), int_literal, literal:Num, suggest_constant_definition
                counter += 1 # assignment_lhs_identifier:counter, augmented_assignment, int_literal, literal:Num
        if counter > pre_counter: # comparison_operator:Gt, if (-> +2)
            largest_number = input1 # assignment, assignment_lhs_identifier:largest_number, assignment_rhs_identifier:input1, if_then_branch (-> +1)
            pre_counter = counter # assignment, assignment_lhs_identifier:pre_counter, assignment_rhs_identifier:counter
    return {"counter": pre_counter, "largest_number": largest_number} # literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_14/sol2.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function:collatz_sequence (-> +8), function_returning_a_value:collatz_sequence (-> +8)
    sequence = [n] # assignment, assignment_lhs_identifier:sequence, assignment_rhs_identifier:n
    while n != 1: # comparison_operator:NotEq, evolve_state (-> +5), int_literal, literal:Num, while (-> +5)
        if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), int_literal, literal:Num
            n //= 2 # assignment_lhs_identifier:n, augmented_assignment, if_then_branch, int_literal, literal:Num
        else:
            n = 3 * n + 1 # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:n, binary_operator:Add, binary_operator:Mult, if_else_branch, int_literal, literal:Num, suggest_constant_definition
        sequence.append(n) # call_parameter:n, method_call:append, method_call_object:sequence
    return sequence
def solution(n): # function:solution (-> +2), function_returning_a_value:solution (-> +2)
    result = max([(len(collatz_sequence(i)), i) for i in range(1, n)]) # assignment, assignment_lhs_identifier:result, assignment_rhs_identifier:collatz_sequence, assignment_rhs_identifier:i, assignment_rhs_identifier:len, assignment_rhs_identifier:max, assignment_rhs_identifier:n, assignment_rhs_identifier:range, call_parameter:i, call_parameter:n, composition, comprehension:List, comprehension_for_count:1, function_call:collatz_sequence, function_call:len, function_call:max, function_call:range, int_literal, literal:Num
    return {"counter": result[0], "largest_number": result[1]} # index, int_literal, literal:Num, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_15/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial # import_from:math
def lattice_paths(n): # function:lattice_paths (-> +3), function_returning_a_value:lattice_paths (-> +3)
    n = 2 * n # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:n, binary_operator:Mult, int_literal, literal:Num
    k = n / 2 # assignment, assignment_lhs_identifier:k, assignment_rhs_identifier:n, binary_operator:Div, int_literal, literal:Num
    return int(factorial(n) / (factorial(k) * factorial(n - k))) # binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_parameter:k, call_parameter:n, composition, function_call:factorial, function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_16/sol1.py
# ----------------------------------------------------------------------------------------
def solution(power): # function:solution (-> +7), function_returning_a_value:solution (-> +7)
    num = 2 ** power # assignment, assignment_lhs_identifier:num, assignment_rhs_identifier:power, binary_operator:Pow, int_literal, literal:Num
    string_num = str(num) # assignment, assignment_lhs_identifier:string_num, assignment_rhs_identifier:num, assignment_rhs_identifier:str, call_parameter:num, function_call:str
    list_num = list(string_num) # assignment, assignment_lhs_identifier:list_num, assignment_rhs_identifier:list, assignment_rhs_identifier:string_num, call_parameter:string_num, function_call:list
    sum_of_num = 0 # assignment, assignment_lhs_identifier:sum_of_num, int_literal, literal:Num
    for i in list_num: # accumulate_elements:1 (-> +1), for:i (-> +1), for_each (-> +1)
        sum_of_num += int(i) # assignment_lhs_identifier:sum_of_num, assignment_rhs_identifier:i, assignment_rhs_identifier:int, augmented_assignment, call_parameter:i, function_call:int
    return sum_of_num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_16/sol2.py
# ----------------------------------------------------------------------------------------
def solution(power): # function:solution (-> +5), function_returning_a_value:solution (-> +5)
    n = 2 ** power # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:power, binary_operator:Pow, int_literal, literal:Num
    r = 0 # assignment, assignment_lhs_identifier:r, int_literal, literal:Num
    while n: # while (-> +1)
        r, n = r + n % 10, n // 10 # assignment, assignment_lhs_identifier:n, assignment_lhs_identifier:r, assignment_rhs_identifier:n, assignment_rhs_identifier:r, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mod, int_literal, literal:Num, suggest_constant_definition
    return r

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_17/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +17), function_returning_a_value:solution (-> +17)
    ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # assignment, assignment_lhs_identifier:ones_counts, int_literal, literal:List, literal:Num, suggest_constant_definition
    tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6] # assignment, assignment_lhs_identifier:tens_counts, int_literal, literal:List, literal:Num, suggest_constant_definition
    count = 0 # assignment, assignment_lhs_identifier:count, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:1 (-> +12), binary_operator:Add, for:i (-> +12), for_range_start (-> +12), function_call:range, int_literal, literal:Num
        if i < 1000: # comparison_operator:Lt, if (-> +11), int_literal, literal:Num, suggest_constant_definition
            if i >= 100: # comparison_operator:GtE, if (-> +3), if_then_branch (-> +8), int_literal, literal:Num, nested_if:1 (-> +3), suggest_constant_definition
                count += ones_counts[i // 100] + 7 # assignment_lhs_identifier:count, assignment_rhs_identifier:i, assignment_rhs_identifier:ones_counts, augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, if_then_branch (-> +2), index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                if i % 100 != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test:100, if (-> +1), int_literal, literal:Num, nested_if:2 (-> +1), suggest_constant_definition
                    count += 3 # assignment_lhs_identifier:count, augmented_assignment, if_then_branch, int_literal, literal:Num, suggest_constant_definition
            if 0 < i % 100 < 20: # binary_operator:Mod, chained_comparison:2, comparison_operator:Lt, if (-> +4), int_literal, literal:Num, nested_if:1 (-> +4), suggest_constant_definition
                count += ones_counts[i % 100] # assignment_lhs_identifier:count, assignment_rhs_identifier:i, assignment_rhs_identifier:ones_counts, augmented_assignment, binary_operator:Mod, if_then_branch, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
            else:
                count += ones_counts[i % 10] # assignment_lhs_identifier:count, assignment_rhs_identifier:i, assignment_rhs_identifier:ones_counts, augmented_assignment, binary_operator:Mod, if_else_branch (-> +1), index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
                count += tens_counts[(i % 100 - i % 10) // 10] # assignment_lhs_identifier:count, assignment_rhs_identifier:i, assignment_rhs_identifier:tens_counts, augmented_assignment, binary_operator:FloorDiv, binary_operator:Mod, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
        else:
            count += ones_counts[i // 1000] + 8 # assignment_lhs_identifier:count, assignment_rhs_identifier:i, assignment_rhs_identifier:ones_counts, augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, if_else_branch, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
    return count

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_18/solution.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +17), function_returning_a_value:solution (-> +17)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, assignment_lhs_identifier:script_dir, assignment_rhs_identifier:__file__, assignment_rhs_identifier:os, call_parameter:__file__, composition, method_call:dirname, method_call:realpath
    triangle = os.path.join(script_dir, "triangle.txt") # assignment, assignment_lhs_identifier:triangle, assignment_rhs_identifier:os, assignment_rhs_identifier:script_dir, call_parameter:script_dir, literal:Str, method_call:join
    with open(triangle, "r") as f: # call_parameter:triangle, function_call:open, literal:Str
        triangle = f.readlines() # assignment, assignment_lhs_identifier:triangle, assignment_rhs_identifier:f, method_call:readlines
    a = [[int(y) for y in x.rstrip("\r\n").split(" ")] for x in triangle] # assignment, assignment_lhs_identifier:a, assignment_rhs_identifier:int, assignment_rhs_identifier:triangle, assignment_rhs_identifier:x, assignment_rhs_identifier:y, call_parameter:y, comprehension:List, comprehension_for_count:1, function_call:int, literal:Str, method_call:rstrip, method_call:split, method_call_object:x, method_chaining
    for i in range(1, len(a)): # call_parameter:a, composition, for:i (-> +10), for_range_start (-> +10), function_call:len, function_call:range, int_literal, literal:Num
        for j in range(len(a[i])): # composition, for:j (-> +9), for_indexes (-> +9), for_range_stop (-> +9), function_call:len, function_call:range, index, nested_for:1 (-> +9)
            if j != len(a[i - 1]): # binary_operator:Sub, comparison_operator:NotEq, function_call:len, if (-> +3), index, index_arithmetic, int_literal, literal:Num, suggest_conditional_expression (-> +3)
                number1 = a[i - 1][j] # assignment, assignment_lhs_identifier:number1, assignment_rhs_identifier:a, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
            else:
                number1 = 0 # assignment, assignment_lhs_identifier:number1, if_else_branch, int_literal, literal:Num
            if j > 0: # comparison_operator:Gt, if (-> +3), int_literal, literal:Num, suggest_conditional_expression (-> +3)
                number2 = a[i - 1][j - 1] # assignment, assignment_lhs_identifier:number2, assignment_rhs_identifier:a, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
            else:
                number2 = 0 # assignment, assignment_lhs_identifier:number2, if_else_branch, int_literal, literal:Num
            a[i][j] += max(number1, number2) # assignment_rhs_identifier:max, assignment_rhs_identifier:number1, assignment_rhs_identifier:number2, augmented_assignment, call_parameter:number1, call_parameter:number2, function_call:max, index
    return max(a[-1]) # function_call:max, index, int_literal, literal:Num, negative_index:-1

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_19/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +24), function_returning_a_value:solution (-> +24)
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # assignment, assignment_lhs_identifier:days_per_month, int_literal, literal:List, literal:Num, suggest_constant_definition
    day = 6 # assignment, assignment_lhs_identifier:day, int_literal, literal:Num, suggest_constant_definition
    month = 1 # assignment, assignment_lhs_identifier:month, int_literal, literal:Num
    year = 1901 # assignment, assignment_lhs_identifier:year, int_literal, literal:Num, suggest_constant_definition
    sundays = 0 # assignment, assignment_lhs_identifier:sundays, int_literal, literal:Num
    while year < 2001: # comparison_operator:Lt, evolve_state (-> +17), int_literal, literal:Num, suggest_constant_definition, while (-> +17)
        day += 7 # assignment_lhs_identifier:day, augmented_assignment, int_literal, literal:Num, suggest_constant_definition
        if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0): # binary_operator:Mod, boolean_operator:And, boolean_operator:Or, comparison_operator:Eq, divisibility_test:100, divisibility_test:4, divisibility_test:400, if (-> +10), int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
            if day > days_per_month[month - 1] and month != 2: # binary_operator:Sub, boolean_operator:And, comparison_operator:Gt, comparison_operator:NotEq, if (-> +5), if_then_branch (-> +5), index, index_arithmetic, int_literal, literal:Num, nested_if:1 (-> +5)
                month += 1 # assignment_lhs_identifier:month, augmented_assignment, if_then_branch (-> +1), int_literal, literal:Num
                day = day - days_per_month[month - 2] # assignment, assignment_lhs_identifier:day, assignment_rhs_identifier:day, assignment_rhs_identifier:days_per_month, assignment_rhs_identifier:month, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, suggest_augmented_assignment
            elif day > 29 and month == 2: # boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, if (-> +2), int_literal, literal:Num, nested_if:1 (-> +2), suggest_constant_definition
                month += 1 # assignment_lhs_identifier:month, augmented_assignment, if_elif_branch (-> +1), int_literal, literal:Num
                day = day - 29 # assignment, assignment_lhs_identifier:day, assignment_rhs_identifier:day, binary_operator:Sub, int_literal, literal:Num, suggest_augmented_assignment, suggest_constant_definition
        else:
            if day > days_per_month[month - 1]: # binary_operator:Sub, comparison_operator:Gt, if (-> +2), index, index_arithmetic, int_literal, literal:Num
                month += 1 # assignment_lhs_identifier:month, augmented_assignment, if_elif_branch (-> +1), int_literal, literal:Num
                day = day - days_per_month[month - 2] # assignment, assignment_lhs_identifier:day, assignment_rhs_identifier:day, assignment_rhs_identifier:days_per_month, assignment_rhs_identifier:month, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, suggest_augmented_assignment
        if month > 12: # comparison_operator:Gt, if (-> +2), int_literal, literal:Num, suggest_constant_definition
            year += 1 # assignment_lhs_identifier:year, augmented_assignment, if_then_branch (-> +1), int_literal, literal:Num
            month = 1 # assignment, assignment_lhs_identifier:month, int_literal, literal:Num
        if year < 2001 and day == 1: # boolean_operator:And, comparison_operator:Eq, comparison_operator:Lt, if (-> +1), int_literal, literal:Num, suggest_constant_definition
            sundays += 1 # assignment_lhs_identifier:sundays, augmented_assignment, if_then_branch, int_literal, literal:Num
    return sundays

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol1.py
# ----------------------------------------------------------------------------------------
def factorial(n): # function:factorial (-> +4), function_returning_a_value:factorial (-> +4)
    fact = 1 # assignment, assignment_lhs_identifier:fact, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:1 (-> +1), binary_operator:Add, for:i (-> +1), for_range_start (-> +1), function_call:range, int_literal, literal:Num
        fact *= i # assignment_lhs_identifier:fact, assignment_rhs_identifier:i, augmented_assignment
    return fact
def split_and_add(number): # function:split_and_add (-> +6), function_returning_a_value:split_and_add (-> +6)
    sum_of_digits = 0 # assignment, assignment_lhs_identifier:sum_of_digits, int_literal, literal:Num
    while number > 0: # comparison_operator:Gt, evolve_state (-> +3), int_literal, literal:Num, while (-> +3)
        last_digit = number % 10 # assignment, assignment_lhs_identifier:last_digit, assignment_rhs_identifier:number, binary_operator:Mod, int_literal, literal:Num, suggest_constant_definition
        sum_of_digits += last_digit # assignment_lhs_identifier:sum_of_digits, assignment_rhs_identifier:last_digit, augmented_assignment
        number = number // 10 # assignment, assignment_lhs_identifier:number, assignment_rhs_identifier:number, binary_operator:FloorDiv, int_literal, literal:Num, suggest_augmented_assignment, suggest_constant_definition
    return sum_of_digits
def solution(n): # function:solution (-> +3), function_returning_a_value:solution (-> +3)
    f = factorial(n) # assignment, assignment_lhs_identifier:f, assignment_rhs_identifier:factorial, assignment_rhs_identifier:n, call_parameter:n, function_call:factorial
    result = split_and_add(f) # assignment, assignment_lhs_identifier:result, assignment_rhs_identifier:f, assignment_rhs_identifier:split_and_add, call_parameter:f, function_call:split_and_add
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol2.py
# ----------------------------------------------------------------------------------------
from math import factorial # import_from:math
def solution(n): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return sum([int(x) for x in str(factorial(n))]) # call_parameter:n, call_parameter:x, composition, comprehension:List, comprehension_for_count:1, function_call:factorial, function_call:int, function_call:str, function_call:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol3.py
# ----------------------------------------------------------------------------------------
from math import factorial # import_from:math
def solution(n): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return sum(map(int, str(factorial(n)))) # call_parameter:int, call_parameter:n, composition, function_call:factorial, function_call:map, function_call:str, function_call:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7), function_returning_a_value:solution (-> +7)
    fact = 1 # assignment, assignment_lhs_identifier:fact, int_literal, literal:Num
    result = 0 # assignment, assignment_lhs_identifier:result, int_literal, literal:Num
    for i in range(1, n + 1): # accumulate_elements:1 (-> +1), binary_operator:Add, for:i (-> +1), for_range_start (-> +1), function_call:range, int_literal, literal:Num
        fact *= i # assignment_lhs_identifier:fact, assignment_rhs_identifier:i, augmented_assignment
    for j in str(fact): # accumulate_elements:1 (-> +1), call_parameter:fact, for:j (-> +1), function_call:str
        result += int(j) # assignment_lhs_identifier:result, assignment_rhs_identifier:int, assignment_rhs_identifier:j, augmented_assignment, call_parameter:j, function_call:int
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_21/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import_from:math
def sum_of_divisors(n): # function:sum_of_divisors (-> +7), function_returning_a_value:sum_of_divisors (-> +7)
    total = 0 # assignment, assignment_lhs_identifier:total, int_literal, literal:Num
    for i in range(1, int(sqrt(n) + 1)): # accumulate_elements:1 (-> +4), binary_operator:Add, call_parameter:n, composition, for:i (-> +4), for_range_start (-> +4), function_call:int, function_call:range, function_call:sqrt, int_literal, literal:Num
        if n % i == 0 and i != sqrt(n): # binary_operator:Mod, boolean_operator:And, call_parameter:n, comparison_operator:Eq, comparison_operator:NotEq, divisibility_test, function_call:sqrt, if (-> +3), int_literal, literal:Num
            total += i + n // i # assignment_lhs_identifier:total, assignment_rhs_identifier:i, assignment_rhs_identifier:n, augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, if_then_branch
        elif i == sqrt(n): # call_parameter:n, comparison_operator:Eq, function_call:sqrt, if (-> +1)
            total += i # assignment_lhs_identifier:total, assignment_rhs_identifier:i, augmented_assignment, if_elif_branch
    return total - n # binary_operator:Sub
def solution(n): # function:solution (-> +8), function_returning_a_value:solution (-> +8)
    total = sum( # assignment, assignment_lhs_identifier:total, assignment_rhs_identifier:sum, composition, function_call:sum
        [
            i # assignment_rhs_identifier:i, comprehension:List, comprehension_for_count:1
            for i in range(1, n) # assignment_rhs_identifier:i, assignment_rhs_identifier:n, assignment_rhs_identifier:range, call_parameter:n, function_call:range, int_literal, literal:Num
            if sum_of_divisors(sum_of_divisors(i)) == i and sum_of_divisors(i) != i # assignment_rhs_identifier:i, assignment_rhs_identifier:sum_of_divisors, boolean_operator:And, call_parameter:i, comparison_operator:Eq, comparison_operator:NotEq, composition, filtered_comprehension, function_call:sum_of_divisors
        ]
    )
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_22/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +12), function_returning_a_value:solution (-> +12)
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator:Add, call_parameter:__file__, composition, function_call:open, literal:Str, method_call:dirname
        names = str(file.readlines()[0]) # assignment, assignment_lhs_identifier:names, assignment_rhs_identifier:file, assignment_rhs_identifier:str, composition, function_call:str, index, int_literal, literal:Num, method_call:readlines, method_call_object:file
        names = names.replace('"', "").split(",") # assignment, assignment_lhs_identifier:names, assignment_rhs_identifier:names, literal:Str, method_call:replace, method_call:split, method_call_object:names, method_chaining
    names.sort() # method_call:sort, method_call_object:names
    name_score = 0 # assignment, assignment_lhs_identifier:name_score, int_literal, literal:Num
    total_score = 0 # assignment, assignment_lhs_identifier:total_score, int_literal, literal:Num
    for i, name in enumerate(names): # call_parameter:names, for:i:name (-> +4), for_indexes_elements (-> +4), function_call:enumerate
        for letter in name: # accumulate_elements:1 (-> +1), for:letter (-> +1), for_each (-> +1), nested_for:1 (-> +1)
            name_score += ord(letter) - 64 # assignment_lhs_identifier:name_score, assignment_rhs_identifier:letter, assignment_rhs_identifier:ord, augmented_assignment, binary_operator:Sub, call_parameter:letter, function_call:ord, int_literal, literal:Num, suggest_constant_definition
        total_score += (i + 1) * name_score # assignment_lhs_identifier:total_score, assignment_rhs_identifier:i, assignment_rhs_identifier:name_score, augmented_assignment, binary_operator:Add, binary_operator:Mult, int_literal, literal:Num
        name_score = 0 # assignment, assignment_lhs_identifier:name_score, int_literal, literal:Num
    return total_score

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_22/sol2.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +12), function_returning_a_value:solution (-> +12)
    total_sum = 0 # assignment, assignment_lhs_identifier:total_sum, int_literal, literal:Num
    temp_sum = 0 # assignment, assignment_lhs_identifier:temp_sum, int_literal, literal:Num
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator:Add, call_parameter:__file__, composition, function_call:open, literal:Str, method_call:dirname
        name = str(file.readlines()[0]) # assignment, assignment_lhs_identifier:name, assignment_rhs_identifier:file, assignment_rhs_identifier:str, composition, function_call:str, index, int_literal, literal:Num, method_call:readlines, method_call_object:file
        name = name.replace('"', "").split(",") # assignment, assignment_lhs_identifier:name, assignment_rhs_identifier:name, literal:Str, method_call:replace, method_call:split, method_call_object:name, method_chaining
    name.sort() # method_call:sort, method_call_object:name
    for i in range(len(name)): # accumulate_elements:1 (-> +4), call_parameter:name, composition, for:i (-> +4), for_indexes (-> +4), for_range_stop (-> +4), function_call:len, function_call:range
        for j in name[i]: # accumulate_elements:1 (-> +1), for:j (-> +1), index, nested_for:1 (-> +1)
            temp_sum += ord(j) - ord("A") + 1 # assignment_lhs_identifier:temp_sum, assignment_rhs_identifier:j, assignment_rhs_identifier:ord, augmented_assignment, binary_operator:Add, binary_operator:Sub, call_parameter:j, function_call:ord, int_literal, literal:Num, literal:Str
        total_sum += (i + 1) * temp_sum # assignment_lhs_identifier:total_sum, assignment_rhs_identifier:i, assignment_rhs_identifier:temp_sum, augmented_assignment, binary_operator:Add, binary_operator:Mult, int_literal, literal:Num
        temp_sum = 0 # assignment, assignment_lhs_identifier:temp_sum, int_literal, literal:Num
    return total_sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_23/sol1.py
# ----------------------------------------------------------------------------------------
def solution(limit=28123): # function:solution (-> +13), function_returning_a_value:solution (-> +13), function_with_default_positional_arguments:solution (-> +13), int_literal, literal:Num
    sumDivs = [1] * (limit + 1) # assignment, assignment_lhs_identifier:sumDivs, assignment_rhs_identifier:limit, binary_operator:Add, binary_operator:Mult, int_literal, literal:List, literal:Num
    for i in range(2, int(limit ** 0.5) + 1): # accumulate_elements:1 (-> +3), binary_operator:Add, binary_operator:Pow, composition, float_literal, for:i (-> +3), for_range_start (-> +3), function_call:int, function_call:range, int_literal, literal:Num, suggest_constant_definition
        sumDivs[i * i] += i # assignment_lhs_identifier:sumDivs, assignment_rhs_identifier:i, augmented_assignment, binary_operator:Mult, index, index_arithmetic
        for k in range(i + 1, limit // i + 1): # accumulate_elements:1 (-> +1), binary_operator:Add, binary_operator:FloorDiv, for:k (-> +1), for_range_start (-> +1), function_call:range, int_literal, literal:Num, nested_for:1 (-> +1)
            sumDivs[k * i] += k + i # assignment_lhs_identifier:sumDivs, assignment_rhs_identifier:i, assignment_rhs_identifier:k, augmented_assignment, binary_operator:Add, binary_operator:Mult, index, index_arithmetic
    abundants = set() # assignment, assignment_lhs_identifier:abundants, assignment_rhs_identifier:set, function_call:set
    res = 0 # assignment, assignment_lhs_identifier:res, int_literal, literal:Num
    for n in range(1, limit + 1): # accumulate_elements:2 (-> +4), binary_operator:Add, for:n (-> +4), for_range_start (-> +4), function_call:range, int_literal, literal:Num
        if sumDivs[n] > n: # comparison_operator:Gt, if (-> +1), index
            abundants.add(n) # call_parameter:n, if_then_branch, method_call:add, method_call_object:abundants
        if not any((n - a in abundants) for a in abundants): # binary_operator:Sub, comparison_operator:In, comprehension:Generator, comprehension_for_count:1, function_call:any, if (-> +1), unary_operator:Not
            res += n # assignment_lhs_identifier:res, assignment_rhs_identifier:n, augmented_assignment, if_then_branch
    return res

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_234/sol1.py
# ----------------------------------------------------------------------------------------
def fib(a, b, n): # function:fib (-> +13), function_returning_a_value:fib (-> +13)
    if n == 1: # comparison_operator:Eq, if (-> +5), int_literal, literal:Num
        return a # if_then_branch
    elif n == 2: # comparison_operator:Eq, if (-> +3), int_literal, literal:Num
        return b # if_elif_branch
    elif n == 3: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num, suggest_constant_definition
        return str(a) + str(b) # binary_operator:Add, call_parameter:a, call_parameter:b, function_call:str, if_elif_branch
    temp = 0 # assignment, assignment_lhs_identifier:temp, int_literal, literal:Num
    for x in range(2, n): # call_parameter:n, for:x (-> +4), for_range_start (-> +4), function_call:range, int_literal, literal:Num
        c = str(a) + str(b) # assignment, assignment_lhs_identifier:c, assignment_rhs_identifier:a, assignment_rhs_identifier:b, assignment_rhs_identifier:str, binary_operator:Add, call_parameter:a, call_parameter:b, function_call:str
        temp = b # assignment, assignment_lhs_identifier:temp, assignment_rhs_identifier:b
        b = c # assignment, assignment_lhs_identifier:b, assignment_rhs_identifier:c
        a = temp # assignment, assignment_lhs_identifier:a, assignment_rhs_identifier:temp
    return c
def solution(n): # function:solution (-> +11), function_returning_a_value:solution (-> +11)
    semidivisible = [] # assignment, assignment_lhs_identifier:semidivisible, literal:List
    for x in range(n): # call_parameter:n, for:x (-> +8), for_range_stop (-> +8), function_call:range
        l = [i for i in input().split()] # assignment, assignment_lhs_identifier:l, assignment_rhs_identifier:i, assignment_rhs_identifier:input, comprehension:List, comprehension_for_count:1, function_call:input, method_call:split
        c2 = 1 # assignment, assignment_lhs_identifier:c2, int_literal, literal:Num
        while 1: # int_literal, literal:Num, while (-> +4)
            if len(fib(l[0], l[1], c2)) < int(l[2]): # call_parameter:c2, comparison_operator:Lt, composition, function_call:fib, function_call:int, function_call:len, if (-> +3), index, int_literal, literal:Num
                c2 += 1 # assignment_lhs_identifier:c2, augmented_assignment, if_then_branch, int_literal, literal:Num
            else:
                break # if_else_branch
        semidivisible.append(fib(l[0], l[1], c2 + 1)[int(l[2]) - 1]) # binary_operator:Add, binary_operator:Sub, composition, function_call:fib, function_call:int, index, index_arithmetic, int_literal, literal:Num, method_call:append, method_call_object:semidivisible
    return semidivisible

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_24/sol1.py
# ----------------------------------------------------------------------------------------
from itertools import permutations # import_from:itertools
def solution(): # function:solution (-> +2), function_returning_a_value:solution (-> +2)
    result = list(map("".join, permutations("0123456789"))) # assignment, assignment_lhs_identifier:result, assignment_rhs_identifier:list, assignment_rhs_identifier:map, assignment_rhs_identifier:permutations, composition, function_call:list, function_call:map, function_call:permutations, literal:Str
    return result[999999] # index, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol1.py
# ----------------------------------------------------------------------------------------
def fibonacci(n): # function:fibonacci (-> +9), function_returning_a_value:fibonacci (-> +9)
    if n == 1 or type(n) is not int: # boolean_operator:Or, call_parameter:n, comparison_operator:Eq, comparison_operator:IsNot, function_call:type, if (-> +8), int_literal, literal:Num
        return 0 # if_then_branch, int_literal, literal:Num
    elif n == 2: # comparison_operator:Eq, if (-> +6), int_literal, literal:Num
        return 1 # if_elif_branch, int_literal, literal:Num
    else:
        sequence = [0, 1] # assignment, assignment_lhs_identifier:sequence, if_else_branch (-> +3), int_literal, literal:List, literal:Num
        for i in range(2, n + 1): # binary_operator:Add, for:i (-> +1), for_range_start (-> +1), function_call:range, int_literal, literal:Num
            sequence.append(sequence[i - 1] + sequence[i - 2]) # binary_operator:Add, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num, method_call:append, method_call_object:sequence
        return sequence[n] # index
def fibonacci_digits_index(n): # function:fibonacci_digits_index (-> +6), function_returning_a_value:fibonacci_digits_index (-> +6)
    digits = 0 # assignment, assignment_lhs_identifier:digits, int_literal, literal:Num
    index = 2 # assignment, assignment_lhs_identifier:index, int_literal, literal:Num
    while digits < n: # comparison_operator:Lt, while (-> +2)
        index += 1 # assignment_lhs_identifier:index, augmented_assignment, int_literal, literal:Num
        digits = len(str(fibonacci(index))) # assignment, assignment_lhs_identifier:digits, assignment_rhs_identifier:fibonacci, assignment_rhs_identifier:index, assignment_rhs_identifier:len, assignment_rhs_identifier:str, call_parameter:index, composition, function_call:fibonacci, function_call:len, function_call:str
    return index
def solution(n): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return fibonacci_digits_index(n) # call_parameter:n, function_call:fibonacci_digits_index

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol2.py
# ----------------------------------------------------------------------------------------
def fibonacci_generator(): # function:fibonacci_generator (-> +4), generator:fibonacci_generator (-> +4), procedure:fibonacci_generator (-> +4)
    a, b = 0, 1 # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, int_literal, literal:Num, literal:Tuple
    while True: # literal:True, while (-> +2)
        a, b = b, a + b # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_identifier:a, assignment_rhs_identifier:b, binary_operator:Add
        yield b
def solution(n): # function:solution (-> +5), function_returning_a_value:solution (-> +5)
    answer = 1 # assignment, assignment_lhs_identifier:answer, int_literal, literal:Num
    gen = fibonacci_generator() # assignment, assignment_lhs_identifier:gen, assignment_rhs_identifier:fibonacci_generator, function_call:fibonacci_generator
    while len(str(next(gen))) < n: # call_parameter:gen, comparison_operator:Lt, composition, function_call:len, function_call:next, function_call:str, while (-> +1)
        answer += 1 # assignment_lhs_identifier:answer, augmented_assignment, int_literal, literal:Num
    return answer + 1 # binary_operator:Add, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +12), function_returning_a_value:solution (-> +12)
    f1, f2 = 1, 1 # assignment, assignment_lhs_identifier:f1, assignment_lhs_identifier:f2, int_literal, literal:Num, literal:Tuple
    index = 2 # assignment, assignment_lhs_identifier:index, int_literal, literal:Num
    while True: # literal:True, while (-> +8)
        i = 0 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
        f = f1 + f2 # assignment, assignment_lhs_identifier:f, assignment_rhs_identifier:f1, assignment_rhs_identifier:f2, binary_operator:Add
        f1, f2 = f2, f # assignment, assignment_lhs_identifier:f1, assignment_lhs_identifier:f2, assignment_rhs_identifier:f, assignment_rhs_identifier:f2
        index += 1 # assignment_lhs_identifier:index, augmented_assignment, int_literal, literal:Num
        for j in str(f): # call_parameter:f, for:j (-> +1), function_call:str
            i += 1 # assignment_lhs_identifier:i, augmented_assignment, int_literal, literal:Num
        if i == n: # comparison_operator:Eq, if (-> +1)
            break # if_then_branch
    return index

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_27/problem_27_sol1.py
# ----------------------------------------------------------------------------------------
import math # import:math
def is_prime(k: int) -> bool: # function:is_prime, function_returning_a_value:is_prime
    if k < 2 or k % 2 == 0: # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, comparison_operator:Lt, divisibility_test:2, if (-> +7), int_literal, literal:Num
        return False # if_then_branch, literal:False
    elif k == 2: # comparison_operator:Eq, if (-> +5), int_literal, literal:Num
        return True # if_elif_branch, literal:True
    else:
        for x in range(3, int(math.sqrt(k) + 1), 2): # binary_operator:Add, call_parameter:k, composition, for:x (-> +2), for_range_step:2 (-> +2), function_call:int, function_call:range, if_else_branch (-> +2), int_literal, literal:Num, method_call:sqrt, suggest_constant_definition
            if k % x == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), int_literal, literal:Num, nested_if:1 (-> +1)
                return False # if_then_branch, literal:False
    return True # literal:True
def solution(a_limit: int, b_limit: int) -> int: # function:solution, function_returning_a_value:solution
    longest = [0, 0, 0] # assignment, assignment_lhs_identifier:longest, int_literal, literal:List, literal:Num
    for a in range((a_limit * -1) + 1, a_limit): # binary_operator:Add, binary_operator:Mult, call_parameter:a_limit, for:a (-> +9), for_range_start (-> +9), function_call:range, int_literal, literal:Num
        for b in range(2, b_limit): # call_parameter:b_limit, for:b (-> +8), for_range_start (-> +8), function_call:range, int_literal, literal:Num, nested_for:1 (-> +8)
            if is_prime(b): # call_parameter:b, function_call:is_prime, if (-> +7)
                count = 0 # assignment, assignment_lhs_identifier:count, if_then_branch (-> +6), int_literal, literal:Num
                n = 0 # assignment, assignment_lhs_identifier:n, int_literal, literal:Num
                while is_prime((n ** 2) + (a * n) + b): # binary_operator:Add, binary_operator:Mult, binary_operator:Pow, function_call:is_prime, int_literal, literal:Num, while (-> +2)
                    count += 1 # assignment_lhs_identifier:count, augmented_assignment, int_literal, literal:Num
                    n += 1 # assignment_lhs_identifier:n, augmented_assignment, int_literal, literal:Num
                if count > longest[0]: # comparison_operator:Gt, if (-> +1), index, int_literal, literal:Num, nested_if:1 (-> +1)
                    longest = [count, a, b] # assignment, assignment_lhs_identifier:longest, assignment_rhs_identifier:a, assignment_rhs_identifier:b, assignment_rhs_identifier:count, if_then_branch
    ans = longest[1] * longest[2] # assignment, assignment_lhs_identifier:ans, assignment_rhs_identifier:longest, binary_operator:Mult, index, int_literal, literal:Num
    return ans

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_28/sol1.py
# ----------------------------------------------------------------------------------------
from math import ceil # import_from:math
def diagonal_sum(n): # function:diagonal_sum (-> +6), function_returning_a_value:diagonal_sum (-> +6)
    total = 1 # assignment, assignment_lhs_identifier:total, int_literal, literal:Num
    for i in range(1, int(ceil(n / 2.0))): # binary_operator:Div, composition, float_literal, for:i (-> +3), for_range_start (-> +3), function_call:ceil, function_call:int, function_call:range, int_literal, literal:Num, suggest_constant_definition
        odd = 2 * i + 1 # assignment, assignment_lhs_identifier:odd, assignment_rhs_identifier:i, binary_operator:Add, binary_operator:Mult, int_literal, literal:Num
        even = 2 * i # assignment, assignment_lhs_identifier:even, assignment_rhs_identifier:i, binary_operator:Mult, int_literal, literal:Num
        total = total + 4 * odd ** 2 - 6 * even # assignment, assignment_lhs_identifier:total, assignment_rhs_identifier:even, assignment_rhs_identifier:odd, assignment_rhs_identifier:total, binary_operator:Add, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_29/solution.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8), function_returning_a_value:solution (-> +8)
    collectPowers = set() # assignment, assignment_lhs_identifier:collectPowers, assignment_rhs_identifier:set, function_call:set
    currentPow = 0 # assignment, assignment_lhs_identifier:currentPow, int_literal, literal:Num
    N = n + 1 # assignment, assignment_lhs_identifier:N, assignment_rhs_identifier:n, binary_operator:Add, int_literal, literal:Num
    for a in range(2, N): # call_parameter:N, for:a (-> +3), for_range_start (-> +3), function_call:range, int_literal, literal:Num, square_nested_for (-> +3)
        for b in range(2, N): # call_parameter:N, for:b (-> +2), for_range_start (-> +2), function_call:range, int_literal, literal:Num, nested_for:1 (-> +2)
            currentPow = a ** b # assignment, assignment_lhs_identifier:currentPow, assignment_rhs_identifier:a, assignment_rhs_identifier:b, binary_operator:Pow
            collectPowers.add(currentPow) # call_parameter:currentPow, method_call:add, method_call_object:collectPowers
    return len(collectPowers) # call_parameter:collectPowers, function_call:len

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_31/sol1.py
# ----------------------------------------------------------------------------------------
def one_pence(): # function:one_pence (-> +1), function_returning_a_value:one_pence (-> +1)
    return 1 # int_literal, literal:Num
def two_pence(x): # body_recursive_function:two_pence (-> +1), function:two_pence (-> +1), function_returning_a_value:two_pence (-> +1), recursive_function:two_pence (-> +1)
    return 0 if x < 0 else two_pence(x - 2) + one_pence() # binary_operator:Add, binary_operator:Sub, comparison_operator:Lt, conditional_expression, function_call:one_pence, function_call:two_pence, int_literal, literal:Num
def five_pence(x): # body_recursive_function:five_pence (-> +1), function:five_pence (-> +1), function_returning_a_value:five_pence (-> +1), recursive_function:five_pence (-> +1)
    return 0 if x < 0 else five_pence(x - 5) + two_pence(x) # binary_operator:Add, binary_operator:Sub, call_parameter:x, comparison_operator:Lt, conditional_expression, function_call:five_pence, function_call:two_pence, int_literal, literal:Num, suggest_constant_definition
def ten_pence(x): # body_recursive_function:ten_pence (-> +1), function:ten_pence (-> +1), function_returning_a_value:ten_pence (-> +1), recursive_function:ten_pence (-> +1)
    return 0 if x < 0 else ten_pence(x - 10) + five_pence(x) # binary_operator:Add, binary_operator:Sub, call_parameter:x, comparison_operator:Lt, conditional_expression, function_call:five_pence, function_call:ten_pence, int_literal, literal:Num, suggest_constant_definition
def twenty_pence(x): # body_recursive_function:twenty_pence (-> +1), function:twenty_pence (-> +1), function_returning_a_value:twenty_pence (-> +1), recursive_function:twenty_pence (-> +1)
    return 0 if x < 0 else twenty_pence(x - 20) + ten_pence(x) # binary_operator:Add, binary_operator:Sub, call_parameter:x, comparison_operator:Lt, conditional_expression, function_call:ten_pence, function_call:twenty_pence, int_literal, literal:Num, suggest_constant_definition
def fifty_pence(x): # body_recursive_function:fifty_pence (-> +1), function:fifty_pence (-> +1), function_returning_a_value:fifty_pence (-> +1), recursive_function:fifty_pence (-> +1)
    return 0 if x < 0 else fifty_pence(x - 50) + twenty_pence(x) # binary_operator:Add, binary_operator:Sub, call_parameter:x, comparison_operator:Lt, conditional_expression, function_call:fifty_pence, function_call:twenty_pence, int_literal, literal:Num, suggest_constant_definition
def one_pound(x): # body_recursive_function:one_pound (-> +1), function:one_pound (-> +1), function_returning_a_value:one_pound (-> +1), recursive_function:one_pound (-> +1)
    return 0 if x < 0 else one_pound(x - 100) + fifty_pence(x) # binary_operator:Add, binary_operator:Sub, call_parameter:x, comparison_operator:Lt, conditional_expression, function_call:fifty_pence, function_call:one_pound, int_literal, literal:Num, suggest_constant_definition
def two_pound(x): # body_recursive_function:two_pound (-> +1), function:two_pound (-> +1), function_returning_a_value:two_pound (-> +1), recursive_function:two_pound (-> +1)
    return 0 if x < 0 else two_pound(x - 200) + one_pound(x) # binary_operator:Add, binary_operator:Sub, call_parameter:x, comparison_operator:Lt, conditional_expression, function_call:one_pound, function_call:two_pound, int_literal, literal:Num, suggest_constant_definition
def solution(n): # function:solution (-> +1), function_returning_a_value:solution (-> +1)
    return two_pound(n) # call_parameter:n, function_call:two_pound

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_32/sol32.py
# ----------------------------------------------------------------------------------------
import itertools # import:itertools
def isCombinationValid(combination): # function:isCombinationValid (-> +6), function_returning_a_value:isCombinationValid (-> +6)
    return ( # boolean_operator:Or
        int("".join(combination[0:2])) * int("".join(combination[2:5])) # binary_operator:Mult, composition, function_call:int, int_literal, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
        == int("".join(combination[5:9])) # comparison_operator:Eq, composition, function_call:int, int_literal, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
    ) or (
        int("".join(combination[0])) * int("".join(combination[1:5])) # binary_operator:Mult, composition, function_call:int, index, int_literal, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
        == int("".join(combination[5:9])) # comparison_operator:Eq, composition, function_call:int, int_literal, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
    )
def solution(): # function:solution (-> +6), function_returning_a_value:solution (-> +6)
    return sum( # composition, function_call:sum
        set( # composition, function_call:set
            [
                int("".join(pandigital[5:9])) # composition, comprehension:List, comprehension_for_count:1, function_call:int, int_literal, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
                for pandigital in itertools.permutations("123456789") # literal:Str, method_call:permutations
                if isCombinationValid(pandigital) # call_parameter:pandigital, filtered_comprehension, function_call:isCombinationValid
            ]
        )
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_33/sol1.py
# ----------------------------------------------------------------------------------------
def isDigitCancelling(num, den): # function:isDigitCancelling (-> +4), function_returning_a_value:isDigitCancelling (-> +4)
    if num != den: # comparison_operator:NotEq, if (-> +3)
        if num % 10 == den // 10: # binary_operator:FloorDiv, binary_operator:Mod, comparison_operator:Eq, divisibility_test:10, if (-> +2), if_then_branch (-> +2), int_literal, literal:Num, nested_if:1 (-> +2), suggest_constant_definition
            if (num // 10) / (den % 10) == num / den: # binary_operator:Div, binary_operator:FloorDiv, binary_operator:Mod, comparison_operator:Eq, if (-> +1), if_then_branch (-> +1), int_literal, literal:Num, nested_if:2 (-> +1), suggest_constant_definition
                return True # if_then_branch, literal:True
def solve(digit_len: int) -> str: # function:solve, function_returning_a_value:solve
    solutions = [] # assignment, assignment_lhs_identifier:solutions, literal:List
    den = 11 # assignment, assignment_lhs_identifier:den, int_literal, literal:Num, suggest_constant_definition
    last_digit = int("1" + "0" * digit_len) # assignment, assignment_lhs_identifier:last_digit, assignment_rhs_identifier:digit_len, assignment_rhs_identifier:int, binary_operator:Add, binary_operator:Mult, function_call:int, literal:Str
    for num in range(den, last_digit): # accumulate_elements:1 (-> +7), call_parameter:den, call_parameter:last_digit, for:num (-> +7), for_range_start (-> +7), function_call:range
        while den <= 99: # comparison_operator:LtE, evolve_state (-> +4), int_literal, literal:Num, suggest_constant_definition, while (-> +4)
            if (num != den) and (num % 10 == den // 10) and (den % 10 != 0): # binary_operator:FloorDiv, binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:NotEq, divisibility_test:10, if (-> +2), int_literal, literal:Num, suggest_constant_definition
                if isDigitCancelling(num, den): # call_parameter:den, call_parameter:num, function_call:isDigitCancelling, if (-> +1), if_then_branch (-> +1), nested_if:1 (-> +1)
                    solutions.append("{}/{}".format(num, den)) # call_parameter:den, call_parameter:num, composition, if_then_branch, literal:Str, method_call:append, method_call:format, method_call_object:solutions
            den += 1 # assignment_lhs_identifier:den, augmented_assignment, int_literal, literal:Num
        num += 1 # assignment_lhs_identifier:num, augmented_assignment, int_literal, literal:Num
        den = 10 # assignment, assignment_lhs_identifier:den, int_literal, literal:Num, suggest_constant_definition
    solutions = " , ".join(solutions) # assignment, assignment_lhs_identifier:solutions, assignment_rhs_identifier:solutions, call_parameter:solutions, literal:Str, method_call:join
    return solutions

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_36/sol1.py
# ----------------------------------------------------------------------------------------
def is_palindrome(n): # function:is_palindrome (-> +5), function_returning_a_value:is_palindrome (-> +5)
    n = str(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_identifier:n, assignment_rhs_identifier:str, call_parameter:n, function_call:str
    if n == n[::-1]: # comparison_operator:Eq, if (-> +3), int_literal, literal:Num, slice_step, suggest_condition_return (-> +3)
        return True # if_then_branch, literal:True
    else:
        return False # if_else_branch, literal:False
def solution(n): # function:solution (-> +5), function_returning_a_value:solution (-> +5)
    total = 0 # assignment, assignment_lhs_identifier:total, int_literal, literal:Num
    for i in range(1, n): # accumulate_elements:1 (-> +2), call_parameter:n, for:i (-> +2), for_range_start (-> +2), function_call:range, int_literal, literal:Num
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]): # boolean_operator:And, call_parameter:i, composition, function_call:bin, function_call:is_palindrome, if (-> +1), index, int_literal, literal:Num, literal:Str, method_call:split
            total += i # assignment_lhs_identifier:total, assignment_rhs_identifier:i, augmented_assignment, if_then_branch
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_40/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +14), function_returning_a_value:solution (-> +14)
    constant = [] # assignment, assignment_lhs_identifier:constant, literal:List
    i = 1 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    while len(constant) < 1e6: # call_parameter:constant, comparison_operator:Lt, evolve_state (-> +2), float_literal, function_call:len, literal:Num, suggest_constant_definition, while (-> +2)
        constant.append(str(i)) # call_parameter:i, composition, function_call:str, method_call:append, method_call_object:constant
        i += 1 # assignment_lhs_identifier:i, augmented_assignment, int_literal, literal:Num
    constant = "".join(constant) # assignment, assignment_lhs_identifier:constant, assignment_rhs_identifier:constant, call_parameter:constant, literal:Str, method_call:join
    return (
        int(constant[0]) # binary_operator:Mult, function_call:int, index, int_literal, literal:Num
        * int(constant[9]) # function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[99]) # binary_operator:Mult, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[999]) # binary_operator:Mult, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[9999]) # binary_operator:Mult, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[99999]) # binary_operator:Mult, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
        * int(constant[999999]) # binary_operator:Mult, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_42/solution42.py
# ----------------------------------------------------------------------------------------
import os # import:os
TRIANGULAR_NUMBERS = [int(0.5 * n * (n + 1)) for n in range(1, 101)] # assignment, assignment_lhs_identifier:TRIANGULAR_NUMBERS, assignment_rhs_identifier:int, assignment_rhs_identifier:n, assignment_rhs_identifier:range, binary_operator:Add, binary_operator:Mult, comprehension:List, comprehension_for_count:1, float_literal, function_call:int, function_call:range, int_literal, literal:Num
def solution(): # function:solution (-> +13), function_returning_a_value:solution (-> +13)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, assignment_lhs_identifier:script_dir, assignment_rhs_identifier:__file__, assignment_rhs_identifier:os, call_parameter:__file__, composition, method_call:dirname, method_call:realpath
    wordsFilePath = os.path.join(script_dir, "words.txt") # assignment, assignment_lhs_identifier:wordsFilePath, assignment_rhs_identifier:os, assignment_rhs_identifier:script_dir, call_parameter:script_dir, literal:Str, method_call:join
    words = "" # assignment, assignment_lhs_identifier:words, literal:Str
    with open(wordsFilePath, "r") as f: # call_parameter:wordsFilePath, function_call:open, literal:Str
        words = f.readline() # assignment, assignment_lhs_identifier:words, assignment_rhs_identifier:f, method_call:readline
    words = list(map(lambda word: word.strip('"'), words.strip("\r\n").split(","))) # assignment, assignment_lhs_identifier:words, assignment_rhs_identifier:list, assignment_rhs_identifier:map, assignment_rhs_identifier:word, assignment_rhs_identifier:words, composition, function_call:list, function_call:map, lambda_function, literal:Str, method_call:split, method_call:strip, method_call_object:words, method_chaining
    words = list( # assignment, assignment_lhs_identifier:words, assignment_rhs_identifier:list, composition, function_call:list
        filter( # assignment_rhs_identifier:filter, composition, function_call:filter
            lambda word: word in TRIANGULAR_NUMBERS, # assignment_rhs_identifier:TRIANGULAR_NUMBERS, assignment_rhs_identifier:word, comparison_operator:In, lambda_function
            map(lambda word: sum(map(lambda x: ord(x) - 64, word)), words), # assignment_rhs_identifier:map, assignment_rhs_identifier:ord, assignment_rhs_identifier:sum, assignment_rhs_identifier:word, assignment_rhs_identifier:words, assignment_rhs_identifier:x, binary_operator:Sub, call_parameter:word, call_parameter:words, call_parameter:x, composition, function_call:map, function_call:ord, function_call:sum, int_literal, lambda_function, literal:Num, suggest_constant_definition
        )
    )
    return len(words) # call_parameter:words, function_call:len

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_48/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +4), function_returning_a_value:solution (-> +4)
    total = 0 # assignment, assignment_lhs_identifier:total, int_literal, literal:Num
    for i in range(1, 1001): # accumulate_elements:1 (-> +1), for:i (-> +1), for_range_start (-> +1), function_call:range, int_literal, literal:Num, suggest_constant_definition
        total += i ** i # assignment_lhs_identifier:total, assignment_rhs_identifier:i, augmented_assignment, binary_operator:Pow
    return str(total)[-10:] # call_parameter:total, function_call:str, int_literal, literal:Num, slice, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_52/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +12), function_returning_a_value:solution (-> +12)
    i = 1 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    while True: # literal:True, while (-> +10)
        if ( # if (-> +8)
            sorted(list(str(i))) # call_parameter:i, chained_comparison:5, composition, function_call:list, function_call:sorted, function_call:str
            == sorted(list(str(2 * i))) # binary_operator:Mult, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, int_literal, literal:Num
            == sorted(list(str(3 * i))) # binary_operator:Mult, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, int_literal, literal:Num, suggest_constant_definition
            == sorted(list(str(4 * i))) # binary_operator:Mult, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, int_literal, literal:Num, suggest_constant_definition
            == sorted(list(str(5 * i))) # binary_operator:Mult, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, int_literal, literal:Num, suggest_constant_definition
            == sorted(list(str(6 * i))) # binary_operator:Mult, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, int_literal, literal:Num, suggest_constant_definition
        ):
            return i # if_then_branch
        i += 1 # assignment_lhs_identifier:i, augmented_assignment, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_53/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial # import_from:math
def combinations(n, r): # function:combinations (-> +1), function_returning_a_value:combinations (-> +1)
    return factorial(n) / (factorial(r) * factorial(n - r)) # binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_parameter:n, call_parameter:r, function_call:factorial
def solution(): # function:solution (-> +6), function_returning_a_value:solution (-> +6)
    total = 0 # assignment, assignment_lhs_identifier:total, int_literal, literal:Num
    for i in range(1, 101): # for:i (-> +3), for_range_start (-> +3), function_call:range, int_literal, literal:Num, suggest_constant_definition
        for j in range(1, i + 1): # binary_operator:Add, for:j (-> +2), for_range_start (-> +2), function_call:range, int_literal, literal:Num, nested_for:1 (-> +2)
            if combinations(i, j) > 1e6: # call_parameter:i, call_parameter:j, comparison_operator:Gt, float_literal, function_call:combinations, if (-> +1), literal:Num, suggest_constant_definition
                total += 1 # assignment_lhs_identifier:total, augmented_assignment, if_then_branch, int_literal, literal:Num
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_551/sol1.py
# ----------------------------------------------------------------------------------------
ks = [k for k in range(2, 20 + 1)] # assignment, assignment_lhs_identifier:ks, assignment_rhs_identifier:k, assignment_rhs_identifier:range, binary_operator:Add, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num
base = [10 ** k for k in range(ks[-1] + 1)] # assignment, assignment_lhs_identifier:base, assignment_rhs_identifier:k, assignment_rhs_identifier:ks, assignment_rhs_identifier:range, binary_operator:Add, binary_operator:Pow, comprehension:List, comprehension_for_count:1, function_call:range, index, int_literal, literal:Num, negative_index:-1
memo = {} # assignment, assignment_lhs_identifier:memo, literal:Dict
def next_term(a_i, k, i, n): # function:next_term (-> +50), function_returning_a_value:next_term (-> +50), recursive_function:next_term (-> +50)
    ds_b = 0 # assignment, assignment_lhs_identifier:ds_b, int_literal, literal:Num
    for j in range(k, len(a_i)): # accumulate_elements:1 (-> +1), call_parameter:a_i, call_parameter:k, composition, for:j (-> +1), for_range_start (-> +1), function_call:len, function_call:range
        ds_b += a_i[j] # assignment_lhs_identifier:ds_b, assignment_rhs_identifier:a_i, assignment_rhs_identifier:j, augmented_assignment, index
    c = 0 # assignment, assignment_lhs_identifier:c, int_literal, literal:Num
    for j in range(min(len(a_i), k)): # accumulate_elements:1 (-> +1), call_parameter:a_i, call_parameter:k, composition, for:j (-> +1), for_range_stop (-> +1), function_call:len, function_call:min, function_call:range
        c += a_i[j] * base[j] # assignment_lhs_identifier:c, assignment_rhs_identifier:a_i, assignment_rhs_identifier:base, assignment_rhs_identifier:j, augmented_assignment, binary_operator:Mult, index
    diff, dn = 0, 0 # assignment, assignment_lhs_identifier:diff, assignment_lhs_identifier:dn, int_literal, literal:Num, literal:Tuple
    max_dn = n - i # assignment, assignment_lhs_identifier:max_dn, assignment_rhs_identifier:i, assignment_rhs_identifier:n, binary_operator:Sub
    sub_memo = memo.get(ds_b) # assignment, assignment_lhs_identifier:sub_memo, assignment_rhs_identifier:ds_b, assignment_rhs_identifier:memo, call_parameter:ds_b, method_call:get
    if sub_memo != None: # comparison_operator:NotEq, if (-> +19), literal:None
        jumps = sub_memo.get(c) # assignment, assignment_lhs_identifier:jumps, assignment_rhs_identifier:c, assignment_rhs_identifier:sub_memo, call_parameter:c, if_then_branch (-> +15), method_call:get
        if jumps != None and len(jumps) > 0: # boolean_operator:And, call_parameter:jumps, comparison_operator:Gt, comparison_operator:NotEq, function_call:len, if (-> +14), int_literal, literal:None, literal:Num, nested_if:1 (-> +14)
            max_jump = -1 # assignment, assignment_lhs_identifier:max_jump, if_then_branch (-> +11), int_literal, literal:Num
            for _k in range(len(jumps) - 1, -1, -1): # binary_operator:Sub, call_parameter:jumps, composition, for:_k (-> +3), for_range_step:-1 (-> +3), function_call:len, function_call:range, int_literal, literal:Num
                if jumps[_k][2] <= k and jumps[_k][1] <= max_dn: # boolean_operator:And, comparison_operator:LtE, if (-> +2), index, int_literal, literal:Num, nested_if:2 (-> +2)
                    max_jump = _k # assignment, assignment_lhs_identifier:max_jump, assignment_rhs_identifier:_k, if_then_branch (-> +1)
                    break
            if max_jump >= 0: # comparison_operator:GtE, if (-> +6), int_literal, literal:Num, nested_if:2 (-> +6)
                diff, dn, _kk = jumps[max_jump] # assignment, assignment_lhs_identifier:_kk, assignment_lhs_identifier:diff, assignment_lhs_identifier:dn, assignment_rhs_identifier:jumps, assignment_rhs_identifier:max_jump, if_then_branch (-> +5), index
                new_c = diff + c # assignment, assignment_lhs_identifier:new_c, assignment_rhs_identifier:c, assignment_rhs_identifier:diff, binary_operator:Add
                for j in range(min(k, len(a_i))): # call_parameter:a_i, call_parameter:k, composition, for:j (-> +1), for_range_stop (-> +1), function_call:len, function_call:min, function_call:range
                    new_c, a_i[j] = divmod(new_c, 10) # assignment, assignment_lhs_identifier:a_i, assignment_lhs_identifier:new_c, assignment_rhs_identifier:divmod, assignment_rhs_identifier:new_c, call_parameter:new_c, function_call:divmod, index, int_literal, literal:Num, suggest_constant_definition
                if new_c > 0: # comparison_operator:Gt, if (-> +1), int_literal, literal:Num, nested_if:3 (-> +1)
                    add(a_i, k, new_c) # call_parameter:a_i, call_parameter:k, call_parameter:new_c, function_call:add, if_then_branch
        else:
            sub_memo[c] = [] # assignment, assignment_lhs_identifier:sub_memo, if_else_branch, index, literal:List
    else:
        sub_memo = {c: []} # assignment, assignment_lhs_identifier:sub_memo, assignment_rhs_identifier:c, if_else_branch (-> +1), literal:List
        memo[ds_b] = sub_memo # assignment, assignment_lhs_identifier:memo, assignment_rhs_identifier:sub_memo, index
    if dn >= max_dn or c + diff >= base[k]: # binary_operator:Add, boolean_operator:Or, comparison_operator:GtE, if (-> +1), index
        return diff, dn # if_then_branch
    if k > ks[0]: # comparison_operator:Gt, if (-> +10), index, int_literal, literal:Num
        while True: # if_then_branch (-> +5), literal:True, while (-> +5)
            _diff, terms_jumped = next_term(a_i, k - 1, i + dn, n) # assignment, assignment_lhs_identifier:_diff, assignment_lhs_identifier:terms_jumped, assignment_rhs_identifier:a_i, assignment_rhs_identifier:dn, assignment_rhs_identifier:i, assignment_rhs_identifier:k, assignment_rhs_identifier:n, assignment_rhs_identifier:next_term, binary_operator:Add, binary_operator:Sub, call_parameter:a_i, call_parameter:n, function_call:next_term, int_literal, literal:Num
            diff += _diff # assignment_lhs_identifier:diff, assignment_rhs_identifier:_diff, augmented_assignment
            dn += terms_jumped # assignment_lhs_identifier:dn, assignment_rhs_identifier:terms_jumped, augmented_assignment
            if dn >= max_dn or c + diff >= base[k]: # binary_operator:Add, boolean_operator:Or, comparison_operator:GtE, if (-> +1), index, nested_if:1 (-> +1)
                break # if_then_branch
    else:
        _diff, terms_jumped = compute(a_i, k, i + dn, n) # assignment, assignment_lhs_identifier:_diff, assignment_lhs_identifier:terms_jumped, assignment_rhs_identifier:a_i, assignment_rhs_identifier:compute, assignment_rhs_identifier:dn, assignment_rhs_identifier:i, assignment_rhs_identifier:k, assignment_rhs_identifier:n, binary_operator:Add, call_parameter:a_i, call_parameter:k, call_parameter:n, function_call:compute, if_else_branch (-> +2)
        diff += _diff # assignment_lhs_identifier:diff, assignment_rhs_identifier:_diff, augmented_assignment
        dn += terms_jumped # assignment_lhs_identifier:dn, assignment_rhs_identifier:terms_jumped, augmented_assignment
    jumps = sub_memo[c] # assignment, assignment_lhs_identifier:jumps, assignment_rhs_identifier:c, assignment_rhs_identifier:sub_memo, index
    j = 0 # assignment, assignment_lhs_identifier:j, int_literal, literal:Num
    while j < len(jumps): # call_parameter:jumps, comparison_operator:Lt, function_call:len, while (-> +3)
        if jumps[j][1] > dn: # comparison_operator:Gt, if (-> +1), index, int_literal, literal:Num
            break # if_then_branch
        j += 1 # assignment_lhs_identifier:j, augmented_assignment, int_literal, literal:Num
    sub_memo[c].insert(j, (diff, dn, k)) # call_parameter:j, index, method_call:insert
    return (diff, dn)
def compute(a_i, k, i, n): # function:compute (-> +25), function_returning_a_value:compute (-> +25)
    if i >= n: # comparison_operator:GtE, if (-> +1)
        return 0, i # if_then_branch, int_literal, literal:Num
    if k > len(a_i): # call_parameter:a_i, comparison_operator:Gt, function_call:len, if (-> +1)
        a_i.extend([0 for _ in range(k - len(a_i))]) # binary_operator:Sub, call_parameter:a_i, composition, comprehension:List, comprehension_for_count:1, function_call:len, function_call:range, if_then_branch, int_literal, literal:Num, method_call:extend, method_call_object:a_i
    start_i = i # assignment, assignment_lhs_identifier:start_i, assignment_rhs_identifier:i
    ds_b, ds_c, diff = 0, 0, 0 # assignment, assignment_lhs_identifier:diff, assignment_lhs_identifier:ds_b, assignment_lhs_identifier:ds_c, int_literal, literal:Num, literal:Tuple
    for j in range(len(a_i)): # accumulate_elements:1 (-> +4), call_parameter:a_i, composition, for:j (-> +4), for_indexes (-> +4), for_range_stop (-> +4), function_call:len, function_call:range
        if j >= k: # comparison_operator:GtE, if (-> +3)
            ds_b += a_i[j] # assignment_lhs_identifier:ds_b, assignment_rhs_identifier:a_i, assignment_rhs_identifier:j, augmented_assignment, if_then_branch, index
        else:
            ds_c += a_i[j] # assignment_lhs_identifier:ds_c, assignment_rhs_identifier:a_i, assignment_rhs_identifier:j, augmented_assignment, if_else_branch, index
    while i < n: # comparison_operator:Lt, while (-> +10)
        i += 1 # assignment_lhs_identifier:i, augmented_assignment, int_literal, literal:Num
        addend = ds_c + ds_b # assignment, assignment_lhs_identifier:addend, assignment_rhs_identifier:ds_b, assignment_rhs_identifier:ds_c, binary_operator:Add
        diff += addend # assignment_lhs_identifier:diff, assignment_rhs_identifier:addend, augmented_assignment
        ds_c = 0 # assignment, assignment_lhs_identifier:ds_c, int_literal, literal:Num
        for j in range(k): # accumulate_elements:1 (-> +3), call_parameter:k, for:j (-> +3), for_range_stop (-> +3), function_call:range
            s = a_i[j] + addend # assignment, assignment_lhs_identifier:s, assignment_rhs_identifier:a_i, assignment_rhs_identifier:addend, assignment_rhs_identifier:j, binary_operator:Add, index
            addend, a_i[j] = divmod(s, 10) # assignment, assignment_lhs_identifier:a_i, assignment_lhs_identifier:addend, assignment_rhs_identifier:divmod, assignment_rhs_identifier:s, call_parameter:s, function_call:divmod, index, int_literal, literal:Num, suggest_constant_definition
            ds_c += a_i[j] # assignment_lhs_identifier:ds_c, assignment_rhs_identifier:a_i, assignment_rhs_identifier:j, augmented_assignment, index
        if addend > 0: # comparison_operator:Gt, if (-> +1), int_literal, literal:Num
            break # if_then_branch
    if addend > 0: # comparison_operator:Gt, if (-> +1), int_literal, literal:Num
        add(a_i, k, addend) # call_parameter:a_i, call_parameter:addend, call_parameter:k, function_call:add, if_then_branch
    return diff, i - start_i # binary_operator:Sub
def add(digits, k, addend): # function:add (-> +13), procedure:add (-> +13)
    for j in range(k, len(digits)): # call_parameter:digits, call_parameter:k, composition, for:j (-> +9), for_range_start (-> +9), function_call:len, function_call:range
        s = digits[j] + addend # assignment, assignment_lhs_identifier:s, assignment_rhs_identifier:addend, assignment_rhs_identifier:digits, assignment_rhs_identifier:j, binary_operator:Add, index
        if s >= 10: # comparison_operator:GtE, if (-> +5), int_literal, literal:Num, suggest_constant_definition
            quotient, digits[j] = divmod(s, 10) # assignment, assignment_lhs_identifier:digits, assignment_lhs_identifier:quotient, assignment_rhs_identifier:divmod, assignment_rhs_identifier:s, call_parameter:s, function_call:divmod, if_then_branch (-> +1), index, int_literal, literal:Num, suggest_constant_definition
            addend = addend // 10 + quotient # assignment, assignment_lhs_identifier:addend, assignment_rhs_identifier:addend, assignment_rhs_identifier:quotient, binary_operator:Add, binary_operator:FloorDiv, int_literal, literal:Num, suggest_constant_definition
        else:
            digits[j] = s # assignment, assignment_lhs_identifier:digits, assignment_rhs_identifier:s, if_else_branch (-> +1), index
            addend = addend // 10 # assignment, assignment_lhs_identifier:addend, assignment_rhs_identifier:addend, binary_operator:FloorDiv, int_literal, literal:Num, suggest_augmented_assignment, suggest_constant_definition
        if addend == 0: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
            break # if_then_branch
    while addend > 0: # comparison_operator:Gt, int_literal, literal:Num, while (-> +2)
        addend, digit = divmod(addend, 10) # assignment, assignment_lhs_identifier:addend, assignment_lhs_identifier:digit, assignment_rhs_identifier:addend, assignment_rhs_identifier:divmod, call_parameter:addend, function_call:divmod, int_literal, literal:Num, suggest_constant_definition
        digits.append(digit) # call_parameter:digit, method_call:append, method_call_object:digits
def solution(n): # function:solution (-> +12), function_returning_a_value:solution (-> +12)
    digits = [1] # assignment, assignment_lhs_identifier:digits, int_literal, literal:List, literal:Num
    i = 1 # assignment, assignment_lhs_identifier:i, int_literal, literal:Num
    dn = 0 # assignment, assignment_lhs_identifier:dn, int_literal, literal:Num
    while True: # literal:True, while (-> +4)
        diff, terms_jumped = next_term(digits, 20, i + dn, n) # assignment, assignment_lhs_identifier:diff, assignment_lhs_identifier:terms_jumped, assignment_rhs_identifier:digits, assignment_rhs_identifier:dn, assignment_rhs_identifier:i, assignment_rhs_identifier:n, assignment_rhs_identifier:next_term, binary_operator:Add, call_parameter:digits, call_parameter:n, function_call:next_term, int_literal, literal:Num, suggest_constant_definition
        dn += terms_jumped # assignment_lhs_identifier:dn, assignment_rhs_identifier:terms_jumped, augmented_assignment
        if dn == n - i: # binary_operator:Sub, comparison_operator:Eq, if (-> +1)
            break # if_then_branch
    a_n = 0 # assignment, assignment_lhs_identifier:a_n, int_literal, literal:Num
    for j in range(len(digits)): # accumulate_elements:1 (-> +1), call_parameter:digits, composition, for:j (-> +1), for_indexes (-> +1), for_range_stop (-> +1), function_call:len, function_call:range
        a_n += digits[j] * 10 ** j # assignment_lhs_identifier:a_n, assignment_rhs_identifier:digits, assignment_rhs_identifier:j, augmented_assignment, binary_operator:Mult, binary_operator:Pow, index, int_literal, literal:Num, suggest_constant_definition
    return a_n

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_56/sol1.py
# ----------------------------------------------------------------------------------------
def maximum_digital_sum(a: int, b: int) -> int: # function:maximum_digital_sum, function_returning_a_value:maximum_digital_sum
    return max( # composition, function_call:max
        [
            sum([int(x) for x in str(base ** power)]) # binary_operator:Pow, call_parameter:x, composition, comprehension:List, comprehension_for_count:1, comprehension_for_count:2, function_call:int, function_call:str, function_call:sum
            for base in range(a) # call_parameter:a, function_call:range
            for power in range(b) # call_parameter:b, function_call:range
        ]
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_67/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +18), function_returning_a_value:solution (-> +18)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, assignment_lhs_identifier:script_dir, assignment_rhs_identifier:__file__, assignment_rhs_identifier:os, call_parameter:__file__, composition, method_call:dirname, method_call:realpath
    triangle = os.path.join(script_dir, "triangle.txt") # assignment, assignment_lhs_identifier:triangle, assignment_rhs_identifier:os, assignment_rhs_identifier:script_dir, call_parameter:script_dir, literal:Str, method_call:join
    with open(triangle, "r") as f: # call_parameter:triangle, function_call:open, literal:Str
        triangle = f.readlines() # assignment, assignment_lhs_identifier:triangle, assignment_rhs_identifier:f, method_call:readlines
    a = map(lambda x: x.rstrip("\r\n").split(" "), triangle) # assignment, assignment_lhs_identifier:a, assignment_rhs_identifier:map, assignment_rhs_identifier:triangle, assignment_rhs_identifier:x, call_parameter:triangle, composition, function_call:map, lambda_function, literal:Str, method_call:rstrip, method_call:split, method_call_object:x, method_chaining
    a = list(map(lambda x: list(map(lambda y: int(y), x)), a)) # assignment, assignment_lhs_identifier:a, assignment_rhs_identifier:a, assignment_rhs_identifier:int, assignment_rhs_identifier:list, assignment_rhs_identifier:map, assignment_rhs_identifier:x, assignment_rhs_identifier:y, call_parameter:a, call_parameter:x, call_parameter:y, composition, function_call:int, function_call:list, function_call:map, lambda_function
    for i in range(1, len(a)): # call_parameter:a, composition, for:i (-> +10), for_range_start (-> +10), function_call:len, function_call:range, int_literal, literal:Num
        for j in range(len(a[i])): # composition, for:j (-> +9), for_indexes (-> +9), for_range_stop (-> +9), function_call:len, function_call:range, index, nested_for:1 (-> +9)
            if j != len(a[i - 1]): # binary_operator:Sub, comparison_operator:NotEq, function_call:len, if (-> +3), index, index_arithmetic, int_literal, literal:Num, suggest_conditional_expression (-> +3)
                number1 = a[i - 1][j] # assignment, assignment_lhs_identifier:number1, assignment_rhs_identifier:a, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
            else:
                number1 = 0 # assignment, assignment_lhs_identifier:number1, if_else_branch, int_literal, literal:Num
            if j > 0: # comparison_operator:Gt, if (-> +3), int_literal, literal:Num, suggest_conditional_expression (-> +3)
                number2 = a[i - 1][j - 1] # assignment, assignment_lhs_identifier:number2, assignment_rhs_identifier:a, assignment_rhs_identifier:i, assignment_rhs_identifier:j, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
            else:
                number2 = 0 # assignment, assignment_lhs_identifier:number2, if_else_branch, int_literal, literal:Num
            a[i][j] += max(number1, number2) # assignment_rhs_identifier:max, assignment_rhs_identifier:number1, assignment_rhs_identifier:number2, augmented_assignment, call_parameter:number1, call_parameter:number2, function_call:max, index
    return max(a[-1]) # function_call:max, index, int_literal, literal:Num, negative_index:-1

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_76/sol1.py
# ----------------------------------------------------------------------------------------
def partition(m): # function:partition (-> +9), function_returning_a_value:partition (-> +9)
    memo = [[0 for _ in range(m)] for _ in range(m + 1)] # assignment, assignment_lhs_identifier:memo, assignment_rhs_identifier:_, assignment_rhs_identifier:m, assignment_rhs_identifier:range, binary_operator:Add, call_parameter:m, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num
    for i in range(m + 1): # binary_operator:Add, for:i (-> +1), for_range_stop (-> +1), function_call:range, int_literal, literal:Num
        memo[i][0] = 1 # assignment, index, int_literal, literal:Num
    for n in range(m + 1): # accumulate_elements:1 (-> +4), binary_operator:Add, for:n (-> +4), for_range_stop (-> +4), function_call:range, int_literal, literal:Num
        for k in range(1, m): # accumulate_elements:1 (-> +3), call_parameter:m, for:k (-> +3), for_range_start (-> +3), function_call:range, int_literal, literal:Num, nested_for:1 (-> +3)
            memo[n][k] += memo[n][k - 1] # assignment_rhs_identifier:k, assignment_rhs_identifier:memo, assignment_rhs_identifier:n, augmented_assignment, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num
            if n > k: # comparison_operator:Gt, if (-> +1)
                memo[n][k] += memo[n - k - 1][k] # assignment_rhs_identifier:k, assignment_rhs_identifier:memo, assignment_rhs_identifier:n, augmented_assignment, binary_operator:Sub, if_then_branch, index, index_arithmetic, int_literal, literal:Num
    return memo[m][m - 1] - 1 # binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_99/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os
from math import log10 # import_from:math
def find_largest(data_file: str = "base_exp.txt") -> int: # function:find_largest, function_returning_a_value:find_largest, function_with_default_positional_arguments:find_largest, literal:Str
    largest = [0, 0] # assignment, assignment_lhs_identifier:largest, int_literal, literal:List, literal:Num
    for i, line in enumerate(open(os.path.join(os.path.dirname(__file__), data_file))): # call_parameter:__file__, call_parameter:data_file, composition, for:i:line (-> +3), for_indexes_elements (-> +3), function_call:enumerate, function_call:open, method_call:dirname, method_call:join
        a, x = list(map(int, line.split(","))) # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:x, assignment_rhs_identifier:int, assignment_rhs_identifier:line, assignment_rhs_identifier:list, assignment_rhs_identifier:map, call_parameter:int, composition, function_call:list, function_call:map, literal:Str, method_call:split
        if x * log10(a) > largest[0]: # binary_operator:Mult, call_parameter:a, comparison_operator:Gt, function_call:log10, if (-> +1), index, int_literal, literal:Num
            largest = [x * log10(a), i + 1] # assignment, assignment_lhs_identifier:largest, assignment_rhs_identifier:a, assignment_rhs_identifier:i, assignment_rhs_identifier:log10, assignment_rhs_identifier:x, binary_operator:Add, binary_operator:Mult, call_parameter:a, function_call:log10, if_then_branch, int_literal, literal:Num
    return largest[1] # index, int_literal, literal:Num
