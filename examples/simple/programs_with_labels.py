# ----------------------------------------------------------------------------------------
# 01_hello_world.py
# ----------------------------------------------------------------------------------------
print("Hello, world!") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:Call, node:Expr, node:Name, node:Str, whole_span:1

# ----------------------------------------------------------------------------------------
# 02_input_ name.py
# ----------------------------------------------------------------------------------------
name = input("What is your name?\n") # assignment:input, assignment_lhs_identifier:name, call_argument:, external_free_call:input, free_call:input, literal:Str, node:Assign, node:Call, node:Name, node:Str, single_assignment:name, whole_span:2 (-> +1)
print("Hi, %s." % name) # binary_operator:Mod, call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:BinOp, node:Call, node:Expr, node:Name, node:Str, string_formatting_operator

# ----------------------------------------------------------------------------------------
# 03_friends.py
# ----------------------------------------------------------------------------------------
friends = ["john", "pat", "gary", "michael"] # assignment, assignment_lhs_identifier:friends, literal:List, literal:Str, node:Assign, node:List, node:Name, node:Str, single_assignment:friends, whole_span:3 (-> +2)
for i, name in enumerate(friends): # call_argument:friends, external_free_call:enumerate, for:i (-> +1), for:name (-> +1), for_indexes_elements (-> +1), free_call:enumerate, literal:Tuple, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:Call, node:For (-> +1), node:Name, node:Tuple
    print("iteration {iteration} is {name}".format(iteration=i, name=name)) # call_argument:, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, member_call:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 04_fibonacci.py
# ----------------------------------------------------------------------------------------
parents, babies = (1, 1) # assignment, assignment_lhs_identifier:babies, assignment_lhs_identifier:parents, assignment_rhs_atom:1, literal:1, literal:Tuple, node:Assign, node:Name, node:Num, node:Tuple, parallel_assignment:2, whole_span:4 (-> +3)
while babies < 100: # comparison_operator:Lt, literal:100, loop:while (-> +2), loop_with_late_exit:while (-> +2), node:Compare, node:Name, node:Num, node:While (-> +2)
    print("This generation has {} babies".format(babies)) # call_argument:, call_argument:babies, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, member_call:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str
    parents, babies = (babies, parents + babies) # addition_operator, assignment, assignment_lhs_identifier:babies, assignment_lhs_identifier:parents, assignment_rhs_atom:babies, assignment_rhs_atom:parents, binary_operator:Add, literal:Tuple, node:Assign, node:BinOp, node:Name, node:Tuple, parallel_assignment:2, slide, update:babies:parents, update:parents:babies, update_by_assignment:babies:parents, update_by_assignment:parents:babies, update_by_assignment_with, update_with

# ----------------------------------------------------------------------------------------
# 05_greet.py
# ----------------------------------------------------------------------------------------
def greet(name): # function:greet (-> +1), function_argument:name, function_argument_flavor:arg, function_returning_nothing:greet (-> +1), node:FunctionDef (-> +1), node:arg, whole_span:5 (-> +4)
    print("Hello", name) # call_argument:, call_argument:name, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:Call, node:Expr, node:Name, node:Str
greet("Jack") # call_argument:, free_call:greet, free_call_without_result:greet, internal_free_call:greet, literal:Str, node:Call, node:Expr, node:Name, node:Str
greet("Jill") # call_argument:, free_call:greet, free_call_without_result:greet, internal_free_call:greet, literal:Str, node:Call, node:Expr, node:Name, node:Str
greet("Bob") # call_argument:, free_call:greet, free_call_without_result:greet, internal_free_call:greet, literal:Str, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 06_regex.py
# ----------------------------------------------------------------------------------------
import re # import:re, import_module:re, node:Import, whole_span:6 (-> +5)
for test_string in ["555-1212", "ILL-EGAL"]: # for:test_string (-> +4), literal:List, literal:Str, loop:for (-> +4), loop_with_late_exit:for (-> +4), node:For (-> +4), node:List, node:Name, node:Str
    if re.match(r"^\d{3}-\d{4}$", test_string): # call_argument:, call_argument:test_string, if (-> +3), if_test_atom:re, if_test_atom:test_string, literal:Str, member_call:match, node:Attribute, node:Call, node:If (-> +3), node:Name, node:Str
        print(test_string, "is a valid US local phone number") # call_argument:, call_argument:test_string, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, node:Call, node:Expr, node:Name, node:Str
    else:
        print(test_string, "rejected") # call_argument:, call_argument:test_string, external_free_call:print, free_call:print, free_call_without_result:print, if_else_branch, literal:Str, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 07_grocery_bill.py
# ----------------------------------------------------------------------------------------
prices = {"apple": 0.40, "banana": 0.50} # assignment, assignment_lhs_identifier:prices, assignment_rhs_atom:0.4, assignment_rhs_atom:0.5, literal:0.4, literal:0.5, literal:Dict, literal:Str, node:Assign, node:Dict, node:Name, node:Num, node:Str, single_assignment:prices, whole_span:4 (-> +3)
my_purchase = {"apple": 1, "banana": 6} # assignment, assignment_lhs_identifier:my_purchase, assignment_rhs_atom:1, assignment_rhs_atom:6, literal:1, literal:6, literal:Dict, literal:Str, node:Assign, node:Dict, node:Name, node:Num, node:Str, single_assignment:my_purchase
grocery_bill = sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase) # assignment:sum, assignment_lhs_identifier:grocery_bill, assignment_rhs_atom:fruit, assignment_rhs_atom:my_purchase, assignment_rhs_atom:prices, binary_operator:Mult, call_argument:, comprehension:Generator, comprehension_for_count:1, external_free_call:sum, free_call:sum, index:fruit, multiplication_operator, node:Assign, node:BinOp, node:Call, node:GeneratorExp, node:Name, node:Subscript, single_assignment:grocery_bill
print("I owe the grocer $%.2f" % grocery_bill) # binary_operator:Mod, call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:BinOp, node:Call, node:Expr, node:Name, node:Str, string_formatting_operator

# ----------------------------------------------------------------------------------------
# 08_arguments.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, node:Import, whole_span:6 (-> +5)
try: # node:Try (-> +4), try_except:ValueError (-> +4)
    total = sum(int(arg) for arg in sys.argv[1:]) # assignment:sum, assignment_lhs_identifier:total, assignment_rhs_atom:1, assignment_rhs_atom:arg, assignment_rhs_atom:sys, call_argument:, call_argument:arg, composition, comprehension:Generator, comprehension_for_count:1, external_free_call:int, external_free_call:sum, free_call:int, free_call:sum, literal:1, node:Assign, node:Attribute, node:Call, node:GeneratorExp, node:Name, node:Num, node:Subscript, single_assignment:total, slice:1::, slice_lower:1, slice_step:, slice_upper:
    print("sum =", total) # call_argument:, call_argument:total, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:Call, node:Expr, node:Name, node:Str
except ValueError: # except:ValueError, node:ExceptHandler (-> +1), node:Name
    print("Please supply integer arguments") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 09_indent.py
# ----------------------------------------------------------------------------------------
import glob # import:glob, import_module:glob, node:Import, whole_span:8 (-> +7)
python_files = glob.glob("*.py") # assignment:glob, assignment_lhs_identifier:python_files, assignment_rhs_atom:glob, call_argument:, literal:Str, member_call:glob, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:python_files
for file_name in sorted(python_files): # call_argument:python_files, external_free_call:sorted, for:file_name (-> +5), free_call:sorted, loop:for (-> +5), loop_with_late_exit:for (-> +5), node:Call, node:For (-> +5), node:Name
    print("    ------" + file_name) # binary_operator:Add, call_argument:, concatenation_operator:Str, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:BinOp, node:Call, node:Expr, node:Name, node:Str
    with open(file_name) as f: # call_argument:file_name, external_free_call:open, free_call:open, node:Call, node:Name, node:With (-> +2)
        for line in f: # for:line (-> +1), for_each (-> +1), loop:for (-> +1), loop_with_late_exit:for (-> +1), nested_for:1 (-> +1), node:For (-> +1), node:Name
            print("    " + line.rstrip()) # binary_operator:Add, call_argument:, composition, concatenation_operator:Str, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, member_call:rstrip, node:Attribute, node:BinOp, node:Call, node:Expr, node:Name, node:Str
    print() # external_free_call:print, free_call:print, free_call_without_arguments:print, free_call_without_result:print, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 10_time.py
# ----------------------------------------------------------------------------------------
from time import localtime # import:time:localtime, import_module:time, import_name:localtime, node:ImportFrom, whole_span:17 (-> +16)
activities = { # assignment, assignment_lhs_identifier:activities, literal:Dict, node:Assign (-> +6), node:Dict (-> +6), node:Name, single_assignment:activities
    8: "Sleeping", # assignment_rhs_atom:8, literal:8, literal:Str, node:Num, node:Str
    9: "Commuting", # assignment_rhs_atom:9, literal:9, literal:Str, node:Num, node:Str
    17: "Working", # assignment_rhs_atom:17, literal:17, literal:Str, node:Num, node:Str
    18: "Commuting", # assignment_rhs_atom:18, literal:18, literal:Str, node:Num, node:Str
    20: "Eating", # assignment_rhs_atom:20, literal:20, literal:Str, node:Num, node:Str
    22: "Resting", # assignment_rhs_atom:22, literal:22, literal:Str, node:Num, node:Str
}
time_now = localtime() # assignment:localtime, assignment_lhs_identifier:time_now, external_free_call:localtime, free_call:localtime, free_call_without_arguments:localtime, node:Assign, node:Call, node:Name, single_assignment:time_now
hour = time_now.tm_hour # assignment, assignment_lhs_identifier:hour, assignment_rhs_atom:time_now, node:Assign, node:Attribute, node:Name, single_assignment:hour
for activity_time in sorted(activities.keys()): # call_argument:, composition, external_free_call:sorted, for:activity_time (-> +5), free_call:sorted, loop:for (-> +5), loop_with_break:for (-> +5), loop_with_early_exit:for:break (-> +5), loop_with_else:for (-> +5), member_call:keys, node:Attribute, node:Call, node:For (-> +5), node:Name
    if hour < activity_time: # comparison_operator:Lt, if (-> +2), if_test_atom:activity_time, if_test_atom:hour, if_without_else (-> +2), node:Compare, node:If (-> +2), node:Name
        print(activities[activity_time]) # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch (-> +1), index:activity_time, node:Call, node:Expr, node:Name, node:Subscript
        break # node:Break
else:
    print("Unknown, AFK or sleeping!") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loop_else, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 11_bottles.py
# ----------------------------------------------------------------------------------------
REFRAIN = """ # assignment, assignment_lhs_identifier:REFRAIN, node:Assign (-> +5), node:Name, single_assignment:REFRAIN, whole_span:10 (-> +9)
%d bottles of beer on the wall,
%d bottles of beer,
take one down, pass it around,
%d bottles of beer on the wall!
""" # literal:Str, node:Str
bottles_of_beer = 9 # assignment:9, assignment_lhs_identifier:bottles_of_beer, assignment_rhs_atom:9, literal:9, node:Assign, node:Name, node:Num, single_assignment:bottles_of_beer, suggest_constant_definition
while bottles_of_beer > 1: # comparison_operator:Gt, literal:1, loop:while (-> +2), loop_with_late_exit:while (-> +2), node:Compare, node:Name, node:Num, node:While (-> +2)
    print(REFRAIN % (bottles_of_beer, bottles_of_beer, bottles_of_beer - 1)) # binary_operator:Mod, binary_operator:Sub, call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:1, literal:Tuple, modulo_operator, node:BinOp, node:Call, node:Expr, node:Name, node:Num, node:Tuple
    bottles_of_beer -= 1 # assignment_lhs_identifier:bottles_of_beer, assignment_rhs_atom:1, augmented_assignment:Sub, literal:1, node:AugAssign, node:Name, node:Num, update:bottles_of_beer:1, update_by_augmented_assignment:bottles_of_beer:1, update_by_augmented_assignment_with:Sub, update_with:Sub

# ----------------------------------------------------------------------------------------
# 12_classes.py
# ----------------------------------------------------------------------------------------
class BankAccount(object): # class:BankAccount (-> +8), node:ClassDef (-> +8), node:Name, whole_span:12 (-> +11)
    def __init__(self, initial_balance=0): # function:__init__ (-> +1), function_argument:initial_balance, function_argument:self, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +1), instance_method:__init__ (-> +1), literal:0, method:__init__ (-> +1), node:FunctionDef (-> +1), node:Num, node:arg
        self.balance = initial_balance # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:initial_balance, node:Assign, node:Attribute, node:Name
    def deposit(self, amount): # function:deposit (-> +1), function_argument:amount, function_argument:self, function_argument_flavor:arg, function_returning_nothing:deposit (-> +1), instance_method:deposit (-> +1), method:deposit (-> +1), node:FunctionDef (-> +1), node:arg
        self.balance += amount # assignment_lhs_identifier:self, assignment_rhs_atom:amount, augmented_assignment:Add, node:Attribute, node:AugAssign, node:Name, update:self:amount, update_by_augmented_assignment:self:amount, update_by_augmented_assignment_with:Add, update_with:Add
    def withdraw(self, amount): # function:withdraw (-> +1), function_argument:amount, function_argument:self, function_argument_flavor:arg, function_returning_nothing:withdraw (-> +1), instance_method:withdraw (-> +1), method:withdraw (-> +1), node:FunctionDef (-> +1), node:arg
        self.balance -= amount # assignment_lhs_identifier:self, assignment_rhs_atom:amount, augmented_assignment:Sub, node:Attribute, node:AugAssign, node:Name, update:self:amount, update_by_augmented_assignment:self:amount, update_by_augmented_assignment_with:Sub, update_with:Sub
    def overdrawn(self): # function:overdrawn (-> +1), function_argument:self, function_argument_flavor:arg, function_returning_something:overdrawn (-> +1), instance_method:overdrawn (-> +1), method:overdrawn (-> +1), node:FunctionDef (-> +1), node:arg
        return self.balance < 0 # comparison_operator:Lt, literal:0, node:Attribute, node:Compare, node:Name, node:Num, node:Return, return
my_account = BankAccount(15) # assignment:BankAccount, assignment_lhs_identifier:my_account, assignment_rhs_atom:15, call_argument:15, external_free_call:BankAccount, free_call:BankAccount, literal:15, node:Assign, node:Call, node:Name, node:Num, single_assignment:my_account
my_account.withdraw(50) # call_argument:50, literal:50, member_call:withdraw, member_call_object:my_account, member_call_without_result:withdraw, node:Attribute, node:Call, node:Expr, node:Name, node:Num
print(my_account.balance, my_account.overdrawn()) # call_argument:, composition, external_free_call:print, free_call:print, free_call_without_result:print, member_call:overdrawn, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 13_unit_testing.py
# ----------------------------------------------------------------------------------------
import unittest # import:unittest, import_module:unittest, node:Import, whole_span:11 (-> +10)
def median(pool): # function:median (-> +6), function_argument:pool, function_argument_flavor:arg, function_returning_something:median (-> +6), node:FunctionDef (-> +6), node:arg
    copy = sorted(pool) # assignment:sorted, assignment_lhs_identifier:copy, assignment_rhs_atom:pool, call_argument:pool, external_free_call:sorted, free_call:sorted, node:Assign, node:Call, node:Name, single_assignment:copy
    size = len(copy) # assignment:len, assignment_lhs_identifier:size, assignment_rhs_atom:copy, call_argument:copy, external_free_call:len, free_call:len, node:Assign, node:Call, node:Name, single_assignment:size
    if size % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:1, if_test_atom:2, if_test_atom:size, literal:1, literal:2, modulo_operator, node:BinOp, node:Compare, node:If (-> +3), node:Name, node:Num
        return copy[int((size - 1) / 2)] # binary_operator:Div, binary_operator:Sub, call_argument:, external_free_call:int, free_call:int, if_then_branch, index:_, literal:1, literal:2, node:BinOp, node:Call, node:Name, node:Num, node:Return, node:Subscript, return
    else:
        return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2 # addition_operator, binary_operator:Add, binary_operator:Div, binary_operator:Sub, call_argument:, external_free_call:int, free_call:int, if_else_branch, index:_, literal:1, literal:2, node:BinOp, node:Call, node:Name, node:Num, node:Return, node:Subscript, return
class TestMedian(unittest.TestCase): # class:TestMedian (-> +2), node:Attribute, node:ClassDef (-> +2), node:Name
    def testMedian(self): # function:testMedian (-> +1), function_argument:self, function_argument_flavor:arg, function_returning_nothing:testMedian (-> +1), instance_method:testMedian (-> +1), method:testMedian (-> +1), node:FunctionDef (-> +1), node:arg
        self.assertEqual(median([2, 9, 9, 7, 9, 2, 4, 5, 8]), 7) # call_argument:, call_argument:7, composition, free_call:median, internal_free_call:median, literal:2, literal:4, literal:5, literal:7, literal:8, literal:9, literal:List, member_call:assertEqual, member_call_object:self, member_call_without_result:assertEqual, node:Attribute, node:Call, node:Expr, node:List, node:Name, node:Num, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# 14_median.py
# ----------------------------------------------------------------------------------------
def median(pool): # function:median (-> +6), function_argument:pool, function_argument_flavor:arg, function_returning_something:median (-> +6), node:FunctionDef (-> +6), node:arg, whole_span:7 (-> +6)
    copy = sorted(pool) # assignment:sorted, assignment_lhs_identifier:copy, assignment_rhs_atom:pool, call_argument:pool, external_free_call:sorted, free_call:sorted, node:Assign, node:Call, node:Name, single_assignment:copy
    size = len(copy) # assignment:len, assignment_lhs_identifier:size, assignment_rhs_atom:copy, call_argument:copy, external_free_call:len, free_call:len, node:Assign, node:Call, node:Name, single_assignment:size
    if size % 2 == 1: # binary_operator:Mod, comparison_operator:Eq, divisibility_test:2, if (-> +3), if_test_atom:1, if_test_atom:2, if_test_atom:size, literal:1, literal:2, modulo_operator, node:BinOp, node:Compare, node:If (-> +3), node:Name, node:Num
        return copy[int((size - 1) / 2)] # binary_operator:Div, binary_operator:Sub, call_argument:, external_free_call:int, free_call:int, if_then_branch, index:_, literal:1, literal:2, node:BinOp, node:Call, node:Name, node:Num, node:Return, node:Subscript, return
    else:
        return (copy[int(size / 2 - 1)] + copy[int(size / 2)]) / 2 # addition_operator, binary_operator:Add, binary_operator:Div, binary_operator:Sub, call_argument:, external_free_call:int, free_call:int, if_else_branch, index:_, literal:1, literal:2, node:BinOp, node:Call, node:Name, node:Num, node:Return, node:Subscript, return

# ----------------------------------------------------------------------------------------
# 15_itertools_groupby.py
# ----------------------------------------------------------------------------------------
from itertools import groupby # import:itertools:groupby, import_module:itertools, import_name:groupby, node:ImportFrom, whole_span:9 (-> +8)
lines = """ # assignment:splitlines, assignment_lhs_identifier:lines, node:Assign (-> +4), node:Name, single_assignment:lines
This is the
first paragraph.
This is the second.
""".splitlines() # literal:Str, member_call:splitlines, node:Attribute, node:Call, node:Str
for has_chars, frags in groupby(lines, bool): # call_argument:bool, call_argument:lines, external_free_call:groupby, for:frags (-> +2), for:has_chars (-> +2), free_call:groupby, literal:Tuple, loop:for (-> +2), loop_with_late_exit:for (-> +2), node:Call, node:For (-> +2), node:Name, node:Tuple
    if has_chars: # if (-> +1), if_without_else (-> +1), node:If (-> +1), node:Name
        print(" ".join(frags)) # call_argument:, call_argument:frags, composition, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, member_call:join, node:Attribute, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 16_csv.py
# ----------------------------------------------------------------------------------------
import csv # import:csv, import_module:csv, node:Import, whole_span:18 (-> +17)
def cmp(a, b): # function:cmp (-> +1), function_argument:a, function_argument:b, function_argument_flavor:arg, function_returning_something:cmp (-> +1), node:FunctionDef (-> +1), node:arg
    return (a > b) - (a < b) # binary_operator:Sub, comparison_operator:Gt, comparison_operator:Lt, node:BinOp, node:Compare, node:Name, node:Return, return
with open("stocks.csv", "w", newline="") as stocksFileW: # call_argument:, empty_literal:Str, external_free_call:open, free_call:open, literal:Str, node:Call, node:Name, node:Str, node:With (-> +6)
    writer = csv.writer(stocksFileW) # assignment:writer, assignment_lhs_identifier:writer, assignment_rhs_atom:csv, assignment_rhs_atom:stocksFileW, call_argument:stocksFileW, member_call:writer, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:writer
    writer.writerows( # member_call:writerows, member_call_object:writer, member_call_without_result:writerows, node:Attribute, node:Call (-> +4), node:Expr (-> +4), node:Name
        [ # call_argument:, literal:List, node:List (-> +3)
            ["GOOG", "Google, Inc.", 505.24, 0.47, 0.09], # literal:0.09, literal:0.47, literal:505.24, literal:List, literal:Str, node:List, node:Num, node:Str, suggest_constant_definition
            ["YHOO", "Yahoo! Inc.", 27.38, 0.33, 1.22], # literal:0.33, literal:1.22, literal:27.38, literal:List, literal:Str, node:List, node:Num, node:Str, suggest_constant_definition
            ["CNET", "CNET Networks, Inc.", 8.62, -0.13, -1.4901], # literal:-0.13, literal:-1.4901, literal:8.62, literal:List, literal:Str, node:List, node:Num, node:Str, suggest_constant_definition
        ]
    )
with open("stocks.csv", "r") as stocksFile: # call_argument:, external_free_call:open, free_call:open, literal:Str, node:Call, node:Name, node:Str, node:With (-> +5)
    stocks = csv.reader(stocksFile) # assignment:reader, assignment_lhs_identifier:stocks, assignment_rhs_atom:csv, assignment_rhs_atom:stocksFile, call_argument:stocksFile, member_call:reader, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:stocks
    status_labels = {-1: "down", 0: "unchanged", 1: "up"} # assignment, assignment_lhs_identifier:status_labels, assignment_rhs_atom:-1, assignment_rhs_atom:0, assignment_rhs_atom:1, literal:-1, literal:0, literal:1, literal:Dict, literal:Str, node:Assign, node:Dict, node:Name, node:Num, node:Str, single_assignment:status_labels
    for ticker, name, price, change, pct in stocks: # for:change (-> +2), for:name (-> +2), for:pct (-> +2), for:price (-> +2), for:ticker (-> +2), for_each (-> +2), literal:Tuple, loop:for (-> +2), loop_with_late_exit:for (-> +2), node:For (-> +2), node:Name, node:Tuple
        status = status_labels[cmp(float(change), 0.0)] # assignment, assignment_lhs_identifier:status, assignment_rhs_atom:0.0, assignment_rhs_atom:change, assignment_rhs_atom:status_labels, call_argument:, call_argument:0.0, call_argument:change, composition, external_free_call:float, free_call:cmp, free_call:float, index:_, internal_free_call:cmp, literal:0.0, node:Assign, node:Call, node:Name, node:Num, node:Subscript, single_assignment:status, suggest_constant_definition
        print("{} is {} ({:.2f})".format(name, status, float(pct))) # call_argument:, call_argument:name, call_argument:pct, call_argument:status, composition, external_free_call:float, external_free_call:print, free_call:float, free_call:print, free_call_without_result:print, literal:Str, member_call:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 18_queens.py
# ----------------------------------------------------------------------------------------
BOARD_SIZE = 8 # assignment:8, assignment_lhs_identifier:BOARD_SIZE, assignment_rhs_atom:8, literal:8, node:Assign, node:Name, node:Num, single_assignment:BOARD_SIZE, whole_span:20 (-> +19)
def under_attack(col, queens): # function:under_attack (-> +6), function_argument:col, function_argument:queens, function_argument_flavor:arg, function_returning_something:under_attack (-> +6), node:FunctionDef (-> +6), node:arg
    left = right = col # assignment, assignment_lhs_identifier:left, assignment_lhs_identifier:right, assignment_rhs_atom:col, chained_assignment, node:Assign, node:Name
    for r, c in reversed(queens): # call_argument:queens, existential_quantification:c (-> +3), external_free_call:reversed, for:c (-> +3), for:r (-> +3), free_call:reversed, literal:Tuple, loop:for (-> +3), loop_with_early_exit:for:return (-> +3), loop_with_return:for (-> +3), node:Call, node:For (-> +3), node:Name, node:Tuple
        left, right = left - 1, right + 1 # addition_operator, assignment, assignment_lhs_identifier:left, assignment_lhs_identifier:right, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:Sub, literal:1, literal:Tuple, node:Assign, node:BinOp, node:Name, node:Num, node:Tuple, parallel_assignment:2, update:left:1, update:left:right, update:right:1, update:right:left, update_by_assignment:left:1, update_by_assignment:left:right, update_by_assignment:right:1, update_by_assignment:right:left, update_by_assignment_with, update_with
        if c in (left, col, right): # comparison_operator:In, if (-> +1), if_test_atom:c, if_test_atom:col, if_test_atom:left, if_test_atom:right, if_without_else (-> +1), literal:Tuple, node:Compare, node:If (-> +1), node:Name, node:Tuple
            return True # if_then_branch, literal:True, node:NameConstant, node:Return, return:True
    return False # literal:False, node:NameConstant, node:Return, return:False
def solve(n): # body_recursive_function:solve (-> +8), function:solve (-> +8), function_argument:n, function_argument_flavor:arg, function_returning_something:solve (-> +8), node:FunctionDef (-> +8), node:arg, recursive_function:solve (-> +8)
    if n == 0: # comparison_operator:Eq, if (-> +1), if_guard (-> +1), if_test_atom:0, if_test_atom:n, if_without_else (-> +1), literal:0, node:Compare, node:If (-> +1), node:Name, node:Num
        return [[]] # empty_literal:List, if_then_branch, literal:List, node:List, node:Return, return
    smaller_solutions = solve(n - 1) # assignment:solve, assignment_lhs_identifier:smaller_solutions, assignment_rhs_atom:1, assignment_rhs_atom:n, binary_operator:Sub, call_argument:, free_call:solve, internal_free_call:solve, literal:1, node:Assign, node:BinOp, node:Call, node:Name, node:Num, single_assignment:smaller_solutions
    return [ # node:Return (-> +4), return
        solution + [(n, i + 1)] # binary_operator:Add, comprehension:List, comprehension_for_count:2, concatenation_operator:List, literal:1, literal:List, literal:Tuple, node:BinOp, node:List, node:ListComp (-> +3), node:Name, node:Num, node:Tuple
        for i in range(BOARD_SIZE) # call_argument:BOARD_SIZE, external_free_call:range, free_call:range, node:Call, node:Name, range:BOARD_SIZE
        for solution in smaller_solutions # node:Name
        if not under_attack(i + 1, solution) # addition_operator, binary_operator:Add, call_argument:, call_argument:solution, filtered_comprehension, free_call:under_attack, internal_free_call:under_attack, literal:1, node:BinOp, node:Call, node:Name, node:Num, node:UnaryOp, unary_operator:Not
    ]
for answer in solve(BOARD_SIZE): # call_argument:BOARD_SIZE, for:answer (-> +1), free_call:solve, internal_free_call:solve, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:Call, node:For (-> +1), node:Name
    print(answer) # call_argument:answer, external_free_call:print, free_call:print, free_call_without_result:print, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 20_prime_numbers.py
# ----------------------------------------------------------------------------------------
import itertools # import:itertools, import_module:itertools, node:Import, whole_span:11 (-> +10)
def iter_primes(): # function:iter_primes (-> +5), function_without_arguments:iter_primes (-> +5), generator:iter_primes (-> +5), node:FunctionDef (-> +5)
    numbers = itertools.count(2) # assignment:count, assignment_lhs_identifier:numbers, assignment_rhs_atom:2, assignment_rhs_atom:itertools, call_argument:2, literal:2, member_call:count, node:Assign, node:Attribute, node:Call, node:Name, node:Num, single_assignment:numbers
    while True: # infinite_while (-> +3), literal:True, loop:while (-> +3), loop_with_late_exit:while (-> +3), node:NameConstant, node:While (-> +3)
        prime = next(numbers) # assignment:next, assignment_lhs_identifier:prime, assignment_rhs_atom:numbers, call_argument:numbers, external_free_call:next, free_call:next, node:Assign, node:Call, node:Name, single_assignment:prime
        yield prime # node:Expr, node:Name, node:Yield, yield:prime
        numbers = filter(prime.__rmod__, numbers) # assignment:filter, assignment_lhs_identifier:numbers, assignment_rhs_atom:numbers, assignment_rhs_atom:prime, call_argument:, call_argument:numbers, external_free_call:filter, free_call:filter, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:numbers, update:numbers:prime, update_by_assignment:numbers:prime, update_by_assignment_with:filter, update_with:filter
for p in iter_primes(): # for:p (-> +3), free_call:iter_primes, free_call_without_arguments:iter_primes, internal_free_call:iter_primes, loop:for (-> +3), loop_with_break:for (-> +3), loop_with_early_exit:for:break (-> +3), node:Call, node:For (-> +3), node:Name
    if p > 1000: # comparison_operator:Gt, if (-> +1), if_test_atom:1000, if_test_atom:p, if_without_else (-> +1), literal:1000, node:Compare, node:If (-> +1), node:Name, node:Num, suggest_constant_definition
        break # if_then_branch, node:Break
    print(p) # call_argument:p, external_free_call:print, free_call:print, free_call_without_result:print, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 21_xml_html_parsing.py
# ----------------------------------------------------------------------------------------
dinner_recipe = """<html><body><table> # assignment, assignment_lhs_identifier:dinner_recipe, node:Assign (-> +6), node:Name, single_assignment:dinner_recipe, whole_span:14 (-> +13)
<tr><th>amt</th><th>unit</th><th>item</th></tr>
<tr><td>24</td><td>slices</td><td>baguette</td></tr>
<tr><td>2+</td><td>tbsp</td><td>olive oil</td></tr>
<tr><td>1</td><td>cup</td><td>tomatoes</td></tr>
<tr><td>1</td><td>jar</td><td>pesto</td></tr>
</table></body></html>""" # literal:Str, node:Str
import xml.etree.ElementTree as etree # import:xml.etree.ElementTree, import_module:xml.etree.ElementTree, node:Import
tree = etree.fromstring(dinner_recipe) # assignment:fromstring, assignment_lhs_identifier:tree, assignment_rhs_atom:dinner_recipe, assignment_rhs_atom:etree, call_argument:dinner_recipe, member_call:fromstring, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:tree
pantry = {"olive oil", "pesto"} # assignment, assignment_lhs_identifier:pantry, literal:Set, literal:Str, node:Assign, node:Name, node:Set, node:Str, single_assignment:pantry
for ingredient in tree.getiterator("tr"): # call_argument:, for:ingredient (-> +3), literal:Str, loop:for (-> +3), loop_with_late_exit:for (-> +3), member_call:getiterator, node:Attribute, node:Call, node:For (-> +3), node:Name, node:Str
    amt, unit, item = ingredient # assignment, assignment_lhs_identifier:amt, assignment_lhs_identifier:item, assignment_lhs_identifier:unit, assignment_rhs_atom:ingredient, literal:Tuple, node:Assign, node:Name, node:Tuple, parallel_assignment:3
    if item.tag == "td" and item.text not in pantry: # boolean_operator:And, comparison_operator:Eq, comparison_operator:NotIn, if (-> +1), if_test_atom:item, if_test_atom:pantry, if_without_else (-> +1), literal:Str, node:Attribute, node:BoolOp, node:Compare, node:If (-> +1), node:Name, node:Str
        print("{}: {} {}".format(item.text, amt.text, unit.text)) # call_argument:, composition, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, member_call:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 28_queens.py
# ----------------------------------------------------------------------------------------
BOARD_SIZE = 8 # assignment:8, assignment_lhs_identifier:BOARD_SIZE, assignment_rhs_atom:8, literal:8, node:Assign, node:Name, node:Num, single_assignment:BOARD_SIZE, whole_span:24 (-> +23)
class BailOut(Exception): # class:BailOut (-> +1), node:ClassDef (-> +1), node:Name
    pass # node:Pass
def validate(queens): # function:validate (-> +5), function_argument:queens, function_argument_flavor:arg, function_returning_nothing:validate (-> +5), node:FunctionDef (-> +5), node:arg
    left = right = col = queens[-1] # assignment, assignment_lhs_identifier:col, assignment_lhs_identifier:left, assignment_lhs_identifier:right, assignment_rhs_atom:-1, assignment_rhs_atom:queens, chained_assignment, index:-1, literal:-1, negative_index:-1, node:Assign, node:Name, node:Num, node:Subscript
    for r in reversed(queens[:-1]): # call_argument:, external_free_call:reversed, for:r (-> +3), free_call:reversed, literal:-1, loop:for (-> +3), loop_with_early_exit:for:raise (-> +3), loop_with_raise:for (-> +3), node:Call, node:For (-> +3), node:Name, node:Num, node:Subscript, slice::-1:, slice_lower:, slice_step:, slice_upper:-1
        left, right = left - 1, right + 1 # addition_operator, assignment, assignment_lhs_identifier:left, assignment_lhs_identifier:right, assignment_rhs_atom:1, assignment_rhs_atom:left, assignment_rhs_atom:right, binary_operator:Add, binary_operator:Sub, literal:1, literal:Tuple, node:Assign, node:BinOp, node:Name, node:Num, node:Tuple, parallel_assignment:2, update:left:1, update:left:right, update:right:1, update:right:left, update_by_assignment:left:1, update_by_assignment:left:right, update_by_assignment:right:1, update_by_assignment:right:left, update_by_assignment_with, update_with
        if r in (left, col, right): # comparison_operator:In, if (-> +1), if_test_atom:col, if_test_atom:left, if_test_atom:r, if_test_atom:right, if_without_else (-> +1), literal:Tuple, node:Compare, node:If (-> +1), node:Name, node:Tuple
            raise BailOut # if_then_branch, node:Name, node:Raise, raise:BailOut
def add_queen(queens): # function:add_queen (-> +11), function_argument:queens, function_argument_flavor:arg, function_returning_something:add_queen (-> +11), node:FunctionDef (-> +11), node:arg, recursive_function:add_queen (-> +11), tail_recursive_function:add_queen (-> +11)
    for i in range(BOARD_SIZE): # call_argument:BOARD_SIZE, external_free_call:range, for:i (-> +9), for_range:BOARD_SIZE (-> +9), free_call:range, loop:for (-> +9), loop_with_early_exit:for:return (-> +9), loop_with_return:for (-> +9), node:Call, node:For (-> +9), node:Name, range:BOARD_SIZE
        test_queens = queens + [i] # assignment:Add, assignment_lhs_identifier:test_queens, assignment_rhs_atom:i, assignment_rhs_atom:queens, binary_operator:Add, concatenation_operator:List, literal:List, node:Assign, node:BinOp, node:List, node:Name, single_assignment:test_queens
        try: # node:Try (-> +7), try_except:BailOut (-> +7)
            validate(test_queens) # call_argument:test_queens, free_call:validate, free_call_without_result:validate, internal_free_call:validate, node:Call, node:Expr, node:Name
            if len(test_queens) == BOARD_SIZE: # call_argument:test_queens, comparison_operator:Eq, external_free_call:len, free_call:len, if (-> +3), if_test_atom:BOARD_SIZE, if_test_atom:test_queens, node:Call, node:Compare, node:If (-> +3), node:Name
                return test_queens # if_then_branch, node:Name, node:Return, return:test_queens
            else:
                return add_queen(test_queens) # call_argument:test_queens, free_call:add_queen, free_tail_call:add_queen, if_else_branch, internal_free_call:add_queen, node:Call, node:Name, node:Return, return
        except BailOut: # except:BailOut, node:ExceptHandler (-> +1), node:Name
            pass # node:Pass
    raise BailOut # node:Name, node:Raise, raise:BailOut
queens = add_queen([]) # assignment:add_queen, assignment_lhs_identifier:queens, call_argument:, empty_literal:List, free_call:add_queen, internal_free_call:add_queen, literal:List, node:Assign, node:Call, node:List, node:Name, single_assignment:queens
print(queens) # call_argument:queens, external_free_call:print, free_call:print, free_call_without_result:print, node:Call, node:Expr, node:Name
print("\n".join(". " * q + "Q " + ". " * (BOARD_SIZE - q - 1) for q in queens)) # binary_operator:Add, binary_operator:Mult, binary_operator:Sub, call_argument:, composition, comprehension:Generator, comprehension_for_count:1, concatenation_operator:Str, external_free_call:print, free_call:print, free_call_without_result:print, literal:1, literal:Str, member_call:join, node:Attribute, node:BinOp, node:Call, node:Expr, node:GeneratorExp, node:Name, node:Num, node:Str, replication_operator:Str

# ----------------------------------------------------------------------------------------
# 33_guess_the_number.py
# ----------------------------------------------------------------------------------------
import random # import:random, import_module:random, node:Import, whole_span:18 (-> +17)
guesses_made = 0 # assignment:0, assignment_lhs_identifier:guesses_made, assignment_rhs_atom:0, literal:0, node:Assign, node:Name, node:Num, single_assignment:guesses_made
name = input("Hello! What is your name?\n") # assignment:input, assignment_lhs_identifier:name, call_argument:, external_free_call:input, free_call:input, literal:Str, node:Assign, node:Call, node:Name, node:Str, single_assignment:name
number = random.randint(1, 20) # assignment:randint, assignment_lhs_identifier:number, assignment_rhs_atom:1, assignment_rhs_atom:20, assignment_rhs_atom:random, call_argument:1, call_argument:20, literal:1, literal:20, member_call:randint, node:Assign, node:Attribute, node:Call, node:Name, node:Num, single_assignment:number
print("Well, {}, I am thinking of a number between 1 and 20.".format(name)) # call_argument:, call_argument:name, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, member_call:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str
while guesses_made < 6: # comparison_operator:Lt, count_states:guesses_made (-> +8), literal:6, loop:while (-> +8), loop_with_break:while (-> +8), loop_with_early_exit:while:break (-> +8), node:Compare, node:Name, node:Num, node:While (-> +8)
    guess = int(input("Take a guess: ")) # assignment:int, assignment_lhs_identifier:guess, call_argument:, composition, external_free_call:input, external_free_call:int, free_call:input, free_call:int, literal:Str, node:Assign, node:Call, node:Name, node:Str, single_assignment:guess
    guesses_made += 1 # assignment_lhs_identifier:guesses_made, assignment_rhs_atom:1, augmented_assignment:Add, increment:guesses_made, literal:1, node:AugAssign, node:Name, node:Num, update:guesses_made:1, update_by_augmented_assignment:guesses_made:1, update_by_augmented_assignment_with:Add, update_with:Add
    if guess < number: # comparison_operator:Lt, if (-> +1), if_test_atom:guess, if_test_atom:number, if_without_else (-> +1), node:Compare, node:If (-> +1), node:Name
        print("Your guess is too low.") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, node:Call, node:Expr, node:Name, node:Str
    if guess > number: # comparison_operator:Gt, if (-> +1), if_test_atom:guess, if_test_atom:number, if_without_else (-> +1), node:Compare, node:If (-> +1), node:Name
        print("Your guess is too high.") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, node:Call, node:Expr, node:Name, node:Str
    if guess == number: # comparison_operator:Eq, if (-> +1), if_test_atom:guess, if_test_atom:number, if_without_else (-> +1), node:Compare, node:If (-> +1), node:Name
        break # if_then_branch, node:Break
if guess == number: # comparison_operator:Eq, if (-> +3), if_test_atom:guess, if_test_atom:number, node:Compare, node:If (-> +3), node:Name
    print("Good job, {}! You guessed my number in {} guesses!".format(name, guesses_made)) # call_argument:, call_argument:guesses_made, call_argument:name, composition, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, literal:Str, member_call:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str
else:
    print("Nope. The number I was thinking of was {}".format(number)) # call_argument:, call_argument:number, composition, external_free_call:print, free_call:print, free_call_without_result:print, if_else_branch, literal:Str, member_call:format, node:Attribute, node:Call, node:Expr, node:Name, node:Str
