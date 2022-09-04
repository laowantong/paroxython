# ----------------------------------------------------------------------------------------
# 01_hello_world.py
# ----------------------------------------------------------------------------------------
print("Hello, world!") # argument:, external_free_call:print, flat_style, free_call:print, free_call_without_result:print, imperative_style, literal:Str, node:Call, node:Expr, node:Name, node:Str, one_liner_style, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 02_input_name.py
# ----------------------------------------------------------------------------------------
name = input("What is your name?\n") # argument:, assignment:input, assignment_lhs_identifier:name, external_free_call:input, flat_style (-> +1), free_call:input, global_scope:name (-> +1), imperative_style (-> +1), literal:Str, node:Assign, node:Call, node:Name, node:Str, scope:name (-> +1), single_assignment:name, special_literal_string:What is your name?\n, variety:1 (-> +1), whole_span:2 (-> +1)
print("Hi, %s." % name) # argument:, binary_operator:Mod, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:name, node:BinOp, node:Call, node:Expr, node:Name, node:Str, string_formatting_operator

# ----------------------------------------------------------------------------------------
# 03_friends.py
# ----------------------------------------------------------------------------------------
friends = ["john", "pat", "gary", "michael"] # assignment, assignment_lhs_identifier:friends, global_scope:friends (-> +2), global_scope:i (-> +2), global_scope:name (-> +2), imperative_style (-> +2), literal:List, literal:Str, node:Assign, node:List, node:Name, node:Str, scope:friends (-> +2), scope:i (-> +2), scope:name (-> +2), single_assignment:friends, variety:1 (-> +2), whole_span:3 (-> +2)
for i, name in enumerate(friends): # argument:friends, external_free_call:enumerate, for:i (-> +1), for:name (-> +1), for_indexes_elements:i (-> +1), free_call:enumerate, iteration_variable:i, iteration_variable:name, literal:Tuple, loaded_variable:friends, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:Call, node:For (-> +1), node:Name, node:Tuple
    print("iteration {iteration} is {name}".format(iteration=i, name=name)) # argument:, argument:i, argument:name, composition, external_free_call:print, free_call:print, free_call_with_keyword_argument:print:iteration, free_call_with_keyword_argument:print:name, free_call_without_result:print, keyword_argument:iteration, keyword_argument:name, literal:Str, loaded_variable:i, loaded_variable:name, member_call_method:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str, node:keyword

# ----------------------------------------------------------------------------------------
# 04_fibonacci.py
# ----------------------------------------------------------------------------------------
parents, babies = (1, 1) # assignment, assignment_lhs_identifier:babies, assignment_lhs_identifier:parents, assignment_rhs_atom:1, global_scope:babies (-> +3), global_scope:parents (-> +3), imperative_style (-> +3), literal:1, literal:Tuple, node:Assign, node:Name, node:Num, node:Tuple, parallel_assignment:2, scope:babies (-> +3), scope:parents (-> +3), variety:2 (-> +3), whole_span:4 (-> +3)
while babies < 100: # comparison_operator:Lt, literal:100, loaded_variable:babies, loop:while (-> +2), loop_with_late_exit:while (-> +2), magic_number:100, node:Compare, node:Name, node:Num, node:While (-> +2)
    print("This generation has {} babies".format(babies)) # argument:, argument:babies, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:babies, member_call_method:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str
    parents, babies = (babies, parents + babies) # addition_operator, assignment, assignment_lhs_identifier:babies, assignment_lhs_identifier:parents, assignment_rhs_atom:babies, assignment_rhs_atom:parents, binary_operator:Add, literal:Tuple, loaded_variable:babies, loaded_variable:parents, node:Assign, node:BinOp, node:Name, node:Tuple, parallel_assignment:2, slide, update:babies:parents, update:parents:babies, update_by_assignment:babies:parents, update_by_assignment:parents:babies, update_by_assignment_with, update_with

# ----------------------------------------------------------------------------------------
# 05_greet.py
# ----------------------------------------------------------------------------------------
def greet(name): # function:greet (-> +1), function_line_count:2 (-> +1), function_parameter:name, function_parameter_flavor:arg, function_returning_nothing:greet (-> +1), local_scope:name (-> +1), node:FunctionDef (-> +1), node:arg, procedural_style (-> +4), scope:name (-> +1), variety:2 (-> +4), whole_span:5 (-> +4)
    print("Hello", name) # argument:, argument:name, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:name, node:Call, node:Expr, node:Name, node:Str
greet("Jack") # argument:, free_call:greet, free_call_without_result:greet, internal_free_call:greet, literal:Str, node:Call, node:Expr, node:Name, node:Str
greet("Jill") # argument:, free_call:greet, free_call_without_result:greet, internal_free_call:greet, literal:Str, node:Call, node:Expr, node:Name, node:Str
greet("Bob") # argument:, free_call:greet, free_call_without_result:greet, internal_free_call:greet, literal:Str, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 06_regex.py
# ----------------------------------------------------------------------------------------
import re # global_scope:test_string (-> +5), imperative_style (-> +5), import:re, import_module:re, node:Import, scope:test_string (-> +5), variety:2 (-> +5), whole_span:6 (-> +5)
for test_string in ["555-1212", "ILL-EGAL"]: # for:test_string (-> +4), iteration_variable:test_string, literal:List, literal:Str, loop:for (-> +4), loop_with_late_exit:for (-> +4), node:For (-> +4), node:List, node:Name, node:Str
    if re.match(r"^\d{3}-\d{4}$", test_string): # argument:, argument:test_string, if (-> +3), if_test_atom:re, if_test_atom:test_string, literal:Str, loaded_variable:re, loaded_variable:test_string, member_call_method:match, node:Attribute, node:Call, node:If (-> +3), node:Name, node:Str, special_literal_string:^\\d{3}-\\d{4}$
        print(test_string, "is a valid US local phone number") # argument:, argument:test_string, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, loaded_variable:test_string, node:Call, node:Expr, node:Name, node:Str
    else:
        print(test_string, "rejected") # argument:, argument:test_string, external_free_call:print, free_call:print, free_call_without_result:print, if_else_branch, literal:Str, loaded_variable:test_string, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 07_grocery_bill.py
# ----------------------------------------------------------------------------------------
prices = {"apple": 0.40, "banana": 0.50} # assignment, assignment_lhs_identifier:prices, assignment_rhs_atom:0.4, assignment_rhs_atom:0.5, flat_style (-> +3), global_scope:grocery_bill (-> +3), global_scope:my_purchase (-> +3), global_scope:prices (-> +3), imperative_style (-> +3), literal:0.4, literal:0.5, literal:Dict, literal:Str, magic_number:0.4, magic_number:0.5, node:Assign, node:Dict, node:Name, node:Num, node:Str, scope:grocery_bill (-> +3), scope:my_purchase (-> +3), scope:prices (-> +3), single_assignment:prices, variety:1 (-> +3), whole_span:4 (-> +3)
my_purchase = {"apple": 1, "banana": 6} # assignment, assignment_lhs_identifier:my_purchase, assignment_rhs_atom:1, assignment_rhs_atom:6, literal:1, literal:6, literal:Dict, literal:Str, magic_number:6, node:Assign, node:Dict, node:Name, node:Num, node:Str, single_assignment:my_purchase
grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase) # argument:, assignment:sum, assignment_lhs_identifier:grocery_bill, assignment_rhs_atom:fruit, assignment_rhs_atom:my_purchase, assignment_rhs_atom:prices, binary_operator:Mult, comprehension:Generator, comprehension_for_count:1, external_free_call:sum, free_call:sum, index:fruit, iteration_variable:fruit, loaded_variable:fruit, loaded_variable:my_purchase, loaded_variable:prices, local_scope:fruit, multiplication_operator, node:Assign, node:BinOp, node:Call, node:GeneratorExp, node:Name, node:Subscript, node:comprehension, scope:fruit, single_assignment:grocery_bill
print("I owe the grocer $%.2f" % grocery_bill) # argument:, binary_operator:Mod, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:grocery_bill, node:BinOp, node:Call, node:Expr, node:Name, node:Str, string_formatting_operator

# ----------------------------------------------------------------------------------------
# 08_arguments.py
# ----------------------------------------------------------------------------------------
import sys # global_scope:total (-> +5), imperative_style (-> +5), import:sys, import_module:sys, node:Import, scope:total (-> +5), variety:3 (-> +5), whole_span:6 (-> +5)
try: # node:Try (-> +4), try_except:ValueError (-> +4)
    total = sum(int(arg) for arg in sys.argv[1:]) # argument:, argument:arg, assignment:sum, assignment_lhs_identifier:total, assignment_rhs_atom:1, assignment_rhs_atom:arg, assignment_rhs_atom:sys, composition, comprehension:Generator, comprehension_for_count:1, external_free_call:int, external_free_call:sum, free_call:int, free_call:sum, iteration_variable:arg, literal:1, loaded_variable:arg, loaded_variable:sys, local_scope:arg, node:Assign, node:Attribute, node:Call, node:GeneratorExp, node:Name, node:Num, node:Slice, node:Subscript, node:comprehension, scope:arg, single_assignment:total, slice:1::, slice_lower:1, slice_step:, slice_upper:, value_attr:argv
    print("sum =", total) # argument:, argument:total, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:total, node:Call, node:Expr, node:Name, node:Str
except ValueError: # except:ValueError, loaded_variable:ValueError, node:ExceptHandler (-> +1), node:Name
    print("Please supply integer arguments") # argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 09_indent.py
# ----------------------------------------------------------------------------------------
import glob # global_scope:file_name (-> +7), global_scope:line (-> +7), global_scope:python_files (-> +7), imperative_style (-> +7), import:glob, import_module:glob, node:Import, scope:file_name (-> +7), scope:line (-> +7), scope:python_files (-> +7), variety:3 (-> +7), whole_span:8 (-> +7)
python_files = glob.glob("*.py") # argument:, assignment:glob, assignment_lhs_identifier:python_files, assignment_rhs_atom:glob, literal:Str, loaded_variable:glob, member_call_method:glob, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:python_files
for file_name in sorted(python_files): # argument:python_files, external_free_call:sorted, for:file_name (-> +5), free_call:sorted, iteration_variable:file_name, loaded_variable:python_files, loop:for (-> +5), loop_with_late_exit:for (-> +5), node:Call, node:For (-> +5), node:Name
    print("    ------" + file_name) # argument:, binary_operator:Add, concatenation_operator:Str, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:file_name, node:BinOp, node:Call, node:Expr, node:Name, node:Str
    with open(file_name) as f: # argument:file_name, external_free_call:open, free_call:open, loaded_variable:file_name, node:Call, node:Name, node:With (-> +2), node:withitem
        for line in f: # for:line (-> +1), for_each:line (-> +1), iteration_variable:line, loaded_variable:f, loop:for (-> +1), loop_with_late_exit:for (-> +1), nested_for:1 (-> +1), node:For (-> +1), node:Name
            print("    " + line.rstrip()) # argument:, binary_operator:Add, composition, concatenation_operator:Str, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:line, member_call_method:rstrip, node:Attribute, node:BinOp, node:Call, node:Expr, node:Name, node:Str
    print() # external_free_call:print, free_call:print, free_call_no_arguments:print, free_call_without_result:print, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 10_time.py
# ----------------------------------------------------------------------------------------
from time import localtime # global_scope:activities (-> +16), global_scope:activity_time (-> +16), global_scope:hour (-> +16), global_scope:time_now (-> +16), imperative_style (-> +16), import:time:localtime, import_module:time, import_name:localtime, node:ImportFrom, scope:activities (-> +16), scope:activity_time (-> +16), scope:hour (-> +16), scope:time_now (-> +16), variety:5 (-> +16), whole_span:17 (-> +16)
activities = { # assignment, assignment_lhs_identifier:activities, literal:Dict, node:Assign (-> +6), node:Dict (-> +6), node:Name, single_assignment:activities
    8: "Sleeping", # assignment_rhs_atom:8, literal:8, literal:Str, magic_number:8, node:Num, node:Str
    9: "Commuting", # assignment_rhs_atom:9, literal:9, literal:Str, magic_number:9, node:Num, node:Str
    17: "Working", # assignment_rhs_atom:17, literal:17, literal:Str, magic_number:17, node:Num, node:Str
    18: "Commuting", # assignment_rhs_atom:18, literal:18, literal:Str, magic_number:18, node:Num, node:Str
    20: "Eating", # assignment_rhs_atom:20, literal:20, literal:Str, magic_number:20, node:Num, node:Str
    22: "Resting", # assignment_rhs_atom:22, literal:22, literal:Str, magic_number:22, node:Num, node:Str
}
time_now = localtime() # assignment:localtime, assignment_lhs_identifier:time_now, external_free_call:localtime, free_call:localtime, free_call_no_arguments:localtime, node:Assign, node:Call, node:Name, single_assignment:time_now
hour = time_now.tm_hour # assignment, assignment_lhs_identifier:hour, assignment_rhs_atom:time_now, loaded_variable:time_now, node:Assign, node:Attribute, node:Name, single_assignment:hour
for activity_time in sorted(activities.keys()): # argument:, composition, external_free_call:sorted, for:activity_time (-> +5), free_call:sorted, iteration_variable:activity_time, loaded_variable:activities, loop:for (-> +5), loop_with_break:for (-> +5), loop_with_early_exit:for:break (-> +5), loop_with_else:for (-> +5), member_call_method:keys, node:Attribute, node:Call, node:For (-> +5), node:Name
    if hour < activity_time: # comparison_operator:Lt, if (-> +2), if_test_atom:activity_time, if_test_atom:hour, if_without_else (-> +2), loaded_variable:activity_time, loaded_variable:hour, node:Compare, node:If (-> +2), node:Name
        print(activities[activity_time]) # argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch (-> +1), index:activity_time, loaded_variable:activities, loaded_variable:activity_time, node:Call, node:Expr, node:Name, node:Subscript
        break # node:Break
else:
    print("Unknown, AFK or sleeping!") # argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loop_else, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 11_bottles.py
# ----------------------------------------------------------------------------------------
REFRAIN = """ # assignment, assignment_lhs_identifier:REFRAIN, global_scope:REFRAIN (-> +9), global_scope:bottles_of_beer (-> +9), imperative_style (-> +9), literal:Str, node:Assign, node:Name, node:Str, scope:REFRAIN (-> +9), scope:bottles_of_beer (-> +9), single_assignment:REFRAIN, special_literal_string:\n%d bottles of beer on the wall,\n%d bottles of beer,\ntake one down, pass it around,\n%d bottles of beer on the wall!\n, variety:3 (-> +9), whole_span:10 (-> +9)
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
"""
bottles_of_beer = 9 # assignment:9, assignment_lhs_identifier:bottles_of_beer, assignment_rhs_atom:9, literal:9, magic_number:9, node:Assign, node:Name, node:Num, single_assignment:bottles_of_beer
while bottles_of_beer > 1: # comparison_operator:Gt, literal:1, loaded_variable:bottles_of_beer, loop:while (-> +2), loop_with_late_exit:while (-> +2), node:Compare, node:Name, node:Num, node:While (-> +2)
    print(REFRAIN % (bottles_of_beer, bottles_of_beer, bottles_of_beer - 1)) # argument:, binary_operator:Mod, binary_operator:Sub, external_free_call:print, free_call:print, free_call_without_result:print, literal:1, literal:Tuple, loaded_variable:REFRAIN, loaded_variable:bottles_of_beer, modulo_operator, node:BinOp, node:Call, node:Expr, node:Name, node:Num, node:Tuple
    bottles_of_beer -= 1 # assignment_lhs_identifier:bottles_of_beer, assignment_rhs_atom:1, augmented_assignment:Sub, literal:1, node:AugAssign, node:Name, node:Num, update:bottles_of_beer:1, update_by_augmented_assignment:bottles_of_beer:1, update_by_augmented_assignment_with:Sub, update_with:Sub

# ----------------------------------------------------------------------------------------
# 12_classes.py
# ----------------------------------------------------------------------------------------
class BankAccount(object): # class:BankAccount (-> +8), class_method_count:4 (-> +8), global_scope:my_account (-> +11), loaded_variable:object, node:ClassDef (-> +8), node:Name, object_oriented_style (-> +11), scope:my_account (-> +11), variety:4 (-> +11), whole_span:12 (-> +11)
    def __init__(self, initial_balance=0): # function:__init__ (-> +1), function_line_count:2 (-> +1), function_parameter:initial_balance, function_parameter:self, function_parameter_default:Num, function_parameter_flavor:arg, function_returning_nothing:__init__ (-> +1), instance_method:__init__ (-> +1), literal:0, local_scope:initial_balance (-> +1), local_scope:self (-> +1), method:__init__ (-> +1), node:FunctionDef (-> +1), node:Num, node:arg, scope:initial_balance (-> +1), scope:self (-> +1)
        self.balance = initial_balance # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:initial_balance, loaded_variable:initial_balance, loaded_variable:self, node:Assign, node:Attribute, node:Name
    def deposit(self, amount): # function:deposit (-> +1), function_line_count:2 (-> +1), function_parameter:amount, function_parameter:self, function_parameter_flavor:arg, function_returning_nothing:deposit (-> +1), instance_method:deposit (-> +1), local_scope:amount (-> +1), local_scope:self (-> +1), method:deposit (-> +1), node:FunctionDef (-> +1), node:arg, scope:amount (-> +1), scope:self (-> +1)
        self.balance += amount # assignment_lhs_identifier:self, assignment_rhs_atom:amount, augmented_assignment:Add, loaded_variable:amount, loaded_variable:self, node:Attribute, node:AugAssign, node:Name, update:self:amount, update_by_augmented_assignment:self:amount, update_by_augmented_assignment_with:Add, update_with:Add
    def withdraw(self, amount): # function:withdraw (-> +1), function_line_count:2 (-> +1), function_parameter:amount, function_parameter:self, function_parameter_flavor:arg, function_returning_nothing:withdraw (-> +1), instance_method:withdraw (-> +1), local_scope:amount (-> +1), local_scope:self (-> +1), method:withdraw (-> +1), node:FunctionDef (-> +1), node:arg, scope:amount (-> +1), scope:self (-> +1)
        self.balance -= amount # assignment_lhs_identifier:self, assignment_rhs_atom:amount, augmented_assignment:Sub, loaded_variable:amount, loaded_variable:self, node:Attribute, node:AugAssign, node:Name, update:self:amount, update_by_augmented_assignment:self:amount, update_by_augmented_assignment_with:Sub, update_with:Sub
    def overdrawn(self): # function:overdrawn (-> +1), function_line_count:2 (-> +1), function_parameter:self, function_parameter_flavor:arg, function_returning_something:overdrawn (-> +1), instance_method:overdrawn (-> +1), local_scope:self (-> +1), method:overdrawn (-> +1), node:FunctionDef (-> +1), node:arg, scope:self (-> +1)
        return self.balance < 0 # comparison_operator:Lt, literal:0, loaded_variable:self, node:Attribute, node:Compare, node:Name, node:Num, node:Return, return
my_account = BankAccount(15) # argument:15, assignment:BankAccount, assignment_lhs_identifier:my_account, assignment_rhs_atom:15, external_free_call:BankAccount, free_call:BankAccount, literal:15, magic_number:15, node:Assign, node:Call, node:Name, node:Num, single_assignment:my_account
my_account.withdraw(50) # argument:50, literal:50, loaded_variable:my_account, magic_number:50, member_call:my_account:withdraw, member_call_method:withdraw, member_call_object:my_account, node:Attribute, node:Call, node:Expr, node:Name, node:Num
print(my_account.balance, my_account.overdrawn()) # argument:, composition, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:my_account, member_call_method:overdrawn, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 13_unit_testing.py
# ----------------------------------------------------------------------------------------
import unittest # import:unittest, import_module:unittest, node:Import, object_oriented_style (-> +10), variety:3 (-> +10), whole_span:11 (-> +10)
def median(pool): # function:median (-> +6), function_line_count:7 (-> +6), function_parameter:pool, function_parameter_flavor:arg, function_returning_something:median (-> +6), impure_function:median (-> +6), local_scope:copy (-> +6), local_scope:pool (-> +6), local_scope:size (-> +6), node:FunctionDef (-> +6), node:arg, scope:copy (-> +6), scope:pool (-> +6), scope:size (-> +6)
    copy = sorted(pool) # argument:pool, assignment:sorted, assignment_lhs_identifier:copy, assignment_rhs_atom:pool, external_free_call:sorted, free_call:sorted, loaded_variable:pool, node:Assign, node:Call, node:Name, single_assignment:copy
    size = len(copy) # argument:copy, assignment:len, assignment_lhs_identifier:size, assignment_rhs_atom:copy, external_free_call:len, free_call:len, loaded_variable:copy, node:Assign, node:Call, node:Name, single_assignment:size
    if size % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:1, if_test_atom:2, if_test_atom:size, literal:1, literal:2, loaded_variable:size, modulo_operator, node:BinOp, node:Compare, node:If (-> +3), node:Name, node:Num
        return copy[int((size - 1) / 2)] # argument:, binary_operator:Div, binary_operator:Sub, external_free_call:int, free_call:int, if_then_branch, index:_, literal:1, literal:2, loaded_variable:copy, loaded_variable:size, node:BinOp, node:Call, node:Name, node:Num, node:Return, node:Subscript, return
    else:
        return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2 # addition_operator, argument:, binary_operator:Add, binary_operator:Div, binary_operator:Sub, external_free_call:int, free_call:int, if_else_branch, index:_, literal:1, literal:2, loaded_variable:copy, loaded_variable:size, node:BinOp, node:Call, node:Name, node:Num, node:Return, node:Subscript, return
class TestMedian(unittest.TestCase): # class:TestMedian (-> +2), class_method_count:1 (-> +2), loaded_variable:unittest, node:Attribute, node:ClassDef (-> +2), node:Name
    def testMedian(self): # function:testMedian (-> +1), function_line_count:2 (-> +1), function_parameter:self, function_parameter_flavor:arg, function_returning_nothing:testMedian (-> +1), instance_method:testMedian (-> +1), local_scope:self (-> +1), method:testMedian (-> +1), node:FunctionDef (-> +1), node:arg, scope:self (-> +1)
        self.assertEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7) # argument:, argument:7, composition, free_call:median, internal_free_call:median, literal:2, literal:4, literal:5, literal:7, literal:8, literal:9, literal:List, loaded_variable:self, magic_number:4, magic_number:5, magic_number:7, magic_number:8, magic_number:9, member_call:self:assertEqual, member_call_method:assertEqual, member_call_object:self, node:Attribute, node:Call, node:Expr, node:List, node:Name, node:Num

# ----------------------------------------------------------------------------------------
# 14_median.py
# ----------------------------------------------------------------------------------------
def median(pool): # function:median (-> +6), function_line_count:7 (-> +6), function_parameter:pool, function_parameter_flavor:arg, function_returning_something:median (-> +6), impure_function:median (-> +6), local_scope:copy (-> +6), local_scope:pool (-> +6), local_scope:size (-> +6), node:FunctionDef (-> +6), node:arg, procedural_style (-> +6), scope:copy (-> +6), scope:pool (-> +6), scope:size (-> +6), variety:2 (-> +6), whole_span:7 (-> +6)
    copy = sorted(pool) # argument:pool, assignment:sorted, assignment_lhs_identifier:copy, assignment_rhs_atom:pool, external_free_call:sorted, free_call:sorted, loaded_variable:pool, node:Assign, node:Call, node:Name, single_assignment:copy
    size = len(copy) # argument:copy, assignment:len, assignment_lhs_identifier:size, assignment_rhs_atom:copy, external_free_call:len, free_call:len, loaded_variable:copy, node:Assign, node:Call, node:Name, single_assignment:size
    if size % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:1, if_test_atom:2, if_test_atom:size, literal:1, literal:2, loaded_variable:size, modulo_operator, node:BinOp, node:Compare, node:If (-> +3), node:Name, node:Num
        return copy[int((size - 1) / 2)] # argument:, binary_operator:Div, binary_operator:Sub, external_free_call:int, free_call:int, if_then_branch, index:_, literal:1, literal:2, loaded_variable:copy, loaded_variable:size, node:BinOp, node:Call, node:Name, node:Num, node:Return, node:Subscript, return
    else:
        return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2 # addition_operator, argument:, binary_operator:Add, binary_operator:Div, binary_operator:Sub, external_free_call:int, free_call:int, if_else_branch, index:_, literal:1, literal:2, loaded_variable:copy, loaded_variable:size, node:BinOp, node:Call, node:Name, node:Num, node:Return, node:Subscript, return

# ----------------------------------------------------------------------------------------
# 15_itertools_groupby.py
# ----------------------------------------------------------------------------------------
from itertools import groupby # global_scope:frags (-> +8), global_scope:has_chars (-> +8), global_scope:lines (-> +8), imperative_style (-> +8), import:itertools:groupby, import_module:itertools, import_name:groupby, node:ImportFrom, scope:frags (-> +8), scope:has_chars (-> +8), scope:lines (-> +8), variety:3 (-> +8), whole_span:9 (-> +8)
lines = """ # assignment:splitlines, assignment_lhs_identifier:lines, literal:Str, member_call_method:splitlines, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:lines, special_literal_string:\nThis is the\nfirst paragraph.\nThis is the second.\n
This is the
first paragraph.
This is the second.
""".splitlines()
for has_chars, frags in groupby(lines, bool): # argument:bool, argument:lines, external_free_call:groupby, for:frags (-> +2), for:has_chars (-> +2), free_call:groupby, iteration_variable:frags, iteration_variable:has_chars, literal:Tuple, loaded_variable:bool, loaded_variable:lines, loop:for (-> +2), loop_with_late_exit:for (-> +2), node:Call, node:For (-> +2), node:Name, node:Tuple
    if has_chars: # if (-> +1), if_without_else (-> +1), loaded_variable:has_chars, node:If (-> +1), node:Name
        print(" ".join(frags)) # argument:, argument:frags, composition, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, loaded_variable:frags, member_call_method:join, node:Attribute, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 16_csv.py
# ----------------------------------------------------------------------------------------
import csv # global_scope:change (-> +17), global_scope:name (-> +17), global_scope:pct (-> +17), global_scope:price (-> +17), global_scope:status (-> +17), global_scope:status_labels (-> +17), global_scope:stocks (-> +17), global_scope:ticker (-> +17), global_scope:writer (-> +17), import:csv, import_module:csv, node:Import, procedural_style (-> +17), scope:change (-> +17), scope:name (-> +17), scope:pct (-> +17), scope:price (-> +17), scope:status (-> +17), scope:status_labels (-> +17), scope:stocks (-> +17), scope:ticker (-> +17), scope:writer (-> +17), variety:3 (-> +17), whole_span:18 (-> +17)
def cmp(a, b): # function:cmp (-> +1), function_line_count:2 (-> +1), function_parameter:a, function_parameter:b, function_parameter_flavor:arg, function_returning_something:cmp (-> +1), local_scope:a (-> +1), local_scope:b (-> +1), node:FunctionDef (-> +1), node:arg, pure_function:cmp (-> +1), scope:a (-> +1), scope:b (-> +1)
    return (a > b) - (a < b) # binary_operator:Sub, comparison_operator:Gt, comparison_operator:Lt, loaded_variable:a, loaded_variable:b, node:BinOp, node:Compare, node:Name, node:Return, return
with open("stocks.csv", "w", newline="") as stocksFileW: # argument:, empty_literal:Str, external_free_call:open, free_call:open, free_call_with_keyword_argument:open:newline, keyword_argument:newline, literal:Str, node:Call, node:Name, node:Str, node:With (-> +6), node:keyword, node:withitem
    writer = csv.writer(stocksFileW) # argument:stocksFileW, assignment:writer, assignment_lhs_identifier:writer, assignment_rhs_atom:csv, assignment_rhs_atom:stocksFileW, loaded_variable:csv, loaded_variable:stocksFileW, member_call_method:writer, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:writer
    writer.writerows( # loaded_variable:writer, member_call:writer:writerows, member_call_method:writerows, member_call_object:writer, node:Attribute, node:Call (-> +4), node:Expr (-> +4), node:Name
        [ # argument:, literal:List, node:List (-> +3)
            ["GOOG", "Google, Inc.", 505.24, 0.47, 0.09], # literal:0.09, literal:0.47, literal:505.24, literal:List, literal:Str, magic_number:0.09, magic_number:0.47, magic_number:505.24, node:List, node:Num, node:Str
            ["YHOO", "Yahoo! Inc.", 27.38, 0.33, 1.22], # literal:0.33, literal:1.22, literal:27.38, literal:List, literal:Str, magic_number:0.33, magic_number:1.22, magic_number:27.38, node:List, node:Num, node:Str
            ["CNET", "CNET Networks, Inc.", 8.62, -0.13, -1.4901], # literal:-0.13, literal:-1.4901, literal:8.62, literal:List, literal:Str, magic_number:-0.13, magic_number:-1.4901, magic_number:8.62, node:List, node:Num, node:Str
        ]
    )
with open("stocks.csv", "r") as stocksFile: # argument:, external_free_call:open, free_call:open, literal:Str, node:Call, node:Name, node:Str, node:With (-> +5), node:withitem
    stocks = csv.reader(stocksFile) # argument:stocksFile, assignment:reader, assignment_lhs_identifier:stocks, assignment_rhs_atom:csv, assignment_rhs_atom:stocksFile, loaded_variable:csv, loaded_variable:stocksFile, member_call_method:reader, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:stocks
    status_labels = {-1: "down", 0: "unchanged", 1: "up"} # assignment, assignment_lhs_identifier:status_labels, assignment_rhs_atom:-1, assignment_rhs_atom:0, assignment_rhs_atom:1, literal:-1, literal:0, literal:1, literal:Dict, literal:Str, node:Assign, node:Dict, node:Name, node:Num, node:Str, single_assignment:status_labels
    for ticker, name, price, change, pct in stocks: # for:change (-> +2), for:name (-> +2), for:pct (-> +2), for:price (-> +2), for:ticker (-> +2), for_each:change (-> +2), for_each:name (-> +2), for_each:pct (-> +2), for_each:price (-> +2), for_each:ticker (-> +2), iteration_variable:change, iteration_variable:name, iteration_variable:pct, iteration_variable:price, iteration_variable:ticker, literal:Tuple, loaded_variable:stocks, loop:for (-> +2), loop_with_late_exit:for (-> +2), node:For (-> +2), node:Name, node:Tuple
        status = status_labels[cmp(float(change), 0.0)] # argument:, argument:0.0, argument:change, assignment, assignment_lhs_identifier:status, assignment_rhs_atom:0.0, assignment_rhs_atom:change, assignment_rhs_atom:status_labels, composition, external_free_call:float, free_call:cmp, free_call:float, index:_, internal_free_call:cmp, literal:0.0, loaded_variable:change, loaded_variable:status_labels, magic_number:0.0, node:Assign, node:Call, node:Name, node:Num, node:Subscript, single_assignment:status
        print("{} is {} ({:.2f})".format(name, status, float(pct))) # argument:, argument:name, argument:pct, argument:status, composition, external_free_call:float, external_free_call:print, free_call:float, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:name, loaded_variable:pct, loaded_variable:status, member_call_method:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 18_queens.py
# ----------------------------------------------------------------------------------------
BOARD_SIZE = 8 # assignment:8, assignment_lhs_identifier:BOARD_SIZE, assignment_rhs_atom:8, global_scope:BOARD_SIZE (-> +19), global_scope:answer (-> +19), literal:8, node:Assign, node:Name, node:Num, procedural_style (-> +19), scope:BOARD_SIZE (-> +19), scope:answer (-> +19), single_assignment:BOARD_SIZE, variety:5 (-> +19), whole_span:20 (-> +19)
def under_attack(col, queens): # function:under_attack (-> +6), function_line_count:7 (-> +6), function_parameter:col, function_parameter:queens, function_parameter_flavor:arg, function_returning_something:under_attack (-> +6), impure_function:under_attack (-> +6), local_scope:c (-> +6), local_scope:col (-> +6), local_scope:left (-> +6), local_scope:queens (-> +6), local_scope:r (-> +6), local_scope:right (-> +6), node:FunctionDef (-> +6), node:arg, scope:c (-> +6), scope:col (-> +6), scope:left (-> +6), scope:queens (-> +6), scope:r (-> +6), scope:right (-> +6)
    left = right = col # assignment, assignment_lhs_identifier:left, assignment_lhs_identifier:right, assignment_rhs_atom:col, chained_assignment, loaded_variable:col, node:Assign, node:Name
    for r, c in reversed(queens): # argument:queens, existential_quantification:c (-> +3), external_free_call:reversed, for:c (-> +3), for:r (-> +3), free_call:reversed, iteration_variable:c, iteration_variable:r, literal:Tuple, loaded_variable:queens, loop:for (-> +3), loop_with_early_exit:for:return (-> +3), loop_with_return:for (-> +3), node:Call, node:For (-> +3), node:Name, node:Tuple
        left, right = left - 1, right + 1 # addition_operator, assignment, assignment_lhs_identifier:left, assignment_lhs_identifier:right, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:Sub, literal:1, literal:Tuple, loaded_variable:left, loaded_variable:right, node:Assign, node:BinOp, node:Name, node:Num, node:Tuple, parallel_assignment:2, update:left:1, update:left:right, update:right:1, update:right:left, update_by_assignment:left:1, update_by_assignment:left:right, update_by_assignment:right:1, update_by_assignment:right:left, update_by_assignment_with, update_with
        if c in (left, col, right): # comparison_operator:In, if (-> +1), if_test_atom:c, if_test_atom:col, if_test_atom:left, if_test_atom:right, if_without_else (-> +1), literal:Tuple, loaded_variable:c, loaded_variable:col, loaded_variable:left, loaded_variable:right, node:Compare, node:If (-> +1), node:Name, node:Tuple
            return True # if_then_branch, literal:True, node:NameConstant, node:Return, return:True
    return False # literal:False, node:NameConstant, node:Return, return:False
def solve(n): # access_outer_scope:BOARD_SIZE (-> +8), body_recursive_function:solve (-> +8), function:solve (-> +8), function_line_count:9 (-> +8), function_parameter:n, function_parameter_flavor:arg, function_returning_something:solve (-> +8), impure_function:solve (-> +8), local_scope:n (-> +8), local_scope:smaller_solutions (-> +8), node:FunctionDef (-> +8), node:arg, recursive_call_count:1 (-> +8), recursive_function:solve (-> +8), scope:n (-> +8), scope:smaller_solutions (-> +8)
    if n == 0: # comparison_operator:Eq, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0, loaded_variable:n, node:Compare, node:If (-> +1), node:Name, node:Num
        return [[]] # empty_literal:List, if_then_branch, literal:List, node:List, node:Return, return
    smaller_solutions = solve(n - 1) # argument:, assignment:solve, assignment_lhs_identifier:smaller_solutions, assignment_rhs_atom:1, assignment_rhs_atom:n, binary_operator:Sub, free_call:solve, internal_free_call:solve, literal:1, loaded_variable:n, node:Assign, node:BinOp, node:Call, node:Name, node:Num, single_assignment:smaller_solutions
    return [ # comprehension:List, comprehension_for_count:2, local_scope:i, local_scope:solution, node:ListComp (-> +4), node:Return (-> +4), return (-> +4), scope:i, scope:solution
        solution + [(n, i + 1)] # binary_operator:Add, concatenation_operator:List, literal:1, literal:List, literal:Tuple, loaded_variable:i, loaded_variable:n, loaded_variable:solution, node:BinOp, node:List, node:Name, node:Num, node:Tuple
        for i in range(BOARD_SIZE) # argument:BOARD_SIZE, external_free_call:range, free_call:range, iteration_variable:i, loaded_variable:BOARD_SIZE, node:Call, node:Name, node:comprehension, range:BOARD_SIZE
        for solution in smaller_solutions # iteration_variable:solution, loaded_variable:smaller_solutions, node:Name, node:comprehension (-> +1)
        if not under_attack(i + 1, solution) # addition_operator, argument:, argument:solution, binary_operator:Add, filtered_comprehension, free_call:under_attack, internal_free_call:under_attack, literal:1, loaded_variable:i, loaded_variable:solution, node:BinOp, node:Call, node:Name, node:Num, node:UnaryOp, unary_operator:Not
    ]
for answer in solve(BOARD_SIZE): # argument:BOARD_SIZE, for:answer (-> +1), free_call:solve, internal_free_call:solve, iteration_variable:answer, loaded_variable:BOARD_SIZE, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:Call, node:For (-> +1), node:Name
    print(answer) # argument:answer, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:answer, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 20_prime_numbers.py
# ----------------------------------------------------------------------------------------
import itertools # global_scope:p (-> +10), import:itertools, import_module:itertools, node:Import, procedural_style (-> +10), scope:p (-> +10), variety:6 (-> +10), whole_span:11 (-> +10)
def iter_primes(): # function:iter_primes (-> +5), function_line_count:6 (-> +5), function_without_parameters:iter_primes (-> +5), generator:iter_primes (-> +5), local_scope:numbers (-> +5), local_scope:prime (-> +5), node:FunctionDef (-> +5), scope:numbers (-> +5), scope:prime (-> +5)
    numbers = itertools.count(2) # argument:2, assignment:count, assignment_lhs_identifier:numbers, assignment_rhs_atom:2, assignment_rhs_atom:itertools, literal:2, loaded_variable:itertools, member_call_method:count, node:Assign, node:Attribute, node:Call, node:Name, node:Num, single_assignment:numbers
    while True: # infinite_while (-> +3), literal:True, loop:while (-> +3), loop_with_late_exit:while (-> +3), node:NameConstant, node:While (-> +3)
        prime = next(numbers) # argument:numbers, assignment:next, assignment_lhs_identifier:prime, assignment_rhs_atom:numbers, external_free_call:next, free_call:next, loaded_variable:numbers, node:Assign, node:Call, node:Name, single_assignment:prime
        yield prime # loaded_variable:prime, node:Expr, node:Name, node:Yield, yield:prime
        numbers = filter(prime.__rmod__, numbers) # argument:, argument:numbers, assignment:filter, assignment_lhs_identifier:numbers, assignment_rhs_atom:numbers, assignment_rhs_atom:prime, external_free_call:filter, free_call:filter, loaded_variable:numbers, loaded_variable:prime, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:numbers, update:numbers:prime, update_by_assignment:numbers:prime, update_by_assignment_with:filter, update_with:filter
for p in iter_primes(): # for:p (-> +3), free_call:iter_primes, free_call_no_arguments:iter_primes, internal_free_call:iter_primes, iteration_variable:p, loop:for (-> +3), loop_with_break:for (-> +3), loop_with_early_exit:for:break (-> +3), node:Call, node:For (-> +3), node:Name
    if p > 1000: # comparison_operator:Gt, if (-> +1), if_test_atom:1000, if_test_atom:p, if_without_else (-> +1), literal:1000, loaded_variable:p, magic_number:1000, node:Compare, node:If (-> +1), node:Name, node:Num
        break # if_then_branch, node:Break
    print(p) # argument:p, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:p, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 21_xml_html_parsing.py
# ----------------------------------------------------------------------------------------
dinner_recipe = """<html><body><table> # assignment, assignment_lhs_identifier:dinner_recipe, global_scope:amt (-> +13), global_scope:dinner_recipe (-> +13), global_scope:ingredient (-> +13), global_scope:item (-> +13), global_scope:pantry (-> +13), global_scope:tree (-> +13), global_scope:unit (-> +13), imperative_style (-> +13), literal:Str, node:Assign, node:Name, node:Str, scope:amt (-> +13), scope:dinner_recipe (-> +13), scope:ingredient (-> +13), scope:item (-> +13), scope:pantry (-> +13), scope:tree (-> +13), scope:unit (-> +13), single_assignment:dinner_recipe, special_literal_string:<html><body><table>\n<tr><th>amt</th><th>unit</th><th>item</th></tr>\n<tr><td>24</td><td>slices</td><td>baguette</td></tr>\n<tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>\n<tr><td>1</td><td>cup</td><td>tomatoes</td></tr>\n<tr><td>1</td><td>jar</td><td>pesto</td></tr>\n</table></body></html>, variety:3 (-> +13), whole_span:14 (-> +13)
<tr><th>amt</th><th>unit</th><th>item</th></tr>
<tr><td>24</td><td>slices</td><td>baguette</td></tr>
<tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>
<tr><td>1</td><td>cup</td><td>tomatoes</td></tr>
<tr><td>1</td><td>jar</td><td>pesto</td></tr>
</table></body></html>"""
import xml.etree.ElementTree as etree # import:xml.etree.ElementTree, import_module:xml.etree.ElementTree, node:Import
tree = etree.fromstring(dinner_recipe) # argument:dinner_recipe, assignment:fromstring, assignment_lhs_identifier:tree, assignment_rhs_atom:dinner_recipe, assignment_rhs_atom:etree, loaded_variable:dinner_recipe, loaded_variable:etree, member_call_method:fromstring, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:tree
pantry = {"olive oil", "pesto"} # assignment, assignment_lhs_identifier:pantry, literal:Set, literal:Str, node:Assign, node:Name, node:Set, node:Str, single_assignment:pantry
for ingredient in tree.getiterator("tr"): # argument:, for:ingredient (-> +3), iteration_variable:ingredient, literal:Str, loaded_variable:tree, loop:for (-> +3), loop_with_late_exit:for (-> +3), member_call_method:getiterator, node:Attribute, node:Call, node:For (-> +3), node:Name, node:Str
    amt, unit, item = ingredient # assignment, assignment_lhs_identifier:amt, assignment_lhs_identifier:item, assignment_lhs_identifier:unit, assignment_rhs_atom:ingredient, literal:Tuple, loaded_variable:ingredient, node:Assign, node:Name, node:Tuple, parallel_assignment:3
    if item.tag == "td" and item.text not in pantry: # boolean_operator:And, comparison_operator:Eq, comparison_operator:NotIn, if (-> +1), if_test_atom:item, if_test_atom:pantry, if_without_else (-> +1), literal:Str, loaded_variable:item, loaded_variable:pantry, node:Attribute, node:BoolOp, node:Compare, node:If (-> +1), node:Name, node:Str
        print("{}: {} {}".format(item.text, amt.text, unit.text)) # argument:, composition, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, loaded_variable:amt, loaded_variable:item, loaded_variable:unit, member_call_method:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 28_queens.py
# ----------------------------------------------------------------------------------------
BOARD_SIZE = 8 # assignment:8, assignment_lhs_identifier:BOARD_SIZE, assignment_rhs_atom:8, global_scope:BOARD_SIZE (-> +23), global_scope:queens (-> +23), literal:8, node:Assign, node:Name, node:Num, object_oriented_style (-> +23), scope:BOARD_SIZE (-> +23), scope:queens (-> +23), single_assignment:BOARD_SIZE, variety:7 (-> +23), whole_span:24 (-> +23)
class BailOut(Exception): # class:BailOut (-> +1), loaded_variable:Exception, node:ClassDef (-> +1), node:Name
    pass # no_operation, node:Pass
def validate(queens): # function:validate (-> +5), function_line_count:6 (-> +5), function_parameter:queens, function_parameter_flavor:arg, function_returning_nothing:validate (-> +5), local_scope:col (-> +5), local_scope:left (-> +5), local_scope:queens (-> +5), local_scope:r (-> +5), local_scope:right (-> +5), node:FunctionDef (-> +5), node:arg, scope:col (-> +5), scope:left (-> +5), scope:queens (-> +5), scope:r (-> +5), scope:right (-> +5), shadowing_scope:queens (-> +5)
    left = right = col = queens[-1] # assignment, assignment_lhs_identifier:col, assignment_lhs_identifier:left, assignment_lhs_identifier:right, assignment_rhs_atom:-1, assignment_rhs_atom:queens, chained_assignment, index:-1, literal:-1, loaded_variable:queens, negative_index:-1, node:Assign, node:Name, node:Num, node:Subscript
    for r in reversed(queens[:-1]): # argument:, external_free_call:reversed, for:r (-> +3), free_call:reversed, iteration_variable:r, literal:-1, loaded_variable:queens, loop:for (-> +3), loop_with_early_exit:for:raise (-> +3), loop_with_raise:for (-> +3), node:Call, node:For (-> +3), node:Name, node:Num, node:Slice, node:Subscript, slice::-1:, slice_lower:, slice_step:, slice_upper:-1
        left, right = left - 1, right + 1 # addition_operator, assignment, assignment_lhs_identifier:left, assignment_lhs_identifier:right, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:Sub, literal:1, literal:Tuple, loaded_variable:left, loaded_variable:right, node:Assign, node:BinOp, node:Name, node:Num, node:Tuple, parallel_assignment:2, update:left:1, update:left:right, update:right:1, update:right:left, update_by_assignment:left:1, update_by_assignment:left:right, update_by_assignment:right:1, update_by_assignment:right:left, update_by_assignment_with, update_with
        if r in (left, col, right): # comparison_operator:In, if (-> +1), if_test_atom:col, if_test_atom:left, if_test_atom:r, if_test_atom:right, if_without_else (-> +1), literal:Tuple, loaded_variable:col, loaded_variable:left, loaded_variable:r, loaded_variable:right, node:Compare, node:If (-> +1), node:Name, node:Tuple
            raise BailOut # if_then_branch, loaded_variable:BailOut, node:Name, node:Raise, raise:BailOut
def add_queen(queens): # access_outer_scope:BOARD_SIZE (-> +11), function:add_queen (-> +11), function_line_count:12 (-> +11), function_parameter:queens, function_parameter_flavor:arg, function_returning_something:add_queen (-> +11), impure_function:add_queen (-> +11), local_scope:i (-> +11), local_scope:queens (-> +11), local_scope:test_queens (-> +11), node:FunctionDef (-> +11), node:arg, recursive_call_count:1 (-> +11), recursive_function:add_queen (-> +11), scope:i (-> +11), scope:queens (-> +11), scope:test_queens (-> +11), shadowing_scope:queens (-> +11), tail_recursive_function:add_queen (-> +11)
    for i in range(BOARD_SIZE): # argument:BOARD_SIZE, external_free_call:range, for:i (-> +9), for_range:BOARD_SIZE (-> +9), free_call:range, iteration_variable:i, loaded_variable:BOARD_SIZE, loop:for (-> +9), loop_with_early_exit:for:return (-> +9), loop_with_return:for (-> +9), node:Call, node:For (-> +9), node:Name, range:BOARD_SIZE
        test_queens = queens + [i] # assignment:Add, assignment_lhs_identifier:test_queens, assignment_rhs_atom:i, assignment_rhs_atom:queens, binary_operator:Add, concatenation_operator:List, literal:List, loaded_variable:i, loaded_variable:queens, node:Assign, node:BinOp, node:List, node:Name, single_assignment:test_queens
        try: # node:Try (-> +7), try_except:BailOut (-> +7)
            validate(test_queens) # argument:test_queens, free_call:validate, free_call_without_result:validate, internal_free_call:validate, loaded_variable:test_queens, node:Call, node:Expr, node:Name
            if len(test_queens) == BOARD_SIZE: # argument:test_queens, comparison_operator:Eq, external_free_call:len, free_call:len, if (-> +3), if_test_atom:BOARD_SIZE, if_test_atom:test_queens, loaded_variable:BOARD_SIZE, loaded_variable:test_queens, node:Call, node:Compare, node:If (-> +3), node:Name
                return test_queens # if_then_branch, loaded_variable:test_queens, node:Name, node:Return, return:test_queens
            else:
                return add_queen(test_queens) # argument:test_queens, free_call:add_queen, free_tail_call:add_queen, if_else_branch, internal_free_call:add_queen, loaded_variable:test_queens, node:Call, node:Name, node:Return, return
        except BailOut: # except:BailOut, loaded_variable:BailOut, node:ExceptHandler (-> +1), node:Name
            pass # no_operation, node:Pass
    raise BailOut # loaded_variable:BailOut, node:Name, node:Raise, raise:BailOut
queens = add_queen([]) # argument:, assignment:add_queen, assignment_lhs_identifier:queens, empty_literal:List, free_call:add_queen, internal_free_call:add_queen, literal:List, node:Assign, node:Call, node:List, node:Name, single_assignment:queens
print(queens) # argument:queens, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:queens, node:Call, node:Expr, node:Name
print("\n".join(". " * q + "Q " + ". " * (BOARD_SIZE - q - 1) for q in queens)) # argument:, binary_operator:Add, binary_operator:Mult, binary_operator:Sub, composition, comprehension:Generator, comprehension_for_count:1, concatenation_operator:Str, external_free_call:print, free_call:print, free_call_without_result:print, iteration_variable:q, literal:1, literal:Str, loaded_variable:BOARD_SIZE, loaded_variable:q, loaded_variable:queens, local_scope:q, member_call_method:join, node:Attribute, node:BinOp, node:Call, node:Expr, node:GeneratorExp, node:Name, node:Num, node:Str, node:comprehension, replication_operator:Str, scope:q, special_literal_string:\n

# ----------------------------------------------------------------------------------------
# 33_guess_the_number.py
# ----------------------------------------------------------------------------------------
import random # global_scope:guess (-> +17), global_scope:guesses_made (-> +17), global_scope:name (-> +17), global_scope:number (-> +17), imperative_style (-> +17), import:random, import_module:random, node:Import, scope:guess (-> +17), scope:guesses_made (-> +17), scope:name (-> +17), scope:number (-> +17), variety:4 (-> +17), whole_span:18 (-> +17)
guesses_made = 0 # assignment:0, assignment_lhs_identifier:guesses_made, assignment_rhs_atom:0, literal:0, node:Assign, node:Name, node:Num, single_assignment:guesses_made
name = input("Hello! What is your name?\n") # argument:, assignment:input, assignment_lhs_identifier:name, external_free_call:input, free_call:input, literal:Str, node:Assign, node:Call, node:Name, node:Str, single_assignment:name, special_literal_string:Hello! What is your name?\n
number = random.randint(1, 20) # argument:1, argument:20, assignment:randint, assignment_lhs_identifier:number, assignment_rhs_atom:1, assignment_rhs_atom:20, assignment_rhs_atom:random, literal:1, literal:20, loaded_variable:random, magic_number:20, member_call_method:randint, node:Assign, node:Attribute, node:Call, node:Name, node:Num, single_assignment:number
print("Well, {}, I am thinking of a number between 1 and 20.".format(name)) # argument:, argument:name, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:name, member_call_method:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str
while guesses_made < 6: # comparison_operator:Lt, count_states:guesses_made (-> +8), literal:6, loaded_variable:guesses_made, loop:while (-> +8), loop_with_break:while (-> +8), loop_with_early_exit:while:break (-> +8), magic_number:6, node:Compare, node:Name, node:Num, node:While (-> +8)
    guess = int(input("Take a guess: ")) # argument:, assignment:int, assignment_lhs_identifier:guess, composition, external_free_call:input, external_free_call:int, free_call:input, free_call:int, literal:Str, node:Assign, node:Call, node:Name, node:Str, single_assignment:guess
    guesses_made += 1 # assignment_lhs_identifier:guesses_made, assignment_rhs_atom:1, augmented_assignment:Add, increment:guesses_made, literal:1, node:AugAssign, node:Name, node:Num, update:guesses_made:1, update_by_augmented_assignment:guesses_made:1, update_by_augmented_assignment_with:Add, update_with:Add
    if guess < number: # comparison_operator:Lt, if (-> +1), if_test_atom:guess, if_test_atom:number, if_without_else (-> +1), loaded_variable:guess, loaded_variable:number, node:Compare, node:If (-> +1), node:Name
        print("Your guess is too low.") # argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, node:Call, node:Expr, node:Name, node:Str
    if guess > number: # comparison_operator:Gt, if (-> +1), if_test_atom:guess, if_test_atom:number, if_without_else (-> +1), loaded_variable:guess, loaded_variable:number, node:Compare, node:If (-> +1), node:Name
        print("Your guess is too high.") # argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, node:Call, node:Expr, node:Name, node:Str
    if guess == number: # comparison_operator:Eq, if (-> +1), if_test_atom:guess, if_test_atom:number, if_without_else (-> +1), loaded_variable:guess, loaded_variable:number, node:Compare, node:If (-> +1), node:Name
        break # if_then_branch, node:Break
if guess == number: # comparison_operator:Eq, if (-> +3), if_test_atom:guess, if_test_atom:number, loaded_variable:guess, loaded_variable:number, node:Compare, node:If (-> +3), node:Name
    print("Good job, {}! You guessed my number in {} guesses!".format(name, guesses_made)) # argument:, argument:guesses_made, argument:name, composition, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, loaded_variable:guesses_made, loaded_variable:name, member_call_method:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str
else:
    print("Nope. The number I was thinking of was {}".format(number)) # argument:, argument:number, composition, external_free_call:print, free_call:print, free_call_without_result:print, if_else_branch, literal:Str, loaded_variable:number, member_call_method:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str
