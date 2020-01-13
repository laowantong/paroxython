# ----------------------------------------------------------------------------------------
# ../Python/maths/3n+1.py
# ----------------------------------------------------------------------------------------
from typing import Tuple, List # import_from:typing
def n31(a: int) -> Tuple[List[int], int]: # function:n31, function_returning_a_value:n31, index
    if not isinstance(a, int): # function_call:isinstance, if (-> +1), unary_operator:Not
        raise TypeError("Must be int, not {0}".format(type(a).__name__)) # composition, function_call:TypeError, function_call:type, if_then_branch, literal:Str, method_call:format, raise_exception:TypeError
    if a < 1: # comparison_operator:Lt, if (-> +1), int_literal, literal:Num
        raise ValueError("Given integer must be greater than 1, not {0}".format(a)) # composition, function_call:ValueError, if_then_branch, literal:Str, method_call:format, raise_exception:ValueError
    path = [a] # assignment, variable_definition:path
    while a != 1: # comparison_operator:NotEq, evolve_state (-> +5), int_literal, literal:Num, while (-> +5)
        if a % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), int_literal, literal:Num, suggest_conditional_expression (-> +3)
            a = a // 2 # assignment, binary_operator:FloorDiv, if_then_branch, int_literal, literal:Num, suggest_augmented_assignment, variable_definition:a
        else:
            a = 3 * a + 1 # assignment, binary_operator:Add, binary_operator:Mult, if_else_branch, int_literal, literal:Num, suggest_constant_definition, variable_definition:a
        path += [a] # augmented_assignment
    return path, len(path) # function_call:len
def test_n31(): # function:test_n31 (-> +113), procedure:test_n31 (-> +113)
    assert n31(4) == ([4, 2, 1], 3) # assertion, comparison_operator:Eq, function_call:n31, int_literal, literal:List, literal:Num, literal:Tuple, suggest_constant_definition
    assert n31(11) == ([11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 15) # assertion, comparison_operator:Eq, function_call:n31, int_literal, literal:List, literal:Num, literal:Tuple, suggest_constant_definition
    assert n31(31) == ( # assertion, function_call:n31, int_literal, literal:Num, suggest_constant_definition
        [ # comparison_operator:Eq, literal:List, literal:Tuple
            31, # int_literal, literal:Num, suggest_constant_definition
            94, # int_literal, literal:Num, suggest_constant_definition
            47, # int_literal, literal:Num, suggest_constant_definition
            142, # int_literal, literal:Num, suggest_constant_definition
            71, # int_literal, literal:Num, suggest_constant_definition
            214, # int_literal, literal:Num, suggest_constant_definition
            107, # int_literal, literal:Num, suggest_constant_definition
            322, # int_literal, literal:Num, suggest_constant_definition
            161, # int_literal, literal:Num, suggest_constant_definition
            484, # int_literal, literal:Num, suggest_constant_definition
            242, # int_literal, literal:Num, suggest_constant_definition
            121, # int_literal, literal:Num, suggest_constant_definition
            364, # int_literal, literal:Num, suggest_constant_definition
            182, # int_literal, literal:Num, suggest_constant_definition
            91, # int_literal, literal:Num, suggest_constant_definition
            274, # int_literal, literal:Num, suggest_constant_definition
            137, # int_literal, literal:Num, suggest_constant_definition
            412, # int_literal, literal:Num, suggest_constant_definition
            206, # int_literal, literal:Num, suggest_constant_definition
            103, # int_literal, literal:Num, suggest_constant_definition
            310, # int_literal, literal:Num, suggest_constant_definition
            155, # int_literal, literal:Num, suggest_constant_definition
            466, # int_literal, literal:Num, suggest_constant_definition
            233, # int_literal, literal:Num, suggest_constant_definition
            700, # int_literal, literal:Num, suggest_constant_definition
            350, # int_literal, literal:Num, suggest_constant_definition
            175, # int_literal, literal:Num, suggest_constant_definition
            526, # int_literal, literal:Num, suggest_constant_definition
            263, # int_literal, literal:Num, suggest_constant_definition
            790, # int_literal, literal:Num, suggest_constant_definition
            395, # int_literal, literal:Num, suggest_constant_definition
            1186, # int_literal, literal:Num, suggest_constant_definition
            593, # int_literal, literal:Num, suggest_constant_definition
            1780, # int_literal, literal:Num, suggest_constant_definition
            890, # int_literal, literal:Num, suggest_constant_definition
            445, # int_literal, literal:Num, suggest_constant_definition
            1336, # int_literal, literal:Num, suggest_constant_definition
            668, # int_literal, literal:Num, suggest_constant_definition
            334, # int_literal, literal:Num, suggest_constant_definition
            167, # int_literal, literal:Num, suggest_constant_definition
            502, # int_literal, literal:Num, suggest_constant_definition
            251, # int_literal, literal:Num, suggest_constant_definition
            754, # int_literal, literal:Num, suggest_constant_definition
            377, # int_literal, literal:Num, suggest_constant_definition
            1132, # int_literal, literal:Num, suggest_constant_definition
            566, # int_literal, literal:Num, suggest_constant_definition
            283, # int_literal, literal:Num, suggest_constant_definition
            850, # int_literal, literal:Num, suggest_constant_definition
            425, # int_literal, literal:Num, suggest_constant_definition
            1276, # int_literal, literal:Num, suggest_constant_definition
            638, # int_literal, literal:Num, suggest_constant_definition
            319, # int_literal, literal:Num, suggest_constant_definition
            958, # int_literal, literal:Num, suggest_constant_definition
            479, # int_literal, literal:Num, suggest_constant_definition
            1438, # int_literal, literal:Num, suggest_constant_definition
            719, # int_literal, literal:Num, suggest_constant_definition
            2158, # int_literal, literal:Num, suggest_constant_definition
            1079, # int_literal, literal:Num, suggest_constant_definition
            3238, # int_literal, literal:Num, suggest_constant_definition
            1619, # int_literal, literal:Num, suggest_constant_definition
            4858, # int_literal, literal:Num, suggest_constant_definition
            2429, # int_literal, literal:Num, suggest_constant_definition
            7288, # int_literal, literal:Num, suggest_constant_definition
            3644, # int_literal, literal:Num, suggest_constant_definition
            1822, # int_literal, literal:Num, suggest_constant_definition
            911, # int_literal, literal:Num, suggest_constant_definition
            2734, # int_literal, literal:Num, suggest_constant_definition
            1367, # int_literal, literal:Num, suggest_constant_definition
            4102, # int_literal, literal:Num, suggest_constant_definition
            2051, # int_literal, literal:Num, suggest_constant_definition
            6154, # int_literal, literal:Num, suggest_constant_definition
            3077, # int_literal, literal:Num, suggest_constant_definition
            9232, # int_literal, literal:Num, suggest_constant_definition
            4616, # int_literal, literal:Num, suggest_constant_definition
            2308, # int_literal, literal:Num, suggest_constant_definition
            1154, # int_literal, literal:Num, suggest_constant_definition
            577, # int_literal, literal:Num, suggest_constant_definition
            1732, # int_literal, literal:Num, suggest_constant_definition
            866, # int_literal, literal:Num, suggest_constant_definition
            433, # int_literal, literal:Num, suggest_constant_definition
            1300, # int_literal, literal:Num, suggest_constant_definition
            650, # int_literal, literal:Num, suggest_constant_definition
            325, # int_literal, literal:Num, suggest_constant_definition
            976, # int_literal, literal:Num, suggest_constant_definition
            488, # int_literal, literal:Num, suggest_constant_definition
            244, # int_literal, literal:Num, suggest_constant_definition
            122, # int_literal, literal:Num, suggest_constant_definition
            61, # int_literal, literal:Num, suggest_constant_definition
            184, # int_literal, literal:Num, suggest_constant_definition
            92, # int_literal, literal:Num, suggest_constant_definition
            46, # int_literal, literal:Num, suggest_constant_definition
            23, # int_literal, literal:Num, suggest_constant_definition
            70, # int_literal, literal:Num, suggest_constant_definition
            35, # int_literal, literal:Num, suggest_constant_definition
            106, # int_literal, literal:Num, suggest_constant_definition
            53, # int_literal, literal:Num, suggest_constant_definition
            160, # int_literal, literal:Num, suggest_constant_definition
            80, # int_literal, literal:Num, suggest_constant_definition
            40, # int_literal, literal:Num, suggest_constant_definition
            20, # int_literal, literal:Num, suggest_constant_definition
            10, # int_literal, literal:Num, suggest_constant_definition
            5, # int_literal, literal:Num, suggest_constant_definition
            16, # int_literal, literal:Num, suggest_constant_definition
            8, # int_literal, literal:Num, suggest_constant_definition
            4, # int_literal, literal:Num, suggest_constant_definition
            2, # int_literal, literal:Num
            1, # int_literal, literal:Num
        ],
        107, # int_literal, literal:Num, suggest_constant_definition
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs.py
# ----------------------------------------------------------------------------------------
def abs_val(num): # function:abs_val (-> +1), function_returning_a_value:abs_val (-> +1)
    return -num if num < 0 else num # comparison_operator:Lt, conditional_expression, int_literal, literal:Num, unary_operator:USub
def test_abs_val(): # function:test_abs_val (-> +3), procedure:test_abs_val (-> +3)
    assert 0 == abs_val(0) # assertion, comparison_operator:Eq, function_call:abs_val, int_literal, literal:Num
    assert 34 == abs_val(34) # assertion, comparison_operator:Eq, function_call:abs_val, int_literal, literal:Num, suggest_constant_definition
    assert 100000000000 == abs_val(-100000000000) # assertion, comparison_operator:Eq, function_call:abs_val, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs_max.py
# ----------------------------------------------------------------------------------------
from typing import List # import_from:typing
def abs_max(x: List[int]) -> int: # function:abs_max, function_returning_a_value:abs_max, index
    j = x[0] # assignment, index, int_literal, literal:Num, variable_definition:j
    for i in x: # find_best_element (-> +2), for (-> +2), for_each (-> +2)
        if abs(i) > abs(j): # comparison_operator:Gt, function_call:abs, if (-> +1)
            j = i # assignment, if_then_branch, variable_definition:j
    return j
def abs_max_sort(x): # function:abs_max_sort (-> +1), function_returning_a_value:abs_max_sort (-> +1)
    return sorted(x, key=abs)[-1] # function_call:sorted, index, int_literal, literal:Num, negative_index:-1
def main(): # function:main (-> +3), procedure:main (-> +3)
    a = [1, 2, -11] # assignment, int_literal, literal:List, literal:Num, suggest_constant_definition, variable_definition:a
    assert abs_max(a) == -11 # assertion, comparison_operator:Eq, function_call:abs_max, int_literal, literal:Num, suggest_constant_definition
    assert abs_max_sort(a) == -11 # assertion, comparison_operator:Eq, function_call:abs_max_sort, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs_min.py
# ----------------------------------------------------------------------------------------
from .abs import abs_val # import_from:abs
def absMin(x): # function:absMin (-> +5), function_returning_a_value:absMin (-> +5)
    j = x[0] # assignment, index, int_literal, literal:Num, variable_definition:j
    for i in x: # find_best_element (-> +2), for (-> +2), for_each (-> +2)
        if abs_val(i) < abs_val(j): # comparison_operator:Lt, function_call:abs_val, if (-> +1)
            j = i # assignment, if_then_branch, variable_definition:j
    return j
def main(): # function:main (-> +2), procedure:main (-> +2)
    a = [-3, -1, 2, -11] # assignment, int_literal, literal:List, literal:Num, suggest_constant_definition, variable_definition:a
    print(absMin(a)) # composition, function_call:absMin, function_call:print

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_mean.py
# ----------------------------------------------------------------------------------------
def average(nums): # function:average (-> +1), function_returning_a_value:average (-> +1)
    return sum(nums) / len(nums) # binary_operator:Div, function_call:len, function_call:sum
def test_average(): # function:test_average (-> +3), procedure:test_average (-> +3)
    assert 12.0 == average([3, 6, 9, 12, 15, 18, 21]) # assertion, comparison_operator:Eq, float_literal, function_call:average, int_literal, literal:List, literal:Num, suggest_constant_definition
    assert 20 == average([5, 10, 15, 20, 25, 30, 35]) # assertion, comparison_operator:Eq, function_call:average, int_literal, literal:List, literal:Num, suggest_constant_definition
    assert 4.5 == average([1, 2, 3, 4, 5, 6, 7, 8]) # assertion, comparison_operator:Eq, float_literal, function_call:average, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_median.py
# ----------------------------------------------------------------------------------------
def median(nums): # function:median (-> +10), function_returning_a_value:median (-> +10)
    sorted_list = sorted(nums) # assignment, function_call:sorted, variable_definition:sorted_list
    med = None # assignment, literal:None, variable_definition:med
    if len(sorted_list) % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, function_call:len, if (-> +6), int_literal, literal:Num
        mid_index_1 = len(sorted_list) // 2 # assignment, binary_operator:FloorDiv, function_call:len, if_then_branch (-> +2), int_literal, literal:Num, variable_definition:mid_index_1
        mid_index_2 = (len(sorted_list) // 2) - 1 # assignment, binary_operator:FloorDiv, binary_operator:Sub, function_call:len, int_literal, literal:Num, variable_definition:mid_index_2
        med = (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / float(2) # assignment, binary_operator:Add, binary_operator:Div, function_call:float, index, int_literal, literal:Num, variable_definition:med
    else:
        mid_index = (len(sorted_list) - 1) // 2 # assignment, binary_operator:FloorDiv, binary_operator:Sub, function_call:len, if_else_branch (-> +1), int_literal, literal:Num, variable_definition:mid_index
        med = sorted_list[mid_index] # assignment, index, variable_definition:med
    return med
def main(): # function:main (-> +4), procedure:main (-> +4)
    print("Odd number of numbers:") # function_call:print, literal:Str
    print(median([2, 4, 6, 8, 20, 50, 70])) # composition, function_call:median, function_call:print, int_literal, literal:List, literal:Num, suggest_constant_definition
    print("Even number of numbers:") # function_call:print, literal:Str
    print(median([2, 4, 6, 8, 20, 50])) # composition, function_call:median, function_call:print, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_mode.py
# ----------------------------------------------------------------------------------------
import statistics # import:statistics
def mode(input_list): # function:mode (-> +7), function_returning_a_value:mode (-> +7)
    check_list = input_list.copy() # assignment, method_call:copy, variable_definition:check_list
    result = list() # assignment, function_call:list, variable_definition:result
    for x in input_list: # accumulate_elements:Attribute (-> +4), for (-> +4), for_each (-> +4)
        result.append(input_list.count(x)) # composition, method_call:append, method_call:count
        input_list.remove(x) # method_call:remove
        y = max(result) # assignment, function_call:max, variable_definition:y
        return check_list[result.index(y)] # index, method_call:index

# ----------------------------------------------------------------------------------------
# ../Python/maths/basic_maths.py
# ----------------------------------------------------------------------------------------
import math # import:math
def prime_factors(n: int) -> list: # function:prime_factors, function_returning_a_value:prime_factors
    pf = [] # assignment, literal:List, variable_definition:pf
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
        pf.append(2) # int_literal, literal:Num, method_call:append
        n = int(n / 2) # assignment, binary_operator:Div, function_call:int, int_literal, literal:Num, variable_definition:n
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_elements:Assign (-> +3), binary_operator:Add, composition, for (-> +3), for_range_step:2 (-> +3), function_call:int, function_call:range, int_literal, literal:Num, method_call:sqrt, suggest_constant_definition
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
            pf.append(i) # method_call:append
            n = int(n / i) # assignment, binary_operator:Div, function_call:int, variable_definition:n
    if n > 2: # comparison_operator:Gt, if (-> +1), int_literal, literal:Num
        pf.append(n) # if_then_branch, method_call:append
    return pf
def number_of_divisors(n: int) -> int: # function:number_of_divisors, function_returning_a_value:number_of_divisors
    div = 1 # assignment, int_literal, literal:Num, variable_definition:div
    temp = 1 # assignment, int_literal, literal:Num, variable_definition:temp
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
        temp += 1 # augmented_assignment, int_literal, literal:Num
        n = int(n / 2) # assignment, binary_operator:Div, function_call:int, int_literal, literal:Num, variable_definition:n
    div *= temp # augmented_assignment
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_elements:Assign (-> +5), binary_operator:Add, composition, for (-> +5), for_range_step:2 (-> +5), function_call:int, function_call:range, int_literal, literal:Num, method_call:sqrt, suggest_constant_definition
        temp = 1 # assignment, int_literal, literal:Num, variable_definition:temp
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +2)
            temp += 1 # augmented_assignment, int_literal, literal:Num
            n = int(n / i) # assignment, binary_operator:Div, function_call:int, variable_definition:n
        div *= temp # augmented_assignment
    return div
def sum_of_divisors(n: int) -> int: # function:sum_of_divisors, function_returning_a_value:sum_of_divisors
    s = 1 # assignment, int_literal, literal:Num, variable_definition:s
    temp = 1 # assignment, int_literal, literal:Num, variable_definition:temp
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
        temp += 1 # augmented_assignment, int_literal, literal:Num
        n = int(n / 2) # assignment, binary_operator:Div, function_call:int, int_literal, literal:Num, variable_definition:n
    if temp > 1: # comparison_operator:Gt, if (-> +1), int_literal, literal:Num
        s *= (2 ** temp - 1) / (2 - 1) # augmented_assignment, binary_operator:Div, binary_operator:Pow, binary_operator:Sub, if_then_branch, int_literal, literal:Num
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_elements:Assign (-> +6), binary_operator:Add, composition, for (-> +6), for_range_step:2 (-> +6), function_call:int, function_call:range, int_literal, literal:Num, method_call:sqrt, suggest_constant_definition
        temp = 1 # assignment, int_literal, literal:Num, variable_definition:temp
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +2)
            temp += 1 # augmented_assignment, int_literal, literal:Num
            n = int(n / i) # assignment, binary_operator:Div, function_call:int, variable_definition:n
        if temp > 1: # comparison_operator:Gt, if (-> +1), int_literal, literal:Num
            s *= (i ** temp - 1) / (i - 1) # augmented_assignment, binary_operator:Div, binary_operator:Pow, binary_operator:Sub, if_then_branch, int_literal, literal:Num
    return int(s) # function_call:int
def euler_phi(n: int) -> int: # function:euler_phi, function_returning_a_value:euler_phi
    s = n # assignment, variable_definition:s
    for x in set(prime_factors(n)): # accumulate_elements:AugAssign (-> +1), composition, for (-> +1), function_call:prime_factors, function_call:set
        s *= (x - 1) / x # augmented_assignment, binary_operator:Div, binary_operator:Sub, int_literal, literal:Num
    return int(s) # function_call:int

# ----------------------------------------------------------------------------------------
# ../Python/maths/binary_exponentiation.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n): # body_recursive_function:binary_exponentiation (-> +7), function:binary_exponentiation (-> +7), function_returning_a_value:binary_exponentiation (-> +7), recursive_function:binary_exponentiation (-> +7)
    if n == 0: # comparison_operator:Eq, if (-> +6), int_literal, literal:Num
        return 1 # if_then_branch, int_literal, literal:Num
    elif n % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +4), int_literal, literal:Num
        return binary_exponentiation(a, n - 1) * a # binary_operator:Mult, binary_operator:Sub, function_call:binary_exponentiation, if_elif_branch, int_literal, literal:Num
    else:
        b = binary_exponentiation(a, n / 2) # assignment, binary_operator:Div, function_call:binary_exponentiation, if_else_branch (-> +1), int_literal, literal:Num, variable_definition:b
        return b * b # binary_operator:Mult

# ----------------------------------------------------------------------------------------
# ../Python/maths/binomial_coefficient.py
# ----------------------------------------------------------------------------------------
def binomial_coefficient(n, r): # function:binomial_coefficient (-> +8), function_returning_a_value:binomial_coefficient (-> +8)
    C = [0 for i in range(r + 1)] # assignment, binary_operator:Add, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num, variable_definition:C
    C[0] = 1 # assignment, index, int_literal, literal:Num
    for i in range(1, n + 1): # binary_operator:Add, for (-> +4), for_range_start (-> +4), function_call:range, int_literal, literal:Num
        j = min(i, r) # assignment, function_call:min, variable_definition:j
        while j > 0: # comparison_operator:Gt, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
            C[j] += C[j - 1] # augmented_assignment, binary_operator:Sub, index, index_arithmetic, int_literal, literal:Num
            j -= 1 # augmented_assignment, int_literal, literal:Num
    return C[r] # index
print(binomial_coefficient(n=10, r=5)) # composition, function_call:binomial_coefficient, function_call:print, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/ceil.py
# ----------------------------------------------------------------------------------------
def ceil(x) -> int: # function:ceil, function_returning_a_value:ceil
    return (
        x if isinstance(x, int) or x - int(x) == 0 else int(x + 1) if x > 0 else int(x) # binary_operator:Add, binary_operator:Sub, boolean_operator:Or, comparison_operator:Eq, comparison_operator:Gt, conditional_expression, function_call:int, function_call:isinstance, int_literal, literal:Num
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/collatz_sequence.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function:collatz_sequence (-> +8), function_returning_a_value:collatz_sequence (-> +8)
    sequence = [n] # assignment, variable_definition:sequence
    while n != 1: # comparison_operator:NotEq, evolve_state (-> +5), int_literal, literal:Num, while (-> +5)
        if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), int_literal, literal:Num
            n //= 2 # augmented_assignment, if_then_branch, int_literal, literal:Num
        else:
            n = 3 * n + 1 # assignment, binary_operator:Add, binary_operator:Mult, if_else_branch, int_literal, literal:Num, suggest_constant_definition, variable_definition:n
        sequence.append(n) # method_call:append
    return sequence
def main(): # function:main (-> +4), procedure:main (-> +4)
    n = 43 # assignment, int_literal, literal:Num, suggest_constant_definition, variable_definition:n
    sequence = collatz_sequence(n) # assignment, function_call:collatz_sequence, variable_definition:sequence
    print(sequence) # function_call:print
    print("collatz sequence from %d took %d steps." % (n, len(sequence))) # binary_operator:Mod, composition, function_call:len, function_call:print, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/explicit_euler.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy
def explicit_euler(ode_func, y0, x0, stepsize, x_end): # function:explicit_euler (-> +8), function_returning_a_value:explicit_euler (-> +8)
    N = int(np.ceil((x_end - x0) / stepsize)) # assignment, binary_operator:Div, binary_operator:Sub, composition, function_call:int, method_call:ceil, variable_definition:N
    y = np.zeros((N + 1,)) # assignment, binary_operator:Add, int_literal, literal:Num, method_call:zeros, variable_definition:y
    y[0] = y0 # assignment, index, int_literal, literal:Num
    x = x0 # assignment, variable_definition:x
    for k in range(N): # accumulate_elements:Assign (-> +2), for (-> +2), for_range_stop (-> +2), function_call:range
        y[k + 1] = y[k] + stepsize * ode_func(x, y[k]) # assignment, binary_operator:Add, binary_operator:Mult, function_call:ode_func, index, index_arithmetic, int_literal, literal:Num
        x += stepsize # augmented_assignment
    return y

# ----------------------------------------------------------------------------------------
# ../Python/maths/extended_euclidean_algorithm.py
# ----------------------------------------------------------------------------------------
import sys # import:sys
def extended_euclidean_algorithm(m, n): # function:extended_euclidean_algorithm (-> +31), function_returning_a_value:extended_euclidean_algorithm (-> +31)
    a = 0 # assignment, int_literal, literal:Num, variable_definition:a
    a_prime = 1 # assignment, int_literal, literal:Num, variable_definition:a_prime
    b = 1 # assignment, int_literal, literal:Num, variable_definition:b
    b_prime = 0 # assignment, int_literal, literal:Num, variable_definition:b_prime
    q = 0 # assignment, int_literal, literal:Num, variable_definition:q
    r = 0 # assignment, int_literal, literal:Num, variable_definition:r
    if m > n: # comparison_operator:Gt, if (-> +5)
        c = m # assignment, if_then_branch (-> +1), variable_definition:c
        d = n # assignment, variable_definition:d
    else:
        c = n # assignment, if_else_branch (-> +1), variable_definition:c
        d = m # assignment, variable_definition:d
    while True: # literal:True, while (-> +12)
        q = int(c / d) # assignment, binary_operator:Div, function_call:int, variable_definition:q
        r = c % d # assignment, binary_operator:Mod, variable_definition:r
        if r == 0: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
            break # if_then_branch
        c = d # assignment, variable_definition:c
        d = r # assignment, variable_definition:d
        t = a_prime # assignment, variable_definition:t
        a_prime = a # assignment, variable_definition:a_prime
        a = t - q * a # assignment, binary_operator:Mult, binary_operator:Sub, variable_definition:a
        t = b_prime # assignment, variable_definition:t
        b_prime = b # assignment, variable_definition:b_prime
        b = t - q * b # assignment, binary_operator:Mult, binary_operator:Sub, variable_definition:b
    pair = None # assignment, literal:None, variable_definition:pair
    if m > n: # comparison_operator:Gt, if (-> +3), suggest_conditional_expression (-> +3)
        pair = (a, b) # assignment, if_then_branch, variable_definition:pair
    else:
        pair = (b, a) # assignment, if_else_branch, variable_definition:pair
    return pair
def main(): # function:main (-> +6), procedure:main (-> +6)
    if len(sys.argv) < 3: # comparison_operator:Lt, function_call:len, if (-> +2), int_literal, literal:Num, suggest_constant_definition
        print("2 integer arguments required") # function_call:print, if_then_branch (-> +1), literal:Str
        exit(1) # function_call:exit, int_literal, literal:Num
    m = int(sys.argv[1]) # assignment, function_call:int, index, int_literal, literal:Num, variable_definition:m
    n = int(sys.argv[2]) # assignment, function_call:int, index, int_literal, literal:Num, variable_definition:n
    print(extended_euclidean_algorithm(m, n)) # composition, function_call:extended_euclidean_algorithm, function_call:print

# ----------------------------------------------------------------------------------------
# ../Python/maths/factorial_python.py
# ----------------------------------------------------------------------------------------
def factorial(input_number: int) -> int: # function:factorial, function_returning_a_value:factorial
    if input_number < 0: # comparison_operator:Lt, if (-> +1), int_literal, literal:Num
        raise ValueError("factorial() not defined for negative values") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    if not isinstance(input_number, int): # function_call:isinstance, if (-> +1), unary_operator:Not
        raise ValueError("factorial() only accepts integral values") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    result = 1 # assignment, int_literal, literal:Num, variable_definition:result
    for i in range(1, input_number): # accumulate_elements:Assign (-> +1), for (-> +1), for_range_start (-> +1), function_call:range, int_literal, literal:Num
        result = result * (i + 1) # assignment, binary_operator:Add, binary_operator:Mult, int_literal, literal:Num, suggest_augmented_assignment, variable_definition:result
    return result

# ----------------------------------------------------------------------------------------
# ../Python/maths/factorial_recursive.py
# ----------------------------------------------------------------------------------------
def factorial(n: int) -> int: # body_recursive_function:factorial, function:factorial, function_returning_a_value:factorial, recursive_function:factorial
    if n < 0: # comparison_operator:Lt, if (-> +1), int_literal, literal:Num
        raise ValueError("factorial() not defined for negative values") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    if not isinstance(n, int): # function_call:isinstance, if (-> +1), unary_operator:Not
        raise ValueError("factorial() only accepts integral values") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    return 1 if n == 0 or n == 1 else n * factorial(n - 1) # binary_operator:Mult, binary_operator:Sub, boolean_operator:Or, comparison_operator:Eq, conditional_expression, function_call:factorial, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/factors.py
# ----------------------------------------------------------------------------------------
def factors_of_a_number(num: int) -> list: # function:factors_of_a_number, function_returning_a_value:factors_of_a_number
    return [i for i in range(1, num + 1) if num % i == 0] # binary_operator:Add, binary_operator:Mod, comparison_operator:Eq, comprehension:List, comprehension_for_count:1, divisibility_test, filtered_comprehension, function_call:range, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/fermat_little_theorem.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n, mod): # body_recursive_function:binary_exponentiation (-> +7), function:binary_exponentiation (-> +7), function_returning_a_value:binary_exponentiation (-> +7), recursive_function:binary_exponentiation (-> +7)
    if n == 0: # comparison_operator:Eq, if (-> +6), int_literal, literal:Num
        return 1 # if_then_branch, int_literal, literal:Num
    elif n % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +4), int_literal, literal:Num
        return (binary_exponentiation(a, n - 1, mod) * a) % mod # binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, function_call:binary_exponentiation, if_elif_branch, int_literal, literal:Num
    else:
        b = binary_exponentiation(a, n / 2, mod) # assignment, binary_operator:Div, function_call:binary_exponentiation, if_else_branch (-> +1), int_literal, literal:Num, variable_definition:b
        return (b * b) % mod # binary_operator:Mod, binary_operator:Mult
p = 701 # assignment, int_literal, literal:Num, suggest_constant_definition, variable_definition:p
a = 1000000000 # assignment, int_literal, literal:Num, suggest_constant_definition, variable_definition:a
b = 10 # assignment, int_literal, literal:Num, suggest_constant_definition, variable_definition:b
print((a / b) % p == (a * binary_exponentiation(b, p - 2, p)) % p) # binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, comparison_operator:Eq, composition, divisibility_test, function_call:binary_exponentiation, function_call:print, int_literal, literal:Num
print((a / b) % p == (a * b ** (p - 2)) % p) # binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, comparison_operator:Eq, divisibility_test, function_call:print, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/fibonacci.py
# ----------------------------------------------------------------------------------------
import math # import:math
import functools # import:functools
import time # import:time
from decimal import getcontext, Decimal # import_from:decimal
getcontext().prec = 100 # assignment, function_call:getcontext, int_literal, literal:Num
def timer_decorator(func): # closure:timer_decorator (-> +10), function:timer_decorator (-> +10), function_returning_a_value:timer_decorator (-> +10), nested_function:timer_decorator (-> +10)
    def timer_wrapper(*args, **kwargs): # function:timer_wrapper (-> +8), function_returning_a_value:timer_wrapper (-> +8)
        start = time.time() # assignment, method_call:time, variable_definition:start
        func(*args, **kwargs) # function_call:func
        end = time.time() # assignment, method_call:time, variable_definition:end
        if int(end - start) > 0: # binary_operator:Sub, comparison_operator:Gt, function_call:int, if (-> +3), int_literal, literal:Num
            print(f"Run time for {func.__name__}: {(end - start):0.2f}s") # binary_operator:Sub, function_call:print, if_then_branch, literal:Str
        else:
            print(f"Run time for {func.__name__}: {(end - start)*1000:0.2f}ms") # binary_operator:Mult, binary_operator:Sub, function_call:print, if_else_branch, int_literal, literal:Num, literal:Str, suggest_constant_definition
        return func(*args, **kwargs) # function_call:func
    return timer_wrapper
class Error(Exception):
    pass
class ValueTooLargeError(Error):
    pass
class ValueTooSmallError(Error):
    pass
class ValueLessThanZero(Error):
    pass
def _check_number_input(n, min_thresh, max_thresh=None): # function:_check_number_input (-> +22), function_returning_a_value:_check_number_input (-> +22), function_with_default_positional_arguments:_check_number_input (-> +22), literal:None
    try: # catch_exception:ValueTooLargeError (-> +19)
        if n >= min_thresh and max_thresh is None: # boolean_operator:And, comparison_operator:GtE, comparison_operator:Is, if (-> +9), literal:None
            return True # if_then_branch, literal:True
        elif min_thresh <= n <= max_thresh: # chained_comparison:2, comparison_operator:LtE, if (-> +7)
            return True # if_elif_branch, literal:True
        elif n < 0: # comparison_operator:Lt, if (-> +5), int_literal, literal:Num
            raise ValueLessThanZero # if_elif_branch
        elif n < min_thresh: # comparison_operator:Lt, if (-> +3)
            raise ValueTooSmallError # if_elif_branch
        elif n > max_thresh: # comparison_operator:Gt, if (-> +1)
            raise ValueTooLargeError # if_elif_branch
    except ValueLessThanZero:
        print("Incorrect Input: number must not be less than 0") # function_call:print, literal:Str
    except ValueTooSmallError:
        print( # function_call:print
            f"Incorrect Input: input number must be > {min_thresh} for the recursive calculation" # literal:Str
        )
    except ValueTooLargeError:
        print( # function_call:print
            f"Incorrect Input: input number must be < {max_thresh} for the recursive calculation" # literal:Str
        )
    return False # literal:False
def fib_iterative(n): # function:fib_iterative (-> +8), function_returning_a_value:fib_iterative (-> +8)
    n = int(n) # assignment, function_call:int, variable_definition:n
    if _check_number_input(n, 2): # function_call:_check_number_input, if (-> +6), int_literal, literal:Num
        seq_out = [0, 1] # assignment, if_then_branch (-> +5), int_literal, literal:List, literal:Num, variable_definition:seq_out
        a, b = 0, 1 # assignment, int_literal, literal:Num, literal:Tuple, variable_definition:a, variable_definition:b
        for _ in range(n - len(seq_out)): # binary_operator:Sub, composition, for (-> +2), for_range_stop (-> +2), function_call:len, function_call:range
            a, b = b, a + b # assignment, binary_operator:Add, variable_definition:a, variable_definition:b
            seq_out.append(b) # method_call:append
        return seq_out
def fib_formula(n): # function:fib_formula (-> +12), function_returning_a_value:fib_formula (-> +12)
    seq_out = [0, 1] # assignment, int_literal, literal:List, literal:Num, variable_definition:seq_out
    n = int(n) # assignment, function_call:int, variable_definition:n
    if _check_number_input(n, 2, 1000000): # function_call:_check_number_input, if (-> +9), int_literal, literal:Num, suggest_constant_definition
        sqrt = Decimal(math.sqrt(5)) # assignment, composition, function_call:Decimal, if_then_branch (-> +8), int_literal, literal:Num, method_call:sqrt, suggest_constant_definition, variable_definition:sqrt
        phi_1 = Decimal(1 + sqrt) / Decimal(2) # assignment, binary_operator:Add, binary_operator:Div, function_call:Decimal, int_literal, literal:Num, variable_definition:phi_1
        phi_2 = Decimal(1 - sqrt) / Decimal(2) # assignment, binary_operator:Div, binary_operator:Sub, function_call:Decimal, int_literal, literal:Num, variable_definition:phi_2
        for i in range(2, n): # for (-> +4), for_range_start (-> +4), function_call:range, int_literal, literal:Num
            temp_out = ((phi_1 ** Decimal(i)) - (phi_2 ** Decimal(i))) * ( # assignment, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, function_call:Decimal, variable_definition:temp_out
                Decimal(sqrt) ** Decimal(-1) # binary_operator:Pow, function_call:Decimal, int_literal, literal:Num
            )
            seq_out.append(int(temp_out)) # composition, function_call:int, method_call:append
        return seq_out

# ----------------------------------------------------------------------------------------
# ../Python/maths/fibonacci_sequence_recursion.py
# ----------------------------------------------------------------------------------------
def recur_fibo(n): # body_recursive_function:recur_fibo (-> +1), function:recur_fibo (-> +1), function_returning_a_value:recur_fibo (-> +1), recursive_function:recur_fibo (-> +1)
    return n if n <= 1 else recur_fibo(n - 1) + recur_fibo(n - 2) # binary_operator:Add, binary_operator:Sub, comparison_operator:LtE, conditional_expression, function_call:recur_fibo, int_literal, literal:Num
def main(): # function:main (-> +6), procedure:main (-> +6)
    limit = int(input("How many terms to include in fibonacci series: ")) # assignment, composition, function_call:input, function_call:int, literal:Str, variable_definition:limit
    if limit > 0: # comparison_operator:Gt, if (-> +4), int_literal, literal:Num
        print(f"The first {limit} terms of the fibonacci series are as follows:") # function_call:print, if_then_branch (-> +1), literal:Str
        print([recur_fibo(n) for n in range(limit)]) # composition, comprehension:List, comprehension_for_count:1, function_call:print, function_call:range, function_call:recur_fibo
    else:
        print("Please enter a positive integer: ") # function_call:print, if_else_branch, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_max.py
# ----------------------------------------------------------------------------------------
def find_max(nums): # function:find_max (-> +5), function_returning_a_value:find_max (-> +5)
    max_num = nums[0] # assignment, index, int_literal, literal:Num, variable_definition:max_num
    for x in nums: # find_best_element (-> +2), for (-> +2), for_each (-> +2)
        if x > max_num: # comparison_operator:Gt, if (-> +1)
            max_num = x # assignment, if_then_branch, variable_definition:max_num
    return max_num
def main(): # function:main (-> +1), procedure:main (-> +1)
    print(find_max([2, 4, 9, 7, 19, 94, 5])) # composition, function_call:find_max, function_call:print, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_max_recursion.py
# ----------------------------------------------------------------------------------------
def find_max(nums, left, right): # function:find_max (-> +6), function_returning_a_value:find_max (-> +6), recursive_function:find_max (-> +6)
    if left == right: # comparison_operator:Eq, if (-> +1)
        return nums[left] # if_then_branch, index
    mid = (left + right) >> 1 # assignment, binary_operator:Add, binary_operator:RShift, int_literal, literal:Num, variable_definition:mid
    left_max = find_max(nums, left, mid) # assignment, function_call:find_max, variable_definition:left_max
    right_max = find_max(nums, mid + 1, right) # assignment, binary_operator:Add, function_call:find_max, int_literal, literal:Num, variable_definition:right_max
    return left_max if left_max >= right_max else right_max # comparison_operator:GtE, conditional_expression

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_min.py
# ----------------------------------------------------------------------------------------
def find_min(nums): # function:find_min (-> +5), function_returning_a_value:find_min (-> +5)
    min_num = nums[0] # assignment, index, int_literal, literal:Num, variable_definition:min_num
    for num in nums: # find_best_element (-> +2), for (-> +2), for_each (-> +2)
        if min_num > num: # comparison_operator:Gt, if (-> +1)
            min_num = num # assignment, if_then_branch, variable_definition:min_num
    return min_num
def main(): # function:main (-> +1), procedure:main (-> +1)
    assert find_min([0, 1, 2, 3, 4, 5, -3, 24, -56]) == -56 # assertion, comparison_operator:Eq, function_call:find_min, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_min_recursion.py
# ----------------------------------------------------------------------------------------
def find_min(nums, left, right): # function:find_min (-> +6), function_returning_a_value:find_min (-> +6), recursive_function:find_min (-> +6)
    if left == right: # comparison_operator:Eq, if (-> +1)
        return nums[left] # if_then_branch, index
    mid = (left + right) >> 1 # assignment, binary_operator:Add, binary_operator:RShift, int_literal, literal:Num, variable_definition:mid
    left_min = find_min(nums, left, mid) # assignment, function_call:find_min, variable_definition:left_min
    right_min = find_min(nums, mid + 1, right) # assignment, binary_operator:Add, function_call:find_min, int_literal, literal:Num, variable_definition:right_min
    return left_min if left_min <= right_min else right_min # comparison_operator:LtE, conditional_expression

# ----------------------------------------------------------------------------------------
# ../Python/maths/floor.py
# ----------------------------------------------------------------------------------------
def floor(x) -> int: # function:floor, function_returning_a_value:floor
    return (
        x if isinstance(x, int) or x - int(x) == 0 else int(x) if x > 0 else int(x - 1) # binary_operator:Sub, boolean_operator:Or, comparison_operator:Eq, comparison_operator:Gt, conditional_expression, function_call:int, function_call:isinstance, int_literal, literal:Num
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/gaussian.py
# ----------------------------------------------------------------------------------------
from numpy import pi, sqrt, exp # import_from:numpy
def gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> int: # float_literal, function:gaussian, function_returning_a_value:gaussian, function_with_default_positional_arguments:gaussian, literal:Num
    return 1 / sqrt(2 * pi * sigma ** 2) * exp(-((x - mu) ** 2) / 2 * sigma ** 2) # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, function_call:exp, function_call:sqrt, int_literal, literal:Num, unary_operator:USub

# ----------------------------------------------------------------------------------------
# ../Python/maths/greatest_common_divisor.py
# ----------------------------------------------------------------------------------------
def greatest_common_divisor(a, b): # function:greatest_common_divisor (-> +1), function_returning_a_value:greatest_common_divisor (-> +1), recursive_function:greatest_common_divisor (-> +1)
    return b if a == 0 else greatest_common_divisor(b % a, a) # binary_operator:Mod, comparison_operator:Eq, conditional_expression, function_call:greatest_common_divisor, int_literal, literal:Num
def gcd_by_iterative(x, y): # function:gcd_by_iterative (-> +3), function_returning_a_value:gcd_by_iterative (-> +3)
    while y: # while (-> +1)
        x, y = y, x % y # assignment, binary_operator:Mod, variable_definition:x, variable_definition:y
    return x
def main(): # function:main (-> +10), procedure:main (-> +10)
    try: # catch_exception (-> +9)
        nums = input("Enter two integers separated by comma (,): ").split(",") # assignment, function_call:input, literal:Str, method_call:split, variable_definition:nums
        num_1 = int(nums[0]) # assignment, function_call:int, index, int_literal, literal:Num, variable_definition:num_1
        num_2 = int(nums[1]) # assignment, function_call:int, index, int_literal, literal:Num, variable_definition:num_2
        print( # composition, function_call:print
            f"greatest_common_divisor({num_1}, {num_2}) = {greatest_common_divisor(num_1, num_2)}" # function_call:greatest_common_divisor, literal:Str
        )
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}") # composition, function_call:gcd_by_iterative, function_call:print, literal:Str
    except (IndexError, UnboundLocalError, ValueError):
        print("Wrong input") # function_call:print, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/hardy_ramanujanalgo.py
# ----------------------------------------------------------------------------------------
import math # import:math
def exactPrimeFactorCount(n): # function:exactPrimeFactorCount (-> +15), function_returning_a_value:exactPrimeFactorCount (-> +15)
    count = 0 # assignment, int_literal, literal:Num, variable_definition:count
    if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), int_literal, literal:Num
        count += 1 # augmented_assignment, if_then_branch (-> +2), int_literal, literal:Num
        while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +1), int_literal, literal:Num, while (-> +1)
            n = int(n / 2) # assignment, binary_operator:Div, function_call:int, int_literal, literal:Num, variable_definition:n
    i = 3 # assignment, int_literal, literal:Num, suggest_constant_definition, variable_definition:i
    while i <= int(math.sqrt(n)): # comparison_operator:LtE, composition, evolve_state (-> +5), function_call:int, method_call:sqrt, while (-> +5)
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +3), int_literal, literal:Num
            count += 1 # augmented_assignment, if_then_branch (-> +2), int_literal, literal:Num
            while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, int_literal, literal:Num, while (-> +1)
                n = int(n / i) # assignment, binary_operator:Div, function_call:int, variable_definition:n
        i = i + 2 # assignment, binary_operator:Add, int_literal, literal:Num, suggest_augmented_assignment, variable_definition:i
    if n > 2: # comparison_operator:Gt, if (-> +1), int_literal, literal:Num
        count += 1 # augmented_assignment, if_then_branch, int_literal, literal:Num
    return count

# ----------------------------------------------------------------------------------------
# ../Python/maths/is_square_free.py
# ----------------------------------------------------------------------------------------
from typing import List # import_from:typing
def is_square_free(factors: List[int]) -> bool: # function:is_square_free, function_returning_a_value:is_square_free, index
    return len(set(factors)) == len(factors) # comparison_operator:Eq, composition, function_call:len, function_call:set

# ----------------------------------------------------------------------------------------
# ../Python/maths/jaccard_similarity.py
# ----------------------------------------------------------------------------------------
def jaccard_similariy(setA, setB, alternativeUnion=False): # function:jaccard_similariy (-> +14), function_returning_a_value:jaccard_similariy (-> +14), function_with_default_positional_arguments:jaccard_similariy (-> +14), literal:False
    if isinstance(setA, set) and isinstance(setB, set): # boolean_operator:And, function_call:isinstance, if (-> +6)
        intersection = len(setA.intersection(setB)) # assignment, composition, function_call:len, if_then_branch (-> +5), method_call:intersection, variable_definition:intersection
        if alternativeUnion: # if (-> +3), nested_if:2 (-> +3), suggest_conditional_expression (-> +3)
            union = len(setA) + len(setB) # assignment, binary_operator:Add, function_call:len, if_then_branch, variable_definition:union
        else:
            union = len(setA.union(setB)) # assignment, composition, function_call:len, if_else_branch, method_call:union, variable_definition:union
        return intersection / union # binary_operator:Div
    if isinstance(setA, (list, tuple)) and isinstance(setB, (list, tuple)): # boolean_operator:And, function_call:isinstance, if (-> +6)
        intersection = [element for element in setA if element in setB] # assignment, comparison_operator:In, comprehension:List, comprehension_for_count:1, filtered_comprehension, if_then_branch (-> +5), variable_definition:intersection
        if alternativeUnion: # if (-> +3), nested_if:2 (-> +3), suggest_conditional_expression (-> +3)
            union = len(setA) + len(setB) # assignment, binary_operator:Add, function_call:len, if_then_branch, variable_definition:union
        else:
            union = setA + [element for element in setB if element not in setA] # assignment, binary_operator:Add, comparison_operator:NotIn, comprehension:List, comprehension_for_count:1, filtered_comprehension, if_else_branch, variable_definition:union
        return len(intersection) / len(union) # binary_operator:Div, function_call:len

# ----------------------------------------------------------------------------------------
# ../Python/maths/karatsuba.py
# ----------------------------------------------------------------------------------------
def karatsuba(a, b): # body_recursive_function:karatsuba (-> +11), function:karatsuba (-> +11), function_returning_a_value:karatsuba (-> +11), recursive_function:karatsuba (-> +11)
    if len(str(a)) == 1 or len(str(b)) == 1: # boolean_operator:Or, comparison_operator:Eq, composition, function_call:len, function_call:str, if (-> +10), int_literal, literal:Num
        return a * b # binary_operator:Mult, if_then_branch
    else:
        m1 = max(len(str(a)), len(str(b))) # assignment, composition, function_call:len, function_call:max, function_call:str, if_else_branch (-> +7), variable_definition:m1
        m2 = m1 // 2 # assignment, binary_operator:FloorDiv, int_literal, literal:Num, variable_definition:m2
        a1, a2 = divmod(a, 10 ** m2) # assignment, binary_operator:Pow, function_call:divmod, int_literal, literal:Num, suggest_constant_definition, variable_definition:a1, variable_definition:a2
        b1, b2 = divmod(b, 10 ** m2) # assignment, binary_operator:Pow, function_call:divmod, int_literal, literal:Num, suggest_constant_definition, variable_definition:b1, variable_definition:b2
        x = karatsuba(a2, b2) # assignment, function_call:karatsuba, variable_definition:x
        y = karatsuba((a1 + a2), (b1 + b2)) # assignment, binary_operator:Add, function_call:karatsuba, variable_definition:y
        z = karatsuba(a1, b1) # assignment, function_call:karatsuba, variable_definition:z
        return (z * 10 ** (2 * m2)) + ((y - z - x) * 10 ** (m2)) + (x) # binary_operator:Add, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition
def main(): # function:main (-> +1), procedure:main (-> +1)
    print(karatsuba(15463, 23489)) # composition, function_call:karatsuba, function_call:print, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/kth_lexicographic_permutation.py
# ----------------------------------------------------------------------------------------
def kthPermutation(k, n): # function:kthPermutation (-> +13), function_returning_a_value:kthPermutation (-> +13)
    factorials = [1] # assignment, int_literal, literal:List, literal:Num, variable_definition:factorials
    for i in range(2, n): # for (-> +1), for_range_start (-> +1), function_call:range, int_literal, literal:Num
        factorials.append(factorials[-1] * i) # binary_operator:Mult, index, int_literal, literal:Num, method_call:append, negative_index:-1
    assert 0 <= k < factorials[-1] * n, "k out of bounds" # assertion, binary_operator:Mult, chained_comparison:2, comparison_operator:Lt, comparison_operator:LtE, index, int_literal, literal:Num, literal:Str, negative_index:-1
    permutation = [] # assignment, literal:List, variable_definition:permutation
    elements = list(range(n)) # assignment, composition, function_call:list, function_call:range, variable_definition:elements
    while factorials: # while (-> +4)
        factorial = factorials.pop() # assignment, method_call:pop, variable_definition:factorial
        number, k = divmod(k, factorial) # assignment, function_call:divmod, variable_definition:k, variable_definition:number
        permutation.append(elements[number]) # index, method_call:append
        elements.remove(elements[number]) # index, method_call:remove
    permutation.append(elements[0]) # index, int_literal, literal:Num, method_call:append
    return permutation

# ----------------------------------------------------------------------------------------
# ../Python/maths/largest_of_very_large_numbers.py
# ----------------------------------------------------------------------------------------
import math # import:math
def res(x, y): # function:res (-> +7), function_returning_a_value:res (-> +7)
    if 0 not in (x, y): # comparison_operator:NotIn, if (-> +6), int_literal, literal:Num
        return y * math.log10(x) # binary_operator:Mult, if_then_branch, method_call:log10
    else:
        if x == 0: # comparison_operator:Eq, if (-> +3), int_literal, literal:Num
            return 0 # if_elif_branch, int_literal, literal:Num
        elif y == 0: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
            return 1 # if_elif_branch, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/least_common_multiple.py
# ----------------------------------------------------------------------------------------
import unittest # import:unittest
def find_lcm(first_num: int, second_num: int) -> int: # function:find_lcm, function_returning_a_value:find_lcm
    max_num = first_num if first_num >= second_num else second_num # assignment, comparison_operator:GtE, conditional_expression, variable_definition:max_num
    common_mult = max_num # assignment, variable_definition:common_mult
    while (common_mult % first_num > 0) or (common_mult % second_num > 0): # binary_operator:Mod, boolean_operator:Or, comparison_operator:Gt, int_literal, literal:Num, while (-> +1)
        common_mult += max_num # augmented_assignment
    return common_mult
class TestLeastCommonMultiple(unittest.TestCase):
    test_inputs = [ # assignment, literal:List, variable_definition:test_inputs
        (10, 20), # int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (13, 15), # int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (4, 31), # int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (10, 42), # int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (43, 34), # int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (5, 12), # int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (12, 25), # int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (10, 25), # int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (6, 9), # int_literal, literal:Num, literal:Tuple, suggest_constant_definition
    ]
    expected_results = [20, 195, 124, 210, 1462, 60, 300, 50, 18] # assignment, int_literal, literal:List, literal:Num, suggest_constant_definition, variable_definition:expected_results
    def test_lcm_function(self): # function:test_lcm_function (-> +4), procedure:test_lcm_function (-> +4)
        for i, (first_num, second_num) in enumerate(self.test_inputs): # for (-> +3), for_indexes_elements (-> +3), function_call:enumerate
            actual_result = find_lcm(first_num, second_num) # assignment, function_call:find_lcm, variable_definition:actual_result
            with self.subTest(i=i): # method_call:subTest
                self.assertEqual(actual_result, self.expected_results[i]) # index, method_call:assertEqual

# ----------------------------------------------------------------------------------------
# ../Python/maths/lucas_series.py
# ----------------------------------------------------------------------------------------
def recur_luc(n): # body_recursive_function:recur_luc (-> +5), function:recur_luc (-> +5), function_returning_a_value:recur_luc (-> +5), recursive_function:recur_luc (-> +5)
    if n == 1: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
        return n # if_then_branch
    if n == 0: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
        return 2 # if_then_branch, int_literal, literal:Num
    return recur_luc(n - 1) + recur_luc(n - 2) # binary_operator:Add, binary_operator:Sub, function_call:recur_luc, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/matrix_exponentiation.py
# ----------------------------------------------------------------------------------------
import timeit # import:timeit
class Matrix(object):
    def __init__(self, arg): # function:__init__ (-> +6), procedure:__init__ (-> +6)
        if isinstance(arg, list): # function_call:isinstance, if (-> +5)
            self.t = arg # assignment, if_then_branch (-> +1)
            self.n = len(arg) # assignment, function_call:len
        else:
            self.n = arg # assignment, if_else_branch (-> +1)
            self.t = [[0 for _ in range(self.n)] for _ in range(self.n)] # assignment, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num
    def __mul__(self, b): # function:__mul__ (-> +6), function_returning_a_value:__mul__ (-> +6)
        matrix = Matrix(self.n) # assignment, function_call:Matrix, variable_definition:matrix
        for i in range(self.n): # accumulate_elements:AugAssign (-> +3), for (-> +3), for_range_stop (-> +3), function_call:range, square_nested_for (-> +3)
            for j in range(self.n): # accumulate_elements:AugAssign (-> +2), for (-> +2), for_range_stop (-> +2), function_call:range, nested_for:2 (-> +2), square_nested_for (-> +2)
                for k in range(self.n): # accumulate_elements:AugAssign (-> +1), for (-> +1), for_range_stop (-> +1), function_call:range, nested_for:3 (-> +1)
                    matrix.t[i][j] += self.t[i][k] * b.t[k][j] # augmented_assignment, binary_operator:Mult, index
        return matrix
def modular_exponentiation(a, b): # function:modular_exponentiation (-> +7), function_returning_a_value:modular_exponentiation (-> +7)
    matrix = Matrix([[1, 0], [0, 1]]) # assignment, function_call:Matrix, int_literal, literal:List, literal:Num, variable_definition:matrix
    while b > 0: # comparison_operator:Gt, evolve_state (-> +4), int_literal, literal:Num, while (-> +4)
        if b & 1: # binary_operator:BitAnd, if (-> +1), int_literal, literal:Num
            matrix *= a # augmented_assignment, if_then_branch
        a *= a # augmented_assignment
        b >>= 1 # augmented_assignment, int_literal, literal:Num
    return matrix
def fibonacci_with_matrix_exponentiation(n, f1, f2): # function:fibonacci_with_matrix_exponentiation (-> +7), function_returning_a_value:fibonacci_with_matrix_exponentiation (-> +7)
    if n == 1: # comparison_operator:Eq, if (-> +3), int_literal, literal:Num
        return f1 # if_then_branch
    elif n == 2: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
        return f2 # if_elif_branch
    matrix = Matrix([[1, 1], [1, 0]]) # assignment, function_call:Matrix, int_literal, literal:List, literal:Num, variable_definition:matrix
    matrix = modular_exponentiation(matrix, n - 2) # assignment, binary_operator:Sub, function_call:modular_exponentiation, int_literal, literal:Num, variable_definition:matrix
    return f2 * matrix.t[0][0] + f1 * matrix.t[0][1] # binary_operator:Add, binary_operator:Mult, index, int_literal, literal:Num
def simple_fibonacci(n, f1, f2): # function:simple_fibonacci (-> +11), function_returning_a_value:simple_fibonacci (-> +11)
    if n == 1: # comparison_operator:Eq, if (-> +3), int_literal, literal:Num
        return f1 # if_then_branch
    elif n == 2: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
        return f2 # if_elif_branch
    fn_1 = f1 # assignment, variable_definition:fn_1
    fn_2 = f2 # assignment, variable_definition:fn_2
    n -= 2 # augmented_assignment, int_literal, literal:Num
    while n > 0: # comparison_operator:Gt, evolve_state (-> +2), int_literal, literal:Num, while (-> +2)
        fn_1, fn_2 = fn_1 + fn_2, fn_1 # assignment, binary_operator:Add, variable_definition:fn_1, variable_definition:fn_2
        n -= 1 # augmented_assignment, int_literal, literal:Num
    return fn_1
def matrix_exponentiation_time(): # function:matrix_exponentiation_time (-> +8), function_returning_a_value:matrix_exponentiation_time (-> +8)
    setup = """ # assignment, variable_definition:setup
from random import randint
from __main__ import fibonacci_with_matrix_exponentiation
""" # literal:Str
    code = "fibonacci_with_matrix_exponentiation(randint(1,70000), 1, 1)" # assignment, literal:Str, variable_definition:code
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100) # assignment, int_literal, literal:Num, method_call:timeit, suggest_constant_definition, variable_definition:exec_time
    print("With matrix exponentiation the average execution time is ", exec_time / 100) # binary_operator:Div, function_call:print, int_literal, literal:Num, literal:Str, suggest_constant_definition
    return exec_time
def simple_fibonacci_time(): # function:simple_fibonacci_time (-> +10), function_returning_a_value:simple_fibonacci_time (-> +10)
    setup = """ # assignment, variable_definition:setup
from random import randint
from __main__ import simple_fibonacci
""" # literal:Str
    code = "simple_fibonacci(randint(1,70000), 1, 1)" # assignment, literal:Str, variable_definition:code
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100) # assignment, int_literal, literal:Num, method_call:timeit, suggest_constant_definition, variable_definition:exec_time
    print( # function_call:print
        "Without matrix exponentiation the average execution time is ", exec_time / 100 # binary_operator:Div, int_literal, literal:Num, literal:Str, suggest_constant_definition
    )
    return exec_time
def main(): # function:main (-> +2), procedure:main (-> +2)
    matrix_exponentiation_time() # function_call:matrix_exponentiation_time
    simple_fibonacci_time() # function_call:simple_fibonacci_time

# ----------------------------------------------------------------------------------------
# ../Python/maths/mobius_function.py
# ----------------------------------------------------------------------------------------
from maths.prime_factors import prime_factors # import_from:maths.prime_factors
from maths.is_square_free import is_square_free # import_from:maths.is_square_free
def mobius(n: int) -> int: # function:mobius, function_returning_a_value:mobius
    factors = prime_factors(n) # assignment, function_call:prime_factors, variable_definition:factors
    if is_square_free(factors): # function_call:is_square_free, if (-> +1)
        return -1 if len(factors) % 2 else 1 # binary_operator:Mod, conditional_expression, function_call:len, if_then_branch, int_literal, literal:Num
    return 0 # int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/modular_exponential.py
# ----------------------------------------------------------------------------------------
def modular_exponential(base, power, mod): # function:modular_exponential (-> +10), function_returning_a_value:modular_exponential (-> +10)
    if power < 0: # comparison_operator:Lt, if (-> +1), int_literal, literal:Num
        return -1 # if_then_branch, int_literal, literal:Num
    base %= mod # augmented_assignment
    result = 1 # assignment, int_literal, literal:Num, variable_definition:result
    while power > 0: # comparison_operator:Gt, evolve_state (-> +4), int_literal, literal:Num, while (-> +4)
        if power & 1: # binary_operator:BitAnd, if (-> +1), int_literal, literal:Num
            result = (result * base) % mod # assignment, binary_operator:Mod, binary_operator:Mult, if_then_branch, variable_definition:result
        power = power >> 1 # assignment, binary_operator:RShift, int_literal, literal:Num, suggest_augmented_assignment, variable_definition:power
        base = (base * base) % mod # assignment, binary_operator:Mod, binary_operator:Mult, variable_definition:base
    return result
def main(): # function:main (-> +1), procedure:main (-> +1)
    print(modular_exponential(3, 200, 13)) # composition, function_call:modular_exponential, function_call:print, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/newton_raphson.py
# ----------------------------------------------------------------------------------------
import math as m # import:math
def calc_derivative(f, a, h=0.001): # float_literal, function:calc_derivative (-> +1), function_returning_a_value:calc_derivative (-> +1), function_with_default_positional_arguments:calc_derivative (-> +1), literal:Num
    return (f(a + h) - f(a - h)) / (2 * h) # binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, function_call:f, int_literal, literal:Num
def newton_raphson(f, x0=0, maxiter=100, step=0.0001, maxerror=1e-6, logsteps=False): # float_literal, function:newton_raphson (-> +17), function_returning_a_value:newton_raphson (-> +17), function_with_default_positional_arguments:newton_raphson (-> +17), int_literal, literal:False, literal:Num
    a = x0 # assignment, variable_definition:a
    steps = [a] # assignment, variable_definition:steps
    error = abs(f(a)) # assignment, composition, function_call:abs, function_call:f, variable_definition:error
    f1 = lambda x: calc_derivative(f, x, h=step) # assignment, function_call:calc_derivative, lambda_function, variable_definition:f1
    for _ in range(maxiter): # for (-> +9), for_range_stop (-> +9), function_call:range
        if f1(a) == 0: # comparison_operator:Eq, function_call:f1, if (-> +1), int_literal, literal:Num
            raise ValueError("No converging solution found") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
        a = a - f(a) / f1(a) # assignment, binary_operator:Div, binary_operator:Sub, function_call:f, function_call:f1, suggest_augmented_assignment, variable_definition:a
        if logsteps: # if (-> +1)
            steps.append(a) # if_then_branch, method_call:append
        if error < maxerror: # comparison_operator:Lt, if (-> +1)
            break # if_then_branch
    else:
        raise ValueError("Iteration limit reached, no converging solution found") # function_call:ValueError, literal:Str, raise_exception:ValueError
    if logsteps: # if (-> +1)
        return a, error, steps # if_then_branch
    return a, error

# ----------------------------------------------------------------------------------------
# ../Python/maths/perfect_square.py
# ----------------------------------------------------------------------------------------
import math # import:math
def perfect_square(num: int) -> bool: # function:perfect_square, function_returning_a_value:perfect_square
    return math.sqrt(num) * math.sqrt(num) == num # binary_operator:Mult, comparison_operator:Eq, method_call:sqrt

# ----------------------------------------------------------------------------------------
# ../Python/maths/polynomial_evaluation.py
# ----------------------------------------------------------------------------------------
from typing import Sequence # import_from:typing
def evaluate_poly(poly: Sequence[float], x: float) -> float: # function:evaluate_poly, function_returning_a_value:evaluate_poly, index
    return sum(c * (x ** i) for i, c in enumerate(poly)) # binary_operator:Mult, binary_operator:Pow, composition, comprehension:Generator, comprehension_for_count:1, function_call:enumerate, function_call:sum
def horner(poly: Sequence[float], x: float) -> float: # function:horner, function_returning_a_value:horner, index
    result = 0.0 # assignment, float_literal, literal:Num, suggest_constant_definition, variable_definition:result
    for coeff in reversed(poly): # accumulate_elements:Assign (-> +1), for (-> +1), function_call:reversed
        result = result * x + coeff # assignment, binary_operator:Add, binary_operator:Mult, variable_definition:result
    return result

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_check.py
# ----------------------------------------------------------------------------------------
import math # import:math
import unittest # import:unittest
def prime_check(number): # function:prime_check (-> +8), function_returning_a_value:prime_check (-> +8)
    if number < 2: # comparison_operator:Lt, if (-> +1), int_literal, literal:Num
        return False # if_then_branch, literal:False
    if number < 4: # comparison_operator:Lt, if (-> +1), int_literal, literal:Num, suggest_constant_definition
        return True # if_then_branch, literal:True
    if number % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), int_literal, literal:Num
        return False # if_then_branch, literal:False
    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2) # assignment, binary_operator:Add, composition, function_call:int, function_call:range, int_literal, literal:Num, method_call:sqrt, suggest_constant_definition, variable_definition:odd_numbers
    return not any(number % i == 0 for i in odd_numbers) # binary_operator:Mod, comparison_operator:Eq, comprehension:Generator, comprehension_for_count:1, divisibility_test, function_call:any, int_literal, literal:Num, unary_operator:Not
class Test(unittest.TestCase):
    def test_primes(self): # function:test_primes (-> +10), procedure:test_primes (-> +10)
        self.assertTrue(prime_check(2)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue
        self.assertTrue(prime_check(3)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(5)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(7)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(11)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(13)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(17)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(19)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(23)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(29)) # composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, suggest_constant_definition
    def test_not_primes(self): # function:test_not_primes (-> +12), procedure:test_not_primes (-> +12)
        self.assertFalse(prime_check(-19), "Negative numbers are not prime.") # composition, function_call:prime_check, int_literal, literal:Num, literal:Str, method_call:assertFalse, suggest_constant_definition
        self.assertFalse( # composition, method_call:assertFalse
            prime_check(0), "Zero doesn't have any divider, primes must have two" # function_call:prime_check, int_literal, literal:Num, literal:Str
        )
        self.assertFalse( # composition, method_call:assertFalse
            prime_check(1), "One just have 1 divider, primes must have two." # function_call:prime_check, int_literal, literal:Num, literal:Str
        )
        self.assertFalse(prime_check(2 * 2)) # binary_operator:Mult, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse
        self.assertFalse(prime_check(2 * 3)) # binary_operator:Mult, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse, suggest_constant_definition
        self.assertFalse(prime_check(3 * 3)) # binary_operator:Mult, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5)) # binary_operator:Mult, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5 * 7)) # binary_operator:Mult, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_factors.py
# ----------------------------------------------------------------------------------------
from typing import List # import_from:typing
def prime_factors(n: int) -> List[int]: # function:prime_factors, function_returning_a_value:prime_factors, index
    i = 2 # assignment, int_literal, literal:Num, variable_definition:i
    factors = [] # assignment, literal:List, variable_definition:factors
    while i * i <= n: # binary_operator:Mult, comparison_operator:LtE, evolve_state (-> +5), while (-> +5)
        if n % i: # binary_operator:Mod, if (-> +4)
            i += 1 # augmented_assignment, if_then_branch, int_literal, literal:Num
        else:
            n //= i # augmented_assignment, if_else_branch (-> +1)
            factors.append(i) # method_call:append
    if n > 1: # comparison_operator:Gt, if (-> +1), int_literal, literal:Num
        factors.append(n) # if_then_branch, method_call:append
    return factors

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_numbers.py
# ----------------------------------------------------------------------------------------
from typing import List # import_from:typing
def primes(max: int) -> List[int]: # function:primes, function_returning_a_value:primes, index
    max += 1 # augmented_assignment, int_literal, literal:Num
    numbers = [False] * max # assignment, binary_operator:Mult, literal:False, literal:List, variable_definition:numbers
    ret = [] # assignment, literal:List, variable_definition:ret
    for i in range(2, max): # accumulate_elements:Attribute (-> +4), for (-> +4), for_range_start (-> +4), function_call:range, int_literal, literal:Num
        if not numbers[i]: # if (-> +3), index, unary_operator:Not
            for j in range(i, max, i): # for (-> +1), for_range_step (-> +1), function_call:range, if_then_branch (-> +2), nested_for:2 (-> +1)
                numbers[j] = True # assignment, index, literal:True
            ret.append(i) # method_call:append
    return ret

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_sieve_eratosthenes.py
# ----------------------------------------------------------------------------------------
def prime_sieve_eratosthenes(num): # function:prime_sieve_eratosthenes (-> +10), procedure:prime_sieve_eratosthenes (-> +10)
    primes = [True for i in range(num + 1)] # assignment, binary_operator:Add, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num, literal:True, variable_definition:primes
    p = 2 # assignment, int_literal, literal:Num, variable_definition:p
    while p * p <= num: # binary_operator:Mult, comparison_operator:LtE, while (-> +4)
        if primes[p] == True: # comparison_operator:Eq, if (-> +2), index, literal:True
            for i in range(p * p, num + 1, p): # binary_operator:Add, binary_operator:Mult, for (-> +1), for_range_step (-> +1), function_call:range, if_then_branch (-> +1), int_literal, literal:Num
                primes[i] = False # assignment, index, literal:False
        p += 1 # augmented_assignment, int_literal, literal:Num
    for prime in range(2, num + 1): # binary_operator:Add, for (-> +2), for_range_start (-> +2), function_call:range, int_literal, literal:Num
        if primes[prime]: # if (-> +1), index
            print(prime, end=" ") # function_call:print, if_then_branch, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/qr_decomposition.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy
def qr_householder(A): # function:qr_householder (-> +16), function_returning_a_value:qr_householder (-> +16)
    m, n = A.shape # assignment, variable_definition:m, variable_definition:n
    t = min(m, n) # assignment, function_call:min, variable_definition:t
    Q = np.eye(m) # assignment, method_call:eye, variable_definition:Q
    R = A.copy() # assignment, method_call:copy, variable_definition:R
    for k in range(t - 1): # accumulate_elements:Assign (-> +10), binary_operator:Sub, for (-> +10), for_range_stop (-> +10), function_call:range, int_literal, literal:Num
        x = R[k:, [k]] # assignment, variable_definition:x
        e1 = np.zeros_like(x) # assignment, method_call:zeros_like, variable_definition:e1
        e1[0] = 1.0 # assignment, float_literal, index, int_literal, literal:Num, suggest_constant_definition
        alpha = np.linalg.norm(x) # assignment, method_call:norm, variable_definition:alpha
        v = x + np.sign(x[0]) * alpha * e1 # assignment, binary_operator:Add, binary_operator:Mult, index, int_literal, literal:Num, method_call:sign, variable_definition:v
        v /= np.linalg.norm(v) # augmented_assignment, method_call:norm
        Q_k = np.eye(m - k) - 2.0 * v @ v.T # assignment, binary_operator:MatMult, binary_operator:Mult, binary_operator:Sub, float_literal, literal:Num, method_call:eye, suggest_constant_definition, variable_definition:Q_k
        Q_k = np.block([[np.eye(k), np.zeros((k, m - k))], [np.zeros((m - k, k)), Q_k]]) # assignment, binary_operator:Sub, composition, method_call:block, method_call:eye, method_call:zeros, variable_definition:Q_k
        Q = Q @ Q_k.T # assignment, binary_operator:MatMult, suggest_augmented_assignment, variable_definition:Q
        R = Q_k @ R # assignment, binary_operator:MatMult, variable_definition:R
    return Q, R

# ----------------------------------------------------------------------------------------
# ../Python/maths/quadratic_equations_complex_numbers.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import_from:math
from typing import Tuple # import_from:typing
def QuadraticEquation(a: int, b: int, c: int) -> Tuple[str, str]: # function:QuadraticEquation, function_returning_a_value:QuadraticEquation, index
    if a == 0: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
        raise ValueError("Coefficient 'a' must not be zero for quadratic equations.") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    delta = b * b - 4 * a * c # assignment, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, suggest_constant_definition, variable_definition:delta
    if delta >= 0: # comparison_operator:GtE, if (-> +1), int_literal, literal:Num
        return str((-b + sqrt(delta)) / (2 * a)), str((-b - sqrt(delta)) / (2 * a)) # binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, composition, function_call:sqrt, function_call:str, if_then_branch, int_literal, literal:Num, unary_operator:USub
    snd = sqrt(-delta) # assignment, function_call:sqrt, unary_operator:USub, variable_definition:snd
    if b == 0: # comparison_operator:Eq, if (-> +1), int_literal, literal:Num
        return f"({snd} * i) / 2", f"({snd} * i) / {2 * a}" # binary_operator:Mult, if_then_branch, int_literal, literal:Num, literal:Str
    b = -abs(b) # assignment, function_call:abs, unary_operator:USub, variable_definition:b
    return f"({b}+{snd} * i) / 2", f"({b}+{snd} * i) / {2 * a}" # binary_operator:Mult, int_literal, literal:Num, literal:Str
def main(): # function:main (-> +2), procedure:main (-> +2)
    solutions = QuadraticEquation(a=5, b=6, c=1) # assignment, function_call:QuadraticEquation, int_literal, literal:Num, suggest_constant_definition, variable_definition:solutions
    print("The equation solutions are: {} and {}".format(*solutions)) # composition, function_call:print, literal:Str, method_call:format

# ----------------------------------------------------------------------------------------
# ../Python/maths/radix2_fft.py
# ----------------------------------------------------------------------------------------
import mpmath # import:mpmath
import numpy as np # import:numpy
class FFT:
    def __init__(self, polyA=[0], polyB=[0]): # function:__init__ (-> +17), function_with_default_positional_arguments:__init__ (-> +17), int_literal, literal:List, literal:Num, procedure:__init__ (-> +17)
        self.polyA = list(polyA)[:] # assignment, function_call:list, slice
        self.polyB = list(polyB)[:] # assignment, function_call:list, slice
        while self.polyA[-1] == 0: # comparison_operator:Eq, evolve_state (-> +1), index, int_literal, literal:Num, negative_index:-1, while (-> +1)
            self.polyA.pop() # method_call:pop
        self.len_A = len(self.polyA) # assignment, function_call:len
        while self.polyB[-1] == 0: # comparison_operator:Eq, evolve_state (-> +1), index, int_literal, literal:Num, negative_index:-1, while (-> +1)
            self.polyB.pop() # method_call:pop
        self.len_B = len(self.polyB) # assignment, function_call:len
        self.C_max_length = int( # assignment, composition, function_call:int
            2 ** np.ceil(np.log2(len(self.polyA) + len(self.polyB) - 1)) # binary_operator:Add, binary_operator:Pow, binary_operator:Sub, composition, function_call:len, int_literal, literal:Num, method_call:ceil, method_call:log2
        )
        while len(self.polyA) < self.C_max_length: # comparison_operator:Lt, evolve_state (-> +1), function_call:len, while (-> +1)
            self.polyA.append(0) # int_literal, literal:Num, method_call:append
        while len(self.polyB) < self.C_max_length: # comparison_operator:Lt, evolve_state (-> +1), function_call:len, while (-> +1)
            self.polyB.append(0) # int_literal, literal:Num, method_call:append
        self.root = complex(mpmath.root(x=1, n=self.C_max_length, k=1)) # assignment, composition, function_call:complex, int_literal, literal:Num, method_call:root
        self.product = self.__multiply() # assignment, method_call:__multiply
    def __DFT(self, which): # function:__DFT (-> +23), function_returning_a_value:__DFT (-> +23)
        if which == "A": # comparison_operator:Eq, if (-> +3), literal:Str, suggest_conditional_expression (-> +3)
            dft = [[x] for x in self.polyA] # assignment, comprehension:List, comprehension_for_count:1, if_then_branch, variable_definition:dft
        else:
            dft = [[x] for x in self.polyB] # assignment, comprehension:List, comprehension_for_count:1, if_else_branch, variable_definition:dft
        if len(dft) <= 1: # comparison_operator:LtE, function_call:len, if (-> +1), int_literal, literal:Num
            return dft[0] # if_then_branch, index, int_literal, literal:Num
        next_ncol = self.C_max_length // 2 # assignment, binary_operator:FloorDiv, int_literal, literal:Num, variable_definition:next_ncol
        while next_ncol > 0: # comparison_operator:Gt, evolve_state (-> +14), int_literal, literal:Num, while (-> +14)
            new_dft = [[] for i in range(next_ncol)] # assignment, comprehension:List, comprehension_for_count:1, function_call:range, literal:List, variable_definition:new_dft
            root = self.root ** next_ncol # assignment, binary_operator:Pow, variable_definition:root
            current_root = 1 # assignment, int_literal, literal:Num, variable_definition:current_root
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator:FloorDiv, binary_operator:Mult, for (-> +3), for_range_stop (-> +3), function_call:range, int_literal, literal:Num
                for i in range(next_ncol): # for (-> +1), for_range_stop (-> +1), function_call:range, nested_for:2 (-> +1)
                    new_dft[i].append(dft[i][j] + current_root * dft[i + next_ncol][j]) # binary_operator:Add, binary_operator:Mult, index, index_arithmetic, method_call:append
                current_root *= root # augmented_assignment
            current_root = 1 # assignment, int_literal, literal:Num, variable_definition:current_root
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator:FloorDiv, binary_operator:Mult, for (-> +3), for_range_stop (-> +3), function_call:range, int_literal, literal:Num
                for i in range(next_ncol): # for (-> +1), for_range_stop (-> +1), function_call:range, nested_for:2 (-> +1)
                    new_dft[i].append(dft[i][j] - current_root * dft[i + next_ncol][j]) # binary_operator:Add, binary_operator:Mult, binary_operator:Sub, index, index_arithmetic, method_call:append
                current_root *= root # augmented_assignment
            dft = new_dft # assignment, variable_definition:dft
            next_ncol = next_ncol // 2 # assignment, binary_operator:FloorDiv, int_literal, literal:Num, suggest_augmented_assignment, variable_definition:next_ncol
        return dft[0] # index, int_literal, literal:Num
    def __multiply(self): # function:__multiply (-> +35), function_returning_a_value:__multiply (-> +35)
        dftA = self.__DFT("A") # assignment, literal:Str, method_call:__DFT, variable_definition:dftA
        dftB = self.__DFT("B") # assignment, literal:Str, method_call:__DFT, variable_definition:dftB
        inverseC = [[dftA[i] * dftB[i] for i in range(self.C_max_length)]] # assignment, binary_operator:Mult, comprehension:List, comprehension_for_count:1, function_call:range, index, variable_definition:inverseC
        del dftA # variable_definition:dftA
        del dftB # variable_definition:dftB
        if len(inverseC[0]) <= 1: # comparison_operator:LtE, function_call:len, if (-> +1), index, int_literal, literal:Num
            return inverseC[0] # if_then_branch, index, int_literal, literal:Num
        next_ncol = 2 # assignment, int_literal, literal:Num, variable_definition:next_ncol
        while next_ncol <= self.C_max_length: # comparison_operator:LtE, evolve_state (-> +22), while (-> +22)
            new_inverseC = [[] for i in range(next_ncol)] # assignment, comprehension:List, comprehension_for_count:1, function_call:range, literal:List, variable_definition:new_inverseC
            root = self.root ** (next_ncol // 2) # assignment, binary_operator:FloorDiv, binary_operator:Pow, int_literal, literal:Num, variable_definition:root
            current_root = 1 # assignment, int_literal, literal:Num, variable_definition:current_root
            for j in range(self.C_max_length // next_ncol): # binary_operator:FloorDiv, for (-> +16), for_range_stop (-> +16), function_call:range
                for i in range(next_ncol // 2): # binary_operator:FloorDiv, for (-> +13), for_range_stop (-> +13), function_call:range, int_literal, literal:Num, nested_for:2 (-> +13)
                    new_inverseC[i].append( # index, method_call:append
                        ( # binary_operator:Div
                            inverseC[i][j] # binary_operator:Add, index
                            + inverseC[i][j + self.C_max_length // next_ncol] # binary_operator:Add, binary_operator:FloorDiv, index, index_arithmetic
                        )
                        / 2 # int_literal, literal:Num
                    )
                    new_inverseC[i + next_ncol // 2].append( # binary_operator:Add, binary_operator:FloorDiv, index, index_arithmetic, int_literal, literal:Num, method_call:append
                        ( # binary_operator:Div
                            inverseC[i][j] # binary_operator:Sub, index
                            - inverseC[i][j + self.C_max_length // next_ncol] # binary_operator:Add, binary_operator:FloorDiv, index, index_arithmetic
                        )
                        / (2 * current_root) # binary_operator:Mult, int_literal, literal:Num
                    )
                current_root *= root # augmented_assignment
            inverseC = new_inverseC # assignment, variable_definition:inverseC
            next_ncol *= 2 # augmented_assignment, int_literal, literal:Num
        inverseC = [round(x[0].real, 8) + round(x[0].imag, 8) * 1j for x in inverseC] # assignment, binary_operator:Add, binary_operator:Mult, comprehension:List, comprehension_for_count:1, function_call:round, imaginary_literal, index, int_literal, literal:Num, suggest_constant_definition, variable_definition:inverseC
        while inverseC[-1] == 0: # comparison_operator:Eq, evolve_state (-> +1), index, int_literal, literal:Num, negative_index:-1, while (-> +1)
            inverseC.pop() # method_call:pop
        return inverseC
    def __str__(self): # function:__str__ (-> +10), function_returning_a_value:__str__ (-> +10)
        A = "A = " + " + ".join( # assignment, binary_operator:Add, composition, literal:Str, method_call:join, variable_definition:A
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyA[: self.len_A]) # comprehension:Generator, comprehension_for_count:1, function_call:enumerate, literal:Str, slice
        )
        B = "B = " + " + ".join( # assignment, binary_operator:Add, composition, literal:Str, method_call:join, variable_definition:B
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyB[: self.len_B]) # comprehension:Generator, comprehension_for_count:1, function_call:enumerate, literal:Str, slice
        )
        C = "A*B = " + " + ".join( # assignment, binary_operator:Add, composition, literal:Str, method_call:join, variable_definition:C
            f"{coef}*x^{i}" for coef, i in enumerate(self.product) # comprehension:Generator, comprehension_for_count:1, function_call:enumerate, literal:Str
        )
        return "\n".join((A, B, C)) # literal:Str, method_call:join

# ----------------------------------------------------------------------------------------
# ../Python/maths/runge_kutta.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy
def runge_kutta(f, y0, x0, h, x_end): # function:runge_kutta (-> +12), function_returning_a_value:runge_kutta (-> +12)
    N = int(np.ceil((x_end - x0) / h)) # assignment, binary_operator:Div, binary_operator:Sub, composition, function_call:int, method_call:ceil, variable_definition:N
    y = np.zeros((N + 1,)) # assignment, binary_operator:Add, int_literal, literal:Num, method_call:zeros, variable_definition:y
    y[0] = y0 # assignment, index, int_literal, literal:Num
    x = x0 # assignment, variable_definition:x
    for k in range(N): # accumulate_elements:Assign (-> +6), for (-> +6), for_range_stop (-> +6), function_call:range
        k1 = f(x, y[k]) # assignment, function_call:f, index, variable_definition:k1
        k2 = f(x + 0.5 * h, y[k] + 0.5 * h * k1) # assignment, binary_operator:Add, binary_operator:Mult, float_literal, function_call:f, index, literal:Num, suggest_constant_definition, variable_definition:k2
        k3 = f(x + 0.5 * h, y[k] + 0.5 * h * k2) # assignment, binary_operator:Add, binary_operator:Mult, float_literal, function_call:f, index, literal:Num, suggest_constant_definition, variable_definition:k3
        k4 = f(x + h, y[k] + h * k3) # assignment, binary_operator:Add, binary_operator:Mult, function_call:f, index, variable_definition:k4
        y[k + 1] = y[k] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4) # assignment, binary_operator:Add, binary_operator:Div, binary_operator:Mult, index, index_arithmetic, int_literal, literal:Num, suggest_constant_definition
        x += h # augmented_assignment
    return y

# ----------------------------------------------------------------------------------------
# ../Python/maths/segmented_sieve.py
# ----------------------------------------------------------------------------------------
import math # import:math
def sieve(n): # function:sieve (-> +33), function_returning_a_value:sieve (-> +33)
    in_prime = [] # assignment, literal:List, variable_definition:in_prime
    start = 2 # assignment, int_literal, literal:Num, variable_definition:start
    end = int(math.sqrt(n)) # assignment, composition, function_call:int, method_call:sqrt, variable_definition:end
    temp = [True] * (end + 1) # assignment, binary_operator:Add, binary_operator:Mult, int_literal, literal:List, literal:Num, literal:True, variable_definition:temp
    prime = [] # assignment, literal:List, variable_definition:prime
    while start <= end: # comparison_operator:LtE, while (-> +6)
        if temp[start] is True: # comparison_operator:Is, if (-> +4), index, literal:True
            in_prime.append(start) # if_then_branch (-> +3), method_call:append
            for i in range(start * start, end + 1, start): # binary_operator:Add, binary_operator:Mult, for (-> +2), for_range_step (-> +2), function_call:range, int_literal, literal:Num
                if temp[i] is True: # comparison_operator:Is, if (-> +1), index, literal:True, nested_if:2 (-> +1)
                    temp[i] = False # assignment, if_then_branch, index, literal:False
        start += 1 # augmented_assignment, int_literal, literal:Num
    prime += in_prime # augmented_assignment
    low = end + 1 # assignment, binary_operator:Add, int_literal, literal:Num, variable_definition:low
    high = low + end - 1 # assignment, binary_operator:Add, binary_operator:Sub, int_literal, literal:Num, variable_definition:high
    if high > n: # comparison_operator:Gt, if (-> +1)
        high = n # assignment, if_then_branch, variable_definition:high
    while low <= n: # comparison_operator:LtE, while (-> +14)
        temp = [True] * (high - low + 1) # assignment, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, int_literal, literal:List, literal:Num, literal:True, variable_definition:temp
        for each in in_prime: # accumulate_elements:AugAssign (-> +5), for (-> +5), for_each (-> +5)
            t = math.floor(low / each) * each # assignment, binary_operator:Div, binary_operator:Mult, method_call:floor, variable_definition:t
            if t < low: # comparison_operator:Lt, if (-> +1)
                t += each # augmented_assignment, if_then_branch
            for j in range(t, high + 1, each): # binary_operator:Add, for (-> +1), for_range_step (-> +1), function_call:range, int_literal, literal:Num, nested_for:2 (-> +1)
                temp[j - low] = False # assignment, binary_operator:Sub, index, index_arithmetic, literal:False
        for j in range(len(temp)): # composition, for (-> +2), for_indexes (-> +2), for_range_stop (-> +2), function_call:len, function_call:range
            if temp[j] is True: # comparison_operator:Is, if (-> +1), index, literal:True
                prime.append(j + low) # binary_operator:Add, if_then_branch, method_call:append
        low = high + 1 # assignment, binary_operator:Add, int_literal, literal:Num, variable_definition:low
        high = low + end - 1 # assignment, binary_operator:Add, binary_operator:Sub, int_literal, literal:Num, variable_definition:high
        if high > n: # comparison_operator:Gt, if (-> +1)
            high = n # assignment, if_then_branch, variable_definition:high
    return prime
print(sieve(10 ** 6)) # binary_operator:Pow, composition, function_call:print, function_call:sieve, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/sieve_of_eratosthenes.py
# ----------------------------------------------------------------------------------------
"""
Sieve of Eratosthones
The sieve of Eratosthenes is an algorithm used to find prime numbers, less than or equal to a given value.
Illustration: https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
doctest provider: Bruno Simas Hadlich (https://github.com/brunohadlich)
Also thanks Dmitry (https://github.com/LizardWizzard) for finding the problem
""" # literal:Str
import math # import:math
def sieve(n): # function:sieve (-> +15), function_returning_a_value:sieve (-> +15)
    l = [True] * (n + 1) # assignment, binary_operator:Add, binary_operator:Mult, int_literal, literal:List, literal:Num, literal:True, variable_definition:l
    prime = [] # assignment, literal:List, variable_definition:prime
    start = 2 # assignment, int_literal, literal:Num, variable_definition:start
    end = int(math.sqrt(n)) # assignment, composition, function_call:int, method_call:sqrt, variable_definition:end
    while start <= end: # comparison_operator:LtE, while (-> +6)
        if l[start] is True: # comparison_operator:Is, if (-> +4), index, literal:True
            prime.append(start) # if_then_branch (-> +3), method_call:append
            for i in range(start * start, n + 1, start): # binary_operator:Add, binary_operator:Mult, for (-> +2), for_range_step (-> +2), function_call:range, int_literal, literal:Num
                if l[i] is True: # comparison_operator:Is, if (-> +1), index, literal:True, nested_if:2 (-> +1)
                    l[i] = False # assignment, if_then_branch, index, literal:False
        start += 1 # augmented_assignment, int_literal, literal:Num
    for j in range(end + 1, n + 1): # accumulate_elements:Attribute (-> +2), binary_operator:Add, for (-> +2), for_range_start (-> +2), function_call:range, int_literal, literal:Num
        if l[j] is True: # comparison_operator:Is, if (-> +1), index, literal:True
            prime.append(j) # if_then_branch, method_call:append
    return prime

# ----------------------------------------------------------------------------------------
# ../Python/maths/simpson_rule.py
# ----------------------------------------------------------------------------------------
def method_2(boundary, steps): # function:method_2 (-> +12), function_returning_a_value:method_2 (-> +12)
    h = (boundary[1] - boundary[0]) / steps # assignment, binary_operator:Div, binary_operator:Sub, index, int_literal, literal:Num, variable_definition:h
    a = boundary[0] # assignment, index, int_literal, literal:Num, variable_definition:a
    b = boundary[1] # assignment, index, int_literal, literal:Num, variable_definition:b
    x_i = make_points(a, b, h) # assignment, function_call:make_points, variable_definition:x_i
    y = 0.0 # assignment, float_literal, literal:Num, suggest_constant_definition, variable_definition:y
    y += (h / 3.0) * f(a) # augmented_assignment, binary_operator:Div, binary_operator:Mult, float_literal, function_call:f, literal:Num, suggest_constant_definition
    cnt = 2 # assignment, int_literal, literal:Num, variable_definition:cnt
    for i in x_i: # accumulate_elements:AugAssign (-> +2), for (-> +2), for_each (-> +2)
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i) # augmented_assignment, binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, function_call:f, int_literal, literal:Num, suggest_constant_definition
        cnt += 1 # augmented_assignment, int_literal, literal:Num
    y += (h / 3.0) * f(b) # augmented_assignment, binary_operator:Div, binary_operator:Mult, float_literal, function_call:f, literal:Num, suggest_constant_definition
    return y
def make_points(a, b, h): # function:make_points (-> +4), generator:make_points (-> +4), procedure:make_points (-> +4)
    x = a + h # assignment, binary_operator:Add, variable_definition:x
    while x < (b - h): # binary_operator:Sub, comparison_operator:Lt, while (-> +2)
        yield x
        x = x + h # assignment, binary_operator:Add, suggest_augmented_assignment, variable_definition:x
def f(x): # function:f (-> +2), function_returning_a_value:f (-> +2)
    y = (x - 0) * (x - 0) # assignment, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, variable_definition:y
    return y
def main(): # function:main (-> +6), procedure:main (-> +6)
    a = 0.0 # assignment, float_literal, literal:Num, suggest_constant_definition, variable_definition:a
    b = 1.0 # assignment, float_literal, literal:Num, suggest_constant_definition, variable_definition:b
    steps = 10.0 # assignment, float_literal, literal:Num, suggest_constant_definition, variable_definition:steps
    boundary = [a, b] # assignment, variable_definition:boundary
    y = method_2(boundary, steps) # assignment, function_call:method_2, variable_definition:y
    print("y = {0}".format(y)) # composition, function_call:print, literal:Str, method_call:format

# ----------------------------------------------------------------------------------------
# ../Python/maths/softmax.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy
def softmax(vector): # function:softmax (-> +4), function_returning_a_value:softmax (-> +4)
    exponentVector = np.exp(vector) # assignment, method_call:exp, variable_definition:exponentVector
    sumOfExponents = np.sum(exponentVector) # assignment, method_call:sum, variable_definition:sumOfExponents
    softmax_vector = exponentVector / sumOfExponents # assignment, binary_operator:Div, variable_definition:softmax_vector
    return softmax_vector

# ----------------------------------------------------------------------------------------
# ../Python/maths/sum_of_arithmetic_series.py
# ----------------------------------------------------------------------------------------
def sum_of_series(first_term, common_diff, num_of_terms): # function:sum_of_series (-> +2), function_returning_a_value:sum_of_series (-> +2)
    sum = (num_of_terms / 2) * (2 * first_term + (num_of_terms - 1) * common_diff) # assignment, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, variable_definition:sum
    return sum
def main(): # function:main (-> +1), procedure:main (-> +1)
    print(sum_of_series(1, 1, 10)) # composition, function_call:print, function_call:sum_of_series, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/test_prime_check.py
# ----------------------------------------------------------------------------------------
from .prime_check import Test # import_from:prime_check
Test() # function_call:Test

# ----------------------------------------------------------------------------------------
# ../Python/maths/trapezoidal_rule.py
# ----------------------------------------------------------------------------------------
def method_1(boundary, steps): # function:method_1 (-> +10), function_returning_a_value:method_1 (-> +10)
    h = (boundary[1] - boundary[0]) / steps # assignment, binary_operator:Div, binary_operator:Sub, index, int_literal, literal:Num, variable_definition:h
    a = boundary[0] # assignment, index, int_literal, literal:Num, variable_definition:a
    b = boundary[1] # assignment, index, int_literal, literal:Num, variable_definition:b
    x_i = make_points(a, b, h) # assignment, function_call:make_points, variable_definition:x_i
    y = 0.0 # assignment, float_literal, literal:Num, suggest_constant_definition, variable_definition:y
    y += (h / 2.0) * f(a) # augmented_assignment, binary_operator:Div, binary_operator:Mult, float_literal, function_call:f, literal:Num, suggest_constant_definition
    for i in x_i: # accumulate_elements:AugAssign (-> +1), for (-> +1), for_each (-> +1)
        y += h * f(i) # augmented_assignment, binary_operator:Mult, function_call:f
    y += (h / 2.0) * f(b) # augmented_assignment, binary_operator:Div, binary_operator:Mult, float_literal, function_call:f, literal:Num, suggest_constant_definition
    return y
def make_points(a, b, h): # function:make_points (-> +4), generator:make_points (-> +4), procedure:make_points (-> +4)
    x = a + h # assignment, binary_operator:Add, variable_definition:x
    while x < (b - h): # binary_operator:Sub, comparison_operator:Lt, while (-> +2)
        yield x
        x = x + h # assignment, binary_operator:Add, suggest_augmented_assignment, variable_definition:x
def f(x): # function:f (-> +2), function_returning_a_value:f (-> +2)
    y = (x - 0) * (x - 0) # assignment, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, variable_definition:y
    return y
def main(): # function:main (-> +6), procedure:main (-> +6)
    a = 0.0 # assignment, float_literal, literal:Num, suggest_constant_definition, variable_definition:a
    b = 1.0 # assignment, float_literal, literal:Num, suggest_constant_definition, variable_definition:b
    steps = 10.0 # assignment, float_literal, literal:Num, suggest_constant_definition, variable_definition:steps
    boundary = [a, b] # assignment, variable_definition:boundary
    y = method_1(boundary, steps) # assignment, function_call:method_1, variable_definition:y
    print("y = {0}".format(y)) # composition, function_call:print, literal:Str, method_call:format

# ----------------------------------------------------------------------------------------
# ../Python/maths/volume.py
# ----------------------------------------------------------------------------------------
from math import pi # import_from:math
def vol_cube(side_length): # function:vol_cube (-> +1), function_returning_a_value:vol_cube (-> +1)
    return float(side_length ** 3) # binary_operator:Pow, function_call:float, int_literal, literal:Num, suggest_constant_definition
def vol_cuboid(width, height, length): # function:vol_cuboid (-> +1), function_returning_a_value:vol_cuboid (-> +1)
    return float(width * height * length) # binary_operator:Mult, function_call:float
def vol_cone(area_of_base, height): # function:vol_cone (-> +1), function_returning_a_value:vol_cone (-> +1)
    return (float(1) / 3) * area_of_base * height # binary_operator:Div, binary_operator:Mult, function_call:float, int_literal, literal:Num, suggest_constant_definition
def vol_right_circ_cone(radius, height): # function:vol_right_circ_cone (-> +1), function_returning_a_value:vol_right_circ_cone (-> +1)
    return (float(1) / 3) * pi * (radius ** 2) * height # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, function_call:float, int_literal, literal:Num, suggest_constant_definition
def vol_prism(area_of_base, height): # function:vol_prism (-> +1), function_returning_a_value:vol_prism (-> +1)
    return float(area_of_base * height) # binary_operator:Mult, function_call:float
def vol_pyramid(area_of_base, height): # function:vol_pyramid (-> +1), function_returning_a_value:vol_pyramid (-> +1)
    return (float(1) / 3) * area_of_base * height # binary_operator:Div, binary_operator:Mult, function_call:float, int_literal, literal:Num, suggest_constant_definition
def vol_sphere(radius): # function:vol_sphere (-> +1), function_returning_a_value:vol_sphere (-> +1)
    return (float(4) / 3) * pi * radius ** 3 # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, function_call:float, int_literal, literal:Num, suggest_constant_definition
def vol_circular_cylinder(radius, height): # function:vol_circular_cylinder (-> +1), function_returning_a_value:vol_circular_cylinder (-> +1)
    return pi * radius ** 2 * height # binary_operator:Mult, binary_operator:Pow, int_literal, literal:Num
def main(): # function:main (-> +9), procedure:main (-> +9)
    print("Volumes:") # function_call:print, literal:Str
    print("Cube: " + str(vol_cube(2))) # binary_operator:Add, composition, function_call:print, function_call:str, function_call:vol_cube, int_literal, literal:Num, literal:Str
    print("Cuboid: " + str(vol_cuboid(2, 2, 2))) # binary_operator:Add, composition, function_call:print, function_call:str, function_call:vol_cuboid, int_literal, literal:Num, literal:Str
    print("Cone: " + str(vol_cone(2, 2))) # binary_operator:Add, composition, function_call:print, function_call:str, function_call:vol_cone, int_literal, literal:Num, literal:Str
    print("Right Circular Cone: " + str(vol_right_circ_cone(2, 2))) # binary_operator:Add, composition, function_call:print, function_call:str, function_call:vol_right_circ_cone, int_literal, literal:Num, literal:Str
    print("Prism: " + str(vol_prism(2, 2))) # binary_operator:Add, composition, function_call:print, function_call:str, function_call:vol_prism, int_literal, literal:Num, literal:Str
    print("Pyramid: " + str(vol_pyramid(2, 2))) # binary_operator:Add, composition, function_call:print, function_call:str, function_call:vol_pyramid, int_literal, literal:Num, literal:Str
    print("Sphere: " + str(vol_sphere(2))) # binary_operator:Add, composition, function_call:print, function_call:str, function_call:vol_sphere, int_literal, literal:Num, literal:Str
    print("Circular Cylinder: " + str(vol_circular_cylinder(2, 2))) # binary_operator:Add, composition, function_call:print, function_call:str, function_call:vol_circular_cylinder, int_literal, literal:Num, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/zellers_congruence.py
# ----------------------------------------------------------------------------------------
import datetime # import:datetime
import argparse # import:argparse
def zeller(date_input: str) -> str: # function:zeller, function_returning_a_value:zeller
    days = { # assignment, literal:Dict, variable_definition:days
        "0": "Sunday", # literal:Str
        "1": "Monday", # literal:Str
        "2": "Tuesday", # literal:Str
        "3": "Wednesday", # literal:Str
        "4": "Thursday", # literal:Str
        "5": "Friday", # literal:Str
        "6": "Saturday", # literal:Str
    }
    convert_datetime_days = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0} # assignment, int_literal, literal:Dict, literal:Num, suggest_constant_definition, variable_definition:convert_datetime_days
    if not 0 < len(date_input) < 11: # chained_comparison:2, comparison_operator:Lt, function_call:len, if (-> +1), int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError("Must be 10 characters long") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    m: int = int(date_input[0] + date_input[1]) # binary_operator:Add, function_call:int, index, int_literal, literal:Num
    if not 0 < m < 13: # chained_comparison:2, comparison_operator:Lt, if (-> +1), int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError("Month must be between 1 - 12") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    sep_1: str = date_input[2] # index, int_literal, literal:Num
    if sep_1 not in ["-", "/"]: # comparison_operator:NotIn, if (-> +1), literal:List, literal:Str
        raise ValueError("Date seperator must be '-' or '/'") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    d: int = int(date_input[3] + date_input[4]) # binary_operator:Add, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
    if not 0 < d < 32: # chained_comparison:2, comparison_operator:Lt, if (-> +1), int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError("Date must be between 1 - 31") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    sep_2: str = date_input[5] # index, int_literal, literal:Num, suggest_constant_definition
    if sep_2 not in ["-", "/"]: # comparison_operator:NotIn, if (-> +1), literal:List, literal:Str
        raise ValueError("Date seperator must be '-' or '/'") # function_call:ValueError, if_then_branch, literal:Str, raise_exception:ValueError
    y: int = int(date_input[6] + date_input[7] + date_input[8] + date_input[9]) # binary_operator:Add, function_call:int, index, int_literal, literal:Num, suggest_constant_definition
    if not 45 < y < 8500: # chained_comparison:2, comparison_operator:Lt, if (-> +2), int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError( # function_call:ValueError, if_then_branch (-> +1), raise_exception:ValueError
            "Year out of range. There has to be some sort of limit...right?" # literal:Str
        )
    dt_ck = datetime.date(int(y), int(m), int(d)) # assignment, composition, function_call:int, method_call:date, variable_definition:dt_ck
    if m <= 2: # comparison_operator:LtE, if (-> +2), int_literal, literal:Num
        y = y - 1 # assignment, binary_operator:Sub, if_then_branch (-> +1), int_literal, literal:Num, suggest_augmented_assignment, variable_definition:y
        m = m + 12 # assignment, binary_operator:Add, int_literal, literal:Num, suggest_augmented_assignment, suggest_constant_definition, variable_definition:m
    c: int = int(str(y)[:2]) # composition, function_call:int, function_call:str, int_literal, literal:Num, slice
    k: int = int(str(y)[2:]) # composition, function_call:int, function_call:str, int_literal, literal:Num, slice
    t: int = int(2.6 * m - 5.39) # binary_operator:Mult, binary_operator:Sub, float_literal, function_call:int, literal:Num, suggest_constant_definition
    u: int = int(c / 4) # binary_operator:Div, function_call:int, int_literal, literal:Num, suggest_constant_definition
    v: int = int(k / 4) # binary_operator:Div, function_call:int, int_literal, literal:Num, suggest_constant_definition
    x: int = int(d + k) # binary_operator:Add, function_call:int
    z: int = int(t + u + v + x) # binary_operator:Add, function_call:int
    w: int = int(z - (2 * c)) # binary_operator:Mult, binary_operator:Sub, function_call:int, int_literal, literal:Num
    f: int = round(w % 7) # binary_operator:Mod, function_call:round, int_literal, literal:Num, suggest_constant_definition
    if f != convert_datetime_days[dt_ck.weekday()]: # comparison_operator:NotEq, if (-> +1), index, method_call:weekday
        raise AssertionError("The date was evaluated incorrectly. Contact developer.") # function_call:AssertionError, if_then_branch, literal:Str, raise_exception:AssertionError
    response: str = f"Your date {date_input}, is a {days[str(f)]}!" # function_call:str, index, literal:Str
    return response
