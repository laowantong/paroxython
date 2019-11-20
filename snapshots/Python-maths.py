# ----------------------------------------------------------------------------------------
# ../Python/maths/3n+1.py
# ----------------------------------------------------------------------------------------
from typing import Tuple, List
def n31(a: int) -> Tuple[List[int], int]: # function_definition, index
    if not isinstance(a, int): # function_call=isinstance, if, unary_operator=Not
        raise TypeError("Must be int, not {0}".format(type(a).__name__)) # composition, function_call=TypeError, function_call=type, literal=Str, method_call=format
    if a < 1: # comparison_operator=Lt, if, literal=Num
        raise ValueError("Given integer must be greater than 1, not {0}".format(a)) # composition, function_call=ValueError, literal=Str, method_call=format
    path = [a] # assignment
    while a != 1: # comparison_operator=NotEq, evolve_state (-> +4), literal=Num
        if a % 2 == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, if, if_else, literal=Num, suggest_conditional_expression (-> +3)
            a = a // 2 # assignment, binary_operator=FloorDiv, literal=Num, suggest_augmented_assignment
        else:
            a = 3 * a + 1 # assignment, binary_operator=Add, binary_operator=Mult, literal=Num, suggest_constant_definition
        path += [a] # augmented_assignment
    return path, len(path) # function_call=len
def test_n31(): # function_definition
    assert n31(4) == ([4, 2, 1], 3) # comparison_operator=Eq, function_call=n31, literal=List, literal=Num, literal=Tuple, suggest_constant_definition
    assert n31(11) == ([11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 15) # comparison_operator=Eq, function_call=n31, literal=List, literal=Num, literal=Tuple, suggest_constant_definition
    assert n31(31) == ( # function_call=n31, literal=Num, suggest_constant_definition
        [ # comparison_operator=Eq, literal=List, literal=Tuple
            31, # literal=Num, suggest_constant_definition
            94, # literal=Num, suggest_constant_definition
            47, # literal=Num, suggest_constant_definition
            142, # literal=Num, suggest_constant_definition
            71, # literal=Num, suggest_constant_definition
            214, # literal=Num, suggest_constant_definition
            107, # literal=Num, suggest_constant_definition
            322, # literal=Num, suggest_constant_definition
            161, # literal=Num, suggest_constant_definition
            484, # literal=Num, suggest_constant_definition
            242, # literal=Num, suggest_constant_definition
            121, # literal=Num, suggest_constant_definition
            364, # literal=Num, suggest_constant_definition
            182, # literal=Num, suggest_constant_definition
            91, # literal=Num, suggest_constant_definition
            274, # literal=Num, suggest_constant_definition
            137, # literal=Num, suggest_constant_definition
            412, # literal=Num, suggest_constant_definition
            206, # literal=Num, suggest_constant_definition
            103, # literal=Num, suggest_constant_definition
            310, # literal=Num, suggest_constant_definition
            155, # literal=Num, suggest_constant_definition
            466, # literal=Num, suggest_constant_definition
            233, # literal=Num, suggest_constant_definition
            700, # literal=Num, suggest_constant_definition
            350, # literal=Num, suggest_constant_definition
            175, # literal=Num, suggest_constant_definition
            526, # literal=Num, suggest_constant_definition
            263, # literal=Num, suggest_constant_definition
            790, # literal=Num, suggest_constant_definition
            395, # literal=Num, suggest_constant_definition
            1186, # literal=Num, suggest_constant_definition
            593, # literal=Num, suggest_constant_definition
            1780, # literal=Num, suggest_constant_definition
            890, # literal=Num, suggest_constant_definition
            445, # literal=Num, suggest_constant_definition
            1336, # literal=Num, suggest_constant_definition
            668, # literal=Num, suggest_constant_definition
            334, # literal=Num, suggest_constant_definition
            167, # literal=Num, suggest_constant_definition
            502, # literal=Num, suggest_constant_definition
            251, # literal=Num, suggest_constant_definition
            754, # literal=Num, suggest_constant_definition
            377, # literal=Num, suggest_constant_definition
            1132, # literal=Num, suggest_constant_definition
            566, # literal=Num, suggest_constant_definition
            283, # literal=Num, suggest_constant_definition
            850, # literal=Num, suggest_constant_definition
            425, # literal=Num, suggest_constant_definition
            1276, # literal=Num, suggest_constant_definition
            638, # literal=Num, suggest_constant_definition
            319, # literal=Num, suggest_constant_definition
            958, # literal=Num, suggest_constant_definition
            479, # literal=Num, suggest_constant_definition
            1438, # literal=Num, suggest_constant_definition
            719, # literal=Num, suggest_constant_definition
            2158, # literal=Num, suggest_constant_definition
            1079, # literal=Num, suggest_constant_definition
            3238, # literal=Num, suggest_constant_definition
            1619, # literal=Num, suggest_constant_definition
            4858, # literal=Num, suggest_constant_definition
            2429, # literal=Num, suggest_constant_definition
            7288, # literal=Num, suggest_constant_definition
            3644, # literal=Num, suggest_constant_definition
            1822, # literal=Num, suggest_constant_definition
            911, # literal=Num, suggest_constant_definition
            2734, # literal=Num, suggest_constant_definition
            1367, # literal=Num, suggest_constant_definition
            4102, # literal=Num, suggest_constant_definition
            2051, # literal=Num, suggest_constant_definition
            6154, # literal=Num, suggest_constant_definition
            3077, # literal=Num, suggest_constant_definition
            9232, # literal=Num, suggest_constant_definition
            4616, # literal=Num, suggest_constant_definition
            2308, # literal=Num, suggest_constant_definition
            1154, # literal=Num, suggest_constant_definition
            577, # literal=Num, suggest_constant_definition
            1732, # literal=Num, suggest_constant_definition
            866, # literal=Num, suggest_constant_definition
            433, # literal=Num, suggest_constant_definition
            1300, # literal=Num, suggest_constant_definition
            650, # literal=Num, suggest_constant_definition
            325, # literal=Num, suggest_constant_definition
            976, # literal=Num, suggest_constant_definition
            488, # literal=Num, suggest_constant_definition
            244, # literal=Num, suggest_constant_definition
            122, # literal=Num, suggest_constant_definition
            61, # literal=Num, suggest_constant_definition
            184, # literal=Num, suggest_constant_definition
            92, # literal=Num, suggest_constant_definition
            46, # literal=Num, suggest_constant_definition
            23, # literal=Num, suggest_constant_definition
            70, # literal=Num, suggest_constant_definition
            35, # literal=Num, suggest_constant_definition
            106, # literal=Num, suggest_constant_definition
            53, # literal=Num, suggest_constant_definition
            160, # literal=Num, suggest_constant_definition
            80, # literal=Num, suggest_constant_definition
            40, # literal=Num, suggest_constant_definition
            20, # literal=Num, suggest_constant_definition
            10, # literal=Num, suggest_constant_definition
            5, # literal=Num, suggest_constant_definition
            16, # literal=Num, suggest_constant_definition
            8, # literal=Num, suggest_constant_definition
            4, # literal=Num, suggest_constant_definition
            2, # literal=Num
            1, # literal=Num
        ],
        107, # literal=Num, suggest_constant_definition
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs.py
# ----------------------------------------------------------------------------------------
def abs_val(num): # function_definition
    return -num if num < 0 else num # comparison_operator=Lt, literal=Num, unary_operator=USub
def test_abs_val(): # function_definition
    assert 0 == abs_val(0) # comparison_operator=Eq, function_call=abs_val, literal=Num
    assert 34 == abs_val(34) # comparison_operator=Eq, function_call=abs_val, literal=Num, suggest_constant_definition
    assert 100000000000 == abs_val(-100000000000) # comparison_operator=Eq, function_call=abs_val, literal=Num, suggest_constant_definition, unary_operator=USub

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs_max.py
# ----------------------------------------------------------------------------------------
from typing import List
def abs_max(x: List[int]) -> int: # function_definition, index
    j = x[0] # assignment, index, literal=Num
    for i in x: # find_best_element (-> +2), for_each
        if abs(i) > abs(j): # comparison_operator=Gt, function_call=abs, if
            j = i # assignment
    return j
def abs_max_sort(x): # function_definition
    return sorted(x, key=abs)[-1] # function_call=sorted, index, literal=Num, unary_operator=USub
def main(): # function_definition
    a = [1, 2, -11] # assignment, literal=List, literal=Num, suggest_constant_definition, unary_operator=USub
    assert abs_max(a) == -11 # comparison_operator=Eq, function_call=abs_max, literal=Num, suggest_constant_definition, unary_operator=USub
    assert abs_max_sort(a) == -11 # comparison_operator=Eq, function_call=abs_max_sort, literal=Num, suggest_constant_definition, unary_operator=USub

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs_min.py
# ----------------------------------------------------------------------------------------
from .abs import abs_val
def absMin(x): # function_definition
    j = x[0] # assignment, index, literal=Num
    for i in x: # find_best_element (-> +2), for_each
        if abs_val(i) < abs_val(j): # comparison_operator=Lt, function_call=abs_val, if
            j = i # assignment
    return j
def main(): # function_definition
    a = [-3, -1, 2, -11] # assignment, literal=List, literal=Num, suggest_constant_definition, unary_operator=USub
    print(absMin(a))  # = -1 # composition, function_call=absMin, function_call=print

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_mean.py
# ----------------------------------------------------------------------------------------
def average(nums): # function_definition
    return sum(nums) / len(nums) # binary_operator=Div, function_call=len, function_call=sum
def test_average(): # function_definition
    assert 12.0 == average([3, 6, 9, 12, 15, 18, 21]) # comparison_operator=Eq, function_call=average, literal=List, literal=Num, suggest_constant_definition
    assert 20 == average([5, 10, 15, 20, 25, 30, 35]) # comparison_operator=Eq, function_call=average, literal=List, literal=Num, suggest_constant_definition
    assert 4.5 == average([1, 2, 3, 4, 5, 6, 7, 8]) # comparison_operator=Eq, function_call=average, literal=List, literal=Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_median.py
# ----------------------------------------------------------------------------------------
def median(nums): # function_definition
    sorted_list = sorted(nums) # assignment, function_call=sorted
    med = None # assignment, literal=None
    if len(sorted_list) % 2 == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, function_call=len, if, if_else, literal=Num
        mid_index_1 = len(sorted_list) // 2 # assignment, binary_operator=FloorDiv, function_call=len, literal=Num
        mid_index_2 = (len(sorted_list) // 2) - 1 # assignment, binary_operator=FloorDiv, binary_operator=Sub, function_call=len, literal=Num
        med = (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / float(2) # assignment, binary_operator=Add, binary_operator=Div, function_call=float, index, literal=Num
    else:
        mid_index = (len(sorted_list) - 1) // 2 # assignment, binary_operator=FloorDiv, binary_operator=Sub, function_call=len, literal=Num
        med = sorted_list[mid_index] # assignment, index
    return med
def main(): # function_definition
    print("Odd number of numbers:") # function_call=print, literal=Str
    print(median([2, 4, 6, 8, 20, 50, 70])) # composition, function_call=median, function_call=print, literal=List, literal=Num, suggest_constant_definition
    print("Even number of numbers:") # function_call=print, literal=Str
    print(median([2, 4, 6, 8, 20, 50])) # composition, function_call=median, function_call=print, literal=List, literal=Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_mode.py
# ----------------------------------------------------------------------------------------
import statistics
def mode(input_list):  # Defining function "mode." # function_definition
    check_list = input_list.copy() # assignment, method_call=copy
    result = list()  # Empty list to store the counts of elements in input_list # assignment, function_call=list
    for x in input_list: # accumulate_elements=Attribute (-> +2), for_each
        result.append(input_list.count(x)) # composition, method_call=append, method_call=count
        input_list.remove(x) # method_call=remove
        y = max(result)  # Gets the maximum value in the result list. # assignment, function_call=max
        return check_list[result.index(y)] # index, method_call=index

# ----------------------------------------------------------------------------------------
# ../Python/maths/basic_maths.py
# ----------------------------------------------------------------------------------------
import math
def prime_factors(n: int) -> list: # function_definition
    pf = [] # assignment, literal=List
    while n % 2 == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, evolve_state (-> +2), literal=Num
        pf.append(2) # literal=Num, method_call=append
        n = int(n / 2) # assignment, binary_operator=Div, function_call=int, literal=Num
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_elements=Assign (-> +3), binary_operator=Add, composition, for_range_step, function_call=int, function_call=range, literal=Num, method_call=sqrt, suggest_constant_definition
        while n % i == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test, evolve_state (-> +1), literal=Num
            pf.append(i) # method_call=append
            n = int(n / i) # assignment, binary_operator=Div, function_call=int
    if n > 2: # comparison_operator=Gt, if, literal=Num
        pf.append(n) # method_call=append
    return pf
def number_of_divisors(n: int) -> int: # function_definition
    div = 1 # assignment, literal=Num
    temp = 1 # assignment, literal=Num
    while n % 2 == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, evolve_state (-> +2), literal=Num
        temp += 1 # augmented_assignment, literal=Num
        n = int(n / 2) # assignment, binary_operator=Div, function_call=int, literal=Num
    div *= temp # augmented_assignment
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_elements=Assign (-> +4), binary_operator=Add, composition, for_range_step, function_call=int, function_call=range, literal=Num, method_call=sqrt, suggest_constant_definition
        temp = 1 # assignment, literal=Num
        while n % i == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test, literal=Num
            temp += 1 # augmented_assignment, literal=Num
            n = int(n / i) # assignment, binary_operator=Div, function_call=int
        div *= temp # augmented_assignment
    return div
def sum_of_divisors(n: int) -> int: # function_definition
    s = 1 # assignment, literal=Num
    temp = 1 # assignment, literal=Num
    while n % 2 == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, evolve_state (-> +2), literal=Num
        temp += 1 # augmented_assignment, literal=Num
        n = int(n / 2) # assignment, binary_operator=Div, function_call=int, literal=Num
    if temp > 1: # comparison_operator=Gt, if, literal=Num
        s *= (2 ** temp - 1) / (2 - 1) # augmented_assignment, binary_operator=Div, binary_operator=Pow, binary_operator=Sub, literal=Num
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_elements=Assign (-> +4), binary_operator=Add, composition, for_range_step, function_call=int, function_call=range, literal=Num, method_call=sqrt, suggest_constant_definition
        temp = 1 # assignment, literal=Num
        while n % i == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test, literal=Num
            temp += 1 # augmented_assignment, literal=Num
            n = int(n / i) # assignment, binary_operator=Div, function_call=int
        if temp > 1: # comparison_operator=Gt, if, literal=Num
            s *= (i ** temp - 1) / (i - 1) # augmented_assignment, binary_operator=Div, binary_operator=Pow, binary_operator=Sub, literal=Num
    return int(s) # function_call=int
def euler_phi(n: int) -> int: # function_definition
    s = n # assignment
    for x in set(prime_factors(n)): # accumulate_elements=AugAssign (-> +1), composition, function_call=prime_factors, function_call=set
        s *= (x - 1) / x # augmented_assignment, binary_operator=Div, binary_operator=Sub, literal=Num
    return int(s) # function_call=int

# ----------------------------------------------------------------------------------------
# ../Python/maths/binary_exponentiation.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n): # function_definition, recursive_function_definition (-> +6)
    if n == 0: # comparison_operator=Eq, if, if_elif, literal=Num
        return 1 # literal=Num
    elif n % 2 == 1: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, if, if_else, literal=Num
        return binary_exponentiation(a, n - 1) * a # binary_operator=Mult, binary_operator=Sub, function_call=binary_exponentiation, literal=Num
    else:
        b = binary_exponentiation(a, n / 2) # assignment, binary_operator=Div, function_call=binary_exponentiation, literal=Num
        return b * b # binary_operator=Mult

# ----------------------------------------------------------------------------------------
# ../Python/maths/binomial_coefficient.py
# ----------------------------------------------------------------------------------------
def binomial_coefficient(n, r): # function_definition
    C = [0 for i in range(r + 1)] # assignment, binary_operator=Add, function_call=range, literal=Num
    C[0] = 1 # assignment, index, literal=Num
    for i in range(1, n + 1): # binary_operator=Add, for_range_start, function_call=range, literal=Num
        j = min(i, r) # assignment, function_call=min
        while j > 0: # comparison_operator=Gt, evolve_state (-> +2), literal=Num
            C[j] += C[j - 1] # augmented_assignment, binary_operator=Sub, index, literal=Num
            j -= 1 # augmented_assignment, literal=Num
    return C[r] # index
print(binomial_coefficient(n=10, r=5)) # composition, function_call=binomial_coefficient, function_call=print, literal=Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/ceil.py
# ----------------------------------------------------------------------------------------
def ceil(x) -> int: # function_definition
    return (
        x if isinstance(x, int) or x - int(x) == 0 else int(x + 1) if x > 0 else int(x) # binary_operator=Add, binary_operator=Sub, boolean_operator=Or, comparison_operator=Eq, comparison_operator=Gt, function_call=int, function_call=isinstance, literal=Num
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/collatz_sequence.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function_definition
    sequence = [n] # assignment
    while n != 1: # comparison_operator=NotEq, evolve_state (-> +4), literal=Num
        if n % 2 == 0:  # even number condition # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, if, if_else, literal=Num
            n //= 2 # augmented_assignment, literal=Num
        else:
            n = 3 * n + 1 # assignment, binary_operator=Add, binary_operator=Mult, literal=Num, suggest_constant_definition
        sequence.append(n) # method_call=append
    return sequence
def main(): # function_definition
    n = 43 # assignment, literal=Num, suggest_constant_definition
    sequence = collatz_sequence(n) # assignment, function_call=collatz_sequence
    print(sequence) # function_call=print
    print("collatz sequence from %d took %d steps." % (n, len(sequence))) # binary_operator=Mod, composition, function_call=len, function_call=print, literal=Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/explicit_euler.py
# ----------------------------------------------------------------------------------------
import numpy as np
def explicit_euler(ode_func, y0, x0, stepsize, x_end): # function_definition
    N = int(np.ceil((x_end - x0) / stepsize)) # assignment, binary_operator=Div, binary_operator=Sub, composition, function_call=int, method_call=ceil
    y = np.zeros((N + 1,)) # assignment, binary_operator=Add, literal=Num, method_call=zeros
    y[0] = y0 # assignment, index, literal=Num
    x = x0 # assignment
    for k in range(N): # accumulate_elements=Assign (-> +1), for_range_stop, function_call=range
        y[k + 1] = y[k] + stepsize * ode_func(x, y[k]) # assignment, binary_operator=Add, binary_operator=Mult, function_call=ode_func, index, literal=Num
        x += stepsize # augmented_assignment
    return y

# ----------------------------------------------------------------------------------------
# ../Python/maths/extended_euclidean_algorithm.py
# ----------------------------------------------------------------------------------------
import sys
def extended_euclidean_algorithm(m, n): # function_definition
    a = 0 # assignment, literal=Num
    a_prime = 1 # assignment, literal=Num
    b = 1 # assignment, literal=Num
    b_prime = 0 # assignment, literal=Num
    q = 0 # assignment, literal=Num
    r = 0 # assignment, literal=Num
    if m > n: # comparison_operator=Gt, if, if_else
        c = m # assignment
        d = n # assignment
    else:
        c = n # assignment
        d = m # assignment
    while True: # literal=True
        q = int(c / d) # assignment, binary_operator=Div, function_call=int
        r = c % d # assignment, binary_operator=Mod
        if r == 0: # comparison_operator=Eq, if, literal=Num
            break
        c = d # assignment
        d = r # assignment
        t = a_prime # assignment
        a_prime = a # assignment
        a = t - q * a # assignment, binary_operator=Mult, binary_operator=Sub
        t = b_prime # assignment
        b_prime = b # assignment
        b = t - q * b # assignment, binary_operator=Mult, binary_operator=Sub
    pair = None # assignment, literal=None
    if m > n: # comparison_operator=Gt, if, if_else, suggest_conditional_expression (-> +3)
        pair = (a, b) # assignment
    else:
        pair = (b, a) # assignment
    return pair
def main(): # function_definition
    if len(sys.argv) < 3: # comparison_operator=Lt, function_call=len, if, literal=Num, suggest_constant_definition
        print("2 integer arguments required") # function_call=print, literal=Str
        exit(1) # function_call=exit, literal=Num
    m = int(sys.argv[1]) # assignment, function_call=int, index, literal=Num
    n = int(sys.argv[2]) # assignment, function_call=int, index, literal=Num
    print(extended_euclidean_algorithm(m, n)) # composition, function_call=extended_euclidean_algorithm, function_call=print

# ----------------------------------------------------------------------------------------
# ../Python/maths/factorial_python.py
# ----------------------------------------------------------------------------------------
def factorial(input_number: int) -> int: # function_definition
    if input_number < 0: # comparison_operator=Lt, if, literal=Num
        raise ValueError("factorial() not defined for negative values") # function_call=ValueError, literal=Str
    if not isinstance(input_number, int): # function_call=isinstance, if, unary_operator=Not
        raise ValueError("factorial() only accepts integral values") # function_call=ValueError, literal=Str
    result = 1 # assignment, literal=Num
    for i in range(1, input_number): # accumulate_elements=Assign (-> +1), for_range_start, function_call=range, literal=Num
        result = result * (i + 1) # assignment, binary_operator=Add, binary_operator=Mult, literal=Num, suggest_augmented_assignment
    return result

# ----------------------------------------------------------------------------------------
# ../Python/maths/factorial_recursive.py
# ----------------------------------------------------------------------------------------
def factorial(n: int) -> int: # function_definition, recursive_function_definition (-> +5)
    if n < 0: # comparison_operator=Lt, if, literal=Num
        raise ValueError("factorial() not defined for negative values") # function_call=ValueError, literal=Str
    if not isinstance(n, int): # function_call=isinstance, if, unary_operator=Not
        raise ValueError("factorial() only accepts integral values") # function_call=ValueError, literal=Str
    return 1 if n == 0 or n == 1 else n * factorial(n - 1) # binary_operator=Mult, binary_operator=Sub, boolean_operator=Or, comparison_operator=Eq, function_call=factorial, literal=Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/factors.py
# ----------------------------------------------------------------------------------------
def factors_of_a_number(num: int) -> list: # function_definition
    return [i for i in range(1, num + 1) if num % i == 0] # binary_operator=Add, binary_operator=Mod, comparison_operator=Eq, divisibility_test, function_call=range, literal=Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/fermat_little_theorem.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n, mod): # function_definition, recursive_function_definition (-> +6)
    if n == 0: # comparison_operator=Eq, if, if_elif, literal=Num
        return 1 # literal=Num
    elif n % 2 == 1: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, if, if_else, literal=Num
        return (binary_exponentiation(a, n - 1, mod) * a) % mod # binary_operator=Mod, binary_operator=Mult, binary_operator=Sub, function_call=binary_exponentiation, literal=Num
    else:
        b = binary_exponentiation(a, n / 2, mod) # assignment, binary_operator=Div, function_call=binary_exponentiation, literal=Num
        return (b * b) % mod # binary_operator=Mod, binary_operator=Mult
p = 701 # assignment, global_variable_definition, literal=Num, suggest_constant_definition
a = 1000000000 # assignment, global_variable_definition, literal=Num, suggest_constant_definition
b = 10 # assignment, global_variable_definition, literal=Num, suggest_constant_definition
print((a / b) % p == (a * binary_exponentiation(b, p - 2, p)) % p) # binary_operator=Div, binary_operator=Mod, binary_operator=Mult, binary_operator=Sub, comparison_operator=Eq, composition, divisibility_test, function_call=binary_exponentiation, function_call=print, literal=Num
print((a / b) % p == (a * b ** (p - 2)) % p) # binary_operator=Div, binary_operator=Mod, binary_operator=Mult, binary_operator=Pow, binary_operator=Sub, comparison_operator=Eq, divisibility_test, function_call=print, literal=Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/fibonacci.py
# ----------------------------------------------------------------------------------------
import math
import functools
import time
from decimal import getcontext, Decimal
getcontext().prec = 100
def timer_decorator(func):
    @functools.wraps(func)
    def timer_wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        if int(end - start) > 0:
            print(f"Run time for {func.__name__}: {(end - start):0.2f}s")
        else:
            print(f"Run time for {func.__name__}: {(end - start)*1000:0.2f}ms")
        return func(*args, **kwargs)
    return timer_wrapper
class Error(Exception):
class ValueTooLargeError(Error):
class ValueTooSmallError(Error):
class ValueLessThanZero(Error):
def _check_number_input(n, min_thresh, max_thresh=None):
    try:
        if n >= min_thresh and max_thresh is None:
            return True
        elif min_thresh <= n <= max_thresh:
            return True
        elif n < 0:
            raise ValueLessThanZero
        elif n < min_thresh:
            raise ValueTooSmallError
        elif n > max_thresh:
            raise ValueTooLargeError
    except ValueLessThanZero:
        print("Incorrect Input: number must not be less than 0")
    except ValueTooSmallError:
        print(
            f"Incorrect Input: input number must be > {min_thresh} for the recursive calculation"
        )
    except ValueTooLargeError:
        print(
            f"Incorrect Input: input number must be < {max_thresh} for the recursive calculation"
        )
    return False
@timer_decorator
def fib_iterative(n):
    n = int(n)
    if _check_number_input(n, 2):
        seq_out = [0, 1]
        a, b = 0, 1
        for _ in range(n - len(seq_out)):
            a, b = b, a + b
            seq_out.append(b)
        return seq_out
@timer_decorator
def fib_formula(n):
    seq_out = [0, 1]
    n = int(n)
    if _check_number_input(n, 2, 1000000):
        sqrt = Decimal(math.sqrt(5))
        phi_1 = Decimal(1 + sqrt) / Decimal(2)
        phi_2 = Decimal(1 - sqrt) / Decimal(2)
        for i in range(2, n):
            temp_out = ((phi_1 ** Decimal(i)) - (phi_2 ** Decimal(i))) * (
                Decimal(sqrt) ** Decimal(-1)
            )
            seq_out.append(int(temp_out))
        return seq_out

# ----------------------------------------------------------------------------------------
# ../Python/maths/fibonacci_sequence_recursion.py
# ----------------------------------------------------------------------------------------
def recur_fibo(n): # function_definition, recursive_function_definition (-> +1)
    return n if n <= 1 else recur_fibo(n - 1) + recur_fibo(n - 2) # binary_operator=Add, binary_operator=Sub, comparison_operator=LtE, function_call=recur_fibo, literal=Num
def main(): # function_definition
    limit = int(input("How many terms to include in fibonacci series: ")) # assignment, composition, function_call=input, function_call=int, literal=Str
    if limit > 0: # comparison_operator=Gt, if, if_else, literal=Num
        print(f"The first {limit} terms of the fibonacci series are as follows:") # function_call=print, literal=Str
        print([recur_fibo(n) for n in range(limit)]) # composition, function_call=print, function_call=range, function_call=recur_fibo
    else:
        print("Please enter a positive integer: ") # function_call=print, literal=Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_max.py
# ----------------------------------------------------------------------------------------
def find_max(nums): # function_definition
    max_num = nums[0] # assignment, index, literal=Num
    for x in nums: # find_best_element (-> +2), for_each
        if x > max_num: # comparison_operator=Gt, if
            max_num = x # assignment
    return max_num
def main(): # function_definition
    print(find_max([2, 4, 9, 7, 19, 94, 5]))  # 94 # composition, function_call=find_max, function_call=print, literal=List, literal=Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_max_recursion.py
# ----------------------------------------------------------------------------------------
def find_max(nums, left, right): # function_definition, recursive_function_definition (-> +5)
    if left == right: # comparison_operator=Eq, if
        return nums[left] # index
    mid = (left + right) >> 1  # the middle # assignment, binary_operator=Add, binary_operator=RShift, literal=Num
    left_max = find_max(nums, left, mid)  # find max in range[left, mid] # assignment, function_call=find_max
    right_max = find_max(nums, mid + 1, right)  # find max in range[mid + 1, right] # assignment, binary_operator=Add, function_call=find_max, literal=Num
    return left_max if left_max >= right_max else right_max # comparison_operator=GtE

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_min.py
# ----------------------------------------------------------------------------------------
def find_min(nums): # function_definition
    min_num = nums[0] # assignment, index, literal=Num
    for num in nums: # find_best_element (-> +2), for_each
        if min_num > num: # comparison_operator=Gt, if
            min_num = num # assignment
    return min_num
def main(): # function_definition
    assert find_min([0, 1, 2, 3, 4, 5, -3, 24, -56]) == -56 # comparison_operator=Eq, function_call=find_min, literal=List, literal=Num, suggest_constant_definition, unary_operator=USub

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_min_recursion.py
# ----------------------------------------------------------------------------------------
def find_min(nums, left, right): # function_definition, recursive_function_definition (-> +5)
    if left == right: # comparison_operator=Eq, if
        return nums[left] # index
    mid = (left + right) >> 1  # the middle # assignment, binary_operator=Add, binary_operator=RShift, literal=Num
    left_min = find_min(nums, left, mid)  # find min in range[left, mid] # assignment, function_call=find_min
    right_min = find_min(nums, mid + 1, right)  # find min in range[mid + 1, right] # assignment, binary_operator=Add, function_call=find_min, literal=Num
    return left_min if left_min <= right_min else right_min # comparison_operator=LtE

# ----------------------------------------------------------------------------------------
# ../Python/maths/floor.py
# ----------------------------------------------------------------------------------------
def floor(x) -> int: # function_definition
    return (
        x if isinstance(x, int) or x - int(x) == 0 else int(x) if x > 0 else int(x - 1) # binary_operator=Sub, boolean_operator=Or, comparison_operator=Eq, comparison_operator=Gt, function_call=int, function_call=isinstance, literal=Num
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/gaussian.py
# ----------------------------------------------------------------------------------------
from numpy import pi, sqrt, exp
def gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> int: # function_definition, literal=Num
    return 1 / sqrt(2 * pi * sigma ** 2) * exp(-((x - mu) ** 2) / 2 * sigma ** 2) # binary_operator=Div, binary_operator=Mult, binary_operator=Pow, binary_operator=Sub, function_call=exp, function_call=sqrt, literal=Num, unary_operator=USub

# ----------------------------------------------------------------------------------------
# ../Python/maths/greatest_common_divisor.py
# ----------------------------------------------------------------------------------------
def greatest_common_divisor(a, b): # function_definition, recursive_function_definition (-> +1)
    return b if a == 0 else greatest_common_divisor(b % a, a) # binary_operator=Mod, comparison_operator=Eq, function_call=greatest_common_divisor, literal=Num
def gcd_by_iterative(x, y): # function_definition
    while y:  # --> when y=0 then loop will terminate and return x as final GCD.
        x, y = y, x % y # assignment, binary_operator=Mod
    return x
def main(): # function_definition
    try:
        nums = input("Enter two integers separated by comma (,): ").split(",") # assignment, function_call=input, literal=Str, method_call=split
        num_1 = int(nums[0]) # assignment, function_call=int, index, literal=Num
        num_2 = int(nums[1]) # assignment, function_call=int, index, literal=Num
        print( # composition, function_call=print
            f"greatest_common_divisor({num_1}, {num_2}) = {greatest_common_divisor(num_1, num_2)}" # function_call=greatest_common_divisor, literal=Str
        )
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}") # composition, function_call=gcd_by_iterative, function_call=print, literal=Str
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong input") # function_call=print, literal=Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/hardy_ramanujanalgo.py
# ----------------------------------------------------------------------------------------
import math
def exactPrimeFactorCount(n): # function_definition
    count = 0 # assignment, literal=Num
    if n % 2 == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, if, literal=Num
        count += 1 # augmented_assignment, literal=Num
        while n % 2 == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, evolve_state (-> +1), literal=Num
            n = int(n / 2) # assignment, binary_operator=Div, function_call=int, literal=Num
    i = 3 # assignment, literal=Num, suggest_constant_definition
    while i <= int(math.sqrt(n)): # comparison_operator=LtE, composition, evolve_state (-> +4), function_call=int, method_call=sqrt
        if n % i == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test, if, literal=Num
            count += 1 # augmented_assignment, literal=Num
            while n % i == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test, literal=Num
                n = int(n / i) # assignment, binary_operator=Div, function_call=int
        i = i + 2 # assignment, binary_operator=Add, literal=Num, suggest_augmented_assignment
    if n > 2: # comparison_operator=Gt, if, literal=Num
        count += 1 # augmented_assignment, literal=Num
    return count

# ----------------------------------------------------------------------------------------
# ../Python/maths/is_square_free.py
# ----------------------------------------------------------------------------------------
from typing import List
def is_square_free(factors: List[int]) -> bool: # function_definition, index
    return len(set(factors)) == len(factors) # comparison_operator=Eq, composition, function_call=len, function_call=set

# ----------------------------------------------------------------------------------------
# ../Python/maths/jaccard_similarity.py
# ----------------------------------------------------------------------------------------
def jaccard_similariy(setA, setB, alternativeUnion=False): # function_definition, literal=False
    if isinstance(setA, set) and isinstance(setB, set): # boolean_operator=And, function_call=isinstance, if
        intersection = len(setA.intersection(setB)) # assignment, composition, function_call=len, method_call=intersection
        if alternativeUnion: # if, if_else, suggest_conditional_expression (-> +3)
            union = len(setA) + len(setB) # assignment, binary_operator=Add, function_call=len
        else:
            union = len(setA.union(setB)) # assignment, composition, function_call=len, method_call=union
        return intersection / union # binary_operator=Div
    if isinstance(setA, (list, tuple)) and isinstance(setB, (list, tuple)): # boolean_operator=And, function_call=isinstance, if
        intersection = [element for element in setA if element in setB] # assignment, comparison_operator=In
        if alternativeUnion: # if, if_else, suggest_conditional_expression (-> +3)
            union = len(setA) + len(setB) # assignment, binary_operator=Add, function_call=len
        else:
            union = setA + [element for element in setB if element not in setA] # assignment, binary_operator=Add, comparison_operator=NotIn
        return len(intersection) / len(union) # binary_operator=Div, function_call=len

# ----------------------------------------------------------------------------------------
# ../Python/maths/karatsuba.py
# ----------------------------------------------------------------------------------------
def karatsuba(a, b): # function_definition, recursive_function_definition (-> +10)
    if len(str(a)) == 1 or len(str(b)) == 1: # boolean_operator=Or, comparison_operator=Eq, composition, function_call=len, function_call=str, if, if_else, literal=Num
        return a * b # binary_operator=Mult
    else:
        m1 = max(len(str(a)), len(str(b))) # assignment, composition, function_call=len, function_call=max, function_call=str
        m2 = m1 // 2 # assignment, binary_operator=FloorDiv, literal=Num
        a1, a2 = divmod(a, 10 ** m2) # assignment, binary_operator=Pow, function_call=divmod, literal=Num, suggest_constant_definition
        b1, b2 = divmod(b, 10 ** m2) # assignment, binary_operator=Pow, function_call=divmod, literal=Num, suggest_constant_definition
        x = karatsuba(a2, b2) # assignment, function_call=karatsuba
        y = karatsuba((a1 + a2), (b1 + b2)) # assignment, binary_operator=Add, function_call=karatsuba
        z = karatsuba(a1, b1) # assignment, function_call=karatsuba
        return (z * 10 ** (2 * m2)) + ((y - z - x) * 10 ** (m2)) + (x) # binary_operator=Add, binary_operator=Mult, binary_operator=Pow, binary_operator=Sub, literal=Num, suggest_constant_definition
def main(): # function_definition
    print(karatsuba(15463, 23489)) # composition, function_call=karatsuba, function_call=print, literal=Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/kth_lexicographic_permutation.py
# ----------------------------------------------------------------------------------------
def kthPermutation(k, n): # function_definition
    factorials = [1] # assignment, literal=List, literal=Num
    for i in range(2, n): # for_range_start, function_call=range, literal=Num
        factorials.append(factorials[-1] * i) # binary_operator=Mult, index, literal=Num, method_call=append, unary_operator=USub
    assert 0 <= k < factorials[-1] * n, "k out of bounds" # binary_operator=Mult, comparison_operator=LtE, index, literal=Num, literal=Str, unary_operator=USub
    permutation = [] # assignment, literal=List
    elements = list(range(n)) # assignment, composition, function_call=list, function_call=range
    while factorials:
        factorial = factorials.pop() # assignment, method_call=pop
        number, k = divmod(k, factorial) # assignment, function_call=divmod
        permutation.append(elements[number]) # index, method_call=append
        elements.remove(elements[number]) # index, method_call=remove
    permutation.append(elements[0]) # index, literal=Num, method_call=append
    return permutation

# ----------------------------------------------------------------------------------------
# ../Python/maths/largest_of_very_large_numbers.py
# ----------------------------------------------------------------------------------------
import math
def res(x, y): # function_definition
    if 0 not in (x, y): # comparison_operator=NotIn, if, if_elif, literal=Num
        return y * math.log10(x) # binary_operator=Mult, method_call=log10
    else:
        if x == 0:  # 0 raised to any number is 0 # comparison_operator=Eq, if, if_elif, literal=Num
            return 0 # literal=Num
        elif y == 0: # comparison_operator=Eq, if, literal=Num
            return 1  # any number raised to 0 is 1 # literal=Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/least_common_multiple.py
# ----------------------------------------------------------------------------------------
import unittest
def find_lcm(first_num: int, second_num: int) -> int: # function_definition
    max_num = first_num if first_num >= second_num else second_num # assignment, comparison_operator=GtE
    common_mult = max_num # assignment
    while (common_mult % first_num > 0) or (common_mult % second_num > 0): # binary_operator=Mod, boolean_operator=Or, comparison_operator=Gt, literal=Num
        common_mult += max_num # augmented_assignment
    return common_mult
class TestLeastCommonMultiple(unittest.TestCase):
    test_inputs = [ # assignment, literal=List
        (10, 20), # literal=Num, literal=Tuple, suggest_constant_definition
        (13, 15), # literal=Num, literal=Tuple, suggest_constant_definition
        (4, 31), # literal=Num, literal=Tuple, suggest_constant_definition
        (10, 42), # literal=Num, literal=Tuple, suggest_constant_definition
        (43, 34), # literal=Num, literal=Tuple, suggest_constant_definition
        (5, 12), # literal=Num, literal=Tuple, suggest_constant_definition
        (12, 25), # literal=Num, literal=Tuple, suggest_constant_definition
        (10, 25), # literal=Num, literal=Tuple, suggest_constant_definition
        (6, 9), # literal=Num, literal=Tuple, suggest_constant_definition
    ]
    expected_results = [20, 195, 124, 210, 1462, 60, 300, 50, 18] # assignment, literal=List, literal=Num, suggest_constant_definition
    def test_lcm_function(self): # function_definition
        for i, (first_num, second_num) in enumerate(self.test_inputs): # for_indexes_values, function_call=enumerate
            actual_result = find_lcm(first_num, second_num) # assignment, function_call=find_lcm
            with self.subTest(i=i): # method_call=subTest
                self.assertEqual(actual_result, self.expected_results[i]) # index, method_call=assertEqual

# ----------------------------------------------------------------------------------------
# ../Python/maths/lucas_series.py
# ----------------------------------------------------------------------------------------
def recur_luc(n): # function_definition, recursive_function_definition (-> +5)
    if n == 1: # comparison_operator=Eq, if, literal=Num
        return n
    if n == 0: # comparison_operator=Eq, if, literal=Num
        return 2 # literal=Num
    return recur_luc(n - 1) + recur_luc(n - 2) # binary_operator=Add, binary_operator=Sub, function_call=recur_luc, literal=Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/matrix_exponentiation.py
# ----------------------------------------------------------------------------------------
import timeit
class Matrix(object):
    def __init__(self, arg): # function_definition
        if isinstance(arg, list):  # Initialzes a matrix identical to the one provided. # function_call=isinstance, if, if_else
            self.t = arg # assignment
            self.n = len(arg) # assignment, function_call=len
        else:  # Initializes a square matrix of the given size and set the values to zero.
            self.n = arg # assignment
            self.t = [[0 for _ in range(self.n)] for _ in range(self.n)] # assignment, function_call=range, literal=Num
    def __mul__(self, b): # function_definition
        matrix = Matrix(self.n) # assignment, function_call=Matrix
        for i in range(self.n): # accumulate_elements=AugAssign (-> +3), for_range_stop, function_call=range, nested_for (-> +1)
            for j in range(self.n): # accumulate_elements=AugAssign (-> +2), for_range_stop, function_call=range, nested_for (-> +1)
                for k in range(self.n): # accumulate_elements=AugAssign (-> +1), for_range_stop, function_call=range
                    matrix.t[i][j] += self.t[i][k] * b.t[k][j] # augmented_assignment, binary_operator=Mult, index
        return matrix
def modular_exponentiation(a, b): # function_definition
    matrix = Matrix([[1, 0], [0, 1]]) # assignment, function_call=Matrix, literal=List, literal=Num
    while b > 0: # comparison_operator=Gt, evolve_state (-> +4), literal=Num
        if b & 1: # binary_operator=BitAnd, if, literal=Num
            matrix *= a # augmented_assignment
        a *= a # augmented_assignment
        b >>= 1 # augmented_assignment, literal=Num
    return matrix
def fibonacci_with_matrix_exponentiation(n, f1, f2): # function_definition
    if n == 1: # comparison_operator=Eq, if, if_elif, literal=Num
        return f1
    elif n == 2: # comparison_operator=Eq, if, literal=Num
        return f2
    matrix = Matrix([[1, 1], [1, 0]]) # assignment, function_call=Matrix, literal=List, literal=Num
    matrix = modular_exponentiation(matrix, n - 2) # assignment, binary_operator=Sub, function_call=modular_exponentiation, literal=Num
    return f2 * matrix.t[0][0] + f1 * matrix.t[0][1] # binary_operator=Add, binary_operator=Mult, index, literal=Num
def simple_fibonacci(n, f1, f2): # function_definition
    if n == 1: # comparison_operator=Eq, if, if_elif, literal=Num
        return f1
    elif n == 2: # comparison_operator=Eq, if, literal=Num
        return f2
    fn_1 = f1 # assignment
    fn_2 = f2 # assignment
    n -= 2 # augmented_assignment, literal=Num
    while n > 0: # comparison_operator=Gt, evolve_state (-> +2), literal=Num
        fn_1, fn_2 = fn_1 + fn_2, fn_1 # assignment, binary_operator=Add
        n -= 1 # augmented_assignment, literal=Num
    return fn_1
def matrix_exponentiation_time(): # function_definition
    setup = """ # assignment
from random import randint
from __main__ import fibonacci_with_matrix_exponentiation
from random import randint
from __main__ import simple_fibonacci
""" # literal=Str
    code = "simple_fibonacci(randint(1,70000), 1, 1)" # assignment, literal=Str
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100) # assignment, literal=Num, method_call=timeit, suggest_constant_definition
    print( # function_call=print
        "Without matrix exponentiation the average execution time is ", exec_time / 100 # binary_operator=Div, literal=Num, literal=Str, suggest_constant_definition
    )
    return exec_time
def main(): # function_definition
    matrix_exponentiation_time() # function_call=matrix_exponentiation_time
    simple_fibonacci_time() # function_call=simple_fibonacci_time

# ----------------------------------------------------------------------------------------
# ../Python/maths/mobius_function.py
# ----------------------------------------------------------------------------------------
from maths.prime_factors import prime_factors
from maths.is_square_free import is_square_free
def mobius(n: int) -> int: # function_definition
    factors = prime_factors(n) # assignment, function_call=prime_factors
    if is_square_free(factors): # function_call=is_square_free, if
        return -1 if len(factors) % 2 else 1 # binary_operator=Mod, function_call=len, literal=Num, unary_operator=USub
    return 0 # literal=Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/modular_exponential.py
# ----------------------------------------------------------------------------------------
def modular_exponential(base, power, mod): # function_definition
    if power < 0: # comparison_operator=Lt, if, literal=Num
        return -1 # literal=Num, unary_operator=USub
    base %= mod # augmented_assignment
    result = 1 # assignment, literal=Num
    while power > 0: # comparison_operator=Gt, evolve_state (-> +3), literal=Num
        if power & 1: # binary_operator=BitAnd, if, literal=Num
            result = (result * base) % mod # assignment, binary_operator=Mod, binary_operator=Mult
        power = power >> 1 # assignment, binary_operator=RShift, literal=Num, suggest_augmented_assignment
        base = (base * base) % mod # assignment, binary_operator=Mod, binary_operator=Mult
    return result
def main(): # function_definition
    print(modular_exponential(3, 200, 13)) # composition, function_call=modular_exponential, function_call=print, literal=Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/newton_raphson.py
# ----------------------------------------------------------------------------------------
import math as m
def calc_derivative(f, a, h=0.001): # function_definition, literal=Num
    return (f(a + h) - f(a - h)) / (2 * h) # binary_operator=Add, binary_operator=Div, binary_operator=Mult, binary_operator=Sub, function_call=f, literal=Num
def newton_raphson(f, x0=0, maxiter=100, step=0.0001, maxerror=1e-6, logsteps=False): # function_definition, literal=False, literal=Num
    a = x0  # set the initial guess # assignment
    steps = [a] # assignment
    error = abs(f(a)) # assignment, composition, function_call=abs, function_call=f
    f1 = lambda x: calc_derivative(f, x, h=step)  # Derivative of f(x) # assignment, function_call=calc_derivative
    for _ in range(maxiter): # for_range_stop, function_call=range
        if f1(a) == 0: # comparison_operator=Eq, function_call=f1, if, literal=Num
            raise ValueError("No converging solution found") # function_call=ValueError, literal=Str
        a = a - f(a) / f1(a)  # Calculate the next estimate # assignment, binary_operator=Div, binary_operator=Sub, function_call=f, function_call=f1, suggest_augmented_assignment
        if logsteps: # if
            steps.append(a) # method_call=append
        if error < maxerror: # comparison_operator=Lt, if
            break
    else:
        raise ValueError("Iteration limit reached, no converging solution found") # function_call=ValueError, literal=Str
    if logsteps: # if
        return a, error, steps
    return a, error

# ----------------------------------------------------------------------------------------
# ../Python/maths/perfect_square.py
# ----------------------------------------------------------------------------------------
import math
def perfect_square(num: int) -> bool: # function_definition
    return math.sqrt(num) * math.sqrt(num) == num # binary_operator=Mult, comparison_operator=Eq, method_call=sqrt

# ----------------------------------------------------------------------------------------
# ../Python/maths/polynomial_evaluation.py
# ----------------------------------------------------------------------------------------
from typing import Sequence
def evaluate_poly(poly: Sequence[float], x: float) -> float: # function_definition, index
    return sum(c * (x ** i) for i, c in enumerate(poly)) # binary_operator=Mult, binary_operator=Pow, composition, function_call=enumerate, function_call=sum
def horner(poly: Sequence[float], x: float) -> float: # function_definition, index
    result = 0.0 # assignment, literal=Num, suggest_constant_definition
    for coeff in reversed(poly): # accumulate_elements=Assign (-> +1), function_call=reversed
        result = result * x + coeff # assignment, binary_operator=Add, binary_operator=Mult
    return result

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_check.py
# ----------------------------------------------------------------------------------------
import math
import unittest
def prime_check(number): # function_definition
    if number < 2: # comparison_operator=Lt, if, literal=Num
        return False # literal=False
    if number < 4: # comparison_operator=Lt, if, literal=Num, suggest_constant_definition
        return True # literal=True
    if number % 2 == 0: # binary_operator=Mod, comparison_operator=Eq, divisibility_test=2, if, literal=Num
        return False # literal=False
    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2) # assignment, binary_operator=Add, composition, function_call=int, function_call=range, literal=Num, method_call=sqrt, suggest_constant_definition
    return not any(number % i == 0 for i in odd_numbers) # binary_operator=Mod, comparison_operator=Eq, divisibility_test, function_call=any, literal=Num, unary_operator=Not
class Test(unittest.TestCase):
    def test_primes(self): # function_definition
        self.assertTrue(prime_check(2)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue
        self.assertTrue(prime_check(3)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(5)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(7)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(11)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(13)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(17)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(19)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(23)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(29)) # composition, function_call=prime_check, literal=Num, method_call=assertTrue, suggest_constant_definition
    def test_not_primes(self): # function_definition
        self.assertFalse(prime_check(-19), "Negative numbers are not prime.") # composition, function_call=prime_check, literal=Num, literal=Str, method_call=assertFalse, suggest_constant_definition, unary_operator=USub
        self.assertFalse( # composition, method_call=assertFalse
            prime_check(0), "Zero doesn't have any divider, primes must have two" # function_call=prime_check, literal=Num, literal=Str
        )
        self.assertFalse( # composition, method_call=assertFalse
            prime_check(1), "One just have 1 divider, primes must have two." # function_call=prime_check, literal=Num, literal=Str
        )
        self.assertFalse(prime_check(2 * 2)) # binary_operator=Mult, composition, function_call=prime_check, literal=Num, method_call=assertFalse
        self.assertFalse(prime_check(2 * 3)) # binary_operator=Mult, composition, function_call=prime_check, literal=Num, method_call=assertFalse, suggest_constant_definition
        self.assertFalse(prime_check(3 * 3)) # binary_operator=Mult, composition, function_call=prime_check, literal=Num, method_call=assertFalse, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5)) # binary_operator=Mult, composition, function_call=prime_check, literal=Num, method_call=assertFalse, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5 * 7)) # binary_operator=Mult, composition, function_call=prime_check, literal=Num, method_call=assertFalse, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_factors.py
# ----------------------------------------------------------------------------------------
from typing import List
def prime_factors(n: int) -> List[int]: # function_definition, index
    i = 2 # assignment, literal=Num
    factors = [] # assignment, literal=List
    while i * i <= n: # binary_operator=Mult, comparison_operator=LtE, evolve_state (-> +4)
        if n % i: # binary_operator=Mod, if, if_else
            i += 1 # augmented_assignment, literal=Num
        else:
            n //= i # augmented_assignment
            factors.append(i) # method_call=append
    if n > 1: # comparison_operator=Gt, if, literal=Num
        factors.append(n) # method_call=append
    return factors

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_numbers.py
# ----------------------------------------------------------------------------------------
from typing import List
def primes(max: int) -> List[int]: # function_definition, index
    max += 1 # augmented_assignment, literal=Num
    numbers = [False] * max # assignment, binary_operator=Mult, literal=False, literal=List
    ret = [] # assignment, literal=List
    for i in range(2, max): # accumulate_elements=Attribute (-> +4), for_range_start, function_call=range, literal=Num
        if not numbers[i]: # if, index, unary_operator=Not
            for j in range(i, max, i): # for_range_step, function_call=range
                numbers[j] = True # assignment, index, literal=True
            ret.append(i) # method_call=append
    return ret

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_sieve_eratosthenes.py
# ----------------------------------------------------------------------------------------
def prime_sieve_eratosthenes(num): # function_definition
    primes = [True for i in range(num + 1)] # assignment, binary_operator=Add, function_call=range, literal=Num, literal=True
    p = 2 # assignment, literal=Num
    while p * p <= num: # binary_operator=Mult, comparison_operator=LtE
        if primes[p] == True: # comparison_operator=Eq, if, index, literal=True
            for i in range(p * p, num + 1, p): # binary_operator=Add, binary_operator=Mult, for_range_step, function_call=range, literal=Num
                primes[i] = False # assignment, index, literal=False
        p += 1 # augmented_assignment, literal=Num
    for prime in range(2, num + 1): # binary_operator=Add, for_range_start, function_call=range, literal=Num
        if primes[prime]: # if, index
            print(prime, end=" ") # function_call=print, literal=Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/qr_decomposition.py
# ----------------------------------------------------------------------------------------
import numpy as np
def qr_householder(A): # function_definition
    m, n = A.shape # assignment
    t = min(m, n) # assignment, function_call=min
    Q = np.eye(m) # assignment, method_call=eye
    R = A.copy() # assignment, method_call=copy
    for k in range(t - 1): # accumulate_elements=Assign (-> +8), binary_operator=Sub, for_range_stop, function_call=range, literal=Num
        x = R[k:, [k]] # assignment
        e1 = np.zeros_like(x) # assignment, method_call=zeros_like
        e1[0] = 1.0 # assignment, index, literal=Num, suggest_constant_definition
        alpha = np.linalg.norm(x) # assignment, method_call=norm
        v = x + np.sign(x[0]) * alpha * e1 # assignment, binary_operator=Add, binary_operator=Mult, index, literal=Num, method_call=sign
        v /= np.linalg.norm(v) # augmented_assignment, method_call=norm
        Q_k = np.eye(m - k) - 2.0 * v @ v.T # assignment, binary_operator=MatMult, binary_operator=Mult, binary_operator=Sub, literal=Num, method_call=eye, suggest_constant_definition
        Q_k = np.block([[np.eye(k), np.zeros((k, m - k))], [np.zeros((m - k, k)), Q_k]]) # assignment, binary_operator=Sub, composition, method_call=block, method_call=eye, method_call=zeros
        Q = Q @ Q_k.T # assignment, binary_operator=MatMult, suggest_augmented_assignment
        R = Q_k @ R # assignment, binary_operator=MatMult
    return Q, R

# ----------------------------------------------------------------------------------------
# ../Python/maths/quadratic_equations_complex_numbers.py
# ----------------------------------------------------------------------------------------
from math import sqrt
from typing import Tuple
def QuadraticEquation(a: int, b: int, c: int) -> Tuple[str, str]: # function_definition, index
    if a == 0: # comparison_operator=Eq, if, literal=Num
        raise ValueError("Coefficient 'a' must not be zero for quadratic equations.") # function_call=ValueError, literal=Str
    delta = b * b - 4 * a * c # assignment, binary_operator=Mult, binary_operator=Sub, literal=Num, suggest_constant_definition
    if delta >= 0: # comparison_operator=GtE, if, literal=Num
        return str((-b + sqrt(delta)) / (2 * a)), str((-b - sqrt(delta)) / (2 * a)) # binary_operator=Add, binary_operator=Div, binary_operator=Mult, binary_operator=Sub, composition, function_call=sqrt, function_call=str, literal=Num, unary_operator=USub
    snd = sqrt(-delta) # assignment, function_call=sqrt, unary_operator=USub
    if b == 0: # comparison_operator=Eq, if, literal=Num
        return f"({snd} * i) / 2", f"({snd} * i) / {2 * a}" # binary_operator=Mult, literal=Num, literal=Str
    b = -abs(b) # assignment, function_call=abs, unary_operator=USub
    return f"({b}+{snd} * i) / 2", f"({b}+{snd} * i) / {2 * a}" # binary_operator=Mult, literal=Num, literal=Str
def main(): # function_definition
    solutions = QuadraticEquation(a=5, b=6, c=1) # assignment, function_call=QuadraticEquation, literal=Num, suggest_constant_definition
    print("The equation solutions are: {} and {}".format(*solutions)) # composition, function_call=print, literal=Str, method_call=format

# ----------------------------------------------------------------------------------------
# ../Python/maths/radix2_fft.py
# ----------------------------------------------------------------------------------------
import mpmath  # for roots of unity
import numpy as np
class FFT:
    def __init__(self, polyA=[0], polyB=[0]): # function_definition, literal=List, literal=Num
        self.polyA = list(polyA)[:] # assignment, function_call=list, slice
        self.polyB = list(polyB)[:] # assignment, function_call=list, slice
        while self.polyA[-1] == 0: # comparison_operator=Eq, evolve_state (-> +1), index, literal=Num, unary_operator=USub
            self.polyA.pop() # method_call=pop
        self.len_A = len(self.polyA) # assignment, function_call=len
        while self.polyB[-1] == 0: # comparison_operator=Eq, evolve_state (-> +1), index, literal=Num, unary_operator=USub
            self.polyB.pop() # method_call=pop
        self.len_B = len(self.polyB) # assignment, function_call=len
        self.C_max_length = int( # assignment, composition, function_call=int
            2 ** np.ceil(np.log2(len(self.polyA) + len(self.polyB) - 1)) # binary_operator=Add, binary_operator=Pow, binary_operator=Sub, composition, function_call=len, literal=Num, method_call=ceil, method_call=log2
        )
        while len(self.polyA) < self.C_max_length: # comparison_operator=Lt, evolve_state (-> +1), function_call=len
            self.polyA.append(0) # literal=Num, method_call=append
        while len(self.polyB) < self.C_max_length: # comparison_operator=Lt, evolve_state (-> +1), function_call=len
            self.polyB.append(0) # literal=Num, method_call=append
        self.root = complex(mpmath.root(x=1, n=self.C_max_length, k=1)) # assignment, composition, function_call=complex, literal=Num, method_call=root
        self.product = self.__multiply() # assignment, method_call=__multiply
    def __DFT(self, which): # function_definition
        if which == "A": # comparison_operator=Eq, if, if_else, literal=Str, suggest_conditional_expression (-> +3)
            dft = [[x] for x in self.polyA] # assignment
        else:
            dft = [[x] for x in self.polyB] # assignment
        if len(dft) <= 1: # comparison_operator=LtE, function_call=len, if, literal=Num
            return dft[0] # index, literal=Num
        next_ncol = self.C_max_length // 2 # assignment, binary_operator=FloorDiv, literal=Num
        while next_ncol > 0: # comparison_operator=Gt, evolve_state (-> +14), literal=Num
            new_dft = [[] for i in range(next_ncol)] # assignment, function_call=range, literal=List
            root = self.root ** next_ncol # assignment, binary_operator=Pow
            current_root = 1 # assignment, literal=Num
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator=FloorDiv, binary_operator=Mult, for_range_stop, function_call=range, literal=Num, nested_for (-> +1)
                for i in range(next_ncol): # for_range_stop, function_call=range
                    new_dft[i].append(dft[i][j] + current_root * dft[i + next_ncol][j]) # binary_operator=Add, binary_operator=Mult, index, method_call=append
                current_root *= root # augmented_assignment
            current_root = 1 # assignment, literal=Num
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator=FloorDiv, binary_operator=Mult, for_range_stop, function_call=range, literal=Num, nested_for (-> +1)
                for i in range(next_ncol): # for_range_stop, function_call=range
                    new_dft[i].append(dft[i][j] - current_root * dft[i + next_ncol][j]) # binary_operator=Add, binary_operator=Mult, binary_operator=Sub, index, method_call=append
                current_root *= root # augmented_assignment
            dft = new_dft # assignment
            next_ncol = next_ncol // 2 # assignment, binary_operator=FloorDiv, literal=Num, suggest_augmented_assignment
        return dft[0] # index, literal=Num
    def __multiply(self): # function_definition
        dftA = self.__DFT("A") # assignment, literal=Str, method_call=__DFT
        dftB = self.__DFT("B") # assignment, literal=Str, method_call=__DFT
        inverseC = [[dftA[i] * dftB[i] for i in range(self.C_max_length)]] # assignment, binary_operator=Mult, function_call=range, index
        del dftA
        del dftB
        if len(inverseC[0]) <= 1: # comparison_operator=LtE, function_call=len, if, index, literal=Num
            return inverseC[0] # index, literal=Num
        next_ncol = 2 # assignment, literal=Num
        while next_ncol <= self.C_max_length: # comparison_operator=LtE, evolve_state (-> +13)
            new_inverseC = [[] for i in range(next_ncol)] # assignment, function_call=range, literal=List
            root = self.root ** (next_ncol // 2) # assignment, binary_operator=FloorDiv, binary_operator=Pow, literal=Num
            current_root = 1 # assignment, literal=Num
            for j in range(self.C_max_length // next_ncol): # binary_operator=FloorDiv, for_range_stop, function_call=range, nested_for (-> +1)
                for i in range(next_ncol // 2): # binary_operator=FloorDiv, for_range_stop, function_call=range, literal=Num
                    new_inverseC[i].append( # index, method_call=append
                        ( # binary_operator=Div
                            inverseC[i][j] # binary_operator=Add, index
                            + inverseC[i][j + self.C_max_length // next_ncol] # binary_operator=Add, binary_operator=FloorDiv, index
                        )
                        / 2 # literal=Num
                    )
                    new_inverseC[i + next_ncol // 2].append( # binary_operator=Add, binary_operator=FloorDiv, index, literal=Num, method_call=append
                        ( # binary_operator=Div
                            inverseC[i][j] # binary_operator=Sub, index
                            - inverseC[i][j + self.C_max_length // next_ncol] # binary_operator=Add, binary_operator=FloorDiv, index
                        )
                        / (2 * current_root) # binary_operator=Mult, literal=Num
                    )
                current_root *= root # augmented_assignment
            inverseC = new_inverseC # assignment
            next_ncol *= 2 # augmented_assignment, literal=Num
        inverseC = [round(x[0].real, 8) + round(x[0].imag, 8) * 1j for x in inverseC] # assignment, binary_operator=Add, binary_operator=Mult, function_call=round, index, literal=Num, suggest_constant_definition
        while inverseC[-1] == 0: # comparison_operator=Eq, evolve_state (-> +1), index, literal=Num, unary_operator=USub
            inverseC.pop() # method_call=pop
        return inverseC
    def __str__(self): # function_definition
        A = "A = " + " + ".join( # assignment, binary_operator=Add, composition, literal=Str, method_call=join
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyA[: self.len_A]) # function_call=enumerate, literal=Str, slice
        )
        B = "B = " + " + ".join( # assignment, binary_operator=Add, composition, literal=Str, method_call=join
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyB[: self.len_B]) # function_call=enumerate, literal=Str, slice
        )
        C = "A*B = " + " + ".join( # assignment, binary_operator=Add, composition, literal=Str, method_call=join
            f"{coef}*x^{i}" for coef, i in enumerate(self.product) # function_call=enumerate, literal=Str
        )
        return "\n".join((A, B, C)) # literal=Str, method_call=join

# ----------------------------------------------------------------------------------------
# ../Python/maths/runge_kutta.py
# ----------------------------------------------------------------------------------------
import numpy as np
def runge_kutta(f, y0, x0, h, x_end): # function_definition
    N = int(np.ceil((x_end - x0) / h)) # assignment, binary_operator=Div, binary_operator=Sub, composition, function_call=int, method_call=ceil
    y = np.zeros((N + 1,)) # assignment, binary_operator=Add, literal=Num, method_call=zeros
    y[0] = y0 # assignment, index, literal=Num
    x = x0 # assignment
    for k in range(N): # accumulate_elements=Assign (-> +5), for_range_stop, function_call=range
        k1 = f(x, y[k]) # assignment, function_call=f, index
        k2 = f(x + 0.5 * h, y[k] + 0.5 * h * k1) # assignment, binary_operator=Add, binary_operator=Mult, function_call=f, index, literal=Num, suggest_constant_definition
        k3 = f(x + 0.5 * h, y[k] + 0.5 * h * k2) # assignment, binary_operator=Add, binary_operator=Mult, function_call=f, index, literal=Num, suggest_constant_definition
        k4 = f(x + h, y[k] + h * k3) # assignment, binary_operator=Add, binary_operator=Mult, function_call=f, index
        y[k + 1] = y[k] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4) # assignment, binary_operator=Add, binary_operator=Div, binary_operator=Mult, index, literal=Num, suggest_constant_definition
        x += h # augmented_assignment
    return y

# ----------------------------------------------------------------------------------------
# ../Python/maths/segmented_sieve.py
# ----------------------------------------------------------------------------------------
import math
def sieve(n): # function_definition
    in_prime = [] # assignment, literal=List
    start = 2 # assignment, literal=Num
    end = int(math.sqrt(n))  # Size of every segment # assignment, composition, function_call=int, method_call=sqrt
    temp = [True] * (end + 1) # assignment, binary_operator=Add, binary_operator=Mult, literal=List, literal=Num, literal=True
    prime = [] # assignment, literal=List
    while start <= end: # comparison_operator=LtE
        if temp[start] is True: # comparison_operator=Is, if, index, literal=True
            in_prime.append(start) # method_call=append
            for i in range(start * start, end + 1, start): # binary_operator=Add, binary_operator=Mult, for_range_step, function_call=range, literal=Num
                if temp[i] is True: # comparison_operator=Is, if, index, literal=True
                    temp[i] = False # assignment, index, literal=False
        start += 1 # augmented_assignment, literal=Num
    prime += in_prime # augmented_assignment
    low = end + 1 # assignment, binary_operator=Add, literal=Num
    high = low + end - 1 # assignment, binary_operator=Add, binary_operator=Sub, literal=Num
    if high > n: # comparison_operator=Gt, if
        high = n # assignment
    while low <= n: # comparison_operator=LtE
        temp = [True] * (high - low + 1) # assignment, binary_operator=Add, binary_operator=Mult, binary_operator=Sub, literal=List, literal=Num, literal=True
        for each in in_prime: # accumulate_elements=AugAssign (-> +3), for_each, nested_for (-> +4)
            t = math.floor(low / each) * each # assignment, binary_operator=Div, binary_operator=Mult, method_call=floor
            if t < low: # comparison_operator=Lt, if
                t += each # augmented_assignment
            for j in range(t, high + 1, each): # binary_operator=Add, for_range_step, function_call=range, literal=Num
                temp[j - low] = False # assignment, binary_operator=Sub, index, literal=False
        for j in range(len(temp)): # composition, for_indexes, for_range_stop, function_call=len, function_call=range
            if temp[j] is True: # comparison_operator=Is, if, index, literal=True
                prime.append(j + low) # binary_operator=Add, method_call=append
        low = high + 1 # assignment, binary_operator=Add, literal=Num
        high = low + end - 1 # assignment, binary_operator=Add, binary_operator=Sub, literal=Num
        if high > n: # comparison_operator=Gt, if
            high = n # assignment
    return prime
print(sieve(10 ** 6)) # binary_operator=Pow, composition, function_call=print, function_call=sieve, literal=Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/sieve_of_eratosthenes.py
# ----------------------------------------------------------------------------------------
import math
def sieve(n): # function_definition
    l = [True] * (n + 1) # assignment, binary_operator=Add, binary_operator=Mult, literal=List, literal=Num, literal=True
    prime = [] # assignment, literal=List
    start = 2 # assignment, literal=Num
    end = int(math.sqrt(n)) # assignment, composition, function_call=int, method_call=sqrt
    while start <= end: # comparison_operator=LtE
        if l[start] is True: # comparison_operator=Is, if, index, literal=True
            prime.append(start) # method_call=append
            for i in range(start * start, n + 1, start): # binary_operator=Add, binary_operator=Mult, for_range_step, function_call=range, literal=Num
                if l[i] is True: # comparison_operator=Is, if, index, literal=True
                    l[i] = False # assignment, index, literal=False
        start += 1 # augmented_assignment, literal=Num
    for j in range(end + 1, n + 1): # accumulate_elements=Attribute (-> +2), binary_operator=Add, for_range_start, function_call=range, literal=Num
        if l[j] is True: # comparison_operator=Is, if, index, literal=True
            prime.append(j) # method_call=append
    return prime

# ----------------------------------------------------------------------------------------
# ../Python/maths/simpson_rule.py
# ----------------------------------------------------------------------------------------
def method_2(boundary, steps): # function_definition
    h = (boundary[1] - boundary[0]) / steps # assignment, binary_operator=Div, binary_operator=Sub, index, literal=Num
    a = boundary[0] # assignment, index, literal=Num
    b = boundary[1] # assignment, index, literal=Num
    x_i = make_points(a, b, h) # assignment, function_call=make_points
    y = 0.0 # assignment, literal=Num, suggest_constant_definition
    y += (h / 3.0) * f(a) # augmented_assignment, binary_operator=Div, binary_operator=Mult, function_call=f, literal=Num, suggest_constant_definition
    cnt = 2 # assignment, literal=Num
    for i in x_i: # accumulate_elements=AugAssign (-> +1), for_each
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i) # augmented_assignment, binary_operator=Div, binary_operator=Mod, binary_operator=Mult, binary_operator=Sub, function_call=f, literal=Num, suggest_constant_definition
        cnt += 1 # augmented_assignment, literal=Num
    y += (h / 3.0) * f(b) # augmented_assignment, binary_operator=Div, binary_operator=Mult, function_call=f, literal=Num, suggest_constant_definition
    return y
def make_points(a, b, h): # function_definition
    x = a + h # assignment, binary_operator=Add
    while x < (b - h): # binary_operator=Sub, comparison_operator=Lt
        yield x
        x = x + h # assignment, binary_operator=Add, suggest_augmented_assignment
def f(x):  # enter your function here # function_definition
    y = (x - 0) * (x - 0) # assignment, binary_operator=Mult, binary_operator=Sub, literal=Num
    return y
def main(): # function_definition
    a = 0.0  # Lower bound of integration # assignment, literal=Num, suggest_constant_definition
    b = 1.0  # Upper bound of integration # assignment, literal=Num, suggest_constant_definition
    steps = 10.0  # define number of steps or resolution # assignment, literal=Num, suggest_constant_definition
    boundary = [a, b]  # define boundary of integration # assignment
    y = method_2(boundary, steps) # assignment, function_call=method_2
    print("y = {0}".format(y)) # composition, function_call=print, literal=Str, method_call=format

# ----------------------------------------------------------------------------------------
# ../Python/maths/softmax.py
# ----------------------------------------------------------------------------------------
import numpy as np
def softmax(vector): # function_definition
    exponentVector = np.exp(vector) # assignment, method_call=exp
    sumOfExponents = np.sum(exponentVector) # assignment, method_call=sum
    softmax_vector = exponentVector / sumOfExponents # assignment, binary_operator=Div
    return softmax_vector

# ----------------------------------------------------------------------------------------
# ../Python/maths/sum_of_arithmetic_series.py
# ----------------------------------------------------------------------------------------
def sum_of_series(first_term, common_diff, num_of_terms): # function_definition
    sum = (num_of_terms / 2) * (2 * first_term + (num_of_terms - 1) * common_diff) # assignment, binary_operator=Add, binary_operator=Div, binary_operator=Mult, binary_operator=Sub, literal=Num
    return sum
def main(): # function_definition
    print(sum_of_series(1, 1, 10)) # composition, function_call=print, function_call=sum_of_series, literal=Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/test_prime_check.py
# ----------------------------------------------------------------------------------------
from .prime_check import Test
Test() # function_call=Test

# ----------------------------------------------------------------------------------------
# ../Python/maths/trapezoidal_rule.py
# ----------------------------------------------------------------------------------------
def method_1(boundary, steps): # function_definition
    h = (boundary[1] - boundary[0]) / steps # assignment, binary_operator=Div, binary_operator=Sub, index, literal=Num
    a = boundary[0] # assignment, index, literal=Num
    b = boundary[1] # assignment, index, literal=Num
    x_i = make_points(a, b, h) # assignment, function_call=make_points
    y = 0.0 # assignment, literal=Num, suggest_constant_definition
    y += (h / 2.0) * f(a) # augmented_assignment, binary_operator=Div, binary_operator=Mult, function_call=f, literal=Num, suggest_constant_definition
    for i in x_i: # accumulate_elements=AugAssign (-> +1), for_each
        y += h * f(i) # augmented_assignment, binary_operator=Mult, function_call=f
    y += (h / 2.0) * f(b) # augmented_assignment, binary_operator=Div, binary_operator=Mult, function_call=f, literal=Num, suggest_constant_definition
    return y
def make_points(a, b, h): # function_definition
    x = a + h # assignment, binary_operator=Add
    while x < (b - h): # binary_operator=Sub, comparison_operator=Lt
        yield x
        x = x + h # assignment, binary_operator=Add, suggest_augmented_assignment
def f(x):  # enter your function here # function_definition
    y = (x - 0) * (x - 0) # assignment, binary_operator=Mult, binary_operator=Sub, literal=Num
    return y
def main(): # function_definition
    a = 0.0  # Lower bound of integration # assignment, literal=Num, suggest_constant_definition
    b = 1.0  # Upper bound of integration # assignment, literal=Num, suggest_constant_definition
    steps = 10.0  # define number of steps or resolution # assignment, literal=Num, suggest_constant_definition
    boundary = [a, b]  # define boundary of integration # assignment
    y = method_1(boundary, steps) # assignment, function_call=method_1
    print("y = {0}".format(y)) # composition, function_call=print, literal=Str, method_call=format

# ----------------------------------------------------------------------------------------
# ../Python/maths/volume.py
# ----------------------------------------------------------------------------------------
from math import pi
def vol_cube(side_length): # function_definition
    return float(side_length ** 3) # binary_operator=Pow, function_call=float, literal=Num, suggest_constant_definition
def vol_cuboid(width, height, length): # function_definition
    return float(width * height * length) # binary_operator=Mult, function_call=float
def vol_cone(area_of_base, height): # function_definition
    return (float(1) / 3) * area_of_base * height # binary_operator=Div, binary_operator=Mult, function_call=float, literal=Num, suggest_constant_definition
def vol_right_circ_cone(radius, height): # function_definition
    return (float(1) / 3) * pi * (radius ** 2) * height # binary_operator=Div, binary_operator=Mult, binary_operator=Pow, function_call=float, literal=Num, suggest_constant_definition
def vol_prism(area_of_base, height): # function_definition
    return float(area_of_base * height) # binary_operator=Mult, function_call=float
def vol_pyramid(area_of_base, height): # function_definition
    return (float(1) / 3) * area_of_base * height # binary_operator=Div, binary_operator=Mult, function_call=float, literal=Num, suggest_constant_definition
def vol_sphere(radius): # function_definition
    return (float(4) / 3) * pi * radius ** 3 # binary_operator=Div, binary_operator=Mult, binary_operator=Pow, function_call=float, literal=Num, suggest_constant_definition
def vol_circular_cylinder(radius, height): # function_definition
    return pi * radius ** 2 * height # binary_operator=Mult, binary_operator=Pow, literal=Num
def main(): # function_definition
    print("Volumes:") # function_call=print, literal=Str
    print("Cube: " + str(vol_cube(2)))  # = 8 # binary_operator=Add, composition, function_call=print, function_call=str, function_call=vol_cube, literal=Num, literal=Str
    print("Cuboid: " + str(vol_cuboid(2, 2, 2)))  # = 8 # binary_operator=Add, composition, function_call=print, function_call=str, function_call=vol_cuboid, literal=Num, literal=Str
    print("Cone: " + str(vol_cone(2, 2)))  # ~= 1.33 # binary_operator=Add, composition, function_call=print, function_call=str, function_call=vol_cone, literal=Num, literal=Str
    print("Right Circular Cone: " + str(vol_right_circ_cone(2, 2)))  # ~= 8.38 # binary_operator=Add, composition, function_call=print, function_call=str, function_call=vol_right_circ_cone, literal=Num, literal=Str
    print("Prism: " + str(vol_prism(2, 2)))  # = 4 # binary_operator=Add, composition, function_call=print, function_call=str, function_call=vol_prism, literal=Num, literal=Str
    print("Pyramid: " + str(vol_pyramid(2, 2)))  # ~= 1.33 # binary_operator=Add, composition, function_call=print, function_call=str, function_call=vol_pyramid, literal=Num, literal=Str
    print("Sphere: " + str(vol_sphere(2)))  # ~= 33.5 # binary_operator=Add, composition, function_call=print, function_call=str, function_call=vol_sphere, literal=Num, literal=Str
    print("Circular Cylinder: " + str(vol_circular_cylinder(2, 2)))  # ~= 25.1 # binary_operator=Add, composition, function_call=print, function_call=str, function_call=vol_circular_cylinder, literal=Num, literal=Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/zellers_congruence.py
# ----------------------------------------------------------------------------------------
import datetime
import argparse
def zeller(date_input: str) -> str: # function_definition
    days = { # assignment, literal=Dict
        "0": "Sunday", # literal=Str
        "1": "Monday", # literal=Str
        "2": "Tuesday", # literal=Str
        "3": "Wednesday", # literal=Str
        "4": "Thursday", # literal=Str
        "5": "Friday", # literal=Str
        "6": "Saturday", # literal=Str
    }
    convert_datetime_days = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0} # assignment, literal=Dict, literal=Num, suggest_constant_definition
    if not 0 < len(date_input) < 11: # comparison_operator=Lt, function_call=len, if, literal=Num, suggest_constant_definition, unary_operator=Not
        raise ValueError("Must be 10 characters long") # function_call=ValueError, literal=Str
    m: int = int(date_input[0] + date_input[1]) # binary_operator=Add, function_call=int, index, literal=Num
    if not 0 < m < 13: # comparison_operator=Lt, if, literal=Num, suggest_constant_definition, unary_operator=Not
        raise ValueError("Month must be between 1 - 12") # function_call=ValueError, literal=Str
    sep_1: str = date_input[2] # index, literal=Num
    if sep_1 not in ["-", "/"]: # comparison_operator=NotIn, if, literal=List, literal=Str
        raise ValueError("Date seperator must be '-' or '/'") # function_call=ValueError, literal=Str
    d: int = int(date_input[3] + date_input[4]) # binary_operator=Add, function_call=int, index, literal=Num, suggest_constant_definition
    if not 0 < d < 32: # comparison_operator=Lt, if, literal=Num, suggest_constant_definition, unary_operator=Not
        raise ValueError("Date must be between 1 - 31") # function_call=ValueError, literal=Str
    sep_2: str = date_input[5] # index, literal=Num, suggest_constant_definition
    if sep_2 not in ["-", "/"]: # comparison_operator=NotIn, if, literal=List, literal=Str
        raise ValueError("Date seperator must be '-' or '/'") # function_call=ValueError, literal=Str
    y: int = int(date_input[6] + date_input[7] + date_input[8] + date_input[9]) # binary_operator=Add, function_call=int, index, literal=Num, suggest_constant_definition
    if not 45 < y < 8500: # comparison_operator=Lt, if, literal=Num, suggest_constant_definition, unary_operator=Not
        raise ValueError( # function_call=ValueError
            "Year out of range. There has to be some sort of limit...right?" # literal=Str
        )
    dt_ck = datetime.date(int(y), int(m), int(d)) # assignment, composition, function_call=int, method_call=date
    if m <= 2: # comparison_operator=LtE, if, literal=Num
        y = y - 1 # assignment, binary_operator=Sub, literal=Num, suggest_augmented_assignment
        m = m + 12 # assignment, binary_operator=Add, literal=Num, suggest_augmented_assignment, suggest_constant_definition
    c: int = int(str(y)[:2]) # composition, function_call=int, function_call=str, literal=Num, slice
    k: int = int(str(y)[2:]) # composition, function_call=int, function_call=str, literal=Num, slice
    t: int = int(2.6 * m - 5.39) # binary_operator=Mult, binary_operator=Sub, function_call=int, literal=Num, suggest_constant_definition
    u: int = int(c / 4) # binary_operator=Div, function_call=int, literal=Num, suggest_constant_definition
    v: int = int(k / 4) # binary_operator=Div, function_call=int, literal=Num, suggest_constant_definition
    x: int = int(d + k) # binary_operator=Add, function_call=int
    z: int = int(t + u + v + x) # binary_operator=Add, function_call=int
    w: int = int(z - (2 * c)) # binary_operator=Mult, binary_operator=Sub, function_call=int, literal=Num
    f: int = round(w % 7) # binary_operator=Mod, function_call=round, literal=Num, suggest_constant_definition
    if f != convert_datetime_days[dt_ck.weekday()]: # comparison_operator=NotEq, if, index, method_call=weekday
        raise AssertionError("The date was evaluated incorrectly. Contact developer.") # function_call=AssertionError, literal=Str
    response: str = f"Your date {date_input}, is a {days[str(f)]}!" # function_call=str, index, literal=Str
    return response
