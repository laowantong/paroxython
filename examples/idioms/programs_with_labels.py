# ----------------------------------------------------------------------------------------
# 001.0003-print-hello-world.py
# ----------------------------------------------------------------------------------------
from __future__ import print_function # flat_style (-> +1), imperative_style (-> +1), import:__future__:print_function, import_module:__future__, import_name:print_function, node:ImportFrom, one_liner_style (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
print("Hello World") # argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 001.1159-print-hello-world.py
# ----------------------------------------------------------------------------------------
print("Hello World") # argument:, external_free_call:print, flat_style, free_call:print, free_call_without_result:print, imperative_style, literal:Str, node:Call, node:Expr, node:Name, node:Str, one_liner_style, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 002.0011-print-hello-10-times.py
# ----------------------------------------------------------------------------------------
for i in range(10): # argument:10, external_free_call:range, for:i (-> +1), for_range:10 (-> +1), free_call:range, global_scope:i (-> +1), imperative_style (-> +1), iteration_variable:i, literal:10, loop:for (-> +1), loop_with_late_exit:for (-> +1), magic_number:10, node:Call, node:For (-> +1), node:Name, node:Num, range:10, scope:i (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    print("Hello") # argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 002.1493-print-hello-10-times.py
# ----------------------------------------------------------------------------------------
print("Hello\n" * 10) # argument:, binary_operator:Mult, external_free_call:print, flat_style, free_call:print, free_call_without_result:print, imperative_style, literal:10, literal:Str, magic_number:10, node:BinOp, node:Call, node:Expr, node:Name, node:Num, node:Str, one_liner_style, replication_operator:Str, special_literal_string:Hello\n, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 002.3117-print-hello-10-times.py
# ----------------------------------------------------------------------------------------
print("Hello\n" * 10) # argument:, binary_operator:Mult, external_free_call:print, flat_style, free_call:print, free_call_without_result:print, imperative_style, literal:10, literal:Str, magic_number:10, node:BinOp, node:Call, node:Expr, node:Name, node:Num, node:Str, one_liner_style, replication_operator:Str, special_literal_string:Hello\n, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 003.0019-create-a-procedure.py
# ----------------------------------------------------------------------------------------
def finish(name): # function:finish (-> +1), function_line_count:2 (-> +1), function_parameter:name, function_parameter_flavor:arg, function_returning_nothing:finish (-> +1), local_scope:name (-> +1), node:FunctionDef (-> +1), node:arg, one_liner_style (-> +1), procedural_style (-> +1), scope:name (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
    print("My job here is done. Goodbye " + name) # argument:, binary_operator:Add, concatenation_operator:Str, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:name, node:BinOp, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 003.2372-create-a-procedure.py
# ----------------------------------------------------------------------------------------
def a(): # function:a (-> +1), function_line_count:2 (-> +1), function_returning_nothing:a (-> +1), function_without_parameters:a (-> +1), node:FunctionDef (-> +1), one_liner_style (-> +1), procedural_style (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
    pass # no_operation, node:Pass

# ----------------------------------------------------------------------------------------
# 004.0024-create-a-function-which-returns-the-square-of-an-integer.py
# ----------------------------------------------------------------------------------------
def square(x): # function:square (-> +1), function_line_count:2 (-> +1), function_parameter:x, function_parameter_flavor:arg, function_returning_something:square (-> +1), functional_style (-> +1), local_scope:x (-> +1), node:FunctionDef (-> +1), node:arg, one_liner_style (-> +1), pure_function:square (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    return x * x # binary_operator:Mult, loaded_variable:x, multiplication_operator, node:BinOp, node:Name, node:Return, return

# ----------------------------------------------------------------------------------------
# 004.2921-create-a-function-which-returns-the-square-of-an-integer.py
# ----------------------------------------------------------------------------------------
def square(x): # function:square (-> +1), function_line_count:2 (-> +1), function_parameter:x, function_parameter_flavor:arg, function_returning_something:square (-> +1), functional_style (-> +1), local_scope:x (-> +1), node:FunctionDef (-> +1), node:arg, one_liner_style (-> +1), pure_function:square (-> +1), scope:x (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
    return x ** 2 # binary_operator:Pow, literal:2, loaded_variable:x, node:BinOp, node:Name, node:Num, node:Return, return

# ----------------------------------------------------------------------------------------
# 005.0663-create-a-2d-point-data-structure.py
# ----------------------------------------------------------------------------------------
from dataclasses import dataclass # import:dataclasses:dataclass, import_module:dataclasses, import_name:dataclass, node:ImportFrom, object_oriented_style (-> +4), variety:3 (-> +4), whole_span:5 (-> +4)
@dataclass # loaded_variable:dataclass, node:Name
class Point: # class:Point (-> +2), node:ClassDef (-> +2)
    x: float # loaded_variable:float, node:AnnAssign, node:Name
    y: float # loaded_variable:float, node:AnnAssign, node:Name

# ----------------------------------------------------------------------------------------
# 006.0032-iterate-over-list-values.py
# ----------------------------------------------------------------------------------------
for x in items: # for:x (-> +1), for_each:x (-> +1), global_scope:x (-> +1), imperative_style (-> +1), iteration_variable:x, loaded_variable:items, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:For (-> +1), node:Name, scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    doSomething(x) # argument:x, external_free_call:doSomething, free_call:doSomething, free_call_without_result:doSomething, loaded_variable:x, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 007.0183-iterate-over-list-indexes-and-values.py
# ----------------------------------------------------------------------------------------
for i, x in enumerate(items): # argument:items, external_free_call:enumerate, for:i (-> +1), for:x (-> +1), for_indexes_elements:i (-> +1), free_call:enumerate, global_scope:i (-> +1), global_scope:x (-> +1), imperative_style (-> +1), iteration_variable:i, iteration_variable:x, literal:Tuple, loaded_variable:items, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:Call, node:For (-> +1), node:Name, node:Tuple, scope:i (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    print(i, x) # argument:i, argument:x, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:i, loaded_variable:x, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 008.0039-initialize-a-new-map-associative-array.py
# ----------------------------------------------------------------------------------------
x = {"one": 1, "two": 2} # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:1, assignment_rhs_atom:2, flat_style, global_scope:x, imperative_style, literal:1, literal:2, literal:Dict, literal:Str, node:Assign, node:Dict, node:Name, node:Num, node:Str, one_liner_style, scope:x, single_assignment:x, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 009.1410-create-a-binary-tree-data-structure.py
# ----------------------------------------------------------------------------------------
class Node: # class:Node (-> +4), class_method_count:1 (-> +4), node:ClassDef (-> +4), object_oriented_style (-> +4), variety:2 (-> +4), whole_span:5 (-> +4)
    def __init__(self, data): # function:__init__ (-> +3), function_line_count:4 (-> +3), function_parameter:data, function_parameter:self, function_parameter_flavor:arg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), local_scope:data (-> +3), local_scope:self (-> +3), method:__init__ (-> +3), node:FunctionDef (-> +3), node:arg, scope:data (-> +3), scope:self (-> +3)
        self.data = data # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:data, loaded_variable:data, loaded_variable:self, node:Assign, node:Attribute, node:Name
        self.left = None # assignment:None, assignment_lhs_identifier:self, assignment_rhs_atom:None, literal:None, loaded_variable:self, node:Assign, node:Attribute, node:Name, node:NameConstant
        self.right = None # assignment:None, assignment_lhs_identifier:self, assignment_rhs_atom:None, literal:None, loaded_variable:self, node:Assign, node:Attribute, node:Name, node:NameConstant

# ----------------------------------------------------------------------------------------
# 009.3176-create-a-binary-tree-data-structure.py
# ----------------------------------------------------------------------------------------
class Node: # class:Node (-> +4), class_method_count:1 (-> +4), node:ClassDef (-> +4), object_oriented_style (-> +4), variety:2 (-> +4), whole_span:5 (-> +4)
    def __init__(self, data, left_child, right_child): # function:__init__ (-> +3), function_line_count:4 (-> +3), function_parameter:data, function_parameter:left_child, function_parameter:right_child, function_parameter:self, function_parameter_flavor:arg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), local_scope:data (-> +3), local_scope:left_child (-> +3), local_scope:right_child (-> +3), local_scope:self (-> +3), method:__init__ (-> +3), node:FunctionDef (-> +3), node:arg, scope:data (-> +3), scope:left_child (-> +3), scope:right_child (-> +3), scope:self (-> +3)
        self.data = data # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:data, loaded_variable:data, loaded_variable:self, node:Assign, node:Attribute, node:Name
        self._left_child = left_child # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:left_child, loaded_variable:left_child, loaded_variable:self, node:Assign, node:Attribute, node:Name
        self._right_child = right_child # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:right_child, loaded_variable:right_child, loaded_variable:self, node:Assign, node:Attribute, node:Name

# ----------------------------------------------------------------------------------------
# 010.0182-shuffle-a-list.py
# ----------------------------------------------------------------------------------------
from random import shuffle # flat_style (-> +1), imperative_style (-> +1), import:random:shuffle, import_module:random, import_name:shuffle, node:ImportFrom, one_liner_style (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
shuffle(x) # argument:x, external_free_call:shuffle, free_call:shuffle, free_call_without_result:shuffle, loaded_variable:x, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 010.1478-shuffle-a-list.py
# ----------------------------------------------------------------------------------------
import random # flat_style (-> +1), imperative_style (-> +1), import:random, import_module:random, node:Import, one_liner_style (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
random.shuffle(list) # argument:list, loaded_variable:list, loaded_variable:random, member_call:random:shuffle, member_call_method:shuffle, member_call_object:random, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 011.0047-pick-a-random-element-from-a-list.py
# ----------------------------------------------------------------------------------------
import random # flat_style (-> +1), imperative_style (-> +1), import:random, import_module:random, node:Import, one_liner_style (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
random.choice(x) # argument:x, loaded_variable:random, loaded_variable:x, member_call:random:choice, member_call_method:choice, member_call_object:random, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 012.0181-check-if-list-contains-a-value.py
# ----------------------------------------------------------------------------------------
x in list # comparison_operator:In, flat_style, imperative_style, loaded_variable:list, loaded_variable:x, node:Compare, node:Expr, node:Name, one_liner_style, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 013.0574-iterate-over-map-keys-and-values.py
# ----------------------------------------------------------------------------------------
for k, v in mymap.items(): # for:k (-> +1), for:v (-> +1), global_scope:k (-> +1), global_scope:v (-> +1), imperative_style (-> +1), iteration_variable:k, iteration_variable:v, literal:Tuple, loaded_variable:mymap, loop:for (-> +1), loop_with_late_exit:for (-> +1), member_call_method:items, node:Attribute, node:Call, node:For (-> +1), node:Name, node:Tuple, scope:k (-> +1), scope:v (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    print(k, v) # argument:k, argument:v, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:k, loaded_variable:v, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 014.0185-pick-uniformly-a-random-floating-point-number-in-ab.py
# ----------------------------------------------------------------------------------------
import random # functional_style (-> +2), import:random, import_module:random, node:Import, one_liner_style (-> +2), variety:2 (-> +2), whole_span:3 (-> +2)
def pick(a, b): # function:pick (-> +1), function_line_count:2 (-> +1), function_parameter:a, function_parameter:b, function_parameter_flavor:arg, function_returning_something:pick (-> +1), local_scope:a (-> +1), local_scope:b (-> +1), node:FunctionDef (-> +1), node:arg, pure_function:pick (-> +1), scope:a (-> +1), scope:b (-> +1)
    return random.randrange(a, b) # argument:a, argument:b, loaded_variable:a, loaded_variable:b, loaded_variable:random, member_call:random:randrange, member_call_method:randrange, member_call_object:random, node:Attribute, node:Call, node:Name, node:Return, return

# ----------------------------------------------------------------------------------------
# 014.3410-pick-uniformly-a-random-floating-point-number-in-ab.py
# ----------------------------------------------------------------------------------------
import random # flat_style (-> +1), imperative_style (-> +1), import:random, import_module:random, node:Import, one_liner_style (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
random.uniform(a, b) # argument:a, argument:b, loaded_variable:a, loaded_variable:b, loaded_variable:random, member_call:random:uniform, member_call_method:uniform, member_call_object:random, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 015.0184-pick-uniformly-a-random-integer-in-ab.py
# ----------------------------------------------------------------------------------------
import random # flat_style (-> +1), imperative_style (-> +1), import:random, import_module:random, node:Import, one_liner_style (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
random.randint(a, b) # argument:a, argument:b, loaded_variable:a, loaded_variable:b, loaded_variable:random, member_call:random:randint, member_call_method:randint, member_call_object:random, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 016.1530-depth-first-traversing-of-a-binary-tree.py
# ----------------------------------------------------------------------------------------
def dfs(bt): # body_recursive_function:dfs (-> +5), function:dfs (-> +5), function_line_count:6 (-> +5), function_parameter:bt, function_parameter_flavor:arg, function_returning_nothing:dfs (-> +5), local_scope:bt (-> +5), node:FunctionDef (-> +5), node:arg, procedural_style (-> +5), recursive_call_count:2 (-> +5), recursive_function:dfs (-> +5), scope:bt (-> +5), variety:4 (-> +5), whole_span:6 (-> +5)
    if bt is None: # comparison_operator:Is, if (-> +1), if_guard (-> +1), if_test_atom:None, if_test_atom:bt, if_without_else (-> +1), literal:None, loaded_variable:bt, node:Compare, node:If (-> +1), node:Name, node:NameConstant
        return # if_then_branch, node:Return, return:None
    dfs(bt.left) # argument:, free_call:dfs, free_call_without_result:dfs, internal_free_call:dfs, loaded_variable:bt, node:Attribute, node:Call, node:Expr, node:Name
    f(bt) # argument:bt, external_free_call:f, free_call:f, free_call_without_result:f, loaded_variable:bt, node:Call, node:Expr, node:Name
    dfs(bt.right) # argument:, free_call:dfs, free_call_without_result:dfs, internal_free_call:dfs, loaded_variable:bt, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 017.1103-create-a-tree-data-structure.py
# ----------------------------------------------------------------------------------------
class Node(object): # class:Node (-> +3), class_method_count:1 (-> +3), loaded_variable:object, node:ClassDef (-> +3), node:Name, object_oriented_style (-> +3), variety:2 (-> +3), whole_span:4 (-> +3)
    def __init__(self, value, *children): # function:__init__ (-> +2), function_line_count:3 (-> +2), function_parameter:children, function_parameter:self, function_parameter:value, function_parameter_flavor:arg, function_parameter_flavor:vararg, function_returning_nothing:__init__ (-> +2), instance_method:__init__ (-> +2), local_scope:children (-> +2), local_scope:self (-> +2), local_scope:value (-> +2), method:__init__ (-> +2), node:FunctionDef (-> +2), node:arg, node:arguments, scope:children (-> +2), scope:self (-> +2), scope:value (-> +2)
        self.value = value # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:value, loaded_variable:self, loaded_variable:value, node:Assign, node:Attribute, node:Name
        self.children = list(children) # argument:children, assignment:list, assignment_lhs_identifier:self, assignment_rhs_atom:children, external_free_call:list, free_call:list, loaded_variable:children, loaded_variable:self, node:Assign, node:Attribute, node:Call, node:Name

# ----------------------------------------------------------------------------------------
# 018.2084-depth-first-traversing-of-a-tree.py
# ----------------------------------------------------------------------------------------
def DFS(f, root): # body_recursive_function:DFS (-> +3), function:DFS (-> +3), function_line_count:4 (-> +3), function_parameter:f, function_parameter:root, function_parameter_flavor:arg, function_returning_nothing:DFS (-> +3), higher_order_function:f (-> +3), local_scope:child (-> +3), local_scope:f (-> +3), local_scope:root (-> +3), node:FunctionDef (-> +3), node:arg, procedural_style (-> +3), recursive_call_count:1 (-> +3), recursive_function:DFS (-> +3), scope:child (-> +3), scope:f (-> +3), scope:root (-> +3), variety:2 (-> +3), whole_span:4 (-> +3)
    f(root) # argument:root, external_free_call:f, free_call:f, free_call_without_result:f, loaded_variable:root, node:Call, node:Expr, node:Name
    for child in root: # for:child (-> +1), for_each:child (-> +1), iteration_variable:child, loaded_variable:root, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:For (-> +1), node:Name
        DFS(f, child) # argument:child, argument:f, free_call:DFS, free_call_without_result:DFS, internal_free_call:DFS, loaded_variable:child, loaded_variable:f, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 019.0197-reverse-a-list.py
# ----------------------------------------------------------------------------------------
x = reversed(x) # argument:x, assignment:reversed, assignment_lhs_identifier:x, assignment_rhs_atom:x, external_free_call:reversed, flat_style, free_call:reversed, global_scope:x, imperative_style, loaded_variable:x, node:Assign, node:Call, node:Name, one_liner_style, scope:x, single_assignment:x, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 019.1983-reverse-a-list.py
# ----------------------------------------------------------------------------------------
y = x[::-1] # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:-1, assignment_rhs_atom:x, flat_style, global_scope:y, imperative_style, literal:-1, loaded_variable:x, node:Assign, node:Name, node:Num, node:Slice, node:Subscript, one_liner_style, scope:y, single_assignment:y, slice:::-1, slice_lower:, slice_step:-1, slice_upper:, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 019.3164-reverse-a-list.py
# ----------------------------------------------------------------------------------------
x.reverse() # flat_style, imperative_style, loaded_variable:x, member_call:x:reverse, member_call_method:reverse, member_call_object:x, node:Attribute, node:Call, node:Expr, node:Name, one_liner_style, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 020.0573-return-two-values.py
# ----------------------------------------------------------------------------------------
def search(m, x): # function:search (-> +3), function_line_count:4 (-> +3), function_parameter:m, function_parameter:x, function_parameter_flavor:arg, function_returning_something:search (-> +3), impure_function:search (-> +3), local_scope:idx (-> +3), local_scope:item (-> +3), local_scope:m (-> +3), local_scope:x (-> +3), node:FunctionDef (-> +3), node:arg, procedural_style (-> +3), scope:idx (-> +3), scope:item (-> +3), scope:m (-> +3), scope:x (-> +3), variety:2 (-> +3), whole_span:4 (-> +3)
    for idx, item in enumerate(m): # argument:m, external_free_call:enumerate, for:idx (-> +2), for:item (-> +2), for_indexes_elements:idx (-> +2), free_call:enumerate, iteration_variable:idx, iteration_variable:item, literal:Tuple, loaded_variable:m, loop:for (-> +2), loop_with_early_exit:for:return (-> +2), loop_with_return:for (-> +2), node:Call, node:For (-> +2), node:Name, node:Tuple
        if x in item: # comparison_operator:In, if (-> +1), if_test_atom:item, if_test_atom:x, if_without_else (-> +1), loaded_variable:item, loaded_variable:x, node:Compare, node:If (-> +1), node:Name
            return idx, item.index(x) # argument:x, if_then_branch, literal:Tuple, loaded_variable:idx, loaded_variable:item, loaded_variable:x, member_call_method:index, node:Attribute, node:Call, node:Name, node:Return, node:Tuple, return

# ----------------------------------------------------------------------------------------
# 021.0084-swap-values-of-variables-a-and-b.py
# ----------------------------------------------------------------------------------------
a, b = b, a # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:a, assignment_rhs_atom:b, flat_style, global_scope:a, global_scope:b, imperative_style, literal:Tuple, loaded_variable:a, loaded_variable:b, node:Assign, node:Name, node:Tuple, one_liner_style, parallel_assignment:2, scope:a, scope:b, swap, update:a:b, update:b:a, update_by_assignment:a:b, update_by_assignment:b:a, update_by_assignment_with, update_with, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 022.0243-convert-string-to-integer.py
# ----------------------------------------------------------------------------------------
i = int(s) # argument:s, assignment:int, assignment_lhs_identifier:i, assignment_rhs_atom:s, external_free_call:int, flat_style, free_call:int, global_scope:i, imperative_style, loaded_variable:s, node:Assign, node:Call, node:Name, one_liner_style, scope:i, single_assignment:i, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 023.1102-convert-real-number-to-string-with-2-decimal-places.py
# ----------------------------------------------------------------------------------------
s = "{:.2f}".format(x) # argument:x, assignment:format, assignment_lhs_identifier:s, assignment_rhs_atom:x, flat_style, global_scope:s, imperative_style, literal:Str, loaded_variable:x, member_call_method:format, node:Assign, node:Attribute, node:Call, node:Name, node:Str, one_liner_style, scope:s, single_assignment:s, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 024.0664-assign-to-string-the-japanese-word-.py
# ----------------------------------------------------------------------------------------
s = "ネコ" # assignment, assignment_lhs_identifier:s, flat_style, global_scope:s, imperative_style, literal:Str, node:Assign, node:Name, node:Str, one_liner_style, scope:s, single_assignment:s, special_literal_string:ネコ, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 025.0195-send-a-value-to-another-thread.py
# ----------------------------------------------------------------------------------------
from queue import Queue # global_scope:q (-> +9), import:queue:Queue, import_module:queue, import_name:Queue, node:ImportFrom, procedural_style (-> +9), scope:q (-> +9), variety:5 (-> +9), whole_span:10 (-> +9)
from threading import Thread # import:threading:Thread, import_module:threading, import_name:Thread, node:ImportFrom
q = Queue() # assignment:Queue, assignment_lhs_identifier:q, external_free_call:Queue, free_call:Queue, free_call_no_arguments:Queue, node:Assign, node:Call, node:Name, single_assignment:q
def worker(): # access_outer_scope:q (-> +3), function:worker (-> +3), function_line_count:4 (-> +3), function_returning_nothing:worker (-> +3), function_without_parameters:worker (-> +3), node:FunctionDef (-> +3)
    while True: # infinite_while (-> +2), literal:True, loop:while (-> +2), loop_with_late_exit:while (-> +2), node:NameConstant, node:While (-> +2)
        print(f"Hello, {q.get()}") # argument:, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:q, member_call:q:get, member_call_method:get, member_call_object:q, node:Attribute, node:Call, node:Expr, node:FormattedValue, node:JoinedStr, node:Name, node:Str
        q.task_done() # loaded_variable:q, member_call:q:task_done, member_call_method:task_done, member_call_object:q, node:Attribute, node:Call, node:Expr, node:Name
Thread(target=worker, daemon=True).start() # argument:True, argument:worker, external_free_call:Thread, free_call:Thread, free_call_with_keyword_argument:Thread:daemon, free_call_with_keyword_argument:Thread:target, keyword_argument:daemon, keyword_argument:target, literal:True, loaded_variable:worker, member_call_method:start, node:Attribute, node:Call, node:Expr, node:Name, node:NameConstant, node:keyword
q.put("Alan") # argument:, literal:Str, loaded_variable:q, member_call:q:put, member_call_method:put, member_call_object:q, node:Attribute, node:Call, node:Expr, node:Name, node:Str
q.join() # loaded_variable:q, member_call:q:join, member_call_method:join, member_call_object:q, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 026.0194-create-a-2-dimensional-array.py
# ----------------------------------------------------------------------------------------
x = [[0 for j in xrange(n)] for i in xrange(m)] # argument:m, argument:n, assignment, assignment_lhs_identifier:x, assignment_rhs_atom:0, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:m, assignment_rhs_atom:n, comprehension:List, comprehension_for_count:1, external_free_call:xrange, flat_style, free_call:xrange, imperative_style, iteration_variable:i, iteration_variable:j, literal:0, loaded_variable:m, loaded_variable:n, local_scope:i, local_scope:j, local_scope:x, node:Assign, node:Call, node:ListComp, node:Name, node:Num, node:comprehension, one_liner_style, scope:i, scope:j, scope:x, single_assignment:x, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 027.0192-create-a-3-dimensional-array.py
# ----------------------------------------------------------------------------------------
x = [[[0 for k in xrange(p)] for j in xrange(n)] for i in xrange(m)] # argument:m, argument:n, argument:p, assignment, assignment_lhs_identifier:x, assignment_rhs_atom:0, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:k, assignment_rhs_atom:m, assignment_rhs_atom:n, assignment_rhs_atom:p, comprehension:List, comprehension_for_count:1, external_free_call:xrange, flat_style, free_call:xrange, imperative_style, iteration_variable:i, iteration_variable:j, iteration_variable:k, literal:0, loaded_variable:m, loaded_variable:n, loaded_variable:p, local_scope:i, local_scope:j, local_scope:k, local_scope:x, node:Assign, node:Call, node:ListComp, node:Name, node:Num, node:comprehension, one_liner_style, scope:i, scope:j, scope:k, scope:x, single_assignment:x, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 027.0193-create-a-3-dimensional-array.py
# ----------------------------------------------------------------------------------------
import numpy # flat_style (-> +1), global_scope:x (-> +1), imperative_style (-> +1), import:numpy, import_module:numpy, node:Import, one_liner_style (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
x = numpy.zeros((m, n, p)) # argument:, assignment:zeros, assignment_lhs_identifier:x, assignment_rhs_atom:m, assignment_rhs_atom:n, assignment_rhs_atom:numpy, assignment_rhs_atom:p, literal:Tuple, loaded_variable:m, loaded_variable:n, loaded_variable:numpy, loaded_variable:p, member_call_method:zeros, node:Assign, node:Attribute, node:Call, node:Name, node:Tuple, single_assignment:x

# ----------------------------------------------------------------------------------------
# 028.0350-sort-by-a-property.py
# ----------------------------------------------------------------------------------------
items = sorted(items, key=lambda x: x.p) # argument:, argument:items, assignment:sorted, assignment_lhs_identifier:items, assignment_rhs_atom:items, assignment_rhs_atom:x, external_free_call:sorted, flat_style, free_call:sorted, free_call_with_keyword_argument:sorted:key, function_parameter:x, function_parameter_flavor:arg, global_scope:items, global_scope:x, imperative_style, keyword_argument:key, loaded_variable:items, loaded_variable:x, node:Assign, node:Attribute, node:Call, node:Lambda, node:Name, node:arg, node:keyword, one_liner_style, scope:items, scope:x, single_assignment:items, update:items:x, update_by_assignment:items:x, update_by_assignment_with:sorted, update_with:sorted, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 029.0199-remove-item-from-list-by-its-index.py
# ----------------------------------------------------------------------------------------
del items[i] # flat_style, imperative_style, index:i, loaded_variable:i, loaded_variable:items, node:Delete, node:Name, node:Subscript, one_liner_style, subscript_deletion:Name, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 030.0189-parallelize-execution-of-1000-independent-tasks.py
# ----------------------------------------------------------------------------------------
from multiprocessing import Pool # global_scope:i (-> +3), global_scope:pool (-> +3), imperative_style (-> +3), import:multiprocessing:Pool, import_module:multiprocessing, import_name:Pool, node:ImportFrom, scope:i (-> +3), scope:pool (-> +3), variety:2 (-> +3), whole_span:4 (-> +3)
pool = Pool() # assignment:Pool, assignment_lhs_identifier:pool, external_free_call:Pool, free_call:Pool, free_call_no_arguments:Pool, node:Assign, node:Call, node:Name, single_assignment:pool
for i in range(1, 1001): # argument:1, argument:1001, external_free_call:range, for:i (-> +1), for_range:1:1001 (-> +1), free_call:range, iteration_variable:i, literal:1, literal:1001, loop:for (-> +1), loop_with_late_exit:for (-> +1), magic_number:1001, node:Call, node:For (-> +1), node:Name, node:Num, range:1:1001
    pool.apply_async(f, [i]) # argument:, argument:f, literal:List, loaded_variable:f, loaded_variable:i, loaded_variable:pool, member_call:pool:apply_async, member_call_method:apply_async, member_call_object:pool, node:Attribute, node:Call, node:Expr, node:List, node:Name

# ----------------------------------------------------------------------------------------
# 031.0188-recursive-factorial-simple.py
# ----------------------------------------------------------------------------------------
def f(i): # body_recursive_function:f (-> +4), function:f (-> +4), function_line_count:5 (-> +4), function_parameter:i, function_parameter_flavor:arg, function_returning_something:f (-> +4), functional_style (-> +4), local_scope:i (-> +4), node:FunctionDef (-> +4), node:arg, pure_function:f (-> +4), recursive_call_count:1 (-> +4), recursive_function:f (-> +4), scope:i (-> +4), variety:3 (-> +4), whole_span:5 (-> +4)
    if i == 0: # comparison_operator:Eq, if (-> +3), if_test_atom:0, if_test_atom:i, literal:0, loaded_variable:i, node:Compare, node:If (-> +3), node:Name, node:Num
        return 1 # if_then_branch, literal:1, node:Num, node:Return, return:1
    else:
        return i * f(i - 1) # argument:, binary_operator:Mult, binary_operator:Sub, free_call:f, if_else_branch, internal_free_call:f, literal:1, loaded_variable:i, multiplication_operator, node:BinOp, node:Call, node:Name, node:Num, node:Return, return

# ----------------------------------------------------------------------------------------
# 032.0196-integer-exponentiation-by-squaring.py
# ----------------------------------------------------------------------------------------
def exp(x, n): # function:exp (-> +1), function_line_count:2 (-> +1), function_parameter:n, function_parameter:x, function_parameter_flavor:arg, function_returning_something:exp (-> +1), functional_style (-> +1), local_scope:n (-> +1), local_scope:x (-> +1), node:FunctionDef (-> +1), node:arg, one_liner_style (-> +1), pure_function:exp (-> +1), scope:n (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    return x ** n # binary_operator:Pow, loaded_variable:n, loaded_variable:x, node:BinOp, node:Name, node:Return, return

# ----------------------------------------------------------------------------------------
# 033.1420-atomically-read-and-update-variable.py
# ----------------------------------------------------------------------------------------
import threading # flat_style (-> +6), global_scope:lock (-> +6), global_scope:x (-> +6), imperative_style (-> +6), import:threading, import_module:threading, node:Import, scope:lock (-> +6), scope:x (-> +6), variety:2 (-> +6), whole_span:7 (-> +6)
lock = threading.Lock() # assignment:Lock, assignment_lhs_identifier:lock, assignment_rhs_atom:threading, loaded_variable:threading, member_call_method:Lock, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:lock
lock.acquire() # loaded_variable:lock, member_call:lock:acquire, member_call_method:acquire, member_call_object:lock, node:Attribute, node:Call, node:Expr, node:Name
try: # node:Try (-> +3)
    x = f(x) # argument:x, assignment:f, assignment_lhs_identifier:x, assignment_rhs_atom:x, external_free_call:f, free_call:f, loaded_variable:x, node:Assign, node:Call, node:Name, single_assignment:x
finally:
    lock.release() # loaded_variable:lock, member_call:lock:release, member_call_method:release, member_call_object:lock, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 034.0625-create-a-set-of-objects.py
# ----------------------------------------------------------------------------------------
class T(object): # class:T (-> +1), global_scope:x (-> +2), loaded_variable:object, node:ClassDef (-> +1), node:Name, object_oriented_style (-> +2), scope:x (-> +2), variety:2 (-> +2), whole_span:3 (-> +2)
    pass # no_operation, node:Pass
x = set(T()) # argument:, assignment:set, assignment_lhs_identifier:x, composition, external_free_call:T, external_free_call:set, free_call:T, free_call:set, free_call_no_arguments:T, node:Assign, node:Call, node:Name, single_assignment:x

# ----------------------------------------------------------------------------------------
# 035.0667-first-class-function--compose.py
# ----------------------------------------------------------------------------------------
def compose(f, g): # function:compose (-> +1), function_line_count:2 (-> +1), function_parameter:f, function_parameter:g, function_parameter_flavor:arg, function_returning_something:compose (-> +1), functional_style (-> +1), higher_order_function:f (-> +1), higher_order_function:g (-> +1), local_scope:a (-> +1), local_scope:f (-> +1), local_scope:g (-> +1), node:FunctionDef (-> +1), node:arg, one_liner_style (-> +1), pure_function:compose (-> +1), scope:a (-> +1), scope:f (-> +1), scope:g (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    return lambda a: g(f(a)) # argument:, argument:a, composition, external_free_call:f, external_free_call:g, free_call:f, free_call:g, function_parameter:a, function_parameter_flavor:arg, loaded_variable:a, node:Call, node:Lambda, node:Name, node:Return, node:arg, return

# ----------------------------------------------------------------------------------------
# 036.0670-first-class-function--generic-composition.py
# ----------------------------------------------------------------------------------------
def compose(f, g): # function:compose (-> +1), function_line_count:2 (-> +1), function_parameter:f, function_parameter:g, function_parameter_flavor:arg, function_returning_something:compose (-> +1), functional_style (-> +1), higher_order_function:f (-> +1), higher_order_function:g (-> +1), local_scope:f (-> +1), local_scope:g (-> +1), local_scope:x (-> +1), node:FunctionDef (-> +1), node:arg, one_liner_style (-> +1), pure_function:compose (-> +1), scope:f (-> +1), scope:g (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    return lambda x: g(f(x)) # argument:, argument:x, composition, external_free_call:f, external_free_call:g, free_call:f, free_call:g, function_parameter:x, function_parameter_flavor:arg, loaded_variable:x, node:Call, node:Lambda, node:Name, node:Return, node:arg, return

# ----------------------------------------------------------------------------------------
# 037.0671-currying.py
# ----------------------------------------------------------------------------------------
from functools import partial # functional_style (-> +5), import:functools:partial, import_module:functools, import_name:partial, node:ImportFrom, variety:3 (-> +5), whole_span:6 (-> +5)
def f(a): # closure:f (-> +3), function:f (-> +3), function_line_count:4 (-> +3), function_parameter:a, function_parameter_flavor:arg, function_returning_something:f (-> +3), local_scope:a (-> +3), nested_function:f (-> +3), node:FunctionDef (-> +3), node:arg, pure_function:f (-> +3), scope:a (-> +3)
    def add(b): # access_outer_scope:a (-> +1), function:add (-> +1), function_line_count:2 (-> +1), function_parameter:b, function_parameter_flavor:arg, function_returning_something:add (-> +1), local_scope:b (-> +1), node:FunctionDef (-> +1), node:arg, pure_function:add (-> +1), scope:b (-> +1)
        return a + b # addition_operator, binary_operator:Add, loaded_variable:a, loaded_variable:b, node:BinOp, node:Name, node:Return, return
    return add # loaded_variable:add, node:Name, node:Return, return:add
print(f(2)(1)) # argument:, argument:1, argument:2, composition, external_free_call:print, free_call:f, free_call:print, free_call_without_result:print, internal_free_call:f, literal:1, literal:2, node:Call, node:Expr, node:Name, node:Num

# ----------------------------------------------------------------------------------------
# 038.0186-extract-a-substring.py
# ----------------------------------------------------------------------------------------
t = s[i:j] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:s, flat_style, global_scope:t, imperative_style, loaded_variable:i, loaded_variable:j, loaded_variable:s, node:Assign, node:Name, node:Slice, node:Subscript, one_liner_style, scope:t, single_assignment:t, slice:i:j:, slice_lower:i, slice_step:, slice_upper:j, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 039.0571-check-if-string-contains-a-word.py
# ----------------------------------------------------------------------------------------
ok = word in s # assignment, assignment_lhs_identifier:ok, assignment_rhs_atom:s, assignment_rhs_atom:word, comparison_operator:In, flat_style, global_scope:ok, imperative_style, loaded_variable:s, loaded_variable:word, node:Assign, node:Compare, node:Name, one_liner_style, scope:ok, single_assignment:ok, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 040.2279-graph-with-adjacency-lists.py
# ----------------------------------------------------------------------------------------
from collections import defaultdict # global_scope:G (-> +12), import:collections:defaultdict, import_module:collections, import_name:defaultdict, node:ImportFrom, object_oriented_style (-> +12), scope:G (-> +12), variety:4 (-> +12), whole_span:13 (-> +12)
class Vertex(set): # class:Vertex (-> +1), class_method_count:2 (-> +1), loaded_variable:set, node:ClassDef (-> +1), node:Name
    pass # no_operation, node:Pass
class Graph(defaultdict): # class:Graph (-> +8), class_method_count:2 (-> +8), loaded_variable:defaultdict, node:ClassDef (-> +8), node:Name
    def __init__(self, *paths): # function:__init__ (-> +3), function_line_count:4 (-> +3), function_parameter:paths, function_parameter:self, function_parameter_flavor:arg, function_parameter_flavor:vararg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), local_scope:path (-> +3), local_scope:paths (-> +3), local_scope:self (-> +3), method:__init__ (-> +3), node:FunctionDef (-> +3), node:arg, node:arguments, scope:path (-> +3), scope:paths (-> +3), scope:self (-> +3)
        self.default_factory = Vertex # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:Vertex, loaded_variable:Vertex, loaded_variable:self, node:Assign, node:Attribute, node:Name
        for path in paths: # for:path (-> +1), for_each:path (-> +1), iteration_variable:path, loaded_variable:paths, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:For (-> +1), node:Name
            self.make_path(path) # argument:path, loaded_variable:path, loaded_variable:self, member_call:self:make_path, member_call_method:make_path, member_call_object:self, node:Attribute, node:Call, node:Expr, node:Name
    def make_path(self, labels): # function:make_path (-> +3), function_line_count:4 (-> +3), function_parameter:labels, function_parameter:self, function_parameter_flavor:arg, function_returning_nothing:make_path (-> +3), instance_method:make_path (-> +3), local_scope:l1 (-> +3), local_scope:l2 (-> +3), local_scope:labels (-> +3), local_scope:self (-> +3), method:make_path (-> +3), node:FunctionDef (-> +3), node:arg, scope:l1 (-> +3), scope:l2 (-> +3), scope:labels (-> +3), scope:self (-> +3)
        for l1, l2 in zip(labels, labels[1:]): # argument:, argument:labels, external_free_call:zip, for:l1 (-> +2), for:l2 (-> +2), free_call:zip, iteration_variable:l1, iteration_variable:l2, literal:1, literal:Tuple, loaded_variable:labels, loop:for (-> +2), loop_with_late_exit:for (-> +2), node:Call, node:For (-> +2), node:Name, node:Num, node:Slice, node:Subscript, node:Tuple, slice:1::, slice_lower:1, slice_step:, slice_upper:
            self[l1].add(l2) # argument:l2, index:l1, loaded_variable:l1, loaded_variable:l2, loaded_variable:self, member_call_method:add, node:Attribute, node:Call, node:Expr, node:Name, node:Subscript
            self[l2].add(l1) # argument:l1, index:l2, loaded_variable:l1, loaded_variable:l2, loaded_variable:self, member_call_method:add, node:Attribute, node:Call, node:Expr, node:Name, node:Subscript
G = Graph((0, 1, 2, 3), (1, 4, 2)) # argument:, assignment:Graph, assignment_lhs_identifier:G, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:4, external_free_call:Graph, free_call:Graph, literal:0, literal:1, literal:2, literal:3, literal:4, literal:Tuple, node:Assign, node:Call, node:Name, node:Num, node:Tuple, single_assignment:G

# ----------------------------------------------------------------------------------------
# 041.0187-reverse-a-string.py
# ----------------------------------------------------------------------------------------
t = s.decode("utf8")[::-1].encode("utf8") # argument:, assignment:encode, assignment_lhs_identifier:t, assignment_rhs_atom:-1, assignment_rhs_atom:s, flat_style, global_scope:t, imperative_style, literal:-1, literal:Str, loaded_variable:s, member_call:s:decode, member_call:s:encode, member_call_method:decode, member_call_method:encode, member_call_object:s, node:Assign, node:Attribute, node:Call, node:Name, node:Num, node:Slice, node:Str, node:Subscript, one_liner_style, scope:t, single_assignment:t, slice:::-1, slice_lower:, slice_step:-1, slice_upper:, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 041.2714-reverse-a-string.py
# ----------------------------------------------------------------------------------------
t = s[::-1] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:-1, assignment_rhs_atom:s, flat_style, global_scope:t, imperative_style, literal:-1, loaded_variable:s, node:Assign, node:Name, node:Num, node:Slice, node:Subscript, one_liner_style, scope:t, single_assignment:t, slice:::-1, slice_lower:, slice_step:-1, slice_upper:, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 042.1264-continue-outer-loop.py
# ----------------------------------------------------------------------------------------
for v in a: # for:v (-> +7), for_each:v (-> +7), global_scope:u (-> +7), global_scope:v (-> +7), imperative_style (-> +7), iteration_variable:v, loaded_variable:a, loop:for (-> +7), loop_with_early_exit:for:raise (-> +7), loop_with_raise:for (-> +7), node:For (-> +7), node:Name, scope:u (-> +7), scope:v (-> +7), variety:4 (-> +7), whole_span:8 (-> +7)
    try: # node:Try (-> +6), try_except:Exception (-> +6), try_raise:Exception (-> +6)
        for u in b: # for:u (-> +2), for_each:u (-> +2), iteration_variable:u, loaded_variable:b, loop:for (-> +2), loop_with_early_exit:for:raise (-> +2), loop_with_raise:for (-> +2), nested_for:1 (-> +2), node:For (-> +2), node:Name
            if v == u: # comparison_operator:Eq, if (-> +1), if_test_atom:u, if_test_atom:v, if_without_else (-> +1), loaded_variable:u, loaded_variable:v, node:Compare, node:If (-> +1), node:Name
                raise Exception() # external_free_call:Exception, free_call:Exception, free_call_no_arguments:Exception, if_then_branch, node:Call, node:Name, node:Raise, raise:Exception
        print(v) # argument:v, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:v, node:Call, node:Expr, node:Name
    except Exception: # except:Exception, loaded_variable:Exception, node:ExceptHandler (-> +1), node:Name
        continue # node:Continue

# ----------------------------------------------------------------------------------------
# 042.3168-continue-outer-loop.py
# ----------------------------------------------------------------------------------------
for v in a: # for:v (-> +4), for_each:v (-> +4), global_scope:v (-> +4), global_scope:v_ (-> +4), imperative_style (-> +4), iteration_variable:v, loaded_variable:a, loop:for (-> +4), loop_with_late_exit:for (-> +4), node:For (-> +4), node:Name, scope:v (-> +4), scope:v_ (-> +4), variety:3 (-> +4), whole_span:5 (-> +4)
    for v_ in b: # for:v_ (-> +3), for_each:v_ (-> +3), iteration_variable:v_, loaded_variable:b, loop:for (-> +3), loop_with_late_exit:for (-> +3), nested_for:1 (-> +3), node:For (-> +3), node:Name
        if v == v_: # comparison_operator:Eq, if (-> +1), if_test_atom:v, if_test_atom:v_, if_without_else (-> +1), loaded_variable:v, loaded_variable:v_, node:Compare, node:If (-> +1), node:Name
            continue # if_then_branch, node:Continue
        print(v) # argument:v, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:v, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 043.0676-break-outer-loop.py
# ----------------------------------------------------------------------------------------
class BreakOuterLoop(Exception): # class:BreakOuterLoop (-> +1), global_scope:column (-> +10), global_scope:position (-> +10), global_scope:row (-> +10), loaded_variable:Exception, node:ClassDef (-> +1), node:Name, object_oriented_style (-> +10), scope:column (-> +10), scope:position (-> +10), scope:row (-> +10), variety:5 (-> +10), whole_span:11 (-> +10)
    pass # no_operation, node:Pass
try: # node:Try (-> +8), try_except:BreakOuterLoop (-> +8), try_raise:BreakOuterLoop (-> +8)
    position = None # assignment:None, assignment_lhs_identifier:position, assignment_rhs_atom:None, literal:None, node:Assign, node:Name, node:NameConstant, single_assignment:position
    for row in m: # for:row (-> +4), for_each:row (-> +4), iteration_variable:row, loaded_variable:m, loop:for (-> +4), loop_with_early_exit:for:raise (-> +4), loop_with_raise:for (-> +4), node:For (-> +4), node:Name
        for column in m[row]: # for:column (-> +3), index:row, iteration_variable:column, loaded_variable:m, loaded_variable:row, loop:for (-> +3), loop_with_early_exit:for:raise (-> +3), loop_with_raise:for (-> +3), nested_for:1 (-> +3), node:For (-> +3), node:Name, node:Subscript
            if m[row][column] == v: # comparison_operator:Eq, if (-> +2), if_test_atom:column, if_test_atom:m, if_test_atom:row, if_test_atom:v, if_without_else (-> +2), index:column, index:row, index_shape:2, loaded_variable:column, loaded_variable:m, loaded_variable:row, loaded_variable:v, nested_index, node:Compare, node:If (-> +2), node:Name, node:Subscript
                position = (row, column) # assignment, assignment_lhs_identifier:position, assignment_rhs_atom:column, assignment_rhs_atom:row, if_then_branch (-> +1), literal:Tuple, loaded_variable:column, loaded_variable:row, node:Assign, node:Name, node:Tuple, single_assignment:position
                raise BreakOuterLoop # loaded_variable:BreakOuterLoop, node:Name, node:Raise, raise:BreakOuterLoop
except BreakOuterLoop: # except:BreakOuterLoop, loaded_variable:BreakOuterLoop, node:ExceptHandler (-> +1), node:Name
    pass # no_operation, node:Pass

# ----------------------------------------------------------------------------------------
# 043.2733-break-outer-loop.py
# ----------------------------------------------------------------------------------------
def loop_breaking(m, v): # function:loop_breaking (-> +5), function_line_count:6 (-> +5), function_parameter:m, function_parameter:v, function_parameter_flavor:arg, function_returning_something:loop_breaking (-> +5), impure_function:loop_breaking (-> +5), local_scope:i (-> +5), local_scope:j (-> +5), local_scope:m (-> +5), local_scope:row (-> +5), local_scope:v (-> +5), local_scope:value (-> +5), node:FunctionDef (-> +5), node:arg, procedural_style (-> +6), scope:i (-> +5), scope:j (-> +5), scope:m (-> +5), scope:row (-> +5), scope:v (-> +5), scope:value (-> +5), variety:2 (-> +6), whole_span:7 (-> +6)
    for i, row in enumerate(m): # argument:m, external_free_call:enumerate, for:i (-> +3), for:row (-> +3), for_indexes_elements:i (-> +3), free_call:enumerate, iteration_variable:i, iteration_variable:row, literal:Tuple, loaded_variable:m, loop:for (-> +3), loop_with_early_exit:for:return (-> +3), loop_with_return:for (-> +3), node:Call, node:For (-> +3), node:Name, node:Tuple
        for j, value in enumerate(row): # argument:row, external_free_call:enumerate, for:j (-> +2), for:value (-> +2), for_indexes_elements:j (-> +2), free_call:enumerate, iteration_variable:j, iteration_variable:value, literal:Tuple, loaded_variable:row, loop:for (-> +2), loop_with_early_exit:for:return (-> +2), loop_with_return:for (-> +2), nested_for:1 (-> +2), node:Call, node:For (-> +2), node:Name, node:Tuple
            if value == v: # comparison_operator:Eq, if (-> +1), if_test_atom:v, if_test_atom:value, if_without_else (-> +1), loaded_variable:v, loaded_variable:value, node:Compare, node:If (-> +1), node:Name
                return (i, j) # if_then_branch, literal:Tuple, loaded_variable:i, loaded_variable:j, node:Name, node:Return, node:Tuple, return
    return None # literal:None, node:NameConstant, node:Return, return:None
print(loop_breaking(([1, 2, 3], [4, 5, 6], [7, 8, 9]), 6)) # argument:, argument:6, composition, external_free_call:print, free_call:loop_breaking, free_call:print, free_call_without_result:print, internal_free_call:loop_breaking, literal:1, literal:2, literal:3, literal:4, literal:5, literal:6, literal:7, literal:8, literal:9, literal:List, literal:Tuple, magic_number:3, magic_number:4, magic_number:5, magic_number:6, magic_number:7, magic_number:8, magic_number:9, node:Call, node:Expr, node:List, node:Name, node:Num, node:Tuple

# ----------------------------------------------------------------------------------------
# 044.0190-insert-element-in-list.py
# ----------------------------------------------------------------------------------------
s.insert(i, x) # argument:i, argument:x, flat_style, imperative_style, loaded_variable:i, loaded_variable:s, loaded_variable:x, member_call:s:insert, member_call_method:insert, member_call_object:s, node:Attribute, node:Call, node:Expr, node:Name, one_liner_style, update:s:i, update:s:x, update_by_member_call:s:i, update_by_member_call:s:x, update_by_member_call_with:insert, update_with:insert, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 045.0570-pause-execution-for-5-seconds.py
# ----------------------------------------------------------------------------------------
import time # flat_style (-> +1), imperative_style (-> +1), import:time, import_module:time, node:Import, one_liner_style (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
time.sleep(5) # argument:5, literal:5, loaded_variable:time, magic_number:5, member_call:time:sleep, member_call_method:sleep, member_call_object:time, node:Attribute, node:Call, node:Expr, node:Name, node:Num

# ----------------------------------------------------------------------------------------
# 046.0191-extract-beginning-of-string-prefix.py
# ----------------------------------------------------------------------------------------
t = s[:5] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:5, assignment_rhs_atom:s, flat_style, global_scope:t, imperative_style, literal:5, loaded_variable:s, magic_number:5, node:Assign, node:Name, node:Num, node:Slice, node:Subscript, one_liner_style, scope:t, single_assignment:t, slice::5:, slice_lower:, slice_step:, slice_upper:5, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 047.0198-extract-string-suffix.py
# ----------------------------------------------------------------------------------------
t = s[-5:] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:-5, assignment_rhs_atom:s, flat_style, global_scope:t, imperative_style, literal:-5, loaded_variable:s, magic_number:-5, node:Assign, node:Name, node:Num, node:Slice, node:Subscript, one_liner_style, scope:t, single_assignment:t, slice:-5::, slice_lower:-5, slice_step:, slice_upper:, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 048.0210-multi-line-string-literal.py
# ----------------------------------------------------------------------------------------
s = """Huey # assignment, assignment_lhs_identifier:s, flat_style, global_scope:s, imperative_style, literal:Str, node:Assign, node:Name, node:Str, one_liner_style, scope:s, single_assignment:s, special_literal_string:Huey\nDewey\nLouie, variety:1, whole_span:1
Dewey
Louie"""

# ----------------------------------------------------------------------------------------
# 049.0242-split-a-space-separated-string.py
# ----------------------------------------------------------------------------------------
chunks = s.split() # assignment:split, assignment_lhs_identifier:chunks, assignment_rhs_atom:s, flat_style, global_scope:chunks, imperative_style, loaded_variable:s, member_call_method:split, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:chunks, single_assignment:chunks, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 050.0572-make-an-infinite-loop.py
# ----------------------------------------------------------------------------------------
while True: # imperative_style (-> +1), infinite_while (-> +1), literal:True, loop:while (-> +1), loop_with_late_exit:while (-> +1), node:NameConstant, node:While (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
    pass # no_operation, node:Pass

# ----------------------------------------------------------------------------------------
# 051.0230-check-if-map-contains-key.py
# ----------------------------------------------------------------------------------------
k in m # comparison_operator:In, flat_style, imperative_style, loaded_variable:k, loaded_variable:m, node:Compare, node:Expr, node:Name, one_liner_style, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 052.0666-check-if-map-contains-value.py
# ----------------------------------------------------------------------------------------
v in map.values() # comparison_operator:In, flat_style, imperative_style, loaded_variable:map, loaded_variable:v, member_call_method:values, node:Attribute, node:Call, node:Compare, node:Expr, node:Name, one_liner_style, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 053.0240-join-a-list-of-strings.py
# ----------------------------------------------------------------------------------------
y = ", ".join(x) # argument:x, assignment:join, assignment_lhs_identifier:y, assignment_rhs_atom:x, flat_style, global_scope:y, imperative_style, literal:Str, loaded_variable:x, member_call_method:join, node:Assign, node:Attribute, node:Call, node:Name, node:Str, one_liner_style, scope:y, single_assignment:y, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 053.1933-join-a-list-of-strings.py
# ----------------------------------------------------------------------------------------
y = ", ".join(map(str, x)) # argument:, argument:str, argument:x, assignment:join, assignment_lhs_identifier:y, assignment_rhs_atom:str, assignment_rhs_atom:x, composition, external_free_call:map, flat_style, free_call:map, global_scope:y, imperative_style, literal:Str, loaded_variable:str, loaded_variable:x, member_call_method:join, node:Assign, node:Attribute, node:Call, node:Name, node:Str, one_liner_style, scope:y, single_assignment:y, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 054.0241-compute-sum-of-integers.py
# ----------------------------------------------------------------------------------------
s = sum(x) # argument:x, assignment:sum, assignment_lhs_identifier:s, assignment_rhs_atom:x, external_free_call:sum, flat_style, free_call:sum, global_scope:s, imperative_style, loaded_variable:x, node:Assign, node:Call, node:Name, one_liner_style, scope:s, single_assignment:s, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 055.0575-convert-integer-to-string.py
# ----------------------------------------------------------------------------------------
s = str(i) # argument:i, assignment:str, assignment_lhs_identifier:s, assignment_rhs_atom:i, external_free_call:str, flat_style, free_call:str, global_scope:s, imperative_style, loaded_variable:i, node:Assign, node:Call, node:Name, one_liner_style, scope:s, single_assignment:s, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 056.1424-launch-1000-parallel-tasks-and-wait-for-completion.py
# ----------------------------------------------------------------------------------------
from multiprocessing import Pool # import:multiprocessing:Pool, import_module:multiprocessing, import_name:Pool, node:ImportFrom, procedural_style (-> +5), variety:3 (-> +5), whole_span:6 (-> +5)
def f(i): # function:f (-> +1), function_line_count:2 (-> +1), function_parameter:i, function_parameter_flavor:arg, function_returning_nothing:f (-> +1), local_scope:i (-> +1), node:FunctionDef (-> +1), node:arg, scope:i (-> +1)
    i * i # binary_operator:Mult, loaded_variable:i, multiplication_operator, node:BinOp, node:Expr, node:Name
with Pool(processes) as p: # argument:processes, external_free_call:Pool, free_call:Pool, loaded_variable:processes, node:Call, node:Name, node:With (-> +1), node:withitem
    p.map(func=f, iterable=range(1, 1001)) # argument:, argument:1, argument:1001, argument:f, external_free_call:range, free_call:range, keyword_argument:func, keyword_argument:iterable, literal:1, literal:1001, loaded_variable:f, loaded_variable:p, magic_number:1001, member_call:p:map, member_call_method:map, member_call_object:p, node:Attribute, node:Call, node:Expr, node:Name, node:Num, node:keyword, range:1:1001
print("Finished") # argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 057.0260-filter-list.py
# ----------------------------------------------------------------------------------------
y = filter(p, x) # argument:p, argument:x, assignment:filter, assignment_lhs_identifier:y, assignment_rhs_atom:p, assignment_rhs_atom:x, external_free_call:filter, flat_style, free_call:filter, global_scope:y, imperative_style, loaded_variable:p, loaded_variable:x, node:Assign, node:Call, node:Name, one_liner_style, scope:y, single_assignment:y, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 057.3173-filter-list.py
# ----------------------------------------------------------------------------------------
y = [element for element in x if p(element)] # argument:element, assignment, assignment_lhs_identifier:y, assignment_rhs_atom:element, assignment_rhs_atom:x, comprehension:List, comprehension_for_count:1, external_free_call:p, filtered_comprehension, flat_style, free_call:p, imperative_style, iteration_variable:element, loaded_variable:element, loaded_variable:x, local_scope:element, local_scope:y, node:Assign, node:Call, node:ListComp, node:Name, node:comprehension, one_liner_style, scope:element, scope:y, single_assignment:y, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 058.0665-extract-file-content-to-a-string.py
# ----------------------------------------------------------------------------------------
lines = open(f).read() # argument:f, assignment:read, assignment_lhs_identifier:lines, assignment_rhs_atom:f, external_free_call:open, flat_style, free_call:open, global_scope:lines, imperative_style, loaded_variable:f, member_call_method:read, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:lines, single_assignment:lines, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 059.0668-write-to-standard-error-stream.py
# ----------------------------------------------------------------------------------------
import sys # flat_style (-> +1), imperative_style (-> +1), import:sys, import_module:sys, node:Import, one_liner_style (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
print(x, "is negative", file=sys.stderr) # argument:, argument:x, external_free_call:print, free_call:print, free_call_with_keyword_argument:print:file, free_call_without_result:print, keyword_argument:file, literal:Str, loaded_variable:sys, loaded_variable:x, node:Attribute, node:Call, node:Expr, node:Name, node:Str, node:keyword, value_attr:stderr

# ----------------------------------------------------------------------------------------
# 060.1084-read-command-line-argument.py
# ----------------------------------------------------------------------------------------
import sys # flat_style (-> +1), global_scope:x (-> +1), imperative_style (-> +1), import:sys, import_module:sys, node:Import, one_liner_style (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
x = sys.argv[1] # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:1, assignment_rhs_atom:sys, index:1, literal:1, loaded_variable:sys, node:Assign, node:Attribute, node:Name, node:Num, node:Subscript, single_assignment:x, value_attr:argv

# ----------------------------------------------------------------------------------------
# 061.0576-get-current-date.py
# ----------------------------------------------------------------------------------------
import datetime # flat_style (-> +1), global_scope:d (-> +1), imperative_style (-> +1), import:datetime, import_module:datetime, node:Import, one_liner_style (-> +1), scope:d (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
d = datetime.datetime.now() # assignment:now, assignment_lhs_identifier:d, assignment_rhs_atom:datetime, loaded_variable:datetime, member_call_method:now, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:d, value_attr:datetime

# ----------------------------------------------------------------------------------------
# 062.1091-find-substring-position.py
# ----------------------------------------------------------------------------------------
i = x.find(y) # argument:y, assignment:find, assignment_lhs_identifier:i, assignment_rhs_atom:x, assignment_rhs_atom:y, flat_style, global_scope:i, imperative_style, loaded_variable:x, loaded_variable:y, member_call_method:find, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:i, single_assignment:i, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 063.1088-replace-fragment-of-a-string.py
# ----------------------------------------------------------------------------------------
x2 = x.replace(y, z) # argument:y, argument:z, assignment:replace, assignment_lhs_identifier:x2, assignment_rhs_atom:x, assignment_rhs_atom:y, assignment_rhs_atom:z, flat_style, global_scope:x2, imperative_style, loaded_variable:x, loaded_variable:y, loaded_variable:z, member_call_method:replace, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:x2, single_assignment:x2, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 064.0274-big-integer--value-3-power-247.py
# ----------------------------------------------------------------------------------------
x = 3 ** 247 # assignment:Pow, assignment_lhs_identifier:x, assignment_rhs_atom:247, assignment_rhs_atom:3, binary_operator:Pow, flat_style, global_scope:x, imperative_style, literal:247, literal:3, magic_number:247, magic_number:3, node:Assign, node:BinOp, node:Name, node:Num, one_liner_style, scope:x, single_assignment:x, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 065.1085-format-decimal-number.py
# ----------------------------------------------------------------------------------------
s = "{:.1%}".format(x) # argument:x, assignment:format, assignment_lhs_identifier:s, assignment_rhs_atom:x, flat_style, global_scope:s, imperative_style, literal:Str, loaded_variable:x, member_call_method:format, node:Assign, node:Attribute, node:Call, node:Name, node:Str, one_liner_style, scope:s, single_assignment:s, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 066.0672-big-integer-exponentiation.py
# ----------------------------------------------------------------------------------------
z = x ** n # assignment:Pow, assignment_lhs_identifier:z, assignment_rhs_atom:n, assignment_rhs_atom:x, binary_operator:Pow, flat_style, global_scope:z, imperative_style, loaded_variable:n, loaded_variable:x, node:Assign, node:BinOp, node:Name, one_liner_style, scope:z, single_assignment:z, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 067.1426-binomial-coefficient-n-choose-k.py
# ----------------------------------------------------------------------------------------
import math # functional_style (-> +2), import:math, import_module:math, node:Import, one_liner_style (-> +2), variety:1 (-> +2), whole_span:3 (-> +2)
def binom(n, k): # function:binom (-> +1), function_line_count:2 (-> +1), function_parameter:k, function_parameter:n, function_parameter_flavor:arg, function_returning_something:binom (-> +1), local_scope:k (-> +1), local_scope:n (-> +1), node:FunctionDef (-> +1), node:arg, pure_function:binom (-> +1), scope:k (-> +1), scope:n (-> +1)
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k) # argument:, argument:k, argument:n, binary_operator:FloorDiv, binary_operator:Sub, loaded_variable:k, loaded_variable:math, loaded_variable:n, member_call_method:factorial, node:Attribute, node:BinOp, node:Call, node:Name, node:Return, return

# ----------------------------------------------------------------------------------------
# 068.2271-create-a-bitset.py
# ----------------------------------------------------------------------------------------
from __future__ import division # flat_style (-> +2), global_scope:x (-> +2), imperative_style (-> +2), import:__future__:division, import_module:__future__, import_name:division, node:ImportFrom, one_liner_style (-> +2), scope:x (-> +2), variety:2 (-> +2), whole_span:3 (-> +2)
import math # import:math, import_module:math, node:Import
x = bytearray(int(math.ceil(n / 8.0))) # argument:, assignment:bytearray, assignment_lhs_identifier:x, assignment_rhs_atom:8.0, assignment_rhs_atom:math, assignment_rhs_atom:n, binary_operator:Div, composition, external_free_call:bytearray, external_free_call:int, free_call:bytearray, free_call:int, literal:8.0, loaded_variable:math, loaded_variable:n, magic_number:8.0, member_call_method:ceil, node:Assign, node:Attribute, node:BinOp, node:Call, node:Name, node:Num, single_assignment:x

# ----------------------------------------------------------------------------------------
# 069.1086-seed-random-generator.py
# ----------------------------------------------------------------------------------------
import random # flat_style (-> +1), global_scope:rand (-> +1), imperative_style (-> +1), import:random, import_module:random, node:Import, one_liner_style (-> +1), scope:rand (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
rand = random.Random(s) # argument:s, assignment:Random, assignment_lhs_identifier:rand, assignment_rhs_atom:random, assignment_rhs_atom:s, loaded_variable:random, loaded_variable:s, member_call_method:Random, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:rand

# ----------------------------------------------------------------------------------------
# 070.1087-use-clock-as-random-generator-seed.py
# ----------------------------------------------------------------------------------------
import random # flat_style (-> +1), global_scope:rand (-> +1), imperative_style (-> +1), import:random, import_module:random, node:Import, one_liner_style (-> +1), scope:rand (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
rand = random.Random() # assignment:Random, assignment_lhs_identifier:rand, assignment_rhs_atom:random, loaded_variable:random, member_call_method:Random, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:rand

# ----------------------------------------------------------------------------------------
# 071.0379-echo-program-implementation.py
# ----------------------------------------------------------------------------------------
import sys # flat_style (-> +1), imperative_style (-> +1), import:sys, import_module:sys, node:Import, one_liner_style (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
print(" ".join(sys.argv[1:])) # argument:, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:1, literal:Str, loaded_variable:sys, member_call_method:join, node:Attribute, node:Call, node:Expr, node:Name, node:Num, node:Slice, node:Str, node:Subscript, slice:1::, slice_lower:1, slice_step:, slice_upper:, value_attr:argv

# ----------------------------------------------------------------------------------------
# 073.0673-create-a-factory.py
# ----------------------------------------------------------------------------------------
def fact(a_class, str_): # function:fact (-> +2), function_line_count:3 (-> +2), function_parameter:a_class, function_parameter:str_, function_parameter_flavor:arg, function_returning_something:fact (-> +2), functional_style (-> +2), higher_order_function:a_class (-> +2), local_scope:a_class (-> +2), local_scope:str_ (-> +2), node:FunctionDef (-> +2), node:arg, pure_function:fact (-> +2), scope:a_class (-> +2), scope:str_ (-> +2), variety:1 (-> +2), whole_span:3 (-> +2)
    if issubclass(a_class, Parent): # argument:Parent, argument:a_class, external_free_call:issubclass, free_call:issubclass, if (-> +1), if_test_atom:Parent, if_test_atom:a_class, if_without_else (-> +1), loaded_variable:Parent, loaded_variable:a_class, node:Call, node:If (-> +1), node:Name
        return a_class(str_) # argument:str_, external_free_call:a_class, free_call:a_class, free_tail_call:a_class, if_then_branch, loaded_variable:str_, node:Call, node:Name, node:Return, return

# ----------------------------------------------------------------------------------------
# 074.0674-compute-gcd.py
# ----------------------------------------------------------------------------------------
from fractions import gcd # flat_style (-> +1), global_scope:x (-> +1), imperative_style (-> +1), import:fractions:gcd, import_module:fractions, import_name:gcd, node:ImportFrom, one_liner_style (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
x = gcd(a, b) # argument:a, argument:b, assignment:gcd, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:b, external_free_call:gcd, free_call:gcd, loaded_variable:a, loaded_variable:b, node:Assign, node:Call, node:Name, single_assignment:x

# ----------------------------------------------------------------------------------------
# 075.0675-compute-lcm.py
# ----------------------------------------------------------------------------------------
from fractions import gcd # flat_style (-> +1), global_scope:x (-> +1), imperative_style (-> +1), import:fractions:gcd, import_module:fractions, import_name:gcd, node:ImportFrom, one_liner_style (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
x = (a * b) // gcd(a, b) # argument:a, argument:b, assignment:FloorDiv, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:FloorDiv, binary_operator:Mult, external_free_call:gcd, free_call:gcd, loaded_variable:a, loaded_variable:b, multiplication_operator, node:Assign, node:BinOp, node:Call, node:Name, single_assignment:x

# ----------------------------------------------------------------------------------------
# 076.1083-binary-digits-from-an-integer.py
# ----------------------------------------------------------------------------------------
s = "{:b}".format(x) # argument:x, assignment:format, assignment_lhs_identifier:s, assignment_rhs_atom:x, flat_style, global_scope:s, imperative_style, literal:Str, loaded_variable:x, member_call_method:format, node:Assign, node:Attribute, node:Call, node:Name, node:Str, one_liner_style, scope:s, single_assignment:s, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 077.1093-complex-number.py
# ----------------------------------------------------------------------------------------
x = 3j - 2 # assignment:Sub, assignment_lhs_identifier:x, assignment_rhs_atom:2, assignment_rhs_atom:3j, binary_operator:Sub, flat_style (-> +1), global_scope:x (-> +1), global_scope:y (-> +1), imperative_style (-> +1), literal:2, literal:3j, node:Assign, node:BinOp, node:Name, node:Num, scope:x (-> +1), scope:y (-> +1), single_assignment:x, variety:1 (-> +1), whole_span:2 (-> +1)
y = x * 1j # assignment:Mult, assignment_lhs_identifier:y, assignment_rhs_atom:1j, assignment_rhs_atom:x, binary_operator:Mult, literal:1j, loaded_variable:x, multiplication_operator, node:Assign, node:BinOp, node:Name, node:Num, single_assignment:y

# ----------------------------------------------------------------------------------------
# 078.1089-do-while-loop.py
# ----------------------------------------------------------------------------------------
while True: # imperative_style (-> +3), infinite_while (-> +3), literal:True, loop:while (-> +3), loop_with_break:while (-> +3), loop_with_early_exit:while:break (-> +3), node:NameConstant, node:While (-> +3), variety:4 (-> +3), whole_span:4 (-> +3)
    do_something() # external_free_call:do_something, free_call:do_something, free_call_no_arguments:do_something, free_call_without_result:do_something, node:Call, node:Expr, node:Name
    if not c: # if (-> +1), if_test_atom:c, if_without_else (-> +1), loaded_variable:c, node:If (-> +1), node:Name, node:UnaryOp, unary_operator:Not
        break # if_then_branch, node:Break

# ----------------------------------------------------------------------------------------
# 079.1090-convert-integer-to-floating-point-number.py
# ----------------------------------------------------------------------------------------
y = float(x) # argument:x, assignment:float, assignment_lhs_identifier:y, assignment_rhs_atom:x, external_free_call:float, flat_style, free_call:float, global_scope:y, imperative_style, loaded_variable:x, node:Assign, node:Call, node:Name, one_liner_style, scope:y, single_assignment:y, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 080.1092-truncate-floating-point-number-to-integer.py
# ----------------------------------------------------------------------------------------
y = int(x) # argument:x, assignment:int, assignment_lhs_identifier:y, assignment_rhs_atom:x, external_free_call:int, flat_style, free_call:int, global_scope:y, imperative_style, loaded_variable:x, node:Assign, node:Call, node:Name, one_liner_style, scope:y, single_assignment:y, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 081.2270-round-floating-point-number-to-integer.py
# ----------------------------------------------------------------------------------------
y = int(x + 0.5) # addition_operator, argument:, assignment:int, assignment_lhs_identifier:y, assignment_rhs_atom:0.5, assignment_rhs_atom:x, binary_operator:Add, external_free_call:int, flat_style, free_call:int, global_scope:y, imperative_style, literal:0.5, loaded_variable:x, magic_number:0.5, node:Assign, node:BinOp, node:Call, node:Name, node:Num, one_liner_style, scope:y, single_assignment:y, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 082.1096-count-substring-occurrences.py
# ----------------------------------------------------------------------------------------
count = s.count(t) # argument:t, assignment:count, assignment_lhs_identifier:count, assignment_rhs_atom:s, assignment_rhs_atom:t, flat_style, global_scope:count, imperative_style, loaded_variable:s, loaded_variable:t, member_call_method:count, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:count, single_assignment:count, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 083.1805-regex-with-character-repetition.py
# ----------------------------------------------------------------------------------------
import re # flat_style (-> +1), global_scope:r (-> +1), imperative_style (-> +1), import:re, import_module:re, node:Import, one_liner_style (-> +1), scope:r (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
r = re.compile(r"htt+p") # argument:, assignment:compile, assignment_lhs_identifier:r, assignment_rhs_atom:re, literal:Str, loaded_variable:re, member_call_method:compile, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:r

# ----------------------------------------------------------------------------------------
# 084.1940-count-bits-set-in-integer-binary-representation.py
# ----------------------------------------------------------------------------------------
c = bin(i).count("1") # argument:, argument:i, assignment:count, assignment_lhs_identifier:c, assignment_rhs_atom:i, external_free_call:bin, flat_style, free_call:bin, global_scope:c, imperative_style, literal:Str, loaded_variable:i, member_call_method:count, node:Assign, node:Attribute, node:Call, node:Name, node:Str, one_liner_style, scope:c, single_assignment:c, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 085.1003-check-if-integer-addition-will-overflow.py
# ----------------------------------------------------------------------------------------
def adding_will_overflow(x, y): # function:adding_will_overflow (-> +1), function_line_count:2 (-> +1), function_parameter:x, function_parameter:y, function_parameter_flavor:arg, function_returning_something:adding_will_overflow (-> +1), functional_style (-> +1), local_scope:x (-> +1), local_scope:y (-> +1), node:FunctionDef (-> +1), node:arg, one_liner_style (-> +1), pure_function:adding_will_overflow (-> +1), scope:x (-> +1), scope:y (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    return False # literal:False, node:NameConstant, node:Return, return:False

# ----------------------------------------------------------------------------------------
# 086.1004-check-if-integer-multiplication-will-overflow.py
# ----------------------------------------------------------------------------------------
def multiplyWillOverflow(x, y): # function:multiplyWillOverflow (-> +1), function_line_count:2 (-> +1), function_parameter:x, function_parameter:y, function_parameter_flavor:arg, function_returning_something:multiplyWillOverflow (-> +1), functional_style (-> +1), local_scope:x (-> +1), local_scope:y (-> +1), node:FunctionDef (-> +1), node:arg, one_liner_style (-> +1), pure_function:multiplyWillOverflow (-> +1), scope:x (-> +1), scope:y (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    return False # literal:False, node:NameConstant, node:Return, return:False

# ----------------------------------------------------------------------------------------
# 087.1139-stop-program.py
# ----------------------------------------------------------------------------------------
import sys # flat_style (-> +1), imperative_style (-> +1), import:sys, import_module:sys, node:Import, one_liner_style (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
sys.exit(1) # argument:1, literal:1, loaded_variable:sys, member_call:sys:exit, member_call_method:exit, member_call_object:sys, node:Attribute, node:Call, node:Expr, node:Name, node:Num

# ----------------------------------------------------------------------------------------
# 088.2143-allocate-1m-bytes.py
# ----------------------------------------------------------------------------------------
buf = bytearray(1000000) # argument:1000000, assignment:bytearray, assignment_lhs_identifier:buf, assignment_rhs_atom:1000000, external_free_call:bytearray, flat_style, free_call:bytearray, global_scope:buf, imperative_style, literal:1000000, magic_number:1000000, node:Assign, node:Call, node:Name, node:Num, one_liner_style, scope:buf, single_assignment:buf, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 089.1097-handle-invalid-argument.py
# ----------------------------------------------------------------------------------------
raise ValueError("x is invalid") # argument:, external_free_call:ValueError, flat_style, free_call:ValueError, imperative_style, literal:Str, node:Call, node:Name, node:Raise, node:Str, one_liner_style, raise:ValueError, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 090.1099-read-only-outside.py
# ----------------------------------------------------------------------------------------
class Foo(object): # class:Foo (-> +5), class_method_count:2 (-> +5), loaded_variable:object, node:ClassDef (-> +5), node:Name, object_oriented_style (-> +5), variety:4 (-> +5), whole_span:6 (-> +5)
    def __init__(self): # function:__init__ (-> +1), function_line_count:2 (-> +1), function_parameter:self, function_parameter_flavor:arg, function_returning_nothing:__init__ (-> +1), instance_method:__init__ (-> +1), local_scope:self (-> +1), method:__init__ (-> +1), node:FunctionDef (-> +1), node:arg, scope:self (-> +1)
        self._x = 0 # assignment:0, assignment_lhs_identifier:self, assignment_rhs_atom:0, literal:0, loaded_variable:self, node:Assign, node:Attribute, node:Name, node:Num
    @property # function_decorator:property (-> +2), loaded_variable:property, node:Name
    def x(self): # decorated_function:x (-> +1), function:x (-> +1), function_line_count:2 (-> +1), function_parameter:self, function_parameter_flavor:arg, function_returning_something:x (-> +1), instance_method:x (-> +1), local_scope:self (-> +1), method:x (-> +1), node:FunctionDef (-> +1), node:arg, scope:self (-> +1)
        return self._x # loaded_variable:self, node:Attribute, node:Name, node:Return, return, value_attr:_x

# ----------------------------------------------------------------------------------------
# 091.1098-load-json-file-into-struct.py
# ----------------------------------------------------------------------------------------
import json # flat_style (-> +2), global_scope:x (-> +2), imperative_style (-> +2), import:json, import_module:json, node:Import, scope:x (-> +2), variety:2 (-> +2), whole_span:3 (-> +2)
with open("data.json", "r") as input: # argument:, external_free_call:open, free_call:open, literal:Str, node:Call, node:Name, node:Str, node:With (-> +1), node:withitem
    x = json.load(input) # argument:input, assignment:load, assignment_lhs_identifier:x, assignment_rhs_atom:input, assignment_rhs_atom:json, loaded_variable:input, loaded_variable:json, member_call_method:load, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:x

# ----------------------------------------------------------------------------------------
# 092.1100-save-object-into-json-file.py
# ----------------------------------------------------------------------------------------
import json # flat_style (-> +2), imperative_style (-> +2), import:json, import_module:json, node:Import, variety:2 (-> +2), whole_span:3 (-> +2)
with open("data.json", "w") as output: # argument:, external_free_call:open, free_call:open, literal:Str, node:Call, node:Name, node:Str, node:With (-> +1), node:withitem
    json.dump(x, output) # argument:output, argument:x, loaded_variable:json, loaded_variable:output, loaded_variable:x, member_call:json:dump, member_call_method:dump, member_call_object:json, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 093.1082-pass-a-runnable-procedure-as-parameter.py
# ----------------------------------------------------------------------------------------
from __future__ import print_function # functional_style (-> +2), import:__future__:print_function, import_module:__future__, import_name:print_function, node:ImportFrom, one_liner_style (-> +2), variety:3 (-> +2), whole_span:3 (-> +2)
def control(f): # function:control (-> +1), function_line_count:2 (-> +1), function_parameter:f, function_parameter_flavor:arg, function_returning_something:control (-> +1), higher_order_function:f (-> +1), local_scope:f (-> +1), node:FunctionDef (-> +1), node:arg, pure_function:control (-> +1), scope:f (-> +1)
    return f() # external_free_call:f, free_call:f, free_call_no_arguments:f, free_tail_call:f, node:Call, node:Name, node:Return, return

# ----------------------------------------------------------------------------------------
# 094.1101-print-type-of-variable.py
# ----------------------------------------------------------------------------------------
print(type(x)) # argument:, argument:x, composition, external_free_call:print, external_free_call:type, flat_style, free_call:print, free_call:type, free_call_without_result:print, imperative_style, loaded_variable:x, node:Call, node:Expr, node:Name, one_liner_style, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 094.1864-print-type-of-variable.py
# ----------------------------------------------------------------------------------------
print(x.__class__) # argument:, external_free_call:print, flat_style, free_call:print, free_call_without_result:print, imperative_style, loaded_variable:x, node:Attribute, node:Call, node:Expr, node:Name, one_liner_style, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 095.2140-get-file-size.py
# ----------------------------------------------------------------------------------------
import os # flat_style (-> +1), global_scope:x (-> +1), imperative_style (-> +1), import:os, import_module:os, node:Import, one_liner_style (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
x = os.path.getsize(path) # argument:path, assignment:getsize, assignment_lhs_identifier:x, assignment_rhs_atom:os, assignment_rhs_atom:path, loaded_variable:os, loaded_variable:path, member_call_method:getsize, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:x, value_attr:path

# ----------------------------------------------------------------------------------------
# 096.1094-check-string-prefix.py
# ----------------------------------------------------------------------------------------
b = s.startswith(prefix) # argument:prefix, assignment:startswith, assignment_lhs_identifier:b, assignment_rhs_atom:prefix, assignment_rhs_atom:s, flat_style, global_scope:b, imperative_style, loaded_variable:prefix, loaded_variable:s, member_call_method:startswith, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:b, single_assignment:b, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 097.1095-check-string-suffix.py
# ----------------------------------------------------------------------------------------
b = s.endswith(suffix) # argument:suffix, assignment:endswith, assignment_lhs_identifier:b, assignment_rhs_atom:s, assignment_rhs_atom:suffix, flat_style, global_scope:b, imperative_style, loaded_variable:s, loaded_variable:suffix, member_call_method:endswith, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:b, single_assignment:b, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 098.2142-epoch-seconds-to-date-object.py
# ----------------------------------------------------------------------------------------
import datetime # flat_style (-> +1), global_scope:d (-> +1), imperative_style (-> +1), import:datetime, import_module:datetime, node:Import, one_liner_style (-> +1), scope:d (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
d = datetime.date.fromtimestamp(ts) # argument:ts, assignment:fromtimestamp, assignment_lhs_identifier:d, assignment_rhs_atom:datetime, assignment_rhs_atom:ts, loaded_variable:datetime, loaded_variable:ts, member_call_method:fromtimestamp, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:d, value_attr:date

# ----------------------------------------------------------------------------------------
# 099.1429-format-date-yyyy-mm-dd.py
# ----------------------------------------------------------------------------------------
from datetime import date # flat_style (-> +2), global_scope:d (-> +2), global_scope:x (-> +2), imperative_style (-> +2), import:datetime:date, import_module:datetime, import_name:date, node:ImportFrom, scope:d (-> +2), scope:x (-> +2), variety:1 (-> +2), whole_span:3 (-> +2)
d = date(2016, 9, 28) # argument:2016, argument:28, argument:9, assignment:date, assignment_lhs_identifier:d, assignment_rhs_atom:2016, assignment_rhs_atom:28, assignment_rhs_atom:9, external_free_call:date, free_call:date, literal:2016, literal:28, literal:9, magic_number:2016, magic_number:28, magic_number:9, node:Assign, node:Call, node:Name, node:Num, single_assignment:d
x = d.strftime("%Y-%m-%d") # argument:, assignment:strftime, assignment_lhs_identifier:x, assignment_rhs_atom:d, literal:Str, loaded_variable:d, member_call_method:strftime, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:x

# ----------------------------------------------------------------------------------------
# 099.2693-format-date-yyyy-mm-dd.py
# ----------------------------------------------------------------------------------------
from datetime import date # flat_style (-> +2), global_scope:d (-> +2), global_scope:x (-> +2), imperative_style (-> +2), import:datetime:date, import_module:datetime, import_name:date, node:ImportFrom, scope:d (-> +2), scope:x (-> +2), variety:1 (-> +2), whole_span:3 (-> +2)
d = date.today() # assignment:today, assignment_lhs_identifier:d, assignment_rhs_atom:date, loaded_variable:date, member_call_method:today, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:d
x = d.isoformat() # assignment:isoformat, assignment_lhs_identifier:x, assignment_rhs_atom:d, loaded_variable:d, member_call_method:isoformat, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:x

# ----------------------------------------------------------------------------------------
# 100.1142-sort-by-a-comparator.py
# ----------------------------------------------------------------------------------------
items.sort(c) # argument:c, flat_style, imperative_style, loaded_variable:c, loaded_variable:items, member_call:items:sort, member_call_method:sort, member_call_object:items, node:Attribute, node:Call, node:Expr, node:Name, one_liner_style, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 101.2172-load-from-http-get-request-into-a-string.py
# ----------------------------------------------------------------------------------------
import urllib.request # flat_style (-> +2), global_scope:s (-> +2), imperative_style (-> +2), import:urllib.request, import_module:urllib.request, node:Import, scope:s (-> +2), variety:2 (-> +2), whole_span:3 (-> +2)
with urllib.request.urlopen(u) as f: # argument:u, loaded_variable:u, loaded_variable:urllib, member_call_method:urlopen, node:Attribute, node:Call, node:Name, node:With (-> +1), node:withitem, value_attr:request
    s = f.read() # assignment:read, assignment_lhs_identifier:s, assignment_rhs_atom:f, loaded_variable:f, member_call_method:read, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:s

# ----------------------------------------------------------------------------------------
# 102.2173-load-from-http-get-request-into-a-file.py
# ----------------------------------------------------------------------------------------
import urllib # flat_style (-> +1), global_scope:filename (-> +1), global_scope:headers (-> +1), imperative_style (-> +1), import:urllib, import_module:urllib, node:Import, one_liner_style (-> +1), scope:filename (-> +1), scope:headers (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
filename, headers = urllib.request.urlretrieve(u, "result.txt") # argument:, argument:u, assignment:urlretrieve, assignment_lhs_identifier:filename, assignment_lhs_identifier:headers, assignment_rhs_atom:u, assignment_rhs_atom:urllib, literal:Str, literal:Tuple, loaded_variable:u, loaded_variable:urllib, member_call_method:urlretrieve, node:Assign, node:Attribute, node:Call, node:Name, node:Str, node:Tuple, parallel_assignment:2, value_attr:request

# ----------------------------------------------------------------------------------------
# 103.2276-load-xml-file-into-struct.py
# ----------------------------------------------------------------------------------------
import lxml.etree # flat_style (-> +1), global_scope:x (-> +1), imperative_style (-> +1), import:lxml.etree, import_module:lxml.etree, node:Import, one_liner_style (-> +1), scope:x (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
x = lxml.etree.parse("data.xml") # argument:, assignment:parse, assignment_lhs_identifier:x, assignment_rhs_atom:lxml, literal:Str, loaded_variable:lxml, member_call_method:parse, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:x, value_attr:etree

# ----------------------------------------------------------------------------------------
# 104.3264-save-object-into-xml-file.py
# ----------------------------------------------------------------------------------------
import pyxser as pyx # global_scope:a (-> +11), global_scope:b (-> +11), global_scope:c (-> +11), global_scope:ser (-> +11), global_scope:tst (-> +11), import:pyxser, import_module:pyxser, node:Import, object_oriented_style (-> +11), scope:a (-> +11), scope:b (-> +11), scope:c (-> +11), scope:ser (-> +11), scope:tst (-> +11), variety:3 (-> +11), whole_span:12 (-> +11)
class TestClass(object): # class:TestClass (-> +7), class_method_count:1 (-> +7), loaded_variable:object, node:ClassDef (-> +7), node:Name
    a = None # assignment:None, assignment_lhs_identifier:a, assignment_rhs_atom:None, literal:None, node:Assign, node:Name, node:NameConstant, single_assignment:a
    b = None # assignment:None, assignment_lhs_identifier:b, assignment_rhs_atom:None, literal:None, node:Assign, node:Name, node:NameConstant, single_assignment:b
    c = None # assignment:None, assignment_lhs_identifier:c, assignment_rhs_atom:None, literal:None, node:Assign, node:Name, node:NameConstant, single_assignment:c
    def __init__(self, a, b, c): # function:__init__ (-> +3), function_line_count:4 (-> +3), function_parameter:a, function_parameter:b, function_parameter:c, function_parameter:self, function_parameter_flavor:arg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), local_scope:a (-> +3), local_scope:b (-> +3), local_scope:c (-> +3), local_scope:self (-> +3), method:__init__ (-> +3), node:FunctionDef (-> +3), node:arg, scope:a (-> +3), scope:b (-> +3), scope:c (-> +3), scope:self (-> +3), shadowing_scope:a (-> +3), shadowing_scope:b (-> +3), shadowing_scope:c (-> +3)
        self.a = a # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:a, loaded_variable:a, loaded_variable:self, node:Assign, node:Attribute, node:Name
        self.b = b # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:b, loaded_variable:b, loaded_variable:self, node:Assign, node:Attribute, node:Name
        self.c = c # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:c, loaded_variable:c, loaded_variable:self, node:Assign, node:Attribute, node:Name
tst = TestClass("var_a", "var_b", "var_c") # argument:, assignment:TestClass, assignment_lhs_identifier:tst, external_free_call:TestClass, free_call:TestClass, literal:Str, node:Assign, node:Call, node:Name, node:Str, single_assignment:tst
ser = pyx.serialize(obj=tst, enc="utf-8") # argument:, argument:tst, assignment:serialize, assignment_lhs_identifier:ser, assignment_rhs_atom:pyx, assignment_rhs_atom:tst, keyword_argument:enc, keyword_argument:obj, literal:Str, loaded_variable:pyx, loaded_variable:tst, member_call_method:serialize, node:Assign, node:Attribute, node:Call, node:Name, node:Str, node:keyword, single_assignment:ser
print(ser) # argument:ser, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:ser, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 105.1804-current-executable-name.py
# ----------------------------------------------------------------------------------------
import sys # flat_style (-> +1), global_scope:s (-> +1), imperative_style (-> +1), import:sys, import_module:sys, node:Import, one_liner_style (-> +1), scope:s (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
s = sys.argv[0] # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:0, assignment_rhs_atom:sys, index:0, literal:0, loaded_variable:sys, node:Assign, node:Attribute, node:Name, node:Num, node:Subscript, single_assignment:s, value_attr:argv

# ----------------------------------------------------------------------------------------
# 106.2039-get-program-working-directory.py
# ----------------------------------------------------------------------------------------
import os # flat_style (-> +1), global_scope:dir (-> +1), imperative_style (-> +1), import:os, import_module:os, node:Import, one_liner_style (-> +1), scope:dir (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
dir = os.getcwd() # assignment:getcwd, assignment_lhs_identifier:dir, assignment_rhs_atom:os, loaded_variable:os, member_call_method:getcwd, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:dir

# ----------------------------------------------------------------------------------------
# 107.2139-get-folder-containing-current-program.py
# ----------------------------------------------------------------------------------------
import os # flat_style (-> +1), global_scope:dir (-> +1), imperative_style (-> +1), import:os, import_module:os, node:Import, one_liner_style (-> +1), scope:dir (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
dir = os.path.dirname(os.path.abspath(__file__)) # argument:, argument:__file__, assignment:dirname, assignment_lhs_identifier:dir, assignment_rhs_atom:__file__, assignment_rhs_atom:os, composition, loaded_variable:__file__, loaded_variable:os, member_call_method:abspath, member_call_method:dirname, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:dir, value_attr:path

# ----------------------------------------------------------------------------------------
# 108.1291-determine-if-variable-name-is-defined.py
# ----------------------------------------------------------------------------------------
if "x" in locals(): # comparison_operator:In, external_free_call:locals, free_call:locals, free_call_no_arguments:locals, if (-> +1), if_without_else (-> +1), imperative_style (-> +1), literal:Str, node:Call, node:Compare, node:If (-> +1), node:Name, node:Str, variety:1 (-> +1), whole_span:2 (-> +1)
    print(x) # argument:x, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch, loaded_variable:x, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 109.2280-number-of-bytes-of-a-type.py
# ----------------------------------------------------------------------------------------
import pympler.asizeof # flat_style (-> +1), global_scope:n (-> +1), imperative_style (-> +1), import:pympler.asizeof, import_module:pympler.asizeof, node:Import, one_liner_style (-> +1), scope:n (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
n = pympler.asizeof.asizeof(t) # argument:t, assignment:asizeof, assignment_lhs_identifier:n, assignment_rhs_atom:pympler, assignment_rhs_atom:t, loaded_variable:pympler, loaded_variable:t, member_call_method:asizeof, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:n, value_attr:asizeof

# ----------------------------------------------------------------------------------------
# 110.1455-check-if-string-is-blank.py
# ----------------------------------------------------------------------------------------
blank = s.strip() == "" # assignment, assignment_lhs_identifier:blank, assignment_rhs_atom:s, comparison_operator:Eq, empty_literal:Str, flat_style, global_scope:blank, imperative_style, literal:Str, loaded_variable:s, member_call_method:strip, node:Assign, node:Attribute, node:Call, node:Compare, node:Name, node:Str, one_liner_style, scope:blank, single_assignment:blank, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 111.2168-launch-other-program.py
# ----------------------------------------------------------------------------------------
import subprocess # flat_style (-> +1), imperative_style (-> +1), import:subprocess, import_module:subprocess, node:Import, one_liner_style (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
subprocess.call(["x", "a", "b"]) # argument:, literal:List, literal:Str, loaded_variable:subprocess, member_call:subprocess:call, member_call_method:call, member_call_object:subprocess, node:Attribute, node:Call, node:Expr, node:List, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 112.2144-iterate-over-map-entries-ordered-by-keys.py
# ----------------------------------------------------------------------------------------
for k in sorted(mymap): # argument:mymap, external_free_call:sorted, for:k (-> +1), free_call:sorted, global_scope:k (-> +1), imperative_style (-> +1), iteration_variable:k, loaded_variable:mymap, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:Call, node:For (-> +1), node:Name, scope:k (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    print(mymap[k]) # argument:, external_free_call:print, free_call:print, free_call_without_result:print, index:k, loaded_variable:k, loaded_variable:mymap, node:Call, node:Expr, node:Name, node:Subscript

# ----------------------------------------------------------------------------------------
# 113.2157-iterate-over-map-entries-ordered-by-values.py
# ----------------------------------------------------------------------------------------
for x, k in sorted((x, k) for k, x in mymap.items()): # argument:, composition, comprehension:Generator, comprehension_for_count:1, external_free_call:sorted, for:k (-> +1), for:x (-> +1), free_call:sorted, global_scope:k (-> +1), global_scope:x (-> +1), imperative_style (-> +1), iteration_variable:k, iteration_variable:x, literal:Tuple, loaded_variable:k, loaded_variable:mymap, loaded_variable:x, local_scope:k, local_scope:x, loop:for (-> +1), loop_with_late_exit:for (-> +1), member_call_method:items, node:Attribute, node:Call, node:For (-> +1), node:GeneratorExp, node:Name, node:Tuple, node:comprehension, scope:k, scope:k (-> +1), scope:x, scope:x (-> +1), shadowing_scope:k, shadowing_scope:x, variety:1 (-> +1), whole_span:2 (-> +1)
    print(k, x) # argument:k, argument:x, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:k, loaded_variable:x, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 114.2273-test-deep-equality.py
# ----------------------------------------------------------------------------------------
b = x == y # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:x, assignment_rhs_atom:y, comparison_operator:Eq, flat_style, global_scope:b, imperative_style, loaded_variable:x, loaded_variable:y, node:Assign, node:Compare, node:Name, one_liner_style, scope:b, single_assignment:b, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 115.2138-compare-dates.py
# ----------------------------------------------------------------------------------------
import datetime # flat_style (-> +1), global_scope:b (-> +1), imperative_style (-> +1), import:datetime, import_module:datetime, node:Import, one_liner_style (-> +1), scope:b (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
b = d1 < d2 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:d1, assignment_rhs_atom:d2, comparison_operator:Lt, loaded_variable:d1, loaded_variable:d2, node:Assign, node:Compare, node:Name, single_assignment:b

# ----------------------------------------------------------------------------------------
# 116.1257-remove-occurrences-of-word-from-string.py
# ----------------------------------------------------------------------------------------
s2 = s1.replace(w, "") # argument:, argument:w, assignment:replace, assignment_lhs_identifier:s2, assignment_rhs_atom:s1, assignment_rhs_atom:w, empty_literal:Str, flat_style, global_scope:s2, imperative_style, literal:Str, loaded_variable:s1, loaded_variable:w, member_call_method:replace, node:Assign, node:Attribute, node:Call, node:Name, node:Str, one_liner_style, scope:s2, single_assignment:s2, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 117.1297-get-list-size.py
# ----------------------------------------------------------------------------------------
n = len(x) # argument:x, assignment:len, assignment_lhs_identifier:n, assignment_rhs_atom:x, external_free_call:len, flat_style, free_call:len, global_scope:n, imperative_style, loaded_variable:x, node:Assign, node:Call, node:Name, one_liner_style, scope:n, single_assignment:n, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 118.1254-list-to-set.py
# ----------------------------------------------------------------------------------------
y = set(x) # argument:x, assignment:set, assignment_lhs_identifier:y, assignment_rhs_atom:x, external_free_call:set, flat_style, free_call:set, global_scope:y, imperative_style, loaded_variable:x, node:Assign, node:Call, node:Name, one_liner_style, scope:y, single_assignment:y, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 118.3266-list-to-set.py
# ----------------------------------------------------------------------------------------
set(x) # argument:x, external_free_call:set, flat_style, free_call:set, free_call_without_result:set, imperative_style, loaded_variable:x, node:Call, node:Expr, node:Name, one_liner_style, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 119.1253-deduplicate-list.py
# ----------------------------------------------------------------------------------------
x = list(set(x)) # argument:, argument:x, assignment:list, assignment_lhs_identifier:x, assignment_rhs_atom:x, composition, external_free_call:list, external_free_call:set, flat_style, free_call:list, free_call:set, global_scope:x, imperative_style, loaded_variable:x, node:Assign, node:Call, node:Name, one_liner_style, scope:x, single_assignment:x, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 119.3263-deduplicate-list.py
# ----------------------------------------------------------------------------------------
elements = ["b", "a", "b", "c"] # assignment, assignment_lhs_identifier:elements, global_scope:elements (-> +7), global_scope:elements_unique (-> +7), global_scope:i (-> +7), global_scope:unique_set (-> +7), imperative_style (-> +7), literal:List, literal:Str, node:Assign, node:List, node:Name, node:Str, scope:elements (-> +7), scope:elements_unique (-> +7), scope:i (-> +7), scope:unique_set (-> +7), single_assignment:elements, variety:3 (-> +7), whole_span:8 (-> +7)
unique_set = set() # assignment:set, assignment_lhs_identifier:unique_set, external_free_call:set, free_call:set, free_call_no_arguments:set, node:Assign, node:Call, node:Name, single_assignment:unique_set
elements_unique = [] # assignment, assignment_lhs_identifier:elements_unique, empty_literal:List, literal:List, node:Assign, node:List, node:Name, single_assignment:elements_unique
for i in elements: # accumulate_elements:add (-> +3), accumulate_elements:append (-> +3), accumulate_some_elements:add (-> +3), accumulate_some_elements:append (-> +3), for:i (-> +3), for_each:i (-> +3), iteration_variable:i, loaded_variable:elements, loop:for (-> +3), loop_with_late_exit:for (-> +3), node:For (-> +3), node:Name
    if i not in unique_set: # comparison_operator:NotIn, if (-> +2), if_test_atom:i, if_test_atom:unique_set, if_without_else (-> +2), loaded_variable:i, loaded_variable:unique_set, node:Compare, node:If (-> +2), node:Name
        unique_set.add(i) # argument:i, if_then_branch (-> +1), loaded_variable:i, loaded_variable:unique_set, member_call:unique_set:add, member_call_method:add, member_call_object:unique_set, node:Attribute, node:Call, node:Expr, node:Name, update:unique_set:i, update_by_member_call:unique_set:i, update_by_member_call_with:add, update_with:add
        elements_unique.append(i) # argument:i, loaded_variable:elements_unique, loaded_variable:i, member_call:elements_unique:append, member_call_method:append, member_call_object:elements_unique, node:Attribute, node:Call, node:Expr, node:Name, update:elements_unique:i, update_by_member_call:elements_unique:i, update_by_member_call_with:append, update_with:append
print(elements_unique) # argument:elements_unique, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:elements_unique, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 120.1479-read-integer-from-stdin.py
# ----------------------------------------------------------------------------------------
input_var = int(raw_input("Input Prompting String: ")) # argument:, assignment:int, assignment_lhs_identifier:input_var, composition, external_free_call:int, external_free_call:raw_input, flat_style, free_call:int, free_call:raw_input, global_scope:input_var, imperative_style, literal:Str, node:Assign, node:Call, node:Name, node:Str, one_liner_style, scope:input_var, single_assignment:input_var, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 121.3029-udp-listen-and-read.py
# ----------------------------------------------------------------------------------------
import socket # global_scope:UDP_IP (-> +6), global_scope:addr (-> +6), global_scope:data (-> +6), global_scope:sock (-> +6), imperative_style (-> +6), import:socket, import_module:socket, node:Import, scope:UDP_IP (-> +6), scope:addr (-> +6), scope:data (-> +6), scope:sock (-> +6), variety:2 (-> +6), whole_span:7 (-> +6)
UDP_IP = "127.0.0.1" # assignment, assignment_lhs_identifier:UDP_IP, literal:Str, node:Assign, node:Name, node:Str, single_assignment:UDP_IP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # argument:, assignment:socket, assignment_lhs_identifier:sock, assignment_rhs_atom:socket, loaded_variable:socket, member_call_method:socket, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:sock
sock.bind((UDP_IP, p)) # argument:, literal:Tuple, loaded_variable:UDP_IP, loaded_variable:p, loaded_variable:sock, member_call:sock:bind, member_call_method:bind, member_call_object:sock, node:Attribute, node:Call, node:Expr, node:Name, node:Tuple
while True: # infinite_while (-> +2), literal:True, loop:while (-> +2), loop_with_late_exit:while (-> +2), node:NameConstant, node:While (-> +2)
    data, addr = sock.recvfrom(1024) # argument:1024, assignment:recvfrom, assignment_lhs_identifier:addr, assignment_lhs_identifier:data, assignment_rhs_atom:1024, assignment_rhs_atom:sock, literal:1024, literal:Tuple, loaded_variable:sock, magic_number:1024, member_call_method:recvfrom, node:Assign, node:Attribute, node:Call, node:Name, node:Num, node:Tuple, parallel_assignment:2
    print("received message:", data) # argument:, argument:data, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:data, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 122.1453-declare-enumeration.py
# ----------------------------------------------------------------------------------------
class Suit: # class:Suit (-> +1), global_scope:CLUBS (-> +1), global_scope:DIAMONDS (-> +1), global_scope:HEARTS (-> +1), global_scope:SPADES (-> +1), node:ClassDef (-> +1), object_oriented_style (-> +1), one_liner_style (-> +1), scope:CLUBS (-> +1), scope:DIAMONDS (-> +1), scope:HEARTS (-> +1), scope:SPADES (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    SPADES, HEARTS, DIAMONDS, CLUBS = range(4) # argument:4, assignment:range, assignment_lhs_identifier:CLUBS, assignment_lhs_identifier:DIAMONDS, assignment_lhs_identifier:HEARTS, assignment_lhs_identifier:SPADES, assignment_rhs_atom:4, external_free_call:range, free_call:range, literal:4, literal:Tuple, magic_number:4, node:Assign, node:Call, node:Name, node:Num, node:Tuple, parallel_assignment:4, range:4

# ----------------------------------------------------------------------------------------
# 122.1454-declare-enumeration.py
# ----------------------------------------------------------------------------------------
from enum import Enum # global_scope:CLUBS (-> +5), global_scope:DIAMONDS (-> +5), global_scope:HEARTS (-> +5), global_scope:SPADES (-> +5), import:enum:Enum, import_module:enum, import_name:Enum, node:ImportFrom, object_oriented_style (-> +5), scope:CLUBS (-> +5), scope:DIAMONDS (-> +5), scope:HEARTS (-> +5), scope:SPADES (-> +5), variety:2 (-> +5), whole_span:6 (-> +5)
class Suit(Enum): # class:Suit (-> +4), loaded_variable:Enum, node:ClassDef (-> +4), node:Name
    SPADES = 1 # assignment:1, assignment_lhs_identifier:SPADES, assignment_rhs_atom:1, literal:1, node:Assign, node:Name, node:Num, single_assignment:SPADES
    HEARTS = 2 # assignment:2, assignment_lhs_identifier:HEARTS, assignment_rhs_atom:2, literal:2, node:Assign, node:Name, node:Num, single_assignment:HEARTS
    DIAMONDS = 3 # assignment:3, assignment_lhs_identifier:DIAMONDS, assignment_rhs_atom:3, literal:3, node:Assign, node:Name, node:Num, single_assignment:DIAMONDS
    CLUBS = 4 # assignment:4, assignment_lhs_identifier:CLUBS, assignment_rhs_atom:4, literal:4, node:Assign, node:Name, node:Num, single_assignment:CLUBS

# ----------------------------------------------------------------------------------------
# 123.2146-assert-condition.py
# ----------------------------------------------------------------------------------------
assert isConsistent # flat_style, imperative_style, loaded_variable:isConsistent, node:Assert, node:Name, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 124.2152-binary-search-for-a-value-in-sorted-array.py
# ----------------------------------------------------------------------------------------
import bisect # import:bisect, import_module:bisect, node:Import, procedural_style (-> +3), variety:2 (-> +3), whole_span:4 (-> +3)
def binarySearch(a, x): # function:binarySearch (-> +2), function_line_count:3 (-> +2), function_parameter:a, function_parameter:x, function_parameter_flavor:arg, function_returning_something:binarySearch (-> +2), impure_function:binarySearch (-> +2), local_scope:a (-> +2), local_scope:i (-> +2), local_scope:x (-> +2), node:FunctionDef (-> +2), node:arg, scope:a (-> +2), scope:i (-> +2), scope:x (-> +2)
    i = bisect.bisect_left(a, x) # argument:a, argument:x, assignment:bisect_left, assignment_lhs_identifier:i, assignment_rhs_atom:a, assignment_rhs_atom:bisect, assignment_rhs_atom:x, loaded_variable:a, loaded_variable:bisect, loaded_variable:x, member_call_method:bisect_left, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:i
    return i if i != len(a) and a[i] == x else -1 # argument:a, boolean_operator:And, comparison_operator:Eq, comparison_operator:NotEq, external_free_call:len, free_call:len, index:i, literal:-1, loaded_variable:a, loaded_variable:i, loaded_variable:x, node:BoolOp, node:Call, node:Compare, node:IfExp, node:Name, node:Num, node:Return, node:Subscript, return

# ----------------------------------------------------------------------------------------
# 125.2167-measure-function-call-duration.py
# ----------------------------------------------------------------------------------------
import time # flat_style (-> +4), global_scope:t1 (-> +4), global_scope:t2 (-> +4), imperative_style (-> +4), import:time, import_module:time, node:Import, scope:t1 (-> +4), scope:t2 (-> +4), variety:2 (-> +4), whole_span:5 (-> +4)
t1 = time.perf_counter() # assignment:perf_counter, assignment_lhs_identifier:t1, assignment_rhs_atom:time, loaded_variable:time, member_call_method:perf_counter, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:t1
foo() # external_free_call:foo, free_call:foo, free_call_no_arguments:foo, free_call_without_result:foo, node:Call, node:Expr, node:Name
t2 = time.perf_counter() # assignment:perf_counter, assignment_lhs_identifier:t2, assignment_rhs_atom:time, loaded_variable:time, member_call_method:perf_counter, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:t2
print("Seconds:", t2 - t1) # argument:, binary_operator:Sub, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, loaded_variable:t1, loaded_variable:t2, node:BinOp, node:Call, node:Expr, node:Name, node:Str

# ----------------------------------------------------------------------------------------
# 126.2137-multiple-return-values.py
# ----------------------------------------------------------------------------------------
def foo(): # function:foo (-> +1), function_line_count:2 (-> +1), function_returning_something:foo (-> +1), function_without_parameters:foo (-> +1), functional_style (-> +1), node:FunctionDef (-> +1), one_liner_style (-> +1), pure_function:foo (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    return "string", True # literal:Str, literal:True, literal:Tuple, node:NameConstant, node:Return, node:Str, node:Tuple, return

# ----------------------------------------------------------------------------------------
# 127.2274-source-code-inclusion.py
# ----------------------------------------------------------------------------------------
import imp # flat_style (-> +1), global_scope:foo (-> +1), imperative_style (-> +1), import:imp, import_module:imp, node:Import, one_liner_style (-> +1), scope:foo (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
foo = imp.load_module("foobody", "foobody.txt").foo # argument:, assignment, assignment_lhs_identifier:foo, assignment_rhs_atom:imp, literal:Str, loaded_variable:imp, member_call:imp:load_module, member_call_method:load_module, member_call_object:imp, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:foo

# ----------------------------------------------------------------------------------------
# 128.2085-breadth-first-traversing-of-a-tree.py
# ----------------------------------------------------------------------------------------
def BFS(f, root): # function:BFS (-> +8), function_line_count:9 (-> +8), function_parameter:f, function_parameter:root, function_parameter_flavor:arg, function_returning_nothing:BFS (-> +8), higher_order_function:f (-> +8), local_scope:Q (-> +8), local_scope:child (-> +8), local_scope:f (-> +8), local_scope:n (-> +8), local_scope:root (-> +8), node:FunctionDef (-> +8), node:arg, procedural_style (-> +8), scope:Q (-> +8), scope:child (-> +8), scope:f (-> +8), scope:n (-> +8), scope:root (-> +8), variety:4 (-> +8), whole_span:9 (-> +8)
    Q = [root] # assignment, assignment_lhs_identifier:Q, assignment_rhs_atom:root, literal:List, loaded_variable:root, node:Assign, node:List, node:Name, single_assignment:Q
    while Q: # loaded_variable:Q, loop:while (-> +6), loop_with_late_exit:while (-> +6), node:Name, node:While (-> +6)
        n = Q.pop(0) # argument:0, assignment:pop, assignment_lhs_identifier:n, assignment_rhs_atom:0, assignment_rhs_atom:Q, literal:0, loaded_variable:Q, member_call_method:pop, node:Assign, node:Attribute, node:Call, node:Name, node:Num, single_assignment:n
        f(n) # argument:n, external_free_call:f, free_call:f, free_call_without_result:f, loaded_variable:n, node:Call, node:Expr, node:Name
        for child in n: # for:child (-> +3), for_each:child (-> +3), iteration_variable:child, loaded_variable:n, loop:for (-> +3), loop_with_late_exit:for (-> +3), node:For (-> +3), node:Name
            if not n.discovered: # if (-> +2), if_test_atom:n, if_without_else (-> +2), loaded_variable:n, node:Attribute, node:If (-> +2), node:Name, node:UnaryOp, unary_operator:Not
                n.discovered = True # assignment:True, assignment_lhs_identifier:n, assignment_rhs_atom:True, if_then_branch (-> +1), literal:True, loaded_variable:n, node:Assign, node:Attribute, node:Name, node:NameConstant
                Q.append(n) # argument:n, loaded_variable:Q, loaded_variable:n, member_call:Q:append, member_call_method:append, member_call_object:Q, node:Attribute, node:Call, node:Expr, node:Name, update:Q:n, update_by_member_call:Q:n, update_by_member_call_with:append, update_with:append

# ----------------------------------------------------------------------------------------
# 129.2282-breadth-first-traversing-in-a-graph.py
# ----------------------------------------------------------------------------------------
from collections import deque # import:collections:deque, import_module:collections, import_name:deque, node:ImportFrom, procedural_style (-> +8), variety:4 (-> +8), whole_span:9 (-> +8)
def breadth_first(start, f): # function:breadth_first (-> +7), function_line_count:8 (-> +7), function_parameter:f, function_parameter:start, function_parameter_flavor:arg, function_returning_nothing:breadth_first (-> +7), higher_order_function:f (-> +7), local_scope:f (-> +7), local_scope:q (-> +7), local_scope:seen (-> +7), local_scope:start (-> +7), local_scope:vertex (-> +7), node:FunctionDef (-> +7), node:arg, scope:f (-> +7), scope:q (-> +7), scope:seen (-> +7), scope:start (-> +7), scope:vertex (-> +7)
    seen = set() # assignment:set, assignment_lhs_identifier:seen, external_free_call:set, free_call:set, free_call_no_arguments:set, node:Assign, node:Call, node:Name, single_assignment:seen
    q = deque([start]) # argument:, assignment:deque, assignment_lhs_identifier:q, assignment_rhs_atom:start, external_free_call:deque, free_call:deque, literal:List, loaded_variable:start, node:Assign, node:Call, node:List, node:Name, single_assignment:q
    while q: # loaded_variable:q, loop:while (-> +4), loop_with_late_exit:while (-> +4), node:Name, node:While (-> +4)
        vertex = q.popleft() # assignment:popleft, assignment_lhs_identifier:vertex, assignment_rhs_atom:q, loaded_variable:q, member_call_method:popleft, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:vertex
        f(vertex) # argument:vertex, external_free_call:f, free_call:f, free_call_without_result:f, loaded_variable:vertex, node:Call, node:Expr, node:Name
        seen.add(vertex) # argument:vertex, loaded_variable:seen, loaded_variable:vertex, member_call:seen:add, member_call_method:add, member_call_object:seen, node:Attribute, node:Call, node:Expr, node:Name, update:seen:vertex, update_by_member_call:seen:vertex, update_by_member_call_with:add, update_with:add
        q.extend(v for v in vertex.adjacent if v not in seen) # argument:, comparison_operator:NotIn, comprehension:Generator, comprehension_for_count:1, filtered_comprehension, iteration_variable:v, loaded_variable:q, loaded_variable:seen, loaded_variable:v, loaded_variable:vertex, local_scope:v, member_call:q:extend, member_call_method:extend, member_call_object:q, node:Attribute, node:Call, node:Compare, node:Expr, node:GeneratorExp, node:Name, node:comprehension, scope:v

# ----------------------------------------------------------------------------------------
# 130.2283-depth-first-traversing-in-a-graph.py
# ----------------------------------------------------------------------------------------
def depth_first(start, f): # function:depth_first (-> +7), function_line_count:8 (-> +7), function_parameter:f, function_parameter:start, function_parameter_flavor:arg, function_returning_nothing:depth_first (-> +7), higher_order_function:f (-> +7), local_scope:f (-> +7), local_scope:seen (-> +7), local_scope:stack (-> +7), local_scope:start (-> +7), local_scope:vertex (-> +7), node:FunctionDef (-> +7), node:arg, procedural_style (-> +7), scope:f (-> +7), scope:seen (-> +7), scope:stack (-> +7), scope:start (-> +7), scope:vertex (-> +7), variety:3 (-> +7), whole_span:8 (-> +7)
    seen = set() # assignment:set, assignment_lhs_identifier:seen, external_free_call:set, free_call:set, free_call_no_arguments:set, node:Assign, node:Call, node:Name, single_assignment:seen
    stack = [start] # assignment, assignment_lhs_identifier:stack, assignment_rhs_atom:start, literal:List, loaded_variable:start, node:Assign, node:List, node:Name, single_assignment:stack
    while stack: # loaded_variable:stack, loop:while (-> +4), loop_with_late_exit:while (-> +4), node:Name, node:While (-> +4)
        vertex = stack.pop() # assignment:pop, assignment_lhs_identifier:vertex, assignment_rhs_atom:stack, loaded_variable:stack, member_call_method:list:pop, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:vertex
        f(vertex) # argument:vertex, external_free_call:f, free_call:f, free_call_without_result:f, loaded_variable:vertex, node:Call, node:Expr, node:Name
        seen.add(vertex) # argument:vertex, loaded_variable:seen, loaded_variable:vertex, member_call:seen:add, member_call_method:add, member_call_object:seen, node:Attribute, node:Call, node:Expr, node:Name, update:seen:vertex, update_by_member_call:seen:vertex, update_by_member_call_with:add, update_with:add
        stack.extend(v for v in vertex.adjacent if v not in seen) # argument:, comparison_operator:NotIn, comprehension:Generator, comprehension_for_count:1, filtered_comprehension, iteration_variable:v, loaded_variable:seen, loaded_variable:stack, loaded_variable:v, loaded_variable:vertex, local_scope:v, member_call:stack:extend, member_call_method:extend, member_call_object:stack, node:Attribute, node:Call, node:Compare, node:Expr, node:GeneratorExp, node:Name, node:comprehension, scope:v

# ----------------------------------------------------------------------------------------
# 131.2083-successive-conditions.py
# ----------------------------------------------------------------------------------------
f1 if c1 else f2 if c2 else f3 if c3 else None # flat_style, imperative_style, literal:None, loaded_variable:c1, loaded_variable:c2, loaded_variable:c3, loaded_variable:f1, loaded_variable:f2, loaded_variable:f3, node:Expr, node:IfExp, node:Name, node:NameConstant, one_liner_style, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 131.2766-successive-conditions.py
# ----------------------------------------------------------------------------------------
if c1: # if (-> +5), imperative_style (-> +5), loaded_variable:c1, node:If (-> +5), node:Name, variety:2 (-> +5), whole_span:6 (-> +5)
    f1() # external_free_call:f1, free_call:f1, free_call_no_arguments:f1, free_call_without_result:f1, if_then_branch, node:Call, node:Expr, node:Name
elif c2: # if (-> +3), loaded_variable:c2, node:If (-> +3), node:Name
    f2() # external_free_call:f2, free_call:f2, free_call_no_arguments:f2, free_call_without_result:f2, if_elif_branch, node:Call, node:Expr, node:Name
elif c3: # if (-> +1), loaded_variable:c3, node:If (-> +1), node:Name
    f3() # external_free_call:f3, free_call:f3, free_call_no_arguments:f3, free_call_without_result:f3, if_elif_branch, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 132.2040-measure-duration-of-procedure-execution.py
# ----------------------------------------------------------------------------------------
import timeit # flat_style (-> +1), global_scope:duration (-> +1), imperative_style (-> +1), import:timeit, import_module:timeit, node:Import, one_liner_style (-> +1), scope:duration (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
duration = timeit.timeit("f()", setup="from __main__ import f") # argument:, assignment:timeit, assignment_lhs_identifier:duration, assignment_rhs_atom:timeit, keyword_argument:setup, literal:Str, loaded_variable:timeit, member_call_method:timeit, node:Assign, node:Attribute, node:Call, node:Name, node:Str, node:keyword, single_assignment:duration

# ----------------------------------------------------------------------------------------
# 133.2160-case-insensitive-string-contains.py
# ----------------------------------------------------------------------------------------
ok = word.lower() in s.lower() # assignment, assignment_lhs_identifier:ok, assignment_rhs_atom:s, assignment_rhs_atom:word, comparison_operator:In, flat_style, global_scope:ok, imperative_style, loaded_variable:s, loaded_variable:word, member_call_method:lower, node:Assign, node:Attribute, node:Call, node:Compare, node:Name, one_liner_style, scope:ok, single_assignment:ok, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 134.1850-create-a-new-list.py
# ----------------------------------------------------------------------------------------
items = [a, b, c] # assignment, assignment_lhs_identifier:items, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:c, flat_style, global_scope:items, imperative_style, literal:List, loaded_variable:a, loaded_variable:b, loaded_variable:c, node:Assign, node:List, node:Name, one_liner_style, scope:items, single_assignment:items, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 135.2158-remove-item-from-list-by-its-value.py
# ----------------------------------------------------------------------------------------
items.remove(x) # argument:x, flat_style, imperative_style, loaded_variable:items, loaded_variable:x, member_call:items:remove, member_call_method:remove, member_call_object:items, node:Attribute, node:Call, node:Expr, node:Name, one_liner_style, update:items:x, update_by_member_call:items:x, update_by_member_call_with:remove, update_with:remove, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 136.2141-remove-all-occurrences-of-a-value-from-a-list.py
# ----------------------------------------------------------------------------------------
newlist = [item for item in items if item != x] # assignment, assignment_lhs_identifier:newlist, assignment_rhs_atom:item, assignment_rhs_atom:items, assignment_rhs_atom:x, comparison_operator:NotEq, comprehension:List, comprehension_for_count:1, filtered_comprehension, flat_style, imperative_style, iteration_variable:item, loaded_variable:item, loaded_variable:items, loaded_variable:x, local_scope:item, local_scope:newlist, node:Assign, node:Compare, node:ListComp, node:Name, node:comprehension, one_liner_style, scope:item, scope:newlist, single_assignment:newlist, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 137.1823-check-if-string-contains-only-digits.py
# ----------------------------------------------------------------------------------------
b = s.isdigit() # assignment:isdigit, assignment_lhs_identifier:b, assignment_rhs_atom:s, flat_style, global_scope:b, imperative_style, loaded_variable:s, member_call_method:isdigit, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:b, single_assignment:b, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 138.2161-create-temp-file.py
# ----------------------------------------------------------------------------------------
import tempfile # flat_style (-> +1), global_scope:file (-> +1), imperative_style (-> +1), import:tempfile, import_module:tempfile, node:Import, one_liner_style (-> +1), scope:file (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
file = tempfile.TemporaryFile() # assignment:TemporaryFile, assignment_lhs_identifier:file, assignment_rhs_atom:tempfile, loaded_variable:tempfile, member_call_method:TemporaryFile, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:file

# ----------------------------------------------------------------------------------------
# 139.2162-create-temp-directory.py
# ----------------------------------------------------------------------------------------
import tempfile # flat_style (-> +1), global_scope:td (-> +1), imperative_style (-> +1), import:tempfile, import_module:tempfile, node:Import, one_liner_style (-> +1), scope:td (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
td = tempfile.TemporaryDirectory() # assignment:TemporaryDirectory, assignment_lhs_identifier:td, assignment_rhs_atom:tempfile, loaded_variable:tempfile, member_call_method:TemporaryDirectory, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:td

# ----------------------------------------------------------------------------------------
# 140.2156-delete-map-entry.py
# ----------------------------------------------------------------------------------------
m.pop(k, None) # argument:None, argument:k, flat_style, imperative_style, literal:None, loaded_variable:k, loaded_variable:m, member_call:m:pop, member_call_method:pop, member_call_object:m, node:Attribute, node:Call, node:Expr, node:Name, node:NameConstant, one_liner_style, update:m:None, update:m:k, update_by_member_call:m:None, update_by_member_call:m:k, update_by_member_call_with:pop, update_with:pop, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 141.2159-iterate-in-sequence-over-two-lists.py
# ----------------------------------------------------------------------------------------
for x in items1 + items2: # addition_operator, binary_operator:Add, for:x (-> +1), global_scope:x (-> +1), imperative_style (-> +1), iteration_variable:x, loaded_variable:items1, loaded_variable:items2, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:BinOp, node:For (-> +1), node:Name, scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    print(x) # argument:x, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:x, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 142.2151-hexadecimal-digits-of-an-integer.py
# ----------------------------------------------------------------------------------------
s = hex(x) # argument:x, assignment:hex, assignment_lhs_identifier:s, assignment_rhs_atom:x, external_free_call:hex, flat_style, free_call:hex, global_scope:s, imperative_style, loaded_variable:x, node:Assign, node:Call, node:Name, one_liner_style, scope:s, single_assignment:s, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 143.2256-iterate-alternatively-over-two-lists.py
# ----------------------------------------------------------------------------------------
for pair in zip(item1, item2): # argument:item1, argument:item2, external_free_call:zip, for:pair (-> +1), free_call:zip, global_scope:pair (-> +1), imperative_style (-> +1), iteration_variable:pair, loaded_variable:item1, loaded_variable:item2, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:Call, node:For (-> +1), node:Name, scope:pair (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    print(pair) # argument:pair, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:pair, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 144.2145-check-if-file-exists.py
# ----------------------------------------------------------------------------------------
import os # flat_style (-> +1), global_scope:b (-> +1), imperative_style (-> +1), import:os, import_module:os, node:Import, one_liner_style (-> +1), scope:b (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
b = os.path.exists(fp) # argument:fp, assignment:exists, assignment_lhs_identifier:b, assignment_rhs_atom:fp, assignment_rhs_atom:os, loaded_variable:fp, loaded_variable:os, member_call_method:exists, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:b, value_attr:path

# ----------------------------------------------------------------------------------------
# 144.2915-check-if-file-exists.py
# ----------------------------------------------------------------------------------------
from pathlib import Path # flat_style (-> +1), global_scope:b (-> +1), imperative_style (-> +1), import:pathlib:Path, import_module:pathlib, import_name:Path, node:ImportFrom, one_liner_style (-> +1), scope:b (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
b = Path(fp).exists() # argument:fp, assignment:exists, assignment_lhs_identifier:b, assignment_rhs_atom:fp, external_free_call:Path, free_call:Path, loaded_variable:fp, member_call_method:exists, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:b

# ----------------------------------------------------------------------------------------
# 145.1822-print-log-line-with-datetime.py
# ----------------------------------------------------------------------------------------
import sys, logging # flat_style (-> +5), global_scope:logger (-> +5), imperative_style (-> +5), import:logging, import:sys, import_module:logging, import_module:sys, node:Import, scope:logger (-> +5), variety:2 (-> +5), whole_span:6 (-> +5)
logging.basicConfig( # loaded_variable:logging, member_call:logging:basicConfig, member_call_method:basicConfig, member_call_object:logging, node:Attribute, node:Call (-> +1), node:Expr (-> +1), node:Name
    stream=sys.stdout, level=logging.DEBUG, format="%(asctime)-15s %(message)s" # argument:, keyword_argument:format, keyword_argument:level, keyword_argument:stream, literal:Str, loaded_variable:logging, loaded_variable:sys, node:Attribute, node:Name, node:Str, node:keyword, value_attr:DEBUG, value_attr:stdout
)
logger = logging.getLogger("NAME OF LOGGER") # argument:, assignment:getLogger, assignment_lhs_identifier:logger, assignment_rhs_atom:logging, literal:Str, loaded_variable:logging, member_call_method:getLogger, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:logger
logger.info(msg) # argument:msg, loaded_variable:logger, loaded_variable:msg, member_call:logger:info, member_call_method:info, member_call_object:logger, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 146.1825-convert-string-to-floating-point-number.py
# ----------------------------------------------------------------------------------------
import locale # flat_style (-> +3), global_scope:f (-> +3), global_scope:s (-> +3), imperative_style (-> +3), import:locale, import_module:locale, node:Import, scope:f (-> +3), scope:s (-> +3), variety:2 (-> +3), whole_span:4 (-> +3)
s = u"545,2222" # assignment, assignment_lhs_identifier:s, literal:Str, node:Assign, node:Name, node:Str, single_assignment:s
locale.setlocale(locale.LC_ALL, "de") # argument:, literal:Str, loaded_variable:locale, member_call:locale:setlocale, member_call_method:setlocale, member_call_object:locale, node:Attribute, node:Call, node:Expr, node:Name, node:Str
f = locale.atof(s) # argument:s, assignment:atof, assignment_lhs_identifier:f, assignment_rhs_atom:locale, assignment_rhs_atom:s, loaded_variable:locale, loaded_variable:s, member_call_method:atof, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:f

# ----------------------------------------------------------------------------------------
# 146.1826-convert-string-to-floating-point-number.py
# ----------------------------------------------------------------------------------------
f = float(s) # argument:s, assignment:float, assignment_lhs_identifier:f, assignment_rhs_atom:s, external_free_call:float, flat_style, free_call:float, global_scope:f, imperative_style, loaded_variable:s, node:Assign, node:Call, node:Name, one_liner_style, scope:f, single_assignment:f, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 146.2739-convert-string-to-floating-point-number.py
# ----------------------------------------------------------------------------------------
float("1.3") # argument:, external_free_call:float, flat_style, free_call:float, free_call_without_result:float, imperative_style, literal:Str, node:Call, node:Expr, node:Name, node:Str, one_liner_style, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 147.2171-remove-all-non-ascii-characters.py
# ----------------------------------------------------------------------------------------
import re # flat_style (-> +1), global_scope:t (-> +1), imperative_style (-> +1), import:re, import_module:re, node:Import, one_liner_style (-> +1), scope:t (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
t = re.sub("[^\u0000-\u007f]", "", s) # argument:, argument:s, assignment:sub, assignment_lhs_identifier:t, assignment_rhs_atom:re, assignment_rhs_atom:s, empty_literal:Str, literal:Str, loaded_variable:re, loaded_variable:s, member_call_method:sub, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:t, special_literal_string:[^\x00-\x7f]

# ----------------------------------------------------------------------------------------
# 148.1829-read-list-of-integer-numbers-from-stdin.py
# ----------------------------------------------------------------------------------------
list(map(int, input().split())) # argument:, argument:int, composition, external_free_call:input, external_free_call:list, external_free_call:map, flat_style, free_call:input, free_call:list, free_call:map, free_call_no_arguments:input, free_call_without_result:list, imperative_style, loaded_variable:int, member_call_method:split, node:Attribute, node:Call, node:Expr, node:Name, one_liner_style, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 150.2154-remove-trailing-slash.py
# ----------------------------------------------------------------------------------------
p = p.rstrip("/") # argument:, assignment:rstrip, assignment_lhs_identifier:p, assignment_rhs_atom:p, flat_style, global_scope:p, imperative_style, literal:Str, loaded_variable:p, member_call_method:rstrip, node:Assign, node:Attribute, node:Call, node:Name, node:Str, one_liner_style, scope:p, single_assignment:p, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 151.2166-remove-string-trailing-path-separator.py
# ----------------------------------------------------------------------------------------
import os # global_scope:p (-> +2), imperative_style (-> +2), import:os, import_module:os, node:Import, scope:p (-> +2), variety:2 (-> +2), whole_span:3 (-> +2)
if p.endswith(os.sep): # argument:, if (-> +1), if_test_atom:os, if_test_atom:p, if_without_else (-> +1), loaded_variable:os, loaded_variable:p, member_call_method:endswith, node:Attribute, node:Call, node:If (-> +1), node:Name
    p = p[:-1] # assignment, assignment_lhs_identifier:p, assignment_rhs_atom:-1, assignment_rhs_atom:p, if_then_branch, literal:-1, loaded_variable:p, node:Assign, node:Name, node:Num, node:Slice, node:Subscript, single_assignment:p, slice::-1:, slice_lower:, slice_step:, slice_upper:-1, update:p:-1, update_by_assignment:p:-1, update_by_assignment_with, update_with

# ----------------------------------------------------------------------------------------
# 152.2153-turn-a-character-into-a-string.py
# ----------------------------------------------------------------------------------------
s = c # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:c, flat_style, global_scope:s, imperative_style, loaded_variable:c, node:Assign, node:Name, one_liner_style, scope:s, single_assignment:s, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 153.1980-concatenate-string-with-integer.py
# ----------------------------------------------------------------------------------------
t = "{}{}".format(s, i) # argument:i, argument:s, assignment:format, assignment_lhs_identifier:t, assignment_rhs_atom:i, assignment_rhs_atom:s, flat_style, global_scope:t, imperative_style, literal:Str, loaded_variable:i, loaded_variable:s, member_call_method:format, node:Assign, node:Attribute, node:Call, node:Name, node:Str, one_liner_style, scope:t, single_assignment:t, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 154.2155-halfway-between-two-hex-color-codes.py
# ----------------------------------------------------------------------------------------
r1, g1, b1 = [int(c1[p : p + 2], 16) for p in range(1, 6, 2)] # addition_operator, argument:, argument:1, argument:16, argument:2, argument:6, assignment, assignment_lhs_identifier:b1, assignment_lhs_identifier:g1, assignment_lhs_identifier:r1, assignment_rhs_atom:1, assignment_rhs_atom:16, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:c1, assignment_rhs_atom:p, binary_operator:Add, comprehension:List, comprehension_for_count:1, external_free_call:int, external_free_call:range, flat_style (-> +2), free_call:int, free_call:range, global_scope:b1 (-> +2), global_scope:b2 (-> +2), global_scope:c (-> +2), global_scope:g1 (-> +2), global_scope:g2 (-> +2), global_scope:r1 (-> +2), global_scope:r2 (-> +2), imperative_style (-> +2), iteration_variable:p, literal:1, literal:16, literal:2, literal:6, literal:Tuple, loaded_variable:c1, loaded_variable:p, local_scope:p, magic_number:16, magic_number:6, node:Assign, node:BinOp, node:Call, node:ListComp, node:Name, node:Num, node:Slice, node:Subscript, node:Tuple, node:comprehension, parallel_assignment:3, range:1:6:2, scope:b1 (-> +2), scope:b2 (-> +2), scope:c (-> +2), scope:g1 (-> +2), scope:g2 (-> +2), scope:p, scope:r1 (-> +2), scope:r2 (-> +2), slice:p:_:, slice_lower:p, slice_step:, slice_upper:_, variety:0 (-> +2), whole_span:3 (-> +2)
r2, g2, b2 = [int(c2[p : p + 2], 16) for p in range(1, 6, 2)] # addition_operator, argument:, argument:1, argument:16, argument:2, argument:6, assignment, assignment_lhs_identifier:b2, assignment_lhs_identifier:g2, assignment_lhs_identifier:r2, assignment_rhs_atom:1, assignment_rhs_atom:16, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:c2, assignment_rhs_atom:p, binary_operator:Add, comprehension:List, comprehension_for_count:1, external_free_call:int, external_free_call:range, free_call:int, free_call:range, iteration_variable:p, literal:1, literal:16, literal:2, literal:6, literal:Tuple, loaded_variable:c2, loaded_variable:p, local_scope:p, magic_number:16, magic_number:6, node:Assign, node:BinOp, node:Call, node:ListComp, node:Name, node:Num, node:Slice, node:Subscript, node:Tuple, node:comprehension, parallel_assignment:3, range:1:6:2, scope:p, slice:p:_:, slice_lower:p, slice_step:, slice_upper:_
c = "#{:02x}{:02x}{:02x}".format((r1 + r2) // 2, (g1 + g2) // 2, (b1 + b2) // 2) # addition_operator, argument:, assignment:format, assignment_lhs_identifier:c, assignment_rhs_atom:2, assignment_rhs_atom:b1, assignment_rhs_atom:b2, assignment_rhs_atom:g1, assignment_rhs_atom:g2, assignment_rhs_atom:r1, assignment_rhs_atom:r2, binary_operator:Add, binary_operator:FloorDiv, literal:2, literal:Str, loaded_variable:b1, loaded_variable:b2, loaded_variable:g1, loaded_variable:g2, loaded_variable:r1, loaded_variable:r2, member_call_method:format, node:Assign, node:Attribute, node:BinOp, node:Call, node:Name, node:Num, node:Str, single_assignment:c

# ----------------------------------------------------------------------------------------
# 154.2292-halfway-between-two-hex-color-codes.py
# ----------------------------------------------------------------------------------------
import numpy # global_scope:c1 (-> +14), global_scope:c2 (-> +14), import:numpy, import_module:numpy, node:Import, object_oriented_style (-> +14), scope:c1 (-> +14), scope:c2 (-> +14), variety:5 (-> +14), whole_span:15 (-> +14)
class RGB(numpy.ndarray): # class:RGB (-> +8), class_method_count:2 (-> +8), loaded_variable:numpy, node:Attribute, node:ClassDef (-> +8), node:Name
    @classmethod # function_decorator:classmethod (-> +4), loaded_variable:classmethod, node:Name
    def from_str(cls, rgbstr): # class_method:from_str (-> +3), decorated_function:from_str (-> +3), function:from_str (-> +3), function_line_count:4 (-> +3), function_parameter:cls, function_parameter:rgbstr, function_parameter_flavor:arg, function_returning_something:from_str (-> +3), local_scope:cls (-> +3), local_scope:rgbstr (-> +3), method:from_str (-> +3), node:FunctionDef (-> +3), node:arg, scope:cls (-> +3), scope:rgbstr (-> +3)
        return numpy.array( # composition, loaded_variable:numpy, member_call:numpy:array, member_call:numpy:view, member_call_method:array, member_call_method:view, member_call_object:numpy, method_chaining, node:Attribute, node:Attribute (-> +1), node:Call (-> +1), node:Call (-> +2), node:Name, node:Return (-> +2), return (-> +2)
            [int(rgbstr[i : i + 2], 16) for i in range(1, len(rgbstr), 2)] # addition_operator, argument:, argument:1, argument:16, argument:2, argument:rgbstr, binary_operator:Add, composition, comprehension:List, comprehension_for_count:1, external_free_call:int, external_free_call:len, external_free_call:range, free_call:int, free_call:len, free_call:range, iteration_variable:i, literal:1, literal:16, literal:2, loaded_variable:i, loaded_variable:rgbstr, local_scope:i, magic_number:16, node:BinOp, node:Call, node:ListComp, node:Name, node:Num, node:Slice, node:Subscript, node:comprehension, range:1:_:2, scope:i, slice:i:_:, slice_lower:i, slice_step:, slice_upper:_
        ).view(cls) # argument:cls, loaded_variable:cls, node:Name
    def __str__(self): # function:__str__ (-> +2), function_line_count:3 (-> +2), function_parameter:self, function_parameter_flavor:arg, function_returning_something:__str__ (-> +2), instance_method:__str__ (-> +2), local_scope:self (-> +2), method:__str__ (-> +2), node:FunctionDef (-> +2), node:arg, scope:self (-> +2)
        self = self.astype(numpy.uint8) # argument:, assignment:astype, assignment_lhs_identifier:self, assignment_rhs_atom:numpy, assignment_rhs_atom:self, loaded_variable:numpy, loaded_variable:self, member_call_method:astype, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:self, update:self:numpy, update_by_assignment:self:numpy, update_by_assignment_with:astype, update_with:astype
        return "#" + "".join(format(n, "x") for n in self) # argument:, argument:n, binary_operator:Add, composition, comprehension:Generator, comprehension_for_count:1, concatenation_operator:Str, empty_literal:Str, external_free_call:format, free_call:format, iteration_variable:n, literal:Str, loaded_variable:n, loaded_variable:self, local_scope:n, member_call_method:join, node:Attribute, node:BinOp, node:Call, node:GeneratorExp, node:Name, node:Return, node:Str, node:comprehension, return, scope:n
c1 = RGB.from_str("#a1b1c1") # argument:, assignment:from_str, assignment_lhs_identifier:c1, assignment_rhs_atom:RGB, literal:Str, loaded_variable:RGB, member_call_method:from_str, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:c1
print(c1) # argument:c1, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:c1, node:Call, node:Expr, node:Name
c2 = RGB.from_str("#1A1B1C") # argument:, assignment:from_str, assignment_lhs_identifier:c2, assignment_rhs_atom:RGB, literal:Str, loaded_variable:RGB, member_call_method:from_str, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:c2
print(c2) # argument:c2, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:c2, node:Call, node:Expr, node:Name
print((c1 + c2) / 2) # addition_operator, argument:, binary_operator:Add, binary_operator:Div, external_free_call:print, free_call:print, free_call_without_result:print, literal:2, loaded_variable:c1, loaded_variable:c2, node:BinOp, node:Call, node:Expr, node:Name, node:Num

# ----------------------------------------------------------------------------------------
# 155.2147-delete-file.py
# ----------------------------------------------------------------------------------------
import pathlib # flat_style (-> +2), global_scope:path (-> +2), imperative_style (-> +2), import:pathlib, import_module:pathlib, node:Import, scope:path (-> +2), variety:2 (-> +2), whole_span:3 (-> +2)
path = pathlib.Path(_filepath) # argument:_filepath, assignment:Path, assignment_lhs_identifier:path, assignment_rhs_atom:_filepath, assignment_rhs_atom:pathlib, loaded_variable:_filepath, loaded_variable:pathlib, member_call_method:Path, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:path
path.unlink() # loaded_variable:path, member_call:path:unlink, member_call_method:unlink, member_call_object:path, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 156.2148-format-integer-with-zero-padding.py
# ----------------------------------------------------------------------------------------
s = format("03d", i) # argument:, argument:i, assignment:format, assignment_lhs_identifier:s, assignment_rhs_atom:i, external_free_call:format, flat_style, free_call:format, global_scope:s, imperative_style, literal:Str, loaded_variable:i, node:Assign, node:Call, node:Name, node:Str, one_liner_style, scope:s, single_assignment:s, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 157.2150-declare-constant-string.py
# ----------------------------------------------------------------------------------------
PLANET = "Earth" # assignment, assignment_lhs_identifier:PLANET, flat_style, global_scope:PLANET, imperative_style, literal:Str, node:Assign, node:Name, node:Str, one_liner_style, scope:PLANET, single_assignment:PLANET, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 158.2163-random-sublist.py
# ----------------------------------------------------------------------------------------
import random # flat_style (-> +1), global_scope:y (-> +1), imperative_style (-> +1), import:random, import_module:random, node:Import, one_liner_style (-> +1), scope:y (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
y = random.sample(x, k) # argument:k, argument:x, assignment:sample, assignment_lhs_identifier:y, assignment_rhs_atom:k, assignment_rhs_atom:random, assignment_rhs_atom:x, loaded_variable:k, loaded_variable:random, loaded_variable:x, member_call_method:sample, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:y

# ----------------------------------------------------------------------------------------
# 159.2281-trie.py
# ----------------------------------------------------------------------------------------
class Trie: # class:Trie (-> +4), class_method_count:1 (-> +4), node:ClassDef (-> +4), object_oriented_style (-> +4), variety:2 (-> +4), whole_span:5 (-> +4)
    def __init__(self, prefix, value=None): # function:__init__ (-> +3), function_line_count:4 (-> +3), function_parameter:prefix, function_parameter:self, function_parameter:value, function_parameter_default:NameConstant, function_parameter_flavor:arg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), literal:None, local_scope:prefix (-> +3), local_scope:self (-> +3), local_scope:value (-> +3), method:__init__ (-> +3), node:FunctionDef (-> +3), node:NameConstant, node:arg, scope:prefix (-> +3), scope:self (-> +3), scope:value (-> +3)
        self.prefix = prefix # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:prefix, loaded_variable:prefix, loaded_variable:self, node:Assign, node:Attribute, node:Name
        self.children = [] # assignment, assignment_lhs_identifier:self, empty_literal:List, literal:List, loaded_variable:self, node:Assign, node:Attribute, node:List, node:Name
        self.value = value # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:value, loaded_variable:self, loaded_variable:value, node:Assign, node:Attribute, node:Name

# ----------------------------------------------------------------------------------------
# 160.2165-detect-if-32-bit-or-64-bit-architecture.py
# ----------------------------------------------------------------------------------------
import sys # imperative_style (-> +4), import:sys, import_module:sys, node:Import, variety:2 (-> +4), whole_span:5 (-> +4)
if sys.maxsize > 2 ** 32: # binary_operator:Pow, comparison_operator:Gt, if (-> +3), if_test_atom:2, if_test_atom:32, if_test_atom:sys, literal:2, literal:32, loaded_variable:sys, magic_number:32, node:Attribute, node:BinOp, node:Compare, node:If (-> +3), node:Name, node:Num
    f64() # external_free_call:f64, free_call:f64, free_call_no_arguments:f64, free_call_without_result:f64, if_then_branch, node:Call, node:Expr, node:Name
else:
    f32() # external_free_call:f32, free_call:f32, free_call_no_arguments:f32, free_call_without_result:f32, if_else_branch, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 161.2098-multiply-all-the-elements-of-a-list.py
# ----------------------------------------------------------------------------------------
elements = [c * x for x in elements] # assignment, assignment_lhs_identifier:elements, assignment_rhs_atom:c, assignment_rhs_atom:elements, assignment_rhs_atom:x, binary_operator:Mult, comprehension:List, comprehension_for_count:1, flat_style, imperative_style, iteration_variable:x, loaded_variable:c, loaded_variable:elements, loaded_variable:x, local_scope:elements, local_scope:x, multiplication_operator, node:Assign, node:BinOp, node:ListComp, node:Name, node:comprehension, one_liner_style, scope:elements, scope:x, single_assignment:elements, update:elements:c, update:elements:x, update_by_assignment:elements:c, update_by_assignment:elements:x, update_by_assignment_with, update_with, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 162.2164-execute-procedures-depending-on-options.py
# ----------------------------------------------------------------------------------------
import sys # imperative_style (-> +4), import:sys, import_module:sys, node:Import, variety:2 (-> +4), whole_span:5 (-> +4)
if "b" in sys.argv[1:]: # comparison_operator:In, if (-> +1), if_test_atom:1, if_test_atom:sys, if_without_else (-> +1), literal:1, literal:Str, loaded_variable:sys, node:Attribute, node:Compare, node:If (-> +1), node:Name, node:Num, node:Slice, node:Str, node:Subscript, slice:1::, slice_lower:1, slice_step:, slice_upper:, value_attr:argv
    bat() # external_free_call:bat, free_call:bat, free_call_no_arguments:bat, free_call_without_result:bat, if_then_branch, node:Call, node:Expr, node:Name
if "f" in sys.argv[1:]: # comparison_operator:In, if (-> +1), if_test_atom:1, if_test_atom:sys, if_without_else (-> +1), literal:1, literal:Str, loaded_variable:sys, node:Attribute, node:Compare, node:If (-> +1), node:Name, node:Num, node:Slice, node:Str, node:Subscript, slice:1::, slice_lower:1, slice_step:, slice_upper:, value_attr:argv
    fox() # external_free_call:fox, free_call:fox, free_call_no_arguments:fox, free_call_without_result:fox, if_then_branch, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 163.2170-print-list-elements-by-group-of-2.py
# ----------------------------------------------------------------------------------------
for x in zip(list[::2], list[1::2]): # argument:, external_free_call:zip, for:x (-> +1), free_call:zip, global_scope:x (-> +1), imperative_style (-> +1), iteration_variable:x, literal:1, literal:2, loaded_variable:list, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:Call, node:For (-> +1), node:Name, node:Num, node:Slice, node:Subscript, scope:x (-> +1), slice:1::2, slice:::2, slice_lower:, slice_lower:1, slice_step:2, slice_upper:, variety:1 (-> +1), whole_span:2 (-> +1)
    print(x) # argument:x, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:x, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 163.3177-print-list-elements-by-group-of-2.py
# ----------------------------------------------------------------------------------------
from itertools import tee # global_scope:a (-> +6), global_scope:b (-> +6), import:itertools:tee, import_module:itertools, import_name:tee, node:ImportFrom, procedural_style (-> +6), scope:a (-> +6), scope:b (-> +6), variety:3 (-> +6), whole_span:7 (-> +6)
def pairwise(iterable): # function:pairwise (-> +3), function_line_count:4 (-> +3), function_parameter:iterable, function_parameter_flavor:arg, function_returning_something:pairwise (-> +3), impure_function:pairwise (-> +3), local_scope:a (-> +3), local_scope:b (-> +3), local_scope:iterable (-> +3), node:FunctionDef (-> +3), node:arg, scope:a (-> +3), scope:b (-> +3), scope:iterable (-> +3), shadowing_scope:a (-> +3), shadowing_scope:b (-> +3)
    a, b = tee(iterable) # argument:iterable, assignment:tee, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:iterable, external_free_call:tee, free_call:tee, literal:Tuple, loaded_variable:iterable, node:Assign, node:Call, node:Name, node:Tuple, parallel_assignment:2
    next(b, None) # argument:None, argument:b, external_free_call:next, free_call:next, free_call_without_result:next, literal:None, loaded_variable:b, node:Call, node:Expr, node:Name, node:NameConstant
    return zip(a, b) # argument:a, argument:b, external_free_call:zip, free_call:zip, free_tail_call:zip, loaded_variable:a, loaded_variable:b, node:Call, node:Name, node:Return, return
for a, b in pairwise(list): # argument:list, for:a (-> +1), for:b (-> +1), free_call:pairwise, internal_free_call:pairwise, iteration_variable:a, iteration_variable:b, literal:Tuple, loaded_variable:list, loop:for (-> +1), loop_with_late_exit:for (-> +1), node:Call, node:For (-> +1), node:Name, node:Tuple
    print(a, b) # argument:a, argument:b, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:a, loaded_variable:b, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 164.2169-open-url-in-default-browser.py
# ----------------------------------------------------------------------------------------
import webbrowser # flat_style (-> +1), imperative_style (-> +1), import:webbrowser, import_module:webbrowser, node:Import, one_liner_style (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
webbrowser.open(s) # argument:s, loaded_variable:s, loaded_variable:webbrowser, member_call:webbrowser:open, member_call_method:open, member_call_object:webbrowser, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 165.2149-last-element-of-list.py
# ----------------------------------------------------------------------------------------
x = items[-1] # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:-1, assignment_rhs_atom:items, flat_style, global_scope:x, imperative_style, index:-1, literal:-1, loaded_variable:items, negative_index:-1, node:Assign, node:Name, node:Num, node:Subscript, one_liner_style, scope:x, single_assignment:x, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 166.2272-concatenate-two-lists.py
# ----------------------------------------------------------------------------------------
ab = a + b # addition_operator, assignment:Add, assignment_lhs_identifier:ab, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, flat_style, global_scope:ab, imperative_style, loaded_variable:a, loaded_variable:b, node:Assign, node:BinOp, node:Name, one_liner_style, scope:ab, single_assignment:ab, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 167.2611-trim-prefix.py
# ----------------------------------------------------------------------------------------
t = s[s.startswith(p) and len(p) :] # argument:p, assignment, assignment_lhs_identifier:t, assignment_rhs_atom:p, assignment_rhs_atom:s, boolean_operator:And, external_free_call:len, flat_style, free_call:len, global_scope:t, imperative_style, loaded_variable:p, loaded_variable:s, member_call_method:startswith, node:Assign, node:Attribute, node:BoolOp, node:Call, node:Name, node:Slice, node:Subscript, one_liner_style, scope:t, single_assignment:t, slice:_::, slice_lower:_, slice_step:, slice_upper:, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 167.3175-trim-prefix.py
# ----------------------------------------------------------------------------------------
t = s.lstrip(p) # argument:p, assignment:lstrip, assignment_lhs_identifier:t, assignment_rhs_atom:p, assignment_rhs_atom:s, flat_style, global_scope:t, imperative_style, loaded_variable:p, loaded_variable:s, member_call_method:lstrip, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:t, single_assignment:t, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 168.2277-trim-suffix.py
# ----------------------------------------------------------------------------------------
t = s.rsplit(w, 1)[0] # argument:1, argument:w, assignment, assignment_lhs_identifier:t, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:s, assignment_rhs_atom:w, flat_style, global_scope:t, imperative_style, index:0, literal:0, literal:1, loaded_variable:s, loaded_variable:w, member_call:s:rsplit, member_call_method:rsplit, member_call_object:s, node:Assign, node:Attribute, node:Call, node:Name, node:Num, node:Subscript, one_liner_style, scope:t, single_assignment:t, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 168.3174-trim-suffix.py
# ----------------------------------------------------------------------------------------
t = s.rstrip(w) # argument:w, assignment:rstrip, assignment_lhs_identifier:t, assignment_rhs_atom:s, assignment_rhs_atom:w, flat_style, global_scope:t, imperative_style, loaded_variable:s, loaded_variable:w, member_call_method:rstrip, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:t, single_assignment:t, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 169.2233-string-length.py
# ----------------------------------------------------------------------------------------
n = len(s) # argument:s, assignment:len, assignment_lhs_identifier:n, assignment_rhs_atom:s, external_free_call:len, flat_style, free_call:len, global_scope:n, imperative_style, loaded_variable:s, node:Assign, node:Call, node:Name, one_liner_style, scope:n, single_assignment:n, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 170.2275-get-map-size.py
# ----------------------------------------------------------------------------------------
n = len(mymap) # argument:mymap, assignment:len, assignment_lhs_identifier:n, assignment_rhs_atom:mymap, external_free_call:len, flat_style, free_call:len, global_scope:n, imperative_style, loaded_variable:mymap, node:Assign, node:Call, node:Name, one_liner_style, scope:n, single_assignment:n, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 171.2446-add-an-element-at-the-end-of-a-list.py
# ----------------------------------------------------------------------------------------
s.append(x) # argument:x, flat_style, imperative_style, loaded_variable:s, loaded_variable:x, member_call:s:append, member_call_method:append, member_call_object:s, node:Attribute, node:Call, node:Expr, node:Name, one_liner_style, update:s:x, update_by_member_call:s:x, update_by_member_call_with:append, update_with:append, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 172.2442-insert-entry-in-map.py
# ----------------------------------------------------------------------------------------
m[k] = v # assignment, assignment_lhs_identifier:m, assignment_rhs_atom:v, flat_style, imperative_style, index:k, loaded_variable:k, loaded_variable:m, loaded_variable:v, node:Assign, node:Name, node:Subscript, one_liner_style, subscript_assignment:Name, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 173.2427-format-a-number-with-grouped-thousands.py
# ----------------------------------------------------------------------------------------
print("f'{1000:,}'") # argument:, external_free_call:print, flat_style, free_call:print, free_call_without_result:print, imperative_style, literal:Str, node:Call, node:Expr, node:Name, node:Str, one_liner_style, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 173.2428-format-a-number-with-grouped-thousands.py
# ----------------------------------------------------------------------------------------
print("format(1000, ',')") # argument:, external_free_call:print, flat_style, free_call:print, free_call_without_result:print, imperative_style, literal:Str, node:Call, node:Expr, node:Name, node:Str, one_liner_style, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 173.2429-format-a-number-with-grouped-thousands.py
# ----------------------------------------------------------------------------------------
print("'{:,}'.format(1000)") # argument:, external_free_call:print, flat_style, free_call:print, free_call_without_result:print, imperative_style, literal:Str, node:Call, node:Expr, node:Name, node:Str, one_liner_style, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 174.2687-make-http-post-request.py
# ----------------------------------------------------------------------------------------
from urllib import request, parse # flat_style (-> +3), global_scope:data (-> +3), global_scope:req (-> +3), global_scope:resp (-> +3), imperative_style (-> +3), import:urllib:parse, import:urllib:request, import_module:urllib, import_name:parse, import_name:request, node:ImportFrom, scope:data (-> +3), scope:req (-> +3), scope:resp (-> +3), variety:1 (-> +3), whole_span:4 (-> +3)
data = parse.urlencode("<your data dict>").encode() # argument:, assignment:encode, assignment_lhs_identifier:data, assignment_rhs_atom:parse, literal:Str, loaded_variable:parse, member_call:parse:encode, member_call:parse:urlencode, member_call_method:encode, member_call_method:urlencode, member_call_object:parse, method_chaining, node:Assign, node:Attribute, node:Call, node:Name, node:Str, single_assignment:data
req = request.Request(u, data=data, method="POST") # argument:, argument:data, argument:u, assignment:Request, assignment_lhs_identifier:req, assignment_rhs_atom:data, assignment_rhs_atom:request, assignment_rhs_atom:u, keyword_argument:data, keyword_argument:method, literal:Str, loaded_variable:data, loaded_variable:request, loaded_variable:u, member_call_method:Request, node:Assign, node:Attribute, node:Call, node:Name, node:Str, node:keyword, single_assignment:req
resp = request.urlopen(req) # argument:req, assignment:urlopen, assignment_lhs_identifier:resp, assignment_rhs_atom:req, assignment_rhs_atom:request, loaded_variable:req, loaded_variable:request, member_call_method:urlopen, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:resp

# ----------------------------------------------------------------------------------------
# 175.2613-bytes-to-hex-string.py
# ----------------------------------------------------------------------------------------
s = a.hex() # assignment:hex, assignment_lhs_identifier:s, assignment_rhs_atom:a, flat_style, global_scope:s, imperative_style, loaded_variable:a, member_call_method:hex, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:s, single_assignment:s, variety:1, whole_span:1

# ----------------------------------------------------------------------------------------
# 176.2614-hex-string-to-byte-array.py
# ----------------------------------------------------------------------------------------
a = bytearray.fromhex(s) # argument:s, assignment:fromhex, assignment_lhs_identifier:a, assignment_rhs_atom:bytearray, assignment_rhs_atom:s, flat_style, global_scope:a, imperative_style, loaded_variable:bytearray, loaded_variable:s, member_call_method:fromhex, node:Assign, node:Attribute, node:Call, node:Name, one_liner_style, scope:a, single_assignment:a, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 177.2709-find-files-with-a-given-list-of-filename-extensions.py
# ----------------------------------------------------------------------------------------
import os # flat_style (-> +2), global_scope:L (-> +2), global_scope:extensions (-> +2), imperative_style (-> +2), import:os, import_module:os, node:Import, scope:L (-> +2), scope:extensions (-> +2), variety:1 (-> +2), whole_span:3 (-> +2)
extensions = [".jpg", ".jpeg", ".png"] # assignment, assignment_lhs_identifier:extensions, literal:List, literal:Str, node:Assign, node:List, node:Name, node:Str, single_assignment:extensions
L = [f for f in os.listdir(D) if os.path.splitext(f)[1] in extensions] # argument:D, argument:f, assignment, assignment_lhs_identifier:L, assignment_rhs_atom:1, assignment_rhs_atom:D, assignment_rhs_atom:extensions, assignment_rhs_atom:f, assignment_rhs_atom:os, comparison_operator:In, comprehension:List, comprehension_for_count:1, filtered_comprehension, index:1, iteration_variable:f, literal:1, loaded_variable:D, loaded_variable:extensions, loaded_variable:f, loaded_variable:os, local_scope:f, member_call_method:listdir, member_call_method:splitext, node:Assign, node:Attribute, node:Call, node:Compare, node:ListComp, node:Name, node:Num, node:Subscript, node:comprehension, scope:f, single_assignment:L, value_attr:path

# ----------------------------------------------------------------------------------------
# 177.2725-find-files-with-a-given-list-of-filename-extensions.py
# ----------------------------------------------------------------------------------------
import re # flat_style (-> +6), global_scope:filtered_files (-> +6), imperative_style (-> +6), import:re, import_module:re, node:Import, scope:filtered_files (-> +6), variety:2 (-> +6), whole_span:7 (-> +6)
import os # import:os, import_module:os, node:Import
filtered_files = [ # assignment, assignment_lhs_identifier:filtered_files, comprehension:List, comprehension_for_count:2, local_scope:_, local_scope:dirpath, local_scope:filename, local_scope:filenames, node:Assign (-> +4), node:ListComp (-> +4), node:Name, scope:_, scope:dirpath, scope:filename, scope:filenames, single_assignment:filtered_files
    "{}/{}".format(dirpath, filename) # argument:dirpath, argument:filename, assignment_rhs_atom:dirpath, assignment_rhs_atom:filename, literal:Str, loaded_variable:dirpath, loaded_variable:filename, member_call_method:format, node:Attribute, node:Call, node:Name, node:Str
    for dirpath, _, filenames in os.walk(D) # argument:D, assignment_rhs_atom:D, assignment_rhs_atom:_, assignment_rhs_atom:dirpath, assignment_rhs_atom:filenames, assignment_rhs_atom:os, iteration_variable:_, iteration_variable:dirpath, iteration_variable:filenames, literal:Tuple, loaded_variable:D, loaded_variable:os, member_call_method:walk, node:Attribute, node:Call, node:Name, node:Tuple, node:comprehension
    for filename in filenames # assignment_rhs_atom:filename, assignment_rhs_atom:filenames, iteration_variable:filename, loaded_variable:filenames, node:Name, node:comprehension (-> +1)
    if re.match(r"^.*\.(?:jpg|jpeg|png)$", filename) # argument:, argument:filename, assignment_rhs_atom:filename, assignment_rhs_atom:re, filtered_comprehension, literal:Str, loaded_variable:filename, loaded_variable:re, member_call_method:match, node:Attribute, node:Call, node:Name, node:Str
]

# ----------------------------------------------------------------------------------------
# 177.3241-find-files-with-a-given-list-of-filename-extensions.py
# ----------------------------------------------------------------------------------------
import glob # flat_style (-> +2), imperative_style (-> +2), import:glob, import_module:glob, node:Import, one_liner_style (-> +2), variety:1 (-> +2), whole_span:3 (-> +2)
import itertools # import:itertools, import_module:itertools, node:Import
list(itertools.chain(*(glob.glob("*/**.%s" % ext) for ext in ["jpg", "jpeg", "png"]))) # argument:, binary_operator:Mod, composition, comprehension:Generator, comprehension_for_count:1, external_free_call:list, free_call:list, free_call_without_result:list, iteration_variable:ext, literal:List, literal:Str, loaded_variable:ext, loaded_variable:glob, loaded_variable:itertools, local_scope:ext, member_call_method:chain, member_call_method:glob, node:Attribute, node:BinOp, node:Call, node:Expr, node:GeneratorExp, node:List, node:Name, node:Starred, node:Str, node:comprehension, scope:ext, string_formatting_operator

# ----------------------------------------------------------------------------------------
# 178.2615-check-if-point-is-inside-rectangle.py
# ----------------------------------------------------------------------------------------
b = (x1 < x < x2) and (y1 < y < y2) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:x, assignment_rhs_atom:x1, assignment_rhs_atom:x2, assignment_rhs_atom:y, assignment_rhs_atom:y1, assignment_rhs_atom:y2, boolean_operator:And, chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, flat_style, global_scope:b, imperative_style, loaded_variable:x, loaded_variable:x1, loaded_variable:x2, loaded_variable:y, loaded_variable:y1, loaded_variable:y2, node:Assign, node:BoolOp, node:Compare, node:Name, one_liner_style, scope:b, single_assignment:b, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 179.2688-get-center-of-a-rectangle.py
# ----------------------------------------------------------------------------------------
center = ((x1 + x2) / 2, (y1 + y2) / 2) # addition_operator, assignment, assignment_lhs_identifier:center, assignment_rhs_atom:2, assignment_rhs_atom:x1, assignment_rhs_atom:x2, assignment_rhs_atom:y1, assignment_rhs_atom:y2, binary_operator:Add, binary_operator:Div, flat_style, global_scope:center, imperative_style, literal:2, literal:Tuple, loaded_variable:x1, loaded_variable:x2, loaded_variable:y1, loaded_variable:y2, node:Assign, node:BinOp, node:Name, node:Num, node:Tuple, one_liner_style, scope:center, single_assignment:center, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 179.2689-get-center-of-a-rectangle.py
# ----------------------------------------------------------------------------------------
from collections import namedtuple # flat_style (-> +2), global_scope:Point (-> +2), global_scope:center (-> +2), imperative_style (-> +2), import:collections:namedtuple, import_module:collections, import_name:namedtuple, node:ImportFrom, scope:Point (-> +2), scope:center (-> +2), variety:1 (-> +2), whole_span:3 (-> +2)
Point = namedtuple("Point", "x y") # argument:, assignment:namedtuple, assignment_lhs_identifier:Point, external_free_call:namedtuple, free_call:namedtuple, literal:Str, node:Assign, node:Call, node:Name, node:Str, single_assignment:Point
center = Point((x1 + x2) / 2, (y1 + y2) / 2) # addition_operator, argument:, assignment:Point, assignment_lhs_identifier:center, assignment_rhs_atom:2, assignment_rhs_atom:x1, assignment_rhs_atom:x2, assignment_rhs_atom:y1, assignment_rhs_atom:y2, binary_operator:Add, binary_operator:Div, external_free_call:Point, free_call:Point, literal:2, loaded_variable:x1, loaded_variable:x2, loaded_variable:y1, loaded_variable:y2, node:Assign, node:BinOp, node:Call, node:Name, node:Num, single_assignment:center

# ----------------------------------------------------------------------------------------
# 180.2612-list-files-in-directory.py
# ----------------------------------------------------------------------------------------
import os # flat_style (-> +1), global_scope:x (-> +1), imperative_style (-> +1), import:os, import_module:os, node:Import, one_liner_style (-> +1), scope:x (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
x = os.listdir(d) # argument:d, assignment:listdir, assignment_lhs_identifier:x, assignment_rhs_atom:d, assignment_rhs_atom:os, loaded_variable:d, loaded_variable:os, member_call_method:listdir, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:x

# ----------------------------------------------------------------------------------------
# 182.2658-quine-program.py
# ----------------------------------------------------------------------------------------
s = "s = %r\nprint(s%%s)" # assignment, assignment_lhs_identifier:s, flat_style (-> +1), global_scope:s (-> +1), imperative_style (-> +1), literal:Str, node:Assign, node:Name, node:Str, scope:s (-> +1), single_assignment:s, special_literal_string:s = %r\nprint(s%%s), variety:1 (-> +1), whole_span:2 (-> +1)
print(s % s) # argument:, binary_operator:Mod, external_free_call:print, free_call:print, free_call_without_result:print, loaded_variable:s, modulo_operator, node:BinOp, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 183.3025-make-http-put-request.py
# ----------------------------------------------------------------------------------------
requests # flat_style (-> +6), global_scope:content (-> +6), global_scope:content_type (-> +6), global_scope:data (-> +6), global_scope:headers (-> +6), global_scope:r (-> +6), global_scope:status_code (-> +6), imperative_style (-> +6), loaded_variable:requests, node:Expr, node:Name, scope:content (-> +6), scope:content_type (-> +6), scope:data (-> +6), scope:headers (-> +6), scope:r (-> +6), scope:status_code (-> +6), variety:2 (-> +6), whole_span:7 (-> +6)
import requests # import:requests, import_module:requests, node:Import
content_type = "text/plain" # assignment, assignment_lhs_identifier:content_type, literal:Str, node:Assign, node:Name, node:Str, single_assignment:content_type
headers = {"Content-Type": content_type} # assignment, assignment_lhs_identifier:headers, assignment_rhs_atom:content_type, literal:Dict, literal:Str, loaded_variable:content_type, node:Assign, node:Dict, node:Name, node:Str, single_assignment:headers
data = {} # assignment, assignment_lhs_identifier:data, empty_literal:Dict, literal:Dict, node:Assign, node:Dict, node:Name, single_assignment:data
r = requests.put(url, headers=headers, data=data) # argument:data, argument:headers, argument:url, assignment:put, assignment_lhs_identifier:r, assignment_rhs_atom:data, assignment_rhs_atom:headers, assignment_rhs_atom:requests, assignment_rhs_atom:url, keyword_argument:data, keyword_argument:headers, loaded_variable:data, loaded_variable:headers, loaded_variable:requests, loaded_variable:url, member_call_method:put, node:Assign, node:Attribute, node:Call, node:Name, node:keyword, single_assignment:r
status_code, content = r.status_code, r.content # assignment, assignment_lhs_identifier:content, assignment_lhs_identifier:status_code, assignment_rhs_atom:r, literal:Tuple, loaded_variable:r, node:Assign, node:Attribute, node:Name, node:Tuple, parallel_assignment:2

# ----------------------------------------------------------------------------------------
# 184.2701-tomorrow.py
# ----------------------------------------------------------------------------------------
from datetime import date, timedelta # flat_style (-> +1), imperative_style (-> +1), import:datetime:date, import:datetime:timedelta, import_module:datetime, import_name:date, import_name:timedelta, node:ImportFrom, one_liner_style (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
date.today() + timedelta(days=1) # addition_operator, argument:1, binary_operator:Add, external_free_call:timedelta, free_call:timedelta, free_call_with_keyword_argument:timedelta:days, keyword_argument:days, literal:1, loaded_variable:date, member_call_method:today, node:Attribute, node:BinOp, node:Call, node:Expr, node:Name, node:Num, node:keyword

# ----------------------------------------------------------------------------------------
# 185.2820-execute-function-in-30-seconds.py
# ----------------------------------------------------------------------------------------
import threading # flat_style (-> +2), global_scope:timer (-> +2), imperative_style (-> +2), import:threading, import_module:threading, node:Import, scope:timer (-> +2), variety:1 (-> +2), whole_span:3 (-> +2)
timer = threading.Timer(30.0, f, args=(42,)) # argument:, argument:30.0, argument:f, assignment:Timer, assignment_lhs_identifier:timer, assignment_rhs_atom:30.0, assignment_rhs_atom:42, assignment_rhs_atom:f, assignment_rhs_atom:threading, keyword_argument:args, literal:30.0, literal:42, literal:Tuple, loaded_variable:f, loaded_variable:threading, magic_number:30.0, magic_number:42, member_call_method:Timer, node:Assign, node:Attribute, node:Call, node:Name, node:Num, node:Tuple, node:keyword, single_assignment:timer
timer.start() # loaded_variable:timer, member_call:timer:start, member_call_method:start, member_call_object:timer, node:Attribute, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 186.2699-exit-program-cleanly.py
# ----------------------------------------------------------------------------------------
import sys # flat_style (-> +1), imperative_style (-> +1), import:sys, import_module:sys, node:Import, one_liner_style (-> +1), variety:2 (-> +1), whole_span:2 (-> +1)
sys.exit(0) # argument:0, literal:0, loaded_variable:sys, member_call:sys:exit, member_call_method:exit, member_call_object:sys, node:Attribute, node:Call, node:Expr, node:Name, node:Num

# ----------------------------------------------------------------------------------------
# 187.3261-disjoint-set.py
# ----------------------------------------------------------------------------------------
class UnionFind: # class:UnionFind (-> +14), class_method_count:4 (-> +14), node:ClassDef (-> +14), object_oriented_style (-> +14), variety:3 (-> +14), whole_span:15 (-> +14)
    def __init__(self, size): # function:__init__ (-> +2), function_line_count:3 (-> +2), function_parameter:self, function_parameter:size, function_parameter_flavor:arg, function_returning_nothing:__init__ (-> +2), instance_method:__init__ (-> +2), local_scope:self (-> +2), local_scope:size (-> +2), method:__init__ (-> +2), node:FunctionDef (-> +2), node:arg, scope:self (-> +2), scope:size (-> +2)
        self.rank = [0] * size # assignment:Mult, assignment_lhs_identifier:self, assignment_rhs_atom:0, assignment_rhs_atom:size, binary_operator:Mult, literal:0, literal:List, loaded_variable:self, loaded_variable:size, node:Assign, node:Attribute, node:BinOp, node:List, node:Name, node:Num, replication_operator:List
        self.p = [i for i in range(size)] # argument:size, assignment, assignment_lhs_identifier:self, assignment_rhs_atom:i, assignment_rhs_atom:size, comprehension:List, comprehension_for_count:1, external_free_call:range, free_call:range, iteration_variable:i, loaded_variable:i, loaded_variable:self, loaded_variable:size, local_scope:i, node:Assign, node:Attribute, node:Call, node:ListComp, node:Name, node:comprehension, range:size, scope:i
    def find_set(self, i): # function:find_set (-> +5), function_line_count:6 (-> +5), function_parameter:i, function_parameter:self, function_parameter_flavor:arg, function_returning_something:find_set (-> +5), instance_method:find_set (-> +5), local_scope:i (-> +5), local_scope:self (-> +5), method:find_set (-> +5), node:FunctionDef (-> +5), node:arg, scope:i (-> +5), scope:self (-> +5)
        if self.p[i] == i: # comparison_operator:Eq, if (-> +4), if_test_atom:i, if_test_atom:self, index:i, loaded_variable:i, loaded_variable:self, node:Attribute, node:Compare, node:If (-> +4), node:Name, node:Subscript, value_attr:p
            return i # if_then_branch, loaded_variable:i, node:Name, node:Return, return:i
        else:
            self.p[i] = self.find_set(self.p[i]) # argument:, assignment:find_set, assignment_rhs_atom:i, assignment_rhs_atom:self, if_else_branch (-> +1), index:i, loaded_variable:i, loaded_variable:self, member_call_method:find_set, node:Assign, node:Attribute, node:Call, node:Name, node:Subscript, subscript_assignment:Name, value_attr:p
            return self.p[i] # index:i, loaded_variable:i, loaded_variable:self, node:Attribute, node:Name, node:Return, node:Subscript, return, value_attr:p
    def is_same_set(self, i, j): # function:is_same_set (-> +1), function_line_count:2 (-> +1), function_parameter:i, function_parameter:j, function_parameter:self, function_parameter_flavor:arg, function_returning_something:is_same_set (-> +1), instance_method:is_same_set (-> +1), local_scope:i (-> +1), local_scope:j (-> +1), local_scope:self (-> +1), method:is_same_set (-> +1), node:FunctionDef (-> +1), node:arg, scope:i (-> +1), scope:j (-> +1), scope:self (-> +1)
        return self.find_set(i) == self.find_set(j) # argument:i, argument:j, comparison_operator:Eq, loaded_variable:i, loaded_variable:j, loaded_variable:self, member_call_method:find_set, node:Attribute, node:Call, node:Compare, node:Name, node:Return, return
    def union_set(self, i, j): # function:union_set (-> +2), function_line_count:3 (-> +2), function_parameter:i, function_parameter:j, function_parameter:self, function_parameter_flavor:arg, function_returning_nothing:union_set (-> +2), instance_method:union_set (-> +2), local_scope:i (-> +2), local_scope:j (-> +2), local_scope:self (-> +2), local_scope:x (-> +2), local_scope:y (-> +2), method:union_set (-> +2), node:FunctionDef (-> +2), node:arg, scope:i (-> +2), scope:j (-> +2), scope:self (-> +2), scope:x (-> +2), scope:y (-> +2)
        if not self.is_same_set(i, j): # argument:i, argument:j, if (-> +1), if_test_atom:i, if_test_atom:j, if_test_atom:self, if_without_else (-> +1), loaded_variable:i, loaded_variable:j, loaded_variable:self, member_call_method:is_same_set, node:Attribute, node:Call, node:If (-> +1), node:Name, node:UnaryOp, unary_operator:Not
            x, y = self.find_set(i), self.find_set(j) # argument:i, argument:j, assignment, assignment_lhs_identifier:x, assignment_lhs_identifier:y, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:self, if_then_branch, literal:Tuple, loaded_variable:i, loaded_variable:j, loaded_variable:self, member_call_method:find_set, node:Assign, node:Attribute, node:Call, node:Name, node:Tuple, parallel_assignment:2

# ----------------------------------------------------------------------------------------
# 188.3171-matrix-multiplication.py
# ----------------------------------------------------------------------------------------
import numpy as np # flat_style (-> +1), global_scope:c (-> +1), imperative_style (-> +1), import:numpy, import_module:numpy, node:Import, one_liner_style (-> +1), scope:c (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
c = a @ b # assignment:MatMult, assignment_lhs_identifier:c, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:MatMult, loaded_variable:a, loaded_variable:b, node:Assign, node:BinOp, node:Name, single_assignment:c

# ----------------------------------------------------------------------------------------
# 188.3284-matrix-multiplication.py
# ----------------------------------------------------------------------------------------
import numpy as np # flat_style (-> +1), global_scope:c (-> +1), imperative_style (-> +1), import:numpy, import_module:numpy, node:Import, one_liner_style (-> +1), scope:c (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
c = np.matmul(a, b) # argument:a, argument:b, assignment:matmul, assignment_lhs_identifier:c, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:np, loaded_variable:a, loaded_variable:b, loaded_variable:np, member_call_method:matmul, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:c

# ----------------------------------------------------------------------------------------
# 189.3236-filter-and-transform-list.py
# ----------------------------------------------------------------------------------------
y = [T(e) for e in x if P(e)] # argument:e, assignment, assignment_lhs_identifier:y, assignment_rhs_atom:e, assignment_rhs_atom:x, comprehension:List, comprehension_for_count:1, external_free_call:P, external_free_call:T, filtered_comprehension, flat_style, free_call:P, free_call:T, imperative_style, iteration_variable:e, loaded_variable:e, loaded_variable:x, local_scope:e, local_scope:y, node:Assign, node:Call, node:ListComp, node:Name, node:comprehension, one_liner_style, scope:e, scope:y, single_assignment:y, variety:0, whole_span:1

# ----------------------------------------------------------------------------------------
# 191.3403-check-if-any-value-in-a-list-is-larger-than-a-limit.py
# ----------------------------------------------------------------------------------------
if any(v > x for v in a): # argument:, comparison_operator:Gt, comprehension:Generator, comprehension_for_count:1, external_free_call:any, free_call:any, if (-> +1), if_test_atom:a, if_test_atom:v, if_test_atom:x, if_without_else (-> +1), imperative_style (-> +1), iteration_variable:v, loaded_variable:a, loaded_variable:v, loaded_variable:x, local_scope:v, node:Call, node:Compare, node:GeneratorExp, node:If (-> +1), node:Name, node:comprehension, scope:v, variety:1 (-> +1), whole_span:2 (-> +1)
    f() # external_free_call:f, free_call:f, free_call_no_arguments:f, free_call_without_result:f, if_then_branch, node:Call, node:Expr, node:Name

# ----------------------------------------------------------------------------------------
# 197.3457-get-a-list-of-lines-from-a-file.py
# ----------------------------------------------------------------------------------------
with open(path) as f: # argument:path, external_free_call:open, flat_style (-> +1), free_call:open, global_scope:lines (-> +1), imperative_style (-> +1), loaded_variable:path, node:Call, node:Name, node:With (-> +1), node:withitem, scope:lines (-> +1), variety:1 (-> +1), whole_span:2 (-> +1)
    lines = f.readlines() # assignment:readlines, assignment_lhs_identifier:lines, assignment_rhs_atom:f, loaded_variable:f, member_call_method:readlines, node:Assign, node:Attribute, node:Call, node:Name, single_assignment:lines
