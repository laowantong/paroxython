# ----------------------------------------------------------------------------------------
# ../Python/maths/3n+1.py
# ----------------------------------------------------------------------------------------
from typing import Tuple, List # import:typing:List, import:typing:Tuple, import_module:typing, import_name:List, import_name:Tuple, lines_of_code:128 (-> +127)
def n31(a: int) -> Tuple[List[int], int]: # function:n31 (-> +12), function_argument:a, function_argument_flavor:arg, function_returning_something:n31 (-> +12), index:_, index:int
    if not isinstance(a, int): # call_argument:a, call_argument:int, function_call:isinstance, if (-> +1), if_test_atom:a, if_test_atom:int, unary_operator:Not
        raise TypeError("Must be int, not {0}".format(type(a).__name__)) # call_argument:, call_argument:a, composition, function_call:TypeError, function_call:type, if_then_branch, literal:Str, method_call:format, raise:TypeError
    if a < 1: # comparison_operator:Lt, if (-> +1), if_test_atom:1, if_test_atom:a, int_literal, literal:Num
        raise ValueError("Given integer must be greater than 1, not {0}".format(a)) # call_argument:, call_argument:a, composition, function_call:ValueError, if_then_branch, literal:Str, method_call:format, raise:ValueError
    path = [a] # assignment, assignment_lhs_identifier:path, assignment_rhs_atom:a, single_assignment:path
    while a != 1: # comparison_operator:NotEq, evolve_state (-> +5), int_literal, literal:Num, loop:while (-> +5), while (-> +5)
        if a % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, falsey_literal:0, if (-> +3), if_test_atom:0, if_test_atom:2, if_test_atom:a, int_literal, literal:Num, suggest_conditional_expression (-> +3)
            a = a // 2 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:2, assignment_rhs_atom:a, binary_operator:FloorDiv, if_then_branch, int_literal, literal:Num, single_assignment:a, suggest_augmented_assignment, variable_update:a:2, variable_update_by_assignment:a:2
        else:
            a = 3 * a + 1 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:a, binary_operator:Add, binary_operator:Mult, if_else_branch, int_literal, literal:Num, single_assignment:a, suggest_constant_definition, variable_update:a:1, variable_update:a:3, variable_update_by_assignment:a:1, variable_update_by_assignment:a:3
        path += [a] # assignment_lhs_identifier:path, assignment_rhs_atom:a, augmented_assignment:Add, variable_update:path:a, variable_update_by_augmented_assignment:path:a
    return path, len(path) # call_argument:path, function_call:len, return
def test_n31(): # function:test_n31 (-> +113), function_returning_nothing:test_n31 (-> +113), function_without_arguments:test_n31 (-> +113)
    assert n31(4) == ([4, 2, 1], 3) # assertion, call_argument:4, comparison_operator:Eq, function_call:n31, int_literal, literal:List, literal:Num, literal:Tuple, suggest_constant_definition
    assert n31(11) == ([11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 15) # assertion, call_argument:11, comparison_operator:Eq, function_call:n31, int_literal, literal:List, literal:Num, literal:Tuple, suggest_constant_definition
    assert n31(31) == ( # assertion, call_argument:31, function_call:n31, int_literal, literal:Num, suggest_constant_definition
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
def abs_val(num): # function:abs_val (-> +1), function_argument:num, function_argument_flavor:arg, function_returning_something:abs_val (-> +1), lines_of_code:6 (-> +5)
    return -num if num < 0 else num # comparison_operator:Lt, conditional_expression, falsey_literal:0, int_literal, literal:Num, return, unary_operator:USub
def test_abs_val(): # function:test_abs_val (-> +3), function_returning_nothing:test_abs_val (-> +3), function_without_arguments:test_abs_val (-> +3)
    assert 0 == abs_val(0) # assertion, call_argument:0, comparison_operator:Eq, falsey_literal:0, function_call:abs_val, int_literal, literal:Num
    assert 34 == abs_val(34) # assertion, call_argument:34, comparison_operator:Eq, function_call:abs_val, int_literal, literal:Num, suggest_constant_definition
    assert 100000000000 == abs_val(-100000000000) # assertion, call_argument:-100000000000, comparison_operator:Eq, function_call:abs_val, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs_max.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List, lines_of_code:13 (-> +12)
def abs_max(x: List[int]) -> int: # function:abs_max (-> +5), function_argument:x, function_argument_flavor:arg, function_returning_something:abs_max (-> +5)
    j = x[0] # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:0, assignment_rhs_atom:x, falsey_literal:0, index:0, int_literal, literal:Num, single_assignment:j
    for i in x: # find_best_element:i:j (-> +2), for:i (-> +2), for_each (-> +2), loop:for (-> +2)
        if abs(i) > abs(j): # call_argument:i, call_argument:j, comparison_operator:Gt, function_call:abs, if (-> +1), if_test_atom:i, if_test_atom:j
            j = i # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:i, if_then_branch, single_assignment:j
    return j # return:j
def abs_max_sort(x): # function:abs_max_sort (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:abs_max_sort (-> +1)
    return sorted(x, key=abs)[-1] # call_argument:x, function_call:sorted, index:-1, int_literal, literal:Num, negative_index:-1, return
def main(): # function:main (-> +3), function_returning_nothing:main (-> +3), function_without_arguments:main (-> +3)
    a = [1, 2, -11] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:-11, assignment_rhs_atom:1, assignment_rhs_atom:2, int_literal, literal:List, literal:Num, single_assignment:a, suggest_constant_definition
    assert abs_max(a) == -11 # assertion, call_argument:a, comparison_operator:Eq, function_call:abs_max, int_literal, literal:Num, suggest_constant_definition
    assert abs_max_sort(a) == -11 # assertion, call_argument:a, comparison_operator:Eq, function_call:abs_max_sort, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/abs_min.py
# ----------------------------------------------------------------------------------------
from .abs import abs_val # import:abs:abs_val, import_module:abs, import_name:abs_val, lines_of_code:10 (-> +9)
def absMin(x): # function:absMin (-> +5), function_argument:x, function_argument_flavor:arg, function_returning_something:absMin (-> +5)
    j = x[0] # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:0, assignment_rhs_atom:x, falsey_literal:0, index:0, int_literal, literal:Num, single_assignment:j
    for i in x: # find_best_element:i:j (-> +2), for:i (-> +2), for_each (-> +2), loop:for (-> +2)
        if abs_val(i) < abs_val(j): # call_argument:i, call_argument:j, comparison_operator:Lt, function_call:abs_val, if (-> +1), if_test_atom:i, if_test_atom:j
            j = i # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:i, if_then_branch, single_assignment:j
    return j # return:j
def main(): # function:main (-> +2), function_returning_nothing:main (-> +2), function_without_arguments:main (-> +2)
    a = [-3, -1, 2, -11] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:-1, assignment_rhs_atom:-11, assignment_rhs_atom:-3, assignment_rhs_atom:2, int_literal, literal:List, literal:Num, single_assignment:a, suggest_constant_definition
    print(absMin(a)) # call_argument:, call_argument:a, composition, function_call:absMin, function_call:print

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_mean.py
# ----------------------------------------------------------------------------------------
def average(nums): # function:average (-> +1), function_argument:nums, function_argument_flavor:arg, function_returning_something:average (-> +1), lines_of_code:6 (-> +5)
    return sum(nums) / len(nums) # binary_operator:Div, call_argument:nums, function_call:len, function_call:sum, return
def test_average(): # function:test_average (-> +3), function_returning_nothing:test_average (-> +3), function_without_arguments:test_average (-> +3)
    assert 12.0 == average([3, 6, 9, 12, 15, 18, 21]) # assertion, call_argument:, comparison_operator:Eq, float_literal, function_call:average, int_literal, literal:List, literal:Num, suggest_constant_definition
    assert 20 == average([5, 10, 15, 20, 25, 30, 35]) # assertion, call_argument:, comparison_operator:Eq, function_call:average, int_literal, literal:List, literal:Num, suggest_constant_definition
    assert 4.5 == average([1, 2, 3, 4, 5, 6, 7, 8]) # assertion, call_argument:, comparison_operator:Eq, float_literal, function_call:average, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_median.py
# ----------------------------------------------------------------------------------------
def median(nums): # function:median (-> +10), function_argument:nums, function_argument_flavor:arg, function_returning_something:median (-> +10), lines_of_code:16 (-> +15)
    sorted_list = sorted(nums) # assignment, assignment_lhs_identifier:sorted_list, assignment_rhs_atom:nums, call_argument:nums, function_call:sorted, single_assignment:sorted_list
    med = None # assignment, assignment_lhs_identifier:med, assignment_rhs_atom:None, falsey_literal:None, literal:None, single_assignment:med
    if len(sorted_list) % 2 == 0: # binary_operator:Mod, call_argument:sorted_list, comparison_operator:Eq, divisibility_test:2, falsey_literal:0, function_call:len, if (-> +6), if_test_atom:0, if_test_atom:2, if_test_atom:sorted_list, int_literal, literal:Num
        mid_index_1 = len(sorted_list) // 2 # assignment, assignment_lhs_identifier:mid_index_1, assignment_rhs_atom:2, assignment_rhs_atom:sorted_list, binary_operator:FloorDiv, call_argument:sorted_list, function_call:len, if_then_branch (-> +2), int_literal, literal:Num, single_assignment:mid_index_1
        mid_index_2 = (len(sorted_list) // 2) - 1 # assignment, assignment_lhs_identifier:mid_index_2, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sorted_list, binary_operator:FloorDiv, binary_operator:Sub, call_argument:sorted_list, function_call:len, int_literal, literal:Num, single_assignment:mid_index_2
        med = (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / float(2) # assignment, assignment_lhs_identifier:med, assignment_rhs_atom:2, assignment_rhs_atom:mid_index_1, assignment_rhs_atom:mid_index_2, assignment_rhs_atom:sorted_list, binary_operator:Add, binary_operator:Div, call_argument:2, function_call:float, index:mid_index_1, index:mid_index_2, int_literal, literal:Num, single_assignment:med
    else:
        mid_index = (len(sorted_list) - 1) // 2 # assignment, assignment_lhs_identifier:mid_index, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sorted_list, binary_operator:FloorDiv, binary_operator:Sub, call_argument:sorted_list, function_call:len, if_else_branch (-> +1), int_literal, literal:Num, single_assignment:mid_index
        med = sorted_list[mid_index] # assignment, assignment_lhs_identifier:med, assignment_rhs_atom:mid_index, assignment_rhs_atom:sorted_list, index:mid_index, single_assignment:med
    return med # return:med
def main(): # function:main (-> +4), function_returning_nothing:main (-> +4), function_without_arguments:main (-> +4)
    print("Odd number of numbers:") # call_argument:, function_call:print, literal:Str
    print(median([2, 4, 6, 8, 20, 50, 70])) # call_argument:, composition, function_call:median, function_call:print, int_literal, literal:List, literal:Num, suggest_constant_definition
    print("Even number of numbers:") # call_argument:, function_call:print, literal:Str
    print(median([2, 4, 6, 8, 20, 50])) # call_argument:, composition, function_call:median, function_call:print, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/average_mode.py
# ----------------------------------------------------------------------------------------
import statistics # import:statistics, import_module:statistics, lines_of_code:9 (-> +8)
def mode(input_list): # function:mode (-> +7), function_argument:input_list, function_argument_flavor:arg, function_returning_something:mode (-> +7)
    check_list = input_list.copy() # assignment, assignment_lhs_identifier:check_list, assignment_rhs_atom:input_list, method_call:copy, single_assignment:check_list
    result = list() # assignment, assignment_lhs_identifier:result, function_call:list, function_call_without_arguments:list, single_assignment:result
    for x in input_list: # accumulate_all_elements:result (-> +4), accumulate_elements:result (-> +4), for:x (-> +4), for_each (-> +4), for_with_early_exit:return (-> +4), loop:for (-> +4)
        result.append(input_list.count(x)) # call_argument:, call_argument:x, composition, method_call:append, method_call:count, method_call_object:result, variable_update:result:x, variable_update_by_method_call:result:x
        input_list.remove(x) # call_argument:x, method_call:remove, method_call_object:input_list
        y = max(result) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:result, call_argument:result, function_call:max, single_assignment:y
        return check_list[result.index(y)] # call_argument:y, index:_, method_call:index, method_call_object:result, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/basic_maths.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, lines_of_code:48 (-> +47)
def prime_factors(n: int) -> list: # function:prime_factors (-> +11), function_argument:n, function_argument_flavor:arg, function_returning_something:prime_factors (-> +11)
    pf = [] # assignment, assignment_lhs_identifier:pf, falsey_literal:List, literal:List, single_assignment:pf
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +2), falsey_literal:0, int_literal, literal:Num, loop:while (-> +2), while (-> +2)
        pf.append(2) # call_argument:2, int_literal, literal:Num, method_call:append, method_call_object:pf, variable_update:pf:2, variable_update_by_method_call:pf:2
        n = int(n / 2) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, single_assignment:n, variable_update:n:2, variable_update_by_assignment:n:2
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_all_elements:n (-> +3), accumulate_all_elements:pf (-> +3), accumulate_elements:n (-> +3), accumulate_elements:pf (-> +3), binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:n, composition, for:i (-> +3), for_range:3:_:2 (-> +3), function_call:int, function_call:range, int_literal, literal:Num, loop:for (-> +3), method_call:sqrt, range:3:_:2, suggest_constant_definition
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, evolve_state (-> +2), falsey_literal:0, int_literal, literal:Num, loop:while (-> +2), while (-> +2)
            pf.append(i) # call_argument:i, method_call:append, method_call_object:pf, variable_update:pf:i, variable_update_by_method_call:pf:i
            n = int(n / i) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, single_assignment:n, variable_update:n:i, variable_update_by_assignment:n:i
    if n > 2: # comparison_operator:Gt, if (-> +1), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        pf.append(n) # call_argument:n, if_then_branch, method_call:append, method_call_object:pf, variable_update:pf:n, variable_update_by_method_call:pf:n
    return pf # return:pf
def number_of_divisors(n: int) -> int: # function:number_of_divisors (-> +13), function_argument:n, function_argument_flavor:arg, function_returning_something:number_of_divisors (-> +13)
    div = 1 # assignment, assignment_lhs_identifier:div, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:div
    temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:temp
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +2), falsey_literal:0, int_literal, literal:Num, loop:while (-> +2), while (-> +2)
        temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, int_literal, literal:Num, variable_increment:temp, variable_update:temp:1, variable_update_by_augmented_assignment:temp:1
        n = int(n / 2) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, single_assignment:n, variable_update:n:2, variable_update_by_assignment:n:2
    div *= temp # assignment_lhs_identifier:div, assignment_rhs_atom:temp, augmented_assignment:Mult, variable_update:div:temp, variable_update_by_augmented_assignment:div:temp
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_all_elements:n (-> +5), accumulate_elements:n (-> +5), binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:n, composition, for:i (-> +5), for_range:3:_:2 (-> +5), function_call:int, function_call:range, int_literal, literal:Num, loop:for (-> +5), method_call:sqrt, range:3:_:2, suggest_constant_definition
        temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:temp
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, falsey_literal:0, int_literal, literal:Num, loop:while (-> +2), while (-> +2)
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, int_literal, literal:Num, variable_increment:temp, variable_update:temp:1, variable_update_by_augmented_assignment:temp:1
            n = int(n / i) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, single_assignment:n, variable_update:n:i, variable_update_by_assignment:n:i
        div *= temp # assignment_lhs_identifier:div, assignment_rhs_atom:temp, augmented_assignment:Mult, variable_update:div:temp, variable_update_by_augmented_assignment:div:temp
    return div # return:div
def sum_of_divisors(n: int) -> int: # function:sum_of_divisors (-> +15), function_argument:n, function_argument_flavor:arg, function_returning_something:sum_of_divisors (-> +15)
    s = 1 # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:s
    temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:temp
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +2), falsey_literal:0, int_literal, literal:Num, loop:while (-> +2), while (-> +2)
        temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, int_literal, literal:Num, variable_increment:temp, variable_update:temp:1, variable_update_by_augmented_assignment:temp:1
        n = int(n / 2) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, single_assignment:n, variable_update:n:2, variable_update_by_assignment:n:2
    if temp > 1: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:temp, int_literal, literal:Num
        s *= (2 ** temp - 1) / (2 - 1) # assignment_lhs_identifier:s, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:temp, augmented_assignment:Mult, binary_operator:Div, binary_operator:Pow, binary_operator:Sub, if_then_branch, int_literal, literal:Num, variable_update:s:1, variable_update:s:2, variable_update:s:temp, variable_update_by_augmented_assignment:s:1, variable_update_by_augmented_assignment:s:2, variable_update_by_augmented_assignment:s:temp
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_all_elements:n (-> +6), accumulate_elements:n (-> +6), accumulate_elements:s (-> +6), accumulate_some_elements:s (-> +6), binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:n, composition, for:i (-> +6), for_range:3:_:2 (-> +6), function_call:int, function_call:range, int_literal, literal:Num, loop:for (-> +6), method_call:sqrt, range:3:_:2, suggest_constant_definition
        temp = 1 # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:temp
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, falsey_literal:0, int_literal, literal:Num, loop:while (-> +2), while (-> +2)
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, int_literal, literal:Num, variable_increment:temp, variable_update:temp:1, variable_update_by_augmented_assignment:temp:1
            n = int(n / i) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, single_assignment:n, variable_update:n:i, variable_update_by_assignment:n:i
        if temp > 1: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:temp, int_literal, literal:Num
            s *= (i ** temp - 1) / (i - 1) # assignment_lhs_identifier:s, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:temp, augmented_assignment:Mult, binary_operator:Div, binary_operator:Pow, binary_operator:Sub, if_then_branch, int_literal, literal:Num, variable_update:s:1, variable_update:s:i, variable_update:s:temp, variable_update_by_augmented_assignment:s:1, variable_update_by_augmented_assignment:s:i, variable_update_by_augmented_assignment:s:temp
    return int(s) # call_argument:s, function_call:int, function_tail_call:int, return
def euler_phi(n: int) -> int: # function:euler_phi (-> +4), function_argument:n, function_argument_flavor:arg, function_returning_something:euler_phi (-> +4)
    s = n # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:n, single_assignment:s
    for x in set(prime_factors(n)): # accumulate_all_elements:s (-> +1), accumulate_elements:s (-> +1), call_argument:, call_argument:n, composition, for:x (-> +1), function_call:prime_factors, function_call:set, loop:for (-> +1)
        s *= (x - 1) / x # assignment_lhs_identifier:s, assignment_rhs_atom:1, assignment_rhs_atom:x, augmented_assignment:Mult, binary_operator:Div, binary_operator:Sub, int_literal, literal:Num, variable_update:s:1, variable_update:s:x, variable_update_by_augmented_assignment:s:1, variable_update_by_augmented_assignment:s:x
    return int(s) # call_argument:s, function_call:int, function_tail_call:int, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/binary_exponentiation.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n): # body_recursive_function:binary_exponentiation (-> +7), function:binary_exponentiation (-> +7), function_argument:a, function_argument:n, function_argument_flavor:arg, function_returning_something:binary_exponentiation (-> +7), lines_of_code:8 (-> +7), recursive_function:binary_exponentiation (-> +7)
    if n == 0: # comparison_operator:Eq, falsey_literal:0, if (-> +6), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        return 1 # if_then_branch, int_literal, literal:Num, return:1
    elif n % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +4), if_test_atom:1, if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        return binary_exponentiation(a, n - 1) * a # binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:a, function_call:binary_exponentiation, if_elif_branch, int_literal, literal:Num, return
    else:
        b = binary_exponentiation(a, n / 2) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:2, assignment_rhs_atom:a, assignment_rhs_atom:n, binary_operator:Div, call_argument:, call_argument:a, function_call:binary_exponentiation, if_else_branch (-> +1), int_literal, literal:Num, single_assignment:b
        return b * b # binary_operator:Mult, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/binomial_coefficient.py
# ----------------------------------------------------------------------------------------
def binomial_coefficient(n, r): # function:binomial_coefficient (-> +8), function_argument:n, function_argument:r, function_argument_flavor:arg, function_returning_something:binomial_coefficient (-> +8), lines_of_code:10 (-> +9)
    C = [0 for i in range(r + 1)] # assignment, assignment_lhs_identifier:C, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:r, binary_operator:Add, call_argument:, comprehension:List, comprehension_for_count:1, falsey_literal:0, function_call:range, int_literal, literal:Num, range:_, single_assignment:C
    C[0] = 1 # assignment, assignment_lhs_identifier:C, assignment_rhs_atom:1, falsey_literal:0, index:0, int_literal, literal:Num
    for i in range(1, n + 1): # binary_operator:Add, call_argument:, call_argument:1, for:i (-> +4), for_range:1:_ (-> +4), function_call:range, int_literal, literal:Num, loop:for (-> +4), range:1:_
        j = min(i, r) # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:i, assignment_rhs_atom:r, call_argument:i, call_argument:r, function_call:min, single_assignment:j
        while j > 0: # comparison_operator:Gt, evolve_state (-> +2), falsey_literal:0, int_literal, literal:Num, loop:while (-> +2), while (-> +2)
            C[j] += C[j - 1] # assignment_lhs_identifier:C, assignment_rhs_atom:1, assignment_rhs_atom:C, assignment_rhs_atom:j, augmented_assignment:Add, binary_operator:Sub, index:_, index:j, index_arithmetic, int_literal, literal:Num, variable_update:C:1, variable_update:C:C, variable_update:C:j, variable_update_by_augmented_assignment:C:1, variable_update_by_augmented_assignment:C:C, variable_update_by_augmented_assignment:C:j
            j -= 1 # assignment_lhs_identifier:j, assignment_rhs_atom:1, augmented_assignment:Sub, int_literal, literal:Num, variable_update:j:1, variable_update_by_augmented_assignment:j:1
    return C[r] # index:r, return
print(binomial_coefficient(n=10, r=5)) # call_argument:, composition, function_call:binomial_coefficient, function_call:print, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/ceil.py
# ----------------------------------------------------------------------------------------
def ceil(x) -> int: # function:ceil (-> +2), function_argument:x, function_argument_flavor:arg, function_returning_something:ceil (-> +2), lines_of_code:3 (-> +2)
    return ( # return
        x if isinstance(x, int) or x - int(x) == 0 else int(x + 1) if x > 0 else int(x) # binary_operator:Add, binary_operator:Sub, boolean_operator:Or, call_argument:, call_argument:int, call_argument:x, comparison_operator:Eq, comparison_operator:Gt, conditional_expression, falsey_literal:0, function_call:int, function_call:isinstance, int_literal, literal:Num
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/collatz_sequence.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function:collatz_sequence (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:collatz_sequence (-> +8), lines_of_code:14 (-> +13)
    sequence = [n] # assignment, assignment_lhs_identifier:sequence, assignment_rhs_atom:n, single_assignment:sequence
    while n != 1: # comparison_operator:NotEq, evolve_state (-> +5), int_literal, literal:Num, loop:while (-> +5), while (-> +5)
        if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, falsey_literal:0, if (-> +3), if_test_atom:0, if_test_atom:2, if_test_atom:n, int_literal, literal:Num
            n //= 2 # assignment_lhs_identifier:n, assignment_rhs_atom:2, augmented_assignment:FloorDiv, if_then_branch, int_literal, literal:Num, variable_update:n:2, variable_update_by_augmented_assignment:n:2
        else:
            n = 3 * n + 1 # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, if_else_branch, int_literal, literal:Num, single_assignment:n, suggest_constant_definition, variable_update:n:1, variable_update:n:3, variable_update_by_assignment:n:1, variable_update_by_assignment:n:3
        sequence.append(n) # call_argument:n, method_call:append, method_call_object:sequence, variable_update:sequence:n, variable_update_by_method_call:sequence:n
    return sequence # return:sequence
def main(): # function:main (-> +4), function_returning_nothing:main (-> +4), function_without_arguments:main (-> +4)
    n = 43 # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:43, int_literal, literal:Num, single_assignment:n, suggest_constant_definition
    sequence = collatz_sequence(n) # assignment, assignment_lhs_identifier:sequence, assignment_rhs_atom:n, call_argument:n, function_call:collatz_sequence, single_assignment:sequence
    print(sequence) # call_argument:sequence, function_call:print
    print("collatz sequence from %d took %d steps." % (n, len(sequence))) # binary_operator:Mod, call_argument:, call_argument:sequence, composition, function_call:len, function_call:print, literal:Str, string_formatting_operator

# ----------------------------------------------------------------------------------------
# ../Python/maths/explicit_euler.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, lines_of_code:10 (-> +9)
def explicit_euler(ode_func, y0, x0, stepsize, x_end): # function:explicit_euler (-> +8), function_argument:ode_func, function_argument:stepsize, function_argument:x0, function_argument:x_end, function_argument:y0, function_argument_flavor:arg, function_returning_something:explicit_euler (-> +8)
    N = int(np.ceil((x_end - x0) / stepsize)) # assignment, assignment_lhs_identifier:N, assignment_rhs_atom:np, assignment_rhs_atom:stepsize, assignment_rhs_atom:x0, assignment_rhs_atom:x_end, binary_operator:Div, binary_operator:Sub, call_argument:, composition, function_call:int, method_call:ceil, single_assignment:N
    y = np.zeros((N + 1,)) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:N, assignment_rhs_atom:np, binary_operator:Add, call_argument:, int_literal, literal:Num, method_call:zeros, single_assignment:y
    y[0] = y0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:y0, falsey_literal:0, index:0, int_literal, literal:Num
    x = x0 # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:x0, single_assignment:x
    for k in range(N): # accumulate_all_elements:y (-> +2), accumulate_elements:y (-> +2), call_argument:N, for:k (-> +2), for_range:N (-> +2), function_call:range, loop:for (-> +2), range:N
        y[k + 1] = y[k] + stepsize * ode_func(x, y[k]) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:k, assignment_rhs_atom:stepsize, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:x, function_call:ode_func, index:_, index:k, index_arithmetic, int_literal, literal:Num, variable_update:y:k, variable_update:y:stepsize, variable_update:y:x, variable_update_by_assignment:y:k, variable_update_by_assignment:y:stepsize, variable_update_by_assignment:y:x
        x += stepsize # assignment_lhs_identifier:x, assignment_rhs_atom:stepsize, augmented_assignment:Add, variable_update:x:stepsize, variable_update_by_augmented_assignment:x:stepsize
    return y # return:y

# ----------------------------------------------------------------------------------------
# ../Python/maths/extended_euclidean_algorithm.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, lines_of_code:40 (-> +39)
def extended_euclidean_algorithm(m, n): # function:extended_euclidean_algorithm (-> +31), function_argument:m, function_argument:n, function_argument_flavor:arg, function_returning_something:extended_euclidean_algorithm (-> +31)
    a = 0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, falsey_literal:0, int_literal, literal:Num, single_assignment:a
    a_prime = 1 # assignment, assignment_lhs_identifier:a_prime, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:a_prime
    b = 1 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:b
    b_prime = 0 # assignment, assignment_lhs_identifier:b_prime, assignment_rhs_atom:0, falsey_literal:0, int_literal, literal:Num, single_assignment:b_prime
    q = 0 # assignment, assignment_lhs_identifier:q, assignment_rhs_atom:0, falsey_literal:0, int_literal, literal:Num, single_assignment:q
    r = 0 # assignment, assignment_lhs_identifier:r, assignment_rhs_atom:0, falsey_literal:0, int_literal, literal:Num, single_assignment:r
    if m > n: # comparison_operator:Gt, if (-> +5), if_test_atom:m, if_test_atom:n
        c = m # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:m, if_then_branch (-> +1), single_assignment:c
        d = n # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:n, single_assignment:d
    else:
        c = n # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:n, if_else_branch (-> +1), single_assignment:c
        d = m # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:m, single_assignment:d
    while True: # infinite_while (-> +12), literal:True, loop:while (-> +12), while (-> +12), while_with_early_exit:break (-> +12)
        q = int(c / d) # assignment, assignment_lhs_identifier:q, assignment_rhs_atom:c, assignment_rhs_atom:d, binary_operator:Div, call_argument:, function_call:int, single_assignment:q
        r = c % d # assignment, assignment_lhs_identifier:r, assignment_rhs_atom:c, assignment_rhs_atom:d, binary_operator:Mod, single_assignment:r
        if r == 0: # comparison_operator:Eq, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:r, int_literal, literal:Num
            break # break, if_then_branch
        c = d # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:d, single_assignment:c
        d = r # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:r, single_assignment:d
        t = a_prime # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:a_prime, single_assignment:t
        a_prime = a # assignment, assignment_lhs_identifier:a_prime, assignment_rhs_atom:a, single_assignment:a_prime
        a = t - q * a # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:a, assignment_rhs_atom:q, assignment_rhs_atom:t, binary_operator:Mult, binary_operator:Sub, single_assignment:a, variable_update:a:q, variable_update:a:t, variable_update_by_assignment:a:q, variable_update_by_assignment:a:t
        t = b_prime # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:b_prime, single_assignment:t
        b_prime = b # assignment, assignment_lhs_identifier:b_prime, assignment_rhs_atom:b, single_assignment:b_prime
        b = t - q * b # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:b, assignment_rhs_atom:q, assignment_rhs_atom:t, binary_operator:Mult, binary_operator:Sub, single_assignment:b, variable_update:b:q, variable_update:b:t, variable_update_by_assignment:b:q, variable_update_by_assignment:b:t
    pair = None # assignment, assignment_lhs_identifier:pair, assignment_rhs_atom:None, falsey_literal:None, literal:None, single_assignment:pair
    if m > n: # comparison_operator:Gt, if (-> +3), if_test_atom:m, if_test_atom:n, suggest_conditional_expression (-> +3)
        pair = (a, b) # assignment, assignment_lhs_identifier:pair, assignment_rhs_atom:a, assignment_rhs_atom:b, if_then_branch, single_assignment:pair
    else:
        pair = (b, a) # assignment, assignment_lhs_identifier:pair, assignment_rhs_atom:a, assignment_rhs_atom:b, if_else_branch, single_assignment:pair
    return pair # return:pair
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6), function_without_arguments:main (-> +6)
    if len(sys.argv) < 3: # call_argument:, comparison_operator:Lt, function_call:len, if (-> +2), if_test_atom:3, if_test_atom:sys, int_literal, literal:Num, suggest_constant_definition
        print("2 integer arguments required") # call_argument:, function_call:print, if_then_branch (-> +1), literal:Str
        exit(1) # call_argument:1, function_call:exit, int_literal, literal:Num
    m = int(sys.argv[1]) # assignment, assignment_lhs_identifier:m, assignment_rhs_atom:1, assignment_rhs_atom:sys, call_argument:, function_call:int, index:1, int_literal, literal:Num, single_assignment:m
    n = int(sys.argv[2]) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:sys, call_argument:, function_call:int, index:2, int_literal, literal:Num, single_assignment:n
    print(extended_euclidean_algorithm(m, n)) # call_argument:, call_argument:m, call_argument:n, composition, function_call:extended_euclidean_algorithm, function_call:print

# ----------------------------------------------------------------------------------------
# ../Python/maths/factorial_python.py
# ----------------------------------------------------------------------------------------
def factorial(input_number: int) -> int: # function:factorial (-> +8), function_argument:input_number, function_argument_flavor:arg, function_returning_something:factorial (-> +8), lines_of_code:9 (-> +8)
    if input_number < 0: # comparison_operator:Lt, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:input_number, int_literal, literal:Num
        raise ValueError("factorial() not defined for negative values") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    if not isinstance(input_number, int): # call_argument:input_number, call_argument:int, function_call:isinstance, if (-> +1), if_test_atom:input_number, if_test_atom:int, unary_operator:Not
        raise ValueError("factorial() only accepts integral values") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    result = 1 # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:result
    for i in range(1, input_number): # accumulate_all_elements:result (-> +1), accumulate_elements:result (-> +1), call_argument:1, call_argument:input_number, for:i (-> +1), for_range:1:input_number (-> +1), function_call:range, int_literal, literal:Num, loop:for (-> +1), range:1:input_number
        result = result * (i + 1) # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:result, binary_operator:Add, binary_operator:Mult, int_literal, literal:Num, single_assignment:result, suggest_augmented_assignment, variable_update:result:1, variable_update:result:i, variable_update_by_assignment:result:1, variable_update_by_assignment:result:i
    return result # return:result

# ----------------------------------------------------------------------------------------
# ../Python/maths/factorial_recursive.py
# ----------------------------------------------------------------------------------------
def factorial(n: int) -> int: # body_recursive_function:factorial (-> +5), function:factorial (-> +5), function_argument:n, function_argument_flavor:arg, function_returning_something:factorial (-> +5), lines_of_code:6 (-> +5), recursive_function:factorial (-> +5)
    if n < 0: # comparison_operator:Lt, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        raise ValueError("factorial() not defined for negative values") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    if not isinstance(n, int): # call_argument:int, call_argument:n, function_call:isinstance, if (-> +1), if_test_atom:int, if_test_atom:n, unary_operator:Not
        raise ValueError("factorial() only accepts integral values") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    return 1 if n == 0 or n == 1 else n * factorial(n - 1) # binary_operator:Mult, binary_operator:Sub, boolean_operator:Or, call_argument:, comparison_operator:Eq, conditional_expression, falsey_literal:0, function_call:factorial, int_literal, literal:Num, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/factors.py
# ----------------------------------------------------------------------------------------
def factors_of_a_number(num: int) -> list: # function:factors_of_a_number (-> +1), function_argument:num, function_argument_flavor:arg, function_returning_something:factors_of_a_number (-> +1), lines_of_code:2 (-> +1)
    return [i for i in range(1, num + 1) if num % i == 0] # binary_operator:Add, binary_operator:Mod, call_argument:, call_argument:1, comparison_operator:Eq, comprehension:List, comprehension_for_count:1, divisibility_test, falsey_literal:0, filtered_comprehension, function_call:range, int_literal, literal:Num, range:1:_, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/fermat_little_theorem.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n, mod): # body_recursive_function:binary_exponentiation (-> +7), function:binary_exponentiation (-> +7), function_argument:a, function_argument:mod, function_argument:n, function_argument_flavor:arg, function_returning_something:binary_exponentiation (-> +7), lines_of_code:13 (-> +12), recursive_function:binary_exponentiation (-> +7)
    if n == 0: # comparison_operator:Eq, falsey_literal:0, if (-> +6), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        return 1 # if_then_branch, int_literal, literal:Num, return:1
    elif n % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +4), if_test_atom:1, if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        return (binary_exponentiation(a, n - 1, mod) * a) % mod # binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:a, call_argument:mod, function_call:binary_exponentiation, if_elif_branch, int_literal, literal:Num, return
    else:
        b = binary_exponentiation(a, n / 2, mod) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:2, assignment_rhs_atom:a, assignment_rhs_atom:mod, assignment_rhs_atom:n, binary_operator:Div, call_argument:, call_argument:a, call_argument:mod, function_call:binary_exponentiation, if_else_branch (-> +1), int_literal, literal:Num, single_assignment:b
        return (b * b) % mod # binary_operator:Mod, binary_operator:Mult, return
p = 701 # assignment, assignment_lhs_identifier:p, assignment_rhs_atom:701, int_literal, literal:Num, single_assignment:p, suggest_constant_definition
a = 1000000000 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:1000000000, int_literal, literal:Num, single_assignment:a, suggest_constant_definition
b = 10 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:10, int_literal, literal:Num, single_assignment:b, suggest_constant_definition
print((a / b) % p == (a * binary_exponentiation(b, p - 2, p)) % p) # binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:b, call_argument:p, comparison_operator:Eq, composition, divisibility_test, function_call:binary_exponentiation, function_call:print, int_literal, literal:Num
print((a / b) % p == (a * b ** (p - 2)) % p) # binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, call_argument:, comparison_operator:Eq, divisibility_test, function_call:print, int_literal, literal:Num

# ----------------------------------------------------------------------------------------
# ../Python/maths/fibonacci.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, lines_of_code:72 (-> +71)
import functools # import:functools, import_module:functools
import time # import:time, import_module:time
from decimal import getcontext, Decimal # import:decimal:Decimal, import:decimal:getcontext, import_module:decimal, import_name:Decimal, import_name:getcontext
getcontext().prec = 100 # assignment, assignment_rhs_atom:100, function_call:getcontext, function_call_without_arguments:getcontext, int_literal, literal:Num
def timer_decorator(func): # closure:timer_decorator (-> +11), function:timer_decorator (-> +11), function_argument:func, function_argument_flavor:arg, function_returning_something:timer_decorator (-> +11), nested_function:timer_decorator (-> +11)
    @functools.wraps(func) # call_argument:func, decorated_function:timer_wrapper (-> +9), function:timer_wrapper (-> +9), function_returning_something:timer_wrapper (-> +9), method_call:wraps
    def timer_wrapper(*args, **kwargs): # function_argument:args, function_argument:kwargs, function_argument_flavor:kwarg, function_argument_flavor:vararg
        start = time.time() # assignment, assignment_lhs_identifier:start, assignment_rhs_atom:time, method_call:time, single_assignment:start
        func(*args, **kwargs) # call_argument:, function_call:func
        end = time.time() # assignment, assignment_lhs_identifier:end, assignment_rhs_atom:time, method_call:time, single_assignment:end
        if int(end - start) > 0: # binary_operator:Sub, call_argument:, comparison_operator:Gt, falsey_literal:0, function_call:int, if (-> +3), if_test_atom:0, if_test_atom:end, if_test_atom:start, int_literal, literal:Num
            print(f"Run time for {func.__name__}: {(end - start):0.2f}s") # binary_operator:Sub, call_argument:, f_string, function_call:print, if_then_branch, literal:Str
        else:
            print(f"Run time for {func.__name__}: {(end - start)*1000:0.2f}ms") # binary_operator:Mult, binary_operator:Sub, call_argument:, f_string, function_call:print, if_else_branch, int_literal, literal:Num, literal:Str, suggest_constant_definition
        return func(*args, **kwargs) # call_argument:, function_call:func, function_tail_call:func, return
    return timer_wrapper # return:timer_wrapper
class Error(Exception): # class:Error (-> +1)
    pass
class ValueTooLargeError(Error): # class:ValueTooLargeError (-> +1)
    pass
class ValueTooSmallError(Error): # class:ValueTooSmallError (-> +1)
    pass
class ValueLessThanZero(Error): # class:ValueLessThanZero (-> +1)
    pass
def _check_number_input(n, min_thresh, max_thresh=None): # falsey_literal:None, function:_check_number_input (-> +22), function_argument:max_thresh, function_argument:min_thresh, function_argument:n, function_argument_flavor:arg, function_returning_something:_check_number_input (-> +22), literal:None
    try: # try (-> +19), try_except:ValueLessThanZero (-> +19), try_except:ValueTooLargeError (-> +19), try_except:ValueTooSmallError (-> +19), try_raise:ValueLessThanZero (-> +19), try_raise:ValueTooLargeError (-> +19), try_raise:ValueTooSmallError (-> +19)
        if n >= min_thresh and max_thresh is None: # boolean_operator:And, comparison_operator:GtE, comparison_operator:Is, falsey_literal:None, if (-> +9), if_test_atom:None, if_test_atom:max_thresh, if_test_atom:min_thresh, if_test_atom:n, literal:None
            return True # if_then_branch, literal:True, return:True
        elif min_thresh <= n <= max_thresh: # chained_comparison:2, chained_inequalities:2, comparison_operator:LtE, if (-> +7), if_test_atom:max_thresh, if_test_atom:min_thresh, if_test_atom:n
            return True # if_elif_branch, literal:True, return:True
        elif n < 0: # comparison_operator:Lt, falsey_literal:0, if (-> +5), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
            raise ValueLessThanZero # if_elif_branch, raise:ValueLessThanZero
        elif n < min_thresh: # comparison_operator:Lt, if (-> +3), if_test_atom:min_thresh, if_test_atom:n
            raise ValueTooSmallError # if_elif_branch, raise:ValueTooSmallError
        elif n > max_thresh: # comparison_operator:Gt, if (-> +1), if_test_atom:max_thresh, if_test_atom:n
            raise ValueTooLargeError # if_elif_branch, raise:ValueTooLargeError
    except ValueLessThanZero: # except:ValueLessThanZero
        print("Incorrect Input: number must not be less than 0") # call_argument:, function_call:print, literal:Str
    except ValueTooSmallError: # except:ValueTooSmallError
        print( # function_call:print
            f"Incorrect Input: input number must be > {min_thresh} for the recursive calculation" # call_argument:, f_string, literal:Str
        )
    except ValueTooLargeError: # except:ValueTooLargeError
        print( # function_call:print
            f"Incorrect Input: input number must be < {max_thresh} for the recursive calculation" # call_argument:, f_string, literal:Str
        )
    return False # falsey_literal:False, literal:False, return:False
@timer_decorator # decorated_function:fib_iterative (-> +9), function:fib_iterative (-> +9), function_decorator:timer_decorator (-> +9), function_returning_something:fib_iterative (-> +9)
def fib_iterative(n): # function_argument:n, function_argument_flavor:arg
    n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int, single_assignment:n
    if _check_number_input(n, 2): # call_argument:2, call_argument:n, function_call:_check_number_input, if (-> +6), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        seq_out = [0, 1] # assignment, assignment_lhs_identifier:seq_out, assignment_rhs_atom:0, assignment_rhs_atom:1, falsey_literal:0, if_then_branch (-> +5), int_literal, literal:List, literal:Num, single_assignment:seq_out
        a, b = 0, 1 # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:0, assignment_rhs_atom:1, falsey_literal:0, int_literal, literal:Num, literal:Tuple
        for _ in range(n - len(seq_out)): # binary_operator:Sub, call_argument:, call_argument:seq_out, composition, for:_ (-> +2), for_range:_ (-> +2), function_call:len, function_call:range, loop:for (-> +2), range:_
            a, b = b, a + b # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, slide, variable_update:a:b, variable_update:b:a, variable_update_by_assignment:a:b, variable_update_by_assignment:b:a
            seq_out.append(b) # call_argument:b, method_call:append, method_call_object:seq_out, variable_update:seq_out:b, variable_update_by_method_call:seq_out:b
        return seq_out # return:seq_out
@timer_decorator # decorated_function:fib_formula (-> +13), function:fib_formula (-> +13), function_decorator:timer_decorator (-> +13), function_returning_something:fib_formula (-> +13)
def fib_formula(n): # function_argument:n, function_argument_flavor:arg
    seq_out = [0, 1] # assignment, assignment_lhs_identifier:seq_out, assignment_rhs_atom:0, assignment_rhs_atom:1, falsey_literal:0, int_literal, literal:List, literal:Num, single_assignment:seq_out
    n = int(n) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, function_call:int, single_assignment:n
    if _check_number_input(n, 2, 1000000): # call_argument:1000000, call_argument:2, call_argument:n, function_call:_check_number_input, if (-> +9), if_test_atom:1000000, if_test_atom:2, if_test_atom:n, int_literal, literal:Num, suggest_constant_definition
        sqrt = Decimal(math.sqrt(5)) # assignment, assignment_lhs_identifier:sqrt, assignment_rhs_atom:5, assignment_rhs_atom:math, call_argument:, call_argument:5, composition, function_call:Decimal, if_then_branch (-> +8), int_literal, literal:Num, method_call:sqrt, single_assignment:sqrt, suggest_constant_definition
        phi_1 = Decimal(1 + sqrt) / Decimal(2) # assignment, assignment_lhs_identifier:phi_1, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sqrt, binary_operator:Add, binary_operator:Div, call_argument:, call_argument:2, function_call:Decimal, int_literal, literal:Num, single_assignment:phi_1
        phi_2 = Decimal(1 - sqrt) / Decimal(2) # assignment, assignment_lhs_identifier:phi_2, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sqrt, binary_operator:Div, binary_operator:Sub, call_argument:, call_argument:2, function_call:Decimal, int_literal, literal:Num, single_assignment:phi_2
        for i in range(2, n): # call_argument:2, call_argument:n, for:i (-> +4), for_range:2:n (-> +4), function_call:range, int_literal, literal:Num, loop:for (-> +4), range:2:n
            temp_out = ((phi_1 ** Decimal(i)) - (phi_2 ** Decimal(i))) * ( # assignment, assignment_lhs_identifier:temp_out, assignment_rhs_atom:i, assignment_rhs_atom:phi_1, assignment_rhs_atom:phi_2, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, call_argument:i, function_call:Decimal, single_assignment:temp_out
                Decimal(sqrt) ** Decimal(-1) # assignment_rhs_atom:-1, assignment_rhs_atom:sqrt, binary_operator:Pow, call_argument:-1, call_argument:sqrt, function_call:Decimal, int_literal, literal:Num
            )
            seq_out.append(int(temp_out)) # call_argument:, call_argument:temp_out, composition, function_call:int, method_call:append, method_call_object:seq_out, variable_update:seq_out:temp_out, variable_update_by_method_call:seq_out:temp_out
        return seq_out # return:seq_out

# ----------------------------------------------------------------------------------------
# ../Python/maths/fibonacci_sequence_recursion.py
# ----------------------------------------------------------------------------------------
def recur_fibo(n): # body_recursive_function:recur_fibo (-> +1), function:recur_fibo (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:recur_fibo (-> +1), lines_of_code:9 (-> +8), recursive_function:recur_fibo (-> +1)
    return n if n <= 1 else recur_fibo(n - 1) + recur_fibo(n - 2) # binary_operator:Add, binary_operator:Sub, call_argument:, comparison_operator:LtE, conditional_expression, function_call:recur_fibo, int_literal, literal:Num, return
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6), function_without_arguments:main (-> +6)
    limit = int(input("How many terms to include in fibonacci series: ")) # assignment, assignment_lhs_identifier:limit, call_argument:, composition, function_call:input, function_call:int, literal:Str, single_assignment:limit
    if limit > 0: # comparison_operator:Gt, falsey_literal:0, if (-> +4), if_test_atom:0, if_test_atom:limit, int_literal, literal:Num
        print(f"The first {limit} terms of the fibonacci series are as follows:") # call_argument:, f_string, function_call:print, if_then_branch (-> +1), literal:Str
        print([recur_fibo(n) for n in range(limit)]) # call_argument:, call_argument:limit, call_argument:n, composition, comprehension:List, comprehension_for_count:1, function_call:print, function_call:range, function_call:recur_fibo, range:limit
    else:
        print("Please enter a positive integer: ") # call_argument:, function_call:print, if_else_branch, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_max.py
# ----------------------------------------------------------------------------------------
def find_max(nums): # function:find_max (-> +5), function_argument:nums, function_argument_flavor:arg, function_returning_something:find_max (-> +5), lines_of_code:8 (-> +7)
    max_num = nums[0] # assignment, assignment_lhs_identifier:max_num, assignment_rhs_atom:0, assignment_rhs_atom:nums, falsey_literal:0, index:0, int_literal, literal:Num, single_assignment:max_num
    for x in nums: # find_best_element:x:max_num (-> +2), for:x (-> +2), for_each (-> +2), loop:for (-> +2)
        if x > max_num: # comparison_operator:Gt, if (-> +1), if_test_atom:max_num, if_test_atom:x
            max_num = x # assignment, assignment_lhs_identifier:max_num, assignment_rhs_atom:x, if_then_branch, single_assignment:max_num
    return max_num # return:max_num
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    print(find_max([2, 4, 9, 7, 19, 94, 5])) # call_argument:, composition, function_call:find_max, function_call:print, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_max_recursion.py
# ----------------------------------------------------------------------------------------
def find_max(nums, left, right): # body_recursive_function:find_max (-> +6), function:find_max (-> +6), function_argument:left, function_argument:nums, function_argument:right, function_argument_flavor:arg, function_returning_something:find_max (-> +6), lines_of_code:7 (-> +6), recursive_function:find_max (-> +6)
    if left == right: # comparison_operator:Eq, if (-> +1), if_test_atom:left, if_test_atom:right
        return nums[left] # if_then_branch, index:left, return
    mid = (left + right) >> 1 # assignment, assignment_lhs_identifier:mid, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:RShift, int_literal, literal:Num, single_assignment:mid
    left_max = find_max(nums, left, mid) # assignment, assignment_lhs_identifier:left_max, assignment_rhs_atom:left, assignment_rhs_atom:mid, assignment_rhs_atom:nums, call_argument:left, call_argument:mid, call_argument:nums, function_call:find_max, single_assignment:left_max
    right_max = find_max(nums, mid + 1, right) # assignment, assignment_lhs_identifier:right_max, assignment_rhs_atom:1, assignment_rhs_atom:mid, assignment_rhs_atom:nums, assignment_rhs_atom:right, binary_operator:Add, call_argument:, call_argument:nums, call_argument:right, function_call:find_max, int_literal, literal:Num, single_assignment:right_max
    return left_max if left_max >= right_max else right_max # comparison_operator:GtE, conditional_expression, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_min.py
# ----------------------------------------------------------------------------------------
def find_min(nums): # function:find_min (-> +5), function_argument:nums, function_argument_flavor:arg, function_returning_something:find_min (-> +5), lines_of_code:8 (-> +7)
    min_num = nums[0] # assignment, assignment_lhs_identifier:min_num, assignment_rhs_atom:0, assignment_rhs_atom:nums, falsey_literal:0, index:0, int_literal, literal:Num, single_assignment:min_num
    for num in nums: # find_best_element:num:min_num (-> +2), for:num (-> +2), for_each (-> +2), loop:for (-> +2)
        if min_num > num: # comparison_operator:Gt, if (-> +1), if_test_atom:min_num, if_test_atom:num
            min_num = num # assignment, assignment_lhs_identifier:min_num, assignment_rhs_atom:num, if_then_branch, single_assignment:min_num
    return min_num # return:min_num
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    assert find_min([0, 1, 2, 3, 4, 5, -3, 24, -56]) == -56 # assertion, call_argument:, comparison_operator:Eq, falsey_literal:0, function_call:find_min, int_literal, literal:List, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/find_min_recursion.py
# ----------------------------------------------------------------------------------------
def find_min(nums, left, right): # body_recursive_function:find_min (-> +6), function:find_min (-> +6), function_argument:left, function_argument:nums, function_argument:right, function_argument_flavor:arg, function_returning_something:find_min (-> +6), lines_of_code:7 (-> +6), recursive_function:find_min (-> +6)
    if left == right: # comparison_operator:Eq, if (-> +1), if_test_atom:left, if_test_atom:right
        return nums[left] # if_then_branch, index:left, return
    mid = (left + right) >> 1 # assignment, assignment_lhs_identifier:mid, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:RShift, int_literal, literal:Num, single_assignment:mid
    left_min = find_min(nums, left, mid) # assignment, assignment_lhs_identifier:left_min, assignment_rhs_atom:left, assignment_rhs_atom:mid, assignment_rhs_atom:nums, call_argument:left, call_argument:mid, call_argument:nums, function_call:find_min, single_assignment:left_min
    right_min = find_min(nums, mid + 1, right) # assignment, assignment_lhs_identifier:right_min, assignment_rhs_atom:1, assignment_rhs_atom:mid, assignment_rhs_atom:nums, assignment_rhs_atom:right, binary_operator:Add, call_argument:, call_argument:nums, call_argument:right, function_call:find_min, int_literal, literal:Num, single_assignment:right_min
    return left_min if left_min <= right_min else right_min # comparison_operator:LtE, conditional_expression, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/floor.py
# ----------------------------------------------------------------------------------------
def floor(x) -> int: # function:floor (-> +2), function_argument:x, function_argument_flavor:arg, function_returning_something:floor (-> +2), lines_of_code:3 (-> +2)
    return ( # return
        x if isinstance(x, int) or x - int(x) == 0 else int(x) if x > 0 else int(x - 1) # binary_operator:Sub, boolean_operator:Or, call_argument:, call_argument:int, call_argument:x, comparison_operator:Eq, comparison_operator:Gt, conditional_expression, falsey_literal:0, function_call:int, function_call:isinstance, int_literal, literal:Num
    )

# ----------------------------------------------------------------------------------------
# ../Python/maths/gaussian.py
# ----------------------------------------------------------------------------------------
from numpy import pi, sqrt, exp # import:numpy:exp, import:numpy:pi, import:numpy:sqrt, import_module:numpy, import_name:exp, import_name:pi, import_name:sqrt, lines_of_code:3 (-> +2)
def gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> int: # falsey_literal:0.0, float_literal, function:gaussian (-> +1), function_argument:mu, function_argument:sigma, function_argument:x, function_argument_flavor:arg, function_returning_something:gaussian (-> +1), literal:Num
    return 1 / sqrt(2 * pi * sigma ** 2) * exp(-((x - mu) ** 2) / 2 * sigma ** 2) # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, call_argument:, function_call:exp, function_call:sqrt, int_literal, literal:Num, return, unary_operator:USub

# ----------------------------------------------------------------------------------------
# ../Python/maths/greatest_common_divisor.py
# ----------------------------------------------------------------------------------------
def greatest_common_divisor(a, b): # function:greatest_common_divisor (-> +1), function_argument:a, function_argument:b, function_argument_flavor:arg, function_returning_something:greatest_common_divisor (-> +1), lines_of_code:17 (-> +16), recursive_function:greatest_common_divisor (-> +1), tail_recursive_function:greatest_common_divisor (-> +1)
    return b if a == 0 else greatest_common_divisor(b % a, a) # binary_operator:Mod, call_argument:, call_argument:a, comparison_operator:Eq, conditional_expression, falsey_literal:0, function_call:greatest_common_divisor, function_tail_call:greatest_common_divisor, int_literal, literal:Num, return
def gcd_by_iterative(x, y): # function:gcd_by_iterative (-> +3), function_argument:x, function_argument:y, function_argument_flavor:arg, function_returning_something:gcd_by_iterative (-> +3)
    while y: # loop:while (-> +1), while (-> +1)
        x, y = y, x % y # assignment, assignment_lhs_identifier:x, assignment_lhs_identifier:y, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Mod, slide, variable_update:x:y, variable_update:y:x, variable_update_by_assignment:x:y, variable_update_by_assignment:y:x
    return x # return:x
def main(): # function:main (-> +10), function_returning_nothing:main (-> +10), function_without_arguments:main (-> +10)
    try: # try (-> +9), try_except:IndexError (-> +9), try_except:UnboundLocalError (-> +9), try_except:ValueError (-> +9)
        nums = input("Enter two integers separated by comma (,): ").split(",") # assignment, assignment_lhs_identifier:nums, call_argument:, function_call:input, literal:Str, method_call:split, single_assignment:nums
        num_1 = int(nums[0]) # assignment, assignment_lhs_identifier:num_1, assignment_rhs_atom:0, assignment_rhs_atom:nums, call_argument:, falsey_literal:0, function_call:int, index:0, int_literal, literal:Num, single_assignment:num_1
        num_2 = int(nums[1]) # assignment, assignment_lhs_identifier:num_2, assignment_rhs_atom:1, assignment_rhs_atom:nums, call_argument:, function_call:int, index:1, int_literal, literal:Num, single_assignment:num_2
        print( # composition, function_call:print
            f"greatest_common_divisor({num_1}, {num_2}) = {greatest_common_divisor(num_1, num_2)}" # call_argument:, call_argument:num_1, call_argument:num_2, f_string, function_call:greatest_common_divisor, literal:Str
        )
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}") # call_argument:, call_argument:num_1, call_argument:num_2, composition, f_string, function_call:gcd_by_iterative, function_call:print, literal:Str
    except (IndexError, UnboundLocalError, ValueError): # except:IndexError, except:UnboundLocalError, except:ValueError
        print("Wrong input") # call_argument:, function_call:print, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/hardy_ramanujanalgo.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, lines_of_code:17 (-> +16)
def exactPrimeFactorCount(n): # function:exactPrimeFactorCount (-> +15), function_argument:n, function_argument_flavor:arg, function_returning_something:exactPrimeFactorCount (-> +15)
    count = 0 # assignment, assignment_lhs_identifier:count, assignment_rhs_atom:0, falsey_literal:0, int_literal, literal:Num, single_assignment:count
    if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, falsey_literal:0, if (-> +3), if_test_atom:0, if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch (-> +2), int_literal, literal:Num, variable_increment:count, variable_update:count:1, variable_update_by_augmented_assignment:count:1
        while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, evolve_state (-> +1), falsey_literal:0, int_literal, literal:Num, loop:while (-> +1), while (-> +1)
            n = int(n / 2) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, single_assignment:n, variable_update:n:2, variable_update_by_assignment:n:2
    i = 3 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:3, int_literal, literal:Num, single_assignment:i, suggest_constant_definition
    while i <= int(math.sqrt(n)): # call_argument:, call_argument:n, comparison_operator:LtE, composition, evolve_state (-> +5), function_call:int, loop:while (-> +5), method_call:sqrt, while (-> +5)
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, falsey_literal:0, if (-> +3), if_test_atom:0, if_test_atom:i, if_test_atom:n, int_literal, literal:Num
            count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch (-> +2), int_literal, literal:Num, variable_increment:count, variable_update:count:1, variable_update_by_augmented_assignment:count:1
            while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, falsey_literal:0, int_literal, literal:Num, loop:while (-> +1), while (-> +1)
                n = int(n / i) # assignment, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, function_call:int, single_assignment:n, variable_update:n:i, variable_update_by_assignment:n:i
        i = i + 2 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:2, assignment_rhs_atom:i, binary_operator:Add, int_literal, literal:Num, single_assignment:i, suggest_augmented_assignment, variable_update:i:2, variable_update_by_assignment:i:2
    if n > 2: # comparison_operator:Gt, if (-> +1), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, int_literal, literal:Num, variable_increment:count, variable_update:count:1, variable_update_by_augmented_assignment:count:1
    return count # return:count

# ----------------------------------------------------------------------------------------
# ../Python/maths/is_square_free.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List, lines_of_code:3 (-> +2)
def is_square_free(factors: List[int]) -> bool: # function:is_square_free (-> +1), function_argument:factors, function_argument_flavor:arg, function_returning_something:is_square_free (-> +1)
    return len(set(factors)) == len(factors) # call_argument:, call_argument:factors, comparison_operator:Eq, composition, function_call:len, function_call:set, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/jaccard_similarity.py
# ----------------------------------------------------------------------------------------
def jaccard_similariy(setA, setB, alternativeUnion=False): # falsey_literal:False, function:jaccard_similariy (-> +14), function_argument:alternativeUnion, function_argument:setA, function_argument:setB, function_argument_flavor:arg, function_returning_something:jaccard_similariy (-> +14), lines_of_code:15 (-> +14), literal:False
    if isinstance(setA, set) and isinstance(setB, set): # boolean_operator:And, call_argument:set, call_argument:setA, call_argument:setB, function_call:isinstance, if (-> +6), if_test_atom:set, if_test_atom:setA, if_test_atom:setB
        intersection = len(setA.intersection(setB)) # assignment, assignment_lhs_identifier:intersection, assignment_rhs_atom:setA, assignment_rhs_atom:setB, call_argument:, call_argument:setB, composition, function_call:len, if_then_branch (-> +5), method_call:intersection, single_assignment:intersection
        if alternativeUnion: # if (-> +3), nested_if:1 (-> +3), suggest_conditional_expression (-> +3)
            union = len(setA) + len(setB) # assignment, assignment_lhs_identifier:union, assignment_rhs_atom:setA, assignment_rhs_atom:setB, binary_operator:Add, call_argument:setA, call_argument:setB, function_call:len, if_then_branch, single_assignment:union
        else:
            union = len(setA.union(setB)) # assignment, assignment_lhs_identifier:union, assignment_rhs_atom:setA, assignment_rhs_atom:setB, call_argument:, call_argument:setB, composition, function_call:len, if_else_branch, method_call:union, single_assignment:union
        return intersection / union # binary_operator:Div, return
    if isinstance(setA, (list, tuple)) and isinstance(setB, (list, tuple)): # boolean_operator:And, call_argument:, call_argument:setA, call_argument:setB, function_call:isinstance, if (-> +6), if_test_atom:list, if_test_atom:setA, if_test_atom:setB, if_test_atom:tuple
        intersection = [element for element in setA if element in setB] # assignment, assignment_lhs_identifier:intersection, assignment_rhs_atom:element, assignment_rhs_atom:setA, assignment_rhs_atom:setB, comparison_operator:In, comprehension:List, comprehension_for_count:1, filtered_comprehension, if_then_branch (-> +5), single_assignment:intersection
        if alternativeUnion: # if (-> +3), nested_if:1 (-> +3), suggest_conditional_expression (-> +3)
            union = len(setA) + len(setB) # assignment, assignment_lhs_identifier:union, assignment_rhs_atom:setA, assignment_rhs_atom:setB, binary_operator:Add, call_argument:setA, call_argument:setB, function_call:len, if_then_branch, single_assignment:union
        else:
            union = setA + [element for element in setB if element not in setA] # assignment, assignment_lhs_identifier:union, assignment_rhs_atom:element, assignment_rhs_atom:setA, assignment_rhs_atom:setB, binary_operator:Add, comparison_operator:NotIn, comprehension:List, comprehension_for_count:1, filtered_comprehension, if_else_branch, single_assignment:union
        return len(intersection) / len(union) # binary_operator:Div, call_argument:intersection, call_argument:union, function_call:len, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/karatsuba.py
# ----------------------------------------------------------------------------------------
def karatsuba(a, b): # body_recursive_function:karatsuba (-> +11), function:karatsuba (-> +11), function_argument:a, function_argument:b, function_argument_flavor:arg, function_returning_something:karatsuba (-> +11), lines_of_code:14 (-> +13), recursive_function:karatsuba (-> +11)
    if len(str(a)) == 1 or len(str(b)) == 1: # boolean_operator:Or, call_argument:, call_argument:a, call_argument:b, comparison_operator:Eq, composition, function_call:len, function_call:str, if (-> +10), if_test_atom:1, if_test_atom:a, if_test_atom:b, int_literal, literal:Num
        return a * b # binary_operator:Mult, if_then_branch, return
    else:
        m1 = max(len(str(a)), len(str(b))) # assignment, assignment_lhs_identifier:m1, assignment_rhs_atom:a, assignment_rhs_atom:b, call_argument:, call_argument:a, call_argument:b, composition, function_call:len, function_call:max, function_call:str, if_else_branch (-> +7), single_assignment:m1
        m2 = m1 // 2 # assignment, assignment_lhs_identifier:m2, assignment_rhs_atom:2, assignment_rhs_atom:m1, binary_operator:FloorDiv, int_literal, literal:Num, single_assignment:m2
        a1, a2 = divmod(a, 10 ** m2) # assignment, assignment_lhs_identifier:a1, assignment_lhs_identifier:a2, assignment_rhs_atom:10, assignment_rhs_atom:a, assignment_rhs_atom:m2, binary_operator:Pow, call_argument:, call_argument:a, function_call:divmod, int_literal, literal:Num, suggest_constant_definition
        b1, b2 = divmod(b, 10 ** m2) # assignment, assignment_lhs_identifier:b1, assignment_lhs_identifier:b2, assignment_rhs_atom:10, assignment_rhs_atom:b, assignment_rhs_atom:m2, binary_operator:Pow, call_argument:, call_argument:b, function_call:divmod, int_literal, literal:Num, suggest_constant_definition
        x = karatsuba(a2, b2) # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:a2, assignment_rhs_atom:b2, call_argument:a2, call_argument:b2, function_call:karatsuba, single_assignment:x
        y = karatsuba((a1 + a2), (b1 + b2)) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:a1, assignment_rhs_atom:a2, assignment_rhs_atom:b1, assignment_rhs_atom:b2, binary_operator:Add, call_argument:, function_call:karatsuba, single_assignment:y
        z = karatsuba(a1, b1) # assignment, assignment_lhs_identifier:z, assignment_rhs_atom:a1, assignment_rhs_atom:b1, call_argument:a1, call_argument:b1, function_call:karatsuba, single_assignment:z
        return (z * 10 ** (2 * m2)) + ((y - z - x) * 10 ** (m2)) + (x) # binary_operator:Add, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, int_literal, literal:Num, return, suggest_constant_definition
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    print(karatsuba(15463, 23489)) # call_argument:, call_argument:15463, call_argument:23489, composition, function_call:karatsuba, function_call:print, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/kth_lexicographic_permutation.py
# ----------------------------------------------------------------------------------------
def kthPermutation(k, n): # function:kthPermutation (-> +13), function_argument:k, function_argument:n, function_argument_flavor:arg, function_returning_something:kthPermutation (-> +13), lines_of_code:14 (-> +13)
    factorials = [1] # assignment, assignment_lhs_identifier:factorials, assignment_rhs_atom:1, int_literal, literal:List, literal:Num, single_assignment:factorials
    for i in range(2, n): # call_argument:2, call_argument:n, for:i (-> +1), for_range:2:n (-> +1), function_call:range, int_literal, literal:Num, loop:for (-> +1), range:2:n
        factorials.append(factorials[-1] * i) # binary_operator:Mult, call_argument:, index:-1, int_literal, literal:Num, method_call:append, method_call_object:factorials, negative_index:-1
    assert 0 <= k < factorials[-1] * n, "k out of bounds" # assertion, binary_operator:Mult, chained_comparison:2, comparison_operator:Lt, comparison_operator:LtE, falsey_literal:0, index:-1, int_literal, literal:Num, literal:Str, negative_index:-1
    permutation = [] # assignment, assignment_lhs_identifier:permutation, falsey_literal:List, literal:List, single_assignment:permutation
    elements = list(range(n)) # assignment, assignment_lhs_identifier:elements, assignment_rhs_atom:n, call_argument:, call_argument:n, composition, function_call:list, function_call:range, range:n, single_assignment:elements
    while factorials: # loop:while (-> +4), while (-> +4)
        factorial = factorials.pop() # assignment, assignment_lhs_identifier:factorial, assignment_rhs_atom:factorials, method_call:pop, single_assignment:factorial
        number, k = divmod(k, factorial) # assignment, assignment_lhs_identifier:k, assignment_lhs_identifier:number, assignment_rhs_atom:factorial, assignment_rhs_atom:k, call_argument:factorial, call_argument:k, function_call:divmod, variable_update:k:factorial, variable_update_by_assignment:k:factorial
        permutation.append(elements[number]) # call_argument:, index:number, method_call:append, method_call_object:permutation
        elements.remove(elements[number]) # call_argument:, index:number, method_call:remove, method_call_object:elements
    permutation.append(elements[0]) # call_argument:, falsey_literal:0, index:0, int_literal, literal:Num, method_call:append, method_call_object:permutation
    return permutation # return:permutation

# ----------------------------------------------------------------------------------------
# ../Python/maths/largest_of_very_large_numbers.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, lines_of_code:9 (-> +8)
def res(x, y): # function:res (-> +7), function_argument:x, function_argument:y, function_argument_flavor:arg, function_returning_something:res (-> +7)
    if 0 not in (x, y): # comparison_operator:NotIn, falsey_literal:0, if (-> +6), if_test_atom:0, if_test_atom:x, if_test_atom:y, int_literal, literal:Num
        return y * math.log10(x) # binary_operator:Mult, call_argument:x, if_then_branch, method_call:log10, return
    else:
        if x == 0: # comparison_operator:Eq, falsey_literal:0, if (-> +3), if_test_atom:0, if_test_atom:x, int_literal, literal:Num
            return 0 # falsey_literal:0, if_elif_branch, int_literal, literal:Num, return:0
        elif y == 0: # comparison_operator:Eq, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:y, int_literal, literal:Num
            return 1 # if_elif_branch, int_literal, literal:Num, return:1

# ----------------------------------------------------------------------------------------
# ../Python/maths/least_common_multiple.py
# ----------------------------------------------------------------------------------------
import unittest # import:unittest, import_module:unittest, lines_of_code:25 (-> +24)
def find_lcm(first_num: int, second_num: int) -> int: # function:find_lcm (-> +5), function_argument:first_num, function_argument:second_num, function_argument_flavor:arg, function_returning_something:find_lcm (-> +5)
    max_num = first_num if first_num >= second_num else second_num # assignment, assignment_lhs_identifier:max_num, assignment_rhs_atom:first_num, assignment_rhs_atom:second_num, comparison_operator:GtE, conditional_expression, single_assignment:max_num
    common_mult = max_num # assignment, assignment_lhs_identifier:common_mult, assignment_rhs_atom:max_num, single_assignment:common_mult
    while (common_mult % first_num > 0) or (common_mult % second_num > 0): # binary_operator:Mod, boolean_operator:Or, comparison_operator:Gt, falsey_literal:0, int_literal, literal:Num, loop:while (-> +1), while (-> +1)
        common_mult += max_num # assignment_lhs_identifier:common_mult, assignment_rhs_atom:max_num, augmented_assignment:Add, variable_update:common_mult:max_num, variable_update_by_augmented_assignment:common_mult:max_num
    return common_mult # return:common_mult
class TestLeastCommonMultiple(unittest.TestCase): # class:TestLeastCommonMultiple (-> +17)
    test_inputs = [ # assignment, assignment_lhs_identifier:test_inputs, literal:List, single_assignment:test_inputs
        (10, 20), # assignment_rhs_atom:10, assignment_rhs_atom:20, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (13, 15), # assignment_rhs_atom:13, assignment_rhs_atom:15, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (4, 31), # assignment_rhs_atom:31, assignment_rhs_atom:4, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (10, 42), # assignment_rhs_atom:10, assignment_rhs_atom:42, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (43, 34), # assignment_rhs_atom:34, assignment_rhs_atom:43, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (5, 12), # assignment_rhs_atom:12, assignment_rhs_atom:5, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (12, 25), # assignment_rhs_atom:12, assignment_rhs_atom:25, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (10, 25), # assignment_rhs_atom:10, assignment_rhs_atom:25, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
        (6, 9), # assignment_rhs_atom:6, assignment_rhs_atom:9, int_literal, literal:Num, literal:Tuple, suggest_constant_definition
    ]
    expected_results = [20, 195, 124, 210, 1462, 60, 300, 50, 18] # assignment, assignment_lhs_identifier:expected_results, assignment_rhs_atom:124, assignment_rhs_atom:1462, assignment_rhs_atom:18, assignment_rhs_atom:195, assignment_rhs_atom:20, assignment_rhs_atom:210, assignment_rhs_atom:300, assignment_rhs_atom:50, assignment_rhs_atom:60, int_literal, literal:List, literal:Num, single_assignment:expected_results, suggest_constant_definition
    def test_lcm_function(self): # function:test_lcm_function (-> +4), function_argument:self, function_argument_flavor:arg, function_returning_nothing:test_lcm_function (-> +4), instance_method:test_lcm_function (-> +4), method:test_lcm_function (-> +4)
        for i, (first_num, second_num) in enumerate(self.test_inputs): # call_argument:, for:first_num (-> +3), for:i (-> +3), for:second_num (-> +3), for_indexes_elements (-> +3), function_call:enumerate, loop:for (-> +3)
            actual_result = find_lcm(first_num, second_num) # assignment, assignment_lhs_identifier:actual_result, assignment_rhs_atom:first_num, assignment_rhs_atom:second_num, call_argument:first_num, call_argument:second_num, function_call:find_lcm, single_assignment:actual_result
            with self.subTest(i=i): # method_call:subTest
                self.assertEqual(actual_result, self.expected_results[i]) # call_argument:, call_argument:actual_result, index:i, method_call:assertEqual, method_call_object:self

# ----------------------------------------------------------------------------------------
# ../Python/maths/lucas_series.py
# ----------------------------------------------------------------------------------------
def recur_luc(n): # body_recursive_function:recur_luc (-> +5), function:recur_luc (-> +5), function_argument:n, function_argument_flavor:arg, function_returning_something:recur_luc (-> +5), lines_of_code:6 (-> +5), recursive_function:recur_luc (-> +5)
    if n == 1: # comparison_operator:Eq, if (-> +1), if_test_atom:1, if_test_atom:n, int_literal, literal:Num
        return n # if_then_branch, return:n
    if n == 0: # comparison_operator:Eq, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:n, int_literal, literal:Num
        return 2 # if_then_branch, int_literal, literal:Num, return:2
    return recur_luc(n - 1) + recur_luc(n - 2) # binary_operator:Add, binary_operator:Sub, call_argument:, function_call:recur_luc, int_literal, literal:Num, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/matrix_exponentiation.py
# ----------------------------------------------------------------------------------------
import timeit # import:timeit, import_module:timeit, lines_of_code:67 (-> +66)
class Matrix(object): # class:Matrix (-> +14)
    def __init__(self, arg): # function:__init__ (-> +6), function_argument:arg, function_argument:self, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +6), instance_method:__init__ (-> +6), method:__init__ (-> +6)
        if isinstance(arg, list): # call_argument:arg, call_argument:list, function_call:isinstance, if (-> +5), if_test_atom:arg, if_test_atom:list
            self.t = arg # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:arg, if_then_branch (-> +1)
            self.n = len(arg) # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:arg, call_argument:arg, function_call:len
        else:
            self.n = arg # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:arg, if_else_branch (-> +1)
            self.t = [[0 for _ in range(self.n)] for _ in range(self.n)] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:0, assignment_rhs_atom:_, assignment_rhs_atom:self, call_argument:, comprehension:List, comprehension_for_count:1, falsey_literal:0, function_call:range, int_literal, literal:Num, range:_, variable_update:self:0, variable_update:self:_, variable_update_by_assignment:self:0, variable_update_by_assignment:self:_
    def __mul__(self, b): # function:__mul__ (-> +6), function_argument:b, function_argument:self, function_argument_flavor:arg, function_returning_something:__mul__ (-> +6), instance_method:__mul__ (-> +6), method:__mul__ (-> +6)
        matrix = Matrix(self.n) # assignment, assignment_lhs_identifier:matrix, assignment_rhs_atom:self, call_argument:, function_call:Matrix, single_assignment:matrix
        for i in range(self.n): # call_argument:, for:i (-> +3), for_range:_ (-> +3), function_call:range, loop:for (-> +3), range:_, square_nested_for (-> +3)
            for j in range(self.n): # call_argument:, for:j (-> +2), for_range:_ (-> +2), function_call:range, loop:for (-> +2), nested_for:1 (-> +2), range:_, square_nested_for (-> +2)
                for k in range(self.n): # call_argument:, for:k (-> +1), for_range:_ (-> +1), function_call:range, loop:for (-> +1), nested_for:2 (-> +1), range:_
                    matrix.t[i][j] += self.t[i][k] * b.t[k][j] # assignment_rhs_atom:b, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:k, assignment_rhs_atom:self, augmented_assignment:Add, binary_operator:Mult, index:i, index:j, index:k
        return matrix # return:matrix
def modular_exponentiation(a, b): # function:modular_exponentiation (-> +7), function_argument:a, function_argument:b, function_argument_flavor:arg, function_returning_something:modular_exponentiation (-> +7)
    matrix = Matrix([[1, 0], [0, 1]]) # assignment, assignment_lhs_identifier:matrix, assignment_rhs_atom:0, assignment_rhs_atom:1, call_argument:, falsey_literal:0, function_call:Matrix, int_literal, literal:List, literal:Num, single_assignment:matrix
    while b > 0: # comparison_operator:Gt, evolve_state (-> +4), falsey_literal:0, int_literal, literal:Num, loop:while (-> +4), while (-> +4)
        if b & 1: # binary_operator:BitAnd, if (-> +1), if_test_atom:1, if_test_atom:b, int_literal, literal:Num
            matrix *= a # assignment_lhs_identifier:matrix, assignment_rhs_atom:a, augmented_assignment:Mult, if_then_branch, variable_update:matrix:a, variable_update_by_augmented_assignment:matrix:a
        a *= a # assignment_lhs_identifier:a, assignment_rhs_atom:a, augmented_assignment:Mult, variable_update:a:a, variable_update_by_augmented_assignment:a:a
        b >>= 1 # assignment_lhs_identifier:b, assignment_rhs_atom:1, augmented_assignment:RShift, int_literal, literal:Num, variable_update:b:1, variable_update_by_augmented_assignment:b:1
    return matrix # return:matrix
def fibonacci_with_matrix_exponentiation(n, f1, f2): # function:fibonacci_with_matrix_exponentiation (-> +7), function_argument:f1, function_argument:f2, function_argument:n, function_argument_flavor:arg, function_returning_something:fibonacci_with_matrix_exponentiation (-> +7)
    if n == 1: # comparison_operator:Eq, if (-> +3), if_test_atom:1, if_test_atom:n, int_literal, literal:Num
        return f1 # if_then_branch, return:f1
    elif n == 2: # comparison_operator:Eq, if (-> +1), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        return f2 # if_elif_branch, return:f2
    matrix = Matrix([[1, 1], [1, 0]]) # assignment, assignment_lhs_identifier:matrix, assignment_rhs_atom:0, assignment_rhs_atom:1, call_argument:, falsey_literal:0, function_call:Matrix, int_literal, literal:List, literal:Num, single_assignment:matrix
    matrix = modular_exponentiation(matrix, n - 2) # assignment, assignment_lhs_identifier:matrix, assignment_rhs_atom:2, assignment_rhs_atom:matrix, assignment_rhs_atom:n, binary_operator:Sub, call_argument:, call_argument:matrix, function_call:modular_exponentiation, int_literal, literal:Num, single_assignment:matrix, variable_update:matrix:2, variable_update:matrix:n, variable_update_by_assignment:matrix:2, variable_update_by_assignment:matrix:n
    return f2 * matrix.t[0][0] + f1 * matrix.t[0][1] # binary_operator:Add, binary_operator:Mult, falsey_literal:0, index:0, index:1, int_literal, literal:Num, return
def simple_fibonacci(n, f1, f2): # function:simple_fibonacci (-> +11), function_argument:f1, function_argument:f2, function_argument:n, function_argument_flavor:arg, function_returning_something:simple_fibonacci (-> +11)
    if n == 1: # comparison_operator:Eq, if (-> +3), if_test_atom:1, if_test_atom:n, int_literal, literal:Num
        return f1 # if_then_branch, return:f1
    elif n == 2: # comparison_operator:Eq, if (-> +1), if_test_atom:2, if_test_atom:n, int_literal, literal:Num
        return f2 # if_elif_branch, return:f2
    fn_1 = f1 # assignment, assignment_lhs_identifier:fn_1, assignment_rhs_atom:f1, single_assignment:fn_1
    fn_2 = f2 # assignment, assignment_lhs_identifier:fn_2, assignment_rhs_atom:f2, single_assignment:fn_2
    n -= 2 # assignment_lhs_identifier:n, assignment_rhs_atom:2, augmented_assignment:Sub, int_literal, literal:Num, variable_update:n:2, variable_update_by_augmented_assignment:n:2
    while n > 0: # comparison_operator:Gt, evolve_state (-> +2), falsey_literal:0, int_literal, literal:Num, loop:while (-> +2), while (-> +2)
        fn_1, fn_2 = fn_1 + fn_2, fn_1 # assignment, assignment_lhs_identifier:fn_1, assignment_lhs_identifier:fn_2, assignment_rhs_atom:fn_1, assignment_rhs_atom:fn_2, binary_operator:Add, variable_update:fn_1:fn_2, variable_update:fn_2:fn_1, variable_update_by_assignment:fn_1:fn_2, variable_update_by_assignment:fn_2:fn_1
        n -= 1 # assignment_lhs_identifier:n, assignment_rhs_atom:1, augmented_assignment:Sub, int_literal, literal:Num, variable_update:n:1, variable_update_by_augmented_assignment:n:1
    return fn_1 # return:fn_1
def matrix_exponentiation_time(): # function:matrix_exponentiation_time (-> +8), function_returning_something:matrix_exponentiation_time (-> +8), function_without_arguments:matrix_exponentiation_time (-> +8)
    setup = """ # assignment, assignment_lhs_identifier:setup, single_assignment:setup
from random import randint
from __main__ import fibonacci_with_matrix_exponentiation
""" # literal:Str
    code = "fibonacci_with_matrix_exponentiation(randint(1,70000), 1, 1)" # assignment, assignment_lhs_identifier:code, literal:Str, single_assignment:code
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100) # assignment, assignment_lhs_identifier:exec_time, assignment_rhs_atom:100, assignment_rhs_atom:code, assignment_rhs_atom:setup, assignment_rhs_atom:timeit, int_literal, literal:Num, method_call:timeit, single_assignment:exec_time, suggest_constant_definition
    print("With matrix exponentiation the average execution time is ", exec_time / 100) # binary_operator:Div, call_argument:, function_call:print, int_literal, literal:Num, literal:Str, suggest_constant_definition
    return exec_time # return:exec_time
def simple_fibonacci_time(): # function:simple_fibonacci_time (-> +10), function_returning_something:simple_fibonacci_time (-> +10), function_without_arguments:simple_fibonacci_time (-> +10)
    setup = """ # assignment, assignment_lhs_identifier:setup, single_assignment:setup
from random import randint
from __main__ import simple_fibonacci
""" # literal:Str
    code = "simple_fibonacci(randint(1,70000), 1, 1)" # assignment, assignment_lhs_identifier:code, literal:Str, single_assignment:code
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100) # assignment, assignment_lhs_identifier:exec_time, assignment_rhs_atom:100, assignment_rhs_atom:code, assignment_rhs_atom:setup, assignment_rhs_atom:timeit, int_literal, literal:Num, method_call:timeit, single_assignment:exec_time, suggest_constant_definition
    print( # function_call:print
        "Without matrix exponentiation the average execution time is ", exec_time / 100 # binary_operator:Div, call_argument:, int_literal, literal:Num, literal:Str, suggest_constant_definition
    )
    return exec_time # return:exec_time
def main(): # function:main (-> +2), function_returning_nothing:main (-> +2), function_without_arguments:main (-> +2)
    matrix_exponentiation_time() # function_call:matrix_exponentiation_time, function_call_without_arguments:matrix_exponentiation_time
    simple_fibonacci_time() # function_call:simple_fibonacci_time, function_call_without_arguments:simple_fibonacci_time

# ----------------------------------------------------------------------------------------
# ../Python/maths/mobius_function.py
# ----------------------------------------------------------------------------------------
from maths.prime_factors import prime_factors # import:maths.prime_factors:prime_factors, import_module:maths.prime_factors, import_name:prime_factors, lines_of_code:7 (-> +6)
from maths.is_square_free import is_square_free # import:maths.is_square_free:is_square_free, import_module:maths.is_square_free, import_name:is_square_free
def mobius(n: int) -> int: # function:mobius (-> +4), function_argument:n, function_argument_flavor:arg, function_returning_something:mobius (-> +4)
    factors = prime_factors(n) # assignment, assignment_lhs_identifier:factors, assignment_rhs_atom:n, call_argument:n, function_call:prime_factors, single_assignment:factors
    if is_square_free(factors): # call_argument:factors, function_call:is_square_free, if (-> +1), if_test_atom:factors
        return -1 if len(factors) % 2 else 1 # binary_operator:Mod, call_argument:factors, conditional_expression, function_call:len, if_then_branch, int_literal, literal:Num, return
    return 0 # falsey_literal:0, int_literal, literal:Num, return:0

# ----------------------------------------------------------------------------------------
# ../Python/maths/modular_exponential.py
# ----------------------------------------------------------------------------------------
def modular_exponential(base, power, mod): # function:modular_exponential (-> +10), function_argument:base, function_argument:mod, function_argument:power, function_argument_flavor:arg, function_returning_something:modular_exponential (-> +10), lines_of_code:13 (-> +12)
    if power < 0: # comparison_operator:Lt, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:power, int_literal, literal:Num
        return -1 # if_then_branch, int_literal, literal:Num, return:-1
    base %= mod # assignment_lhs_identifier:base, assignment_rhs_atom:mod, augmented_assignment:Mod, variable_update:base:mod, variable_update_by_augmented_assignment:base:mod
    result = 1 # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:result
    while power > 0: # comparison_operator:Gt, evolve_state (-> +4), falsey_literal:0, int_literal, literal:Num, loop:while (-> +4), while (-> +4)
        if power & 1: # binary_operator:BitAnd, if (-> +1), if_test_atom:1, if_test_atom:power, int_literal, literal:Num
            result = (result * base) % mod # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:base, assignment_rhs_atom:mod, assignment_rhs_atom:result, binary_operator:Mod, binary_operator:Mult, if_then_branch, single_assignment:result, variable_update:result:base, variable_update:result:mod, variable_update_by_assignment:result:base, variable_update_by_assignment:result:mod
        power = power >> 1 # assignment, assignment_lhs_identifier:power, assignment_rhs_atom:1, assignment_rhs_atom:power, binary_operator:RShift, int_literal, literal:Num, single_assignment:power, suggest_augmented_assignment, variable_update:power:1, variable_update_by_assignment:power:1
        base = (base * base) % mod # assignment, assignment_lhs_identifier:base, assignment_rhs_atom:base, assignment_rhs_atom:mod, binary_operator:Mod, binary_operator:Mult, single_assignment:base, variable_update:base:mod, variable_update_by_assignment:base:mod
    return result # return:result
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    print(modular_exponential(3, 200, 13)) # call_argument:, call_argument:13, call_argument:200, call_argument:3, composition, function_call:modular_exponential, function_call:print, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/newton_raphson.py
# ----------------------------------------------------------------------------------------
import math as m # import:math, import_module:math, lines_of_code:21 (-> +20)
def calc_derivative(f, a, h=0.001): # float_literal, function:calc_derivative (-> +1), function_argument:a, function_argument:f, function_argument:h, function_argument_flavor:arg, function_returning_something:calc_derivative (-> +1), literal:Num
    return (f(a + h) - f(a - h)) / (2 * h) # binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, function_call:f, int_literal, literal:Num, return
def newton_raphson(f, x0=0, maxiter=100, step=0.0001, maxerror=1e-6, logsteps=False): # falsey_literal:0, falsey_literal:False, float_literal, function:newton_raphson (-> +17), function_argument:f, function_argument:logsteps, function_argument:maxerror, function_argument:maxiter, function_argument:step, function_argument:x0, function_argument_flavor:arg, function_returning_something:newton_raphson (-> +17), int_literal, literal:False, literal:Num
    a = x0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:x0, single_assignment:a
    steps = [a] # assignment, assignment_lhs_identifier:steps, assignment_rhs_atom:a, single_assignment:steps
    error = abs(f(a)) # assignment, assignment_lhs_identifier:error, assignment_rhs_atom:a, call_argument:, call_argument:a, composition, function_call:abs, function_call:f, single_assignment:error
    f1 = lambda x: calc_derivative(f, x, h=step) # assignment, assignment_lhs_identifier:f1, assignment_rhs_atom:f, assignment_rhs_atom:step, assignment_rhs_atom:x, call_argument:f, call_argument:x, function_argument:x, function_argument_flavor:arg, function_call:calc_derivative, lambda_function, single_assignment:f1
    for _ in range(maxiter): # call_argument:maxiter, for:_ (-> +9), for_range:maxiter (-> +9), for_with_early_exit:break (-> +9), for_with_else (-> +9), function_call:range, loop:for (-> +9), range:maxiter
        if f1(a) == 0: # call_argument:a, comparison_operator:Eq, falsey_literal:0, function_call:f1, if (-> +1), if_test_atom:0, if_test_atom:a, int_literal, literal:Num
            raise ValueError("No converging solution found") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
        a = a - f(a) / f1(a) # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:a, binary_operator:Div, binary_operator:Sub, call_argument:a, function_call:f, function_call:f1, single_assignment:a, suggest_augmented_assignment
        if logsteps: # if (-> +1)
            steps.append(a) # call_argument:a, if_then_branch, method_call:append, method_call_object:steps, variable_update:steps:a, variable_update_by_method_call:steps:a
        if error < maxerror: # comparison_operator:Lt, if (-> +1), if_test_atom:error, if_test_atom:maxerror
            break # break, if_then_branch
    else:
        raise ValueError("Iteration limit reached, no converging solution found") # call_argument:, function_call:ValueError, literal:Str, loop_else, raise:ValueError
    if logsteps: # if (-> +1)
        return a, error, steps # if_then_branch, return
    return a, error # return

# ----------------------------------------------------------------------------------------
# ../Python/maths/perfect_square.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, lines_of_code:3 (-> +2)
def perfect_square(num: int) -> bool: # function:perfect_square (-> +1), function_argument:num, function_argument_flavor:arg, function_returning_something:perfect_square (-> +1)
    return math.sqrt(num) * math.sqrt(num) == num # binary_operator:Mult, call_argument:num, comparison_operator:Eq, method_call:sqrt, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/polynomial_evaluation.py
# ----------------------------------------------------------------------------------------
from typing import Sequence # import:typing:Sequence, import_module:typing, import_name:Sequence, lines_of_code:8 (-> +7)
def evaluate_poly(poly: Sequence[float], x: float) -> float: # function:evaluate_poly (-> +1), function_argument:poly, function_argument:x, function_argument_flavor:arg, function_returning_something:evaluate_poly (-> +1)
    return sum(c * (x ** i) for i, c in enumerate(poly)) # binary_operator:Mult, binary_operator:Pow, call_argument:, call_argument:poly, composition, comprehension:Generator, comprehension_for_count:1, function_call:enumerate, function_call:sum, function_tail_call:sum, return
def horner(poly: Sequence[float], x: float) -> float: # function:horner (-> +4), function_argument:poly, function_argument:x, function_argument_flavor:arg, function_returning_something:horner (-> +4)
    result = 0.0 # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:0.0, falsey_literal:0.0, float_literal, literal:Num, single_assignment:result, suggest_constant_definition
    for coeff in reversed(poly): # accumulate_all_elements:result (-> +1), accumulate_elements:result (-> +1), call_argument:poly, for:coeff (-> +1), function_call:reversed, loop:for (-> +1)
        result = result * x + coeff # assignment, assignment_lhs_identifier:result, assignment_rhs_atom:coeff, assignment_rhs_atom:result, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, single_assignment:result, variable_update:result:coeff, variable_update:result:x, variable_update_by_assignment:result:coeff, variable_update_by_assignment:result:x
    return result # return:result

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_check.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, lines_of_code:36 (-> +35)
import unittest # import:unittest, import_module:unittest
def prime_check(number): # function:prime_check (-> +8), function_argument:number, function_argument_flavor:arg, function_returning_something:prime_check (-> +8)
    if number < 2: # comparison_operator:Lt, if (-> +1), if_test_atom:2, if_test_atom:number, int_literal, literal:Num
        return False # falsey_literal:False, if_then_branch, literal:False, return:False
    if number < 4: # comparison_operator:Lt, if (-> +1), if_test_atom:4, if_test_atom:number, int_literal, literal:Num, suggest_constant_definition
        return True # if_then_branch, literal:True, return:True
    if number % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:number, int_literal, literal:Num
        return False # falsey_literal:False, if_then_branch, literal:False, return:False
    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2) # assignment, assignment_lhs_identifier:odd_numbers, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:math, assignment_rhs_atom:number, binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:number, composition, function_call:int, function_call:range, int_literal, literal:Num, method_call:sqrt, range:3:_:2, single_assignment:odd_numbers, suggest_constant_definition
    return not any(number % i == 0 for i in odd_numbers) # binary_operator:Mod, call_argument:, comparison_operator:Eq, comprehension:Generator, comprehension_for_count:1, divisibility_test, falsey_literal:0, function_call:any, int_literal, literal:Num, return, unary_operator:Not
class Test(unittest.TestCase): # class:Test (-> +24)
    def test_primes(self): # function:test_primes (-> +10), function_argument:self, function_argument_flavor:arg, function_returning_nothing:test_primes (-> +10), instance_method:test_primes (-> +10), method:test_primes (-> +10)
        self.assertTrue(prime_check(2)) # call_argument:, call_argument:2, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self
        self.assertTrue(prime_check(3)) # call_argument:, call_argument:3, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(5)) # call_argument:, call_argument:5, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(7)) # call_argument:, call_argument:7, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(11)) # call_argument:, call_argument:11, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(13)) # call_argument:, call_argument:13, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(17)) # call_argument:, call_argument:17, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(19)) # call_argument:, call_argument:19, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(23)) # call_argument:, call_argument:23, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self, suggest_constant_definition
        self.assertTrue(prime_check(29)) # call_argument:, call_argument:29, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertTrue, method_call_object:self, suggest_constant_definition
    def test_not_primes(self): # function:test_not_primes (-> +12), function_argument:self, function_argument_flavor:arg, function_returning_nothing:test_not_primes (-> +12), instance_method:test_not_primes (-> +12), method:test_not_primes (-> +12)
        self.assertFalse(prime_check(-19), "Negative numbers are not prime.") # call_argument:, call_argument:-19, composition, function_call:prime_check, int_literal, literal:Num, literal:Str, method_call:assertFalse, method_call_object:self, suggest_constant_definition
        self.assertFalse( # composition, method_call:assertFalse, method_call_object:self
            prime_check(0), "Zero doesn't have any divider, primes must have two" # call_argument:, call_argument:0, falsey_literal:0, function_call:prime_check, int_literal, literal:Num, literal:Str
        )
        self.assertFalse( # composition, method_call:assertFalse, method_call_object:self
            prime_check(1), "One just have 1 divider, primes must have two." # call_argument:, call_argument:1, function_call:prime_check, int_literal, literal:Num, literal:Str
        )
        self.assertFalse(prime_check(2 * 2)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse, method_call_object:self
        self.assertFalse(prime_check(2 * 3)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse, method_call_object:self, suggest_constant_definition
        self.assertFalse(prime_check(3 * 3)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse, method_call_object:self, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse, method_call_object:self, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5 * 7)) # binary_operator:Mult, call_argument:, composition, function_call:prime_check, int_literal, literal:Num, method_call:assertFalse, method_call_object:self, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_factors.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List, lines_of_code:13 (-> +12)
def prime_factors(n: int) -> List[int]: # function:prime_factors (-> +11), function_argument:n, function_argument_flavor:arg, function_returning_something:prime_factors (-> +11), index:int
    i = 2 # assignment, assignment_lhs_identifier:i, assignment_rhs_atom:2, int_literal, literal:Num, single_assignment:i
    factors = [] # assignment, assignment_lhs_identifier:factors, falsey_literal:List, literal:List, single_assignment:factors
    while i * i <= n: # binary_operator:Mult, comparison_operator:LtE, evolve_state (-> +5), loop:while (-> +5), while (-> +5)
        if n % i: # binary_operator:Mod, if (-> +4), if_test_atom:i, if_test_atom:n
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, int_literal, literal:Num, variable_increment:i, variable_update:i:1, variable_update_by_augmented_assignment:i:1
        else:
            n //= i # assignment_lhs_identifier:n, assignment_rhs_atom:i, augmented_assignment:FloorDiv, if_else_branch (-> +1), variable_update:n:i, variable_update_by_augmented_assignment:n:i
            factors.append(i) # call_argument:i, method_call:append, method_call_object:factors, variable_update:factors:i, variable_update_by_method_call:factors:i
    if n > 1: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:n, int_literal, literal:Num
        factors.append(n) # call_argument:n, if_then_branch, method_call:append, method_call_object:factors, variable_update:factors:n, variable_update_by_method_call:factors:n
    return factors # return:factors

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_numbers.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List, lines_of_code:11 (-> +10)
def primes(max: int) -> List[int]: # function:primes (-> +9), function_argument:max, function_argument_flavor:arg, function_returning_something:primes (-> +9), index:int
    max += 1 # assignment_lhs_identifier:max, assignment_rhs_atom:1, augmented_assignment:Add, int_literal, literal:Num, variable_increment:max, variable_update:max:1, variable_update_by_augmented_assignment:max:1
    numbers = [False] * max # assignment, assignment_lhs_identifier:numbers, assignment_rhs_atom:False, assignment_rhs_atom:max, binary_operator:Mult, falsey_literal:False, literal:False, literal:List, replication_operator:List, single_assignment:numbers
    ret = [] # assignment, assignment_lhs_identifier:ret, falsey_literal:List, literal:List, single_assignment:ret
    for i in range(2, max): # accumulate_elements:ret (-> +4), accumulate_some_elements:ret (-> +4), call_argument:2, call_argument:max, for:i (-> +4), for_range:2:max (-> +4), for_range:i:max:i (-> +4), function_call:range, int_literal, literal:Num, loop:for (-> +4), range:2:max
        if not numbers[i]: # if (-> +3), if_test_atom:i, if_test_atom:numbers, index:i, unary_operator:Not
            for j in range(i, max, i): # call_argument:i, call_argument:max, for:j (-> +1), for_range:i:max:i (-> +1), function_call:range, if_then_branch (-> +2), loop:for (-> +1), nested_for:1 (-> +1), range:i:max:i
                numbers[j] = True # assignment, assignment_lhs_identifier:numbers, assignment_rhs_atom:True, index:j, literal:True
            ret.append(i) # call_argument:i, method_call:append, method_call_object:ret, variable_update:ret:i, variable_update_by_method_call:ret:i
    return ret # return:ret

# ----------------------------------------------------------------------------------------
# ../Python/maths/prime_sieve_eratosthenes.py
# ----------------------------------------------------------------------------------------
def prime_sieve_eratosthenes(num): # function:prime_sieve_eratosthenes (-> +10), function_argument:num, function_argument_flavor:arg, function_returning_nothing:prime_sieve_eratosthenes (-> +10), lines_of_code:11 (-> +10)
    primes = [True for i in range(num + 1)] # assignment, assignment_lhs_identifier:primes, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:i, assignment_rhs_atom:num, binary_operator:Add, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, int_literal, literal:Num, literal:True, range:_, single_assignment:primes
    p = 2 # assignment, assignment_lhs_identifier:p, assignment_rhs_atom:2, int_literal, literal:Num, single_assignment:p
    while p * p <= num: # binary_operator:Mult, comparison_operator:LtE, loop:while (-> +4), while (-> +4)
        if primes[p] == True: # comparison_operator:Eq, if (-> +2), if_test_atom:True, if_test_atom:p, if_test_atom:primes, index:p, literal:True
            for i in range(p * p, num + 1, p): # binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:p, for:i (-> +1), for_range:_:_:p (-> +1), function_call:range, if_then_branch (-> +1), int_literal, literal:Num, loop:for (-> +1), range:_:_:p
                primes[i] = False # assignment, assignment_lhs_identifier:primes, assignment_rhs_atom:False, falsey_literal:False, index:i, literal:False
        p += 1 # assignment_lhs_identifier:p, assignment_rhs_atom:1, augmented_assignment:Add, int_literal, literal:Num, variable_increment:p, variable_update:p:1, variable_update_by_augmented_assignment:p:1
    for prime in range(2, num + 1): # binary_operator:Add, call_argument:, call_argument:2, for:prime (-> +2), for_range:2:_ (-> +2), function_call:range, int_literal, literal:Num, loop:for (-> +2), range:2:_
        if primes[prime]: # if (-> +1), if_test_atom:prime, if_test_atom:primes, index:prime
            print(prime, end=" ") # call_argument:prime, function_call:print, if_then_branch, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/qr_decomposition.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, lines_of_code:18 (-> +17)
def qr_householder(A): # function:qr_householder (-> +16), function_argument:A, function_argument_flavor:arg, function_returning_something:qr_householder (-> +16)
    m, n = A.shape # assignment, assignment_lhs_identifier:m, assignment_lhs_identifier:n, assignment_rhs_atom:A
    t = min(m, n) # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:m, assignment_rhs_atom:n, call_argument:m, call_argument:n, function_call:min, single_assignment:t
    Q = np.eye(m) # assignment, assignment_lhs_identifier:Q, assignment_rhs_atom:m, assignment_rhs_atom:np, call_argument:m, method_call:eye, single_assignment:Q
    R = A.copy() # assignment, assignment_lhs_identifier:R, assignment_rhs_atom:A, method_call:copy, single_assignment:R
    for k in range(t - 1): # accumulate_all_elements:Q_k (-> +10), accumulate_elements:Q_k (-> +10), binary_operator:Sub, call_argument:, for:k (-> +10), for_range:_ (-> +10), function_call:range, int_literal, literal:Num, loop:for (-> +10), range:_
        x = R[k:, [k]] # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:R, assignment_rhs_atom:k, single_assignment:x
        e1 = np.zeros_like(x) # assignment, assignment_lhs_identifier:e1, assignment_rhs_atom:np, assignment_rhs_atom:x, call_argument:x, method_call:zeros_like, single_assignment:e1
        e1[0] = 1.0 # assignment, assignment_lhs_identifier:e1, assignment_rhs_atom:1.0, falsey_literal:0, float_literal, index:0, int_literal, literal:Num, suggest_constant_definition
        alpha = np.linalg.norm(x) # assignment, assignment_lhs_identifier:alpha, assignment_rhs_atom:np, assignment_rhs_atom:x, call_argument:x, method_call:norm, single_assignment:alpha
        v = x + np.sign(x[0]) * alpha * e1 # assignment, assignment_lhs_identifier:v, assignment_rhs_atom:0, assignment_rhs_atom:alpha, assignment_rhs_atom:e1, assignment_rhs_atom:np, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, call_argument:, falsey_literal:0, index:0, int_literal, literal:Num, method_call:sign, single_assignment:v
        v /= np.linalg.norm(v) # assignment_lhs_identifier:v, assignment_rhs_atom:np, assignment_rhs_atom:v, augmented_assignment:Div, call_argument:v, method_call:norm, variable_update:v:np, variable_update:v:v, variable_update_by_augmented_assignment:v:np, variable_update_by_augmented_assignment:v:v
        Q_k = np.eye(m - k) - 2.0 * v @ v.T # assignment, assignment_lhs_identifier:Q_k, assignment_rhs_atom:2.0, assignment_rhs_atom:k, assignment_rhs_atom:m, assignment_rhs_atom:np, assignment_rhs_atom:v, binary_operator:MatMult, binary_operator:Mult, binary_operator:Sub, call_argument:, float_literal, literal:Num, method_call:eye, single_assignment:Q_k, suggest_constant_definition
        Q_k = np.block([[np.eye(k), np.zeros((k, m - k))], [np.zeros((m - k, k)), Q_k]]) # assignment, assignment_lhs_identifier:Q_k, assignment_rhs_atom:Q_k, assignment_rhs_atom:k, assignment_rhs_atom:m, assignment_rhs_atom:np, binary_operator:Sub, call_argument:, call_argument:k, composition, method_call:block, method_call:eye, method_call:zeros, single_assignment:Q_k, variable_update:Q_k:k, variable_update:Q_k:m, variable_update:Q_k:np, variable_update_by_assignment:Q_k:k, variable_update_by_assignment:Q_k:m, variable_update_by_assignment:Q_k:np
        Q = Q @ Q_k.T # assignment, assignment_lhs_identifier:Q, assignment_rhs_atom:Q, assignment_rhs_atom:Q_k, binary_operator:MatMult, single_assignment:Q, suggest_augmented_assignment, variable_update:Q:Q_k, variable_update_by_assignment:Q:Q_k
        R = Q_k @ R # assignment, assignment_lhs_identifier:R, assignment_rhs_atom:Q_k, assignment_rhs_atom:R, binary_operator:MatMult, single_assignment:R, variable_update:R:Q_k, variable_update_by_assignment:R:Q_k
    return Q, R # return

# ----------------------------------------------------------------------------------------
# ../Python/maths/quadratic_equations_complex_numbers.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt, lines_of_code:16 (-> +15)
from typing import Tuple # import:typing:Tuple, import_module:typing, import_name:Tuple
def QuadraticEquation(a: int, b: int, c: int) -> Tuple[str, str]: # function:QuadraticEquation (-> +10), function_argument:a, function_argument:b, function_argument:c, function_argument_flavor:arg, function_returning_something:QuadraticEquation (-> +10), index:_
    if a == 0: # comparison_operator:Eq, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:a, int_literal, literal:Num
        raise ValueError("Coefficient 'a' must not be zero for quadratic equations.") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    delta = b * b - 4 * a * c # assignment, assignment_lhs_identifier:delta, assignment_rhs_atom:4, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:c, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, single_assignment:delta, suggest_constant_definition
    if delta >= 0: # comparison_operator:GtE, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:delta, int_literal, literal:Num
        return str((-b + sqrt(delta)) / (2 * a)), str((-b - sqrt(delta)) / (2 * a)) # binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:delta, composition, function_call:sqrt, function_call:str, if_then_branch, int_literal, literal:Num, return, unary_operator:USub
    snd = sqrt(-delta) # assignment, assignment_lhs_identifier:snd, assignment_rhs_atom:delta, call_argument:, function_call:sqrt, single_assignment:snd, unary_operator:USub
    if b == 0: # comparison_operator:Eq, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:b, int_literal, literal:Num
        return f"({snd} * i) / 2", f"({snd} * i) / {2 * a}" # binary_operator:Mult, if_then_branch, int_literal, literal:Num, literal:Str, return
    b = -abs(b) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:b, call_argument:b, function_call:abs, single_assignment:b, unary_operator:USub
    return f"({b}+{snd} * i) / 2", f"({b}+{snd} * i) / {2 * a}" # binary_operator:Mult, int_literal, literal:Num, literal:Str, return
def main(): # function:main (-> +2), function_returning_nothing:main (-> +2), function_without_arguments:main (-> +2)
    solutions = QuadraticEquation(a=5, b=6, c=1) # assignment, assignment_lhs_identifier:solutions, assignment_rhs_atom:1, assignment_rhs_atom:5, assignment_rhs_atom:6, function_call:QuadraticEquation, int_literal, literal:Num, single_assignment:solutions, suggest_constant_definition
    print("The equation solutions are: {} and {}".format(*solutions)) # call_argument:, composition, function_call:print, literal:Str, method_call:format

# ----------------------------------------------------------------------------------------
# ../Python/maths/radix2_fft.py
# ----------------------------------------------------------------------------------------
import mpmath # import:mpmath, import_module:mpmath, lines_of_code:92 (-> +91)
import numpy as np # import:numpy, import_module:numpy
class FFT: # class:FFT (-> +89)
    def __init__(self, polyA=[0], polyB=[0]): # falsey_literal:0, function:__init__ (-> +17), function_argument:polyA, function_argument:polyB, function_argument:self, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +17), instance_method:__init__ (-> +17), int_literal, literal:List, literal:Num, method:__init__ (-> +17)
        self.polyA = list(polyA)[:] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:polyA, call_argument:polyA, function_call:list, slice:::, slice_lower:, slice_step:, slice_upper:
        self.polyB = list(polyB)[:] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:polyB, call_argument:polyB, function_call:list, slice:::, slice_lower:, slice_step:, slice_upper:
        while self.polyA[-1] == 0: # comparison_operator:Eq, evolve_state (-> +1), falsey_literal:0, index:-1, int_literal, literal:Num, loop:while (-> +1), negative_index:-1, while (-> +1)
            self.polyA.pop() # method_call:pop
        self.len_A = len(self.polyA) # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:self, call_argument:, function_call:len
        while self.polyB[-1] == 0: # comparison_operator:Eq, evolve_state (-> +1), falsey_literal:0, index:-1, int_literal, literal:Num, loop:while (-> +1), negative_index:-1, while (-> +1)
            self.polyB.pop() # method_call:pop
        self.len_B = len(self.polyB) # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:self, call_argument:, function_call:len
        self.C_max_length = int( # assignment, assignment_lhs_identifier:self, composition, function_call:int, variable_update:self:1, variable_update:self:2, variable_update:self:np, variable_update_by_assignment:self:1, variable_update_by_assignment:self:2, variable_update_by_assignment:self:np
            2 ** np.ceil(np.log2(len(self.polyA) + len(self.polyB) - 1)) # assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:np, assignment_rhs_atom:self, binary_operator:Add, binary_operator:Pow, binary_operator:Sub, call_argument:, composition, function_call:len, int_literal, literal:Num, method_call:ceil, method_call:log2
        )
        while len(self.polyA) < self.C_max_length: # call_argument:, comparison_operator:Lt, evolve_state (-> +1), function_call:len, loop:while (-> +1), while (-> +1)
            self.polyA.append(0) # call_argument:0, falsey_literal:0, int_literal, literal:Num, method_call:append
        while len(self.polyB) < self.C_max_length: # call_argument:, comparison_operator:Lt, evolve_state (-> +1), function_call:len, loop:while (-> +1), while (-> +1)
            self.polyB.append(0) # call_argument:0, falsey_literal:0, int_literal, literal:Num, method_call:append
        self.root = complex(mpmath.root(x=1, n=self.C_max_length, k=1)) # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:1, assignment_rhs_atom:mpmath, assignment_rhs_atom:self, call_argument:, composition, function_call:complex, int_literal, literal:Num, method_call:root, variable_update:self:1, variable_update:self:mpmath, variable_update_by_assignment:self:1, variable_update_by_assignment:self:mpmath
        self.product = self.__multiply() # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:self, method_call:__multiply
    def __DFT(self, which): # function:__DFT (-> +23), function_argument:self, function_argument:which, function_argument_flavor:arg, function_returning_something:__DFT (-> +23), instance_method:__DFT (-> +23), method:__DFT (-> +23)
        if which == "A": # comparison_operator:Eq, if (-> +3), if_test_atom:which, literal:Str, suggest_conditional_expression (-> +3)
            dft = [[x] for x in self.polyA] # assignment, assignment_lhs_identifier:dft, assignment_rhs_atom:self, assignment_rhs_atom:x, comprehension:List, comprehension_for_count:1, if_then_branch, single_assignment:dft
        else:
            dft = [[x] for x in self.polyB] # assignment, assignment_lhs_identifier:dft, assignment_rhs_atom:self, assignment_rhs_atom:x, comprehension:List, comprehension_for_count:1, if_else_branch, single_assignment:dft
        if len(dft) <= 1: # call_argument:dft, comparison_operator:LtE, function_call:len, if (-> +1), if_test_atom:1, if_test_atom:dft, int_literal, literal:Num
            return dft[0] # falsey_literal:0, if_then_branch, index:0, int_literal, literal:Num, return
        next_ncol = self.C_max_length // 2 # assignment, assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, assignment_rhs_atom:self, binary_operator:FloorDiv, int_literal, literal:Num, single_assignment:next_ncol
        while next_ncol > 0: # comparison_operator:Gt, evolve_state (-> +14), falsey_literal:0, int_literal, literal:Num, loop:while (-> +14), while (-> +14)
            new_dft = [[] for i in range(next_ncol)] # assignment, assignment_lhs_identifier:new_dft, assignment_rhs_atom:i, assignment_rhs_atom:next_ncol, call_argument:next_ncol, comprehension:List, comprehension_for_count:1, falsey_literal:List, function_call:range, literal:List, range:next_ncol, single_assignment:new_dft
            root = self.root ** next_ncol # assignment, assignment_lhs_identifier:root, assignment_rhs_atom:next_ncol, assignment_rhs_atom:self, binary_operator:Pow, single_assignment:root
            current_root = 1 # assignment, assignment_lhs_identifier:current_root, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:current_root
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator:FloorDiv, binary_operator:Mult, call_argument:, for:j (-> +3), for_range:_ (-> +3), for_range:next_ncol (-> +3), function_call:range, int_literal, literal:Num, loop:for (-> +3), range:_
                for i in range(next_ncol): # call_argument:next_ncol, for:i (-> +1), for_range:next_ncol (-> +1), function_call:range, loop:for (-> +1), nested_for:1 (-> +1), range:next_ncol
                    new_dft[i].append(dft[i][j] + current_root * dft[i + next_ncol][j]) # binary_operator:Add, binary_operator:Mult, call_argument:, index:_, index:i, index:j, index_arithmetic, method_call:append
                current_root *= root # assignment_lhs_identifier:current_root, assignment_rhs_atom:root, augmented_assignment:Mult, variable_update:current_root:root, variable_update_by_augmented_assignment:current_root:root
            current_root = 1 # assignment, assignment_lhs_identifier:current_root, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:current_root
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator:FloorDiv, binary_operator:Mult, call_argument:, for:j (-> +3), for_range:_ (-> +3), for_range:next_ncol (-> +3), function_call:range, int_literal, literal:Num, loop:for (-> +3), range:_
                for i in range(next_ncol): # call_argument:next_ncol, for:i (-> +1), for_range:next_ncol (-> +1), function_call:range, loop:for (-> +1), nested_for:1 (-> +1), range:next_ncol
                    new_dft[i].append(dft[i][j] - current_root * dft[i + next_ncol][j]) # binary_operator:Add, binary_operator:Mult, binary_operator:Sub, call_argument:, index:_, index:i, index:j, index_arithmetic, method_call:append
                current_root *= root # assignment_lhs_identifier:current_root, assignment_rhs_atom:root, augmented_assignment:Mult, variable_update:current_root:root, variable_update_by_augmented_assignment:current_root:root
            dft = new_dft # assignment, assignment_lhs_identifier:dft, assignment_rhs_atom:new_dft, single_assignment:dft
            next_ncol = next_ncol // 2 # assignment, assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, assignment_rhs_atom:next_ncol, binary_operator:FloorDiv, int_literal, literal:Num, single_assignment:next_ncol, suggest_augmented_assignment, variable_update:next_ncol:2, variable_update_by_assignment:next_ncol:2
        return dft[0] # falsey_literal:0, index:0, int_literal, literal:Num, return
    def __multiply(self): # function:__multiply (-> +35), function_argument:self, function_argument_flavor:arg, function_returning_something:__multiply (-> +35), instance_method:__multiply (-> +35), method:__multiply (-> +35)
        dftA = self.__DFT("A") # assignment, assignment_lhs_identifier:dftA, assignment_rhs_atom:self, call_argument:, literal:Str, method_call:__DFT, single_assignment:dftA
        dftB = self.__DFT("B") # assignment, assignment_lhs_identifier:dftB, assignment_rhs_atom:self, call_argument:, literal:Str, method_call:__DFT, single_assignment:dftB
        inverseC = [[dftA[i] * dftB[i] for i in range(self.C_max_length)]] # assignment, assignment_lhs_identifier:inverseC, assignment_rhs_atom:dftA, assignment_rhs_atom:dftB, assignment_rhs_atom:i, assignment_rhs_atom:self, binary_operator:Mult, call_argument:, comprehension:List, comprehension_for_count:1, function_call:range, index:i, range:_, single_assignment:inverseC
        del dftA
        del dftB
        if len(inverseC[0]) <= 1: # call_argument:, comparison_operator:LtE, falsey_literal:0, function_call:len, if (-> +1), if_test_atom:0, if_test_atom:1, if_test_atom:inverseC, index:0, int_literal, literal:Num
            return inverseC[0] # falsey_literal:0, if_then_branch, index:0, int_literal, literal:Num, return
        next_ncol = 2 # assignment, assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, int_literal, literal:Num, single_assignment:next_ncol
        while next_ncol <= self.C_max_length: # comparison_operator:LtE, evolve_state (-> +22), loop:while (-> +22), while (-> +22)
            new_inverseC = [[] for i in range(next_ncol)] # assignment, assignment_lhs_identifier:new_inverseC, assignment_rhs_atom:i, assignment_rhs_atom:next_ncol, call_argument:next_ncol, comprehension:List, comprehension_for_count:1, falsey_literal:List, function_call:range, literal:List, range:next_ncol, single_assignment:new_inverseC
            root = self.root ** (next_ncol // 2) # assignment, assignment_lhs_identifier:root, assignment_rhs_atom:2, assignment_rhs_atom:next_ncol, assignment_rhs_atom:self, binary_operator:FloorDiv, binary_operator:Pow, int_literal, literal:Num, single_assignment:root
            current_root = 1 # assignment, assignment_lhs_identifier:current_root, assignment_rhs_atom:1, int_literal, literal:Num, single_assignment:current_root
            for j in range(self.C_max_length // next_ncol): # binary_operator:FloorDiv, call_argument:, for:j (-> +16), for_range:_ (-> +16), function_call:range, loop:for (-> +16), range:_
                for i in range(next_ncol // 2): # binary_operator:FloorDiv, call_argument:, for:i (-> +13), for_range:_ (-> +13), function_call:range, int_literal, literal:Num, loop:for (-> +13), nested_for:1 (-> +13), range:_
                    new_inverseC[i].append( # index:i, method_call:append
                        ( # binary_operator:Div, call_argument:
                            inverseC[i][j] # binary_operator:Add, index:i, index:j
                            + inverseC[i][j + self.C_max_length // next_ncol] # binary_operator:Add, binary_operator:FloorDiv, index:_, index:i, index_arithmetic
                        )
                        / 2 # int_literal, literal:Num
                    )
                    new_inverseC[i + next_ncol // 2].append( # binary_operator:Add, binary_operator:FloorDiv, index:_, index_arithmetic, int_literal, literal:Num, method_call:append
                        ( # binary_operator:Div, call_argument:
                            inverseC[i][j] # binary_operator:Sub, index:i, index:j
                            - inverseC[i][j + self.C_max_length // next_ncol] # binary_operator:Add, binary_operator:FloorDiv, index:_, index:i, index_arithmetic
                        )
                        / (2 * current_root) # binary_operator:Mult, int_literal, literal:Num
                    )
                current_root *= root # assignment_lhs_identifier:current_root, assignment_rhs_atom:root, augmented_assignment:Mult, variable_update:current_root:root, variable_update_by_augmented_assignment:current_root:root
            inverseC = new_inverseC # assignment, assignment_lhs_identifier:inverseC, assignment_rhs_atom:new_inverseC, single_assignment:inverseC
            next_ncol *= 2 # assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, augmented_assignment:Mult, int_literal, literal:Num, variable_update:next_ncol:2, variable_update_by_augmented_assignment:next_ncol:2
        inverseC = [round(x[0].real, 8) + round(x[0].imag, 8) * 1j for x in inverseC] # assignment, assignment_lhs_identifier:inverseC, assignment_rhs_atom:0, assignment_rhs_atom:1j, assignment_rhs_atom:8, assignment_rhs_atom:inverseC, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:8, comprehension:List, comprehension_for_count:1, falsey_literal:0, function_call:round, imaginary_literal, index:0, int_literal, literal:Num, single_assignment:inverseC, suggest_constant_definition, variable_update:inverseC:0, variable_update:inverseC:1j, variable_update:inverseC:8, variable_update:inverseC:x, variable_update_by_assignment:inverseC:0, variable_update_by_assignment:inverseC:1j, variable_update_by_assignment:inverseC:8, variable_update_by_assignment:inverseC:x
        while inverseC[-1] == 0: # comparison_operator:Eq, evolve_state (-> +1), falsey_literal:0, index:-1, int_literal, literal:Num, loop:while (-> +1), negative_index:-1, while (-> +1)
            inverseC.pop() # method_call:pop, method_call_object:inverseC
        return inverseC # return:inverseC
    def __str__(self): # function:__str__ (-> +10), function_argument:self, function_argument_flavor:arg, function_returning_something:__str__ (-> +10), instance_method:__str__ (-> +10), method:__str__ (-> +10)
        A = "A = " + " + ".join( # assignment, assignment_lhs_identifier:A, binary_operator:Add, composition, concatenation operator:Str, literal:Str, method_call:join, single_assignment:A
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyA[: self.len_A]) # assignment_rhs_atom:coef, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, comprehension:Generator, comprehension_for_count:1, function_call:enumerate, literal:Str, slice::_:, slice_lower:, slice_step:, slice_upper:_
        )
        B = "B = " + " + ".join( # assignment, assignment_lhs_identifier:B, binary_operator:Add, composition, concatenation operator:Str, literal:Str, method_call:join, single_assignment:B
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyB[: self.len_B]) # assignment_rhs_atom:coef, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, comprehension:Generator, comprehension_for_count:1, function_call:enumerate, literal:Str, slice::_:, slice_lower:, slice_step:, slice_upper:_
        )
        C = "A*B = " + " + ".join( # assignment, assignment_lhs_identifier:C, binary_operator:Add, composition, concatenation operator:Str, literal:Str, method_call:join, single_assignment:C
            f"{coef}*x^{i}" for coef, i in enumerate(self.product) # assignment_rhs_atom:coef, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, comprehension:Generator, comprehension_for_count:1, function_call:enumerate, literal:Str
        )
        return "\n".join((A, B, C)) # call_argument:, literal:Str, method_call:join, return

# ----------------------------------------------------------------------------------------
# ../Python/maths/runge_kutta.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, lines_of_code:14 (-> +13)
def runge_kutta(f, y0, x0, h, x_end): # function:runge_kutta (-> +12), function_argument:f, function_argument:h, function_argument:x0, function_argument:x_end, function_argument:y0, function_argument_flavor:arg, function_returning_something:runge_kutta (-> +12)
    N = int(np.ceil((x_end - x0) / h)) # assignment, assignment_lhs_identifier:N, assignment_rhs_atom:h, assignment_rhs_atom:np, assignment_rhs_atom:x0, assignment_rhs_atom:x_end, binary_operator:Div, binary_operator:Sub, call_argument:, composition, function_call:int, method_call:ceil, single_assignment:N
    y = np.zeros((N + 1,)) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:N, assignment_rhs_atom:np, binary_operator:Add, call_argument:, int_literal, literal:Num, method_call:zeros, single_assignment:y
    y[0] = y0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:y0, falsey_literal:0, index:0, int_literal, literal:Num
    x = x0 # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:x0, single_assignment:x
    for k in range(N): # accumulate_all_elements:y (-> +6), accumulate_elements:y (-> +6), call_argument:N, for:k (-> +6), for_range:N (-> +6), function_call:range, loop:for (-> +6), range:N
        k1 = f(x, y[k]) # assignment, assignment_lhs_identifier:k1, assignment_rhs_atom:k, assignment_rhs_atom:x, assignment_rhs_atom:y, call_argument:, call_argument:x, function_call:f, index:k, single_assignment:k1
        k2 = f(x + 0.5 * h, y[k] + 0.5 * h * k1) # assignment, assignment_lhs_identifier:k2, assignment_rhs_atom:0.5, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k1, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, float_literal, function_call:f, index:k, literal:Num, single_assignment:k2, suggest_constant_definition
        k3 = f(x + 0.5 * h, y[k] + 0.5 * h * k2) # assignment, assignment_lhs_identifier:k3, assignment_rhs_atom:0.5, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k2, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, float_literal, function_call:f, index:k, literal:Num, single_assignment:k3, suggest_constant_definition
        k4 = f(x + h, y[k] + h * k3) # assignment, assignment_lhs_identifier:k4, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k3, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, function_call:f, index:k, single_assignment:k4
        y[k + 1] = y[k] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k1, assignment_rhs_atom:k2, assignment_rhs_atom:k3, assignment_rhs_atom:k4, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Div, binary_operator:Mult, index:_, index:k, index_arithmetic, int_literal, literal:Num, suggest_constant_definition, variable_update:y:1, variable_update:y:2, variable_update:y:6, variable_update:y:h, variable_update:y:k, variable_update:y:k1, variable_update:y:k2, variable_update:y:k3, variable_update:y:k4, variable_update_by_assignment:y:1, variable_update_by_assignment:y:2, variable_update_by_assignment:y:6, variable_update_by_assignment:y:h, variable_update_by_assignment:y:k, variable_update_by_assignment:y:k1, variable_update_by_assignment:y:k2, variable_update_by_assignment:y:k3, variable_update_by_assignment:y:k4
        x += h # assignment_lhs_identifier:x, assignment_rhs_atom:h, augmented_assignment:Add, variable_update:x:h, variable_update_by_augmented_assignment:x:h
    return y # return:y

# ----------------------------------------------------------------------------------------
# ../Python/maths/segmented_sieve.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, lines_of_code:36 (-> +35)
def sieve(n): # function:sieve (-> +33), function_argument:n, function_argument_flavor:arg, function_returning_something:sieve (-> +33)
    in_prime = [] # assignment, assignment_lhs_identifier:in_prime, falsey_literal:List, literal:List, single_assignment:in_prime
    start = 2 # assignment, assignment_lhs_identifier:start, assignment_rhs_atom:2, int_literal, literal:Num, single_assignment:start
    end = int(math.sqrt(n)) # assignment, assignment_lhs_identifier:end, assignment_rhs_atom:math, assignment_rhs_atom:n, call_argument:, call_argument:n, composition, function_call:int, method_call:sqrt, single_assignment:end
    temp = [True] * (end + 1) # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:end, binary_operator:Add, binary_operator:Mult, int_literal, literal:List, literal:Num, literal:True, replication_operator:List, single_assignment:temp
    prime = [] # assignment, assignment_lhs_identifier:prime, falsey_literal:List, literal:List, single_assignment:prime
    while start <= end: # comparison_operator:LtE, loop:while (-> +6), while (-> +6)
        if temp[start] is True: # comparison_operator:Is, if (-> +4), if_test_atom:True, if_test_atom:start, if_test_atom:temp, index:start, literal:True
            in_prime.append(start) # call_argument:start, if_then_branch (-> +3), method_call:append, method_call_object:in_prime, variable_update:in_prime:start, variable_update_by_method_call:in_prime:start
            for i in range(start * start, end + 1, start): # binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:start, for:i (-> +2), for_range:_:_:start (-> +2), function_call:range, int_literal, literal:Num, loop:for (-> +2), range:_:_:start
                if temp[i] is True: # comparison_operator:Is, if (-> +1), if_test_atom:True, if_test_atom:i, if_test_atom:temp, index:i, literal:True, nested_if:1 (-> +1)
                    temp[i] = False # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:False, falsey_literal:False, if_then_branch, index:i, literal:False
        start += 1 # assignment_lhs_identifier:start, assignment_rhs_atom:1, augmented_assignment:Add, int_literal, literal:Num, variable_increment:start, variable_update:start:1, variable_update_by_augmented_assignment:start:1
    prime += in_prime # assignment_lhs_identifier:prime, assignment_rhs_atom:in_prime, augmented_assignment:Add, variable_update:prime:in_prime, variable_update_by_augmented_assignment:prime:in_prime
    low = end + 1 # assignment, assignment_lhs_identifier:low, assignment_rhs_atom:1, assignment_rhs_atom:end, binary_operator:Add, int_literal, literal:Num, single_assignment:low
    high = low + end - 1 # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:1, assignment_rhs_atom:end, assignment_rhs_atom:low, binary_operator:Add, binary_operator:Sub, int_literal, literal:Num, single_assignment:high
    if high > n: # comparison_operator:Gt, if (-> +1), if_test_atom:high, if_test_atom:n
        high = n # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:n, if_then_branch, single_assignment:high
    while low <= n: # comparison_operator:LtE, loop:while (-> +14), while (-> +14)
        temp = [True] * (high - low + 1) # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:high, assignment_rhs_atom:low, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, int_literal, literal:List, literal:Num, literal:True, replication_operator:List, single_assignment:temp
        for each in in_prime: # accumulate_elements:t (-> +5), accumulate_some_elements:t (-> +5), for:each (-> +5), for_each (-> +5), for_range:t:_:each (-> +5), loop:for (-> +5)
            t = math.floor(low / each) * each # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:each, assignment_rhs_atom:low, assignment_rhs_atom:math, binary_operator:Div, binary_operator:Mult, call_argument:, method_call:floor, single_assignment:t
            if t < low: # comparison_operator:Lt, if (-> +1), if_test_atom:low, if_test_atom:t
                t += each # assignment_lhs_identifier:t, assignment_rhs_atom:each, augmented_assignment:Add, if_then_branch, variable_update:t:each, variable_update_by_augmented_assignment:t:each
            for j in range(t, high + 1, each): # binary_operator:Add, call_argument:, call_argument:each, call_argument:t, for:j (-> +1), for_range:t:_:each (-> +1), function_call:range, int_literal, literal:Num, loop:for (-> +1), nested_for:1 (-> +1), range:t:_:each
                temp[j - low] = False # assignment, assignment_lhs_identifier:temp, assignment_rhs_atom:False, binary_operator:Sub, falsey_literal:False, index:_, index_arithmetic, literal:False
        for j in range(len(temp)): # call_argument:, call_argument:temp, composition, for:j (-> +2), for_indexes (-> +2), for_range:_ (-> +2), function_call:len, function_call:range, loop:for (-> +2), range:_
            if temp[j] is True: # comparison_operator:Is, if (-> +1), if_test_atom:True, if_test_atom:j, if_test_atom:temp, index:j, literal:True
                prime.append(j + low) # binary_operator:Add, call_argument:, if_then_branch, method_call:append, method_call_object:prime
        low = high + 1 # assignment, assignment_lhs_identifier:low, assignment_rhs_atom:1, assignment_rhs_atom:high, binary_operator:Add, int_literal, literal:Num, single_assignment:low
        high = low + end - 1 # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:1, assignment_rhs_atom:end, assignment_rhs_atom:low, binary_operator:Add, binary_operator:Sub, int_literal, literal:Num, single_assignment:high
        if high > n: # comparison_operator:Gt, if (-> +1), if_test_atom:high, if_test_atom:n
            high = n # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:n, if_then_branch, single_assignment:high
    return prime # return:prime
print(sieve(10 ** 6)) # binary_operator:Pow, call_argument:, composition, function_call:print, function_call:sieve, int_literal, literal:Num

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
""" # lines_of_code:25 (-> +17), literal:Str
import math # import:math, import_module:math
def sieve(n): # function:sieve (-> +15), function_argument:n, function_argument_flavor:arg, function_returning_something:sieve (-> +15)
    l = [True] * (n + 1) # assignment, assignment_lhs_identifier:l, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, int_literal, literal:List, literal:Num, literal:True, replication_operator:List, single_assignment:l
    prime = [] # assignment, assignment_lhs_identifier:prime, falsey_literal:List, literal:List, single_assignment:prime
    start = 2 # assignment, assignment_lhs_identifier:start, assignment_rhs_atom:2, int_literal, literal:Num, single_assignment:start
    end = int(math.sqrt(n)) # assignment, assignment_lhs_identifier:end, assignment_rhs_atom:math, assignment_rhs_atom:n, call_argument:, call_argument:n, composition, function_call:int, method_call:sqrt, single_assignment:end
    while start <= end: # comparison_operator:LtE, loop:while (-> +6), while (-> +6)
        if l[start] is True: # comparison_operator:Is, if (-> +4), if_test_atom:True, if_test_atom:l, if_test_atom:start, index:start, literal:True
            prime.append(start) # call_argument:start, if_then_branch (-> +3), method_call:append, method_call_object:prime, variable_update:prime:start, variable_update_by_method_call:prime:start
            for i in range(start * start, n + 1, start): # binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:start, for:i (-> +2), for_range:_:_:start (-> +2), function_call:range, int_literal, literal:Num, loop:for (-> +2), range:_:_:start
                if l[i] is True: # comparison_operator:Is, if (-> +1), if_test_atom:True, if_test_atom:i, if_test_atom:l, index:i, literal:True, nested_if:1 (-> +1)
                    l[i] = False # assignment, assignment_lhs_identifier:l, assignment_rhs_atom:False, falsey_literal:False, if_then_branch, index:i, literal:False
        start += 1 # assignment_lhs_identifier:start, assignment_rhs_atom:1, augmented_assignment:Add, int_literal, literal:Num, variable_increment:start, variable_update:start:1, variable_update_by_augmented_assignment:start:1
    for j in range(end + 1, n + 1): # accumulate_elements:prime (-> +2), accumulate_some_elements:prime (-> +2), binary_operator:Add, call_argument:, for:j (-> +2), for_range:_:_ (-> +2), function_call:range, int_literal, literal:Num, loop:for (-> +2), range:_:_
        if l[j] is True: # comparison_operator:Is, if (-> +1), if_test_atom:True, if_test_atom:j, if_test_atom:l, index:j, literal:True
            prime.append(j) # call_argument:j, if_then_branch, method_call:append, method_call_object:prime, variable_update:prime:j, variable_update_by_method_call:prime:j
    return prime # return:prime

# ----------------------------------------------------------------------------------------
# ../Python/maths/simpson_rule.py
# ----------------------------------------------------------------------------------------
def method_2(boundary, steps): # function:method_2 (-> +12), function_argument:boundary, function_argument:steps, function_argument_flavor:arg, function_returning_something:method_2 (-> +12), lines_of_code:28 (-> +27)
    h = (boundary[1] - boundary[0]) / steps # assignment, assignment_lhs_identifier:h, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, binary_operator:Div, binary_operator:Sub, falsey_literal:0, index:0, index:1, int_literal, literal:Num, single_assignment:h
    a = boundary[0] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, assignment_rhs_atom:boundary, falsey_literal:0, index:0, int_literal, literal:Num, single_assignment:a
    b = boundary[1] # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1, assignment_rhs_atom:boundary, index:1, int_literal, literal:Num, single_assignment:b
    x_i = make_points(a, b, h) # assignment, assignment_lhs_identifier:x_i, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:h, call_argument:a, call_argument:b, call_argument:h, function_call:make_points, single_assignment:x_i
    y = 0.0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:0.0, falsey_literal:0.0, float_literal, literal:Num, single_assignment:y, suggest_constant_definition
    y += (h / 3.0) * f(a) # assignment_lhs_identifier:y, assignment_rhs_atom:3.0, assignment_rhs_atom:a, assignment_rhs_atom:h, augmented_assignment:Add, binary_operator:Div, binary_operator:Mult, call_argument:a, float_literal, function_call:f, literal:Num, suggest_constant_definition, variable_update:y:3.0, variable_update:y:a, variable_update:y:h, variable_update_by_augmented_assignment:y:3.0, variable_update_by_augmented_assignment:y:a, variable_update_by_augmented_assignment:y:h
    cnt = 2 # assignment, assignment_lhs_identifier:cnt, assignment_rhs_atom:2, int_literal, literal:Num, single_assignment:cnt
    for i in x_i: # accumulate_all_elements:y (-> +2), accumulate_elements:y (-> +2), count_elements:cnt (-> +2), for:i (-> +2), for_each (-> +2), loop:for (-> +2)
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i) # assignment_lhs_identifier:y, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:4, assignment_rhs_atom:cnt, assignment_rhs_atom:h, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, call_argument:i, function_call:f, int_literal, literal:Num, suggest_constant_definition, variable_update:y:2, variable_update:y:3, variable_update:y:4, variable_update:y:cnt, variable_update:y:h, variable_update:y:i, variable_update_by_augmented_assignment:y:2, variable_update_by_augmented_assignment:y:3, variable_update_by_augmented_assignment:y:4, variable_update_by_augmented_assignment:y:cnt, variable_update_by_augmented_assignment:y:h, variable_update_by_augmented_assignment:y:i
        cnt += 1 # assignment_lhs_identifier:cnt, assignment_rhs_atom:1, augmented_assignment:Add, int_literal, literal:Num, variable_increment:cnt, variable_update:cnt:1, variable_update_by_augmented_assignment:cnt:1
    y += (h / 3.0) * f(b) # assignment_lhs_identifier:y, assignment_rhs_atom:3.0, assignment_rhs_atom:b, assignment_rhs_atom:h, augmented_assignment:Add, binary_operator:Div, binary_operator:Mult, call_argument:b, float_literal, function_call:f, literal:Num, suggest_constant_definition, variable_update:y:3.0, variable_update:y:b, variable_update:y:h, variable_update_by_augmented_assignment:y:3.0, variable_update_by_augmented_assignment:y:b, variable_update_by_augmented_assignment:y:h
    return y # return:y
def make_points(a, b, h): # function:make_points (-> +4), function_argument:a, function_argument:b, function_argument:h, function_argument_flavor:arg, generator:make_points (-> +4)
    x = a + h # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:h, binary_operator:Add, single_assignment:x
    while x < (b - h): # binary_operator:Sub, comparison_operator:Lt, loop:while (-> +2), while (-> +2)
        yield x # yield:x
        x = x + h # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:h, assignment_rhs_atom:x, binary_operator:Add, single_assignment:x, suggest_augmented_assignment, variable_update:x:h, variable_update_by_assignment:x:h
def f(x): # function:f (-> +2), function_argument:x, function_argument_flavor:arg, function_returning_something:f (-> +2)
    y = (x - 0) * (x - 0) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:0, assignment_rhs_atom:x, binary_operator:Mult, binary_operator:Sub, falsey_literal:0, int_literal, literal:Num, single_assignment:y
    return y # return:y
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6), function_without_arguments:main (-> +6)
    a = 0.0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0.0, falsey_literal:0.0, float_literal, literal:Num, single_assignment:a, suggest_constant_definition
    b = 1.0 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1.0, float_literal, literal:Num, single_assignment:b, suggest_constant_definition
    steps = 10.0 # assignment, assignment_lhs_identifier:steps, assignment_rhs_atom:10.0, float_literal, literal:Num, single_assignment:steps, suggest_constant_definition
    boundary = [a, b] # assignment, assignment_lhs_identifier:boundary, assignment_rhs_atom:a, assignment_rhs_atom:b, single_assignment:boundary
    y = method_2(boundary, steps) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, call_argument:boundary, call_argument:steps, function_call:method_2, single_assignment:y
    print("y = {0}".format(y)) # call_argument:, call_argument:y, composition, function_call:print, literal:Str, method_call:format

# ----------------------------------------------------------------------------------------
# ../Python/maths/softmax.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, lines_of_code:6 (-> +5)
def softmax(vector): # function:softmax (-> +4), function_argument:vector, function_argument_flavor:arg, function_returning_something:softmax (-> +4)
    exponentVector = np.exp(vector) # assignment, assignment_lhs_identifier:exponentVector, assignment_rhs_atom:np, assignment_rhs_atom:vector, call_argument:vector, method_call:exp, single_assignment:exponentVector
    sumOfExponents = np.sum(exponentVector) # assignment, assignment_lhs_identifier:sumOfExponents, assignment_rhs_atom:exponentVector, assignment_rhs_atom:np, call_argument:exponentVector, method_call:sum, single_assignment:sumOfExponents
    softmax_vector = exponentVector / sumOfExponents # assignment, assignment_lhs_identifier:softmax_vector, assignment_rhs_atom:exponentVector, assignment_rhs_atom:sumOfExponents, binary_operator:Div, single_assignment:softmax_vector
    return softmax_vector # return:softmax_vector

# ----------------------------------------------------------------------------------------
# ../Python/maths/sum_of_arithmetic_series.py
# ----------------------------------------------------------------------------------------
def sum_of_series(first_term, common_diff, num_of_terms): # function:sum_of_series (-> +2), function_argument:common_diff, function_argument:first_term, function_argument:num_of_terms, function_argument_flavor:arg, function_returning_something:sum_of_series (-> +2), lines_of_code:5 (-> +4)
    sum = (num_of_terms / 2) * (2 * first_term + (num_of_terms - 1) * common_diff) # assignment, assignment_lhs_identifier:sum, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:common_diff, assignment_rhs_atom:first_term, assignment_rhs_atom:num_of_terms, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, int_literal, literal:Num, single_assignment:sum
    return sum # return:sum
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    print(sum_of_series(1, 1, 10)) # call_argument:, call_argument:1, call_argument:10, composition, function_call:print, function_call:sum_of_series, int_literal, literal:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# ../Python/maths/test_prime_check.py
# ----------------------------------------------------------------------------------------
from .prime_check import Test # import:prime_check:Test, import_module:prime_check, import_name:Test, lines_of_code:2 (-> +1)
Test() # function_call:Test, function_call_without_arguments:Test

# ----------------------------------------------------------------------------------------
# ../Python/maths/trapezoidal_rule.py
# ----------------------------------------------------------------------------------------
def method_1(boundary, steps): # function:method_1 (-> +10), function_argument:boundary, function_argument:steps, function_argument_flavor:arg, function_returning_something:method_1 (-> +10), lines_of_code:26 (-> +25)
    h = (boundary[1] - boundary[0]) / steps # assignment, assignment_lhs_identifier:h, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, binary_operator:Div, binary_operator:Sub, falsey_literal:0, index:0, index:1, int_literal, literal:Num, single_assignment:h
    a = boundary[0] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, assignment_rhs_atom:boundary, falsey_literal:0, index:0, int_literal, literal:Num, single_assignment:a
    b = boundary[1] # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1, assignment_rhs_atom:boundary, index:1, int_literal, literal:Num, single_assignment:b
    x_i = make_points(a, b, h) # assignment, assignment_lhs_identifier:x_i, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:h, call_argument:a, call_argument:b, call_argument:h, function_call:make_points, single_assignment:x_i
    y = 0.0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:0.0, falsey_literal:0.0, float_literal, literal:Num, single_assignment:y, suggest_constant_definition
    y += (h / 2.0) * f(a) # assignment_lhs_identifier:y, assignment_rhs_atom:2.0, assignment_rhs_atom:a, assignment_rhs_atom:h, augmented_assignment:Add, binary_operator:Div, binary_operator:Mult, call_argument:a, float_literal, function_call:f, literal:Num, suggest_constant_definition, variable_update:y:2.0, variable_update:y:a, variable_update:y:h, variable_update_by_augmented_assignment:y:2.0, variable_update_by_augmented_assignment:y:a, variable_update_by_augmented_assignment:y:h
    for i in x_i: # accumulate_all_elements:y (-> +1), accumulate_elements:y (-> +1), for:i (-> +1), for_each (-> +1), loop:for (-> +1)
        y += h * f(i) # assignment_lhs_identifier:y, assignment_rhs_atom:h, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Mult, call_argument:i, function_call:f, variable_update:y:h, variable_update:y:i, variable_update_by_augmented_assignment:y:h, variable_update_by_augmented_assignment:y:i
    y += (h / 2.0) * f(b) # assignment_lhs_identifier:y, assignment_rhs_atom:2.0, assignment_rhs_atom:b, assignment_rhs_atom:h, augmented_assignment:Add, binary_operator:Div, binary_operator:Mult, call_argument:b, float_literal, function_call:f, literal:Num, suggest_constant_definition, variable_update:y:2.0, variable_update:y:b, variable_update:y:h, variable_update_by_augmented_assignment:y:2.0, variable_update_by_augmented_assignment:y:b, variable_update_by_augmented_assignment:y:h
    return y # return:y
def make_points(a, b, h): # function:make_points (-> +4), function_argument:a, function_argument:b, function_argument:h, function_argument_flavor:arg, generator:make_points (-> +4)
    x = a + h # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:h, binary_operator:Add, single_assignment:x
    while x < (b - h): # binary_operator:Sub, comparison_operator:Lt, loop:while (-> +2), while (-> +2)
        yield x # yield:x
        x = x + h # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:h, assignment_rhs_atom:x, binary_operator:Add, single_assignment:x, suggest_augmented_assignment, variable_update:x:h, variable_update_by_assignment:x:h
def f(x): # function:f (-> +2), function_argument:x, function_argument_flavor:arg, function_returning_something:f (-> +2)
    y = (x - 0) * (x - 0) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:0, assignment_rhs_atom:x, binary_operator:Mult, binary_operator:Sub, falsey_literal:0, int_literal, literal:Num, single_assignment:y
    return y # return:y
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6), function_without_arguments:main (-> +6)
    a = 0.0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0.0, falsey_literal:0.0, float_literal, literal:Num, single_assignment:a, suggest_constant_definition
    b = 1.0 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1.0, float_literal, literal:Num, single_assignment:b, suggest_constant_definition
    steps = 10.0 # assignment, assignment_lhs_identifier:steps, assignment_rhs_atom:10.0, float_literal, literal:Num, single_assignment:steps, suggest_constant_definition
    boundary = [a, b] # assignment, assignment_lhs_identifier:boundary, assignment_rhs_atom:a, assignment_rhs_atom:b, single_assignment:boundary
    y = method_1(boundary, steps) # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, call_argument:boundary, call_argument:steps, function_call:method_1, single_assignment:y
    print("y = {0}".format(y)) # call_argument:, call_argument:y, composition, function_call:print, literal:Str, method_call:format

# ----------------------------------------------------------------------------------------
# ../Python/maths/volume.py
# ----------------------------------------------------------------------------------------
from math import pi # import:math:pi, import_module:math, import_name:pi, lines_of_code:27 (-> +26)
def vol_cube(side_length): # function:vol_cube (-> +1), function_argument:side_length, function_argument_flavor:arg, function_returning_something:vol_cube (-> +1)
    return float(side_length ** 3) # binary_operator:Pow, call_argument:, function_call:float, function_tail_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_cuboid(width, height, length): # function:vol_cuboid (-> +1), function_argument:height, function_argument:length, function_argument:width, function_argument_flavor:arg, function_returning_something:vol_cuboid (-> +1)
    return float(width * height * length) # binary_operator:Mult, call_argument:, function_call:float, function_tail_call:float, return
def vol_cone(area_of_base, height): # function:vol_cone (-> +1), function_argument:area_of_base, function_argument:height, function_argument_flavor:arg, function_returning_something:vol_cone (-> +1)
    return (float(1) / 3) * area_of_base * height # binary_operator:Div, binary_operator:Mult, call_argument:1, function_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_right_circ_cone(radius, height): # function:vol_right_circ_cone (-> +1), function_argument:height, function_argument:radius, function_argument_flavor:arg, function_returning_something:vol_right_circ_cone (-> +1)
    return (float(1) / 3) * pi * (radius ** 2) * height # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, call_argument:1, function_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_prism(area_of_base, height): # function:vol_prism (-> +1), function_argument:area_of_base, function_argument:height, function_argument_flavor:arg, function_returning_something:vol_prism (-> +1)
    return float(area_of_base * height) # binary_operator:Mult, call_argument:, function_call:float, function_tail_call:float, return
def vol_pyramid(area_of_base, height): # function:vol_pyramid (-> +1), function_argument:area_of_base, function_argument:height, function_argument_flavor:arg, function_returning_something:vol_pyramid (-> +1)
    return (float(1) / 3) * area_of_base * height # binary_operator:Div, binary_operator:Mult, call_argument:1, function_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_sphere(radius): # function:vol_sphere (-> +1), function_argument:radius, function_argument_flavor:arg, function_returning_something:vol_sphere (-> +1)
    return (float(4) / 3) * pi * radius ** 3 # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, call_argument:4, function_call:float, int_literal, literal:Num, return, suggest_constant_definition
def vol_circular_cylinder(radius, height): # function:vol_circular_cylinder (-> +1), function_argument:height, function_argument:radius, function_argument_flavor:arg, function_returning_something:vol_circular_cylinder (-> +1)
    return pi * radius ** 2 * height # binary_operator:Mult, binary_operator:Pow, int_literal, literal:Num, return
def main(): # function:main (-> +9), function_returning_nothing:main (-> +9), function_without_arguments:main (-> +9)
    print("Volumes:") # call_argument:, function_call:print, literal:Str
    print("Cube: " + str(vol_cube(2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation operator:Str, function_call:print, function_call:str, function_call:vol_cube, int_literal, literal:Num, literal:Str
    print("Cuboid: " + str(vol_cuboid(2, 2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation operator:Str, function_call:print, function_call:str, function_call:vol_cuboid, int_literal, literal:Num, literal:Str
    print("Cone: " + str(vol_cone(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation operator:Str, function_call:print, function_call:str, function_call:vol_cone, int_literal, literal:Num, literal:Str
    print("Right Circular Cone: " + str(vol_right_circ_cone(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation operator:Str, function_call:print, function_call:str, function_call:vol_right_circ_cone, int_literal, literal:Num, literal:Str
    print("Prism: " + str(vol_prism(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation operator:Str, function_call:print, function_call:str, function_call:vol_prism, int_literal, literal:Num, literal:Str
    print("Pyramid: " + str(vol_pyramid(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation operator:Str, function_call:print, function_call:str, function_call:vol_pyramid, int_literal, literal:Num, literal:Str
    print("Sphere: " + str(vol_sphere(2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation operator:Str, function_call:print, function_call:str, function_call:vol_sphere, int_literal, literal:Num, literal:Str
    print("Circular Cylinder: " + str(vol_circular_cylinder(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation operator:Str, function_call:print, function_call:str, function_call:vol_circular_cylinder, int_literal, literal:Num, literal:Str

# ----------------------------------------------------------------------------------------
# ../Python/maths/zellers_congruence.py
# ----------------------------------------------------------------------------------------
import datetime # import:datetime, import_module:datetime, lines_of_code:49 (-> +48)
import argparse # import:argparse, import_module:argparse
def zeller(date_input: str) -> str: # function:zeller (-> +46), function_argument:date_input, function_argument_flavor:arg, function_returning_something:zeller (-> +46)
    days = { # assignment, assignment_lhs_identifier:days, literal:Dict, single_assignment:days
        "0": "Sunday", # literal:Str
        "1": "Monday", # literal:Str
        "2": "Tuesday", # literal:Str
        "3": "Wednesday", # literal:Str
        "4": "Thursday", # literal:Str
        "5": "Friday", # literal:Str
        "6": "Saturday", # literal:Str
    }
    convert_datetime_days = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0} # assignment, assignment_lhs_identifier:convert_datetime_days, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:4, assignment_rhs_atom:5, assignment_rhs_atom:6, falsey_literal:0, int_literal, literal:Dict, literal:Num, single_assignment:convert_datetime_days, suggest_constant_definition
    if not 0 < len(date_input) < 11: # call_argument:date_input, chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, falsey_literal:0, function_call:len, if (-> +1), if_test_atom:0, if_test_atom:11, if_test_atom:date_input, int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError("Must be 10 characters long") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    m: int = int(date_input[0] + date_input[1]) # binary_operator:Add, call_argument:, falsey_literal:0, function_call:int, index:0, index:1, int_literal, literal:Num
    if not 0 < m < 13: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:13, if_test_atom:m, int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError("Month must be between 1 - 12") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    sep_1: str = date_input[2] # index:2, int_literal, literal:Num
    if sep_1 not in ["-", "/"]: # comparison_operator:NotIn, if (-> +1), if_test_atom:sep_1, literal:List, literal:Str
        raise ValueError("Date seperator must be '-' or '/'") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    d: int = int(date_input[3] + date_input[4]) # binary_operator:Add, call_argument:, function_call:int, index:3, index:4, int_literal, literal:Num, suggest_constant_definition
    if not 0 < d < 32: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, falsey_literal:0, if (-> +1), if_test_atom:0, if_test_atom:32, if_test_atom:d, int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError("Date must be between 1 - 31") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    sep_2: str = date_input[5] # index:5, int_literal, literal:Num, suggest_constant_definition
    if sep_2 not in ["-", "/"]: # comparison_operator:NotIn, if (-> +1), if_test_atom:sep_2, literal:List, literal:Str
        raise ValueError("Date seperator must be '-' or '/'") # call_argument:, function_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    y: int = int(date_input[6] + date_input[7] + date_input[8] + date_input[9]) # binary_operator:Add, call_argument:, function_call:int, index:6, index:7, index:8, index:9, int_literal, literal:Num, suggest_constant_definition
    if not 45 < y < 8500: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +2), if_test_atom:45, if_test_atom:8500, if_test_atom:y, int_literal, literal:Num, suggest_constant_definition, unary_operator:Not
        raise ValueError( # function_call:ValueError, if_then_branch (-> +1), raise:ValueError
            "Year out of range. There has to be some sort of limit...right?" # call_argument:, literal:Str
        )
    dt_ck = datetime.date(int(y), int(m), int(d)) # assignment, assignment_lhs_identifier:dt_ck, assignment_rhs_atom:d, assignment_rhs_atom:datetime, assignment_rhs_atom:m, assignment_rhs_atom:y, call_argument:, call_argument:d, call_argument:m, call_argument:y, composition, function_call:int, method_call:date, single_assignment:dt_ck
    if m <= 2: # comparison_operator:LtE, if (-> +2), if_test_atom:2, if_test_atom:m, int_literal, literal:Num
        y = y - 1 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:y, binary_operator:Sub, if_then_branch (-> +1), int_literal, literal:Num, single_assignment:y, suggest_augmented_assignment, variable_update:y:1, variable_update_by_assignment:y:1
        m = m + 12 # assignment, assignment_lhs_identifier:m, assignment_rhs_atom:12, assignment_rhs_atom:m, binary_operator:Add, int_literal, literal:Num, single_assignment:m, suggest_augmented_assignment, suggest_constant_definition, variable_increment:m, variable_update:m:12, variable_update_by_assignment:m:12
    c: int = int(str(y)[:2]) # call_argument:, call_argument:y, composition, function_call:int, function_call:str, int_literal, literal:Num, slice::2:, slice_lower:, slice_step:, slice_upper:2
    k: int = int(str(y)[2:]) # call_argument:, call_argument:y, composition, function_call:int, function_call:str, int_literal, literal:Num, slice:2::, slice_lower:2, slice_step:, slice_upper:
    t: int = int(2.6 * m - 5.39) # binary_operator:Mult, binary_operator:Sub, call_argument:, float_literal, function_call:int, literal:Num, suggest_constant_definition
    u: int = int(c / 4) # binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, suggest_constant_definition
    v: int = int(k / 4) # binary_operator:Div, call_argument:, function_call:int, int_literal, literal:Num, suggest_constant_definition
    x: int = int(d + k) # binary_operator:Add, call_argument:, function_call:int
    z: int = int(t + u + v + x) # binary_operator:Add, call_argument:, function_call:int
    w: int = int(z - (2 * c)) # binary_operator:Mult, binary_operator:Sub, call_argument:, function_call:int, int_literal, literal:Num
    f: int = round(w % 7) # binary_operator:Mod, call_argument:, function_call:round, int_literal, literal:Num, suggest_constant_definition
    if f != convert_datetime_days[dt_ck.weekday()]: # comparison_operator:NotEq, if (-> +1), if_test_atom:convert_datetime_days, if_test_atom:dt_ck, if_test_atom:f, index:_, method_call:weekday, method_call_object:dt_ck
        raise AssertionError("The date was evaluated incorrectly. Contact developer.") # call_argument:, function_call:AssertionError, if_then_branch, literal:Str, raise:AssertionError
    response: str = f"Your date {date_input}, is a {days[str(f)]}!" # call_argument:f, function_call:str, index:_, literal:Str
    return response # return:response
