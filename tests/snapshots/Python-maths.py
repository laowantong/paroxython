# ----------------------------------------------------------------------------------------
# 3n+1.py
# ----------------------------------------------------------------------------------------
from typing import Tuple, List # import:typing:List, import:typing:Tuple, import_module:typing, import_name:List, import_name:Tuple, whole_span:128 (-> +127)
def n31(a: int) -> Tuple[List[int], int]: # function:n31 (-> +12), function_argument:a, function_argument_flavor:arg, function_returning_something:n31 (-> +12), index:_, index:int, literal:Tuple, nested_index:2
    if not isinstance(a, int): # call_argument:a, call_argument:int, external_free_call:isinstance, free_call:isinstance, if (-> +1), if_test_atom:a, if_test_atom:int, if_without_else (-> +1), unary_operator:Not
        raise TypeError("Must be int, not {0}".format(type(a).__name__)) # call_argument:, call_argument:a, composition, external_free_call:TypeError, external_free_call:type, free_call:TypeError, free_call:type, if_then_branch, literal:Str, member_call:format, raise:TypeError
    if a < 1: # comparison_operator:Lt, if (-> +1), if_test_atom:1, if_test_atom:a, if_without_else (-> +1), literal:1
        raise ValueError("Given integer must be greater than 1, not {0}".format(a)) # call_argument:, call_argument:a, composition, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, member_call:format, raise:ValueError
    path = [a] # assignment, assignment_lhs_identifier:path, assignment_rhs_atom:a, literal:List, single_assignment:path
    while a != 1: # comparison_operator:NotEq, literal:1, loop:while (-> +5), loop_with_late_exit:while (-> +5), while (-> +5)
        if a % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:0, if_test_atom:2, if_test_atom:a, literal:0, literal:2, modulo_operator, verbose_conditional_assignment (-> +3)
            a = a // 2 # assignment:FloorDiv, assignment_lhs_identifier:a, assignment_rhs_atom:2, assignment_rhs_atom:a, binary_operator:FloorDiv, if_then_branch, literal:2, single_assignment:a, suggest_augmented_assignment, update:a:2, update_by_assignment:a:2, update_by_assignment_with:FloorDiv, update_with:FloorDiv
        else:
            a = 3 * a + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:a, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:a, binary_operator:Add, binary_operator:Mult, if_else_branch, literal:1, literal:3, multiplication_operator, single_assignment:a, suggest_constant_definition, update:a:1, update:a:3, update_by_assignment:a:1, update_by_assignment:a:3, update_by_assignment_with:Add, update_with:Add
        path += [a] # assignment_lhs_identifier:path, assignment_rhs_atom:a, augmented_assignment:Add, concatenation_operator:List, literal:List, update:path:a, update_by_augmented_assignment:path:a, update_by_augmented_assignment_with:Add, update_with:Add
    return path, len(path) # call_argument:path, external_free_call:len, free_call:len, literal:Tuple, return
def test_n31(): # function:test_n31 (-> +113), function_returning_nothing:test_n31 (-> +113), function_without_arguments:test_n31 (-> +113)
    assert n31(4) == ([4, 2, 1], 3) # assertion, call_argument:4, comparison_operator:Eq, free_call:n31, internal_free_call:n31, literal:1, literal:2, literal:3, literal:4, literal:List, literal:Tuple, suggest_constant_definition
    assert n31(11) == ([11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], 15) # assertion, call_argument:11, comparison_operator:Eq, free_call:n31, internal_free_call:n31, literal:1, literal:10, literal:11, literal:13, literal:15, literal:16, literal:17, literal:2, literal:20, literal:26, literal:34, literal:4, literal:40, literal:5, literal:52, literal:8, literal:List, literal:Tuple, suggest_constant_definition
    assert n31(31) == ( # assertion, call_argument:31, free_call:n31, internal_free_call:n31, literal:31, suggest_constant_definition
        [ # comparison_operator:Eq, literal:List, literal:Tuple
            31, # literal:31, suggest_constant_definition
            94, # literal:94, suggest_constant_definition
            47, # literal:47, suggest_constant_definition
            142, # literal:142, suggest_constant_definition
            71, # literal:71, suggest_constant_definition
            214, # literal:214, suggest_constant_definition
            107, # literal:107, suggest_constant_definition
            322, # literal:322, suggest_constant_definition
            161, # literal:161, suggest_constant_definition
            484, # literal:484, suggest_constant_definition
            242, # literal:242, suggest_constant_definition
            121, # literal:121, suggest_constant_definition
            364, # literal:364, suggest_constant_definition
            182, # literal:182, suggest_constant_definition
            91, # literal:91, suggest_constant_definition
            274, # literal:274, suggest_constant_definition
            137, # literal:137, suggest_constant_definition
            412, # literal:412, suggest_constant_definition
            206, # literal:206, suggest_constant_definition
            103, # literal:103, suggest_constant_definition
            310, # literal:310, suggest_constant_definition
            155, # literal:155, suggest_constant_definition
            466, # literal:466, suggest_constant_definition
            233, # literal:233, suggest_constant_definition
            700, # literal:700, suggest_constant_definition
            350, # literal:350, suggest_constant_definition
            175, # literal:175, suggest_constant_definition
            526, # literal:526, suggest_constant_definition
            263, # literal:263, suggest_constant_definition
            790, # literal:790, suggest_constant_definition
            395, # literal:395, suggest_constant_definition
            1186, # literal:1186, suggest_constant_definition
            593, # literal:593, suggest_constant_definition
            1780, # literal:1780, suggest_constant_definition
            890, # literal:890, suggest_constant_definition
            445, # literal:445, suggest_constant_definition
            1336, # literal:1336, suggest_constant_definition
            668, # literal:668, suggest_constant_definition
            334, # literal:334, suggest_constant_definition
            167, # literal:167, suggest_constant_definition
            502, # literal:502, suggest_constant_definition
            251, # literal:251, suggest_constant_definition
            754, # literal:754, suggest_constant_definition
            377, # literal:377, suggest_constant_definition
            1132, # literal:1132, suggest_constant_definition
            566, # literal:566, suggest_constant_definition
            283, # literal:283, suggest_constant_definition
            850, # literal:850, suggest_constant_definition
            425, # literal:425, suggest_constant_definition
            1276, # literal:1276, suggest_constant_definition
            638, # literal:638, suggest_constant_definition
            319, # literal:319, suggest_constant_definition
            958, # literal:958, suggest_constant_definition
            479, # literal:479, suggest_constant_definition
            1438, # literal:1438, suggest_constant_definition
            719, # literal:719, suggest_constant_definition
            2158, # literal:2158, suggest_constant_definition
            1079, # literal:1079, suggest_constant_definition
            3238, # literal:3238, suggest_constant_definition
            1619, # literal:1619, suggest_constant_definition
            4858, # literal:4858, suggest_constant_definition
            2429, # literal:2429, suggest_constant_definition
            7288, # literal:7288, suggest_constant_definition
            3644, # literal:3644, suggest_constant_definition
            1822, # literal:1822, suggest_constant_definition
            911, # literal:911, suggest_constant_definition
            2734, # literal:2734, suggest_constant_definition
            1367, # literal:1367, suggest_constant_definition
            4102, # literal:4102, suggest_constant_definition
            2051, # literal:2051, suggest_constant_definition
            6154, # literal:6154, suggest_constant_definition
            3077, # literal:3077, suggest_constant_definition
            9232, # literal:9232, suggest_constant_definition
            4616, # literal:4616, suggest_constant_definition
            2308, # literal:2308, suggest_constant_definition
            1154, # literal:1154, suggest_constant_definition
            577, # literal:577, suggest_constant_definition
            1732, # literal:1732, suggest_constant_definition
            866, # literal:866, suggest_constant_definition
            433, # literal:433, suggest_constant_definition
            1300, # literal:1300, suggest_constant_definition
            650, # literal:650, suggest_constant_definition
            325, # literal:325, suggest_constant_definition
            976, # literal:976, suggest_constant_definition
            488, # literal:488, suggest_constant_definition
            244, # literal:244, suggest_constant_definition
            122, # literal:122, suggest_constant_definition
            61, # literal:61, suggest_constant_definition
            184, # literal:184, suggest_constant_definition
            92, # literal:92, suggest_constant_definition
            46, # literal:46, suggest_constant_definition
            23, # literal:23, suggest_constant_definition
            70, # literal:70, suggest_constant_definition
            35, # literal:35, suggest_constant_definition
            106, # literal:106, suggest_constant_definition
            53, # literal:53, suggest_constant_definition
            160, # literal:160, suggest_constant_definition
            80, # literal:80, suggest_constant_definition
            40, # literal:40, suggest_constant_definition
            20, # literal:20, suggest_constant_definition
            10, # literal:10, suggest_constant_definition
            5, # literal:5, suggest_constant_definition
            16, # literal:16, suggest_constant_definition
            8, # literal:8, suggest_constant_definition
            4, # literal:4, suggest_constant_definition
            2, # literal:2
            1, # literal:1
        ],
        107, # literal:107, suggest_constant_definition
    )

# ----------------------------------------------------------------------------------------
# abs.py
# ----------------------------------------------------------------------------------------
def abs_val(num): # function:abs_val (-> +1), function_argument:num, function_argument_flavor:arg, function_returning_something:abs_val (-> +1), whole_span:6 (-> +5)
    return -num if num < 0 else num # comparison_operator:Lt, conditional_expression, literal:0, return, unary_operator:USub
def test_abs_val(): # function:test_abs_val (-> +3), function_returning_nothing:test_abs_val (-> +3), function_without_arguments:test_abs_val (-> +3)
    assert 0 == abs_val(0) # assertion, call_argument:0, comparison_operator:Eq, free_call:abs_val, internal_free_call:abs_val, literal:0, yoda_comparison:Eq
    assert 34 == abs_val(34) # assertion, call_argument:34, comparison_operator:Eq, free_call:abs_val, internal_free_call:abs_val, literal:34, suggest_constant_definition, yoda_comparison:Eq
    assert 100000000000 == abs_val(-100000000000) # assertion, call_argument:-100000000000, comparison_operator:Eq, free_call:abs_val, internal_free_call:abs_val, literal:-100000000000, literal:100000000000, suggest_constant_definition, yoda_comparison:Eq

# ----------------------------------------------------------------------------------------
# abs_max.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List, whole_span:13 (-> +12)
def abs_max(x: List[int]) -> int: # function:abs_max (-> +5), function_argument:x, function_argument_flavor:arg, function_returning_something:abs_max (-> +5)
    j = x[0] # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:0, assignment_rhs_atom:x, index:0, literal:0, single_assignment:j
    for i in x: # find_best_element:i:j (-> +2), for:i (-> +2), for_each (-> +2), loop:for (-> +2), loop_with_late_exit:for (-> +2)
        if abs(i) > abs(j): # call_argument:i, call_argument:j, comparison_operator:Gt, external_free_call:abs, free_call:abs, if (-> +1), if_test_atom:i, if_test_atom:j, if_without_else (-> +1)
            j = i # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:i, if_then_branch, single_assignment:j
    return j # return:j
def abs_max_sort(x): # function:abs_max_sort (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:abs_max_sort (-> +1)
    return sorted(x, key=abs)[-1] # call_argument:x, external_free_call:sorted, free_call:sorted, index:-1, literal:-1, negative_index:-1, return
def main(): # function:main (-> +3), function_returning_nothing:main (-> +3), function_without_arguments:main (-> +3)
    a = [1, 2, -11] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:-11, assignment_rhs_atom:1, assignment_rhs_atom:2, literal:-11, literal:1, literal:2, literal:List, single_assignment:a, suggest_constant_definition
    assert abs_max(a) == -11 # assertion, call_argument:a, comparison_operator:Eq, free_call:abs_max, internal_free_call:abs_max, literal:-11, suggest_constant_definition
    assert abs_max_sort(a) == -11 # assertion, call_argument:a, comparison_operator:Eq, free_call:abs_max_sort, internal_free_call:abs_max_sort, literal:-11, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# abs_min.py
# ----------------------------------------------------------------------------------------
from .abs import abs_val # import_internally:abs:abs_val, import_module_internally:abs, import_name:abs_val, whole_span:10 (-> +9)
def absMin(x): # function:absMin (-> +5), function_argument:x, function_argument_flavor:arg, function_returning_something:absMin (-> +5)
    j = x[0] # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:0, assignment_rhs_atom:x, index:0, literal:0, single_assignment:j
    for i in x: # find_best_element:i:j (-> +2), for:i (-> +2), for_each (-> +2), loop:for (-> +2), loop_with_late_exit:for (-> +2)
        if abs_val(i) < abs_val(j): # call_argument:i, call_argument:j, comparison_operator:Lt, external_free_call:abs_val, free_call:abs_val, if (-> +1), if_test_atom:i, if_test_atom:j, if_without_else (-> +1)
            j = i # assignment, assignment_lhs_identifier:j, assignment_rhs_atom:i, if_then_branch, single_assignment:j
    return j # return:j
def main(): # function:main (-> +2), function_returning_nothing:main (-> +2), function_without_arguments:main (-> +2)
    a = [-3, -1, 2, -11] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:-1, assignment_rhs_atom:-11, assignment_rhs_atom:-3, assignment_rhs_atom:2, literal:-1, literal:-11, literal:-3, literal:2, literal:List, single_assignment:a, suggest_constant_definition
    print(absMin(a)) # call_argument:, call_argument:a, composition, external_free_call:print, free_call:absMin, free_call:print, free_call_without_result:print, internal_free_call:absMin

# ----------------------------------------------------------------------------------------
# average_mean.py
# ----------------------------------------------------------------------------------------
def average(nums): # function:average (-> +1), function_argument:nums, function_argument_flavor:arg, function_returning_something:average (-> +1), whole_span:6 (-> +5)
    return sum(nums) / len(nums) # binary_operator:Div, call_argument:nums, external_free_call:len, external_free_call:sum, free_call:len, free_call:sum, return
def test_average(): # function:test_average (-> +3), function_returning_nothing:test_average (-> +3), function_without_arguments:test_average (-> +3)
    assert 12.0 == average([3, 6, 9, 12, 15, 18, 21]) # assertion, call_argument:, comparison_operator:Eq, free_call:average, internal_free_call:average, literal:12, literal:12.0, literal:15, literal:18, literal:21, literal:3, literal:6, literal:9, literal:List, suggest_constant_definition, yoda_comparison:Eq
    assert 20 == average([5, 10, 15, 20, 25, 30, 35]) # assertion, call_argument:, comparison_operator:Eq, free_call:average, internal_free_call:average, literal:10, literal:15, literal:20, literal:25, literal:30, literal:35, literal:5, literal:List, suggest_constant_definition, yoda_comparison:Eq
    assert 4.5 == average([1, 2, 3, 4, 5, 6, 7, 8]) # assertion, call_argument:, comparison_operator:Eq, free_call:average, internal_free_call:average, literal:1, literal:2, literal:3, literal:4, literal:4.5, literal:5, literal:6, literal:7, literal:8, literal:List, suggest_constant_definition, yoda_comparison:Eq

# ----------------------------------------------------------------------------------------
# average_median.py
# ----------------------------------------------------------------------------------------
def median(nums): # function:median (-> +10), function_argument:nums, function_argument_flavor:arg, function_returning_something:median (-> +10), whole_span:16 (-> +15)
    sorted_list = sorted(nums) # assignment:sorted, assignment_lhs_identifier:sorted_list, assignment_rhs_atom:nums, call_argument:nums, external_free_call:sorted, free_call:sorted, single_assignment:sorted_list
    med = None # assignment:None, assignment_lhs_identifier:med, assignment_rhs_atom:None, literal:None, single_assignment:med
    if len(sorted_list) % 2 == 0: # binary_operator:Mod, call_argument:sorted_list, comparison_operator:Eq, divisibility_test:2, external_free_call:len, free_call:len, if (-> +6), if_test_atom:0, if_test_atom:2, if_test_atom:sorted_list, literal:0, literal:2, modulo_operator
        mid_index_1 = len(sorted_list) // 2 # assignment:FloorDiv, assignment_lhs_identifier:mid_index_1, assignment_rhs_atom:2, assignment_rhs_atom:sorted_list, binary_operator:FloorDiv, call_argument:sorted_list, external_free_call:len, free_call:len, if_then_branch (-> +2), literal:2, single_assignment:mid_index_1
        mid_index_2 = (len(sorted_list) // 2) - 1 # assignment:Sub, assignment_lhs_identifier:mid_index_2, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sorted_list, binary_operator:FloorDiv, binary_operator:Sub, call_argument:sorted_list, external_free_call:len, free_call:len, literal:1, literal:2, single_assignment:mid_index_2
        med = (sorted_list[mid_index_1] + sorted_list[mid_index_2]) / float(2) # addition_operator, assignment:Div, assignment_lhs_identifier:med, assignment_rhs_atom:2, assignment_rhs_atom:mid_index_1, assignment_rhs_atom:mid_index_2, assignment_rhs_atom:sorted_list, binary_operator:Add, binary_operator:Div, call_argument:2, external_free_call:float, free_call:float, index:mid_index_1, index:mid_index_2, literal:2, single_assignment:med
    else:
        mid_index = (len(sorted_list) - 1) // 2 # assignment:FloorDiv, assignment_lhs_identifier:mid_index, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sorted_list, binary_operator:FloorDiv, binary_operator:Sub, call_argument:sorted_list, external_free_call:len, free_call:len, if_else_branch (-> +1), literal:1, literal:2, single_assignment:mid_index
        med = sorted_list[mid_index] # assignment, assignment_lhs_identifier:med, assignment_rhs_atom:mid_index, assignment_rhs_atom:sorted_list, index:mid_index, single_assignment:med
    return med # return:med
def main(): # function:main (-> +4), function_returning_nothing:main (-> +4), function_without_arguments:main (-> +4)
    print("Odd number of numbers:") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str
    print(median([2, 4, 6, 8, 20, 50, 70])) # call_argument:, composition, external_free_call:print, free_call:median, free_call:print, free_call_without_result:print, internal_free_call:median, literal:2, literal:20, literal:4, literal:50, literal:6, literal:70, literal:8, literal:List, suggest_constant_definition
    print("Even number of numbers:") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str
    print(median([2, 4, 6, 8, 20, 50])) # call_argument:, composition, external_free_call:print, free_call:median, free_call:print, free_call_without_result:print, internal_free_call:median, literal:2, literal:20, literal:4, literal:50, literal:6, literal:8, literal:List, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# average_mode.py
# ----------------------------------------------------------------------------------------
import statistics # import:statistics, import_module:statistics, whole_span:9 (-> +8)
def mode(input_list): # function:mode (-> +7), function_argument:input_list, function_argument_flavor:arg, function_returning_something:mode (-> +7)
    check_list = input_list.copy() # assignment:copy, assignment_lhs_identifier:check_list, assignment_rhs_atom:input_list, member_call:copy, single_assignment:check_list
    result = list() # assignment:list, assignment_lhs_identifier:result, external_free_call:list, free_call:list, free_call_without_arguments:list, single_assignment:result
    for x in input_list: # accumulate_all_elements:append (-> +4), accumulate_all_elements:remove (-> +4), accumulate_elements:append (-> +4), accumulate_elements:remove (-> +4), for:x (-> +4), for_each (-> +4), loop:for (-> +4), loop_with_early_exit:for:return (-> +4), loop_with_return:for (-> +4)
        result.append(input_list.count(x)) # call_argument:, call_argument:x, composition, member_call:append, member_call:count, member_call_object:result, member_call_without_result:append, update:result:x, update_by_member_call:result:x, update_by_member_call_with:append, update_with:append
        input_list.remove(x) # call_argument:x, member_call:remove, member_call_object:input_list, member_call_without_result:remove, update:input_list:x, update_by_member_call:input_list:x, update_by_member_call_with:remove, update_with:remove
        y = max(result) # assignment:max, assignment_lhs_identifier:y, assignment_rhs_atom:result, call_argument:result, external_free_call:max, free_call:max, single_assignment:y
        return check_list[result.index(y)] # call_argument:y, index:_, member_call:index, member_call_object:result, return

# ----------------------------------------------------------------------------------------
# basic_maths.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, whole_span:48 (-> +47)
def prime_factors(n: int) -> list: # function:prime_factors (-> +11), function_argument:n, function_argument_flavor:arg, function_returning_something:prime_factors (-> +11)
    pf = [] # assignment, assignment_lhs_identifier:pf, empty_literal:List, literal:List, single_assignment:pf
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, literal:0, literal:2, loop:while (-> +2), loop_with_late_exit:while (-> +2), modulo_operator, while (-> +2)
        pf.append(2) # call_argument:2, literal:2, member_call:append, member_call_object:pf, member_call_without_result:append, update:pf:2, update_by_member_call:pf:2, update_by_member_call_with:append, update_with:append
        n = int(n / 2) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, external_free_call:int, free_call:int, literal:2, single_assignment:n, update:n:2, update_by_assignment:n:2, update_by_assignment_with:int, update_with:int
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_all_elements:append (-> +3), accumulate_all_elements:int (-> +3), accumulate_elements:append (-> +3), accumulate_elements:int (-> +3), addition_operator, binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:n, composition, external_free_call:int, external_free_call:range, for:i (-> +3), for_range:3:_:2 (-> +3), free_call:int, free_call:range, literal:1, literal:2, literal:3, loop:for (-> +3), loop_with_late_exit:for (-> +3), member_call:sqrt, range:3:_:2, suggest_constant_definition
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, literal:0, loop:while (-> +2), loop_with_late_exit:while (-> +2), modulo_operator, while (-> +2)
            pf.append(i) # call_argument:i, member_call:append, member_call_object:pf, member_call_without_result:append, update:pf:i, update_by_member_call:pf:i, update_by_member_call_with:append, update_with:append
            n = int(n / i) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, external_free_call:int, free_call:int, single_assignment:n, update:n:i, update_by_assignment:n:i, update_by_assignment_with:int, update_with:int
    if n > 2: # comparison_operator:Gt, if (-> +1), if_test_atom:2, if_test_atom:n, if_without_else (-> +1), literal:2
        pf.append(n) # call_argument:n, if_then_branch, member_call:append, member_call_object:pf, member_call_without_result:append, update:pf:n, update_by_member_call:pf:n, update_by_member_call_with:append, update_with:append
    return pf # return:pf
def number_of_divisors(n: int) -> int: # function:number_of_divisors (-> +13), function_argument:n, function_argument_flavor:arg, function_returning_something:number_of_divisors (-> +13)
    div = 1 # assignment:1, assignment_lhs_identifier:div, assignment_rhs_atom:1, literal:1, single_assignment:div
    temp = 1 # assignment:1, assignment_lhs_identifier:temp, assignment_rhs_atom:1, literal:1, single_assignment:temp
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, count_states:temp (-> +2), divisibility_test:2, literal:0, literal:2, loop:while (-> +2), loop_with_late_exit:while (-> +2), modulo_operator, while (-> +2)
        temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, increment:temp, literal:1, update:temp:1, update_by_augmented_assignment:temp:1, update_by_augmented_assignment_with:Add, update_with:Add
        n = int(n / 2) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, external_free_call:int, free_call:int, literal:2, single_assignment:n, update:n:2, update_by_assignment:n:2, update_by_assignment_with:int, update_with:int
    div *= temp # assignment_lhs_identifier:div, assignment_rhs_atom:temp, augmented_assignment:Mult, update:div:temp, update_by_augmented_assignment:div:temp, update_by_augmented_assignment_with:Mult, update_with:Mult
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_all_elements:int (-> +5), accumulate_elements:int (-> +5), addition_operator, binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:n, composition, external_free_call:int, external_free_call:range, for:i (-> +5), for_range:3:_:2 (-> +5), free_call:int, free_call:range, literal:1, literal:2, literal:3, loop:for (-> +5), loop_with_late_exit:for (-> +5), member_call:sqrt, range:3:_:2, suggest_constant_definition
        temp = 1 # assignment:1, assignment_lhs_identifier:temp, assignment_rhs_atom:1, literal:1, single_assignment:temp
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, count_states:temp (-> +2), divisibility_test, literal:0, loop:while (-> +2), loop_with_late_exit:while (-> +2), modulo_operator, while (-> +2)
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, increment:temp, literal:1, update:temp:1, update_by_augmented_assignment:temp:1, update_by_augmented_assignment_with:Add, update_with:Add
            n = int(n / i) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, external_free_call:int, free_call:int, single_assignment:n, update:n:i, update_by_assignment:n:i, update_by_assignment_with:int, update_with:int
        div *= temp # assignment_lhs_identifier:div, assignment_rhs_atom:temp, augmented_assignment:Mult, update:div:temp, update_by_augmented_assignment:div:temp, update_by_augmented_assignment_with:Mult, update_with:Mult
    return div # return:div
def sum_of_divisors(n: int) -> int: # function:sum_of_divisors (-> +15), function_argument:n, function_argument_flavor:arg, function_returning_something:sum_of_divisors (-> +15)
    s = 1 # assignment:1, assignment_lhs_identifier:s, assignment_rhs_atom:1, literal:1, single_assignment:s
    temp = 1 # assignment:1, assignment_lhs_identifier:temp, assignment_rhs_atom:1, literal:1, single_assignment:temp
    while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, count_states:temp (-> +2), divisibility_test:2, literal:0, literal:2, loop:while (-> +2), loop_with_late_exit:while (-> +2), modulo_operator, while (-> +2)
        temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, increment:temp, literal:1, update:temp:1, update_by_augmented_assignment:temp:1, update_by_augmented_assignment_with:Add, update_with:Add
        n = int(n / 2) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, external_free_call:int, free_call:int, literal:2, single_assignment:n, update:n:2, update_by_assignment:n:2, update_by_assignment_with:int, update_with:int
    if temp > 1: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:temp, if_without_else (-> +1), literal:1
        s *= (2 ** temp - 1) / (2 - 1) # assignment_lhs_identifier:s, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:temp, augmented_assignment:Mult, binary_operator:Div, binary_operator:Pow, binary_operator:Sub, if_then_branch, literal:1, literal:2, update:s:1, update:s:2, update:s:temp, update_by_augmented_assignment:s:1, update_by_augmented_assignment:s:2, update_by_augmented_assignment:s:temp, update_by_augmented_assignment_with:Mult, update_with:Mult
    for i in range(3, int(math.sqrt(n)) + 1, 2): # accumulate_all_elements:int (-> +6), accumulate_elements:Mult (-> +6), accumulate_elements:int (-> +6), accumulate_some_elements:Mult (-> +6), addition_operator, binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:n, composition, external_free_call:int, external_free_call:range, for:i (-> +6), for_range:3:_:2 (-> +6), free_call:int, free_call:range, literal:1, literal:2, literal:3, loop:for (-> +6), loop_with_late_exit:for (-> +6), member_call:sqrt, range:3:_:2, suggest_constant_definition
        temp = 1 # assignment:1, assignment_lhs_identifier:temp, assignment_rhs_atom:1, literal:1, single_assignment:temp
        while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, count_states:temp (-> +2), divisibility_test, literal:0, loop:while (-> +2), loop_with_late_exit:while (-> +2), modulo_operator, while (-> +2)
            temp += 1 # assignment_lhs_identifier:temp, assignment_rhs_atom:1, augmented_assignment:Add, increment:temp, literal:1, update:temp:1, update_by_augmented_assignment:temp:1, update_by_augmented_assignment_with:Add, update_with:Add
            n = int(n / i) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, external_free_call:int, free_call:int, single_assignment:n, update:n:i, update_by_assignment:n:i, update_by_assignment_with:int, update_with:int
        if temp > 1: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:temp, if_without_else (-> +1), literal:1
            s *= (i ** temp - 1) / (i - 1) # assignment_lhs_identifier:s, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:temp, augmented_assignment:Mult, binary_operator:Div, binary_operator:Pow, binary_operator:Sub, if_then_branch, literal:1, update:s:1, update:s:i, update:s:temp, update_by_augmented_assignment:s:1, update_by_augmented_assignment:s:i, update_by_augmented_assignment:s:temp, update_by_augmented_assignment_with:Mult, update_with:Mult
    return int(s) # call_argument:s, external_free_call:int, free_call:int, free_tail_call:int, return
def euler_phi(n: int) -> int: # function:euler_phi (-> +4), function_argument:n, function_argument_flavor:arg, function_returning_something:euler_phi (-> +4)
    s = n # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:n, single_assignment:s
    for x in set(prime_factors(n)): # accumulate_all_elements:Mult (-> +1), accumulate_elements:Mult (-> +1), call_argument:, call_argument:n, composition, external_free_call:set, for:x (-> +1), free_call:prime_factors, free_call:set, internal_free_call:prime_factors, loop:for (-> +1), loop_with_late_exit:for (-> +1)
        s *= (x - 1) / x # assignment_lhs_identifier:s, assignment_rhs_atom:1, assignment_rhs_atom:x, augmented_assignment:Mult, binary_operator:Div, binary_operator:Sub, literal:1, update:s:1, update:s:x, update_by_augmented_assignment:s:1, update_by_augmented_assignment:s:x, update_by_augmented_assignment_with:Mult, update_with:Mult
    return int(s) # call_argument:s, external_free_call:int, free_call:int, free_tail_call:int, return

# ----------------------------------------------------------------------------------------
# binary_exponentiation.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n): # body_recursive_function:binary_exponentiation (-> +7), function:binary_exponentiation (-> +7), function_argument:a, function_argument:n, function_argument_flavor:arg, function_returning_something:binary_exponentiation (-> +7), recursive_function:binary_exponentiation (-> +7), whole_span:8 (-> +7)
    if n == 0: # comparison_operator:Eq, if (-> +6), if_test_atom:0, if_test_atom:n, literal:0
        return 1 # if_then_branch, literal:1, return:1
    elif n % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +4), if_test_atom:1, if_test_atom:2, if_test_atom:n, literal:1, literal:2, modulo_operator
        return binary_exponentiation(a, n - 1) * a # binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:a, free_call:binary_exponentiation, if_elif_branch, internal_free_call:binary_exponentiation, literal:1, multiplication_operator, return
    else:
        b = binary_exponentiation(a, n / 2) # assignment:binary_exponentiation, assignment_lhs_identifier:b, assignment_rhs_atom:2, assignment_rhs_atom:a, assignment_rhs_atom:n, binary_operator:Div, call_argument:, call_argument:a, free_call:binary_exponentiation, if_else_branch (-> +1), internal_free_call:binary_exponentiation, literal:2, single_assignment:b
        return b * b # binary_operator:Mult, multiplication_operator, return

# ----------------------------------------------------------------------------------------
# binomial_coefficient.py
# ----------------------------------------------------------------------------------------
def binomial_coefficient(n, r): # function:binomial_coefficient (-> +8), function_argument:n, function_argument:r, function_argument_flavor:arg, function_returning_something:binomial_coefficient (-> +8), whole_span:10 (-> +9)
    C = [0 for i in range(r + 1)] # addition_operator, assignment, assignment_lhs_identifier:C, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:r, binary_operator:Add, call_argument:, comprehension:List, comprehension_for_count:1, external_free_call:range, free_call:range, literal:0, literal:1, range:_, single_assignment:C
    C[0] = 1 # assignment:1, assignment_lhs_identifier:C, assignment_rhs_atom:1, index:0, literal:0, literal:1
    for i in range(1, n + 1): # addition_operator, binary_operator:Add, call_argument:, call_argument:1, external_free_call:range, for:i (-> +4), for_range:1:_ (-> +4), free_call:range, literal:1, loop:for (-> +4), loop_with_late_exit:for (-> +4), range:1:_
        j = min(i, r) # assignment:min, assignment_lhs_identifier:j, assignment_rhs_atom:i, assignment_rhs_atom:r, call_argument:i, call_argument:r, external_free_call:min, free_call:min, single_assignment:j
        while j > 0: # comparison_operator:Gt, literal:0, loop:while (-> +2), loop_with_late_exit:while (-> +2), while (-> +2)
            C[j] += C[j - 1] # assignment_lhs_identifier:C, assignment_rhs_atom:1, assignment_rhs_atom:C, assignment_rhs_atom:j, augmented_assignment:Add, binary_operator:Sub, index:_, index:j, index_arithmetic, literal:1, subscript_augmented_assignment:Add, update:C:1, update:C:C, update:C:j, update_by_augmented_assignment:C:1, update_by_augmented_assignment:C:C, update_by_augmented_assignment:C:j, update_by_augmented_assignment_with:Add, update_with:Add
            j -= 1 # assignment_lhs_identifier:j, assignment_rhs_atom:1, augmented_assignment:Sub, literal:1, update:j:1, update_by_augmented_assignment:j:1, update_by_augmented_assignment_with:Sub, update_with:Sub
    return C[r] # index:r, return
print(binomial_coefficient(n=10, r=5)) # call_argument:, composition, external_free_call:print, free_call:binomial_coefficient, free_call:print, free_call_without_result:print, internal_free_call:binomial_coefficient, literal:10, literal:5

# ----------------------------------------------------------------------------------------
# ceil.py
# ----------------------------------------------------------------------------------------
def ceil(x) -> int: # function:ceil (-> +2), function_argument:x, function_argument_flavor:arg, function_returning_something:ceil (-> +2), whole_span:3 (-> +2)
    return ( # return
        x if isinstance(x, int) or x - int(x) == 0 else int(x + 1) if x > 0 else int(x) # addition_operator, binary_operator:Add, binary_operator:Sub, boolean_operator:Or, call_argument:, call_argument:int, call_argument:x, comparison_operator:Eq, comparison_operator:Gt, conditional_expression, external_free_call:int, external_free_call:isinstance, free_call:int, free_call:isinstance, literal:0, literal:1
    )

# ----------------------------------------------------------------------------------------
# collatz_sequence.py
# ----------------------------------------------------------------------------------------
def collatz_sequence(n): # function:collatz_sequence (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:collatz_sequence (-> +8), whole_span:14 (-> +13)
    sequence = [n] # assignment, assignment_lhs_identifier:sequence, assignment_rhs_atom:n, literal:List, single_assignment:sequence
    while n != 1: # comparison_operator:NotEq, literal:1, loop:while (-> +5), loop_with_late_exit:while (-> +5), while (-> +5)
        if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:0, if_test_atom:2, if_test_atom:n, literal:0, literal:2, modulo_operator
            n //= 2 # assignment_lhs_identifier:n, assignment_rhs_atom:2, augmented_assignment:FloorDiv, if_then_branch, literal:2, update:n:2, update_by_augmented_assignment:n:2, update_by_augmented_assignment_with:FloorDiv, update_with:FloorDiv
        else:
            n = 3 * n + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:n, assignment_rhs_atom:1, assignment_rhs_atom:3, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, if_else_branch, literal:1, literal:3, multiplication_operator, single_assignment:n, suggest_constant_definition, update:n:1, update:n:3, update_by_assignment:n:1, update_by_assignment:n:3, update_by_assignment_with:Add, update_with:Add
        sequence.append(n) # call_argument:n, member_call:append, member_call_object:sequence, member_call_without_result:append, update:sequence:n, update_by_member_call:sequence:n, update_by_member_call_with:append, update_with:append
    return sequence # return:sequence
def main(): # function:main (-> +4), function_returning_nothing:main (-> +4), function_without_arguments:main (-> +4)
    n = 43 # assignment:43, assignment_lhs_identifier:n, assignment_rhs_atom:43, literal:43, single_assignment:n, suggest_constant_definition
    sequence = collatz_sequence(n) # assignment:collatz_sequence, assignment_lhs_identifier:sequence, assignment_rhs_atom:n, call_argument:n, free_call:collatz_sequence, internal_free_call:collatz_sequence, single_assignment:sequence
    print(sequence) # call_argument:sequence, external_free_call:print, free_call:print, free_call_without_result:print
    print("collatz sequence from %d took %d steps." % (n, len(sequence))) # binary_operator:Mod, call_argument:, call_argument:sequence, composition, external_free_call:len, external_free_call:print, free_call:len, free_call:print, free_call_without_result:print, literal:Str, literal:Tuple, string_formatting_operator

# ----------------------------------------------------------------------------------------
# explicit_euler.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, whole_span:10 (-> +9)
def explicit_euler(ode_func, y0, x0, stepsize, x_end): # function:explicit_euler (-> +8), function_argument:ode_func, function_argument:stepsize, function_argument:x0, function_argument:x_end, function_argument:y0, function_argument_flavor:arg, function_returning_something:explicit_euler (-> +8), higher_order_function:ode_func (-> +8)
    N = int(np.ceil((x_end - x0) / stepsize)) # assignment:int, assignment_lhs_identifier:N, assignment_rhs_atom:np, assignment_rhs_atom:stepsize, assignment_rhs_atom:x0, assignment_rhs_atom:x_end, binary_operator:Div, binary_operator:Sub, call_argument:, composition, external_free_call:int, free_call:int, member_call:ceil, single_assignment:N
    y = np.zeros((N + 1,)) # addition_operator, assignment:zeros, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:N, assignment_rhs_atom:np, binary_operator:Add, call_argument:, literal:1, literal:Tuple, member_call:zeros, single_assignment:y
    y[0] = y0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:y0, index:0, literal:0
    x = x0 # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:x0, single_assignment:x
    for k in range(N): # accumulate_all_elements:Add (-> +2), accumulate_elements:Add (-> +2), call_argument:N, external_free_call:range, for:k (-> +2), for_range:N (-> +2), free_call:range, loop:for (-> +2), loop_with_late_exit:for (-> +2), range:N
        y[k + 1] = y[k] + stepsize * ode_func(x, y[k]) # addition_operator, assignment:Add, assignment_lhs_identifier:y, assignment_rhs_atom:k, assignment_rhs_atom:stepsize, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:x, external_free_call:ode_func, free_call:ode_func, index:_, index:k, index_arithmetic, literal:1, multiplication_operator, update:y:k, update:y:stepsize, update:y:x, update_by_assignment:y:k, update_by_assignment:y:stepsize, update_by_assignment:y:x, update_by_assignment_with:Add, update_with:Add
        x += stepsize # assignment_lhs_identifier:x, assignment_rhs_atom:stepsize, augmented_assignment:Add, update:x:stepsize, update_by_augmented_assignment:x:stepsize, update_by_augmented_assignment_with:Add, update_with:Add
    return y # return:y

# ----------------------------------------------------------------------------------------
# extended_euclidean_algorithm.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, whole_span:40 (-> +39)
def extended_euclidean_algorithm(m, n): # function:extended_euclidean_algorithm (-> +31), function_argument:m, function_argument:n, function_argument_flavor:arg, function_returning_something:extended_euclidean_algorithm (-> +31)
    a = 0 # assignment:0, assignment_lhs_identifier:a, assignment_rhs_atom:0, literal:0, single_assignment:a
    a_prime = 1 # assignment:1, assignment_lhs_identifier:a_prime, assignment_rhs_atom:1, literal:1, single_assignment:a_prime
    b = 1 # assignment:1, assignment_lhs_identifier:b, assignment_rhs_atom:1, literal:1, single_assignment:b
    b_prime = 0 # assignment:0, assignment_lhs_identifier:b_prime, assignment_rhs_atom:0, literal:0, single_assignment:b_prime
    q = 0 # assignment:0, assignment_lhs_identifier:q, assignment_rhs_atom:0, literal:0, single_assignment:q
    r = 0 # assignment:0, assignment_lhs_identifier:r, assignment_rhs_atom:0, literal:0, single_assignment:r
    if m > n: # comparison_operator:Gt, if (-> +5), if_test_atom:m, if_test_atom:n
        c = m # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:m, if_then_branch (-> +1), single_assignment:c
        d = n # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:n, single_assignment:d
    else:
        c = n # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:n, if_else_branch (-> +1), single_assignment:c
        d = m # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:m, single_assignment:d
    while True: # infinite_while (-> +12), literal:True, loop:while (-> +12), loop_with_break:while (-> +12), loop_with_early_exit:while:break (-> +12), while (-> +12)
        q = int(c / d) # assignment:int, assignment_lhs_identifier:q, assignment_rhs_atom:c, assignment_rhs_atom:d, binary_operator:Div, call_argument:, external_free_call:int, free_call:int, single_assignment:q
        r = c % d # assignment:Mod, assignment_lhs_identifier:r, assignment_rhs_atom:c, assignment_rhs_atom:d, binary_operator:Mod, modulo_operator, single_assignment:r
        if r == 0: # comparison_operator:Eq, if (-> +1), if_test_atom:0, if_test_atom:r, if_without_else (-> +1), literal:0
            break # break, if_then_branch
        c = d # assignment, assignment_lhs_identifier:c, assignment_rhs_atom:d, single_assignment:c
        d = r # assignment, assignment_lhs_identifier:d, assignment_rhs_atom:r, single_assignment:d
        t = a_prime # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:a_prime, single_assignment:t
        a_prime = a # assignment, assignment_lhs_identifier:a_prime, assignment_rhs_atom:a, single_assignment:a_prime
        a = t - q * a # assignment:Sub, assignment_lhs_identifier:a, assignment_rhs_atom:a, assignment_rhs_atom:q, assignment_rhs_atom:t, binary_operator:Mult, binary_operator:Sub, multiplication_operator, single_assignment:a, update:a:q, update:a:t, update_by_assignment:a:q, update_by_assignment:a:t, update_by_assignment_with:Sub, update_with:Sub
        t = b_prime # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:b_prime, single_assignment:t
        b_prime = b # assignment, assignment_lhs_identifier:b_prime, assignment_rhs_atom:b, single_assignment:b_prime
        b = t - q * b # assignment:Sub, assignment_lhs_identifier:b, assignment_rhs_atom:b, assignment_rhs_atom:q, assignment_rhs_atom:t, binary_operator:Mult, binary_operator:Sub, multiplication_operator, single_assignment:b, update:b:q, update:b:t, update_by_assignment:b:q, update_by_assignment:b:t, update_by_assignment_with:Sub, update_with:Sub
    pair = None # assignment:None, assignment_lhs_identifier:pair, assignment_rhs_atom:None, literal:None, single_assignment:pair
    if m > n: # comparison_operator:Gt, if (-> +3), if_test_atom:m, if_test_atom:n, verbose_conditional_assignment (-> +3)
        pair = (a, b) # assignment, assignment_lhs_identifier:pair, assignment_rhs_atom:a, assignment_rhs_atom:b, if_then_branch, literal:Tuple, single_assignment:pair
    else:
        pair = (b, a) # assignment, assignment_lhs_identifier:pair, assignment_rhs_atom:a, assignment_rhs_atom:b, if_else_branch, literal:Tuple, single_assignment:pair
    return pair # return:pair
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6), function_without_arguments:main (-> +6)
    if len(sys.argv) < 3: # call_argument:, comparison_operator:Lt, external_free_call:len, free_call:len, if (-> +2), if_test_atom:3, if_test_atom:sys, if_without_else (-> +2), literal:3, suggest_constant_definition
        print("2 integer arguments required") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch (-> +1), literal:Str
        exit(1) # call_argument:1, external_free_call:exit, free_call:exit, free_call_without_result:exit, literal:1
    m = int(sys.argv[1]) # assignment:int, assignment_lhs_identifier:m, assignment_rhs_atom:1, assignment_rhs_atom:sys, call_argument:, external_free_call:int, free_call:int, index:1, literal:1, single_assignment:m
    n = int(sys.argv[2]) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:sys, call_argument:, external_free_call:int, free_call:int, index:2, literal:2, single_assignment:n
    print(extended_euclidean_algorithm(m, n)) # call_argument:, call_argument:m, call_argument:n, composition, external_free_call:print, free_call:extended_euclidean_algorithm, free_call:print, free_call_without_result:print, internal_free_call:extended_euclidean_algorithm

# ----------------------------------------------------------------------------------------
# factorial_python.py
# ----------------------------------------------------------------------------------------
def factorial(input_number: int) -> int: # function:factorial (-> +8), function_argument:input_number, function_argument_flavor:arg, function_returning_something:factorial (-> +8), whole_span:9 (-> +8)
    if input_number < 0: # comparison_operator:Lt, if (-> +1), if_test_atom:0, if_test_atom:input_number, if_without_else (-> +1), literal:0
        raise ValueError("factorial() not defined for negative values") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    if not isinstance(input_number, int): # call_argument:input_number, call_argument:int, external_free_call:isinstance, free_call:isinstance, if (-> +1), if_test_atom:input_number, if_test_atom:int, if_without_else (-> +1), unary_operator:Not
        raise ValueError("factorial() only accepts integral values") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    result = 1 # assignment:1, assignment_lhs_identifier:result, assignment_rhs_atom:1, literal:1, single_assignment:result
    for i in range(1, input_number): # accumulate_all_elements:Mult (-> +1), accumulate_elements:Mult (-> +1), call_argument:1, call_argument:input_number, external_free_call:range, for:i (-> +1), for_range:1:input_number (-> +1), free_call:range, literal:1, loop:for (-> +1), loop_with_late_exit:for (-> +1), range:1:input_number
        result = result * (i + 1) # addition_operator, assignment:Mult, assignment_lhs_identifier:result, assignment_rhs_atom:1, assignment_rhs_atom:i, assignment_rhs_atom:result, binary_operator:Add, binary_operator:Mult, literal:1, multiplication_operator, single_assignment:result, suggest_augmented_assignment, update:result:1, update:result:i, update_by_assignment:result:1, update_by_assignment:result:i, update_by_assignment_with:Mult, update_with:Mult
    return result # return:result

# ----------------------------------------------------------------------------------------
# factorial_recursive.py
# ----------------------------------------------------------------------------------------
def factorial(n: int) -> int: # body_recursive_function:factorial (-> +5), function:factorial (-> +5), function_argument:n, function_argument_flavor:arg, function_returning_something:factorial (-> +5), recursive_function:factorial (-> +5), whole_span:6 (-> +5)
    if n < 0: # comparison_operator:Lt, if (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0
        raise ValueError("factorial() not defined for negative values") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    if not isinstance(n, int): # call_argument:int, call_argument:n, external_free_call:isinstance, free_call:isinstance, if (-> +1), if_test_atom:int, if_test_atom:n, if_without_else (-> +1), unary_operator:Not
        raise ValueError("factorial() only accepts integral values") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    return 1 if n == 0 or n == 1 else n * factorial(n - 1) # binary_operator:Mult, binary_operator:Sub, boolean_operator:Or, call_argument:, comparison_operator:Eq, conditional_expression, free_call:factorial, internal_free_call:factorial, literal:0, literal:1, multiplication_operator, return

# ----------------------------------------------------------------------------------------
# factors.py
# ----------------------------------------------------------------------------------------
def factors_of_a_number(num: int) -> list: # function:factors_of_a_number (-> +1), function_argument:num, function_argument_flavor:arg, function_returning_something:factors_of_a_number (-> +1), whole_span:2 (-> +1)
    return [i for i in range(1, num + 1) if num % i == 0] # addition_operator, binary_operator:Add, binary_operator:Mod, call_argument:, call_argument:1, comparison_operator:Eq, comprehension:List, comprehension_for_count:1, divisibility_test, external_free_call:range, filtered_comprehension, free_call:range, literal:0, literal:1, modulo_operator, range:1:_, return

# ----------------------------------------------------------------------------------------
# fermat_little_theorem.py
# ----------------------------------------------------------------------------------------
def binary_exponentiation(a, n, mod): # body_recursive_function:binary_exponentiation (-> +7), function:binary_exponentiation (-> +7), function_argument:a, function_argument:mod, function_argument:n, function_argument_flavor:arg, function_returning_something:binary_exponentiation (-> +7), recursive_function:binary_exponentiation (-> +7), whole_span:13 (-> +12)
    if n == 0: # comparison_operator:Eq, if (-> +6), if_test_atom:0, if_test_atom:n, literal:0
        return 1 # if_then_branch, literal:1, return:1
    elif n % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +4), if_test_atom:1, if_test_atom:2, if_test_atom:n, literal:1, literal:2, modulo_operator
        return (binary_exponentiation(a, n - 1, mod) * a) % mod # binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:a, call_argument:mod, free_call:binary_exponentiation, if_elif_branch, internal_free_call:binary_exponentiation, literal:1, modulo_operator, multiplication_operator, return
    else:
        b = binary_exponentiation(a, n / 2, mod) # assignment:binary_exponentiation, assignment_lhs_identifier:b, assignment_rhs_atom:2, assignment_rhs_atom:a, assignment_rhs_atom:mod, assignment_rhs_atom:n, binary_operator:Div, call_argument:, call_argument:a, call_argument:mod, free_call:binary_exponentiation, if_else_branch (-> +1), internal_free_call:binary_exponentiation, literal:2, single_assignment:b
        return (b * b) % mod # binary_operator:Mod, binary_operator:Mult, modulo_operator, multiplication_operator, return
p = 701 # assignment:701, assignment_lhs_identifier:p, assignment_rhs_atom:701, literal:701, single_assignment:p, suggest_constant_definition
a = 1000000000 # assignment:1000000000, assignment_lhs_identifier:a, assignment_rhs_atom:1000000000, literal:1000000000, single_assignment:a, suggest_constant_definition
b = 10 # assignment:10, assignment_lhs_identifier:b, assignment_rhs_atom:10, literal:10, single_assignment:b, suggest_constant_definition
print((a / b) % p == (a * binary_exponentiation(b, p - 2, p)) % p) # binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:b, call_argument:p, comparison_operator:Eq, composition, divisibility_test, external_free_call:print, free_call:binary_exponentiation, free_call:print, free_call_without_result:print, internal_free_call:binary_exponentiation, literal:2, modulo_operator, multiplication_operator
print((a / b) % p == (a * b ** (p - 2)) % p) # binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, call_argument:, comparison_operator:Eq, divisibility_test, external_free_call:print, free_call:print, free_call_without_result:print, literal:2, modulo_operator, multiplication_operator

# ----------------------------------------------------------------------------------------
# fibonacci.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, whole_span:72 (-> +71)
import functools # import:functools, import_module:functools
import time # import:time, import_module:time
from decimal import getcontext, Decimal # import:decimal:Decimal, import:decimal:getcontext, import_module:decimal, import_name:Decimal, import_name:getcontext
getcontext().prec = 100 # assignment:100, assignment_rhs_atom:100, external_free_call:getcontext, free_call:getcontext, free_call_without_arguments:getcontext, literal:100
def timer_decorator(func): # closure:timer_decorator (-> +11), function:timer_decorator (-> +11), function_argument:func, function_argument_flavor:arg, function_returning_something:timer_decorator (-> +11), higher_order_function:func (-> +11), nested_function:timer_decorator (-> +11)
    @functools.wraps(func) # call_argument:func, decorated_function:timer_wrapper (-> +9), function:timer_wrapper (-> +9), function_returning_something:timer_wrapper (-> +9), member_call:wraps
    def timer_wrapper(*args, **kwargs): # function_argument:args, function_argument:kwargs, function_argument_flavor:kwarg, function_argument_flavor:vararg
        start = time.time() # assignment:time, assignment_lhs_identifier:start, assignment_rhs_atom:time, member_call:time, single_assignment:start
        func(*args, **kwargs) # call_argument:, external_free_call:func, free_call:func, free_call_without_result:func
        end = time.time() # assignment:time, assignment_lhs_identifier:end, assignment_rhs_atom:time, member_call:time, single_assignment:end
        if int(end - start) > 0: # binary_operator:Sub, call_argument:, comparison_operator:Gt, external_free_call:int, free_call:int, if (-> +3), if_test_atom:0, if_test_atom:end, if_test_atom:start, literal:0
            print(f"Run time for {func.__name__}: {(end - start):0.2f}s") # binary_operator:Sub, call_argument:, external_free_call:print, f_string, free_call:print, free_call_without_result:print, if_then_branch, literal:Str
        else:
            print(f"Run time for {func.__name__}: {(end - start)*1000:0.2f}ms") # binary_operator:Mult, binary_operator:Sub, call_argument:, external_free_call:print, f_string, free_call:print, free_call_without_result:print, if_else_branch, literal:1000, literal:Str, multiplication_operator, suggest_constant_definition
        return func(*args, **kwargs) # call_argument:, external_free_call:func, free_call:func, free_tail_call:func, return
    return timer_wrapper # return:timer_wrapper
class Error(Exception): # class:Error (-> +1)
    pass # null_operation
class ValueTooLargeError(Error): # class:ValueTooLargeError (-> +1)
    pass # null_operation
class ValueTooSmallError(Error): # class:ValueTooSmallError (-> +1)
    pass # null_operation
class ValueLessThanZero(Error): # class:ValueLessThanZero (-> +1)
    pass # null_operation
def _check_number_input(n, min_thresh, max_thresh=None): # function:_check_number_input (-> +22), function_argument:max_thresh, function_argument:min_thresh, function_argument:n, function_argument_flavor:arg, function_returning_something:_check_number_input (-> +22), literal:None
    try: # try (-> +19), try_except:ValueLessThanZero (-> +19), try_except:ValueTooLargeError (-> +19), try_except:ValueTooSmallError (-> +19), try_raise:ValueLessThanZero (-> +19), try_raise:ValueTooLargeError (-> +19), try_raise:ValueTooSmallError (-> +19)
        if n >= min_thresh and max_thresh is None: # boolean_operator:And, comparison_operator:GtE, comparison_operator:Is, if (-> +9), if_test_atom:None, if_test_atom:max_thresh, if_test_atom:min_thresh, if_test_atom:n, literal:None
            return True # if_then_branch, literal:True, return:True
        elif min_thresh <= n <= max_thresh: # chained_comparison:2, chained_inequalities:2, comparison_operator:LtE, if (-> +7), if_test_atom:max_thresh, if_test_atom:min_thresh, if_test_atom:n
            return True # if_elif_branch, literal:True, return:True
        elif n < 0: # comparison_operator:Lt, if (-> +5), if_test_atom:0, if_test_atom:n, literal:0
            raise ValueLessThanZero # if_elif_branch, raise:ValueLessThanZero
        elif n < min_thresh: # comparison_operator:Lt, if (-> +3), if_test_atom:min_thresh, if_test_atom:n
            raise ValueTooSmallError # if_elif_branch, raise:ValueTooSmallError
        elif n > max_thresh: # comparison_operator:Gt, if (-> +1), if_test_atom:max_thresh, if_test_atom:n
            raise ValueTooLargeError # if_elif_branch, raise:ValueTooLargeError
    except ValueLessThanZero: # except:ValueLessThanZero
        print("Incorrect Input: number must not be less than 0") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str
    except ValueTooSmallError: # except:ValueTooSmallError
        print( # external_free_call:print, free_call:print, free_call_without_result:print
            f"Incorrect Input: input number must be > {min_thresh} for the recursive calculation" # call_argument:, f_string, literal:Str
        )
    except ValueTooLargeError: # except:ValueTooLargeError
        print( # external_free_call:print, free_call:print, free_call_without_result:print
            f"Incorrect Input: input number must be < {max_thresh} for the recursive calculation" # call_argument:, f_string, literal:Str
        )
    return False # literal:False, return:False
@timer_decorator # decorated_function:fib_iterative (-> +9), function:fib_iterative (-> +9), function_decorator:timer_decorator (-> +9), function_returning_something:fib_iterative (-> +9)
def fib_iterative(n): # function_argument:n, function_argument_flavor:arg
    n = int(n) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, external_free_call:int, free_call:int, single_assignment:n
    if _check_number_input(n, 2): # call_argument:2, call_argument:n, free_call:_check_number_input, if (-> +6), if_test_atom:2, if_test_atom:n, if_without_else (-> +6), internal_free_call:_check_number_input, literal:2
        seq_out = [0, 1] # assignment, assignment_lhs_identifier:seq_out, assignment_rhs_atom:0, assignment_rhs_atom:1, if_then_branch (-> +5), literal:0, literal:1, literal:List, single_assignment:seq_out
        a, b = 0, 1 # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:0, assignment_rhs_atom:1, literal:0, literal:1, literal:Tuple, parallel_assignment:2
        for _ in range(n - len(seq_out)): # binary_operator:Sub, call_argument:, call_argument:seq_out, composition, external_free_call:len, external_free_call:range, for:_ (-> +2), for_range:_ (-> +2), free_call:len, free_call:range, loop:for (-> +2), loop_with_late_exit:for (-> +2), range:_
            a, b = b, a + b # addition_operator, assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, literal:Tuple, parallel_assignment:2, slide, update:a:b, update:b:a, update_by_assignment:a:b, update_by_assignment:b:a, update_by_assignment_with, update_with
            seq_out.append(b) # call_argument:b, member_call:append, member_call_object:seq_out, member_call_without_result:append, update:seq_out:b, update_by_member_call:seq_out:b, update_by_member_call_with:append, update_with:append
        return seq_out # return:seq_out
@timer_decorator # decorated_function:fib_formula (-> +13), function:fib_formula (-> +13), function_decorator:timer_decorator (-> +13), function_returning_something:fib_formula (-> +13)
def fib_formula(n): # function_argument:n, function_argument_flavor:arg
    seq_out = [0, 1] # assignment, assignment_lhs_identifier:seq_out, assignment_rhs_atom:0, assignment_rhs_atom:1, literal:0, literal:1, literal:List, single_assignment:seq_out
    n = int(n) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:n, call_argument:n, external_free_call:int, free_call:int, single_assignment:n
    if _check_number_input(n, 2, 1000000): # call_argument:1000000, call_argument:2, call_argument:n, free_call:_check_number_input, if (-> +9), if_test_atom:1000000, if_test_atom:2, if_test_atom:n, if_without_else (-> +9), internal_free_call:_check_number_input, literal:1000000, literal:2, suggest_constant_definition
        sqrt = Decimal(math.sqrt(5)) # assignment:Decimal, assignment_lhs_identifier:sqrt, assignment_rhs_atom:5, assignment_rhs_atom:math, call_argument:, call_argument:5, composition, external_free_call:Decimal, free_call:Decimal, if_then_branch (-> +8), literal:5, member_call:sqrt, single_assignment:sqrt, suggest_constant_definition
        phi_1 = Decimal(1 + sqrt) / Decimal(2) # addition_operator, assignment:Div, assignment_lhs_identifier:phi_1, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sqrt, binary_operator:Add, binary_operator:Div, call_argument:, call_argument:2, external_free_call:Decimal, free_call:Decimal, literal:1, literal:2, single_assignment:phi_1
        phi_2 = Decimal(1 - sqrt) / Decimal(2) # assignment:Div, assignment_lhs_identifier:phi_2, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:sqrt, binary_operator:Div, binary_operator:Sub, call_argument:, call_argument:2, external_free_call:Decimal, free_call:Decimal, literal:1, literal:2, single_assignment:phi_2
        for i in range(2, n): # call_argument:2, call_argument:n, external_free_call:range, for:i (-> +4), for_range:2:n (-> +4), free_call:range, literal:2, loop:for (-> +4), loop_with_late_exit:for (-> +4), range:2:n
            temp_out = ((phi_1 ** Decimal(i)) - (phi_2 ** Decimal(i))) * ( # assignment:Mult, assignment_lhs_identifier:temp_out, assignment_rhs_atom:i, assignment_rhs_atom:phi_1, assignment_rhs_atom:phi_2, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, call_argument:i, external_free_call:Decimal, free_call:Decimal, multiplication_operator, single_assignment:temp_out
                Decimal(sqrt) ** Decimal(-1) # assignment_rhs_atom:-1, assignment_rhs_atom:sqrt, binary_operator:Pow, call_argument:-1, call_argument:sqrt, external_free_call:Decimal, free_call:Decimal, literal:-1
            )
            seq_out.append(int(temp_out)) # call_argument:, call_argument:temp_out, composition, external_free_call:int, free_call:int, member_call:append, member_call_object:seq_out, member_call_without_result:append, update:seq_out:temp_out, update_by_member_call:seq_out:temp_out, update_by_member_call_with:append, update_with:append
        return seq_out # return:seq_out

# ----------------------------------------------------------------------------------------
# fibonacci_sequence_recursion.py
# ----------------------------------------------------------------------------------------
def recur_fibo(n): # body_recursive_function:recur_fibo (-> +1), function:recur_fibo (-> +1), function_argument:n, function_argument_flavor:arg, function_returning_something:recur_fibo (-> +1), recursive_function:recur_fibo (-> +1), whole_span:9 (-> +8)
    return n if n <= 1 else recur_fibo(n - 1) + recur_fibo(n - 2) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, comparison_operator:LtE, conditional_expression, free_call:recur_fibo, internal_free_call:recur_fibo, literal:1, literal:2, return
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6), function_without_arguments:main (-> +6)
    limit = int(input("How many terms to include in fibonacci series: ")) # assignment:int, assignment_lhs_identifier:limit, call_argument:, composition, external_free_call:input, external_free_call:int, free_call:input, free_call:int, literal:Str, single_assignment:limit
    if limit > 0: # comparison_operator:Gt, if (-> +4), if_test_atom:0, if_test_atom:limit, literal:0
        print(f"The first {limit} terms of the fibonacci series are as follows:") # call_argument:, external_free_call:print, f_string, free_call:print, free_call_without_result:print, if_then_branch (-> +1), literal:Str
        print([recur_fibo(n) for n in range(limit)]) # call_argument:, call_argument:limit, call_argument:n, composition, comprehension:List, comprehension_for_count:1, external_free_call:print, external_free_call:range, free_call:print, free_call:range, free_call:recur_fibo, free_call_without_result:print, internal_free_call:recur_fibo, range:limit
    else:
        print("Please enter a positive integer: ") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_else_branch, literal:Str

# ----------------------------------------------------------------------------------------
# find_max.py
# ----------------------------------------------------------------------------------------
def find_max(nums): # function:find_max (-> +5), function_argument:nums, function_argument_flavor:arg, function_returning_something:find_max (-> +5), whole_span:8 (-> +7)
    max_num = nums[0] # assignment, assignment_lhs_identifier:max_num, assignment_rhs_atom:0, assignment_rhs_atom:nums, index:0, literal:0, single_assignment:max_num
    for x in nums: # find_best_element:x:max_num (-> +2), for:x (-> +2), for_each (-> +2), loop:for (-> +2), loop_with_late_exit:for (-> +2)
        if x > max_num: # comparison_operator:Gt, if (-> +1), if_test_atom:max_num, if_test_atom:x, if_without_else (-> +1)
            max_num = x # assignment, assignment_lhs_identifier:max_num, assignment_rhs_atom:x, if_then_branch, single_assignment:max_num
    return max_num # return:max_num
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    print(find_max([2, 4, 9, 7, 19, 94, 5])) # call_argument:, composition, external_free_call:print, free_call:find_max, free_call:print, free_call_without_result:print, internal_free_call:find_max, literal:19, literal:2, literal:4, literal:5, literal:7, literal:9, literal:94, literal:List, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# find_max_recursion.py
# ----------------------------------------------------------------------------------------
def find_max(nums, left, right): # body_recursive_function:find_max (-> +6), function:find_max (-> +6), function_argument:left, function_argument:nums, function_argument:right, function_argument_flavor:arg, function_returning_something:find_max (-> +6), recursive_function:find_max (-> +6), whole_span:7 (-> +6)
    if left == right: # comparison_operator:Eq, if (-> +1), if_guard (-> +1), if_test_atom:left, if_test_atom:right, if_without_else (-> +1)
        return nums[left] # if_then_branch, index:left, return
    mid = (left + right) >> 1 # addition_operator, assignment:RShift, assignment_lhs_identifier:mid, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:RShift, literal:1, single_assignment:mid
    left_max = find_max(nums, left, mid) # assignment:find_max, assignment_lhs_identifier:left_max, assignment_rhs_atom:left, assignment_rhs_atom:mid, assignment_rhs_atom:nums, call_argument:left, call_argument:mid, call_argument:nums, free_call:find_max, internal_free_call:find_max, single_assignment:left_max
    right_max = find_max(nums, mid + 1, right) # addition_operator, assignment:find_max, assignment_lhs_identifier:right_max, assignment_rhs_atom:1, assignment_rhs_atom:mid, assignment_rhs_atom:nums, assignment_rhs_atom:right, binary_operator:Add, call_argument:, call_argument:nums, call_argument:right, free_call:find_max, internal_free_call:find_max, literal:1, single_assignment:right_max
    return left_max if left_max >= right_max else right_max # comparison_operator:GtE, conditional_expression, return

# ----------------------------------------------------------------------------------------
# find_min.py
# ----------------------------------------------------------------------------------------
def find_min(nums): # function:find_min (-> +5), function_argument:nums, function_argument_flavor:arg, function_returning_something:find_min (-> +5), whole_span:8 (-> +7)
    min_num = nums[0] # assignment, assignment_lhs_identifier:min_num, assignment_rhs_atom:0, assignment_rhs_atom:nums, index:0, literal:0, single_assignment:min_num
    for num in nums: # find_best_element:num:min_num (-> +2), for:num (-> +2), for_each (-> +2), loop:for (-> +2), loop_with_late_exit:for (-> +2)
        if min_num > num: # comparison_operator:Gt, if (-> +1), if_test_atom:min_num, if_test_atom:num, if_without_else (-> +1)
            min_num = num # assignment, assignment_lhs_identifier:min_num, assignment_rhs_atom:num, if_then_branch, single_assignment:min_num
    return min_num # return:min_num
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    assert find_min([0, 1, 2, 3, 4, 5, -3, 24, -56]) == -56 # assertion, call_argument:, comparison_operator:Eq, free_call:find_min, internal_free_call:find_min, literal:-3, literal:-56, literal:0, literal:1, literal:2, literal:24, literal:3, literal:4, literal:5, literal:List, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# find_min_recursion.py
# ----------------------------------------------------------------------------------------
def find_min(nums, left, right): # body_recursive_function:find_min (-> +6), function:find_min (-> +6), function_argument:left, function_argument:nums, function_argument:right, function_argument_flavor:arg, function_returning_something:find_min (-> +6), recursive_function:find_min (-> +6), whole_span:7 (-> +6)
    if left == right: # comparison_operator:Eq, if (-> +1), if_guard (-> +1), if_test_atom:left, if_test_atom:right, if_without_else (-> +1)
        return nums[left] # if_then_branch, index:left, return
    mid = (left + right) >> 1 # addition_operator, assignment:RShift, assignment_lhs_identifier:mid, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:RShift, literal:1, single_assignment:mid
    left_min = find_min(nums, left, mid) # assignment:find_min, assignment_lhs_identifier:left_min, assignment_rhs_atom:left, assignment_rhs_atom:mid, assignment_rhs_atom:nums, call_argument:left, call_argument:mid, call_argument:nums, free_call:find_min, internal_free_call:find_min, single_assignment:left_min
    right_min = find_min(nums, mid + 1, right) # addition_operator, assignment:find_min, assignment_lhs_identifier:right_min, assignment_rhs_atom:1, assignment_rhs_atom:mid, assignment_rhs_atom:nums, assignment_rhs_atom:right, binary_operator:Add, call_argument:, call_argument:nums, call_argument:right, free_call:find_min, internal_free_call:find_min, literal:1, single_assignment:right_min
    return left_min if left_min <= right_min else right_min # comparison_operator:LtE, conditional_expression, return

# ----------------------------------------------------------------------------------------
# floor.py
# ----------------------------------------------------------------------------------------
def floor(x) -> int: # function:floor (-> +2), function_argument:x, function_argument_flavor:arg, function_returning_something:floor (-> +2), whole_span:3 (-> +2)
    return ( # return
        x if isinstance(x, int) or x - int(x) == 0 else int(x) if x > 0 else int(x - 1) # binary_operator:Sub, boolean_operator:Or, call_argument:, call_argument:int, call_argument:x, comparison_operator:Eq, comparison_operator:Gt, conditional_expression, external_free_call:int, external_free_call:isinstance, free_call:int, free_call:isinstance, literal:0, literal:1
    )

# ----------------------------------------------------------------------------------------
# gaussian.py
# ----------------------------------------------------------------------------------------
from numpy import pi, sqrt, exp # import:numpy:exp, import:numpy:pi, import:numpy:sqrt, import_module:numpy, import_name:exp, import_name:pi, import_name:sqrt, whole_span:3 (-> +2)
def gaussian(x, mu: float = 0.0, sigma: float = 1.0) -> int: # function:gaussian (-> +1), function_argument:mu, function_argument:sigma, function_argument:x, function_argument_flavor:arg, function_returning_something:gaussian (-> +1), literal:0.0, literal:1.0
    return 1 / sqrt(2 * pi * sigma ** 2) * exp(-((x - mu) ** 2) / 2 * sigma ** 2) # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, call_argument:, external_free_call:exp, external_free_call:sqrt, free_call:exp, free_call:sqrt, literal:1, literal:2, multiplication_operator, return, unary_operator:USub

# ----------------------------------------------------------------------------------------
# greatest_common_divisor.py
# ----------------------------------------------------------------------------------------
def greatest_common_divisor(a, b): # function:greatest_common_divisor (-> +1), function_argument:a, function_argument:b, function_argument_flavor:arg, function_returning_something:greatest_common_divisor (-> +1), recursive_function:greatest_common_divisor (-> +1), tail_recursive_function:greatest_common_divisor (-> +1), whole_span:17 (-> +16)
    return b if a == 0 else greatest_common_divisor(b % a, a) # binary_operator:Mod, call_argument:, call_argument:a, comparison_operator:Eq, conditional_expression, free_call:greatest_common_divisor, free_tail_call:greatest_common_divisor, internal_free_call:greatest_common_divisor, literal:0, modulo_operator, return
def gcd_by_iterative(x, y): # function:gcd_by_iterative (-> +3), function_argument:x, function_argument:y, function_argument_flavor:arg, function_returning_something:gcd_by_iterative (-> +3)
    while y: # loop:while (-> +1), loop_with_late_exit:while (-> +1), while (-> +1)
        x, y = y, x % y # assignment, assignment_lhs_identifier:x, assignment_lhs_identifier:y, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Mod, literal:Tuple, modulo_operator, parallel_assignment:2, slide, update:x:y, update:y:x, update_by_assignment:x:y, update_by_assignment:y:x, update_by_assignment_with, update_with
    return x # return:x
def main(): # function:main (-> +10), function_returning_nothing:main (-> +10), function_without_arguments:main (-> +10)
    try: # try (-> +9), try_except:IndexError (-> +9), try_except:UnboundLocalError (-> +9), try_except:ValueError (-> +9)
        nums = input("Enter two integers separated by comma (,): ").split(",") # assignment:split, assignment_lhs_identifier:nums, call_argument:, external_free_call:input, free_call:input, literal:Str, member_call:split, single_assignment:nums
        num_1 = int(nums[0]) # assignment:int, assignment_lhs_identifier:num_1, assignment_rhs_atom:0, assignment_rhs_atom:nums, call_argument:, external_free_call:int, free_call:int, index:0, literal:0, single_assignment:num_1
        num_2 = int(nums[1]) # assignment:int, assignment_lhs_identifier:num_2, assignment_rhs_atom:1, assignment_rhs_atom:nums, call_argument:, external_free_call:int, free_call:int, index:1, literal:1, single_assignment:num_2
        print( # composition, external_free_call:print, free_call:print, free_call_without_result:print
            f"greatest_common_divisor({num_1}, {num_2}) = {greatest_common_divisor(num_1, num_2)}" # call_argument:, call_argument:num_1, call_argument:num_2, f_string, free_call:greatest_common_divisor, internal_free_call:greatest_common_divisor, literal:Str
        )
        print(f"By iterative gcd({num_1}, {num_2}) = {gcd_by_iterative(num_1, num_2)}") # call_argument:, call_argument:num_1, call_argument:num_2, composition, external_free_call:print, f_string, free_call:gcd_by_iterative, free_call:print, free_call_without_result:print, internal_free_call:gcd_by_iterative, literal:Str
    except (IndexError, UnboundLocalError, ValueError): # except:IndexError, except:UnboundLocalError, except:ValueError, literal:Tuple
        print("Wrong input") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str

# ----------------------------------------------------------------------------------------
# hardy_ramanujanalgo.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, whole_span:17 (-> +16)
def exactPrimeFactorCount(n): # function:exactPrimeFactorCount (-> +15), function_argument:n, function_argument_flavor:arg, function_returning_something:exactPrimeFactorCount (-> +15)
    count = 0 # assignment:0, assignment_lhs_identifier:count, assignment_rhs_atom:0, literal:0, single_assignment:count
    if n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:0, if_test_atom:2, if_test_atom:n, if_without_else (-> +3), literal:0, literal:2, modulo_operator
        count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch (-> +2), increment:count, literal:1, update:count:1, update_by_augmented_assignment:count:1, update_by_augmented_assignment_with:Add, update_with:Add
        while n % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, literal:0, literal:2, loop:while (-> +1), loop_with_late_exit:while (-> +1), modulo_operator, while (-> +1)
            n = int(n / 2) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:2, assignment_rhs_atom:n, binary_operator:Div, call_argument:, external_free_call:int, free_call:int, literal:2, single_assignment:n, update:n:2, update_by_assignment:n:2, update_by_assignment_with:int, update_with:int
    i = 3 # assignment:3, assignment_lhs_identifier:i, assignment_rhs_atom:3, literal:3, single_assignment:i, suggest_constant_definition
    while i <= int(math.sqrt(n)): # call_argument:, call_argument:n, comparison_operator:LtE, composition, count_states:count (-> +5), external_free_call:int, free_call:int, loop:while (-> +5), loop_with_late_exit:while (-> +5), member_call:sqrt, while (-> +5)
        if n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, if (-> +3), if_test_atom:0, if_test_atom:i, if_test_atom:n, if_without_else (-> +3), literal:0, modulo_operator
            count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch (-> +2), increment:count, literal:1, update:count:1, update_by_augmented_assignment:count:1, update_by_augmented_assignment_with:Add, update_with:Add
            while n % i == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test, literal:0, loop:while (-> +1), loop_with_late_exit:while (-> +1), modulo_operator, while (-> +1)
                n = int(n / i) # assignment:int, assignment_lhs_identifier:n, assignment_rhs_atom:i, assignment_rhs_atom:n, binary_operator:Div, call_argument:, external_free_call:int, free_call:int, single_assignment:n, update:n:i, update_by_assignment:n:i, update_by_assignment_with:int, update_with:int
        i = i + 2 # addition_operator, assignment:Add, assignment_lhs_identifier:i, assignment_rhs_atom:2, assignment_rhs_atom:i, binary_operator:Add, literal:2, single_assignment:i, suggest_augmented_assignment, update:i:2, update_by_assignment:i:2, update_by_assignment_with:Add, update_with:Add
    if n > 2: # comparison_operator:Gt, if (-> +1), if_test_atom:2, if_test_atom:n, if_without_else (-> +1), literal:2
        count += 1 # assignment_lhs_identifier:count, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment:count, literal:1, update:count:1, update_by_augmented_assignment:count:1, update_by_augmented_assignment_with:Add, update_with:Add
    return count # return:count

# ----------------------------------------------------------------------------------------
# is_square_free.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List, whole_span:3 (-> +2)
def is_square_free(factors: List[int]) -> bool: # function:is_square_free (-> +1), function_argument:factors, function_argument_flavor:arg, function_returning_something:is_square_free (-> +1)
    return len(set(factors)) == len(factors) # call_argument:, call_argument:factors, comparison_operator:Eq, composition, external_free_call:len, external_free_call:set, free_call:len, free_call:set, return

# ----------------------------------------------------------------------------------------
# jaccard_similarity.py
# ----------------------------------------------------------------------------------------
def jaccard_similariy(setA, setB, alternativeUnion=False): # function:jaccard_similariy (-> +14), function_argument:alternativeUnion, function_argument:setA, function_argument:setB, function_argument_flavor:arg, function_returning_something:jaccard_similariy (-> +14), literal:False, whole_span:15 (-> +14)
    if isinstance(setA, set) and isinstance(setB, set): # boolean_operator:And, call_argument:set, call_argument:setA, call_argument:setB, external_free_call:isinstance, free_call:isinstance, if (-> +6), if_guard (-> +6), if_test_atom:set, if_test_atom:setA, if_test_atom:setB, if_without_else (-> +6)
        intersection = len(setA.intersection(setB)) # assignment:len, assignment_lhs_identifier:intersection, assignment_rhs_atom:setA, assignment_rhs_atom:setB, call_argument:, call_argument:setB, composition, external_free_call:len, free_call:len, if_then_branch (-> +5), member_call:intersection, single_assignment:intersection
        if alternativeUnion: # if (-> +3), nested_if:1 (-> +3), verbose_conditional_assignment (-> +3)
            union = len(setA) + len(setB) # addition_operator, assignment:Add, assignment_lhs_identifier:union, assignment_rhs_atom:setA, assignment_rhs_atom:setB, binary_operator:Add, call_argument:setA, call_argument:setB, external_free_call:len, free_call:len, if_then_branch, single_assignment:union
        else:
            union = len(setA.union(setB)) # assignment:len, assignment_lhs_identifier:union, assignment_rhs_atom:setA, assignment_rhs_atom:setB, call_argument:, call_argument:setB, composition, external_free_call:len, free_call:len, if_else_branch, member_call:union, single_assignment:union
        return intersection / union # binary_operator:Div, return
    if isinstance(setA, (list, tuple)) and isinstance(setB, (list, tuple)): # boolean_operator:And, call_argument:, call_argument:setA, call_argument:setB, external_free_call:isinstance, free_call:isinstance, if (-> +6), if_test_atom:list, if_test_atom:setA, if_test_atom:setB, if_test_atom:tuple, if_without_else (-> +6), literal:Tuple
        intersection = [element for element in setA if element in setB] # assignment, assignment_lhs_identifier:intersection, assignment_rhs_atom:element, assignment_rhs_atom:setA, assignment_rhs_atom:setB, comparison_operator:In, comprehension:List, comprehension_for_count:1, filtered_comprehension, if_then_branch (-> +5), single_assignment:intersection
        if alternativeUnion: # if (-> +3), nested_if:1 (-> +3), verbose_conditional_assignment (-> +3)
            union = len(setA) + len(setB) # addition_operator, assignment:Add, assignment_lhs_identifier:union, assignment_rhs_atom:setA, assignment_rhs_atom:setB, binary_operator:Add, call_argument:setA, call_argument:setB, external_free_call:len, free_call:len, if_then_branch, single_assignment:union
        else:
            union = setA + [element for element in setB if element not in setA] # addition_operator, assignment:Add, assignment_lhs_identifier:union, assignment_rhs_atom:element, assignment_rhs_atom:setA, assignment_rhs_atom:setB, binary_operator:Add, comparison_operator:NotIn, comprehension:List, comprehension_for_count:1, filtered_comprehension, if_else_branch, single_assignment:union
        return len(intersection) / len(union) # binary_operator:Div, call_argument:intersection, call_argument:union, external_free_call:len, free_call:len, return

# ----------------------------------------------------------------------------------------
# karatsuba.py
# ----------------------------------------------------------------------------------------
def karatsuba(a, b): # body_recursive_function:karatsuba (-> +11), function:karatsuba (-> +11), function_argument:a, function_argument:b, function_argument_flavor:arg, function_returning_something:karatsuba (-> +11), recursive_function:karatsuba (-> +11), whole_span:14 (-> +13)
    if len(str(a)) == 1 or len(str(b)) == 1: # boolean_operator:Or, call_argument:, call_argument:a, call_argument:b, comparison_operator:Eq, composition, external_free_call:len, external_free_call:str, free_call:len, free_call:str, if (-> +10), if_test_atom:1, if_test_atom:a, if_test_atom:b, literal:1
        return a * b # binary_operator:Mult, if_then_branch, multiplication_operator, return
    else:
        m1 = max(len(str(a)), len(str(b))) # assignment:max, assignment_lhs_identifier:m1, assignment_rhs_atom:a, assignment_rhs_atom:b, call_argument:, call_argument:a, call_argument:b, composition, external_free_call:len, external_free_call:max, external_free_call:str, free_call:len, free_call:max, free_call:str, if_else_branch (-> +7), single_assignment:m1
        m2 = m1 // 2 # assignment:FloorDiv, assignment_lhs_identifier:m2, assignment_rhs_atom:2, assignment_rhs_atom:m1, binary_operator:FloorDiv, literal:2, single_assignment:m2
        a1, a2 = divmod(a, 10 ** m2) # assignment:divmod, assignment_lhs_identifier:a1, assignment_lhs_identifier:a2, assignment_rhs_atom:10, assignment_rhs_atom:a, assignment_rhs_atom:m2, binary_operator:Pow, call_argument:, call_argument:a, external_free_call:divmod, free_call:divmod, literal:10, literal:Tuple, parallel_assignment:2, suggest_constant_definition
        b1, b2 = divmod(b, 10 ** m2) # assignment:divmod, assignment_lhs_identifier:b1, assignment_lhs_identifier:b2, assignment_rhs_atom:10, assignment_rhs_atom:b, assignment_rhs_atom:m2, binary_operator:Pow, call_argument:, call_argument:b, external_free_call:divmod, free_call:divmod, literal:10, literal:Tuple, parallel_assignment:2, suggest_constant_definition
        x = karatsuba(a2, b2) # assignment:karatsuba, assignment_lhs_identifier:x, assignment_rhs_atom:a2, assignment_rhs_atom:b2, call_argument:a2, call_argument:b2, free_call:karatsuba, internal_free_call:karatsuba, single_assignment:x
        y = karatsuba((a1 + a2), (b1 + b2)) # addition_operator, assignment:karatsuba, assignment_lhs_identifier:y, assignment_rhs_atom:a1, assignment_rhs_atom:a2, assignment_rhs_atom:b1, assignment_rhs_atom:b2, binary_operator:Add, call_argument:, free_call:karatsuba, internal_free_call:karatsuba, single_assignment:y
        z = karatsuba(a1, b1) # assignment:karatsuba, assignment_lhs_identifier:z, assignment_rhs_atom:a1, assignment_rhs_atom:b1, call_argument:a1, call_argument:b1, free_call:karatsuba, internal_free_call:karatsuba, single_assignment:z
        return (z * 10 ** (2 * m2)) + ((y - z - x) * 10 ** (m2)) + (x) # addition_operator, binary_operator:Add, binary_operator:Mult, binary_operator:Pow, binary_operator:Sub, literal:10, literal:2, multiplication_operator, return, suggest_constant_definition
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    print(karatsuba(15463, 23489)) # call_argument:, call_argument:15463, call_argument:23489, composition, external_free_call:print, free_call:karatsuba, free_call:print, free_call_without_result:print, internal_free_call:karatsuba, literal:15463, literal:23489, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# kth_lexicographic_permutation.py
# ----------------------------------------------------------------------------------------
def kthPermutation(k, n): # function:kthPermutation (-> +13), function_argument:k, function_argument:n, function_argument_flavor:arg, function_returning_something:kthPermutation (-> +13), whole_span:14 (-> +13)
    factorials = [1] # assignment, assignment_lhs_identifier:factorials, assignment_rhs_atom:1, literal:1, literal:List, single_assignment:factorials
    for i in range(2, n): # call_argument:2, call_argument:n, external_free_call:range, for:i (-> +1), for_range:2:n (-> +1), free_call:range, literal:2, loop:for (-> +1), loop_with_late_exit:for (-> +1), range:2:n
        factorials.append(factorials[-1] * i) # binary_operator:Mult, call_argument:, index:-1, literal:-1, member_call:append, member_call_object:factorials, member_call_without_result:append, multiplication_operator, negative_index:-1
    assert 0 <= k < factorials[-1] * n, "k out of bounds" # assertion, binary_operator:Mult, chained_comparison:2, comparison_operator:Lt, comparison_operator:LtE, index:-1, literal:-1, literal:0, literal:Str, multiplication_operator, negative_index:-1, yoda_comparison:LtE
    permutation = [] # assignment, assignment_lhs_identifier:permutation, empty_literal:List, literal:List, single_assignment:permutation
    elements = list(range(n)) # assignment:list, assignment_lhs_identifier:elements, assignment_rhs_atom:n, call_argument:, call_argument:n, composition, external_free_call:list, external_free_call:range, free_call:list, free_call:range, range:n, single_assignment:elements
    while factorials: # loop:while (-> +4), loop_with_late_exit:while (-> +4), while (-> +4)
        factorial = factorials.pop() # assignment:pop, assignment_lhs_identifier:factorial, assignment_rhs_atom:factorials, member_call:pop, single_assignment:factorial
        number, k = divmod(k, factorial) # assignment:divmod, assignment_lhs_identifier:k, assignment_lhs_identifier:number, assignment_rhs_atom:factorial, assignment_rhs_atom:k, call_argument:factorial, call_argument:k, external_free_call:divmod, free_call:divmod, literal:Tuple, parallel_assignment:2, update:k:factorial, update_by_assignment:k:factorial, update_by_assignment_with:divmod, update_with:divmod
        permutation.append(elements[number]) # call_argument:, index:number, member_call:append, member_call_object:permutation, member_call_without_result:append
        elements.remove(elements[number]) # call_argument:, index:number, member_call:remove, member_call_object:elements, member_call_without_result:remove
    permutation.append(elements[0]) # call_argument:, index:0, literal:0, member_call:append, member_call_object:permutation, member_call_without_result:append
    return permutation # return:permutation

# ----------------------------------------------------------------------------------------
# largest_of_very_large_numbers.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, whole_span:9 (-> +8)
def res(x, y): # function:res (-> +7), function_argument:x, function_argument:y, function_argument_flavor:arg, function_returning_something:res (-> +7)
    if 0 not in (x, y): # comparison_operator:NotIn, if (-> +6), if_test_atom:0, if_test_atom:x, if_test_atom:y, literal:0, literal:Tuple
        return y * math.log10(x) # binary_operator:Mult, call_argument:x, if_then_branch, member_call:log10, multiplication_operator, return
    else:
        if x == 0: # comparison_operator:Eq, if (-> +3), if_test_atom:0, if_test_atom:x, literal:0
            return 0 # if_elif_branch, literal:0, return:0
        elif y == 0: # comparison_operator:Eq, if (-> +1), if_test_atom:0, if_test_atom:y, literal:0
            return 1 # if_elif_branch, literal:1, return:1

# ----------------------------------------------------------------------------------------
# least_common_multiple.py
# ----------------------------------------------------------------------------------------
import unittest # import:unittest, import_module:unittest, whole_span:25 (-> +24)
def find_lcm(first_num: int, second_num: int) -> int: # function:find_lcm (-> +5), function_argument:first_num, function_argument:second_num, function_argument_flavor:arg, function_returning_something:find_lcm (-> +5)
    max_num = first_num if first_num >= second_num else second_num # assignment, assignment_lhs_identifier:max_num, assignment_rhs_atom:first_num, assignment_rhs_atom:second_num, compact_conditional_assignment, comparison_operator:GtE, conditional_expression, single_assignment:max_num
    common_mult = max_num # assignment, assignment_lhs_identifier:common_mult, assignment_rhs_atom:max_num, single_assignment:common_mult
    while (common_mult % first_num > 0) or (common_mult % second_num > 0): # binary_operator:Mod, boolean_operator:Or, comparison_operator:Gt, literal:0, loop:while (-> +1), loop_with_late_exit:while (-> +1), modulo_operator, while (-> +1)
        common_mult += max_num # assignment_lhs_identifier:common_mult, assignment_rhs_atom:max_num, augmented_assignment:Add, update:common_mult:max_num, update_by_augmented_assignment:common_mult:max_num, update_by_augmented_assignment_with:Add, update_with:Add
    return common_mult # return:common_mult
class TestLeastCommonMultiple(unittest.TestCase): # class:TestLeastCommonMultiple (-> +17)
    test_inputs = [ # assignment, assignment_lhs_identifier:test_inputs, literal:List, single_assignment:test_inputs
        (10, 20), # assignment_rhs_atom:10, assignment_rhs_atom:20, literal:10, literal:20, literal:Tuple, suggest_constant_definition
        (13, 15), # assignment_rhs_atom:13, assignment_rhs_atom:15, literal:13, literal:15, literal:Tuple, suggest_constant_definition
        (4, 31), # assignment_rhs_atom:31, assignment_rhs_atom:4, literal:31, literal:4, literal:Tuple, suggest_constant_definition
        (10, 42), # assignment_rhs_atom:10, assignment_rhs_atom:42, literal:10, literal:42, literal:Tuple, suggest_constant_definition
        (43, 34), # assignment_rhs_atom:34, assignment_rhs_atom:43, literal:34, literal:43, literal:Tuple, suggest_constant_definition
        (5, 12), # assignment_rhs_atom:12, assignment_rhs_atom:5, literal:12, literal:5, literal:Tuple, suggest_constant_definition
        (12, 25), # assignment_rhs_atom:12, assignment_rhs_atom:25, literal:12, literal:25, literal:Tuple, suggest_constant_definition
        (10, 25), # assignment_rhs_atom:10, assignment_rhs_atom:25, literal:10, literal:25, literal:Tuple, suggest_constant_definition
        (6, 9), # assignment_rhs_atom:6, assignment_rhs_atom:9, literal:6, literal:9, literal:Tuple, suggest_constant_definition
    ]
    expected_results = [20, 195, 124, 210, 1462, 60, 300, 50, 18] # assignment, assignment_lhs_identifier:expected_results, assignment_rhs_atom:124, assignment_rhs_atom:1462, assignment_rhs_atom:18, assignment_rhs_atom:195, assignment_rhs_atom:20, assignment_rhs_atom:210, assignment_rhs_atom:300, assignment_rhs_atom:50, assignment_rhs_atom:60, literal:124, literal:1462, literal:18, literal:195, literal:20, literal:210, literal:300, literal:50, literal:60, literal:List, single_assignment:expected_results, suggest_constant_definition
    def test_lcm_function(self): # function:test_lcm_function (-> +4), function_argument:self, function_argument_flavor:arg, function_returning_nothing:test_lcm_function (-> +4), instance_method:test_lcm_function (-> +4), method:test_lcm_function (-> +4)
        for i, (first_num, second_num) in enumerate(self.test_inputs): # call_argument:, external_free_call:enumerate, for:first_num (-> +3), for:i (-> +3), for:second_num (-> +3), for_indexes_elements (-> +3), free_call:enumerate, literal:Tuple, loop:for (-> +3), loop_with_late_exit:for (-> +3)
            actual_result = find_lcm(first_num, second_num) # assignment:find_lcm, assignment_lhs_identifier:actual_result, assignment_rhs_atom:first_num, assignment_rhs_atom:second_num, call_argument:first_num, call_argument:second_num, free_call:find_lcm, internal_free_call:find_lcm, single_assignment:actual_result
            with self.subTest(i=i): # member_call:subTest
                self.assertEqual(actual_result, self.expected_results[i]) # call_argument:, call_argument:actual_result, index:i, member_call:assertEqual, member_call_object:self, member_call_without_result:assertEqual

# ----------------------------------------------------------------------------------------
# lucas_series.py
# ----------------------------------------------------------------------------------------
def recur_luc(n): # body_recursive_function:recur_luc (-> +5), function:recur_luc (-> +5), function_argument:n, function_argument_flavor:arg, function_returning_something:recur_luc (-> +5), recursive_function:recur_luc (-> +5), whole_span:6 (-> +5)
    if n == 1: # comparison_operator:Eq, if (-> +1), if_guard (-> +1), if_test_atom:1, if_test_atom:n, if_without_else (-> +1), literal:1
        return n # if_then_branch, return:n
    if n == 0: # comparison_operator:Eq, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0
        return 2 # if_then_branch, literal:2, return:2
    return recur_luc(n - 1) + recur_luc(n - 2) # addition_operator, binary_operator:Add, binary_operator:Sub, call_argument:, free_call:recur_luc, internal_free_call:recur_luc, literal:1, literal:2, return

# ----------------------------------------------------------------------------------------
# matrix_exponentiation.py
# ----------------------------------------------------------------------------------------
import timeit # import:timeit, import_module:timeit, whole_span:67 (-> +66)
class Matrix(object): # class:Matrix (-> +14)
    def __init__(self, arg): # function:__init__ (-> +6), function_argument:arg, function_argument:self, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +6), instance_method:__init__ (-> +6), method:__init__ (-> +6)
        if isinstance(arg, list): # call_argument:arg, call_argument:list, external_free_call:isinstance, free_call:isinstance, if (-> +5), if_test_atom:arg, if_test_atom:list
            self.t = arg # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:arg, if_then_branch (-> +1)
            self.n = len(arg) # assignment:len, assignment_lhs_identifier:self, assignment_rhs_atom:arg, call_argument:arg, external_free_call:len, free_call:len
        else:
            self.n = arg # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:arg, if_else_branch (-> +1)
            self.t = [[0 for _ in range(self.n)] for _ in range(self.n)] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:0, assignment_rhs_atom:_, assignment_rhs_atom:self, call_argument:, comprehension:List, comprehension_for_count:1, external_free_call:range, free_call:range, literal:0, range:_, update:self:0, update:self:_, update_by_assignment:self:0, update_by_assignment:self:_, update_by_assignment_with, update_with
    def __mul__(self, b): # function:__mul__ (-> +6), function_argument:b, function_argument:self, function_argument_flavor:arg, function_returning_something:__mul__ (-> +6), instance_method:__mul__ (-> +6), method:__mul__ (-> +6)
        matrix = Matrix(self.n) # assignment:Matrix, assignment_lhs_identifier:matrix, assignment_rhs_atom:self, call_argument:, external_free_call:Matrix, free_call:Matrix, single_assignment:matrix
        for i in range(self.n): # call_argument:, external_free_call:range, for:i (-> +3), for_range:_ (-> +3), free_call:range, loop:for (-> +3), loop_with_late_exit:for (-> +3), range:_, square_nested_for (-> +3)
            for j in range(self.n): # call_argument:, external_free_call:range, for:j (-> +2), for_range:_ (-> +2), free_call:range, loop:for (-> +2), loop_with_late_exit:for (-> +2), nested_for:1 (-> +2), range:_, square_nested_for (-> +2)
                for k in range(self.n): # call_argument:, external_free_call:range, for:k (-> +1), for_range:_ (-> +1), free_call:range, loop:for (-> +1), loop_with_late_exit:for (-> +1), nested_for:2 (-> +1), range:_
                    matrix.t[i][j] += self.t[i][k] * b.t[k][j] # assignment_rhs_atom:b, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:k, assignment_rhs_atom:self, augmented_assignment:Add, binary_operator:Mult, index:i, index:j, index:k, multiplication_operator, nested_index:2, subscript_augmented_assignment:Add
        return matrix # return:matrix
def modular_exponentiation(a, b): # function:modular_exponentiation (-> +7), function_argument:a, function_argument:b, function_argument_flavor:arg, function_returning_something:modular_exponentiation (-> +7)
    matrix = Matrix([[1, 0], [0, 1]]) # assignment:Matrix, assignment_lhs_identifier:matrix, assignment_rhs_atom:0, assignment_rhs_atom:1, call_argument:, external_free_call:Matrix, free_call:Matrix, literal:0, literal:1, literal:List, single_assignment:matrix
    while b > 0: # comparison_operator:Gt, literal:0, loop:while (-> +4), loop_with_late_exit:while (-> +4), while (-> +4)
        if b & 1: # binary_operator:BitAnd, if (-> +1), if_test_atom:1, if_test_atom:b, if_without_else (-> +1), literal:1
            matrix *= a # assignment_lhs_identifier:matrix, assignment_rhs_atom:a, augmented_assignment:Mult, if_then_branch, update:matrix:a, update_by_augmented_assignment:matrix:a, update_by_augmented_assignment_with:Mult, update_with:Mult
        a *= a # assignment_lhs_identifier:a, assignment_rhs_atom:a, augmented_assignment:Mult, update:a:a, update_by_augmented_assignment:a:a, update_by_augmented_assignment_with:Mult, update_with:Mult
        b >>= 1 # assignment_lhs_identifier:b, assignment_rhs_atom:1, augmented_assignment:RShift, literal:1, update:b:1, update_by_augmented_assignment:b:1, update_by_augmented_assignment_with:RShift, update_with:RShift
    return matrix # return:matrix
def fibonacci_with_matrix_exponentiation(n, f1, f2): # function:fibonacci_with_matrix_exponentiation (-> +7), function_argument:f1, function_argument:f2, function_argument:n, function_argument_flavor:arg, function_returning_something:fibonacci_with_matrix_exponentiation (-> +7)
    if n == 1: # comparison_operator:Eq, if (-> +3), if_test_atom:1, if_test_atom:n, literal:1
        return f1 # if_then_branch, return:f1
    elif n == 2: # comparison_operator:Eq, if (-> +1), if_test_atom:2, if_test_atom:n, literal:2
        return f2 # if_elif_branch, return:f2
    matrix = Matrix([[1, 1], [1, 0]]) # assignment:Matrix, assignment_lhs_identifier:matrix, assignment_rhs_atom:0, assignment_rhs_atom:1, call_argument:, external_free_call:Matrix, free_call:Matrix, literal:0, literal:1, literal:List, single_assignment:matrix
    matrix = modular_exponentiation(matrix, n - 2) # assignment:modular_exponentiation, assignment_lhs_identifier:matrix, assignment_rhs_atom:2, assignment_rhs_atom:matrix, assignment_rhs_atom:n, binary_operator:Sub, call_argument:, call_argument:matrix, free_call:modular_exponentiation, internal_free_call:modular_exponentiation, literal:2, single_assignment:matrix, update:matrix:2, update:matrix:n, update_by_assignment:matrix:2, update_by_assignment:matrix:n, update_by_assignment_with:modular_exponentiation, update_with:modular_exponentiation
    return f2 * matrix.t[0][0] + f1 * matrix.t[0][1] # addition_operator, binary_operator:Add, binary_operator:Mult, index:0, index:1, literal:0, literal:1, multiplication_operator, nested_index:2, return
def simple_fibonacci(n, f1, f2): # function:simple_fibonacci (-> +11), function_argument:f1, function_argument:f2, function_argument:n, function_argument_flavor:arg, function_returning_something:simple_fibonacci (-> +11)
    if n == 1: # comparison_operator:Eq, if (-> +3), if_test_atom:1, if_test_atom:n, literal:1
        return f1 # if_then_branch, return:f1
    elif n == 2: # comparison_operator:Eq, if (-> +1), if_test_atom:2, if_test_atom:n, literal:2
        return f2 # if_elif_branch, return:f2
    fn_1 = f1 # assignment, assignment_lhs_identifier:fn_1, assignment_rhs_atom:f1, single_assignment:fn_1
    fn_2 = f2 # assignment, assignment_lhs_identifier:fn_2, assignment_rhs_atom:f2, single_assignment:fn_2
    n -= 2 # assignment_lhs_identifier:n, assignment_rhs_atom:2, augmented_assignment:Sub, literal:2, update:n:2, update_by_augmented_assignment:n:2, update_by_augmented_assignment_with:Sub, update_with:Sub
    while n > 0: # comparison_operator:Gt, literal:0, loop:while (-> +2), loop_with_late_exit:while (-> +2), while (-> +2)
        fn_1, fn_2 = fn_1 + fn_2, fn_1 # addition_operator, assignment, assignment_lhs_identifier:fn_1, assignment_lhs_identifier:fn_2, assignment_rhs_atom:fn_1, assignment_rhs_atom:fn_2, binary_operator:Add, literal:Tuple, parallel_assignment:2, update:fn_1:fn_2, update:fn_2:fn_1, update_by_assignment:fn_1:fn_2, update_by_assignment:fn_2:fn_1, update_by_assignment_with, update_with
        n -= 1 # assignment_lhs_identifier:n, assignment_rhs_atom:1, augmented_assignment:Sub, literal:1, update:n:1, update_by_augmented_assignment:n:1, update_by_augmented_assignment_with:Sub, update_with:Sub
    return fn_1 # return:fn_1
def matrix_exponentiation_time(): # function:matrix_exponentiation_time (-> +8), function_returning_something:matrix_exponentiation_time (-> +8), function_without_arguments:matrix_exponentiation_time (-> +8)
    setup = """ # assignment, assignment_lhs_identifier:setup, single_assignment:setup
from random import randint
from __main__ import fibonacci_with_matrix_exponentiation
""" # literal:Str
    code = "fibonacci_with_matrix_exponentiation(randint(1,70000), 1, 1)" # assignment, assignment_lhs_identifier:code, literal:Str, single_assignment:code
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100) # assignment:timeit, assignment_lhs_identifier:exec_time, assignment_rhs_atom:100, assignment_rhs_atom:code, assignment_rhs_atom:setup, assignment_rhs_atom:timeit, literal:100, member_call:timeit, single_assignment:exec_time, suggest_constant_definition
    print("With matrix exponentiation the average execution time is ", exec_time / 100) # binary_operator:Div, call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:100, literal:Str, suggest_constant_definition
    return exec_time # return:exec_time
def simple_fibonacci_time(): # function:simple_fibonacci_time (-> +10), function_returning_something:simple_fibonacci_time (-> +10), function_without_arguments:simple_fibonacci_time (-> +10)
    setup = """ # assignment, assignment_lhs_identifier:setup, single_assignment:setup
from random import randint
from __main__ import simple_fibonacci
""" # literal:Str
    code = "simple_fibonacci(randint(1,70000), 1, 1)" # assignment, assignment_lhs_identifier:code, literal:Str, single_assignment:code
    exec_time = timeit.timeit(setup=setup, stmt=code, number=100) # assignment:timeit, assignment_lhs_identifier:exec_time, assignment_rhs_atom:100, assignment_rhs_atom:code, assignment_rhs_atom:setup, assignment_rhs_atom:timeit, literal:100, member_call:timeit, single_assignment:exec_time, suggest_constant_definition
    print( # external_free_call:print, free_call:print, free_call_without_result:print
        "Without matrix exponentiation the average execution time is ", exec_time / 100 # binary_operator:Div, call_argument:, literal:100, literal:Str, suggest_constant_definition
    )
    return exec_time # return:exec_time
def main(): # function:main (-> +2), function_returning_nothing:main (-> +2), function_without_arguments:main (-> +2)
    matrix_exponentiation_time() # free_call:matrix_exponentiation_time, free_call_without_arguments:matrix_exponentiation_time, free_call_without_result:matrix_exponentiation_time, internal_free_call:matrix_exponentiation_time
    simple_fibonacci_time() # free_call:simple_fibonacci_time, free_call_without_arguments:simple_fibonacci_time, free_call_without_result:simple_fibonacci_time, internal_free_call:simple_fibonacci_time

# ----------------------------------------------------------------------------------------
# mobius_function.py
# ----------------------------------------------------------------------------------------
from maths.prime_factors import prime_factors # import:maths.prime_factors:prime_factors, import_module:maths.prime_factors, import_name:prime_factors, whole_span:7 (-> +6)
from maths.is_square_free import is_square_free # import:maths.is_square_free:is_square_free, import_module:maths.is_square_free, import_name:is_square_free
def mobius(n: int) -> int: # function:mobius (-> +4), function_argument:n, function_argument_flavor:arg, function_returning_something:mobius (-> +4)
    factors = prime_factors(n) # assignment:prime_factors, assignment_lhs_identifier:factors, assignment_rhs_atom:n, call_argument:n, external_free_call:prime_factors, free_call:prime_factors, single_assignment:factors
    if is_square_free(factors): # call_argument:factors, external_free_call:is_square_free, free_call:is_square_free, if (-> +1), if_guard (-> +1), if_test_atom:factors, if_without_else (-> +1)
        return -1 if len(factors) % 2 else 1 # binary_operator:Mod, call_argument:factors, conditional_expression, external_free_call:len, free_call:len, if_then_branch, literal:-1, literal:1, literal:2, modulo_operator, return
    return 0 # literal:0, return:0

# ----------------------------------------------------------------------------------------
# modular_exponential.py
# ----------------------------------------------------------------------------------------
def modular_exponential(base, power, mod): # function:modular_exponential (-> +10), function_argument:base, function_argument:mod, function_argument:power, function_argument_flavor:arg, function_returning_something:modular_exponential (-> +10), whole_span:13 (-> +12)
    if power < 0: # comparison_operator:Lt, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:power, if_without_else (-> +1), literal:0
        return -1 # if_then_branch, literal:-1, return:-1
    base %= mod # assignment_lhs_identifier:base, assignment_rhs_atom:mod, augmented_assignment:Mod, update:base:mod, update_by_augmented_assignment:base:mod, update_by_augmented_assignment_with:Mod, update_with:Mod
    result = 1 # assignment:1, assignment_lhs_identifier:result, assignment_rhs_atom:1, literal:1, single_assignment:result
    while power > 0: # comparison_operator:Gt, literal:0, loop:while (-> +4), loop_with_late_exit:while (-> +4), while (-> +4)
        if power & 1: # binary_operator:BitAnd, if (-> +1), if_test_atom:1, if_test_atom:power, if_without_else (-> +1), literal:1
            result = (result * base) % mod # assignment:Mod, assignment_lhs_identifier:result, assignment_rhs_atom:base, assignment_rhs_atom:mod, assignment_rhs_atom:result, binary_operator:Mod, binary_operator:Mult, if_then_branch, modulo_operator, multiplication_operator, single_assignment:result, update:result:base, update:result:mod, update_by_assignment:result:base, update_by_assignment:result:mod, update_by_assignment_with:Mod, update_with:Mod
        power = power >> 1 # assignment:RShift, assignment_lhs_identifier:power, assignment_rhs_atom:1, assignment_rhs_atom:power, binary_operator:RShift, literal:1, single_assignment:power, suggest_augmented_assignment, update:power:1, update_by_assignment:power:1, update_by_assignment_with:RShift, update_with:RShift
        base = (base * base) % mod # assignment:Mod, assignment_lhs_identifier:base, assignment_rhs_atom:base, assignment_rhs_atom:mod, binary_operator:Mod, binary_operator:Mult, modulo_operator, multiplication_operator, single_assignment:base, update:base:mod, update_by_assignment:base:mod, update_by_assignment_with:Mod, update_with:Mod
    return result # return:result
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    print(modular_exponential(3, 200, 13)) # call_argument:, call_argument:13, call_argument:200, call_argument:3, composition, external_free_call:print, free_call:modular_exponential, free_call:print, free_call_without_result:print, internal_free_call:modular_exponential, literal:13, literal:200, literal:3, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# newton_raphson.py
# ----------------------------------------------------------------------------------------
import math as m # import:math, import_module:math, whole_span:21 (-> +20)
def calc_derivative(f, a, h=0.001): # function:calc_derivative (-> +1), function_argument:a, function_argument:f, function_argument:h, function_argument_flavor:arg, function_returning_something:calc_derivative (-> +1), higher_order_function:f (-> +1), literal:0.001
    return (f(a + h) - f(a - h)) / (2 * h) # addition_operator, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, external_free_call:f, free_call:f, literal:2, multiplication_operator, return
def newton_raphson(f, x0=0, maxiter=100, step=0.0001, maxerror=1e-6, logsteps=False): # function:newton_raphson (-> +17), function_argument:f, function_argument:logsteps, function_argument:maxerror, function_argument:maxiter, function_argument:step, function_argument:x0, function_argument_flavor:arg, function_returning_something:newton_raphson (-> +17), higher_order_function:f (-> +17), literal:0, literal:0.0001, literal:100, literal:1e-06, literal:False
    a = x0 # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:x0, single_assignment:a
    steps = [a] # assignment, assignment_lhs_identifier:steps, assignment_rhs_atom:a, literal:List, single_assignment:steps
    error = abs(f(a)) # assignment:abs, assignment_lhs_identifier:error, assignment_rhs_atom:a, call_argument:, call_argument:a, composition, external_free_call:abs, external_free_call:f, free_call:abs, free_call:f, single_assignment:error
    f1 = lambda x: calc_derivative(f, x, h=step) # assignment, assignment_lhs_identifier:f1, assignment_rhs_atom:f, assignment_rhs_atom:step, assignment_rhs_atom:x, call_argument:f, call_argument:x, free_call:calc_derivative, function_argument:x, function_argument_flavor:arg, internal_free_call:calc_derivative, lambda_function, single_assignment:f1
    for _ in range(maxiter): # call_argument:maxiter, external_free_call:range, for:_ (-> +9), for_range:maxiter (-> +9), free_call:range, loop:for (-> +9), loop_with_break:for (-> +9), loop_with_early_exit:for:break (-> +9), loop_with_early_exit:for:raise (-> +9), loop_with_else:for (-> +9), loop_with_raise:for (-> +9), range:maxiter
        if f1(a) == 0: # call_argument:a, comparison_operator:Eq, external_free_call:f1, free_call:f1, if (-> +1), if_test_atom:0, if_test_atom:a, if_without_else (-> +1), literal:0
            raise ValueError("No converging solution found") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
        a = a - f(a) / f1(a) # assignment:Sub, assignment_lhs_identifier:a, assignment_rhs_atom:a, binary_operator:Div, binary_operator:Sub, call_argument:a, external_free_call:f, external_free_call:f1, free_call:f, free_call:f1, single_assignment:a, suggest_augmented_assignment
        if logsteps: # if (-> +1), if_without_else (-> +1)
            steps.append(a) # call_argument:a, if_then_branch, member_call:append, member_call_object:steps, member_call_without_result:append, update:steps:a, update_by_member_call:steps:a, update_by_member_call_with:append, update_with:append
        if error < maxerror: # comparison_operator:Lt, if (-> +1), if_test_atom:error, if_test_atom:maxerror, if_without_else (-> +1)
            break # break, if_then_branch
    else:
        raise ValueError("Iteration limit reached, no converging solution found") # call_argument:, external_free_call:ValueError, free_call:ValueError, literal:Str, loop_else, raise:ValueError
    if logsteps: # if (-> +1), if_guard (-> +1), if_without_else (-> +1)
        return a, error, steps # if_then_branch, literal:Tuple, return
    return a, error # literal:Tuple, return

# ----------------------------------------------------------------------------------------
# perfect_square.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, whole_span:3 (-> +2)
def perfect_square(num: int) -> bool: # function:perfect_square (-> +1), function_argument:num, function_argument_flavor:arg, function_returning_something:perfect_square (-> +1)
    return math.sqrt(num) * math.sqrt(num) == num # binary_operator:Mult, call_argument:num, comparison_operator:Eq, member_call:sqrt, multiplication_operator, return

# ----------------------------------------------------------------------------------------
# polynomial_evaluation.py
# ----------------------------------------------------------------------------------------
from typing import Sequence # import:typing:Sequence, import_module:typing, import_name:Sequence, whole_span:8 (-> +7)
def evaluate_poly(poly: Sequence[float], x: float) -> float: # function:evaluate_poly (-> +1), function_argument:poly, function_argument:x, function_argument_flavor:arg, function_returning_something:evaluate_poly (-> +1)
    return sum(c * (x ** i) for i, c in enumerate(poly)) # binary_operator:Mult, binary_operator:Pow, call_argument:, call_argument:poly, composition, comprehension:Generator, comprehension_for_count:1, external_free_call:enumerate, external_free_call:sum, free_call:enumerate, free_call:sum, free_tail_call:sum, literal:Tuple, multiplication_operator, return
def horner(poly: Sequence[float], x: float) -> float: # function:horner (-> +4), function_argument:poly, function_argument:x, function_argument_flavor:arg, function_returning_something:horner (-> +4)
    result = 0.0 # assignment:0.0, assignment_lhs_identifier:result, assignment_rhs_atom:0.0, literal:0.0, single_assignment:result, suggest_constant_definition
    for coeff in reversed(poly): # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), call_argument:poly, external_free_call:reversed, for:coeff (-> +1), free_call:reversed, loop:for (-> +1), loop_with_late_exit:for (-> +1)
        result = result * x + coeff # addition_operator, assignment:Add, assignment_lhs_identifier:result, assignment_rhs_atom:coeff, assignment_rhs_atom:result, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, multiplication_operator, single_assignment:result, update:result:coeff, update:result:x, update_by_assignment:result:coeff, update_by_assignment:result:x, update_by_assignment_with:Add, update_with:Add
    return result # return:result

# ----------------------------------------------------------------------------------------
# prime_check.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, whole_span:36 (-> +35)
import unittest # import:unittest, import_module:unittest
def prime_check(number): # function:prime_check (-> +8), function_argument:number, function_argument_flavor:arg, function_returning_something:prime_check (-> +8)
    if number < 2: # comparison_operator:Lt, if (-> +1), if_guard (-> +1), if_test_atom:2, if_test_atom:number, if_without_else (-> +1), literal:2
        return False # if_then_branch, literal:False, return:False
    if number < 4: # comparison_operator:Lt, if (-> +1), if_guard (-> +1), if_test_atom:4, if_test_atom:number, if_without_else (-> +1), literal:4, suggest_constant_definition
        return True # if_then_branch, literal:True, return:True
    if number % 2 == 0: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:2, if_test_atom:number, if_without_else (-> +1), literal:0, literal:2, modulo_operator
        return False # if_then_branch, literal:False, return:False
    odd_numbers = range(3, int(math.sqrt(number)) + 1, 2) # addition_operator, assignment:range, assignment_lhs_identifier:odd_numbers, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:math, assignment_rhs_atom:number, binary_operator:Add, call_argument:, call_argument:2, call_argument:3, call_argument:number, composition, external_free_call:int, external_free_call:range, free_call:int, free_call:range, literal:1, literal:2, literal:3, member_call:sqrt, range:3:_:2, single_assignment:odd_numbers, suggest_constant_definition
    return not any(number % i == 0 for i in odd_numbers) # binary_operator:Mod, call_argument:, comparison_operator:Eq, comprehension:Generator, comprehension_for_count:1, divisibility_test, external_free_call:any, free_call:any, literal:0, modulo_operator, return, unary_operator:Not
class Test(unittest.TestCase): # class:Test (-> +24)
    def test_primes(self): # function:test_primes (-> +10), function_argument:self, function_argument_flavor:arg, function_returning_nothing:test_primes (-> +10), instance_method:test_primes (-> +10), method:test_primes (-> +10)
        self.assertTrue(prime_check(2)) # call_argument:, call_argument:2, composition, free_call:prime_check, internal_free_call:prime_check, literal:2, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue
        self.assertTrue(prime_check(3)) # call_argument:, call_argument:3, composition, free_call:prime_check, internal_free_call:prime_check, literal:3, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(5)) # call_argument:, call_argument:5, composition, free_call:prime_check, internal_free_call:prime_check, literal:5, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(7)) # call_argument:, call_argument:7, composition, free_call:prime_check, internal_free_call:prime_check, literal:7, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(11)) # call_argument:, call_argument:11, composition, free_call:prime_check, internal_free_call:prime_check, literal:11, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(13)) # call_argument:, call_argument:13, composition, free_call:prime_check, internal_free_call:prime_check, literal:13, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(17)) # call_argument:, call_argument:17, composition, free_call:prime_check, internal_free_call:prime_check, literal:17, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(19)) # call_argument:, call_argument:19, composition, free_call:prime_check, internal_free_call:prime_check, literal:19, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(23)) # call_argument:, call_argument:23, composition, free_call:prime_check, internal_free_call:prime_check, literal:23, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue, suggest_constant_definition
        self.assertTrue(prime_check(29)) # call_argument:, call_argument:29, composition, free_call:prime_check, internal_free_call:prime_check, literal:29, member_call:assertTrue, member_call_object:self, member_call_without_result:assertTrue, suggest_constant_definition
    def test_not_primes(self): # function:test_not_primes (-> +12), function_argument:self, function_argument_flavor:arg, function_returning_nothing:test_not_primes (-> +12), instance_method:test_not_primes (-> +12), method:test_not_primes (-> +12)
        self.assertFalse(prime_check(-19), "Negative numbers are not prime.") # call_argument:, call_argument:-19, composition, free_call:prime_check, internal_free_call:prime_check, literal:-19, literal:Str, member_call:assertFalse, member_call_object:self, member_call_without_result:assertFalse, suggest_constant_definition
        self.assertFalse( # composition, member_call:assertFalse, member_call_object:self, member_call_without_result:assertFalse
            prime_check(0), "Zero doesn't have any divider, primes must have two" # call_argument:, call_argument:0, free_call:prime_check, internal_free_call:prime_check, literal:0, literal:Str
        )
        self.assertFalse( # composition, member_call:assertFalse, member_call_object:self, member_call_without_result:assertFalse
            prime_check(1), "One just have 1 divider, primes must have two." # call_argument:, call_argument:1, free_call:prime_check, internal_free_call:prime_check, literal:1, literal:Str
        )
        self.assertFalse(prime_check(2 * 2)) # binary_operator:Mult, call_argument:, composition, free_call:prime_check, internal_free_call:prime_check, literal:2, member_call:assertFalse, member_call_object:self, member_call_without_result:assertFalse, multiplication_operator
        self.assertFalse(prime_check(2 * 3)) # binary_operator:Mult, call_argument:, composition, free_call:prime_check, internal_free_call:prime_check, literal:2, literal:3, member_call:assertFalse, member_call_object:self, member_call_without_result:assertFalse, multiplication_operator, suggest_constant_definition
        self.assertFalse(prime_check(3 * 3)) # binary_operator:Mult, call_argument:, composition, free_call:prime_check, internal_free_call:prime_check, literal:3, member_call:assertFalse, member_call_object:self, member_call_without_result:assertFalse, multiplication_operator, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5)) # binary_operator:Mult, call_argument:, composition, free_call:prime_check, internal_free_call:prime_check, literal:3, literal:5, member_call:assertFalse, member_call_object:self, member_call_without_result:assertFalse, multiplication_operator, suggest_constant_definition
        self.assertFalse(prime_check(3 * 5 * 7)) # binary_operator:Mult, call_argument:, composition, free_call:prime_check, internal_free_call:prime_check, literal:3, literal:5, literal:7, member_call:assertFalse, member_call_object:self, member_call_without_result:assertFalse, multiplication_operator, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# prime_factors.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List, whole_span:13 (-> +12)
def prime_factors(n: int) -> List[int]: # function:prime_factors (-> +11), function_argument:n, function_argument_flavor:arg, function_returning_something:prime_factors (-> +11), index:int
    i = 2 # assignment:2, assignment_lhs_identifier:i, assignment_rhs_atom:2, literal:2, single_assignment:i
    factors = [] # assignment, assignment_lhs_identifier:factors, empty_literal:List, literal:List, single_assignment:factors
    while i * i <= n: # binary_operator:Mult, comparison_operator:LtE, count_states:i (-> +5), loop:while (-> +5), loop_with_late_exit:while (-> +5), multiplication_operator, while (-> +5)
        if n % i: # binary_operator:Mod, if (-> +4), if_test_atom:i, if_test_atom:n, modulo_operator
            i += 1 # assignment_lhs_identifier:i, assignment_rhs_atom:1, augmented_assignment:Add, if_then_branch, increment:i, literal:1, update:i:1, update_by_augmented_assignment:i:1, update_by_augmented_assignment_with:Add, update_with:Add
        else:
            n //= i # assignment_lhs_identifier:n, assignment_rhs_atom:i, augmented_assignment:FloorDiv, if_else_branch (-> +1), update:n:i, update_by_augmented_assignment:n:i, update_by_augmented_assignment_with:FloorDiv, update_with:FloorDiv
            factors.append(i) # call_argument:i, member_call:append, member_call_object:factors, member_call_without_result:append, update:factors:i, update_by_member_call:factors:i, update_by_member_call_with:append, update_with:append
    if n > 1: # comparison_operator:Gt, if (-> +1), if_test_atom:1, if_test_atom:n, if_without_else (-> +1), literal:1
        factors.append(n) # call_argument:n, if_then_branch, member_call:append, member_call_object:factors, member_call_without_result:append, update:factors:n, update_by_member_call:factors:n, update_by_member_call_with:append, update_with:append
    return factors # return:factors

# ----------------------------------------------------------------------------------------
# prime_numbers.py
# ----------------------------------------------------------------------------------------
from typing import List # import:typing:List, import_module:typing, import_name:List, whole_span:11 (-> +10)
def primes(max: int) -> List[int]: # function:primes (-> +9), function_argument:max, function_argument_flavor:arg, function_returning_something:primes (-> +9), index:int
    max += 1 # assignment_lhs_identifier:max, assignment_rhs_atom:1, augmented_assignment:Add, increment:max, literal:1, update:max:1, update_by_augmented_assignment:max:1, update_by_augmented_assignment_with:Add, update_with:Add
    numbers = [False] * max # assignment:Mult, assignment_lhs_identifier:numbers, assignment_rhs_atom:False, assignment_rhs_atom:max, binary_operator:Mult, literal:False, literal:List, replication_operator:List, single_assignment:numbers
    ret = [] # assignment, assignment_lhs_identifier:ret, empty_literal:List, literal:List, single_assignment:ret
    for i in range(2, max): # accumulate_elements:append (-> +4), accumulate_some_elements:append (-> +4), call_argument:2, call_argument:max, external_free_call:range, for:i (-> +4), for_range:2:max (-> +4), for_range:i:max:i (-> +4), free_call:range, literal:2, loop:for (-> +4), loop_with_late_exit:for (-> +4), range:2:max
        if not numbers[i]: # if (-> +3), if_test_atom:i, if_test_atom:numbers, if_without_else (-> +3), index:i, unary_operator:Not
            for j in range(i, max, i): # call_argument:i, call_argument:max, external_free_call:range, for:j (-> +1), for_range:i:max:i (-> +1), free_call:range, if_then_branch (-> +2), loop:for (-> +1), loop_with_late_exit:for (-> +1), nested_for:1 (-> +1), range:i:max:i
                numbers[j] = True # assignment:True, assignment_lhs_identifier:numbers, assignment_rhs_atom:True, index:j, literal:True
            ret.append(i) # call_argument:i, member_call:append, member_call_object:ret, member_call_without_result:append, update:ret:i, update_by_member_call:ret:i, update_by_member_call_with:append, update_with:append
    return ret # return:ret

# ----------------------------------------------------------------------------------------
# prime_sieve_eratosthenes.py
# ----------------------------------------------------------------------------------------
def prime_sieve_eratosthenes(num): # function:prime_sieve_eratosthenes (-> +10), function_argument:num, function_argument_flavor:arg, function_returning_nothing:prime_sieve_eratosthenes (-> +10), whole_span:11 (-> +10)
    primes = [True for i in range(num + 1)] # addition_operator, assignment, assignment_lhs_identifier:primes, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:i, assignment_rhs_atom:num, binary_operator:Add, call_argument:, comprehension:List, comprehension_for_count:1, external_free_call:range, free_call:range, literal:1, literal:True, range:_, single_assignment:primes
    p = 2 # assignment:2, assignment_lhs_identifier:p, assignment_rhs_atom:2, literal:2, single_assignment:p
    while p * p <= num: # binary_operator:Mult, comparison_operator:LtE, count_states:p (-> +4), loop:while (-> +4), loop_with_late_exit:while (-> +4), multiplication_operator, while (-> +4)
        if primes[p] == True: # comparison_operator:Eq, if (-> +2), if_test_atom:True, if_test_atom:p, if_test_atom:primes, if_without_else (-> +2), index:p, literal:True
            for i in range(p * p, num + 1, p): # addition_operator, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:p, external_free_call:range, for:i (-> +1), for_range:_:_:p (-> +1), free_call:range, if_then_branch (-> +1), literal:1, loop:for (-> +1), loop_with_late_exit:for (-> +1), multiplication_operator, range:_:_:p
                primes[i] = False # assignment:False, assignment_lhs_identifier:primes, assignment_rhs_atom:False, index:i, literal:False
        p += 1 # assignment_lhs_identifier:p, assignment_rhs_atom:1, augmented_assignment:Add, increment:p, literal:1, update:p:1, update_by_augmented_assignment:p:1, update_by_augmented_assignment_with:Add, update_with:Add
    for prime in range(2, num + 1): # addition_operator, binary_operator:Add, call_argument:, call_argument:2, external_free_call:range, for:prime (-> +2), for_range:2:_ (-> +2), free_call:range, literal:1, literal:2, loop:for (-> +2), loop_with_late_exit:for (-> +2), range:2:_
        if primes[prime]: # if (-> +1), if_test_atom:prime, if_test_atom:primes, if_without_else (-> +1), index:prime
            print(prime, end=" ") # call_argument:prime, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str

# ----------------------------------------------------------------------------------------
# qr_decomposition.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, whole_span:18 (-> +17)
def qr_householder(A): # function:qr_householder (-> +16), function_argument:A, function_argument_flavor:arg, function_returning_something:qr_householder (-> +16)
    m, n = A.shape # assignment, assignment_lhs_identifier:m, assignment_lhs_identifier:n, assignment_rhs_atom:A, literal:Tuple, parallel_assignment:2
    t = min(m, n) # assignment:min, assignment_lhs_identifier:t, assignment_rhs_atom:m, assignment_rhs_atom:n, call_argument:m, call_argument:n, external_free_call:min, free_call:min, single_assignment:t
    Q = np.eye(m) # assignment:eye, assignment_lhs_identifier:Q, assignment_rhs_atom:m, assignment_rhs_atom:np, call_argument:m, member_call:eye, single_assignment:Q
    R = A.copy() # assignment:copy, assignment_lhs_identifier:R, assignment_rhs_atom:A, member_call:copy, single_assignment:R
    for k in range(t - 1): # accumulate_all_elements:block (-> +10), accumulate_elements:block (-> +10), binary_operator:Sub, call_argument:, external_free_call:range, for:k (-> +10), for_range:_ (-> +10), free_call:range, literal:1, loop:for (-> +10), loop_with_late_exit:for (-> +10), range:_
        x = R[k:, [k]] # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:R, assignment_rhs_atom:k, literal:List, single_assignment:x
        e1 = np.zeros_like(x) # assignment:zeros_like, assignment_lhs_identifier:e1, assignment_rhs_atom:np, assignment_rhs_atom:x, call_argument:x, member_call:zeros_like, single_assignment:e1
        e1[0] = 1.0 # assignment:1.0, assignment_lhs_identifier:e1, assignment_rhs_atom:1.0, index:0, literal:0, literal:1.0, suggest_constant_definition
        alpha = np.linalg.norm(x) # assignment:norm, assignment_lhs_identifier:alpha, assignment_rhs_atom:np, assignment_rhs_atom:x, call_argument:x, member_call:norm, single_assignment:alpha
        v = x + np.sign(x[0]) * alpha * e1 # addition_operator, assignment:Add, assignment_lhs_identifier:v, assignment_rhs_atom:0, assignment_rhs_atom:alpha, assignment_rhs_atom:e1, assignment_rhs_atom:np, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, call_argument:, index:0, literal:0, member_call:sign, multiplication_operator, single_assignment:v
        v /= np.linalg.norm(v) # assignment_lhs_identifier:v, assignment_rhs_atom:np, assignment_rhs_atom:v, augmented_assignment:Div, call_argument:v, member_call:norm, update:v:np, update:v:v, update_by_augmented_assignment:v:np, update_by_augmented_assignment:v:v, update_by_augmented_assignment_with:Div, update_with:Div
        Q_k = np.eye(m - k) - 2.0 * v @ v.T # assignment:Sub, assignment_lhs_identifier:Q_k, assignment_rhs_atom:2.0, assignment_rhs_atom:k, assignment_rhs_atom:m, assignment_rhs_atom:np, assignment_rhs_atom:v, binary_operator:MatMult, binary_operator:Mult, binary_operator:Sub, call_argument:, literal:2.0, member_call:eye, multiplication_operator, single_assignment:Q_k, suggest_constant_definition
        Q_k = np.block([[np.eye(k), np.zeros((k, m - k))], [np.zeros((m - k, k)), Q_k]]) # assignment:block, assignment_lhs_identifier:Q_k, assignment_rhs_atom:Q_k, assignment_rhs_atom:k, assignment_rhs_atom:m, assignment_rhs_atom:np, binary_operator:Sub, call_argument:, call_argument:k, composition, literal:List, literal:Tuple, member_call:block, member_call:eye, member_call:zeros, single_assignment:Q_k, update:Q_k:k, update:Q_k:m, update:Q_k:np, update_by_assignment:Q_k:k, update_by_assignment:Q_k:m, update_by_assignment:Q_k:np, update_by_assignment_with:block, update_with:block
        Q = Q @ Q_k.T # assignment:MatMult, assignment_lhs_identifier:Q, assignment_rhs_atom:Q, assignment_rhs_atom:Q_k, binary_operator:MatMult, single_assignment:Q, suggest_augmented_assignment, update:Q:Q_k, update_by_assignment:Q:Q_k, update_by_assignment_with:MatMult, update_with:MatMult
        R = Q_k @ R # assignment:MatMult, assignment_lhs_identifier:R, assignment_rhs_atom:Q_k, assignment_rhs_atom:R, binary_operator:MatMult, single_assignment:R, update:R:Q_k, update_by_assignment:R:Q_k, update_by_assignment_with:MatMult, update_with:MatMult
    return Q, R # literal:Tuple, return

# ----------------------------------------------------------------------------------------
# quadratic_equations_complex_numbers.py
# ----------------------------------------------------------------------------------------
from math import sqrt # import:math:sqrt, import_module:math, import_name:sqrt, whole_span:16 (-> +15)
from typing import Tuple # import:typing:Tuple, import_module:typing, import_name:Tuple
def QuadraticEquation(a: int, b: int, c: int) -> Tuple[str, str]: # function:QuadraticEquation (-> +10), function_argument:a, function_argument:b, function_argument:c, function_argument_flavor:arg, function_returning_something:QuadraticEquation (-> +10), index:_, literal:Tuple
    if a == 0: # comparison_operator:Eq, if (-> +1), if_test_atom:0, if_test_atom:a, if_without_else (-> +1), literal:0
        raise ValueError("Coefficient 'a' must not be zero for quadratic equations.") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    delta = b * b - 4 * a * c # assignment:Sub, assignment_lhs_identifier:delta, assignment_rhs_atom:4, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:c, binary_operator:Mult, binary_operator:Sub, literal:4, multiplication_operator, single_assignment:delta, suggest_constant_definition
    if delta >= 0: # comparison_operator:GtE, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:delta, if_without_else (-> +1), literal:0
        return str((-b + sqrt(delta)) / (2 * a)), str((-b - sqrt(delta)) / (2 * a)) # addition_operator, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, call_argument:, call_argument:delta, composition, external_free_call:sqrt, external_free_call:str, free_call:sqrt, free_call:str, if_then_branch, literal:2, literal:Tuple, multiplication_operator, return, unary_operator:USub
    snd = sqrt(-delta) # assignment:sqrt, assignment_lhs_identifier:snd, assignment_rhs_atom:delta, call_argument:, external_free_call:sqrt, free_call:sqrt, single_assignment:snd, unary_operator:USub
    if b == 0: # comparison_operator:Eq, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:b, if_without_else (-> +1), literal:0
        return f"({snd} * i) / 2", f"({snd} * i) / {2 * a}" # binary_operator:Mult, if_then_branch, literal:2, literal:Str, literal:Tuple, multiplication_operator, return
    b = -abs(b) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:b, call_argument:b, external_free_call:abs, free_call:abs, single_assignment:b, unary_operator:USub
    return f"({b}+{snd} * i) / 2", f"({b}+{snd} * i) / {2 * a}" # binary_operator:Mult, literal:2, literal:Str, literal:Tuple, multiplication_operator, return
def main(): # function:main (-> +2), function_returning_nothing:main (-> +2), function_without_arguments:main (-> +2)
    solutions = QuadraticEquation(a=5, b=6, c=1) # assignment:QuadraticEquation, assignment_lhs_identifier:solutions, assignment_rhs_atom:1, assignment_rhs_atom:5, assignment_rhs_atom:6, free_call:QuadraticEquation, internal_free_call:QuadraticEquation, literal:1, literal:5, literal:6, single_assignment:solutions, suggest_constant_definition
    print("The equation solutions are: {} and {}".format(*solutions)) # call_argument:, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, member_call:format

# ----------------------------------------------------------------------------------------
# radix2_fft.py
# ----------------------------------------------------------------------------------------
import mpmath # import:mpmath, import_module:mpmath, whole_span:92 (-> +91)
import numpy as np # import:numpy, import_module:numpy
class FFT: # class:FFT (-> +89)
    def __init__(self, polyA=[0], polyB=[0]): # function:__init__ (-> +17), function_argument:polyA, function_argument:polyB, function_argument:self, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +17), instance_method:__init__ (-> +17), literal:0, literal:List, method:__init__ (-> +17)
        self.polyA = list(polyA)[:] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:polyA, call_argument:polyA, external_free_call:list, free_call:list, slice:::, slice_lower:, slice_step:, slice_upper:
        self.polyB = list(polyB)[:] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:polyB, call_argument:polyB, external_free_call:list, free_call:list, slice:::, slice_lower:, slice_step:, slice_upper:
        while self.polyA[-1] == 0: # comparison_operator:Eq, index:-1, literal:-1, literal:0, loop:while (-> +1), loop_with_late_exit:while (-> +1), negative_index:-1, while (-> +1)
            self.polyA.pop() # member_call:pop, member_call_without_result:pop
        self.len_A = len(self.polyA) # assignment:len, assignment_lhs_identifier:self, assignment_rhs_atom:self, call_argument:, external_free_call:len, free_call:len
        while self.polyB[-1] == 0: # comparison_operator:Eq, index:-1, literal:-1, literal:0, loop:while (-> +1), loop_with_late_exit:while (-> +1), negative_index:-1, while (-> +1)
            self.polyB.pop() # member_call:pop, member_call_without_result:pop
        self.len_B = len(self.polyB) # assignment:len, assignment_lhs_identifier:self, assignment_rhs_atom:self, call_argument:, external_free_call:len, free_call:len
        self.C_max_length = int( # assignment:int, assignment_lhs_identifier:self, composition, external_free_call:int, free_call:int, update:self:1, update:self:2, update:self:np, update_by_assignment:self:1, update_by_assignment:self:2, update_by_assignment:self:np, update_by_assignment_with:int, update_with:int
            2 ** np.ceil(np.log2(len(self.polyA) + len(self.polyB) - 1)) # addition_operator, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:np, assignment_rhs_atom:self, binary_operator:Add, binary_operator:Pow, binary_operator:Sub, call_argument:, composition, external_free_call:len, free_call:len, literal:1, literal:2, member_call:ceil, member_call:log2
        )
        while len(self.polyA) < self.C_max_length: # call_argument:, comparison_operator:Lt, external_free_call:len, free_call:len, loop:while (-> +1), loop_with_late_exit:while (-> +1), while (-> +1)
            self.polyA.append(0) # call_argument:0, literal:0, member_call:append, member_call_without_result:append
        while len(self.polyB) < self.C_max_length: # call_argument:, comparison_operator:Lt, external_free_call:len, free_call:len, loop:while (-> +1), loop_with_late_exit:while (-> +1), while (-> +1)
            self.polyB.append(0) # call_argument:0, literal:0, member_call:append, member_call_without_result:append
        self.root = complex(mpmath.root(x=1, n=self.C_max_length, k=1)) # assignment:complex, assignment_lhs_identifier:self, assignment_rhs_atom:1, assignment_rhs_atom:mpmath, assignment_rhs_atom:self, call_argument:, composition, external_free_call:complex, free_call:complex, literal:1, member_call:root, update:self:1, update:self:mpmath, update_by_assignment:self:1, update_by_assignment:self:mpmath, update_by_assignment_with:complex, update_with:complex
        self.product = self.__multiply() # assignment:__multiply, assignment_lhs_identifier:self, assignment_rhs_atom:self, member_call:__multiply
    def __DFT(self, which): # function:__DFT (-> +23), function_argument:self, function_argument:which, function_argument_flavor:arg, function_returning_something:__DFT (-> +23), instance_method:__DFT (-> +23), method:__DFT (-> +23)
        if which == "A": # comparison_operator:Eq, if (-> +3), if_test_atom:which, literal:Str, verbose_conditional_assignment (-> +3)
            dft = [[x] for x in self.polyA] # assignment, assignment_lhs_identifier:dft, assignment_rhs_atom:self, assignment_rhs_atom:x, comprehension:List, comprehension_for_count:1, if_then_branch, literal:List, single_assignment:dft
        else:
            dft = [[x] for x in self.polyB] # assignment, assignment_lhs_identifier:dft, assignment_rhs_atom:self, assignment_rhs_atom:x, comprehension:List, comprehension_for_count:1, if_else_branch, literal:List, single_assignment:dft
        if len(dft) <= 1: # call_argument:dft, comparison_operator:LtE, external_free_call:len, free_call:len, if (-> +1), if_guard (-> +1), if_test_atom:1, if_test_atom:dft, if_without_else (-> +1), literal:1
            return dft[0] # if_then_branch, index:0, literal:0, return
        next_ncol = self.C_max_length // 2 # assignment:FloorDiv, assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, assignment_rhs_atom:self, binary_operator:FloorDiv, literal:2, single_assignment:next_ncol
        while next_ncol > 0: # comparison_operator:Gt, literal:0, loop:while (-> +14), loop_with_late_exit:while (-> +14), while (-> +14)
            new_dft = [[] for i in range(next_ncol)] # assignment, assignment_lhs_identifier:new_dft, assignment_rhs_atom:i, assignment_rhs_atom:next_ncol, call_argument:next_ncol, comprehension:List, comprehension_for_count:1, empty_literal:List, external_free_call:range, free_call:range, literal:List, range:next_ncol, single_assignment:new_dft
            root = self.root ** next_ncol # assignment:Pow, assignment_lhs_identifier:root, assignment_rhs_atom:next_ncol, assignment_rhs_atom:self, binary_operator:Pow, single_assignment:root
            current_root = 1 # assignment:1, assignment_lhs_identifier:current_root, assignment_rhs_atom:1, literal:1, single_assignment:current_root
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator:FloorDiv, binary_operator:Mult, call_argument:, external_free_call:range, for:j (-> +3), for_range:_ (-> +3), for_range:next_ncol (-> +3), free_call:range, literal:2, loop:for (-> +3), loop_with_late_exit:for (-> +3), multiplication_operator, range:_
                for i in range(next_ncol): # call_argument:next_ncol, external_free_call:range, for:i (-> +1), for_range:next_ncol (-> +1), free_call:range, loop:for (-> +1), loop_with_late_exit:for (-> +1), nested_for:1 (-> +1), range:next_ncol
                    new_dft[i].append(dft[i][j] + current_root * dft[i + next_ncol][j]) # addition_operator, binary_operator:Add, binary_operator:Mult, call_argument:, index:_, index:i, index:j, index_arithmetic, member_call:append, member_call_without_result:append, multiplication_operator, nested_index:2
                current_root *= root # assignment_lhs_identifier:current_root, assignment_rhs_atom:root, augmented_assignment:Mult, update:current_root:root, update_by_augmented_assignment:current_root:root, update_by_augmented_assignment_with:Mult, update_with:Mult
            current_root = 1 # assignment:1, assignment_lhs_identifier:current_root, assignment_rhs_atom:1, literal:1, single_assignment:current_root
            for j in range(self.C_max_length // (next_ncol * 2)): # binary_operator:FloorDiv, binary_operator:Mult, call_argument:, external_free_call:range, for:j (-> +3), for_range:_ (-> +3), for_range:next_ncol (-> +3), free_call:range, literal:2, loop:for (-> +3), loop_with_late_exit:for (-> +3), multiplication_operator, range:_
                for i in range(next_ncol): # call_argument:next_ncol, external_free_call:range, for:i (-> +1), for_range:next_ncol (-> +1), free_call:range, loop:for (-> +1), loop_with_late_exit:for (-> +1), nested_for:1 (-> +1), range:next_ncol
                    new_dft[i].append(dft[i][j] - current_root * dft[i + next_ncol][j]) # addition_operator, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, call_argument:, index:_, index:i, index:j, index_arithmetic, member_call:append, member_call_without_result:append, multiplication_operator, nested_index:2
                current_root *= root # assignment_lhs_identifier:current_root, assignment_rhs_atom:root, augmented_assignment:Mult, update:current_root:root, update_by_augmented_assignment:current_root:root, update_by_augmented_assignment_with:Mult, update_with:Mult
            dft = new_dft # assignment, assignment_lhs_identifier:dft, assignment_rhs_atom:new_dft, single_assignment:dft
            next_ncol = next_ncol // 2 # assignment:FloorDiv, assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, assignment_rhs_atom:next_ncol, binary_operator:FloorDiv, literal:2, single_assignment:next_ncol, suggest_augmented_assignment, update:next_ncol:2, update_by_assignment:next_ncol:2, update_by_assignment_with:FloorDiv, update_with:FloorDiv
        return dft[0] # index:0, literal:0, return
    def __multiply(self): # function:__multiply (-> +35), function_argument:self, function_argument_flavor:arg, function_returning_something:__multiply (-> +35), instance_method:__multiply (-> +35), method:__multiply (-> +35)
        dftA = self.__DFT("A") # assignment:__DFT, assignment_lhs_identifier:dftA, assignment_rhs_atom:self, call_argument:, literal:Str, member_call:__DFT, single_assignment:dftA
        dftB = self.__DFT("B") # assignment:__DFT, assignment_lhs_identifier:dftB, assignment_rhs_atom:self, call_argument:, literal:Str, member_call:__DFT, single_assignment:dftB
        inverseC = [[dftA[i] * dftB[i] for i in range(self.C_max_length)]] # assignment, assignment_lhs_identifier:inverseC, assignment_rhs_atom:dftA, assignment_rhs_atom:dftB, assignment_rhs_atom:i, assignment_rhs_atom:self, binary_operator:Mult, call_argument:, comprehension:List, comprehension_for_count:1, external_free_call:range, free_call:range, index:i, literal:List, multiplication_operator, range:_, single_assignment:inverseC
        del dftA # unbinding:dftA
        del dftB # unbinding:dftB
        if len(inverseC[0]) <= 1: # call_argument:, comparison_operator:LtE, external_free_call:len, free_call:len, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:1, if_test_atom:inverseC, if_without_else (-> +1), index:0, literal:0, literal:1
            return inverseC[0] # if_then_branch, index:0, literal:0, return
        next_ncol = 2 # assignment:2, assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, literal:2, single_assignment:next_ncol
        while next_ncol <= self.C_max_length: # comparison_operator:LtE, loop:while (-> +22), loop_with_late_exit:while (-> +22), while (-> +22)
            new_inverseC = [[] for i in range(next_ncol)] # assignment, assignment_lhs_identifier:new_inverseC, assignment_rhs_atom:i, assignment_rhs_atom:next_ncol, call_argument:next_ncol, comprehension:List, comprehension_for_count:1, empty_literal:List, external_free_call:range, free_call:range, literal:List, range:next_ncol, single_assignment:new_inverseC
            root = self.root ** (next_ncol // 2) # assignment:Pow, assignment_lhs_identifier:root, assignment_rhs_atom:2, assignment_rhs_atom:next_ncol, assignment_rhs_atom:self, binary_operator:FloorDiv, binary_operator:Pow, literal:2, single_assignment:root
            current_root = 1 # assignment:1, assignment_lhs_identifier:current_root, assignment_rhs_atom:1, literal:1, single_assignment:current_root
            for j in range(self.C_max_length // next_ncol): # binary_operator:FloorDiv, call_argument:, external_free_call:range, for:j (-> +16), for_range:_ (-> +16), free_call:range, loop:for (-> +16), loop_with_late_exit:for (-> +16), range:_
                for i in range(next_ncol // 2): # binary_operator:FloorDiv, call_argument:, external_free_call:range, for:i (-> +13), for_range:_ (-> +13), free_call:range, literal:2, loop:for (-> +13), loop_with_late_exit:for (-> +13), nested_for:1 (-> +13), range:_
                    new_inverseC[i].append( # index:i, member_call:append, member_call_without_result:append
                        ( # binary_operator:Div, call_argument:
                            inverseC[i][j] # addition_operator, binary_operator:Add, index:i, index:j, nested_index:2
                            + inverseC[i][j + self.C_max_length // next_ncol] # addition_operator, binary_operator:Add, binary_operator:FloorDiv, index:_, index:i, index_arithmetic, nested_index:2
                        )
                        / 2 # literal:2
                    )
                    new_inverseC[i + next_ncol // 2].append( # addition_operator, binary_operator:Add, binary_operator:FloorDiv, index:_, index_arithmetic, literal:2, member_call:append, member_call_without_result:append
                        ( # binary_operator:Div, call_argument:
                            inverseC[i][j] # binary_operator:Sub, index:i, index:j, nested_index:2
                            - inverseC[i][j + self.C_max_length // next_ncol] # addition_operator, binary_operator:Add, binary_operator:FloorDiv, index:_, index:i, index_arithmetic, nested_index:2
                        )
                        / (2 * current_root) # binary_operator:Mult, literal:2, multiplication_operator
                    )
                current_root *= root # assignment_lhs_identifier:current_root, assignment_rhs_atom:root, augmented_assignment:Mult, update:current_root:root, update_by_augmented_assignment:current_root:root, update_by_augmented_assignment_with:Mult, update_with:Mult
            inverseC = new_inverseC # assignment, assignment_lhs_identifier:inverseC, assignment_rhs_atom:new_inverseC, single_assignment:inverseC
            next_ncol *= 2 # assignment_lhs_identifier:next_ncol, assignment_rhs_atom:2, augmented_assignment:Mult, literal:2, update:next_ncol:2, update_by_augmented_assignment:next_ncol:2, update_by_augmented_assignment_with:Mult, update_with:Mult
        inverseC = [round(x[0].real, 8) + round(x[0].imag, 8) * 1j for x in inverseC] # addition_operator, assignment, assignment_lhs_identifier:inverseC, assignment_rhs_atom:0, assignment_rhs_atom:1j, assignment_rhs_atom:8, assignment_rhs_atom:inverseC, assignment_rhs_atom:x, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:8, comprehension:List, comprehension_for_count:1, external_free_call:round, free_call:round, index:0, literal:0, literal:1j, literal:8, multiplication_operator, single_assignment:inverseC, suggest_constant_definition, update:inverseC:0, update:inverseC:1j, update:inverseC:8, update:inverseC:x, update_by_assignment:inverseC:0, update_by_assignment:inverseC:1j, update_by_assignment:inverseC:8, update_by_assignment:inverseC:x, update_by_assignment_with, update_with
        while inverseC[-1] == 0: # comparison_operator:Eq, index:-1, literal:-1, literal:0, loop:while (-> +1), loop_with_late_exit:while (-> +1), negative_index:-1, while (-> +1)
            inverseC.pop() # member_call:pop, member_call_object:inverseC, member_call_without_result:pop
        return inverseC # return:inverseC
    def __str__(self): # function:__str__ (-> +10), function_argument:self, function_argument_flavor:arg, function_returning_something:__str__ (-> +10), instance_method:__str__ (-> +10), method:__str__ (-> +10)
        A = "A = " + " + ".join( # assignment:Add, assignment_lhs_identifier:A, binary_operator:Add, composition, concatenation_operator:Str, literal:Str, member_call:join, single_assignment:A
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyA[: self.len_A]) # assignment_rhs_atom:coef, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, comprehension:Generator, comprehension_for_count:1, external_free_call:enumerate, free_call:enumerate, literal:Str, literal:Tuple, slice::_:, slice_lower:, slice_step:, slice_upper:_
        )
        B = "B = " + " + ".join( # assignment:Add, assignment_lhs_identifier:B, binary_operator:Add, composition, concatenation_operator:Str, literal:Str, member_call:join, single_assignment:B
            f"{coef}*x^{i}" for coef, i in enumerate(self.polyB[: self.len_B]) # assignment_rhs_atom:coef, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, comprehension:Generator, comprehension_for_count:1, external_free_call:enumerate, free_call:enumerate, literal:Str, literal:Tuple, slice::_:, slice_lower:, slice_step:, slice_upper:_
        )
        C = "A*B = " + " + ".join( # assignment:Add, assignment_lhs_identifier:C, binary_operator:Add, composition, concatenation_operator:Str, literal:Str, member_call:join, single_assignment:C
            f"{coef}*x^{i}" for coef, i in enumerate(self.product) # assignment_rhs_atom:coef, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, comprehension:Generator, comprehension_for_count:1, external_free_call:enumerate, free_call:enumerate, literal:Str, literal:Tuple
        )
        return "\n".join((A, B, C)) # call_argument:, literal:Str, literal:Tuple, member_call:join, return

# ----------------------------------------------------------------------------------------
# runge_kutta.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, whole_span:14 (-> +13)
def runge_kutta(f, y0, x0, h, x_end): # function:runge_kutta (-> +12), function_argument:f, function_argument:h, function_argument:x0, function_argument:x_end, function_argument:y0, function_argument_flavor:arg, function_returning_something:runge_kutta (-> +12), higher_order_function:f (-> +12)
    N = int(np.ceil((x_end - x0) / h)) # assignment:int, assignment_lhs_identifier:N, assignment_rhs_atom:h, assignment_rhs_atom:np, assignment_rhs_atom:x0, assignment_rhs_atom:x_end, binary_operator:Div, binary_operator:Sub, call_argument:, composition, external_free_call:int, free_call:int, member_call:ceil, single_assignment:N
    y = np.zeros((N + 1,)) # addition_operator, assignment:zeros, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:N, assignment_rhs_atom:np, binary_operator:Add, call_argument:, literal:1, literal:Tuple, member_call:zeros, single_assignment:y
    y[0] = y0 # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:y0, index:0, literal:0
    x = x0 # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:x0, single_assignment:x
    for k in range(N): # accumulate_all_elements:Add (-> +6), accumulate_elements:Add (-> +6), call_argument:N, external_free_call:range, for:k (-> +6), for_range:N (-> +6), free_call:range, loop:for (-> +6), loop_with_late_exit:for (-> +6), range:N
        k1 = f(x, y[k]) # assignment:f, assignment_lhs_identifier:k1, assignment_rhs_atom:k, assignment_rhs_atom:x, assignment_rhs_atom:y, call_argument:, call_argument:x, external_free_call:f, free_call:f, index:k, single_assignment:k1
        k2 = f(x + 0.5 * h, y[k] + 0.5 * h * k1) # addition_operator, assignment:f, assignment_lhs_identifier:k2, assignment_rhs_atom:0.5, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k1, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, external_free_call:f, free_call:f, index:k, literal:0.5, multiplication_operator, single_assignment:k2, suggest_constant_definition
        k3 = f(x + 0.5 * h, y[k] + 0.5 * h * k2) # addition_operator, assignment:f, assignment_lhs_identifier:k3, assignment_rhs_atom:0.5, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k2, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, external_free_call:f, free_call:f, index:k, literal:0.5, multiplication_operator, single_assignment:k3, suggest_constant_definition
        k4 = f(x + h, y[k] + h * k3) # addition_operator, assignment:f, assignment_lhs_identifier:k4, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k3, assignment_rhs_atom:x, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Mult, call_argument:, external_free_call:f, free_call:f, index:k, multiplication_operator, single_assignment:k4
        y[k + 1] = y[k] + (1 / 6) * h * (k1 + 2 * k2 + 2 * k3 + k4) # addition_operator, assignment:Add, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:h, assignment_rhs_atom:k, assignment_rhs_atom:k1, assignment_rhs_atom:k2, assignment_rhs_atom:k3, assignment_rhs_atom:k4, assignment_rhs_atom:y, binary_operator:Add, binary_operator:Div, binary_operator:Mult, index:_, index:k, index_arithmetic, literal:1, literal:2, literal:6, multiplication_operator, suggest_constant_definition, update:y:1, update:y:2, update:y:6, update:y:h, update:y:k, update:y:k1, update:y:k2, update:y:k3, update:y:k4, update_by_assignment:y:1, update_by_assignment:y:2, update_by_assignment:y:6, update_by_assignment:y:h, update_by_assignment:y:k, update_by_assignment:y:k1, update_by_assignment:y:k2, update_by_assignment:y:k3, update_by_assignment:y:k4, update_by_assignment_with:Add, update_with:Add
        x += h # assignment_lhs_identifier:x, assignment_rhs_atom:h, augmented_assignment:Add, update:x:h, update_by_augmented_assignment:x:h, update_by_augmented_assignment_with:Add, update_with:Add
    return y # return:y

# ----------------------------------------------------------------------------------------
# segmented_sieve.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, whole_span:36 (-> +35)
def sieve(n): # function:sieve (-> +33), function_argument:n, function_argument_flavor:arg, function_returning_something:sieve (-> +33)
    in_prime = [] # assignment, assignment_lhs_identifier:in_prime, empty_literal:List, literal:List, single_assignment:in_prime
    start = 2 # assignment:2, assignment_lhs_identifier:start, assignment_rhs_atom:2, literal:2, single_assignment:start
    end = int(math.sqrt(n)) # assignment:int, assignment_lhs_identifier:end, assignment_rhs_atom:math, assignment_rhs_atom:n, call_argument:, call_argument:n, composition, external_free_call:int, free_call:int, member_call:sqrt, single_assignment:end
    temp = [True] * (end + 1) # addition_operator, assignment:Mult, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:end, binary_operator:Add, binary_operator:Mult, literal:1, literal:List, literal:True, replication_operator:List, single_assignment:temp
    prime = [] # assignment, assignment_lhs_identifier:prime, empty_literal:List, literal:List, single_assignment:prime
    while start <= end: # comparison_operator:LtE, count_states:start (-> +6), loop:while (-> +6), loop_with_late_exit:while (-> +6), while (-> +6)
        if temp[start] is True: # comparison_operator:Is, if (-> +4), if_test_atom:True, if_test_atom:start, if_test_atom:temp, if_without_else (-> +4), index:start, literal:True
            in_prime.append(start) # call_argument:start, if_then_branch (-> +3), member_call:append, member_call_object:in_prime, member_call_without_result:append, update:in_prime:start, update_by_member_call:in_prime:start, update_by_member_call_with:append, update_with:append
            for i in range(start * start, end + 1, start): # addition_operator, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:start, external_free_call:range, for:i (-> +2), for_range:_:_:start (-> +2), free_call:range, literal:1, loop:for (-> +2), loop_with_late_exit:for (-> +2), multiplication_operator, range:_:_:start
                if temp[i] is True: # comparison_operator:Is, if (-> +1), if_test_atom:True, if_test_atom:i, if_test_atom:temp, if_without_else (-> +1), index:i, literal:True, nested_if:1 (-> +1)
                    temp[i] = False # assignment:False, assignment_lhs_identifier:temp, assignment_rhs_atom:False, if_then_branch, index:i, literal:False
        start += 1 # assignment_lhs_identifier:start, assignment_rhs_atom:1, augmented_assignment:Add, increment:start, literal:1, update:start:1, update_by_augmented_assignment:start:1, update_by_augmented_assignment_with:Add, update_with:Add
    prime += in_prime # assignment_lhs_identifier:prime, assignment_rhs_atom:in_prime, augmented_assignment:Add, update:prime:in_prime, update_by_augmented_assignment:prime:in_prime, update_by_augmented_assignment_with:Add, update_with:Add
    low = end + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:low, assignment_rhs_atom:1, assignment_rhs_atom:end, binary_operator:Add, literal:1, single_assignment:low
    high = low + end - 1 # addition_operator, assignment:Sub, assignment_lhs_identifier:high, assignment_rhs_atom:1, assignment_rhs_atom:end, assignment_rhs_atom:low, binary_operator:Add, binary_operator:Sub, corrective_conditional_assignment (-> +2), literal:1, single_assignment:high
    if high > n: # comparison_operator:Gt, if (-> +1), if_test_atom:high, if_test_atom:n, if_without_else (-> +1)
        high = n # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:n, if_then_branch, single_assignment:high
    while low <= n: # comparison_operator:LtE, loop:while (-> +14), loop_with_late_exit:while (-> +14), while (-> +14)
        temp = [True] * (high - low + 1) # addition_operator, assignment:Mult, assignment_lhs_identifier:temp, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:high, assignment_rhs_atom:low, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, literal:1, literal:List, literal:True, replication_operator:List, single_assignment:temp
        for each in in_prime: # accumulate_elements:Add (-> +5), accumulate_some_elements:Add (-> +5), for:each (-> +5), for_each (-> +5), for_range:t:_:each (-> +5), loop:for (-> +5), loop_with_late_exit:for (-> +5)
            t = math.floor(low / each) * each # assignment:Mult, assignment_lhs_identifier:t, assignment_rhs_atom:each, assignment_rhs_atom:low, assignment_rhs_atom:math, binary_operator:Div, binary_operator:Mult, call_argument:, corrective_conditional_assignment (-> +2), member_call:floor, multiplication_operator, single_assignment:t
            if t < low: # comparison_operator:Lt, if (-> +1), if_test_atom:low, if_test_atom:t, if_without_else (-> +1)
                t += each # assignment_lhs_identifier:t, assignment_rhs_atom:each, augmented_assignment:Add, if_then_branch, update:t:each, update_by_augmented_assignment:t:each, update_by_augmented_assignment_with:Add, update_with:Add
            for j in range(t, high + 1, each): # addition_operator, binary_operator:Add, call_argument:, call_argument:each, call_argument:t, external_free_call:range, for:j (-> +1), for_range:t:_:each (-> +1), free_call:range, literal:1, loop:for (-> +1), loop_with_late_exit:for (-> +1), nested_for:1 (-> +1), range:t:_:each
                temp[j - low] = False # assignment:False, assignment_lhs_identifier:temp, assignment_rhs_atom:False, binary_operator:Sub, index:_, index_arithmetic, literal:False
        for j in range(len(temp)): # call_argument:, call_argument:temp, composition, external_free_call:len, external_free_call:range, for:j (-> +2), for_indexes (-> +2), for_range:_ (-> +2), free_call:len, free_call:range, loop:for (-> +2), loop_with_late_exit:for (-> +2), range:_
            if temp[j] is True: # comparison_operator:Is, if (-> +1), if_test_atom:True, if_test_atom:j, if_test_atom:temp, if_without_else (-> +1), index:j, literal:True
                prime.append(j + low) # addition_operator, binary_operator:Add, call_argument:, if_then_branch, member_call:append, member_call_object:prime, member_call_without_result:append
        low = high + 1 # addition_operator, assignment:Add, assignment_lhs_identifier:low, assignment_rhs_atom:1, assignment_rhs_atom:high, binary_operator:Add, literal:1, single_assignment:low
        high = low + end - 1 # addition_operator, assignment:Sub, assignment_lhs_identifier:high, assignment_rhs_atom:1, assignment_rhs_atom:end, assignment_rhs_atom:low, binary_operator:Add, binary_operator:Sub, corrective_conditional_assignment (-> +2), literal:1, single_assignment:high
        if high > n: # comparison_operator:Gt, if (-> +1), if_test_atom:high, if_test_atom:n, if_without_else (-> +1)
            high = n # assignment, assignment_lhs_identifier:high, assignment_rhs_atom:n, if_then_branch, single_assignment:high
    return prime # return:prime
print(sieve(10 ** 6)) # binary_operator:Pow, call_argument:, composition, external_free_call:print, free_call:print, free_call:sieve, free_call_without_result:print, internal_free_call:sieve, literal:10, literal:6

# ----------------------------------------------------------------------------------------
# sieve_of_eratosthenes.py
# ----------------------------------------------------------------------------------------
"""
Sieve of Eratosthones
The sieve of Eratosthenes is an algorithm used to find prime numbers, less than or equal to a given value.
Illustration: https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
Reference: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
doctest provider: Bruno Simas Hadlich (https://github.com/brunohadlich)
Also thanks Dmitry (https://github.com/LizardWizzard) for finding the problem
""" # literal:Str, whole_span:25 (-> +17)
import math # import:math, import_module:math
def sieve(n): # function:sieve (-> +15), function_argument:n, function_argument_flavor:arg, function_returning_something:sieve (-> +15)
    l = [True] * (n + 1) # addition_operator, assignment:Mult, assignment_lhs_identifier:l, assignment_rhs_atom:1, assignment_rhs_atom:True, assignment_rhs_atom:n, binary_operator:Add, binary_operator:Mult, literal:1, literal:List, literal:True, replication_operator:List, single_assignment:l
    prime = [] # assignment, assignment_lhs_identifier:prime, empty_literal:List, literal:List, single_assignment:prime
    start = 2 # assignment:2, assignment_lhs_identifier:start, assignment_rhs_atom:2, literal:2, single_assignment:start
    end = int(math.sqrt(n)) # assignment:int, assignment_lhs_identifier:end, assignment_rhs_atom:math, assignment_rhs_atom:n, call_argument:, call_argument:n, composition, external_free_call:int, free_call:int, member_call:sqrt, single_assignment:end
    while start <= end: # comparison_operator:LtE, count_states:start (-> +6), loop:while (-> +6), loop_with_late_exit:while (-> +6), while (-> +6)
        if l[start] is True: # comparison_operator:Is, if (-> +4), if_test_atom:True, if_test_atom:l, if_test_atom:start, if_without_else (-> +4), index:start, literal:True
            prime.append(start) # call_argument:start, if_then_branch (-> +3), member_call:append, member_call_object:prime, member_call_without_result:append, update:prime:start, update_by_member_call:prime:start, update_by_member_call_with:append, update_with:append
            for i in range(start * start, n + 1, start): # addition_operator, binary_operator:Add, binary_operator:Mult, call_argument:, call_argument:start, external_free_call:range, for:i (-> +2), for_range:_:_:start (-> +2), free_call:range, literal:1, loop:for (-> +2), loop_with_late_exit:for (-> +2), multiplication_operator, range:_:_:start
                if l[i] is True: # comparison_operator:Is, if (-> +1), if_test_atom:True, if_test_atom:i, if_test_atom:l, if_without_else (-> +1), index:i, literal:True, nested_if:1 (-> +1)
                    l[i] = False # assignment:False, assignment_lhs_identifier:l, assignment_rhs_atom:False, if_then_branch, index:i, literal:False
        start += 1 # assignment_lhs_identifier:start, assignment_rhs_atom:1, augmented_assignment:Add, increment:start, literal:1, update:start:1, update_by_augmented_assignment:start:1, update_by_augmented_assignment_with:Add, update_with:Add
    for j in range(end + 1, n + 1): # accumulate_elements:append (-> +2), accumulate_some_elements:append (-> +2), addition_operator, binary_operator:Add, call_argument:, external_free_call:range, for:j (-> +2), for_range:_:_ (-> +2), free_call:range, literal:1, loop:for (-> +2), loop_with_late_exit:for (-> +2), range:_:_
        if l[j] is True: # comparison_operator:Is, if (-> +1), if_test_atom:True, if_test_atom:j, if_test_atom:l, if_without_else (-> +1), index:j, literal:True
            prime.append(j) # call_argument:j, if_then_branch, member_call:append, member_call_object:prime, member_call_without_result:append, update:prime:j, update_by_member_call:prime:j, update_by_member_call_with:append, update_with:append
    return prime # return:prime

# ----------------------------------------------------------------------------------------
# simpson_rule.py
# ----------------------------------------------------------------------------------------
def method_2(boundary, steps): # function:method_2 (-> +12), function_argument:boundary, function_argument:steps, function_argument_flavor:arg, function_returning_something:method_2 (-> +12), whole_span:28 (-> +27)
    h = (boundary[1] - boundary[0]) / steps # assignment:Div, assignment_lhs_identifier:h, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, binary_operator:Div, binary_operator:Sub, index:0, index:1, literal:0, literal:1, single_assignment:h
    a = boundary[0] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, assignment_rhs_atom:boundary, index:0, literal:0, single_assignment:a
    b = boundary[1] # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1, assignment_rhs_atom:boundary, index:1, literal:1, single_assignment:b
    x_i = make_points(a, b, h) # assignment:make_points, assignment_lhs_identifier:x_i, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:h, call_argument:a, call_argument:b, call_argument:h, free_call:make_points, internal_free_call:make_points, single_assignment:x_i
    y = 0.0 # assignment:0.0, assignment_lhs_identifier:y, assignment_rhs_atom:0.0, literal:0.0, single_assignment:y, suggest_constant_definition
    y += (h / 3.0) * f(a) # assignment_lhs_identifier:y, assignment_rhs_atom:3.0, assignment_rhs_atom:a, assignment_rhs_atom:h, augmented_assignment:Add, binary_operator:Div, binary_operator:Mult, call_argument:a, free_call:f, internal_free_call:f, literal:3.0, multiplication_operator, suggest_constant_definition, update:y:3.0, update:y:a, update:y:h, update_by_augmented_assignment:y:3.0, update_by_augmented_assignment:y:a, update_by_augmented_assignment:y:h, update_by_augmented_assignment_with:Add, update_with:Add
    cnt = 2 # assignment:2, assignment_lhs_identifier:cnt, assignment_rhs_atom:2, literal:2, single_assignment:cnt
    for i in x_i: # accumulate_all_elements:Add (-> +2), accumulate_elements:Add (-> +2), count_elements:cnt (-> +2), for:i (-> +2), for_each (-> +2), loop:for (-> +2), loop_with_late_exit:for (-> +2)
        y += (h / 3) * (4 - 2 * (cnt % 2)) * f(i) # assignment_lhs_identifier:y, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:4, assignment_rhs_atom:cnt, assignment_rhs_atom:h, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Div, binary_operator:Mod, binary_operator:Mult, binary_operator:Sub, call_argument:i, free_call:f, internal_free_call:f, literal:2, literal:3, literal:4, modulo_operator, multiplication_operator, suggest_constant_definition, update:y:2, update:y:3, update:y:4, update:y:cnt, update:y:h, update:y:i, update_by_augmented_assignment:y:2, update_by_augmented_assignment:y:3, update_by_augmented_assignment:y:4, update_by_augmented_assignment:y:cnt, update_by_augmented_assignment:y:h, update_by_augmented_assignment:y:i, update_by_augmented_assignment_with:Add, update_with:Add
        cnt += 1 # assignment_lhs_identifier:cnt, assignment_rhs_atom:1, augmented_assignment:Add, increment:cnt, literal:1, update:cnt:1, update_by_augmented_assignment:cnt:1, update_by_augmented_assignment_with:Add, update_with:Add
    y += (h / 3.0) * f(b) # assignment_lhs_identifier:y, assignment_rhs_atom:3.0, assignment_rhs_atom:b, assignment_rhs_atom:h, augmented_assignment:Add, binary_operator:Div, binary_operator:Mult, call_argument:b, free_call:f, internal_free_call:f, literal:3.0, multiplication_operator, suggest_constant_definition, update:y:3.0, update:y:b, update:y:h, update_by_augmented_assignment:y:3.0, update_by_augmented_assignment:y:b, update_by_augmented_assignment:y:h, update_by_augmented_assignment_with:Add, update_with:Add
    return y # return:y
def make_points(a, b, h): # function:make_points (-> +4), function_argument:a, function_argument:b, function_argument:h, function_argument_flavor:arg, generator:make_points (-> +4)
    x = a + h # addition_operator, assignment:Add, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:h, binary_operator:Add, single_assignment:x
    while x < (b - h): # binary_operator:Sub, comparison_operator:Lt, loop:while (-> +2), loop_with_late_exit:while (-> +2), while (-> +2)
        yield x # yield:x
        x = x + h # addition_operator, assignment:Add, assignment_lhs_identifier:x, assignment_rhs_atom:h, assignment_rhs_atom:x, binary_operator:Add, single_assignment:x, suggest_augmented_assignment, update:x:h, update_by_assignment:x:h, update_by_assignment_with:Add, update_with:Add
def f(x): # function:f (-> +2), function_argument:x, function_argument_flavor:arg, function_returning_something:f (-> +2)
    y = (x - 0) * (x - 0) # assignment:Mult, assignment_lhs_identifier:y, assignment_rhs_atom:0, assignment_rhs_atom:x, binary_operator:Mult, binary_operator:Sub, literal:0, multiplication_operator, single_assignment:y
    return y # return:y
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6), function_without_arguments:main (-> +6)
    a = 0.0 # assignment:0.0, assignment_lhs_identifier:a, assignment_rhs_atom:0.0, literal:0.0, single_assignment:a, suggest_constant_definition
    b = 1.0 # assignment:1.0, assignment_lhs_identifier:b, assignment_rhs_atom:1.0, literal:1.0, single_assignment:b, suggest_constant_definition
    steps = 10.0 # assignment:10.0, assignment_lhs_identifier:steps, assignment_rhs_atom:10.0, literal:10.0, single_assignment:steps, suggest_constant_definition
    boundary = [a, b] # assignment, assignment_lhs_identifier:boundary, assignment_rhs_atom:a, assignment_rhs_atom:b, literal:List, single_assignment:boundary
    y = method_2(boundary, steps) # assignment:method_2, assignment_lhs_identifier:y, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, call_argument:boundary, call_argument:steps, free_call:method_2, internal_free_call:method_2, single_assignment:y
    print("y = {0}".format(y)) # call_argument:, call_argument:y, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, member_call:format

# ----------------------------------------------------------------------------------------
# softmax.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, whole_span:6 (-> +5)
def softmax(vector): # function:softmax (-> +4), function_argument:vector, function_argument_flavor:arg, function_returning_something:softmax (-> +4)
    exponentVector = np.exp(vector) # assignment:exp, assignment_lhs_identifier:exponentVector, assignment_rhs_atom:np, assignment_rhs_atom:vector, call_argument:vector, member_call:exp, single_assignment:exponentVector
    sumOfExponents = np.sum(exponentVector) # assignment:sum, assignment_lhs_identifier:sumOfExponents, assignment_rhs_atom:exponentVector, assignment_rhs_atom:np, call_argument:exponentVector, member_call:sum, single_assignment:sumOfExponents
    softmax_vector = exponentVector / sumOfExponents # assignment:Div, assignment_lhs_identifier:softmax_vector, assignment_rhs_atom:exponentVector, assignment_rhs_atom:sumOfExponents, binary_operator:Div, single_assignment:softmax_vector
    return softmax_vector # return:softmax_vector

# ----------------------------------------------------------------------------------------
# sum_of_arithmetic_series.py
# ----------------------------------------------------------------------------------------
def sum_of_series(first_term, common_diff, num_of_terms): # function:sum_of_series (-> +2), function_argument:common_diff, function_argument:first_term, function_argument:num_of_terms, function_argument_flavor:arg, function_returning_something:sum_of_series (-> +2), whole_span:5 (-> +4)
    sum = (num_of_terms / 2) * (2 * first_term + (num_of_terms - 1) * common_diff) # addition_operator, assignment:Mult, assignment_lhs_identifier:sum, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:common_diff, assignment_rhs_atom:first_term, assignment_rhs_atom:num_of_terms, binary_operator:Add, binary_operator:Div, binary_operator:Mult, binary_operator:Sub, literal:1, literal:2, multiplication_operator, single_assignment:sum
    return sum # return:sum
def main(): # function:main (-> +1), function_returning_nothing:main (-> +1), function_without_arguments:main (-> +1)
    print(sum_of_series(1, 1, 10)) # call_argument:, call_argument:1, call_argument:10, composition, external_free_call:print, free_call:print, free_call:sum_of_series, free_call_without_result:print, internal_free_call:sum_of_series, literal:1, literal:10, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# test_prime_check.py
# ----------------------------------------------------------------------------------------
from .prime_check import Test # import_internally:prime_check:Test, import_module_internally:prime_check, import_name:Test, whole_span:2 (-> +1)
Test() # external_free_call:Test, free_call:Test, free_call_without_arguments:Test, free_call_without_result:Test

# ----------------------------------------------------------------------------------------
# trapezoidal_rule.py
# ----------------------------------------------------------------------------------------
def method_1(boundary, steps): # function:method_1 (-> +10), function_argument:boundary, function_argument:steps, function_argument_flavor:arg, function_returning_something:method_1 (-> +10), whole_span:26 (-> +25)
    h = (boundary[1] - boundary[0]) / steps # assignment:Div, assignment_lhs_identifier:h, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, binary_operator:Div, binary_operator:Sub, index:0, index:1, literal:0, literal:1, single_assignment:h
    a = boundary[0] # assignment, assignment_lhs_identifier:a, assignment_rhs_atom:0, assignment_rhs_atom:boundary, index:0, literal:0, single_assignment:a
    b = boundary[1] # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:1, assignment_rhs_atom:boundary, index:1, literal:1, single_assignment:b
    x_i = make_points(a, b, h) # assignment:make_points, assignment_lhs_identifier:x_i, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:h, call_argument:a, call_argument:b, call_argument:h, free_call:make_points, internal_free_call:make_points, single_assignment:x_i
    y = 0.0 # assignment:0.0, assignment_lhs_identifier:y, assignment_rhs_atom:0.0, literal:0.0, single_assignment:y, suggest_constant_definition
    y += (h / 2.0) * f(a) # assignment_lhs_identifier:y, assignment_rhs_atom:2.0, assignment_rhs_atom:a, assignment_rhs_atom:h, augmented_assignment:Add, binary_operator:Div, binary_operator:Mult, call_argument:a, free_call:f, internal_free_call:f, literal:2.0, multiplication_operator, suggest_constant_definition, update:y:2.0, update:y:a, update:y:h, update_by_augmented_assignment:y:2.0, update_by_augmented_assignment:y:a, update_by_augmented_assignment:y:h, update_by_augmented_assignment_with:Add, update_with:Add
    for i in x_i: # accumulate_all_elements:Add (-> +1), accumulate_elements:Add (-> +1), for:i (-> +1), for_each (-> +1), loop:for (-> +1), loop_with_late_exit:for (-> +1)
        y += h * f(i) # assignment_lhs_identifier:y, assignment_rhs_atom:h, assignment_rhs_atom:i, augmented_assignment:Add, binary_operator:Mult, call_argument:i, free_call:f, internal_free_call:f, multiplication_operator, update:y:h, update:y:i, update_by_augmented_assignment:y:h, update_by_augmented_assignment:y:i, update_by_augmented_assignment_with:Add, update_with:Add
    y += (h / 2.0) * f(b) # assignment_lhs_identifier:y, assignment_rhs_atom:2.0, assignment_rhs_atom:b, assignment_rhs_atom:h, augmented_assignment:Add, binary_operator:Div, binary_operator:Mult, call_argument:b, free_call:f, internal_free_call:f, literal:2.0, multiplication_operator, suggest_constant_definition, update:y:2.0, update:y:b, update:y:h, update_by_augmented_assignment:y:2.0, update_by_augmented_assignment:y:b, update_by_augmented_assignment:y:h, update_by_augmented_assignment_with:Add, update_with:Add
    return y # return:y
def make_points(a, b, h): # function:make_points (-> +4), function_argument:a, function_argument:b, function_argument:h, function_argument_flavor:arg, generator:make_points (-> +4)
    x = a + h # addition_operator, assignment:Add, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:h, binary_operator:Add, single_assignment:x
    while x < (b - h): # binary_operator:Sub, comparison_operator:Lt, loop:while (-> +2), loop_with_late_exit:while (-> +2), while (-> +2)
        yield x # yield:x
        x = x + h # addition_operator, assignment:Add, assignment_lhs_identifier:x, assignment_rhs_atom:h, assignment_rhs_atom:x, binary_operator:Add, single_assignment:x, suggest_augmented_assignment, update:x:h, update_by_assignment:x:h, update_by_assignment_with:Add, update_with:Add
def f(x): # function:f (-> +2), function_argument:x, function_argument_flavor:arg, function_returning_something:f (-> +2)
    y = (x - 0) * (x - 0) # assignment:Mult, assignment_lhs_identifier:y, assignment_rhs_atom:0, assignment_rhs_atom:x, binary_operator:Mult, binary_operator:Sub, literal:0, multiplication_operator, single_assignment:y
    return y # return:y
def main(): # function:main (-> +6), function_returning_nothing:main (-> +6), function_without_arguments:main (-> +6)
    a = 0.0 # assignment:0.0, assignment_lhs_identifier:a, assignment_rhs_atom:0.0, literal:0.0, single_assignment:a, suggest_constant_definition
    b = 1.0 # assignment:1.0, assignment_lhs_identifier:b, assignment_rhs_atom:1.0, literal:1.0, single_assignment:b, suggest_constant_definition
    steps = 10.0 # assignment:10.0, assignment_lhs_identifier:steps, assignment_rhs_atom:10.0, literal:10.0, single_assignment:steps, suggest_constant_definition
    boundary = [a, b] # assignment, assignment_lhs_identifier:boundary, assignment_rhs_atom:a, assignment_rhs_atom:b, literal:List, single_assignment:boundary
    y = method_1(boundary, steps) # assignment:method_1, assignment_lhs_identifier:y, assignment_rhs_atom:boundary, assignment_rhs_atom:steps, call_argument:boundary, call_argument:steps, free_call:method_1, internal_free_call:method_1, single_assignment:y
    print("y = {0}".format(y)) # call_argument:, call_argument:y, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, member_call:format

# ----------------------------------------------------------------------------------------
# volume.py
# ----------------------------------------------------------------------------------------
from math import pi # import:math:pi, import_module:math, import_name:pi, whole_span:27 (-> +26)
def vol_cube(side_length): # function:vol_cube (-> +1), function_argument:side_length, function_argument_flavor:arg, function_returning_something:vol_cube (-> +1)
    return float(side_length ** 3) # binary_operator:Pow, call_argument:, external_free_call:float, free_call:float, free_tail_call:float, literal:3, return, suggest_constant_definition
def vol_cuboid(width, height, length): # function:vol_cuboid (-> +1), function_argument:height, function_argument:length, function_argument:width, function_argument_flavor:arg, function_returning_something:vol_cuboid (-> +1)
    return float(width * height * length) # binary_operator:Mult, call_argument:, external_free_call:float, free_call:float, free_tail_call:float, multiplication_operator, return
def vol_cone(area_of_base, height): # function:vol_cone (-> +1), function_argument:area_of_base, function_argument:height, function_argument_flavor:arg, function_returning_something:vol_cone (-> +1)
    return (float(1) / 3) * area_of_base * height # binary_operator:Div, binary_operator:Mult, call_argument:1, external_free_call:float, free_call:float, literal:1, literal:3, multiplication_operator, return, suggest_constant_definition
def vol_right_circ_cone(radius, height): # function:vol_right_circ_cone (-> +1), function_argument:height, function_argument:radius, function_argument_flavor:arg, function_returning_something:vol_right_circ_cone (-> +1)
    return (float(1) / 3) * pi * (radius ** 2) * height # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, call_argument:1, external_free_call:float, free_call:float, literal:1, literal:2, literal:3, multiplication_operator, return, suggest_constant_definition
def vol_prism(area_of_base, height): # function:vol_prism (-> +1), function_argument:area_of_base, function_argument:height, function_argument_flavor:arg, function_returning_something:vol_prism (-> +1)
    return float(area_of_base * height) # binary_operator:Mult, call_argument:, external_free_call:float, free_call:float, free_tail_call:float, multiplication_operator, return
def vol_pyramid(area_of_base, height): # function:vol_pyramid (-> +1), function_argument:area_of_base, function_argument:height, function_argument_flavor:arg, function_returning_something:vol_pyramid (-> +1)
    return (float(1) / 3) * area_of_base * height # binary_operator:Div, binary_operator:Mult, call_argument:1, external_free_call:float, free_call:float, literal:1, literal:3, multiplication_operator, return, suggest_constant_definition
def vol_sphere(radius): # function:vol_sphere (-> +1), function_argument:radius, function_argument_flavor:arg, function_returning_something:vol_sphere (-> +1)
    return (float(4) / 3) * pi * radius ** 3 # binary_operator:Div, binary_operator:Mult, binary_operator:Pow, call_argument:4, external_free_call:float, free_call:float, literal:3, literal:4, multiplication_operator, return, suggest_constant_definition
def vol_circular_cylinder(radius, height): # function:vol_circular_cylinder (-> +1), function_argument:height, function_argument:radius, function_argument_flavor:arg, function_returning_something:vol_circular_cylinder (-> +1)
    return pi * radius ** 2 * height # binary_operator:Mult, binary_operator:Pow, literal:2, multiplication_operator, return
def main(): # function:main (-> +9), function_returning_nothing:main (-> +9), function_without_arguments:main (-> +9)
    print("Volumes:") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str
    print("Cube: " + str(vol_cube(2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation_operator:Str, external_free_call:print, external_free_call:str, free_call:print, free_call:str, free_call:vol_cube, free_call_without_result:print, internal_free_call:vol_cube, literal:2, literal:Str
    print("Cuboid: " + str(vol_cuboid(2, 2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation_operator:Str, external_free_call:print, external_free_call:str, free_call:print, free_call:str, free_call:vol_cuboid, free_call_without_result:print, internal_free_call:vol_cuboid, literal:2, literal:Str
    print("Cone: " + str(vol_cone(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation_operator:Str, external_free_call:print, external_free_call:str, free_call:print, free_call:str, free_call:vol_cone, free_call_without_result:print, internal_free_call:vol_cone, literal:2, literal:Str
    print("Right Circular Cone: " + str(vol_right_circ_cone(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation_operator:Str, external_free_call:print, external_free_call:str, free_call:print, free_call:str, free_call:vol_right_circ_cone, free_call_without_result:print, internal_free_call:vol_right_circ_cone, literal:2, literal:Str
    print("Prism: " + str(vol_prism(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation_operator:Str, external_free_call:print, external_free_call:str, free_call:print, free_call:str, free_call:vol_prism, free_call_without_result:print, internal_free_call:vol_prism, literal:2, literal:Str
    print("Pyramid: " + str(vol_pyramid(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation_operator:Str, external_free_call:print, external_free_call:str, free_call:print, free_call:str, free_call:vol_pyramid, free_call_without_result:print, internal_free_call:vol_pyramid, literal:2, literal:Str
    print("Sphere: " + str(vol_sphere(2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation_operator:Str, external_free_call:print, external_free_call:str, free_call:print, free_call:str, free_call:vol_sphere, free_call_without_result:print, internal_free_call:vol_sphere, literal:2, literal:Str
    print("Circular Cylinder: " + str(vol_circular_cylinder(2, 2))) # binary_operator:Add, call_argument:, call_argument:2, composition, concatenation_operator:Str, external_free_call:print, external_free_call:str, free_call:print, free_call:str, free_call:vol_circular_cylinder, free_call_without_result:print, internal_free_call:vol_circular_cylinder, literal:2, literal:Str

# ----------------------------------------------------------------------------------------
# zellers_congruence.py
# ----------------------------------------------------------------------------------------
import datetime # import:datetime, import_module:datetime, whole_span:49 (-> +48)
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
    convert_datetime_days = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 0} # assignment, assignment_lhs_identifier:convert_datetime_days, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:4, assignment_rhs_atom:5, assignment_rhs_atom:6, literal:0, literal:1, literal:2, literal:3, literal:4, literal:5, literal:6, literal:Dict, single_assignment:convert_datetime_days, suggest_constant_definition
    if not 0 < len(date_input) < 11: # call_argument:date_input, chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, external_free_call:len, free_call:len, if (-> +1), if_test_atom:0, if_test_atom:11, if_test_atom:date_input, if_without_else (-> +1), literal:0, literal:11, suggest_constant_definition, unary_operator:Not, yoda_comparison:Lt
        raise ValueError("Must be 10 characters long") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    m: int = int(date_input[0] + date_input[1]) # addition_operator, binary_operator:Add, call_argument:, external_free_call:int, free_call:int, index:0, index:1, literal:0, literal:1
    if not 0 < m < 13: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +1), if_test_atom:0, if_test_atom:13, if_test_atom:m, if_without_else (-> +1), literal:0, literal:13, suggest_constant_definition, unary_operator:Not, yoda_comparison:Lt
        raise ValueError("Month must be between 1 - 12") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    sep_1: str = date_input[2] # index:2, literal:2
    if sep_1 not in ["-", "/"]: # comparison_operator:NotIn, if (-> +1), if_test_atom:sep_1, if_without_else (-> +1), literal:List, literal:Str
        raise ValueError("Date seperator must be '-' or '/'") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    d: int = int(date_input[3] + date_input[4]) # addition_operator, binary_operator:Add, call_argument:, external_free_call:int, free_call:int, index:3, index:4, literal:3, literal:4, suggest_constant_definition
    if not 0 < d < 32: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +1), if_test_atom:0, if_test_atom:32, if_test_atom:d, if_without_else (-> +1), literal:0, literal:32, suggest_constant_definition, unary_operator:Not, yoda_comparison:Lt
        raise ValueError("Date must be between 1 - 31") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    sep_2: str = date_input[5] # index:5, literal:5, suggest_constant_definition
    if sep_2 not in ["-", "/"]: # comparison_operator:NotIn, if (-> +1), if_test_atom:sep_2, if_without_else (-> +1), literal:List, literal:Str
        raise ValueError("Date seperator must be '-' or '/'") # call_argument:, external_free_call:ValueError, free_call:ValueError, if_then_branch, literal:Str, raise:ValueError
    y: int = int(date_input[6] + date_input[7] + date_input[8] + date_input[9]) # addition_operator, binary_operator:Add, call_argument:, external_free_call:int, free_call:int, index:6, index:7, index:8, index:9, literal:6, literal:7, literal:8, literal:9, suggest_constant_definition
    if not 45 < y < 8500: # chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, if (-> +2), if_test_atom:45, if_test_atom:8500, if_test_atom:y, if_without_else (-> +2), literal:45, literal:8500, suggest_constant_definition, unary_operator:Not, yoda_comparison:Lt
        raise ValueError( # external_free_call:ValueError, free_call:ValueError, if_then_branch (-> +1), raise:ValueError
            "Year out of range. There has to be some sort of limit...right?" # call_argument:, literal:Str
        )
    dt_ck = datetime.date(int(y), int(m), int(d)) # assignment:date, assignment_lhs_identifier:dt_ck, assignment_rhs_atom:d, assignment_rhs_atom:datetime, assignment_rhs_atom:m, assignment_rhs_atom:y, call_argument:, call_argument:d, call_argument:m, call_argument:y, composition, external_free_call:int, free_call:int, member_call:date, single_assignment:dt_ck
    if m <= 2: # comparison_operator:LtE, if (-> +2), if_test_atom:2, if_test_atom:m, if_without_else (-> +2), literal:2
        y = y - 1 # assignment:Sub, assignment_lhs_identifier:y, assignment_rhs_atom:1, assignment_rhs_atom:y, binary_operator:Sub, if_then_branch (-> +1), literal:1, single_assignment:y, suggest_augmented_assignment, update:y:1, update_by_assignment:y:1, update_by_assignment_with:Sub, update_with:Sub
        m = m + 12 # addition_operator, assignment:Add, assignment_lhs_identifier:m, assignment_rhs_atom:12, assignment_rhs_atom:m, binary_operator:Add, increment:m, literal:12, single_assignment:m, suggest_augmented_assignment, suggest_constant_definition, update:m:12, update_by_assignment:m:12, update_by_assignment_with:Add, update_with:Add
    c: int = int(str(y)[:2]) # call_argument:, call_argument:y, composition, external_free_call:int, external_free_call:str, free_call:int, free_call:str, literal:2, slice::2:, slice_lower:, slice_step:, slice_upper:2
    k: int = int(str(y)[2:]) # call_argument:, call_argument:y, composition, external_free_call:int, external_free_call:str, free_call:int, free_call:str, literal:2, slice:2::, slice_lower:2, slice_step:, slice_upper:
    t: int = int(2.6 * m - 5.39) # binary_operator:Mult, binary_operator:Sub, call_argument:, external_free_call:int, free_call:int, literal:2.6, literal:5.39, multiplication_operator, suggest_constant_definition
    u: int = int(c / 4) # binary_operator:Div, call_argument:, external_free_call:int, free_call:int, literal:4, suggest_constant_definition
    v: int = int(k / 4) # binary_operator:Div, call_argument:, external_free_call:int, free_call:int, literal:4, suggest_constant_definition
    x: int = int(d + k) # addition_operator, binary_operator:Add, call_argument:, external_free_call:int, free_call:int
    z: int = int(t + u + v + x) # addition_operator, binary_operator:Add, call_argument:, external_free_call:int, free_call:int
    w: int = int(z - (2 * c)) # binary_operator:Mult, binary_operator:Sub, call_argument:, external_free_call:int, free_call:int, literal:2, multiplication_operator
    f: int = round(w % 7) # binary_operator:Mod, call_argument:, external_free_call:round, free_call:round, literal:7, modulo_operator, suggest_constant_definition
    if f != convert_datetime_days[dt_ck.weekday()]: # comparison_operator:NotEq, if (-> +1), if_test_atom:convert_datetime_days, if_test_atom:dt_ck, if_test_atom:f, if_without_else (-> +1), index:_, member_call:weekday, member_call_object:dt_ck
        raise AssertionError("The date was evaluated incorrectly. Contact developer.") # call_argument:, external_free_call:AssertionError, free_call:AssertionError, if_then_branch, literal:Str, raise:AssertionError
    response: str = f"Your date {date_input}, is a {days[str(f)]}!" # call_argument:f, external_free_call:str, free_call:str, index:_, literal:Str
    return response # return:response
