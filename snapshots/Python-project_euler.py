# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +1)
    return sum([e for e in range(3, n) if e % 3 == 0 or e % 5 == 0]) # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, composition, comprehension:List, comprehension_for_count:1, divisibility_test:3, divisibility_test:5, filtered_comprehension, function_call:range, function_call:sum, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8)
    sum = 0 # assignment, literal:Num
    terms = (n - 1) // 3 # assignment, binary_operator:FloorDiv, binary_operator:Sub, literal:Num, suggest_constant_definition
    sum += ((terms) * (6 + (terms - 1) * 3)) // 2 # augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, literal:Num, suggest_constant_definition
    terms = (n - 1) // 5 # assignment, binary_operator:FloorDiv, binary_operator:Sub, literal:Num, suggest_constant_definition
    sum += ((terms) * (10 + (terms - 1) * 5)) // 2 # augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, literal:Num, suggest_constant_definition
    terms = (n - 1) // 15 # assignment, binary_operator:FloorDiv, binary_operator:Sub, literal:Num, suggest_constant_definition
    sum -= ((terms) * (30 + (terms - 1) * 15)) // 2 # augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, literal:Num, suggest_constant_definition
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +32)
    sum = 0 # assignment, literal:Num
    num = 0 # assignment, literal:Num
    while 1: # literal:Num
        num += 3 # augmented_assignment, literal:Num, suggest_constant_definition
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break
        sum += num # augmented_assignment
        num += 2 # augmented_assignment, literal:Num
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break
        sum += num # augmented_assignment
        num += 1 # augmented_assignment, literal:Num
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break
        sum += num # augmented_assignment
        num += 3 # augmented_assignment, literal:Num, suggest_constant_definition
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break
        sum += num # augmented_assignment
        num += 1 # augmented_assignment, literal:Num
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break
        sum += num # augmented_assignment
        num += 2 # augmented_assignment, literal:Num
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break
        sum += num # augmented_assignment
        num += 3 # augmented_assignment, literal:Num, suggest_constant_definition
        if num >= n: # comparison_operator:GtE, if (-> +1)
            break
        sum += num # augmented_assignment
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +22)
    xmulti = [] # assignment, literal:List
    zmulti = [] # assignment, literal:List
    z = 3 # assignment, literal:Num, suggest_constant_definition
    x = 5 # assignment, literal:Num, suggest_constant_definition
    temp = 1 # assignment, literal:Num
    while True: # literal:True
        result = z * temp # assignment, binary_operator:Mult
        if result < n: # comparison_operator:Lt, if (-> +5), if_else (-> +5)
            zmulti.append(result) # method_call:append
            temp += 1 # augmented_assignment, literal:Num
        else:
            temp = 1 # assignment, literal:Num
            break
    while True: # literal:True
        result = x * temp # assignment, binary_operator:Mult
        if result < n: # comparison_operator:Lt, if (-> +4), if_else (-> +4)
            xmulti.append(result) # method_call:append
            temp += 1 # augmented_assignment, literal:Num
        else:
            break
    collection = list(set(xmulti + zmulti)) # assignment, binary_operator:Add, composition, function_call:list, function_call:set
    return sum(collection) # function_call:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +1)
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0]) # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, composition, comprehension:List, comprehension_for_count:1, divisibility_test:3, divisibility_test:5, filtered_comprehension, function_call:range, function_call:sum, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol6.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +9)
    a = 3 # assignment, literal:Num, suggest_constant_definition
    result = 0 # assignment, literal:Num
    while a < n: # comparison_operator:Lt
        if a % 3 == 0 or a % 5 == 0: # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, divisibility_test:3, divisibility_test:5, if (-> +3), if_elif (-> +3), literal:Num, suggest_constant_definition
            result += a # augmented_assignment
        elif a % 15 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:15, if (-> +1), literal:Num, suggest_constant_definition
            result -= a # augmented_assignment
        a += 1 # augmented_assignment, literal:Num
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol7.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7)
    result = 0 # assignment, literal:Num
    for i in range(n): # accumulate_elements:AugAssign (-> +4), for_range_stop (-> +4), function_call:range
        if i % 3 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:3, if (-> +3), if_elif (-> +3), literal:Num, suggest_constant_definition
            result += i # augmented_assignment
        elif i % 5 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:5, if (-> +1), literal:Num, suggest_constant_definition
            result += i # augmented_assignment
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8)
    i = 1 # assignment, literal:Num
    j = 2 # assignment, literal:Num
    sum = 0 # assignment, literal:Num
    while j <= n: # comparison_operator:LtE
        if j % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), literal:Num
            sum += j # augmented_assignment
        i, j = j, i + j # assignment, binary_operator:Add
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7)
    ls = [] # assignment, literal:List
    a, b = 0, 1 # assignment, literal:Num, literal:Tuple
    while b <= n: # comparison_operator:LtE
        if b % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), literal:Num
            ls.append(b) # method_call:append
        a, b = b, a + b # assignment, binary_operator:Add
    return ls

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +9)
    if n <= 1: # comparison_operator:LtE, if (-> +1), literal:Num
        return 0 # literal:Num
    a = 0 # assignment, literal:Num
    b = 2 # assignment, literal:Num
    count = 0 # assignment, literal:Num
    while 4 * b + a <= n: # binary_operator:Add, binary_operator:Mult, comparison_operator:LtE, literal:Num, suggest_constant_definition
        a, b = b, 4 * b + a # assignment, binary_operator:Add, binary_operator:Mult, literal:Num, suggest_constant_definition
        count += a # augmented_assignment
    return count + b # binary_operator:Add

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol4.py
# ----------------------------------------------------------------------------------------
import math # import:math
from decimal import Decimal, getcontext # import_from:decimal
def solution(n): # function:solution (-> +12)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, literal:Str, raise_exception:ValueError
    getcontext().prec = 100 # assignment, function_call:getcontext, literal:Num, suggest_constant_definition
    phi = (Decimal(5) ** Decimal(0.5) + 1) / Decimal(2) # assignment, binary_operator:Add, binary_operator:Div, binary_operator:Pow, function_call:Decimal, literal:Num, suggest_constant_definition
    index = (math.floor(math.log(n * (phi + 2), phi) - 1) // 3) * 3 + 2 # assignment, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, composition, literal:Num, method_call:floor, method_call:log, suggest_constant_definition
    num = Decimal(round(phi ** Decimal(index + 1))) / (phi + 2) # assignment, binary_operator:Add, binary_operator:Div, binary_operator:Pow, composition, function_call:Decimal, function_call:round, literal:Num
    sum = num // 2 # assignment, binary_operator:FloorDiv, literal:Num
    return int(sum) # function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +12)
    a = [0, 1] # assignment, literal:List, literal:Num
    i = 0 # assignment, literal:Num
    while a[i] <= n: # comparison_operator:LtE, index
        a.append(a[i] + a[i + 1]) # binary_operator:Add, index, index_arithmetic, literal:Num, method_call:append
        if a[i + 2] > n: # binary_operator:Add, comparison_operator:Gt, if (-> +1), index, index_arithmetic, literal:Num
            break
        i += 1 # augmented_assignment, literal:Num
    sum = 0 # assignment, literal:Num
    for j in range(len(a) - 1): # accumulate_elements:AugAssign (-> +2), binary_operator:Sub, composition, for_range_stop (-> +2), function_call:len, function_call:range, literal:Num
        if a[j] % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), index, literal:Num
            sum += a[j] # augmented_assignment, index
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol1.py
# ----------------------------------------------------------------------------------------
import math # import:math
def isprime(no): # function:isprime (-> +9)
    if no == 2: # comparison_operator:Eq, if (-> +3), if_elif (-> +3), literal:Num
        return True # literal:True
    elif no % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), literal:Num
        return False # literal:False
    sq = int(math.sqrt(no)) + 1 # assignment, binary_operator:Add, composition, function_call:int, literal:Num, method_call:sqrt
    for i in range(3, sq, 2): # for_range_step:2 (-> +2), function_call:range, literal:Num, suggest_constant_definition, universal_quantifier (-> +3)
        if no % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), literal:Num
            return False # literal:False
    return True # literal:True
def solution(n): # function:solution (-> +24)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, literal:Str, raise_exception:ValueError
    maxNumber = 0 # assignment, literal:Num
    if isprime(n): # function_call:isprime, if (-> +16), if_else (-> +16)
        return n
    else:
        while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +1), literal:Num
            n = n / 2 # assignment, binary_operator:Div, literal:Num, suggest_augmented_assignment
        if isprime(n): # function_call:isprime, if (-> +11), if_else (-> +11)
            return int(n) # function_call:int
        else:
            n1 = int(math.sqrt(n)) + 1 # assignment, binary_operator:Add, composition, function_call:int, literal:Num, method_call:sqrt
            for i in range(3, n1, 2): # for_range_step:2 (-> +6), function_call:range, literal:Num, suggest_constant_definition
                if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +5), literal:Num
                    if isprime(n / i): # binary_operator:Div, function_call:isprime, if (-> +4), if_elif (-> +4)
                        maxNumber = n / i # assignment, binary_operator:Div
                        break
                    elif isprime(i): # function_call:isprime, if (-> +1)
                        maxNumber = i # assignment
            return maxNumber

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +16)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, literal:Str, raise_exception:ValueError
    prime = 1 # assignment, literal:Num
    i = 2 # assignment, literal:Num
    while i * i <= n: # binary_operator:Mult, comparison_operator:LtE, evolve_state (-> +4)
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, literal:Num
            prime = i # assignment
            n //= i # augmented_assignment
        i += 1 # augmented_assignment, literal:Num
    if n > 1: # comparison_operator:Gt, if (-> +1), literal:Num
        prime = n # assignment
    return int(prime) # function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n: int) -> int: # function:solution
    try: # catch_exception (-> +3)
        n = int(n) # assignment, function_call:int
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, literal:Str, raise_exception:ValueError
    i = 2 # assignment, literal:Num
    ans = 0 # assignment, literal:Num
    if n == 2: # comparison_operator:Eq, if (-> +1), literal:Num
        return 2 # literal:Num
    while n > 2: # comparison_operator:Gt, evolve_state (-> +5), literal:Num
        while n % i != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test, evolve_state (-> +1), literal:Num
            i += 1 # augmented_assignment, literal:Num
        ans = i # assignment
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, literal:Num
            n = n / i # assignment, binary_operator:Div, suggest_augmented_assignment
        i += 1 # augmented_assignment, literal:Num
    return int(ans) # function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_04/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8)
    for number in range(n - 1, 10000, -1): # binary_operator:Sub, find_first_element (-> +6), for_range_step:-1 (-> +7), function_call:range, literal:Num, suggest_constant_definition
        strNumber = str(number) # assignment, function_call:str
        if strNumber == strNumber[::-1]: # comparison_operator:Eq, if (-> +5), literal:Num, slice_step
            divisor = 999 # assignment, literal:Num, suggest_constant_definition
            while divisor != 99: # comparison_operator:NotEq, evolve_state (-> +3), literal:Num, suggest_constant_definition
                if (number % divisor == 0) and (len(str(int(number / divisor))) == 3): # binary_operator:Div, binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, composition, divisibility_test, function_call:int, function_call:len, function_call:str, if (-> +1), literal:Num, suggest_constant_definition
                    return number
                divisor -= 1 # augmented_assignment, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_04/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7)
    answer = 0 # assignment, literal:Num
    for i in range(999, 99, -1): # accumulate_elements:Assign (-> +4), for_range_step:-1 (-> +4), function_call:range, literal:Num, nested_for (-> +4), square_nested_for (-> +4), suggest_constant_definition
        for j in range(999, 99, -1): # accumulate_elements:Assign (-> +3), for_range_step:-1 (-> +3), function_call:range, literal:Num, suggest_constant_definition
            t = str(i * j) # assignment, binary_operator:Mult, function_call:str
            if t == t[::-1] and i * j < n: # binary_operator:Mult, boolean_operator:And, comparison_operator:Eq, comparison_operator:Lt, if (-> +1), literal:Num, slice_step
                answer = max(answer, i * j) # assignment, binary_operator:Mult, function_call:max
    return answer

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_05/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +18)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, literal:Str, raise_exception:ValueError
    i = 0 # assignment, literal:Num
    while 1: # literal:Num
        i += n * (n - 1) # augmented_assignment, binary_operator:Mult, binary_operator:Sub, literal:Num
        nfound = 0 # assignment, literal:Num
        for j in range(2, n): # for_range_start (-> +3), function_call:range, literal:Num
            if i % j != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test, if (-> +2), literal:Num
                nfound = 1 # assignment, literal:Num
                break
        if nfound == 0: # comparison_operator:Eq, if (-> +3), literal:Num
            if i == 0: # comparison_operator:Eq, if (-> +1), literal:Num
                i = 1 # assignment, literal:Num
            return i

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_05/sol2.py
# ----------------------------------------------------------------------------------------
def gcd(x, y): # function:gcd (-> +1), recursive_function:gcd (-> +1)
    return x if y == 0 else gcd(y, x % y) # binary_operator:Mod, comparison_operator:Eq, conditional_expression, function_call:gcd, literal:Num
def lcm(x, y): # function:lcm (-> +1)
    return (x * y) // gcd(x, y) # binary_operator:FloorDiv, binary_operator:Mult, function_call:gcd
def solution(n): # function:solution (-> +4)
    g = 1 # assignment, literal:Num
    for i in range(1, n + 1): # accumulate_elements:Assign (-> +1), binary_operator:Add, for_range_start (-> +1), function_call:range, literal:Num
        g = lcm(g, i) # assignment, function_call:lcm
    return g

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7)
    suma = 0 # assignment, literal:Num
    sumb = 0 # assignment, literal:Num
    for i in range(1, n + 1): # accumulate_elements:AugAssign (-> +2), binary_operator:Add, for_range_start (-> +2), function_call:range, literal:Num
        suma += i ** 2 # augmented_assignment, binary_operator:Pow, literal:Num
        sumb += i # augmented_assignment
    sum = sumb ** 2 - suma # assignment, binary_operator:Pow, binary_operator:Sub, literal:Num
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +4)
    suma = n * (n + 1) / 2 # assignment, binary_operator:Add, binary_operator:Div, binary_operator:Mult, literal:Num
    suma **= 2 # augmented_assignment, literal:Num
    sumb = n * (n + 1) * (2 * n + 1) / 6 # assignment, binary_operator:Add, binary_operator:Div, binary_operator:Mult, literal:Num, suggest_constant_definition
    return int(suma - sumb) # binary_operator:Sub, function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol3.py
# ----------------------------------------------------------------------------------------
import math # import:math
def solution(n): # function:solution (-> +3)
    sum_of_squares = sum([i * i for i in range(1, n + 1)]) # assignment, binary_operator:Add, binary_operator:Mult, composition, comprehension:List, comprehension_for_count:1, function_call:range, function_call:sum, literal:Num
    square_of_sum = int(math.pow(sum(range(1, n + 1)), 2)) # assignment, binary_operator:Add, composition, function_call:int, function_call:range, function_call:sum, literal:Num, method_call:pow
    return square_of_sum - sum_of_squares # binary_operator:Sub

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +3)
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6 # assignment, binary_operator:Add, binary_operator:Div, binary_operator:Mult, literal:Num, suggest_constant_definition
    square_of_sum = (n * (n + 1) / 2) ** 2 # assignment, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Pow, literal:Num
    return int(square_of_sum - sum_of_squares) # binary_operator:Sub, function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import_from:math
def isprime(n): # function:isprime (-> +10)
    if n == 2: # comparison_operator:Eq, if (-> +8), if_elif (-> +8), literal:Num
        return True # literal:True
    elif n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +6), if_else (-> +6), literal:Num
        return False # literal:False
    else:
        sq = int(sqrt(n)) + 1 # assignment, binary_operator:Add, composition, function_call:int, function_call:sqrt, literal:Num
        for i in range(3, sq, 2): # for_range_step:2 (-> +2), function_call:range, literal:Num, suggest_constant_definition
            if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), literal:Num
                return False # literal:False
    return True # literal:True
def solution(n): # function:solution (-> +11)
    i = 0 # assignment, literal:Num
    j = 1 # assignment, literal:Num
    while i != n and j < 3: # boolean_operator:And, comparison_operator:Lt, comparison_operator:NotEq, evolve_state (-> +3), literal:Num, suggest_constant_definition
        j += 1 # augmented_assignment, literal:Num
        if isprime(j): # function_call:isprime, if (-> +1)
            i += 1 # augmented_assignment, literal:Num
    while i != n: # comparison_operator:NotEq
        j += 2 # augmented_assignment, literal:Num
        if isprime(j): # function_call:isprime, if (-> +1)
            i += 1 # augmented_assignment, literal:Num
    return j

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol2.py
# ----------------------------------------------------------------------------------------
def isprime(number): # function:isprime (-> +4)
    for i in range(2, int(number ** 0.5) + 1): # binary_operator:Add, binary_operator:Pow, composition, for_range_start (-> +2), function_call:int, function_call:range, literal:Num, suggest_constant_definition, universal_quantifier (-> +3)
        if number % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), literal:Num
            return False # literal:False
    return True # literal:True
def solution(n): # function:solution (-> +15)
    try: # catch_exception (-> +3)
        n = int(n) # assignment, function_call:int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # function_call:TypeError, literal:Str, raise_exception:TypeError
    if n <= 0: # comparison_operator:LtE, if (-> +1), literal:Num
        raise ValueError("Parameter n must be greater or equal to one.") # function_call:ValueError, literal:Str, raise_exception:ValueError
    primes = [] # assignment, literal:List
    num = 2 # assignment, literal:Num
    while len(primes) < n: # comparison_operator:Lt, function_call:len
        if isprime(num): # function_call:isprime, if (-> +4), if_else (-> +4)
            primes.append(num) # method_call:append
            num += 1 # augmented_assignment, literal:Num
        else:
            num += 1 # augmented_assignment, literal:Num
    return primes[len(primes) - 1] # binary_operator:Sub, function_call:len, index, index_arithmetic, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol3.py
# ----------------------------------------------------------------------------------------
import math # import:math
import itertools # import:itertools
def primeCheck(number): # function:primeCheck (-> +3)
    if number % 2 == 0 and number > 2: # binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, divisibility_test:2, if (-> +1), literal:Num
        return False # literal:False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # binary_operator:Add, binary_operator:Mod, composition, comprehension:Generator, comprehension_for_count:1, function_call:all, function_call:int, function_call:range, literal:Num, method_call:sqrt, suggest_constant_definition
def prime_generator(): # function:prime_generator (-> +5), generator:prime_generator (-> +5)
    num = 2 # assignment, literal:Num
    while True: # literal:True
        if primeCheck(num): # function_call:primeCheck, if (-> +1)
            yield num
        num += 1 # augmented_assignment, literal:Num
def solution(n): # function:solution (-> +1)
    return next(itertools.islice(prime_generator(), n - 1, n)) # binary_operator:Sub, composition, function_call:next, function_call:prime_generator, literal:Num, method_call:islice

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol1.py
# ----------------------------------------------------------------------------------------
import sys # import:sys
N = """73167176531330624919225119674426574742355349194934\ # assignment, global_constant_definition
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
def solution(n): # function:solution (-> +8)
    LargestProduct = -sys.maxsize - 1 # assignment, binary_operator:Sub, literal:Num, unary_operator:USub
    for i in range(len(n) - 12): # accumulate_elements:AugAssign (-> +5), binary_operator:Sub, composition, for_range_stop (-> +5), function_call:len, function_call:range, literal:Num, nested_for (-> +5), suggest_constant_definition
        product = 1 # assignment, literal:Num
        for j in range(13): # accumulate_elements:AugAssign (-> +1), for_range_stop (-> +1), function_call:range, literal:Num, suggest_constant_definition
            product *= int(n[i + j]) # augmented_assignment, binary_operator:Add, function_call:int, index, index_arithmetic
        if product > LargestProduct: # comparison_operator:Gt, if (-> +1)
            LargestProduct = product # assignment
    return LargestProduct

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol2.py
# ----------------------------------------------------------------------------------------
from functools import reduce # import_from:functools
N = ( # assignment, global_constant_definition
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
def solution(n): # function:solution (-> +4)
    return max( # composition, function_call:max
        [
            reduce(lambda x, y: int(x) * int(y), n[i : i + 13]) # binary_operator:Add, binary_operator:Mult, composition, comprehension:List, comprehension_for_count:1, function_call:int, function_call:reduce, lambda_function, literal:Num, slice, suggest_constant_definition
            for i in range(len(n) - 12) # binary_operator:Sub, composition, function_call:len, function_call:range, literal:Num, suggest_constant_definition
        ]
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol3.py
# ----------------------------------------------------------------------------------------
import sys # import:sys
N = """73167176531330624919225119674426574742355349194934\ # assignment, global_constant_definition
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
def streval(s: str) -> int: # function:streval
    ret = 1 # assignment, literal:Num
    for it in s: # accumulate_elements:AugAssign (-> +1), for_each (-> +1)
        ret *= int(it) # augmented_assignment, function_call:int
    return ret
def solution(n: str) -> int: # function:solution
    LargestProduct = -sys.maxsize - 1 # assignment, binary_operator:Sub, literal:Num, unary_operator:USub
    substr = n[:13] # assignment, literal:Num, slice, suggest_constant_definition
    cur_index = 13 # assignment, literal:Num, suggest_constant_definition
    while cur_index < len(n) - 13: # binary_operator:Sub, comparison_operator:Lt, function_call:len, literal:Num, suggest_constant_definition
        if int(n[cur_index]) >= int(substr[0]): # comparison_operator:GtE, function_call:int, if (-> +6), if_else (-> +6), index, literal:Num
            substr = substr[1:] + n[cur_index] # assignment, binary_operator:Add, index, literal:Num, slice
            cur_index += 1 # augmented_assignment, literal:Num
        else:
            LargestProduct = max(LargestProduct, streval(substr)) # assignment, composition, function_call:max, function_call:streval
            substr = n[cur_index : cur_index + 13] # assignment, binary_operator:Add, literal:Num, slice, suggest_constant_definition
            cur_index += 13 # augmented_assignment, literal:Num, suggest_constant_definition
    return LargestProduct

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +7)
    for a in range(300): # for_range_stop (-> +6), function_call:range, literal:Num, nested_for (-> +6), suggest_constant_definition
        for b in range(400): # for_range_stop (-> +5), function_call:range, literal:Num, nested_for (-> +5), suggest_constant_definition
            for c in range(500): # for_range_stop (-> +4), function_call:range, literal:Num, suggest_constant_definition
                if a < b < c: # chained_comparison:2, comparison_operator:Lt, if (-> +3)
                    if (a ** 2) + (b ** 2) == (c ** 2): # binary_operator:Add, binary_operator:Pow, comparison_operator:Eq, if (-> +2), literal:Num
                        if (a + b + c) == 1000: # binary_operator:Add, comparison_operator:Eq, if (-> +1), literal:Num, suggest_constant_definition
                            return a * b * c # binary_operator:Mult

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +10)
    product = -1 # assignment, literal:Num
    d = 0 # assignment, literal:Num
    for a in range(1, n // 3): # binary_operator:FloorDiv, for_range_start (-> +6), function_call:range, literal:Num, suggest_constant_definition
        b = (n * n - 2 * a * n) // (2 * n - 2 * a) # assignment, binary_operator:FloorDiv, binary_operator:Mult, binary_operator:Sub, literal:Num
        c = n - a - b # assignment, binary_operator:Sub
        if c * c == (a * a + b * b): # binary_operator:Add, binary_operator:Mult, comparison_operator:Eq, if (-> +3)
            d = a * b * c # assignment, binary_operator:Mult
            if d >= product: # comparison_operator:GtE, if (-> +1)
                product = d # assignment
    return product

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol3.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +7)
    return [
        a * b * c # binary_operator:Mult, comprehension:List, comprehension_for_count:3, index
        for a in range(1, 999) # function_call:range, literal:Num, suggest_constant_definition
        for b in range(a, 999) # function_call:range, literal:Num, suggest_constant_definition
        for c in range(b, 999) # function_call:range, literal:Num, suggest_constant_definition
        if (a * a + b * b == c * c) and (a + b + c == 1000) # binary_operator:Add, binary_operator:Mult, boolean_operator:And, comparison_operator:Eq, filtered_comprehension, literal:Num, suggest_constant_definition
    ][0] # literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import_from:math
def is_prime(n): # function:is_prime (-> +4)
    for i in range(2, int(sqrt(n)) + 1): # binary_operator:Add, composition, for_range_start (-> +2), function_call:int, function_call:range, function_call:sqrt, literal:Num, universal_quantifier (-> +3)
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), literal:Num
            return False # literal:False
    return True # literal:True
def sum_of_primes(n): # function:sum_of_primes (-> +8)
    if n > 2: # comparison_operator:Gt, if (-> +3), if_else (-> +3), literal:Num
        sumOfPrimes = 2 # assignment, literal:Num
    else:
        return 0 # literal:Num
    for i in range(3, n, 2): # accumulate_elements:AugAssign (-> +2), for_range_step:2 (-> +2), function_call:range, literal:Num, suggest_constant_definition
        if is_prime(i): # function_call:is_prime, if (-> +1)
            sumOfPrimes += i # augmented_assignment
    return sumOfPrimes
def solution(n): # function:solution (-> +1)
    return sum_of_primes(n) # function_call:sum_of_primes

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol2.py
# ----------------------------------------------------------------------------------------
import math # import:math
from itertools import takewhile # import_from:itertools
def primeCheck(number): # function:primeCheck (-> +3)
    if number % 2 == 0 and number > 2: # binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, divisibility_test:2, if (-> +1), literal:Num
        return False # literal:False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # binary_operator:Add, binary_operator:Mod, composition, comprehension:Generator, comprehension_for_count:1, function_call:all, function_call:int, function_call:range, literal:Num, method_call:sqrt, suggest_constant_definition
def prime_generator(): # function:prime_generator (-> +5), generator:prime_generator (-> +5)
    num = 2 # assignment, literal:Num
    while True: # literal:True
        if primeCheck(num): # function_call:primeCheck, if (-> +1)
            yield num
        num += 1 # augmented_assignment, literal:Num
def solution(n): # function:solution (-> +1)
    return sum(takewhile(lambda x: x < n, prime_generator())) # comparison_operator:Lt, composition, function_call:prime_generator, function_call:sum, function_call:takewhile, lambda_function

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol3.py
# ----------------------------------------------------------------------------------------
def prime_sum(n: int) -> int: # function:prime_sum
    list_ = [0 for i in range(n + 1)] # assignment, binary_operator:Add, comprehension:List, comprehension_for_count:1, function_call:range, literal:Num
    list_[0] = 1 # assignment, index, literal:Num
    list_[1] = 1 # assignment, index, literal:Num
    for i in range(2, int(n ** 0.5) + 1): # binary_operator:Add, binary_operator:Pow, composition, for_range_start (-> +3), function_call:int, function_call:range, literal:Num, suggest_constant_definition
        if list_[i] == 0: # comparison_operator:Eq, if (-> +2), index, literal:Num
            for j in range(i * i, n + 1, i): # binary_operator:Add, binary_operator:Mult, for_range_step (-> +1), function_call:range, literal:Num
                list_[j] = 1 # assignment, index, literal:Num
    s = 0 # assignment, literal:Num
    for i in range(n): # accumulate_elements:AugAssign (-> +2), for_range_stop (-> +2), function_call:range
        if list_[i] == 0: # comparison_operator:Eq, if (-> +1), index, literal:Num
            s += i # augmented_assignment
    return s

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_11/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os
def largest_product(grid): # function:largest_product (-> +27)
    nColumns = len(grid[0]) # assignment, function_call:len, index, literal:Num
    nRows = len(grid) # assignment, function_call:len
    largest = 0 # assignment, literal:Num
    lrDiagProduct = 0 # assignment, literal:Num
    rlDiagProduct = 0 # assignment, literal:Num
    for i in range(nColumns): # for_range_stop (-> +20), function_call:range, nested_for (-> +20)
        for j in range(nRows - 3): # binary_operator:Sub, for_range_stop (-> +19), function_call:range, literal:Num, suggest_constant_definition
            vertProduct = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i] # assignment, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, literal:Num, suggest_constant_definition
            horzProduct = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3] # assignment, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, literal:Num, suggest_constant_definition
            if i < nColumns - 3: # binary_operator:Sub, comparison_operator:Lt, if (-> +5), literal:Num, suggest_constant_definition
                lrDiagProduct = ( # assignment
                    grid[i][j] # binary_operator:Mult, index
                    * grid[i + 1][j + 1] # binary_operator:Add, index, index_arithmetic, literal:Num
                    * grid[i + 2][j + 2] # binary_operator:Add, binary_operator:Mult, index, index_arithmetic, literal:Num
                    * grid[i + 3][j + 3] # binary_operator:Add, binary_operator:Mult, index, index_arithmetic, literal:Num, suggest_constant_definition
                )
            if i > 2: # comparison_operator:Gt, if (-> +5), literal:Num
                rlDiagProduct = ( # assignment
                    grid[i][j] # binary_operator:Mult, index
                    * grid[i - 1][j + 1] # binary_operator:Add, binary_operator:Sub, index, index_arithmetic, literal:Num
                    * grid[i - 2][j + 2] # binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, literal:Num
                    * grid[i - 3][j + 3] # binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, literal:Num, suggest_constant_definition
                )
            maxProduct = max(vertProduct, horzProduct, lrDiagProduct, rlDiagProduct) # assignment, function_call:max
            if maxProduct > largest: # comparison_operator:Gt, if (-> +1)
                largest = maxProduct # assignment
    return largest
def solution(): # function:solution (-> +6)
    grid = [] # assignment, literal:List
    with open(os.path.dirname(__file__) + "/grid.txt") as file: # binary_operator:Add, composition, function_call:open, literal:Str, method_call:dirname
        for line in file: # for_each (-> +1)
            grid.append(line.strip("\n").split(" ")) # composition, literal:Str, method_call:append, method_call:split, method_call:strip, method_chaining
    grid = [[int(i) for i in grid[j]] for j in range(len(grid))] # assignment, composition, comprehension:List, comprehension_for_count:1, function_call:int, function_call:len, function_call:range, index
    return largest_product(grid) # function_call:largest_product

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_11/sol2.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +26)
    with open(os.path.dirname(__file__) + "/grid.txt") as f: # binary_operator:Add, composition, function_call:open, literal:Str, method_call:dirname
        l = [] # assignment, literal:List
        for i in range(20): # for_range_stop (-> +1), function_call:range, literal:Num, suggest_constant_definition
            l.append([int(x) for x in f.readline().split()]) # composition, comprehension:List, comprehension_for_count:1, function_call:int, method_call:append, method_call:readline, method_call:split, method_chaining
        maximum = 0 # assignment, literal:Num
        for i in range(20): # for_range_stop (-> +4), function_call:range, literal:Num, nested_for (-> +4), suggest_constant_definition
            for j in range(17): # for_range_stop (-> +3), function_call:range, literal:Num, suggest_constant_definition
                temp = l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3] # assignment, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1)
                    maximum = temp # assignment
        for i in range(17): # for_range_stop (-> +4), function_call:range, literal:Num, nested_for (-> +4), suggest_constant_definition
            for j in range(20): # for_range_stop (-> +3), function_call:range, literal:Num, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j] # assignment, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1)
                    maximum = temp # assignment
        for i in range(17): # for_range_stop (-> +4), function_call:range, literal:Num, nested_for (-> +4), square_nested_for (-> +4), suggest_constant_definition
            for j in range(17): # for_range_stop (-> +3), function_call:range, literal:Num, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3] # assignment, binary_operator:Add, binary_operator:Mult, index, index_arithmetic, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1)
                    maximum = temp # assignment
        for i in range(17): # for_range_stop (-> +4), function_call:range, literal:Num, nested_for (-> +4), suggest_constant_definition
            for j in range(3, 20): # for_range_start (-> +3), function_call:range, literal:Num, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3] # assignment, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, literal:Num, suggest_constant_definition
                if temp > maximum: # comparison_operator:Gt, if (-> +1)
                    maximum = temp # assignment
        return maximum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_12/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import_from:math
def count_divisors(n): # function:count_divisors (-> +7)
    nDivisors = 0 # assignment, literal:Num
    for i in range(1, int(sqrt(n)) + 1): # binary_operator:Add, composition, for_range_start (-> +2), function_call:int, function_call:range, function_call:sqrt, literal:Num
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), literal:Num
            nDivisors += 2 # augmented_assignment, literal:Num
    if n ** 0.5 == int(n ** 0.5): # binary_operator:Pow, comparison_operator:Eq, function_call:int, if (-> +1), literal:Num, suggest_constant_definition
        nDivisors -= 1 # augmented_assignment, literal:Num
    return nDivisors
def solution(): # function:solution (-> +8)
    tNum = 1 # assignment, literal:Num
    i = 1 # assignment, literal:Num
    while True: # literal:True
        i += 1 # augmented_assignment, literal:Num
        tNum += i # augmented_assignment
        if count_divisors(tNum) > 500: # comparison_operator:Gt, function_call:count_divisors, if (-> +1), literal:Num, suggest_constant_definition
            break
    return tNum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_12/sol2.py
# ----------------------------------------------------------------------------------------
def triangle_number_generator(): # function:triangle_number_generator (-> +2), generator:triangle_number_generator (-> +2)
    for n in range(1, 1000000): # for_range_start (-> +1), function_call:range, literal:Num, suggest_constant_definition
        yield n * (n + 1) // 2 # binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mult, literal:Num
def count_divisors(n): # function:count_divisors (-> +1)
    return sum([2 for i in range(1, int(n ** 0.5) + 1) if n % i == 0 and i * i != n]) # binary_operator:Add, binary_operator:Mod, binary_operator:Mult, binary_operator:Pow, boolean_operator:And, comparison_operator:Eq, comparison_operator:NotEq, composition, comprehension:List, comprehension_for_count:1, divisibility_test, filtered_comprehension, function_call:int, function_call:range, function_call:sum, literal:Num, suggest_constant_definition
def solution(): # function:solution (-> +1)
    return next(i for i in triangle_number_generator() if count_divisors(i) > 500) # comparison_operator:Gt, composition, comprehension:Generator, comprehension_for_count:1, filtered_comprehension, function_call:count_divisors, function_call:next, function_call:triangle_number_generator, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_13/sol1.py
# ----------------------------------------------------------------------------------------
def solution(array): # function:solution (-> +1)
    return str(sum(array))[:10] # composition, function_call:str, function_call:sum, literal:Num, slice, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_14/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +16)
    largest_number = 0 # assignment, literal:Num
    pre_counter = 0 # assignment, literal:Num
    for input1 in range(n): # for_range_stop (-> +12), function_call:range
        counter = 1 # assignment, literal:Num
        number = input1 # assignment
        while number > 1: # comparison_operator:Gt, evolve_state (-> +6), literal:Num
            if number % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +5), if_else (-> +5), literal:Num
                number /= 2 # augmented_assignment, literal:Num
                counter += 1 # augmented_assignment, literal:Num
            else:
                number = (3 * number) + 1 # assignment, binary_operator:Add, binary_operator:Mult, literal:Num, suggest_constant_definition
                counter += 1 # augmented_assignment, literal:Num
        if counter > pre_counter: # comparison_operator:Gt, if (-> +2)
            largest_number = input1 # assignment
            pre_counter = counter # assignment
    return {"counter": pre_counter, "largest_number": largest_number} # literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_14/sol2.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function:collatz_sequence (-> +8)
    sequence = [n] # assignment
    while n != 1: # comparison_operator:NotEq, evolve_state (-> +5), literal:Num
        if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_else (-> +3), literal:Num
            n //= 2 # augmented_assignment, literal:Num
        else:
            n = 3 * n + 1 # assignment, binary_operator:Add, binary_operator:Mult, literal:Num, suggest_constant_definition
        sequence.append(n) # method_call:append
    return sequence
def solution(n): # function:solution (-> +2)
    result = max([(len(collatz_sequence(i)), i) for i in range(1, n)]) # assignment, composition, comprehension:List, comprehension_for_count:1, function_call:collatz_sequence, function_call:len, function_call:max, function_call:range, literal:Num
    return {"counter": result[0], "largest_number": result[1]} # index, literal:Num, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_15/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial # import_from:math
def lattice_paths(n): # function:lattice_paths (-> +3)
    n = 2 * n # assignment, binary_operator:Mult, literal:Num
    k = n / 2 # assignment, binary_operator:Div, literal:Num
    return int(factorial(n) / (factorial(k) * factorial(n - k))) # binary_operator:Div, binary_operator:Mult, binary_operator:Sub, composition, function_call:factorial, function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_16/sol1.py
# ----------------------------------------------------------------------------------------
def solution(power): # function:solution (-> +7)
    num = 2 ** power # assignment, binary_operator:Pow, literal:Num
    string_num = str(num) # assignment, function_call:str
    list_num = list(string_num) # assignment, function_call:list
    sum_of_num = 0 # assignment, literal:Num
    for i in list_num: # accumulate_elements:AugAssign (-> +1), for_each (-> +1)
        sum_of_num += int(i) # augmented_assignment, function_call:int
    return sum_of_num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_16/sol2.py
# ----------------------------------------------------------------------------------------
def solution(power): # function:solution (-> +5)
    n = 2 ** power # assignment, binary_operator:Pow, literal:Num
    r = 0 # assignment, literal:Num
    while n:
        r, n = r + n % 10, n // 10 # assignment, binary_operator:Add, binary_operator:FloorDiv, binary_operator:Mod, literal:Num, suggest_constant_definition
    return r

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_17/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +17)
    ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # assignment, literal:List, literal:Num, suggest_constant_definition
    tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6] # assignment, literal:List, literal:Num, suggest_constant_definition
    count = 0 # assignment, literal:Num
    for i in range(1, n + 1): # accumulate_elements:AugAssign (-> +12), binary_operator:Add, for_range_start (-> +12), function_call:range, literal:Num
        if i < 1000: # comparison_operator:Lt, if (-> +11), if_else (-> +11), literal:Num, suggest_constant_definition
            if i >= 100: # comparison_operator:GtE, if (-> +3), literal:Num, suggest_constant_definition
                count += ones_counts[i // 100] + 7 # augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, index, index_arithmetic, literal:Num, suggest_constant_definition
                if i % 100 != 0: # binary_operator:Mod, comparison_operator:NotEq, divisibility_test:100, if (-> +1), literal:Num, suggest_constant_definition
                    count += 3 # augmented_assignment, literal:Num, suggest_constant_definition
            if 0 < i % 100 < 20: # binary_operator:Mod, chained_comparison:2, comparison_operator:Lt, if (-> +4), if_else (-> +4), literal:Num, suggest_constant_definition
                count += ones_counts[i % 100] # augmented_assignment, binary_operator:Mod, index, index_arithmetic, literal:Num, suggest_constant_definition
            else:
                count += ones_counts[i % 10] # augmented_assignment, binary_operator:Mod, index, index_arithmetic, literal:Num, suggest_constant_definition
                count += tens_counts[(i % 100 - i % 10) // 10] # augmented_assignment, binary_operator:FloorDiv, binary_operator:Mod, binary_operator:Sub, index, index_arithmetic, literal:Num, suggest_constant_definition
        else:
            count += ones_counts[i // 1000] + 8 # augmented_assignment, binary_operator:Add, binary_operator:FloorDiv, index, index_arithmetic, literal:Num, suggest_constant_definition
    return count

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_18/solution.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +17)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, composition, method_call:dirname, method_call:realpath
    triangle = os.path.join(script_dir, "triangle.txt") # assignment, literal:Str, method_call:join
    with open(triangle, "r") as f: # function_call:open, literal:Str
        triangle = f.readlines() # assignment, method_call:readlines
    a = [[int(y) for y in x.rstrip("\r\n").split(" ")] for x in triangle] # assignment, comprehension:List, comprehension_for_count:1, function_call:int, literal:Str, method_call:rstrip, method_call:split, method_chaining
    for i in range(1, len(a)): # composition, for_range_start (-> +10), function_call:len, function_call:range, literal:Num, nested_for (-> +10)
        for j in range(len(a[i])): # composition, for_indexes (-> +9), for_range_stop (-> +9), function_call:len, function_call:range, index
            if j != len(a[i - 1]): # binary_operator:Sub, comparison_operator:NotEq, function_call:len, if (-> +3), if_else (-> +3), index, index_arithmetic, literal:Num, suggest_conditional_expression (-> +3)
                number1 = a[i - 1][j] # assignment, binary_operator:Sub, index, index_arithmetic, literal:Num
            else:
                number1 = 0 # assignment, literal:Num
            if j > 0: # comparison_operator:Gt, if (-> +3), if_else (-> +3), literal:Num, suggest_conditional_expression (-> +3)
                number2 = a[i - 1][j - 1] # assignment, binary_operator:Sub, index, index_arithmetic, literal:Num
            else:
                number2 = 0 # assignment, literal:Num
            a[i][j] += max(number1, number2) # augmented_assignment, function_call:max, index
    return max(a[-1]) # function_call:max, index, literal:Num, negative_index:-1

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_19/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +24)
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # assignment, literal:List, literal:Num, suggest_constant_definition
    day = 6 # assignment, literal:Num, suggest_constant_definition
    month = 1 # assignment, literal:Num
    year = 1901 # assignment, literal:Num, suggest_constant_definition
    sundays = 0 # assignment, literal:Num
    while year < 2001: # comparison_operator:Lt, evolve_state (-> +17), literal:Num, suggest_constant_definition
        day += 7 # augmented_assignment, literal:Num, suggest_constant_definition
        if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0): # binary_operator:Mod, boolean_operator:And, boolean_operator:Or, comparison_operator:Eq, divisibility_test:100, divisibility_test:4, divisibility_test:400, if (-> +10), if_elif (-> +10), literal:Num, suggest_constant_definition, unary_operator:Not
            if day > days_per_month[month - 1] and month != 2: # binary_operator:Sub, boolean_operator:And, comparison_operator:Gt, comparison_operator:NotEq, if (-> +5), if_elif (-> +5), index, index_arithmetic, literal:Num
                month += 1 # augmented_assignment, literal:Num
                day = day - days_per_month[month - 2] # assignment, binary_operator:Sub, index, index_arithmetic, literal:Num, suggest_augmented_assignment
            elif day > 29 and month == 2: # boolean_operator:And, comparison_operator:Eq, comparison_operator:Gt, if (-> +2), literal:Num, suggest_constant_definition
                month += 1 # augmented_assignment, literal:Num
                day = day - 29 # assignment, binary_operator:Sub, literal:Num, suggest_augmented_assignment, suggest_constant_definition
        else:
            if day > days_per_month[month - 1]: # binary_operator:Sub, comparison_operator:Gt, if (-> +2), index, index_arithmetic, literal:Num
                month += 1 # augmented_assignment, literal:Num
                day = day - days_per_month[month - 2] # assignment, binary_operator:Sub, index, index_arithmetic, literal:Num, suggest_augmented_assignment
        if month > 12: # comparison_operator:Gt, if (-> +2), literal:Num, suggest_constant_definition
            year += 1 # augmented_assignment, literal:Num
            month = 1 # assignment, literal:Num
        if year < 2001 and day == 1: # boolean_operator:And, comparison_operator:Eq, comparison_operator:Lt, if (-> +1), literal:Num, suggest_constant_definition
            sundays += 1 # augmented_assignment, literal:Num
    return sundays

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol1.py
# ----------------------------------------------------------------------------------------
def factorial(n): # function:factorial (-> +4)
    fact = 1 # assignment, literal:Num
    for i in range(1, n + 1): # accumulate_elements:AugAssign (-> +1), binary_operator:Add, for_range_start (-> +1), function_call:range, literal:Num
        fact *= i # augmented_assignment
    return fact
def split_and_add(number): # function:split_and_add (-> +6)
    sum_of_digits = 0 # assignment, literal:Num
    while number > 0: # comparison_operator:Gt, evolve_state (-> +3), literal:Num
        last_digit = number % 10 # assignment, binary_operator:Mod, literal:Num, suggest_constant_definition
        sum_of_digits += last_digit # augmented_assignment
        number = number // 10 # assignment, binary_operator:FloorDiv, literal:Num, suggest_augmented_assignment, suggest_constant_definition
    return sum_of_digits
def solution(n): # function:solution (-> +3)
    f = factorial(n) # assignment, function_call:factorial
    result = split_and_add(f) # assignment, function_call:split_and_add
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol2.py
# ----------------------------------------------------------------------------------------
from math import factorial # import_from:math
def solution(n): # function:solution (-> +1)
    return sum([int(x) for x in str(factorial(n))]) # composition, comprehension:List, comprehension_for_count:1, function_call:factorial, function_call:int, function_call:str, function_call:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol3.py
# ----------------------------------------------------------------------------------------
from math import factorial # import_from:math
def solution(n): # function:solution (-> +1)
    return sum(map(int, str(factorial(n)))) # composition, function_call:factorial, function_call:map, function_call:str, function_call:sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +7)
    fact = 1 # assignment, literal:Num
    result = 0 # assignment, literal:Num
    for i in range(1, n + 1): # accumulate_elements:AugAssign (-> +1), binary_operator:Add, for_range_start (-> +1), function_call:range, literal:Num
        fact *= i # augmented_assignment
    for j in str(fact): # accumulate_elements:AugAssign (-> +1), function_call:str
        result += int(j) # augmented_assignment, function_call:int
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_21/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import_from:math
def sum_of_divisors(n): # function:sum_of_divisors (-> +7)
    total = 0 # assignment, literal:Num
    for i in range(1, int(sqrt(n) + 1)): # accumulate_elements:AugAssign (-> +4), binary_operator:Add, composition, for_range_start (-> +4), function_call:int, function_call:range, function_call:sqrt, literal:Num
        if n % i == 0 and i != sqrt(n): # binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:NotEq, divisibility_test, function_call:sqrt, if (-> +3), if_elif (-> +3), literal:Num
            total += i + n // i # augmented_assignment, binary_operator:Add, binary_operator:FloorDiv
        elif i == sqrt(n): # comparison_operator:Eq, function_call:sqrt, if (-> +1)
            total += i # augmented_assignment
    return total - n # binary_operator:Sub
def solution(n): # function:solution (-> +8)
    total = sum( # assignment, composition, function_call:sum
        [
            i # comprehension:List, comprehension_for_count:1
            for i in range(1, n) # function_call:range, literal:Num
            if sum_of_divisors(sum_of_divisors(i)) == i and sum_of_divisors(i) != i # boolean_operator:And, comparison_operator:Eq, comparison_operator:NotEq, composition, filtered_comprehension, function_call:sum_of_divisors
        ]
    )
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_22/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +12)
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator:Add, composition, function_call:open, literal:Str, method_call:dirname
        names = str(file.readlines()[0]) # assignment, composition, function_call:str, index, literal:Num, method_call:readlines
        names = names.replace('"', "").split(",") # assignment, literal:Str, method_call:replace, method_call:split, method_chaining
    names.sort() # method_call:sort
    name_score = 0 # assignment, literal:Num
    total_score = 0 # assignment, literal:Num
    for i, name in enumerate(names): # for_indexes_elements (-> +4), function_call:enumerate, nested_for (-> +4)
        for letter in name: # accumulate_elements:AugAssign (-> +1), for_each (-> +1)
            name_score += ord(letter) - 64 # augmented_assignment, binary_operator:Sub, function_call:ord, literal:Num, suggest_constant_definition
        total_score += (i + 1) * name_score # augmented_assignment, binary_operator:Add, binary_operator:Mult, literal:Num
        name_score = 0 # assignment, literal:Num
    return total_score

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_22/sol2.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +12)
    total_sum = 0 # assignment, literal:Num
    temp_sum = 0 # assignment, literal:Num
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator:Add, composition, function_call:open, literal:Str, method_call:dirname
        name = str(file.readlines()[0]) # assignment, composition, function_call:str, index, literal:Num, method_call:readlines
        name = name.replace('"', "").split(",") # assignment, literal:Str, method_call:replace, method_call:split, method_chaining
    name.sort() # method_call:sort
    for i in range(len(name)): # accumulate_elements:AugAssign (-> +4), composition, for_indexes (-> +4), for_range_stop (-> +4), function_call:len, function_call:range, nested_for (-> +4)
        for j in name[i]: # accumulate_elements:AugAssign (-> +1), index
            temp_sum += ord(j) - ord("A") + 1 # augmented_assignment, binary_operator:Add, binary_operator:Sub, function_call:ord, literal:Num, literal:Str
        total_sum += (i + 1) * temp_sum # augmented_assignment, binary_operator:Add, binary_operator:Mult, literal:Num
        temp_sum = 0 # assignment, literal:Num
    return total_sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_23/sol1.py
# ----------------------------------------------------------------------------------------
def solution(limit=28123): # function:solution (-> +13), function_with_default_positional_arguments:solution (-> +13), literal:Num
    sumDivs = [1] * (limit + 1) # assignment, binary_operator:Add, binary_operator:Mult, literal:List, literal:Num
    for i in range(2, int(limit ** 0.5) + 1): # accumulate_elements:AugAssign (-> +3), binary_operator:Add, binary_operator:Pow, composition, for_range_start (-> +3), function_call:int, function_call:range, literal:Num, nested_for (-> +3), suggest_constant_definition
        sumDivs[i * i] += i # augmented_assignment, binary_operator:Mult, index, index_arithmetic
        for k in range(i + 1, limit // i + 1): # accumulate_elements:AugAssign (-> +1), binary_operator:Add, binary_operator:FloorDiv, for_range_start (-> +1), function_call:range, literal:Num
            sumDivs[k * i] += k + i # augmented_assignment, binary_operator:Add, binary_operator:Mult, index, index_arithmetic
    abundants = set() # assignment, function_call:set
    res = 0 # assignment, literal:Num
    for n in range(1, limit + 1): # accumulate_elements:AugAssign (-> +4), binary_operator:Add, for_range_start (-> +4), function_call:range, literal:Num
        if sumDivs[n] > n: # comparison_operator:Gt, if (-> +1), index
            abundants.add(n) # method_call:add
        if not any((n - a in abundants) for a in abundants): # binary_operator:Sub, comparison_operator:In, comprehension:Generator, comprehension_for_count:1, function_call:any, if (-> +1), unary_operator:Not
            res += n # augmented_assignment
    return res

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_234/sol1.py
# ----------------------------------------------------------------------------------------
def fib(a, b, n): # function:fib (-> +13)
    if n == 1: # comparison_operator:Eq, if (-> +5), if_elif (-> +5), literal:Num
        return a
    elif n == 2: # comparison_operator:Eq, if (-> +3), if_elif (-> +3), literal:Num
        return b
    elif n == 3: # comparison_operator:Eq, if (-> +1), literal:Num, suggest_constant_definition
        return str(a) + str(b) # binary_operator:Add, function_call:str
    temp = 0 # assignment, literal:Num
    for x in range(2, n): # for_range_start (-> +4), function_call:range, literal:Num
        c = str(a) + str(b) # assignment, binary_operator:Add, function_call:str
        temp = b # assignment
        b = c # assignment
        a = temp # assignment
    return c
def solution(n): # function:solution (-> +11)
    semidivisible = [] # assignment, literal:List
    for x in range(n): # for_range_stop (-> +8), function_call:range
        l = [i for i in input().split()] # assignment, comprehension:List, comprehension_for_count:1, function_call:input, method_call:split
        c2 = 1 # assignment, literal:Num
        while 1: # literal:Num
            if len(fib(l[0], l[1], c2)) < int(l[2]): # comparison_operator:Lt, composition, function_call:fib, function_call:int, function_call:len, if (-> +3), if_else (-> +3), index, literal:Num
                c2 += 1 # augmented_assignment, literal:Num
            else:
                break
        semidivisible.append(fib(l[0], l[1], c2 + 1)[int(l[2]) - 1]) # binary_operator:Add, binary_operator:Sub, composition, function_call:fib, function_call:int, index, index_arithmetic, literal:Num, method_call:append
    return semidivisible

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_24/sol1.py
# ----------------------------------------------------------------------------------------
from itertools import permutations # import_from:itertools
def solution(): # function:solution (-> +2)
    result = list(map("".join, permutations("0123456789"))) # assignment, composition, function_call:list, function_call:map, function_call:permutations, literal:Str
    return result[999999] # index, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol1.py
# ----------------------------------------------------------------------------------------
def fibonacci(n): # function:fibonacci (-> +9)
    if n == 1 or type(n) is not int: # boolean_operator:Or, comparison_operator:Eq, comparison_operator:IsNot, function_call:type, if (-> +8), if_elif (-> +8), literal:Num
        return 0 # literal:Num
    elif n == 2: # comparison_operator:Eq, if (-> +6), if_else (-> +6), literal:Num
        return 1 # literal:Num
    else:
        sequence = [0, 1] # assignment, literal:List, literal:Num
        for i in range(2, n + 1): # binary_operator:Add, for_range_start (-> +1), function_call:range, literal:Num
            sequence.append(sequence[i - 1] + sequence[i - 2]) # binary_operator:Add, binary_operator:Sub, index, index_arithmetic, literal:Num, method_call:append
        return sequence[n] # index
def fibonacci_digits_index(n): # function:fibonacci_digits_index (-> +6)
    digits = 0 # assignment, literal:Num
    index = 2 # assignment, literal:Num
    while digits < n: # comparison_operator:Lt
        index += 1 # augmented_assignment, literal:Num
        digits = len(str(fibonacci(index))) # assignment, composition, function_call:fibonacci, function_call:len, function_call:str
    return index
def solution(n): # function:solution (-> +1)
    return fibonacci_digits_index(n) # function_call:fibonacci_digits_index

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol2.py
# ----------------------------------------------------------------------------------------
def fibonacci_generator(): # function:fibonacci_generator (-> +4), generator:fibonacci_generator (-> +4)
    a, b = 0, 1 # assignment, literal:Num, literal:Tuple
    while True: # literal:True
        a, b = b, a + b # assignment, binary_operator:Add
        yield b
def solution(n): # function:solution (-> +5)
    answer = 1 # assignment, literal:Num
    gen = fibonacci_generator() # assignment, function_call:fibonacci_generator
    while len(str(next(gen))) < n: # comparison_operator:Lt, composition, function_call:len, function_call:next, function_call:str
        answer += 1 # augmented_assignment, literal:Num
    return answer + 1 # binary_operator:Add, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +12)
    f1, f2 = 1, 1 # assignment, literal:Num, literal:Tuple
    index = 2 # assignment, literal:Num
    while True: # literal:True
        i = 0 # assignment, literal:Num
        f = f1 + f2 # assignment, binary_operator:Add
        f1, f2 = f2, f # assignment
        index += 1 # augmented_assignment, literal:Num
        for j in str(f): # function_call:str
            i += 1 # augmented_assignment, literal:Num
        if i == n: # comparison_operator:Eq, if (-> +1)
            break
    return index

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_27/problem_27_sol1.py
# ----------------------------------------------------------------------------------------
import math # import:math
def is_prime(k: int) -> bool: # function:is_prime
    if k < 2 or k % 2 == 0: # binary_operator:Mod, boolean_operator:Or, comparison_operator:Eq, comparison_operator:Lt, divisibility_test:2, if (-> +7), if_elif (-> +7), literal:Num
        return False # literal:False
    elif k == 2: # comparison_operator:Eq, if (-> +5), if_else (-> +5), literal:Num
        return True # literal:True
    else:
        for x in range(3, int(math.sqrt(k) + 1), 2): # binary_operator:Add, composition, for_range_step:2 (-> +2), function_call:int, function_call:range, literal:Num, method_call:sqrt, suggest_constant_definition
            if k % x == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +1), literal:Num
                return False # literal:False
    return True # literal:True
def solution(a_limit: int, b_limit: int) -> int: # function:solution
    longest = [0, 0, 0] # assignment, literal:List, literal:Num
    for a in range((a_limit * -1) + 1, a_limit): # binary_operator:Add, binary_operator:Mult, for_range_start (-> +9), function_call:range, literal:Num, nested_for (-> +9)
        for b in range(2, b_limit): # for_range_start (-> +8), function_call:range, literal:Num
            if is_prime(b): # function_call:is_prime, if (-> +7)
                count = 0 # assignment, literal:Num
                n = 0 # assignment, literal:Num
                while is_prime((n ** 2) + (a * n) + b): # binary_operator:Add, binary_operator:Mult, binary_operator:Pow, function_call:is_prime, literal:Num
                    count += 1 # augmented_assignment, literal:Num
                    n += 1 # augmented_assignment, literal:Num
                if count > longest[0]: # comparison_operator:Gt, if (-> +1), index, literal:Num
                    longest = [count, a, b] # assignment
    ans = longest[1] * longest[2] # assignment, binary_operator:Mult, index, literal:Num
    return ans

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_28/sol1.py
# ----------------------------------------------------------------------------------------
from math import ceil # import_from:math
def diagonal_sum(n): # function:diagonal_sum (-> +6)
    total = 1 # assignment, literal:Num
    for i in range(1, int(ceil(n / 2.0))): # binary_operator:Div, composition, for_range_start (-> +3), function_call:ceil, function_call:int, function_call:range, literal:Num, suggest_constant_definition
        odd = 2 * i + 1 # assignment, binary_operator:Add, binary_operator:Mult, literal:Num
        even = 2 * i # assignment, binary_operator:Mult, literal:Num
        total = total + 4 * odd ** 2 - 6 * even # assignment, binary_operator:Add, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, literal:Num, suggest_constant_definition
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_29/solution.py
# ----------------------------------------------------------------------------------------
def solution(n): # function:solution (-> +8)
    collectPowers = set() # assignment, function_call:set
    currentPow = 0 # assignment, literal:Num
    N = n + 1 # assignment, binary_operator:Add, literal:Num
    for a in range(2, N): # for_range_start (-> +3), function_call:range, literal:Num, nested_for (-> +3), square_nested_for (-> +3)
        for b in range(2, N): # for_range_start (-> +2), function_call:range, literal:Num
            currentPow = a ** b # assignment, binary_operator:Pow
            collectPowers.add(currentPow) # method_call:add
    return len(collectPowers) # function_call:len

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_31/sol1.py
# ----------------------------------------------------------------------------------------
def one_pence(): # function:one_pence (-> +1)
    return 1 # literal:Num
def two_pence(x): # body_recursive_function:two_pence (-> +1), function:two_pence (-> +1), recursive_function:two_pence (-> +1)
    return 0 if x < 0 else two_pence(x - 2) + one_pence() # binary_operator:Add, binary_operator:Sub, comparison_operator:Lt, conditional_expression, function_call:one_pence, function_call:two_pence, literal:Num
def five_pence(x): # body_recursive_function:five_pence (-> +1), function:five_pence (-> +1), recursive_function:five_pence (-> +1)
    return 0 if x < 0 else five_pence(x - 5) + two_pence(x) # binary_operator:Add, binary_operator:Sub, comparison_operator:Lt, conditional_expression, function_call:five_pence, function_call:two_pence, literal:Num, suggest_constant_definition
def ten_pence(x): # body_recursive_function:ten_pence (-> +1), function:ten_pence (-> +1), recursive_function:ten_pence (-> +1)
    return 0 if x < 0 else ten_pence(x - 10) + five_pence(x) # binary_operator:Add, binary_operator:Sub, comparison_operator:Lt, conditional_expression, function_call:five_pence, function_call:ten_pence, literal:Num, suggest_constant_definition
def twenty_pence(x): # body_recursive_function:twenty_pence (-> +1), function:twenty_pence (-> +1), recursive_function:twenty_pence (-> +1)
    return 0 if x < 0 else twenty_pence(x - 20) + ten_pence(x) # binary_operator:Add, binary_operator:Sub, comparison_operator:Lt, conditional_expression, function_call:ten_pence, function_call:twenty_pence, literal:Num, suggest_constant_definition
def fifty_pence(x): # body_recursive_function:fifty_pence (-> +1), function:fifty_pence (-> +1), recursive_function:fifty_pence (-> +1)
    return 0 if x < 0 else fifty_pence(x - 50) + twenty_pence(x) # binary_operator:Add, binary_operator:Sub, comparison_operator:Lt, conditional_expression, function_call:fifty_pence, function_call:twenty_pence, literal:Num, suggest_constant_definition
def one_pound(x): # body_recursive_function:one_pound (-> +1), function:one_pound (-> +1), recursive_function:one_pound (-> +1)
    return 0 if x < 0 else one_pound(x - 100) + fifty_pence(x) # binary_operator:Add, binary_operator:Sub, comparison_operator:Lt, conditional_expression, function_call:fifty_pence, function_call:one_pound, literal:Num, suggest_constant_definition
def two_pound(x): # body_recursive_function:two_pound (-> +1), function:two_pound (-> +1), recursive_function:two_pound (-> +1)
    return 0 if x < 0 else two_pound(x - 200) + one_pound(x) # binary_operator:Add, binary_operator:Sub, comparison_operator:Lt, conditional_expression, function_call:one_pound, function_call:two_pound, literal:Num, suggest_constant_definition
def solution(n): # function:solution (-> +1)
    return two_pound(n) # function_call:two_pound

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_32/sol32.py
# ----------------------------------------------------------------------------------------
import itertools # import:itertools
def isCombinationValid(combination): # function:isCombinationValid (-> +6)
    return ( # boolean_operator:Or
        int("".join(combination[0:2])) * int("".join(combination[2:5])) # binary_operator:Mult, composition, function_call:int, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
        == int("".join(combination[5:9])) # comparison_operator:Eq, composition, function_call:int, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
    ) or (
        int("".join(combination[0])) * int("".join(combination[1:5])) # binary_operator:Mult, composition, function_call:int, index, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
        == int("".join(combination[5:9])) # comparison_operator:Eq, composition, function_call:int, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
    )
def solution(): # function:solution (-> +6)
    return sum( # composition, function_call:sum
        set( # composition, function_call:set
            [
                int("".join(pandigital[5:9])) # composition, comprehension:List, comprehension_for_count:1, function_call:int, literal:Num, literal:Str, method_call:join, slice, suggest_constant_definition
                for pandigital in itertools.permutations("123456789") # literal:Str, method_call:permutations
                if isCombinationValid(pandigital) # filtered_comprehension, function_call:isCombinationValid
            ]
        )
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_33/sol1.py
# ----------------------------------------------------------------------------------------
def isDigitCancelling(num, den): # function:isDigitCancelling (-> +4)
    if num != den: # comparison_operator:NotEq, if (-> +3)
        if num % 10 == den // 10: # binary_operator:FloorDiv, binary_operator:Mod, comparison_operator:Eq, divisibility_test:10, if (-> +2), literal:Num, suggest_constant_definition
            if (num // 10) / (den % 10) == num / den: # binary_operator:Div, binary_operator:FloorDiv, binary_operator:Mod, comparison_operator:Eq, if (-> +1), literal:Num, suggest_constant_definition
                return True # literal:True
def solve(digit_len: int) -> str: # function:solve
    solutions = [] # assignment, literal:List
    den = 11 # assignment, literal:Num, suggest_constant_definition
    last_digit = int("1" + "0" * digit_len) # assignment, binary_operator:Add, binary_operator:Mult, function_call:int, literal:Str
    for num in range(den, last_digit): # for_range_start (-> +7), function_call:range
        while den <= 99: # comparison_operator:LtE, evolve_state (-> +4), literal:Num, suggest_constant_definition
            if (num != den) and (num % 10 == den // 10) and (den % 10 != 0): # binary_operator:FloorDiv, binary_operator:Mod, boolean_operator:And, comparison_operator:Eq, comparison_operator:NotEq, divisibility_test:10, if (-> +2), literal:Num, suggest_constant_definition
                if isDigitCancelling(num, den): # function_call:isDigitCancelling, if (-> +1)
                    solutions.append("{}/{}".format(num, den)) # composition, literal:Str, method_call:append, method_call:format
            den += 1 # augmented_assignment, literal:Num
        num += 1 # augmented_assignment, literal:Num
        den = 10 # assignment, literal:Num, suggest_constant_definition
    solutions = " , ".join(solutions) # assignment, literal:Str, method_call:join
    return solutions

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_36/sol1.py
# ----------------------------------------------------------------------------------------
def is_palindrome(n): # function:is_palindrome (-> +5)
    n = str(n) # assignment, function_call:str
    if n == n[::-1]: # comparison_operator:Eq, if (-> +3), if_else (-> +3), literal:Num, slice_step, suggest_condition_return (-> +3)
        return True # literal:True
    else:
        return False # literal:False
def solution(n): # function:solution (-> +5)
    total = 0 # assignment, literal:Num
    for i in range(1, n): # accumulate_elements:AugAssign (-> +2), for_range_start (-> +2), function_call:range, literal:Num
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]): # boolean_operator:And, composition, function_call:bin, function_call:is_palindrome, if (-> +1), index, literal:Num, literal:Str, method_call:split
            total += i # augmented_assignment
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_40/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +14)
    constant = [] # assignment, literal:List
    i = 1 # assignment, literal:Num
    while len(constant) < 1e6: # comparison_operator:Lt, evolve_state (-> +2), function_call:len, literal:Num, suggest_constant_definition
        constant.append(str(i)) # composition, function_call:str, method_call:append
        i += 1 # augmented_assignment, literal:Num
    constant = "".join(constant) # assignment, literal:Str, method_call:join
    return (
        int(constant[0]) # binary_operator:Mult, function_call:int, index, literal:Num
        * int(constant[9]) # function_call:int, index, literal:Num, suggest_constant_definition
        * int(constant[99]) # binary_operator:Mult, function_call:int, index, literal:Num, suggest_constant_definition
        * int(constant[999]) # binary_operator:Mult, function_call:int, index, literal:Num, suggest_constant_definition
        * int(constant[9999]) # binary_operator:Mult, function_call:int, index, literal:Num, suggest_constant_definition
        * int(constant[99999]) # binary_operator:Mult, function_call:int, index, literal:Num, suggest_constant_definition
        * int(constant[999999]) # binary_operator:Mult, function_call:int, index, literal:Num, suggest_constant_definition
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_42/solution42.py
# ----------------------------------------------------------------------------------------
import os # import:os
TRIANGULAR_NUMBERS = [int(0.5 * n * (n + 1)) for n in range(1, 101)] # assignment, binary_operator:Add, binary_operator:Mult, comprehension:List, comprehension_for_count:1, function_call:int, function_call:range, global_constant_definition, literal:Num
def solution(): # function:solution (-> +13)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, composition, method_call:dirname, method_call:realpath
    wordsFilePath = os.path.join(script_dir, "words.txt") # assignment, literal:Str, method_call:join
    words = "" # assignment, literal:Str
    with open(wordsFilePath, "r") as f: # function_call:open, literal:Str
        words = f.readline() # assignment, method_call:readline
    words = list(map(lambda word: word.strip('"'), words.strip("\r\n").split(","))) # assignment, composition, function_call:list, function_call:map, lambda_function, literal:Str, method_call:split, method_call:strip, method_chaining
    words = list( # assignment, composition, function_call:list
        filter( # composition, function_call:filter
            lambda word: word in TRIANGULAR_NUMBERS, # comparison_operator:In, lambda_function
            map(lambda word: sum(map(lambda x: ord(x) - 64, word)), words), # binary_operator:Sub, composition, function_call:map, function_call:ord, function_call:sum, lambda_function, literal:Num, suggest_constant_definition
        )
    )
    return len(words) # function_call:len

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_48/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +4)
    total = 0 # assignment, literal:Num
    for i in range(1, 1001): # accumulate_elements:AugAssign (-> +1), for_range_start (-> +1), function_call:range, literal:Num, suggest_constant_definition
        total += i ** i # augmented_assignment, binary_operator:Pow
    return str(total)[-10:] # function_call:str, literal:Num, slice, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_52/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function:solution (-> +12)
    i = 1 # assignment, literal:Num
    while True: # literal:True
        if ( # if (-> +8)
            sorted(list(str(i))) # chained_comparison:5, composition, function_call:list, function_call:sorted, function_call:str
            == sorted(list(str(2 * i))) # binary_operator:Mult, comparison_operator:Eq, composition, function_call:list, function_call:sorted, function_call:str, literal:Num
            == sorted(list(str(3 * i))) # binary_operator:Mult, composition, function_call:list, function_call:sorted, function_call:str, literal:Num, suggest_constant_definition
            == sorted(list(str(4 * i))) # binary_operator:Mult, composition, function_call:list, function_call:sorted, function_call:str, literal:Num, suggest_constant_definition
            == sorted(list(str(5 * i))) # binary_operator:Mult, composition, function_call:list, function_call:sorted, function_call:str, literal:Num, suggest_constant_definition
            == sorted(list(str(6 * i))) # binary_operator:Mult, composition, function_call:list, function_call:sorted, function_call:str, literal:Num, suggest_constant_definition
        ):
            return i
        i += 1 # augmented_assignment, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_53/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial # import_from:math
def combinations(n, r): # function:combinations (-> +1)
    return factorial(n) / (factorial(r) * factorial(n - r)) # binary_operator:Div, binary_operator:Mult, binary_operator:Sub, function_call:factorial
def solution(): # function:solution (-> +6)
    total = 0 # assignment, literal:Num
    for i in range(1, 101): # for_range_start (-> +3), function_call:range, literal:Num, nested_for (-> +3), suggest_constant_definition
        for j in range(1, i + 1): # binary_operator:Add, for_range_start (-> +2), function_call:range, literal:Num
            if combinations(i, j) > 1e6: # comparison_operator:Gt, function_call:combinations, if (-> +1), literal:Num, suggest_constant_definition
                total += 1 # augmented_assignment, literal:Num
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_551/sol1.py
# ----------------------------------------------------------------------------------------
ks = [k for k in range(2, 20 + 1)] # assignment, binary_operator:Add, comprehension:List, comprehension_for_count:1, function_call:range, global_variable_definition, literal:Num
base = [10 ** k for k in range(ks[-1] + 1)] # assignment, binary_operator:Add, binary_operator:Pow, comprehension:List, comprehension_for_count:1, function_call:range, global_variable_definition, index, literal:Num, negative_index:-1
memo = {} # assignment, global_variable_definition, literal:Dict
def next_term(a_i, k, i, n): # function:next_term (-> +50), recursive_function:next_term (-> +50)
    ds_b = 0 # assignment, literal:Num
    for j in range(k, len(a_i)): # accumulate_elements:AugAssign (-> +1), composition, for_range_start (-> +1), function_call:len, function_call:range
        ds_b += a_i[j] # augmented_assignment, index
    c = 0 # assignment, literal:Num
    for j in range(min(len(a_i), k)): # accumulate_elements:AugAssign (-> +1), composition, for_range_stop (-> +1), function_call:len, function_call:min, function_call:range
        c += a_i[j] * base[j] # augmented_assignment, binary_operator:Mult, index
    diff, dn = 0, 0 # assignment, literal:Num, literal:Tuple
    max_dn = n - i # assignment, binary_operator:Sub
    sub_memo = memo.get(ds_b) # assignment, method_call:get
    if sub_memo != None: # comparison_operator:NotEq, if (-> +19), if_else (-> +19), literal:None
        jumps = sub_memo.get(c) # assignment, method_call:get
        if jumps != None and len(jumps) > 0: # boolean_operator:And, comparison_operator:Gt, comparison_operator:NotEq, function_call:len, if (-> +14), if_else (-> +14), literal:None, literal:Num
            max_jump = -1 # assignment, literal:Num
            for _k in range(len(jumps) - 1, -1, -1): # binary_operator:Sub, composition, for_range_step:-1 (-> +3), function_call:len, function_call:range, literal:Num
                if jumps[_k][2] <= k and jumps[_k][1] <= max_dn: # boolean_operator:And, comparison_operator:LtE, if (-> +2), index, literal:Num
                    max_jump = _k # assignment
                    break
            if max_jump >= 0: # comparison_operator:GtE, if (-> +6), literal:Num
                diff, dn, _kk = jumps[max_jump] # assignment, index
                new_c = diff + c # assignment, binary_operator:Add
                for j in range(min(k, len(a_i))): # composition, for_range_stop (-> +1), function_call:len, function_call:min, function_call:range
                    new_c, a_i[j] = divmod(new_c, 10) # assignment, function_call:divmod, index, literal:Num, suggest_constant_definition
                if new_c > 0: # comparison_operator:Gt, if (-> +1), literal:Num
                    add(a_i, k, new_c) # function_call:add
        else:
            sub_memo[c] = [] # assignment, index, literal:List
    else:
        sub_memo = {c: []} # assignment, literal:List
        memo[ds_b] = sub_memo # assignment, index
    if dn >= max_dn or c + diff >= base[k]: # binary_operator:Add, boolean_operator:Or, comparison_operator:GtE, if (-> +1), index
        return diff, dn
    if k > ks[0]: # comparison_operator:Gt, if (-> +10), if_else (-> +10), index, literal:Num
        while True: # literal:True
            _diff, terms_jumped = next_term(a_i, k - 1, i + dn, n) # assignment, binary_operator:Add, binary_operator:Sub, function_call:next_term, literal:Num
            diff += _diff # augmented_assignment
            dn += terms_jumped # augmented_assignment
            if dn >= max_dn or c + diff >= base[k]: # binary_operator:Add, boolean_operator:Or, comparison_operator:GtE, if (-> +1), index
                break
    else:
        _diff, terms_jumped = compute(a_i, k, i + dn, n) # assignment, binary_operator:Add, function_call:compute
        diff += _diff # augmented_assignment
        dn += terms_jumped # augmented_assignment
    jumps = sub_memo[c] # assignment, index
    j = 0 # assignment, literal:Num
    while j < len(jumps): # comparison_operator:Lt, function_call:len
        if jumps[j][1] > dn: # comparison_operator:Gt, if (-> +1), index, literal:Num
            break
        j += 1 # augmented_assignment, literal:Num
    sub_memo[c].insert(j, (diff, dn, k)) # index, method_call:insert
    return (diff, dn)
def compute(a_i, k, i, n): # function:compute (-> +25)
    if i >= n: # comparison_operator:GtE, if (-> +1)
        return 0, i # literal:Num
    if k > len(a_i): # comparison_operator:Gt, function_call:len, if (-> +1)
        a_i.extend([0 for _ in range(k - len(a_i))]) # binary_operator:Sub, composition, comprehension:List, comprehension_for_count:1, function_call:len, function_call:range, literal:Num, method_call:extend
    start_i = i # assignment
    ds_b, ds_c, diff = 0, 0, 0 # assignment, literal:Num, literal:Tuple
    for j in range(len(a_i)): # accumulate_elements:AugAssign (-> +4), composition, for_indexes (-> +4), for_range_stop (-> +4), function_call:len, function_call:range
        if j >= k: # comparison_operator:GtE, if (-> +3), if_else (-> +3)
            ds_b += a_i[j] # augmented_assignment, index
        else:
            ds_c += a_i[j] # augmented_assignment, index
    while i < n: # comparison_operator:Lt
        i += 1 # augmented_assignment, literal:Num
        addend = ds_c + ds_b # assignment, binary_operator:Add
        diff += addend # augmented_assignment
        ds_c = 0 # assignment, literal:Num
        for j in range(k): # accumulate_elements:AugAssign (-> +3), for_range_stop (-> +3), function_call:range
            s = a_i[j] + addend # assignment, binary_operator:Add, index
            addend, a_i[j] = divmod(s, 10) # assignment, function_call:divmod, index, literal:Num, suggest_constant_definition
            ds_c += a_i[j] # augmented_assignment, index
        if addend > 0: # comparison_operator:Gt, if (-> +1), literal:Num
            break
    if addend > 0: # comparison_operator:Gt, if (-> +1), literal:Num
        add(a_i, k, addend) # function_call:add
    return diff, i - start_i # binary_operator:Sub
def add(digits, k, addend): # function:add (-> +13)
    for j in range(k, len(digits)): # composition, for_range_start (-> +9), function_call:len, function_call:range
        s = digits[j] + addend # assignment, binary_operator:Add, index
        if s >= 10: # comparison_operator:GtE, if (-> +5), if_else (-> +5), literal:Num, suggest_constant_definition
            quotient, digits[j] = divmod(s, 10) # assignment, function_call:divmod, index, literal:Num, suggest_constant_definition
            addend = addend // 10 + quotient # assignment, binary_operator:Add, binary_operator:FloorDiv, literal:Num, suggest_constant_definition
        else:
            digits[j] = s # assignment, index
            addend = addend // 10 # assignment, binary_operator:FloorDiv, literal:Num, suggest_augmented_assignment, suggest_constant_definition
        if addend == 0: # comparison_operator:Eq, if (-> +1), literal:Num
            break
    while addend > 0: # comparison_operator:Gt, literal:Num
        addend, digit = divmod(addend, 10) # assignment, function_call:divmod, literal:Num, suggest_constant_definition
        digits.append(digit) # method_call:append
def solution(n): # function:solution (-> +12)
    digits = [1] # assignment, literal:List, literal:Num
    i = 1 # assignment, literal:Num
    dn = 0 # assignment, literal:Num
    while True: # literal:True
        diff, terms_jumped = next_term(digits, 20, i + dn, n) # assignment, binary_operator:Add, function_call:next_term, literal:Num, suggest_constant_definition
        dn += terms_jumped # augmented_assignment
        if dn == n - i: # binary_operator:Sub, comparison_operator:Eq, if (-> +1)
            break
    a_n = 0 # assignment, literal:Num
    for j in range(len(digits)): # accumulate_elements:AugAssign (-> +1), composition, for_indexes (-> +1), for_range_stop (-> +1), function_call:len, function_call:range
        a_n += digits[j] * 10 ** j # augmented_assignment, binary_operator:Mult, binary_operator:Pow, index, literal:Num, suggest_constant_definition
    return a_n

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_56/sol1.py
# ----------------------------------------------------------------------------------------
def maximum_digital_sum(a: int, b: int) -> int: # function:maximum_digital_sum
    return max( # composition, function_call:max
        [
            sum([int(x) for x in str(base ** power)]) # binary_operator:Pow, composition, comprehension:List, comprehension_for_count:1, comprehension_for_count:2, function_call:int, function_call:str, function_call:sum
            for base in range(a) # function_call:range
            for power in range(b) # function_call:range
        ]
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_67/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os
def solution(): # function:solution (-> +18)
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, composition, method_call:dirname, method_call:realpath
    triangle = os.path.join(script_dir, "triangle.txt") # assignment, literal:Str, method_call:join
    with open(triangle, "r") as f: # function_call:open, literal:Str
        triangle = f.readlines() # assignment, method_call:readlines
    a = map(lambda x: x.rstrip("\r\n").split(" "), triangle) # assignment, composition, function_call:map, lambda_function, literal:Str, method_call:rstrip, method_call:split, method_chaining
    a = list(map(lambda x: list(map(lambda y: int(y), x)), a)) # assignment, composition, function_call:int, function_call:list, function_call:map, lambda_function
    for i in range(1, len(a)): # composition, for_range_start (-> +10), function_call:len, function_call:range, literal:Num, nested_for (-> +10)
        for j in range(len(a[i])): # composition, for_indexes (-> +9), for_range_stop (-> +9), function_call:len, function_call:range, index
            if j != len(a[i - 1]): # binary_operator:Sub, comparison_operator:NotEq, function_call:len, if (-> +3), if_else (-> +3), index, index_arithmetic, literal:Num, suggest_conditional_expression (-> +3)
                number1 = a[i - 1][j] # assignment, binary_operator:Sub, index, index_arithmetic, literal:Num
            else:
                number1 = 0 # assignment, literal:Num
            if j > 0: # comparison_operator:Gt, if (-> +3), if_else (-> +3), literal:Num, suggest_conditional_expression (-> +3)
                number2 = a[i - 1][j - 1] # assignment, binary_operator:Sub, index, index_arithmetic, literal:Num
            else:
                number2 = 0 # assignment, literal:Num
            a[i][j] += max(number1, number2) # augmented_assignment, function_call:max, index
    return max(a[-1]) # function_call:max, index, literal:Num, negative_index:-1

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_76/sol1.py
# ----------------------------------------------------------------------------------------
def partition(m): # function:partition (-> +9)
    memo = [[0 for _ in range(m)] for _ in range(m + 1)] # assignment, binary_operator:Add, comprehension:List, comprehension_for_count:1, function_call:range, literal:Num
    for i in range(m + 1): # binary_operator:Add, for_range_stop (-> +1), function_call:range, literal:Num
        memo[i][0] = 1 # assignment, index, literal:Num
    for n in range(m + 1): # accumulate_elements:AugAssign (-> +4), binary_operator:Add, for_range_stop (-> +4), function_call:range, literal:Num, nested_for (-> +4)
        for k in range(1, m): # accumulate_elements:AugAssign (-> +3), for_range_start (-> +3), function_call:range, literal:Num
            memo[n][k] += memo[n][k - 1] # augmented_assignment, binary_operator:Sub, index, index_arithmetic, literal:Num
            if n > k: # comparison_operator:Gt, if (-> +1)
                memo[n][k] += memo[n - k - 1][k] # augmented_assignment, binary_operator:Sub, index, index_arithmetic, literal:Num
    return memo[m][m - 1] - 1 # binary_operator:Sub, index, index_arithmetic, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_99/sol1.py
# ----------------------------------------------------------------------------------------
import os # import:os
from math import log10 # import_from:math
def find_largest(data_file: str = "base_exp.txt") -> int: # function:find_largest, function_with_default_positional_arguments:find_largest, literal:Str
    largest = [0, 0] # assignment, literal:List, literal:Num
    for i, line in enumerate(open(os.path.join(os.path.dirname(__file__), data_file))): # composition, for_indexes_elements (-> +3), function_call:enumerate, function_call:open, method_call:dirname, method_call:join
        a, x = list(map(int, line.split(","))) # assignment, composition, function_call:list, function_call:map, literal:Str, method_call:split
        if x * log10(a) > largest[0]: # binary_operator:Mult, comparison_operator:Gt, function_call:log10, if (-> +1), index, literal:Num
            largest = [x * log10(a), i + 1] # assignment, binary_operator:Add, binary_operator:Mult, function_call:log10, literal:Num
    return largest[1] # index, literal:Num
