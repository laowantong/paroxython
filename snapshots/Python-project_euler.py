# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    return sum([e for e in range(3, n) if e % 3 == 0 or e % 5 == 0]) # binary_operator-Mod, boolean_operator-Or, builtin_function_call-range, builtin_function_call-sum, comparison_operator-Eq, composition, divisibility_test-3, divisibility_test-5, literal-Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    sum = 0 # assignment, literal-Num
    terms = (n - 1) // 3 # assignment, binary_operator-FloorDiv, binary_operator-Sub, literal-Num, suggest_constant_definition
    sum += ((terms) * (6 + (terms - 1) * 3)) // 2  # sum of an A.P. # augmented_assignment, binary_operator-Add, binary_operator-FloorDiv, binary_operator-Mult, binary_operator-Sub, literal-Num, suggest_constant_definition
    terms = (n - 1) // 5 # assignment, binary_operator-FloorDiv, binary_operator-Sub, literal-Num, suggest_constant_definition
    sum += ((terms) * (10 + (terms - 1) * 5)) // 2 # augmented_assignment, binary_operator-Add, binary_operator-FloorDiv, binary_operator-Mult, binary_operator-Sub, literal-Num, suggest_constant_definition
    terms = (n - 1) // 15 # assignment, binary_operator-FloorDiv, binary_operator-Sub, literal-Num, suggest_constant_definition
    sum -= ((terms) * (30 + (terms - 1) * 15)) // 2 # augmented_assignment, binary_operator-Add, binary_operator-FloorDiv, binary_operator-Mult, binary_operator-Sub, literal-Num, suggest_constant_definition
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    sum = 0 # assignment, literal-Num
    num = 0 # assignment, literal-Num
    while 1: # literal-Num
        num += 3 # augmented_assignment, literal-Num, suggest_constant_definition
        if num >= n: # comparison_operator-GtE, if
            break
        sum += num # augmented_assignment
        num += 2 # augmented_assignment, literal-Num
        if num >= n: # comparison_operator-GtE, if
            break
        sum += num # augmented_assignment
        num += 1 # augmented_assignment, literal-Num
        if num >= n: # comparison_operator-GtE, if
            break
        sum += num # augmented_assignment
        num += 3 # augmented_assignment, literal-Num, suggest_constant_definition
        if num >= n: # comparison_operator-GtE, if
            break
        sum += num # augmented_assignment
        num += 1 # augmented_assignment, literal-Num
        if num >= n: # comparison_operator-GtE, if
            break
        sum += num # augmented_assignment
        num += 2 # augmented_assignment, literal-Num
        if num >= n: # comparison_operator-GtE, if
            break
        sum += num # augmented_assignment
        num += 3 # augmented_assignment, literal-Num, suggest_constant_definition
        if num >= n: # comparison_operator-GtE, if
            break
        sum += num # augmented_assignment
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    xmulti = [] # assignment, literal-List
    zmulti = [] # assignment, literal-List
    z = 3 # assignment, literal-Num, suggest_constant_definition
    x = 5 # assignment, literal-Num, suggest_constant_definition
    temp = 1 # assignment, literal-Num
    while True: # literal-True
        result = z * temp # assignment, binary_operator-Mult
        if result < n: # comparison_operator-Lt, if, if_else
            zmulti.append(result) # mutable_sequence_method_call-append
            temp += 1 # augmented_assignment, literal-Num
        else:
            temp = 1 # assignment, literal-Num
            break
    while True: # literal-True
        result = x * temp # assignment, binary_operator-Mult
        if result < n: # comparison_operator-Lt, if, if_else
            xmulti.append(result) # mutable_sequence_method_call-append
            temp += 1 # augmented_assignment, literal-Num
        else:
            break
    collection = list(set(xmulti + zmulti)) # assignment, binary_operator-Add, builtin_function_call-list, builtin_function_call-set, composition
    return sum(collection) # builtin_function_call-sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0]) # binary_operator-Mod, boolean_operator-Or, builtin_function_call-range, builtin_function_call-sum, comparison_operator-Eq, composition, divisibility_test-3, divisibility_test-5, literal-Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol6.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    a = 3 # assignment, literal-Num, suggest_constant_definition
    result = 0 # assignment, literal-Num
    while a < n: # comparison_operator-Lt
        if a % 3 == 0 or a % 5 == 0: # binary_operator-Mod, boolean_operator-Or, comparison_operator-Eq, divisibility_test-3, divisibility_test-5, if, if_elif, literal-Num, suggest_constant_definition
            result += a # augmented_assignment
        elif a % 15 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-15, if, literal-Num, suggest_constant_definition
            result -= a # augmented_assignment
        a += 1 # augmented_assignment, literal-Num
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_01/sol7.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    result = 0 # assignment, literal-Num
    for i in range(n): # accumulate_elements-AugAssign (-> +2), builtin_function_call-range, for_range_stop
        if i % 3 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-3, if, if_elif, literal-Num, suggest_constant_definition
            result += i # augmented_assignment
        elif i % 5 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-5, if, literal-Num, suggest_constant_definition
            result += i # augmented_assignment
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    i = 1 # assignment, literal-Num
    j = 2 # assignment, literal-Num
    sum = 0 # assignment, literal-Num
    while j <= n: # comparison_operator-LtE
        if j % 2 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-2, if, literal-Num
            sum += j # augmented_assignment
        i, j = j, i + j # assignment, binary_operator-Add
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    ls = [] # assignment, literal-List
    a, b = 0, 1 # assignment, literal-Num, literal-Tuple
    while b <= n: # comparison_operator-LtE
        if b % 2 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-2, if, literal-Num
            ls.append(b) # mutable_sequence_method_call-append
        a, b = b, a + b # assignment, binary_operator-Add
    return ls

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    if n <= 1: # comparison_operator-LtE, if, literal-Num
        return 0 # literal-Num
    a = 0 # assignment, literal-Num
    b = 2 # assignment, literal-Num
    count = 0 # assignment, literal-Num
    while 4 * b + a <= n: # binary_operator-Add, binary_operator-Mult, comparison_operator-LtE, literal-Num, suggest_constant_definition
        a, b = b, 4 * b + a # assignment, binary_operator-Add, binary_operator-Mult, literal-Num, suggest_constant_definition
        count += a # augmented_assignment
    return count + b # binary_operator-Add

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol4.py
# ----------------------------------------------------------------------------------------
import math
from decimal import Decimal, getcontext
def solution(n): # function_definition
    try:
        n = int(n) # assignment, builtin_function_call-int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # literal-Str
    if n <= 0: # comparison_operator-LtE, if, literal-Num
        raise ValueError("Parameter n must be greater or equal to one.") # literal-Str
    getcontext().prec = 100 # assignment, literal-Num, suggest_constant_definition
    phi = (Decimal(5) ** Decimal(0.5) + 1) / Decimal(2) # assignment, binary_operator-Add, binary_operator-Div, binary_operator-Pow, literal-Num, suggest_constant_definition
    index = (math.floor(math.log(n * (phi + 2), phi) - 1) // 3) * 3 + 2 # assignment, binary_operator-Add, binary_operator-FloorDiv, binary_operator-Mult, binary_operator-Sub, composition, literal-Num, suggest_constant_definition
    num = Decimal(round(phi ** Decimal(index + 1))) / (phi + 2) # assignment, binary_operator-Add, binary_operator-Div, binary_operator-Pow, builtin_function_call-round, composition, literal-Num
    sum = num // 2 # assignment, binary_operator-FloorDiv, literal-Num
    return int(sum) # builtin_function_call-int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_02/sol5.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    a = [0, 1] # assignment, literal-List, literal-Num
    i = 0 # assignment, literal-Num
    while a[i] <= n: # comparison_operator-LtE, index
        a.append(a[i] + a[i + 1]) # binary_operator-Add, index, literal-Num, mutable_sequence_method_call-append
        if a[i + 2] > n: # binary_operator-Add, comparison_operator-Gt, if, index, literal-Num
            break
        i += 1 # augmented_assignment, literal-Num
    sum = 0 # assignment, literal-Num
    for j in range(len(a) - 1): # accumulate_elements-AugAssign (-> +2), binary_operator-Sub, builtin_function_call-len, builtin_function_call-range, composition, for_range_stop, literal-Num
        if a[j] % 2 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-2, if, index, literal-Num
            sum += a[j] # augmented_assignment, index
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol1.py
# ----------------------------------------------------------------------------------------
import math
def isprime(no): # function_definition
    if no == 2: # comparison_operator-Eq, if, if_elif, literal-Num
        return True # literal-True
    elif no % 2 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-2, if, literal-Num
        return False # literal-False
    sq = int(math.sqrt(no)) + 1 # assignment, binary_operator-Add, builtin_function_call-int, composition, literal-Num
    for i in range(3, sq, 2): # builtin_function_call-range, for_range_step, literal-Num, suggest_constant_definition, universal_quantifier (-> +3)
        if no % i == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test, if, literal-Num
            return False # literal-False
    return True # literal-True
def solution(n): # function_definition
    try:
        n = int(n) # assignment, builtin_function_call-int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # literal-Str
    if n <= 0: # comparison_operator-LtE, if, literal-Num
        raise ValueError("Parameter n must be greater or equal to one.") # literal-Str
    maxNumber = 0 # assignment, literal-Num
    if isprime(n): # if, if_else
        return n
    else:
        while n % 2 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-2, evolve_state (-> +1), literal-Num
            n = n / 2 # assignment, binary_operator-Div, literal-Num, suggest_augmented_assignment
        if isprime(n): # if, if_else
            return int(n) # builtin_function_call-int
        else:
            n1 = int(math.sqrt(n)) + 1 # assignment, binary_operator-Add, builtin_function_call-int, composition, literal-Num
            for i in range(3, n1, 2): # builtin_function_call-range, for_range_step, literal-Num, suggest_constant_definition
                if n % i == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test, if, literal-Num
                    if isprime(n / i): # binary_operator-Div, if, if_elif
                        maxNumber = n / i # assignment, binary_operator-Div
                        break
                    elif isprime(i): # if
                        maxNumber = i # assignment
            return maxNumber

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    try:
        n = int(n) # assignment, builtin_function_call-int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # literal-Str
    if n <= 0: # comparison_operator-LtE, if, literal-Num
        raise ValueError("Parameter n must be greater or equal to one.") # literal-Str
    prime = 1 # assignment, literal-Num
    i = 2 # assignment, literal-Num
    while i * i <= n: # binary_operator-Mult, comparison_operator-LtE, evolve_state (-> +3)
        while n % i == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test, literal-Num
            prime = i # assignment
            n //= i # augmented_assignment
        i += 1 # augmented_assignment, literal-Num
    if n > 1: # comparison_operator-Gt, if, literal-Num
        prime = n # assignment
    return int(prime) # builtin_function_call-int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_03/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n: int) -> int: # function_definition
    try:
        n = int(n) # assignment, builtin_function_call-int
    except (TypeError, ValueError):
        raise TypeError("Parameter n must be int or passive of cast to int.") # literal-Str
    if n <= 0: # comparison_operator-LtE, if, literal-Num
        raise ValueError("Parameter n must be greater or equal to one.") # literal-Str
    i = 2 # assignment, literal-Num
    ans = 0 # assignment, literal-Num
    if n == 2: # comparison_operator-Eq, if, literal-Num
        return 2 # literal-Num
    while n > 2: # comparison_operator-Gt, evolve_state (-> +5), literal-Num
        while n % i != 0: # binary_operator-Mod, comparison_operator-NotEq, divisibility_test, evolve_state (-> +1), literal-Num
            i += 1 # augmented_assignment, literal-Num
        ans = i # assignment
        while n % i == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test, literal-Num
            n = n / i # assignment, binary_operator-Div, suggest_augmented_assignment
        i += 1 # augmented_assignment, literal-Num
    return int(ans) # builtin_function_call-int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_04/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    for number in range(n - 1, 10000, -1): # binary_operator-Sub, builtin_function_call-range, find_first_element (-> +6), for_range_backwards, for_range_step, literal-Num, suggest_constant_definition, unary_operator-USub
        strNumber = str(number) # assignment, builtin_function_call-str
        if strNumber == strNumber[::-1]: # comparison_operator-Eq, if, literal-Num, slice_step, unary_operator-USub
            divisor = 999 # assignment, literal-Num, suggest_constant_definition
            while divisor != 99: # comparison_operator-NotEq, evolve_state (-> +3), literal-Num, suggest_constant_definition
                if (number % divisor == 0) and (len(str(int(number / divisor))) == 3): # binary_operator-Div, binary_operator-Mod, boolean_operator-And, builtin_function_call-int, builtin_function_call-len, builtin_function_call-str, comparison_operator-Eq, composition, divisibility_test, if, literal-Num, suggest_constant_definition
                    return number
                divisor -= 1 # augmented_assignment, literal-Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_04/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    answer = 0 # assignment, literal-Num
    for i in range(999, 99, -1):  # 3 digit nimbers range from 999 down to 100 # accumulate_elements-Assign (-> +4), builtin_function_call-range, for_range_backwards, for_range_step, literal-Num, nested_for, suggest_constant_definition, unary_operator-USub
        for j in range(999, 99, -1): # accumulate_elements-Assign (-> +3), builtin_function_call-range, for_range_backwards, for_range_step, literal-Num, suggest_constant_definition, unary_operator-USub
            t = str(i * j) # assignment, binary_operator-Mult, builtin_function_call-str
            if t == t[::-1] and i * j < n: # binary_operator-Mult, boolean_operator-And, comparison_operator-Eq, comparison_operator-Lt, if, literal-Num, slice_step, unary_operator-USub
                answer = max(answer, i * j) # assignment, binary_operator-Mult, builtin_function_call-max
    return answer

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_05/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    try:
        n = int(n) # assignment, builtin_function_call-int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # literal-Str
    if n <= 0: # comparison_operator-LtE, if, literal-Num
        raise ValueError("Parameter n must be greater or equal to one.") # literal-Str
    i = 0 # assignment, literal-Num
    while 1: # literal-Num
        i += n * (n - 1) # augmented_assignment, binary_operator-Mult, binary_operator-Sub, literal-Num
        nfound = 0 # assignment, literal-Num
        for j in range(2, n): # builtin_function_call-range, for_range_start, literal-Num
            if i % j != 0: # binary_operator-Mod, comparison_operator-NotEq, divisibility_test, if, literal-Num
                nfound = 1 # assignment, literal-Num
                break
        if nfound == 0: # comparison_operator-Eq, if, literal-Num
            if i == 0: # comparison_operator-Eq, if, literal-Num
                i = 1 # assignment, literal-Num
            return i

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_05/sol2.py
# ----------------------------------------------------------------------------------------
def gcd(x, y): # function_definition, recursive_function_definition (-> +1)
    return x if y == 0 else gcd(y, x % y) # binary_operator-Mod, comparison_operator-Eq, literal-Num
def lcm(x, y): # function_definition
    return (x * y) // gcd(x, y) # binary_operator-FloorDiv, binary_operator-Mult
def solution(n): # function_definition
    g = 1 # assignment, literal-Num
    for i in range(1, n + 1): # accumulate_elements-Assign (-> +1), binary_operator-Add, builtin_function_call-range, for_range_start, literal-Num
        g = lcm(g, i) # assignment
    return g

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    suma = 0 # assignment, literal-Num
    sumb = 0 # assignment, literal-Num
    for i in range(1, n + 1): # accumulate_elements-AugAssign (-> +2), binary_operator-Add, builtin_function_call-range, for_range_start, literal-Num
        suma += i ** 2 # augmented_assignment, binary_operator-Pow, literal-Num
        sumb += i # augmented_assignment
    sum = sumb ** 2 - suma # assignment, binary_operator-Pow, binary_operator-Sub, literal-Num
    return sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    suma = n * (n + 1) / 2 # assignment, binary_operator-Add, binary_operator-Div, binary_operator-Mult, literal-Num
    suma **= 2 # augmented_assignment, literal-Num
    sumb = n * (n + 1) * (2 * n + 1) / 6 # assignment, binary_operator-Add, binary_operator-Div, binary_operator-Mult, literal-Num, suggest_constant_definition
    return int(suma - sumb) # binary_operator-Sub, builtin_function_call-int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol3.py
# ----------------------------------------------------------------------------------------
import math
def solution(n): # function_definition
    sum_of_squares = sum([i * i for i in range(1, n + 1)]) # assignment, binary_operator-Add, binary_operator-Mult, builtin_function_call-range, builtin_function_call-sum, composition, literal-Num
    square_of_sum = int(math.pow(sum(range(1, n + 1)), 2)) # assignment, binary_operator-Add, builtin_function_call-int, builtin_function_call-range, builtin_function_call-sum, composition, literal-Num
    return square_of_sum - sum_of_squares # binary_operator-Sub

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_06/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6 # assignment, binary_operator-Add, binary_operator-Div, binary_operator-Mult, literal-Num, suggest_constant_definition
    square_of_sum = (n * (n + 1) / 2) ** 2 # assignment, binary_operator-Add, binary_operator-Div, binary_operator-Mult, binary_operator-Pow, literal-Num
    return int(square_of_sum - sum_of_squares) # binary_operator-Sub, builtin_function_call-int

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt
def isprime(n): # function_definition
    if n == 2: # comparison_operator-Eq, if, if_elif, literal-Num
        return True # literal-True
    elif n % 2 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-2, if, if_else, literal-Num
        return False # literal-False
    else:
        sq = int(sqrt(n)) + 1 # assignment, binary_operator-Add, builtin_function_call-int, composition, literal-Num
        for i in range(3, sq, 2): # builtin_function_call-range, for_range_step, literal-Num, suggest_constant_definition
            if n % i == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test, if, literal-Num
                return False # literal-False
    return True # literal-True
def solution(n): # function_definition
    i = 0 # assignment, literal-Num
    j = 1 # assignment, literal-Num
    while i != n and j < 3: # boolean_operator-And, comparison_operator-Lt, comparison_operator-NotEq, evolve_state (-> +1), literal-Num, suggest_constant_definition
        j += 1 # augmented_assignment, literal-Num
        if isprime(j): # if
            i += 1 # augmented_assignment, literal-Num
    while i != n: # comparison_operator-NotEq
        j += 2 # augmented_assignment, literal-Num
        if isprime(j): # if
            i += 1 # augmented_assignment, literal-Num
    return j

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol2.py
# ----------------------------------------------------------------------------------------
def isprime(number): # function_definition
    for i in range(2, int(number ** 0.5) + 1): # binary_operator-Add, binary_operator-Pow, builtin_function_call-int, builtin_function_call-range, composition, for_range_start, literal-Num, suggest_constant_definition, universal_quantifier (-> +3)
        if number % i == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test, if, literal-Num
            return False # literal-False
    return True # literal-True
def solution(n): # function_definition
    try:
        n = int(n) # assignment, builtin_function_call-int
    except (TypeError, ValueError) as e:
        raise TypeError("Parameter n must be int or passive of cast to int.") # literal-Str
    if n <= 0: # comparison_operator-LtE, if, literal-Num
        raise ValueError("Parameter n must be greater or equal to one.") # literal-Str
    primes = [] # assignment, literal-List
    num = 2 # assignment, literal-Num
    while len(primes) < n: # builtin_function_call-len, comparison_operator-Lt
        if isprime(num): # if, if_else
            primes.append(num) # mutable_sequence_method_call-append
            num += 1 # augmented_assignment, literal-Num
        else:
            num += 1 # augmented_assignment, literal-Num
    return primes[len(primes) - 1] # binary_operator-Sub, builtin_function_call-len, index, literal-Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_07/sol3.py
# ----------------------------------------------------------------------------------------
import math
import itertools
def primeCheck(number): # function_definition
    if number % 2 == 0 and number > 2: # binary_operator-Mod, boolean_operator-And, comparison_operator-Eq, comparison_operator-Gt, divisibility_test-2, if, literal-Num
        return False # literal-False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # binary_operator-Add, binary_operator-Mod, builtin_function_call-all, builtin_function_call-int, builtin_function_call-range, composition, literal-Num, suggest_constant_definition
def prime_generator(): # function_definition
    num = 2 # assignment, literal-Num
    while True: # literal-True
        if primeCheck(num): # if
            yield num
        num += 1 # augmented_assignment, literal-Num
def solution(n): # function_definition
    return next(itertools.islice(prime_generator(), n - 1, n)) # binary_operator-Sub, builtin_function_call-next, composition, literal-Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol1.py
# ----------------------------------------------------------------------------------------
import sys
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
71636269561882670428252483600823257530420752963450""" # literal-Str
def solution(n): # function_definition
    LargestProduct = -sys.maxsize - 1 # assignment, binary_operator-Sub, literal-Num, unary_operator-USub
    for i in range(len(n) - 12): # accumulate_elements-AugAssign (-> +3), binary_operator-Sub, builtin_function_call-len, builtin_function_call-range, composition, for_range_stop, literal-Num, suggest_constant_definition
        product = 1 # assignment, literal-Num
        for j in range(13): # accumulate_elements-AugAssign (-> +1), builtin_function_call-range, for_range_stop, literal-Num, suggest_constant_definition
            product *= int(n[i + j]) # augmented_assignment, binary_operator-Add, builtin_function_call-int, index
        if product > LargestProduct: # comparison_operator-Gt, if
            LargestProduct = product # assignment
    return LargestProduct

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol2.py
# ----------------------------------------------------------------------------------------
from functools import reduce
N = ( # assignment, global_constant_definition
    "73167176531330624919225119674426574742355349194934" # literal-Str
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
def solution(n): # function_definition
    return max( # builtin_function_call-max, composition
        [
            reduce(lambda x, y: int(x) * int(y), n[i : i + 13]) # binary_operator-Add, binary_operator-Mult, builtin_function_call-int, composition, literal-Num, slice, suggest_constant_definition
            for i in range(len(n) - 12) # binary_operator-Sub, builtin_function_call-len, builtin_function_call-range, composition, literal-Num, suggest_constant_definition
        ]
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_08/sol3.py
# ----------------------------------------------------------------------------------------
import sys
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
71636269561882670428252483600823257530420752963450""" # literal-Str
def streval(s: str) -> int: # function_definition
    ret = 1 # assignment, literal-Num
    for it in s: # accumulate_elements-AugAssign (-> +1), for_each
        ret *= int(it) # augmented_assignment, builtin_function_call-int
    return ret
def solution(n: str) -> int: # function_definition
    LargestProduct = -sys.maxsize - 1 # assignment, binary_operator-Sub, literal-Num, unary_operator-USub
    substr = n[:13] # assignment, literal-Num, slice, suggest_constant_definition
    cur_index = 13 # assignment, literal-Num, suggest_constant_definition
    while cur_index < len(n) - 13: # binary_operator-Sub, builtin_function_call-len, comparison_operator-Lt, literal-Num, suggest_constant_definition
        if int(n[cur_index]) >= int(substr[0]): # builtin_function_call-int, comparison_operator-GtE, if, if_else, index, literal-Num
            substr = substr[1:] + n[cur_index] # assignment, binary_operator-Add, index, literal-Num, slice
            cur_index += 1 # augmented_assignment, literal-Num
        else:
            LargestProduct = max(LargestProduct, streval(substr)) # assignment, builtin_function_call-max, composition
            substr = n[cur_index : cur_index + 13] # assignment, binary_operator-Add, literal-Num, slice, suggest_constant_definition
            cur_index += 13 # augmented_assignment, literal-Num, suggest_constant_definition
    return LargestProduct

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function_definition
    for a in range(300): # builtin_function_call-range, for_range_stop, literal-Num, nested_for, suggest_constant_definition
        for b in range(400): # builtin_function_call-range, for_range_stop, literal-Num, nested_for, suggest_constant_definition
            for c in range(500): # builtin_function_call-range, for_range_stop, literal-Num, suggest_constant_definition
                if a < b < c: # comparison_operator-Lt, if
                    if (a ** 2) + (b ** 2) == (c ** 2): # binary_operator-Add, binary_operator-Pow, comparison_operator-Eq, if, literal-Num
                        if (a + b + c) == 1000: # binary_operator-Add, comparison_operator-Eq, if, literal-Num, suggest_constant_definition
                            return a * b * c # binary_operator-Mult

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol2.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    product = -1 # assignment, literal-Num, unary_operator-USub
    d = 0 # assignment, literal-Num
    for a in range(1, n // 3): # binary_operator-FloorDiv, builtin_function_call-range, for_range_start, literal-Num, suggest_constant_definition
        b = (n * n - 2 * a * n) // (2 * n - 2 * a) # assignment, binary_operator-FloorDiv, binary_operator-Mult, binary_operator-Sub, literal-Num
        c = n - a - b # assignment, binary_operator-Sub
        if c * c == (a * a + b * b): # binary_operator-Add, binary_operator-Mult, comparison_operator-Eq, if
            d = a * b * c # assignment, binary_operator-Mult
            if d >= product: # comparison_operator-GtE, if
                product = d # assignment
    return product

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_09/sol3.py
# ----------------------------------------------------------------------------------------
def solution(): # function_definition
    return [
        a * b * c # binary_operator-Mult, index
        for a in range(1, 999) # builtin_function_call-range, literal-Num, suggest_constant_definition
        for b in range(a, 999) # builtin_function_call-range, literal-Num, suggest_constant_definition
        for c in range(b, 999) # builtin_function_call-range, literal-Num, suggest_constant_definition
        if (a * a + b * b == c * c) and (a + b + c == 1000) # binary_operator-Add, binary_operator-Mult, boolean_operator-And, comparison_operator-Eq, literal-Num, suggest_constant_definition
    ][0] # literal-Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt
def is_prime(n): # function_definition
    for i in range(2, int(sqrt(n)) + 1): # binary_operator-Add, builtin_function_call-int, builtin_function_call-range, composition, for_range_start, literal-Num, universal_quantifier (-> +3)
        if n % i == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test, if, literal-Num
            return False # literal-False
    return True # literal-True
def sum_of_primes(n): # function_definition
    if n > 2: # comparison_operator-Gt, if, if_else, literal-Num
        sumOfPrimes = 2 # assignment, literal-Num
    else:
        return 0 # literal-Num
    for i in range(3, n, 2): # accumulate_elements-AugAssign (-> +2), builtin_function_call-range, for_range_step, literal-Num, suggest_constant_definition
        if is_prime(i): # if
            sumOfPrimes += i # augmented_assignment
    return sumOfPrimes
def solution(n): # function_definition
    return sum_of_primes(n)

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol2.py
# ----------------------------------------------------------------------------------------
import math
from itertools import takewhile
def primeCheck(number): # function_definition
    if number % 2 == 0 and number > 2: # binary_operator-Mod, boolean_operator-And, comparison_operator-Eq, comparison_operator-Gt, divisibility_test-2, if, literal-Num
        return False # literal-False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2)) # binary_operator-Add, binary_operator-Mod, builtin_function_call-all, builtin_function_call-int, builtin_function_call-range, composition, literal-Num, suggest_constant_definition
def prime_generator(): # function_definition
    num = 2 # assignment, literal-Num
    while True: # literal-True
        if primeCheck(num): # if
            yield num
        num += 1 # augmented_assignment, literal-Num
def solution(n): # function_definition
    return sum(takewhile(lambda x: x < n, prime_generator())) # builtin_function_call-sum, comparison_operator-Lt, composition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_10/sol3.py
# ----------------------------------------------------------------------------------------
def prime_sum(n: int) -> int: # function_definition
    list_ = [0 for i in range(n + 1)] # assignment, binary_operator-Add, builtin_function_call-range, literal-Num
    list_[0] = 1 # assignment, index, literal-Num
    list_[1] = 1 # assignment, index, literal-Num
    for i in range(2, int(n ** 0.5) + 1): # binary_operator-Add, binary_operator-Pow, builtin_function_call-int, builtin_function_call-range, composition, for_range_start, literal-Num, suggest_constant_definition
        if list_[i] == 0: # comparison_operator-Eq, if, index, literal-Num
            for j in range(i * i, n + 1, i): # binary_operator-Add, binary_operator-Mult, builtin_function_call-range, for_range_step, literal-Num
                list_[j] = 1 # assignment, index, literal-Num
    s = 0 # assignment, literal-Num
    for i in range(n): # accumulate_elements-AugAssign (-> +2), builtin_function_call-range, for_range_stop
        if list_[i] == 0: # comparison_operator-Eq, if, index, literal-Num
            s += i # augmented_assignment
    return s

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_11/sol1.py
# ----------------------------------------------------------------------------------------
import os
def largest_product(grid): # function_definition
    nColumns = len(grid[0]) # assignment, builtin_function_call-len, index, literal-Num
    nRows = len(grid) # assignment, builtin_function_call-len
    largest = 0 # assignment, literal-Num
    lrDiagProduct = 0 # assignment, literal-Num
    rlDiagProduct = 0 # assignment, literal-Num
    for i in range(nColumns): # builtin_function_call-range, for_range_stop, nested_for
        for j in range(nRows - 3): # binary_operator-Sub, builtin_function_call-range, for_range_stop, literal-Num, suggest_constant_definition
            vertProduct = grid[j][i] * grid[j + 1][i] * grid[j + 2][i] * grid[j + 3][i] # assignment, binary_operator-Add, binary_operator-Mult, index, literal-Num, suggest_constant_definition
            horzProduct = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3] # assignment, binary_operator-Add, binary_operator-Mult, index, literal-Num, suggest_constant_definition
            if i < nColumns - 3: # binary_operator-Sub, comparison_operator-Lt, if, literal-Num, suggest_constant_definition
                lrDiagProduct = ( # assignment
                    grid[i][j] # binary_operator-Mult, index
                    * grid[i + 1][j + 1] # binary_operator-Add, index, literal-Num
                    * grid[i + 2][j + 2] # binary_operator-Add, binary_operator-Mult, index, literal-Num
                    * grid[i + 3][j + 3] # binary_operator-Add, binary_operator-Mult, index, literal-Num, suggest_constant_definition
                )
            if i > 2: # comparison_operator-Gt, if, literal-Num
                rlDiagProduct = ( # assignment
                    grid[i][j] # binary_operator-Mult, index
                    * grid[i - 1][j + 1] # binary_operator-Add, binary_operator-Sub, index, literal-Num
                    * grid[i - 2][j + 2] # binary_operator-Add, binary_operator-Mult, binary_operator-Sub, index, literal-Num
                    * grid[i - 3][j + 3] # binary_operator-Add, binary_operator-Mult, binary_operator-Sub, index, literal-Num, suggest_constant_definition
                )
            maxProduct = max(vertProduct, horzProduct, lrDiagProduct, rlDiagProduct) # assignment, builtin_function_call-max
            if maxProduct > largest: # comparison_operator-Gt, if
                largest = maxProduct # assignment
    return largest
def solution(): # function_definition
    grid = [] # assignment, literal-List
    with open(os.path.dirname(__file__) + "/grid.txt") as file: # binary_operator-Add, builtin_function_call-open, composition, literal-Str
        for line in file: # for_each
            grid.append(line.strip("\n").split(" ")) # composition, literal-Str, method_chaining, mutable_sequence_method_call-append, string_method_call-strip
    grid = [[int(i) for i in grid[j]] for j in range(len(grid))] # assignment, builtin_function_call-int, builtin_function_call-len, builtin_function_call-range, composition, index
    return largest_product(grid)

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_11/sol2.py
# ----------------------------------------------------------------------------------------
import os
def solution(): # function_definition
    with open(os.path.dirname(__file__) + "/grid.txt") as f: # binary_operator-Add, builtin_function_call-open, composition, literal-Str
        l = [] # assignment, literal-List
        for i in range(20): # builtin_function_call-range, for_range_stop, literal-Num, suggest_constant_definition
            l.append([int(x) for x in f.readline().split()]) # builtin_function_call-int, composition, method_chaining, mutable_sequence_method_call-append
        maximum = 0 # assignment, literal-Num
        for i in range(20): # builtin_function_call-range, for_range_stop, literal-Num, nested_for, suggest_constant_definition
            for j in range(17): # builtin_function_call-range, for_range_stop, literal-Num, suggest_constant_definition
                temp = l[i][j] * l[i][j + 1] * l[i][j + 2] * l[i][j + 3] # assignment, binary_operator-Add, binary_operator-Mult, index, literal-Num, suggest_constant_definition
                if temp > maximum: # comparison_operator-Gt, if
                    maximum = temp # assignment
        for i in range(17): # builtin_function_call-range, for_range_stop, literal-Num, nested_for, suggest_constant_definition
            for j in range(20): # builtin_function_call-range, for_range_stop, literal-Num, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j] * l[i + 2][j] * l[i + 3][j] # assignment, binary_operator-Add, binary_operator-Mult, index, literal-Num, suggest_constant_definition
                if temp > maximum: # comparison_operator-Gt, if
                    maximum = temp # assignment
        for i in range(17): # builtin_function_call-range, for_range_stop, literal-Num, nested_for, suggest_constant_definition
            for j in range(17): # builtin_function_call-range, for_range_stop, literal-Num, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j + 1] * l[i + 2][j + 2] * l[i + 3][j + 3] # assignment, binary_operator-Add, binary_operator-Mult, index, literal-Num, suggest_constant_definition
                if temp > maximum: # comparison_operator-Gt, if
                    maximum = temp # assignment
        for i in range(17): # builtin_function_call-range, for_range_stop, literal-Num, nested_for, suggest_constant_definition
            for j in range(3, 20): # builtin_function_call-range, for_range_start, literal-Num, suggest_constant_definition
                temp = l[i][j] * l[i + 1][j - 1] * l[i + 2][j - 2] * l[i + 3][j - 3] # assignment, binary_operator-Add, binary_operator-Mult, binary_operator-Sub, index, literal-Num, suggest_constant_definition
                if temp > maximum: # comparison_operator-Gt, if
                    maximum = temp # assignment
        return maximum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_12/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt
def count_divisors(n): # function_definition
    nDivisors = 0 # assignment, literal-Num
    for i in range(1, int(sqrt(n)) + 1): # binary_operator-Add, builtin_function_call-int, builtin_function_call-range, composition, for_range_start, literal-Num
        if n % i == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test, if, literal-Num
            nDivisors += 2 # augmented_assignment, literal-Num
    if n ** 0.5 == int(n ** 0.5): # binary_operator-Pow, builtin_function_call-int, comparison_operator-Eq, if, literal-Num, suggest_constant_definition
        nDivisors -= 1 # augmented_assignment, literal-Num
    return nDivisors
def solution(): # function_definition
    tNum = 1 # assignment, literal-Num
    i = 1 # assignment, literal-Num
    while True: # literal-True
        i += 1 # augmented_assignment, literal-Num
        tNum += i # augmented_assignment
        if count_divisors(tNum) > 500: # comparison_operator-Gt, if, literal-Num, suggest_constant_definition
            break
    return tNum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_12/sol2.py
# ----------------------------------------------------------------------------------------
def triangle_number_generator(): # function_definition
    for n in range(1, 1000000): # builtin_function_call-range, for_range_start, literal-Num, suggest_constant_definition
        yield n * (n + 1) // 2 # binary_operator-Add, binary_operator-FloorDiv, binary_operator-Mult, literal-Num
def count_divisors(n): # function_definition
    return sum([2 for i in range(1, int(n ** 0.5) + 1) if n % i == 0 and i * i != n]) # binary_operator-Add, binary_operator-Mod, binary_operator-Mult, binary_operator-Pow, boolean_operator-And, builtin_function_call-int, builtin_function_call-range, builtin_function_call-sum, comparison_operator-Eq, comparison_operator-NotEq, composition, divisibility_test, literal-Num, suggest_constant_definition
def solution(): # function_definition
    return next(i for i in triangle_number_generator() if count_divisors(i) > 500) # builtin_function_call-next, comparison_operator-Gt, composition, literal-Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_13/sol1.py
# ----------------------------------------------------------------------------------------
def solution(array): # function_definition
    return str(sum(array))[:10] # builtin_function_call-str, builtin_function_call-sum, composition, literal-Num, slice, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_14/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    largest_number = 0 # assignment, literal-Num
    pre_counter = 0 # assignment, literal-Num
    for input1 in range(n): # builtin_function_call-range, for_range_stop
        counter = 1 # assignment, literal-Num
        number = input1 # assignment
        while number > 1: # comparison_operator-Gt, evolve_state (-> +5), literal-Num
            if number % 2 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-2, if, if_else, literal-Num
                number /= 2 # augmented_assignment, literal-Num
                counter += 1 # augmented_assignment, literal-Num
            else:
                number = (3 * number) + 1 # assignment, binary_operator-Add, binary_operator-Mult, literal-Num, suggest_constant_definition
                counter += 1 # augmented_assignment, literal-Num
        if counter > pre_counter: # comparison_operator-Gt, if
            largest_number = input1 # assignment
            pre_counter = counter # assignment
    return {"counter": pre_counter, "largest_number": largest_number} # literal-Str

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_14/sol2.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function_definition
    sequence = [n] # assignment
    while n != 1: # comparison_operator-NotEq, evolve_state (-> +4), literal-Num
        if n % 2 == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test-2, if, if_else, literal-Num
            n //= 2 # augmented_assignment, literal-Num
        else:
            n = 3 * n + 1 # assignment, binary_operator-Add, binary_operator-Mult, literal-Num, suggest_constant_definition
        sequence.append(n) # mutable_sequence_method_call-append
    return sequence
def solution(n): # function_definition
    result = max([(len(collatz_sequence(i)), i) for i in range(1, n)]) # assignment, builtin_function_call-len, builtin_function_call-max, builtin_function_call-range, composition, literal-Num
    return {"counter": result[0], "largest_number": result[1]} # index, literal-Num, literal-Str

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_15/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial
def lattice_paths(n): # function_definition
    n = 2 * n  # middle entry of odd rows starting at row 3 is the solution for n = 1, # assignment, binary_operator-Mult, literal-Num
    k = n / 2 # assignment, binary_operator-Div, literal-Num
    return int(factorial(n) / (factorial(k) * factorial(n - k))) # binary_operator-Div, binary_operator-Mult, binary_operator-Sub, builtin_function_call-int, composition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_16/sol1.py
# ----------------------------------------------------------------------------------------
def solution(power): # function_definition
    num = 2 ** power # assignment, binary_operator-Pow, literal-Num
    string_num = str(num) # assignment, builtin_function_call-str
    list_num = list(string_num) # assignment, builtin_function_call-list
    sum_of_num = 0 # assignment, literal-Num
    for i in list_num: # accumulate_elements-AugAssign (-> +1), for_each
        sum_of_num += int(i) # augmented_assignment, builtin_function_call-int
    return sum_of_num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_16/sol2.py
# ----------------------------------------------------------------------------------------
def solution(power): # function_definition
    n = 2 ** power # assignment, binary_operator-Pow, literal-Num
    r = 0 # assignment, literal-Num
    while n:
        r, n = r + n % 10, n // 10 # assignment, binary_operator-Add, binary_operator-FloorDiv, binary_operator-Mod, literal-Num, suggest_constant_definition
    return r

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_17/sol1.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    ones_counts = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8] # assignment, literal-List, literal-Num, suggest_constant_definition
    tens_counts = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6] # assignment, literal-List, literal-Num, suggest_constant_definition
    count = 0 # assignment, literal-Num
    for i in range(1, n + 1): # accumulate_elements-AugAssign (-> +7), binary_operator-Add, builtin_function_call-range, for_range_start, literal-Num
        if i < 1000: # comparison_operator-Lt, if, if_else, literal-Num, suggest_constant_definition
            if i >= 100: # comparison_operator-GtE, if, literal-Num, suggest_constant_definition
                count += ones_counts[i // 100] + 7 # augmented_assignment, binary_operator-Add, binary_operator-FloorDiv, index, literal-Num, suggest_constant_definition
                if i % 100 != 0: # binary_operator-Mod, comparison_operator-NotEq, divisibility_test-100, if, literal-Num, suggest_constant_definition
                    count += 3 # augmented_assignment, literal-Num, suggest_constant_definition
            if 0 < i % 100 < 20: # binary_operator-Mod, comparison_operator-Lt, if, if_else, literal-Num, suggest_constant_definition
                count += ones_counts[i % 100] # augmented_assignment, binary_operator-Mod, index, literal-Num, suggest_constant_definition
            else:
                count += ones_counts[i % 10] # augmented_assignment, binary_operator-Mod, index, literal-Num, suggest_constant_definition
                count += tens_counts[(i % 100 - i % 10) // 10] # augmented_assignment, binary_operator-FloorDiv, binary_operator-Mod, binary_operator-Sub, index, literal-Num, suggest_constant_definition
        else:
            count += ones_counts[i // 1000] + 8 # augmented_assignment, binary_operator-Add, binary_operator-FloorDiv, index, literal-Num, suggest_constant_definition
    return count

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_18/solution.py
# ----------------------------------------------------------------------------------------
import os
def solution(): # function_definition
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, composition
    triangle = os.path.join(script_dir, "triangle.txt") # assignment, literal-Str, string_method_call-join
    with open(triangle, "r") as f: # builtin_function_call-open, literal-Str
        triangle = f.readlines() # assignment
    a = [[int(y) for y in x.rstrip("\r\n").split(" ")] for x in triangle] # assignment, builtin_function_call-int, literal-Str, method_chaining, string_method_call-rstrip
    for i in range(1, len(a)): # builtin_function_call-len, builtin_function_call-range, composition, for_range_start, literal-Num, nested_for
        for j in range(len(a[i])): # builtin_function_call-len, builtin_function_call-range, composition, for_indexes, for_range_stop, index
            if j != len(a[i - 1]): # binary_operator-Sub, builtin_function_call-len, comparison_operator-NotEq, if, if_else, index, literal-Num, suggest_conditional_expression (-> +3)
                number1 = a[i - 1][j] # assignment, binary_operator-Sub, index, literal-Num
            else:
                number1 = 0 # assignment, literal-Num
            if j > 0: # comparison_operator-Gt, if, if_else, literal-Num, suggest_conditional_expression (-> +3)
                number2 = a[i - 1][j - 1] # assignment, binary_operator-Sub, index, literal-Num
            else:
                number2 = 0 # assignment, literal-Num
            a[i][j] += max(number1, number2) # augmented_assignment, builtin_function_call-max, index
    return max(a[-1]) # builtin_function_call-max, index, literal-Num, unary_operator-USub

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_19/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function_definition
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # assignment, literal-List, literal-Num, suggest_constant_definition
    day = 6 # assignment, literal-Num, suggest_constant_definition
    month = 1 # assignment, literal-Num
    year = 1901 # assignment, literal-Num, suggest_constant_definition
    sundays = 0 # assignment, literal-Num
    while year < 2001: # comparison_operator-Lt, evolve_state (-> +14), literal-Num, suggest_constant_definition
        day += 7 # augmented_assignment, literal-Num, suggest_constant_definition
        if (year % 4 == 0 and not year % 100 == 0) or (year % 400 == 0): # binary_operator-Mod, boolean_operator-And, boolean_operator-Or, comparison_operator-Eq, divisibility_test-100, divisibility_test-4, divisibility_test-400, if, if_elif, literal-Num, suggest_constant_definition, unary_operator-Not
            if day > days_per_month[month - 1] and month != 2: # binary_operator-Sub, boolean_operator-And, comparison_operator-Gt, comparison_operator-NotEq, if, if_elif, index, literal-Num
                month += 1 # augmented_assignment, literal-Num
                day = day - days_per_month[month - 2] # assignment, binary_operator-Sub, index, literal-Num, suggest_augmented_assignment
            elif day > 29 and month == 2: # boolean_operator-And, comparison_operator-Eq, comparison_operator-Gt, if, literal-Num, suggest_constant_definition
                month += 1 # augmented_assignment, literal-Num
                day = day - 29 # assignment, binary_operator-Sub, literal-Num, suggest_augmented_assignment, suggest_constant_definition
        else:
            if day > days_per_month[month - 1]: # binary_operator-Sub, comparison_operator-Gt, if, index, literal-Num
                month += 1 # augmented_assignment, literal-Num
                day = day - days_per_month[month - 2] # assignment, binary_operator-Sub, index, literal-Num, suggest_augmented_assignment
        if month > 12: # comparison_operator-Gt, if, literal-Num, suggest_constant_definition
            year += 1 # augmented_assignment, literal-Num
            month = 1 # assignment, literal-Num
        if year < 2001 and day == 1: # boolean_operator-And, comparison_operator-Eq, comparison_operator-Lt, if, literal-Num, suggest_constant_definition
            sundays += 1 # augmented_assignment, literal-Num
    return sundays

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol1.py
# ----------------------------------------------------------------------------------------
def factorial(n): # function_definition
    fact = 1 # assignment, literal-Num
    for i in range(1, n + 1): # accumulate_elements-AugAssign (-> +1), binary_operator-Add, builtin_function_call-range, for_range_start, literal-Num
        fact *= i # augmented_assignment
    return fact
def split_and_add(number): # function_definition
    sum_of_digits = 0 # assignment, literal-Num
    while number > 0: # comparison_operator-Gt, evolve_state (-> +3), literal-Num
        last_digit = number % 10 # assignment, binary_operator-Mod, literal-Num, suggest_constant_definition
        sum_of_digits += last_digit # augmented_assignment
        number = number // 10  # Removing the last_digit from the given number # assignment, binary_operator-FloorDiv, literal-Num, suggest_augmented_assignment, suggest_constant_definition
    return sum_of_digits
def solution(n): # function_definition
    f = factorial(n) # assignment
    result = split_and_add(f) # assignment
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol2.py
# ----------------------------------------------------------------------------------------
from math import factorial
def solution(n): # function_definition
    return sum([int(x) for x in str(factorial(n))]) # builtin_function_call-int, builtin_function_call-str, builtin_function_call-sum, composition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol3.py
# ----------------------------------------------------------------------------------------
from math import factorial
def solution(n): # function_definition
    return sum(map(int, str(factorial(n)))) # builtin_function_call-map, builtin_function_call-str, builtin_function_call-sum, composition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_20/sol4.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    fact = 1 # assignment, literal-Num
    result = 0 # assignment, literal-Num
    for i in range(1, n + 1): # accumulate_elements-AugAssign (-> +1), binary_operator-Add, builtin_function_call-range, for_range_start, literal-Num
        fact *= i # augmented_assignment
    for j in str(fact): # accumulate_elements-AugAssign (-> +1), builtin_function_call-str
        result += int(j) # augmented_assignment, builtin_function_call-int
    return result

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_21/sol1.py
# ----------------------------------------------------------------------------------------
from math import sqrt
def sum_of_divisors(n): # function_definition
    total = 0 # assignment, literal-Num
    for i in range(1, int(sqrt(n) + 1)): # accumulate_elements-AugAssign (-> +2), binary_operator-Add, builtin_function_call-int, builtin_function_call-range, composition, for_range_start, literal-Num
        if n % i == 0 and i != sqrt(n): # binary_operator-Mod, boolean_operator-And, comparison_operator-Eq, comparison_operator-NotEq, divisibility_test, if, if_elif, literal-Num
            total += i + n // i # augmented_assignment, binary_operator-Add, binary_operator-FloorDiv
        elif i == sqrt(n): # comparison_operator-Eq, if
            total += i # augmented_assignment
    return total - n # binary_operator-Sub
def solution(n): # function_definition
    total = sum( # assignment, builtin_function_call-sum, composition
        [
            i
            for i in range(1, n) # builtin_function_call-range, literal-Num
            if sum_of_divisors(sum_of_divisors(i)) == i and sum_of_divisors(i) != i # boolean_operator-And, comparison_operator-Eq, comparison_operator-NotEq, composition
        ]
    )
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_22/sol1.py
# ----------------------------------------------------------------------------------------
import os
def solution(): # function_definition
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator-Add, builtin_function_call-open, composition, literal-Str
        names = str(file.readlines()[0]) # assignment, builtin_function_call-str, composition, index, literal-Num
        names = names.replace('"', "").split(",") # assignment, literal-Str, method_chaining, string_method_call-replace
    names.sort() # list_method_call-sort
    name_score = 0 # assignment, literal-Num
    total_score = 0 # assignment, literal-Num
    for i, name in enumerate(names): # builtin_function_call-enumerate, for_indexes_values, nested_for
        for letter in name: # accumulate_elements-AugAssign (-> +1), for_each
            name_score += ord(letter) - 64 # augmented_assignment, binary_operator-Sub, builtin_function_call-ord, literal-Num, suggest_constant_definition
        total_score += (i + 1) * name_score # augmented_assignment, binary_operator-Add, binary_operator-Mult, literal-Num
        name_score = 0 # assignment, literal-Num
    return total_score

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_22/sol2.py
# ----------------------------------------------------------------------------------------
import os
def solution(): # function_definition
    total_sum = 0 # assignment, literal-Num
    temp_sum = 0 # assignment, literal-Num
    with open(os.path.dirname(__file__) + "/p022_names.txt") as file: # binary_operator-Add, builtin_function_call-open, composition, literal-Str
        name = str(file.readlines()[0]) # assignment, builtin_function_call-str, composition, index, literal-Num
        name = name.replace('"', "").split(",") # assignment, literal-Str, method_chaining, string_method_call-replace
    name.sort() # list_method_call-sort
    for i in range(len(name)): # accumulate_elements-AugAssign (-> +3), builtin_function_call-len, builtin_function_call-range, composition, for_indexes, for_range_stop, nested_for
        for j in name[i]: # accumulate_elements-AugAssign (-> +1), index
            temp_sum += ord(j) - ord("A") + 1 # augmented_assignment, binary_operator-Add, binary_operator-Sub, builtin_function_call-ord, literal-Num, literal-Str
        total_sum += (i + 1) * temp_sum # augmented_assignment, binary_operator-Add, binary_operator-Mult, literal-Num
        temp_sum = 0 # assignment, literal-Num
    return total_sum

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_23/sol1.py
# ----------------------------------------------------------------------------------------
def solution(limit=28123): # function_definition, literal-Num
    sumDivs = [1] * (limit + 1) # assignment, binary_operator-Add, binary_operator-Mult, literal-List, literal-Num
    for i in range(2, int(limit ** 0.5) + 1): # accumulate_elements-AugAssign (-> +3), binary_operator-Add, binary_operator-Pow, builtin_function_call-int, builtin_function_call-range, composition, for_range_start, literal-Num, suggest_constant_definition
        sumDivs[i * i] += i # augmented_assignment, binary_operator-Mult, index
        for k in range(i + 1, limit // i + 1): # accumulate_elements-AugAssign (-> +1), binary_operator-Add, binary_operator-FloorDiv, builtin_function_call-range, for_range_start, literal-Num
            sumDivs[k * i] += k + i # augmented_assignment, binary_operator-Add, binary_operator-Mult, index
    abundants = set() # assignment, builtin_function_call-set
    res = 0 # assignment, literal-Num
    for n in range(1, limit + 1): # accumulate_elements-AugAssign (-> +4), binary_operator-Add, builtin_function_call-range, for_range_start, literal-Num
        if sumDivs[n] > n: # comparison_operator-Gt, if, index
            abundants.add(n) # set_method_call-add
        if not any((n - a in abundants) for a in abundants): # binary_operator-Sub, builtin_function_call-any, comparison_operator-In, if, unary_operator-Not
            res += n # augmented_assignment
    return res

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_234/sol1.py
# ----------------------------------------------------------------------------------------
def fib(a, b, n): # function_definition
    if n == 1: # comparison_operator-Eq, if, if_elif, literal-Num
        return a
    elif n == 2: # comparison_operator-Eq, if, if_elif, literal-Num
        return b
    elif n == 3: # comparison_operator-Eq, if, literal-Num, suggest_constant_definition
        return str(a) + str(b) # binary_operator-Add, builtin_function_call-str
    temp = 0 # assignment, literal-Num
    for x in range(2, n): # builtin_function_call-range, for_range_start, literal-Num
        c = str(a) + str(b) # assignment, binary_operator-Add, builtin_function_call-str
        temp = b # assignment
        b = c # assignment
        a = temp # assignment
    return c
def solution(n): # function_definition
    semidivisible = [] # assignment, literal-List
    for x in range(n): # builtin_function_call-range, for_range_stop
        l = [i for i in input().split()] # assignment, builtin_function_call-input
        c2 = 1 # assignment, literal-Num
        while 1: # literal-Num
            if len(fib(l[0], l[1], c2)) < int(l[2]): # builtin_function_call-int, builtin_function_call-len, comparison_operator-Lt, composition, if, if_else, index, literal-Num
                c2 += 1 # augmented_assignment, literal-Num
            else:
                break
        semidivisible.append(fib(l[0], l[1], c2 + 1)[int(l[2]) - 1]) # binary_operator-Add, binary_operator-Sub, builtin_function_call-int, composition, index, literal-Num, mutable_sequence_method_call-append
    return semidivisible

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_24/sol1.py
# ----------------------------------------------------------------------------------------
from itertools import permutations
def solution(): # function_definition
    result = list(map("".join, permutations("0123456789"))) # assignment, builtin_function_call-list, builtin_function_call-map, composition, literal-Str
    return result[999999] # index, literal-Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol1.py
# ----------------------------------------------------------------------------------------
def fibonacci(n): # function_definition
    if n == 1 or type(n) is not int: # boolean_operator-Or, builtin_function_call-type, comparison_operator-Eq, comparison_operator-IsNot, if, if_elif, literal-Num
        return 0 # literal-Num
    elif n == 2: # comparison_operator-Eq, if, if_else, literal-Num
        return 1 # literal-Num
    else:
        sequence = [0, 1] # assignment, literal-List, literal-Num
        for i in range(2, n + 1): # binary_operator-Add, builtin_function_call-range, for_range_start, literal-Num
            sequence.append(sequence[i - 1] + sequence[i - 2]) # binary_operator-Add, binary_operator-Sub, index, literal-Num, mutable_sequence_method_call-append
        return sequence[n] # index
def fibonacci_digits_index(n): # function_definition
    digits = 0 # assignment, literal-Num
    index = 2 # assignment, literal-Num
    while digits < n: # comparison_operator-Lt
        index += 1 # augmented_assignment, literal-Num
        digits = len(str(fibonacci(index))) # assignment, builtin_function_call-len, builtin_function_call-str, composition
    return index
def solution(n): # function_definition
    return fibonacci_digits_index(n)

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol2.py
# ----------------------------------------------------------------------------------------
def fibonacci_generator(): # function_definition
    a, b = 0, 1 # assignment, literal-Num, literal-Tuple
    while True: # literal-True
        a, b = b, a + b # assignment, binary_operator-Add
        yield b
def solution(n): # function_definition
    answer = 1 # assignment, literal-Num
    gen = fibonacci_generator() # assignment
    while len(str(next(gen))) < n: # builtin_function_call-len, builtin_function_call-next, builtin_function_call-str, comparison_operator-Lt, composition
        answer += 1 # augmented_assignment, literal-Num
    return answer + 1 # binary_operator-Add, literal-Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_25/sol3.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    f1, f2 = 1, 1 # assignment, literal-Num, literal-Tuple
    index = 2 # assignment, literal-Num
    while True: # literal-True
        i = 0 # assignment, literal-Num
        f = f1 + f2 # assignment, binary_operator-Add
        f1, f2 = f2, f # assignment
        index += 1 # augmented_assignment, literal-Num
        for j in str(f): # builtin_function_call-str
            i += 1 # augmented_assignment, literal-Num
        if i == n: # comparison_operator-Eq, if
            break
    return index

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_27/problem_27_sol1.py
# ----------------------------------------------------------------------------------------
import math
def is_prime(k: int) -> bool: # function_definition
    if k < 2 or k % 2 == 0: # binary_operator-Mod, boolean_operator-Or, comparison_operator-Eq, comparison_operator-Lt, divisibility_test-2, if, if_elif, literal-Num
        return False # literal-False
    elif k == 2: # comparison_operator-Eq, if, if_else, literal-Num
        return True # literal-True
    else:
        for x in range(3, int(math.sqrt(k) + 1), 2): # binary_operator-Add, builtin_function_call-int, builtin_function_call-range, composition, for_range_step, literal-Num, suggest_constant_definition
            if k % x == 0: # binary_operator-Mod, comparison_operator-Eq, divisibility_test, if, literal-Num
                return False # literal-False
    return True # literal-True
def solution(a_limit: int, b_limit: int) -> int: # function_definition
    longest = [0, 0, 0]  # length, a, b # assignment, literal-List, literal-Num
    for a in range((a_limit * -1) + 1, a_limit): # binary_operator-Add, binary_operator-Mult, builtin_function_call-range, for_range_start, literal-Num, nested_for, unary_operator-USub
        for b in range(2, b_limit): # builtin_function_call-range, for_range_start, literal-Num
            if is_prime(b): # if
                count = 0 # assignment, literal-Num
                n = 0 # assignment, literal-Num
                while is_prime((n ** 2) + (a * n) + b): # binary_operator-Add, binary_operator-Mult, binary_operator-Pow, literal-Num
                    count += 1 # augmented_assignment, literal-Num
                    n += 1 # augmented_assignment, literal-Num
                if count > longest[0]: # comparison_operator-Gt, if, index, literal-Num
                    longest = [count, a, b] # assignment
    ans = longest[1] * longest[2] # assignment, binary_operator-Mult, index, literal-Num
    return ans

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_28/sol1.py
# ----------------------------------------------------------------------------------------
from math import ceil
def diagonal_sum(n): # function_definition
    total = 1 # assignment, literal-Num
    for i in range(1, int(ceil(n / 2.0))): # binary_operator-Div, builtin_function_call-int, builtin_function_call-range, composition, for_range_start, literal-Num, suggest_constant_definition
        odd = 2 * i + 1 # assignment, binary_operator-Add, binary_operator-Mult, literal-Num
        even = 2 * i # assignment, binary_operator-Mult, literal-Num
        total = total + 4 * odd ** 2 - 6 * even # assignment, binary_operator-Add, binary_operator-Mult, binary_operator-Pow, binary_operator-Sub, literal-Num, suggest_constant_definition
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_29/solution.py
# ----------------------------------------------------------------------------------------
def solution(n): # function_definition
    collectPowers = set() # assignment, builtin_function_call-set
    currentPow = 0 # assignment, literal-Num
    N = n + 1  # maximum limit # assignment, binary_operator-Add, literal-Num
    for a in range(2, N): # builtin_function_call-range, for_range_start, literal-Num, nested_for
        for b in range(2, N): # builtin_function_call-range, for_range_start, literal-Num
            currentPow = a ** b  # calculates the current power # assignment, binary_operator-Pow
            collectPowers.add(currentPow)  # adds the result to the set # set_method_call-add
    return len(collectPowers) # builtin_function_call-len

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_31/sol1.py
# ----------------------------------------------------------------------------------------
def one_pence(): # function_definition
    return 1 # literal-Num
def two_pence(x): # function_definition, recursive_function_definition (-> +1)
    return 0 if x < 0 else two_pence(x - 2) + one_pence() # binary_operator-Add, binary_operator-Sub, comparison_operator-Lt, literal-Num
def five_pence(x): # function_definition, recursive_function_definition (-> +1)
    return 0 if x < 0 else five_pence(x - 5) + two_pence(x) # binary_operator-Add, binary_operator-Sub, comparison_operator-Lt, literal-Num, suggest_constant_definition
def ten_pence(x): # function_definition, recursive_function_definition (-> +1)
    return 0 if x < 0 else ten_pence(x - 10) + five_pence(x) # binary_operator-Add, binary_operator-Sub, comparison_operator-Lt, literal-Num, suggest_constant_definition
def twenty_pence(x): # function_definition, recursive_function_definition (-> +1)
    return 0 if x < 0 else twenty_pence(x - 20) + ten_pence(x) # binary_operator-Add, binary_operator-Sub, comparison_operator-Lt, literal-Num, suggest_constant_definition
def fifty_pence(x): # function_definition, recursive_function_definition (-> +1)
    return 0 if x < 0 else fifty_pence(x - 50) + twenty_pence(x) # binary_operator-Add, binary_operator-Sub, comparison_operator-Lt, literal-Num, suggest_constant_definition
def one_pound(x): # function_definition, recursive_function_definition (-> +1)
    return 0 if x < 0 else one_pound(x - 100) + fifty_pence(x) # binary_operator-Add, binary_operator-Sub, comparison_operator-Lt, literal-Num, suggest_constant_definition
def two_pound(x): # function_definition, recursive_function_definition (-> +1)
    return 0 if x < 0 else two_pound(x - 200) + one_pound(x) # binary_operator-Add, binary_operator-Sub, comparison_operator-Lt, literal-Num, suggest_constant_definition
def solution(n): # function_definition
    return two_pound(n)

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_32/sol32.py
# ----------------------------------------------------------------------------------------
import itertools
def isCombinationValid(combination): # function_definition
    return ( # boolean_operator-Or
        int("".join(combination[0:2])) * int("".join(combination[2:5])) # binary_operator-Mult, builtin_function_call-int, composition, literal-Num, literal-Str, slice, string_method_call-join, suggest_constant_definition
        == int("".join(combination[5:9])) # builtin_function_call-int, comparison_operator-Eq, composition, literal-Num, literal-Str, slice, string_method_call-join, suggest_constant_definition
    ) or (
        int("".join(combination[0])) * int("".join(combination[1:5])) # binary_operator-Mult, builtin_function_call-int, composition, index, literal-Num, literal-Str, slice, string_method_call-join, suggest_constant_definition
        == int("".join(combination[5:9])) # builtin_function_call-int, comparison_operator-Eq, composition, literal-Num, literal-Str, slice, string_method_call-join, suggest_constant_definition
    )
def solution(): # function_definition
    return sum( # builtin_function_call-sum, composition
        set( # builtin_function_call-set, composition
            [
                int("".join(pandigital[5:9])) # builtin_function_call-int, composition, literal-Num, literal-Str, slice, string_method_call-join, suggest_constant_definition
                for pandigital in itertools.permutations("123456789") # literal-Str
                if isCombinationValid(pandigital)
            ]
        )
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_33/sol1.py
# ----------------------------------------------------------------------------------------
def isDigitCancelling(num, den): # function_definition
    if num != den: # comparison_operator-NotEq, if
        if num % 10 == den // 10: # binary_operator-FloorDiv, binary_operator-Mod, comparison_operator-Eq, divisibility_test-10, if, literal-Num, suggest_constant_definition
            if (num // 10) / (den % 10) == num / den: # binary_operator-Div, binary_operator-FloorDiv, binary_operator-Mod, comparison_operator-Eq, if, literal-Num, suggest_constant_definition
                return True # literal-True
def solve(digit_len: int) -> str: # function_definition
    solutions = [] # assignment, literal-List
    den = 11 # assignment, literal-Num, suggest_constant_definition
    last_digit = int("1" + "0" * digit_len) # assignment, binary_operator-Add, binary_operator-Mult, builtin_function_call-int, literal-Str
    for num in range(den, last_digit): # builtin_function_call-range, for_range_start
        while den <= 99: # comparison_operator-LtE, evolve_state (-> +4), literal-Num, suggest_constant_definition
            if (num != den) and (num % 10 == den // 10) and (den % 10 != 0): # binary_operator-FloorDiv, binary_operator-Mod, boolean_operator-And, comparison_operator-Eq, comparison_operator-NotEq, divisibility_test-10, if, literal-Num, suggest_constant_definition
                if isDigitCancelling(num, den): # if
                    solutions.append("{}/{}".format(num, den)) # composition, literal-Str, mutable_sequence_method_call-append
            den += 1 # augmented_assignment, literal-Num
        num += 1 # augmented_assignment, literal-Num
        den = 10 # assignment, literal-Num, suggest_constant_definition
    solutions = " , ".join(solutions) # assignment, literal-Str, string_method_call-join
    return solutions

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_36/sol1.py
# ----------------------------------------------------------------------------------------
def is_palindrome(n): # function_definition
    n = str(n) # assignment, builtin_function_call-str
    if n == n[::-1]: # comparison_operator-Eq, if, if_else, literal-Num, slice_step, suggest_condition_return (-> +3), unary_operator-USub
        return True # literal-True
    else:
        return False # literal-False
def solution(n): # function_definition
    total = 0 # assignment, literal-Num
    for i in range(1, n): # accumulate_elements-AugAssign (-> +2), builtin_function_call-range, for_range_start, literal-Num
        if is_palindrome(i) and is_palindrome(bin(i).split("b")[1]): # boolean_operator-And, builtin_function_call-bin, composition, if, index, literal-Num, literal-Str
            total += i # augmented_assignment
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_40/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function_definition
    constant = [] # assignment, literal-List
    i = 1 # assignment, literal-Num
    while len(constant) < 1e6: # builtin_function_call-len, comparison_operator-Lt, evolve_state (-> +1), literal-Num, suggest_constant_definition
        constant.append(str(i)) # builtin_function_call-str, composition, mutable_sequence_method_call-append
        i += 1 # augmented_assignment, literal-Num
    constant = "".join(constant) # assignment, literal-Str, string_method_call-join
    return (
        int(constant[0]) # binary_operator-Mult, builtin_function_call-int, index, literal-Num
        * int(constant[9]) # builtin_function_call-int, index, literal-Num, suggest_constant_definition
        * int(constant[99]) # binary_operator-Mult, builtin_function_call-int, index, literal-Num, suggest_constant_definition
        * int(constant[999]) # binary_operator-Mult, builtin_function_call-int, index, literal-Num, suggest_constant_definition
        * int(constant[9999]) # binary_operator-Mult, builtin_function_call-int, index, literal-Num, suggest_constant_definition
        * int(constant[99999]) # binary_operator-Mult, builtin_function_call-int, index, literal-Num, suggest_constant_definition
        * int(constant[999999]) # binary_operator-Mult, builtin_function_call-int, index, literal-Num, suggest_constant_definition
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_42/solution42.py
# ----------------------------------------------------------------------------------------
import os
TRIANGULAR_NUMBERS = [int(0.5 * n * (n + 1)) for n in range(1, 101)] # assignment, binary_operator-Add, binary_operator-Mult, builtin_function_call-int, builtin_function_call-range, global_constant_definition, literal-Num
def solution(): # function_definition
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, composition
    wordsFilePath = os.path.join(script_dir, "words.txt") # assignment, literal-Str, string_method_call-join
    words = "" # assignment, literal-Str
    with open(wordsFilePath, "r") as f: # builtin_function_call-open, literal-Str
        words = f.readline() # assignment
    words = list(map(lambda word: word.strip('"'), words.strip("\r\n").split(","))) # assignment, builtin_function_call-list, builtin_function_call-map, composition, literal-Str, method_chaining, string_method_call-strip
    words = list( # assignment, builtin_function_call-list, composition
        filter( # builtin_function_call-filter, composition
            lambda word: word in TRIANGULAR_NUMBERS, # comparison_operator-In
            map(lambda word: sum(map(lambda x: ord(x) - 64, word)), words), # binary_operator-Sub, builtin_function_call-map, builtin_function_call-ord, builtin_function_call-sum, composition, literal-Num, suggest_constant_definition
        )
    )
    return len(words) # builtin_function_call-len

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_48/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function_definition
    total = 0 # assignment, literal-Num
    for i in range(1, 1001): # accumulate_elements-AugAssign (-> +1), builtin_function_call-range, for_range_start, literal-Num, suggest_constant_definition
        total += i ** i # augmented_assignment, binary_operator-Pow
    return str(total)[-10:] # builtin_function_call-str, literal-Num, slice, suggest_constant_definition, unary_operator-USub

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_52/sol1.py
# ----------------------------------------------------------------------------------------
def solution(): # function_definition
    i = 1 # assignment, literal-Num
    while True: # literal-True
        if ( # if
            sorted(list(str(i))) # builtin_function_call-list, builtin_function_call-sorted, builtin_function_call-str, composition
            == sorted(list(str(2 * i))) # binary_operator-Mult, builtin_function_call-list, builtin_function_call-sorted, builtin_function_call-str, comparison_operator-Eq, composition, literal-Num
            == sorted(list(str(3 * i))) # binary_operator-Mult, builtin_function_call-list, builtin_function_call-sorted, builtin_function_call-str, composition, literal-Num, suggest_constant_definition
            == sorted(list(str(4 * i))) # binary_operator-Mult, builtin_function_call-list, builtin_function_call-sorted, builtin_function_call-str, composition, literal-Num, suggest_constant_definition
            == sorted(list(str(5 * i))) # binary_operator-Mult, builtin_function_call-list, builtin_function_call-sorted, builtin_function_call-str, composition, literal-Num, suggest_constant_definition
            == sorted(list(str(6 * i))) # binary_operator-Mult, builtin_function_call-list, builtin_function_call-sorted, builtin_function_call-str, composition, literal-Num, suggest_constant_definition
        ):
            return i
        i += 1 # augmented_assignment, literal-Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_53/sol1.py
# ----------------------------------------------------------------------------------------
from math import factorial
def combinations(n, r): # function_definition
    return factorial(n) / (factorial(r) * factorial(n - r)) # binary_operator-Div, binary_operator-Mult, binary_operator-Sub
def solution(): # function_definition
    total = 0 # assignment, literal-Num
    for i in range(1, 101): # builtin_function_call-range, for_range_start, literal-Num, nested_for, suggest_constant_definition
        for j in range(1, i + 1): # binary_operator-Add, builtin_function_call-range, for_range_start, literal-Num
            if combinations(i, j) > 1e6: # comparison_operator-Gt, if, literal-Num, suggest_constant_definition
                total += 1 # augmented_assignment, literal-Num
    return total

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_551/sol1.py
# ----------------------------------------------------------------------------------------
ks = [k for k in range(2, 20 + 1)] # assignment, binary_operator-Add, builtin_function_call-range, global_variable_definition, literal-Num
base = [10 ** k for k in range(ks[-1] + 1)] # assignment, binary_operator-Add, binary_operator-Pow, builtin_function_call-range, global_variable_definition, index, literal-Num, unary_operator-USub
memo = {} # assignment, global_variable_definition, literal-Dict
def next_term(a_i, k, i, n): # function_definition, recursive_function_definition (-> +34)
    ds_b = 0 # assignment, literal-Num
    for j in range(k, len(a_i)): # accumulate_elements-AugAssign (-> +1), builtin_function_call-len, builtin_function_call-range, composition, for_range_start
        ds_b += a_i[j] # augmented_assignment, index
    c = 0 # assignment, literal-Num
    for j in range(min(len(a_i), k)): # accumulate_elements-AugAssign (-> +1), builtin_function_call-len, builtin_function_call-min, builtin_function_call-range, composition, for_range_stop
        c += a_i[j] * base[j] # augmented_assignment, binary_operator-Mult, index
    diff, dn = 0, 0 # assignment, literal-Num, literal-Tuple
    max_dn = n - i # assignment, binary_operator-Sub
    sub_memo = memo.get(ds_b) # assignment, dict_method_call-get
    if sub_memo != None: # comparison_operator-NotEq, if, if_else, literal-None
        jumps = sub_memo.get(c) # assignment, dict_method_call-get
        if jumps != None and len(jumps) > 0: # boolean_operator-And, builtin_function_call-len, comparison_operator-Gt, comparison_operator-NotEq, if, if_else, literal-None, literal-Num
            max_jump = -1 # assignment, literal-Num, unary_operator-USub
            for _k in range(len(jumps) - 1, -1, -1): # binary_operator-Sub, builtin_function_call-len, builtin_function_call-range, composition, for_range_backwards, for_range_step, literal-Num, unary_operator-USub
                if jumps[_k][2] <= k and jumps[_k][1] <= max_dn: # boolean_operator-And, comparison_operator-LtE, if, index, literal-Num
                    max_jump = _k # assignment
                    break
            if max_jump >= 0: # comparison_operator-GtE, if, literal-Num
                diff, dn, _kk = jumps[max_jump] # assignment, index
                new_c = diff + c # assignment, binary_operator-Add
                for j in range(min(k, len(a_i))): # builtin_function_call-len, builtin_function_call-min, builtin_function_call-range, composition, for_range_stop
                    new_c, a_i[j] = divmod(new_c, 10) # assignment, builtin_function_call-divmod, index, literal-Num, suggest_constant_definition
                if new_c > 0: # comparison_operator-Gt, if, literal-Num
                    add(a_i, k, new_c)
        else:
            sub_memo[c] = [] # assignment, index, literal-List
    else:
        sub_memo = {c: []} # assignment, literal-List
        memo[ds_b] = sub_memo # assignment, index
    if dn >= max_dn or c + diff >= base[k]: # binary_operator-Add, boolean_operator-Or, comparison_operator-GtE, if, index
        return diff, dn
    if k > ks[0]: # comparison_operator-Gt, if, if_else, index, literal-Num
        while True: # literal-True
            _diff, terms_jumped = next_term(a_i, k - 1, i + dn, n) # assignment, binary_operator-Add, binary_operator-Sub, literal-Num
            diff += _diff # augmented_assignment
            dn += terms_jumped # augmented_assignment
            if dn >= max_dn or c + diff >= base[k]: # binary_operator-Add, boolean_operator-Or, comparison_operator-GtE, if, index
                break
    else:
        _diff, terms_jumped = compute(a_i, k, i + dn, n) # assignment, binary_operator-Add
        diff += _diff # augmented_assignment
        dn += terms_jumped # augmented_assignment
    jumps = sub_memo[c] # assignment, index
    j = 0 # assignment, literal-Num
    while j < len(jumps): # builtin_function_call-len, comparison_operator-Lt
        if jumps[j][1] > dn: # comparison_operator-Gt, if, index, literal-Num
            break
        j += 1 # augmented_assignment, literal-Num
    sub_memo[c].insert(j, (diff, dn, k)) # index, mutable_sequence_method_call-insert
    return (diff, dn)
def compute(a_i, k, i, n): # function_definition
    if i >= n: # comparison_operator-GtE, if
        return 0, i # literal-Num
    if k > len(a_i): # builtin_function_call-len, comparison_operator-Gt, if
        a_i.extend([0 for _ in range(k - len(a_i))]) # binary_operator-Sub, builtin_function_call-len, builtin_function_call-range, composition, literal-Num, mutable_sequence_method_call-extend
    start_i = i # assignment
    ds_b, ds_c, diff = 0, 0, 0 # assignment, literal-Num, literal-Tuple
    for j in range(len(a_i)): # accumulate_elements-AugAssign (-> +2), builtin_function_call-len, builtin_function_call-range, composition, for_indexes, for_range_stop
        if j >= k: # comparison_operator-GtE, if, if_else
            ds_b += a_i[j] # augmented_assignment, index
        else:
            ds_c += a_i[j] # augmented_assignment, index
    while i < n: # comparison_operator-Lt
        i += 1 # augmented_assignment, literal-Num
        addend = ds_c + ds_b # assignment, binary_operator-Add
        diff += addend # augmented_assignment
        ds_c = 0 # assignment, literal-Num
        for j in range(k): # accumulate_elements-AugAssign (-> +3), builtin_function_call-range, for_range_stop
            s = a_i[j] + addend # assignment, binary_operator-Add, index
            addend, a_i[j] = divmod(s, 10) # assignment, builtin_function_call-divmod, index, literal-Num, suggest_constant_definition
            ds_c += a_i[j] # augmented_assignment, index
        if addend > 0: # comparison_operator-Gt, if, literal-Num
            break
    if addend > 0: # comparison_operator-Gt, if, literal-Num
        add(a_i, k, addend)
    return diff, i - start_i # binary_operator-Sub
def add(digits, k, addend): # function_definition
    for j in range(k, len(digits)): # builtin_function_call-len, builtin_function_call-range, composition, for_range_start
        s = digits[j] + addend # assignment, binary_operator-Add, index
        if s >= 10: # comparison_operator-GtE, if, if_else, literal-Num, suggest_constant_definition
            quotient, digits[j] = divmod(s, 10) # assignment, builtin_function_call-divmod, index, literal-Num, suggest_constant_definition
            addend = addend // 10 + quotient # assignment, binary_operator-Add, binary_operator-FloorDiv, literal-Num, suggest_constant_definition
        else:
            digits[j] = s # assignment, index
            addend = addend // 10 # assignment, binary_operator-FloorDiv, literal-Num, suggest_augmented_assignment, suggest_constant_definition
        if addend == 0: # comparison_operator-Eq, if, literal-Num
            break
    while addend > 0: # comparison_operator-Gt, literal-Num
        addend, digit = divmod(addend, 10) # assignment, builtin_function_call-divmod, literal-Num, suggest_constant_definition
        digits.append(digit) # mutable_sequence_method_call-append
def solution(n): # function_definition
    digits = [1] # assignment, literal-List, literal-Num
    i = 1 # assignment, literal-Num
    dn = 0 # assignment, literal-Num
    while True: # literal-True
        diff, terms_jumped = next_term(digits, 20, i + dn, n) # assignment, binary_operator-Add, literal-Num, suggest_constant_definition
        dn += terms_jumped # augmented_assignment
        if dn == n - i: # binary_operator-Sub, comparison_operator-Eq, if
            break
    a_n = 0 # assignment, literal-Num
    for j in range(len(digits)): # accumulate_elements-AugAssign (-> +1), builtin_function_call-len, builtin_function_call-range, composition, for_indexes, for_range_stop
        a_n += digits[j] * 10 ** j # augmented_assignment, binary_operator-Mult, binary_operator-Pow, index, literal-Num, suggest_constant_definition
    return a_n

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_56/sol1.py
# ----------------------------------------------------------------------------------------
def maximum_digital_sum(a: int, b: int) -> int: # function_definition
    return max( # builtin_function_call-max, composition
        [
            sum([int(x) for x in str(base ** power)]) # binary_operator-Pow, builtin_function_call-int, builtin_function_call-str, builtin_function_call-sum, composition
            for base in range(a) # builtin_function_call-range
            for power in range(b) # builtin_function_call-range
        ]
    )

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_67/sol1.py
# ----------------------------------------------------------------------------------------
import os
def solution(): # function_definition
    script_dir = os.path.dirname(os.path.realpath(__file__)) # assignment, composition
    triangle = os.path.join(script_dir, "triangle.txt") # assignment, literal-Str, string_method_call-join
    with open(triangle, "r") as f: # builtin_function_call-open, literal-Str
        triangle = f.readlines() # assignment
    a = map(lambda x: x.rstrip("\r\n").split(" "), triangle) # assignment, builtin_function_call-map, composition, literal-Str, method_chaining, string_method_call-rstrip
    a = list(map(lambda x: list(map(lambda y: int(y), x)), a)) # assignment, builtin_function_call-int, builtin_function_call-list, builtin_function_call-map, composition
    for i in range(1, len(a)): # builtin_function_call-len, builtin_function_call-range, composition, for_range_start, literal-Num, nested_for
        for j in range(len(a[i])): # builtin_function_call-len, builtin_function_call-range, composition, for_indexes, for_range_stop, index
            if j != len(a[i - 1]): # binary_operator-Sub, builtin_function_call-len, comparison_operator-NotEq, if, if_else, index, literal-Num, suggest_conditional_expression (-> +3)
                number1 = a[i - 1][j] # assignment, binary_operator-Sub, index, literal-Num
            else:
                number1 = 0 # assignment, literal-Num
            if j > 0: # comparison_operator-Gt, if, if_else, literal-Num, suggest_conditional_expression (-> +3)
                number2 = a[i - 1][j - 1] # assignment, binary_operator-Sub, index, literal-Num
            else:
                number2 = 0 # assignment, literal-Num
            a[i][j] += max(number1, number2) # augmented_assignment, builtin_function_call-max, index
    return max(a[-1]) # builtin_function_call-max, index, literal-Num, unary_operator-USub

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_76/sol1.py
# ----------------------------------------------------------------------------------------
def partition(m): # function_definition
    memo = [[0 for _ in range(m)] for _ in range(m + 1)] # assignment, binary_operator-Add, builtin_function_call-range, literal-Num
    for i in range(m + 1): # binary_operator-Add, builtin_function_call-range, for_range_stop, literal-Num
        memo[i][0] = 1 # assignment, index, literal-Num
    for n in range(m + 1): # accumulate_elements-AugAssign (-> +4), binary_operator-Add, builtin_function_call-range, for_range_stop, literal-Num, nested_for
        for k in range(1, m): # accumulate_elements-AugAssign (-> +3), builtin_function_call-range, for_range_start, literal-Num
            memo[n][k] += memo[n][k - 1] # augmented_assignment, binary_operator-Sub, index, literal-Num
            if n > k: # comparison_operator-Gt, if
                memo[n][k] += memo[n - k - 1][k] # augmented_assignment, binary_operator-Sub, index, literal-Num
    return memo[m][m - 1] - 1 # binary_operator-Sub, index, literal-Num

# ----------------------------------------------------------------------------------------
# ../Python/project_euler/problem_99/sol1.py
# ----------------------------------------------------------------------------------------
import os
from math import log10
def find_largest(data_file: str = "base_exp.txt") -> int: # function_definition, literal-Str
    largest = [0, 0] # assignment, literal-List, literal-Num
    for i, line in enumerate(open(os.path.join(os.path.dirname(__file__), data_file))): # builtin_function_call-enumerate, builtin_function_call-open, composition, for_indexes_values, string_method_call-join
        a, x = list(map(int, line.split(","))) # assignment, builtin_function_call-list, builtin_function_call-map, composition, literal-Str
        if x * log10(a) > largest[0]: # binary_operator-Mult, comparison_operator-Gt, if, index, literal-Num
            largest = [x * log10(a), i + 1] # assignment, binary_operator-Add, binary_operator-Mult, literal-Num
    return largest[1] # index, literal-Num
