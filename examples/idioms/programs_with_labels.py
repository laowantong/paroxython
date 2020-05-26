# ----------------------------------------------------------------------------------------
# 001.0003-print-hello-world.py
# ----------------------------------------------------------------------------------------
from __future__ import print_function # import:__future__:print_function, import_module:__future__, import_name:print_function, whole_span:2 (-> +1)
print("Hello World") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str

# ----------------------------------------------------------------------------------------
# 001.1159-print-hello-world.py
# ----------------------------------------------------------------------------------------
print("Hello World") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, whole_span:1

# ----------------------------------------------------------------------------------------
# 002.0011-print-hello-10-times.py
# ----------------------------------------------------------------------------------------
for i in range(10): # call_argument:10, external_free_call:range, for:i (-> +1), for_range:10 (-> +1), free_call:range, literal:10, loop:for (-> +1), loop_with_late_exit:for (-> +1), range:10, whole_span:2 (-> +1)
    print("Hello") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str

# ----------------------------------------------------------------------------------------
# 002.1493-print-hello-10-times.py
# ----------------------------------------------------------------------------------------
print("Hello\n" * 10) # binary_operator:Mult, call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:10, literal:Str, replication_operator:Str, whole_span:1

# ----------------------------------------------------------------------------------------
# 002.3117-print-hello-10-times.py
# ----------------------------------------------------------------------------------------
print("Hello\n" * 10) # binary_operator:Mult, call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:10, literal:Str, replication_operator:Str, whole_span:1

# ----------------------------------------------------------------------------------------
# 003.0019-create-a-procedure.py
# ----------------------------------------------------------------------------------------
def finish(name): # function:finish (-> +1), function_argument:name, function_argument_flavor:arg, function_returning_nothing:finish (-> +1), whole_span:2 (-> +1)
    print("My job here is done. Goodbye " + name) # binary_operator:Add, call_argument:, concatenation_operator:Str, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str

# ----------------------------------------------------------------------------------------
# 003.2372-create-a-procedure.py
# ----------------------------------------------------------------------------------------
def a(): # function:a (-> +1), function_returning_nothing:a (-> +1), function_without_arguments:a (-> +1), whole_span:2 (-> +1)
    pass # null_operation

# ----------------------------------------------------------------------------------------
# 004.0024-create-a-function-which-returns-the-square-of-an-integer.py
# ----------------------------------------------------------------------------------------
def square(x): # function:square (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:square (-> +1), whole_span:2 (-> +1)
    return x * x # binary_operator:Mult, multiplication_operator, return

# ----------------------------------------------------------------------------------------
# 004.2921-create-a-function-which-returns-the-square-of-an-integer.py
# ----------------------------------------------------------------------------------------
def square(x): # function:square (-> +1), function_argument:x, function_argument_flavor:arg, function_returning_something:square (-> +1), whole_span:2 (-> +1)
    return x ** 2 # binary_operator:Pow, literal:2, return

# ----------------------------------------------------------------------------------------
# 005.0663-create-a-2d-point-data-structure.py
# ----------------------------------------------------------------------------------------
from dataclasses import dataclass # import:dataclasses:dataclass, import_module:dataclasses, import_name:dataclass, whole_span:2 (-> +1)
@dataclass # class:Point
class Point:
    x: float
    y: float

# ----------------------------------------------------------------------------------------
# 006.0032-iterate-over-list-values.py
# ----------------------------------------------------------------------------------------
for x in items: # for:x (-> +1), for_each (-> +1), loop:for (-> +1), loop_with_late_exit:for (-> +1), whole_span:2 (-> +1)
    doSomething(x) # call_argument:x, external_free_call:doSomething, free_call:doSomething, free_call_without_result:doSomething

# ----------------------------------------------------------------------------------------
# 007.0183-iterate-over-list-indexes-and-values.py
# ----------------------------------------------------------------------------------------
for i, x in enumerate(items): # call_argument:items, external_free_call:enumerate, for:i (-> +1), for:x (-> +1), for_indexes_elements (-> +1), free_call:enumerate, literal:Tuple, loop:for (-> +1), loop_with_late_exit:for (-> +1), whole_span:2 (-> +1)
    print(i, x) # call_argument:i, call_argument:x, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 008.0039-initialize-a-new-map-associative-array.py
# ----------------------------------------------------------------------------------------
x = {"one": 1, "two": 2} # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:1, assignment_rhs_atom:2, literal:1, literal:2, literal:Dict, literal:Str, single_assignment:x, whole_span:1

# ----------------------------------------------------------------------------------------
# 009.1410-create-a-binary-tree-data-structure.py
# ----------------------------------------------------------------------------------------
class Node: # class:Node (-> +4), whole_span:5 (-> +4)
    def __init__(self, data): # function:__init__ (-> +3), function_argument:data, function_argument:self, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), method:__init__ (-> +3)
        self.data = data # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:data
        self.left = None # assignment:None, assignment_lhs_identifier:self, assignment_rhs_atom:None, literal:None
        self.right = None # assignment:None, assignment_lhs_identifier:self, assignment_rhs_atom:None, literal:None

# ----------------------------------------------------------------------------------------
# 009.3176-create-a-binary-tree-data-structure.py
# ----------------------------------------------------------------------------------------
class Node: # class:Node (-> +4), whole_span:5 (-> +4)
    def __init__(self, data, left_child, right_child): # function:__init__ (-> +3), function_argument:data, function_argument:left_child, function_argument:right_child, function_argument:self, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), method:__init__ (-> +3)
        self.data = data # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:data
        self._left_child = left_child # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:left_child
        self._right_child = right_child # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:right_child

# ----------------------------------------------------------------------------------------
# 010.0182-shuffle-a-list.py
# ----------------------------------------------------------------------------------------
from random import shuffle # import:random:shuffle, import_module:random, import_name:shuffle, whole_span:2 (-> +1)
shuffle(x) # call_argument:x, external_free_call:shuffle, free_call:shuffle, free_call_without_result:shuffle

# ----------------------------------------------------------------------------------------
# 010.1478-shuffle-a-list.py
# ----------------------------------------------------------------------------------------
import random # import:random, import_module:random, whole_span:2 (-> +1)
random.shuffle(list) # call_argument:list, member_call:shuffle, member_call_object:random, member_call_without_result:shuffle

# ----------------------------------------------------------------------------------------
# 011.0047-pick-a-random-element-from-a-list.py
# ----------------------------------------------------------------------------------------
import random # import:random, import_module:random, whole_span:2 (-> +1)
random.choice(x) # call_argument:x, member_call:choice, member_call_object:random, member_call_without_result:choice

# ----------------------------------------------------------------------------------------
# 012.0181-check-if-list-contains-a-value.py
# ----------------------------------------------------------------------------------------
x in list # comparison_operator:In, whole_span:1

# ----------------------------------------------------------------------------------------
# 013.0574-iterate-over-map-keys-and-values.py
# ----------------------------------------------------------------------------------------
for k, v in mymap.items(): # for:k (-> +1), for:v (-> +1), literal:Tuple, loop:for (-> +1), loop_with_late_exit:for (-> +1), member_call:items, whole_span:2 (-> +1)
    print(k, v) # call_argument:k, call_argument:v, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 014.0185-pick-uniformly-a-random-floating-point-number-in-ab.py
# ----------------------------------------------------------------------------------------
import random # import:random, import_module:random, whole_span:3 (-> +2)
def pick(a, b): # function:pick (-> +1), function_argument:a, function_argument:b, function_argument_flavor:arg, function_returning_something:pick (-> +1)
    return random.randrange(a, b) # call_argument:a, call_argument:b, member_call:randrange, member_call_object:random, return

# ----------------------------------------------------------------------------------------
# 014.3410-pick-uniformly-a-random-floating-point-number-in-ab.py
# ----------------------------------------------------------------------------------------
import random # import:random, import_module:random, whole_span:2 (-> +1)
random.uniform(a, b) # call_argument:a, call_argument:b, member_call:uniform, member_call_object:random, member_call_without_result:uniform

# ----------------------------------------------------------------------------------------
# 015.0184-pick-uniformly-a-random-integer-in-ab.py
# ----------------------------------------------------------------------------------------
import random # import:random, import_module:random, whole_span:2 (-> +1)
random.randint(a, b) # call_argument:a, call_argument:b, member_call:randint, member_call_object:random, member_call_without_result:randint

# ----------------------------------------------------------------------------------------
# 016.1530-depth-first-traversing-of-a-binary-tree.py
# ----------------------------------------------------------------------------------------
def dfs(bt): # body_recursive_function:dfs (-> +5), function:dfs (-> +5), function_argument:bt, function_argument_flavor:arg, function_returning_nothing:dfs (-> +5), recursive_function:dfs (-> +5), whole_span:6 (-> +5)
    if bt is None: # comparison_operator:Is, if (-> +1), if_guard (-> +1), if_test_atom:None, if_test_atom:bt, if_without_else (-> +1), literal:None
        return # if_then_branch, return:None
    dfs(bt.left) # call_argument:, free_call:dfs, free_call_without_result:dfs, internal_free_call:dfs
    f(bt) # call_argument:bt, external_free_call:f, free_call:f, free_call_without_result:f
    dfs(bt.right) # call_argument:, free_call:dfs, free_call_without_result:dfs, internal_free_call:dfs

# ----------------------------------------------------------------------------------------
# 017.1103-create-a-tree-data-structure.py
# ----------------------------------------------------------------------------------------
class Node(object): # class:Node (-> +3), whole_span:4 (-> +3)
    def __init__(self, value, *children): # function:__init__ (-> +2), function_argument:children, function_argument:self, function_argument:value, function_argument_flavor:arg, function_argument_flavor:vararg, function_returning_nothing:__init__ (-> +2), instance_method:__init__ (-> +2), method:__init__ (-> +2)
        self.value = value # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:value
        self.children = list(children) # assignment:list, assignment_lhs_identifier:self, assignment_rhs_atom:children, call_argument:children, external_free_call:list, free_call:list

# ----------------------------------------------------------------------------------------
# 018.2084-depth-first-traversing-of-a-tree.py
# ----------------------------------------------------------------------------------------
def DFS(f, root): # body_recursive_function:DFS (-> +3), function:DFS (-> +3), function_argument:f, function_argument:root, function_argument_flavor:arg, function_returning_nothing:DFS (-> +3), higher_order_function:f (-> +3), recursive_function:DFS (-> +3), whole_span:4 (-> +3)
    f(root) # call_argument:root, external_free_call:f, free_call:f, free_call_without_result:f
    for child in root: # for:child (-> +1), for_each (-> +1), loop:for (-> +1), loop_with_late_exit:for (-> +1)
        DFS(f, child) # call_argument:child, call_argument:f, free_call:DFS, free_call_without_result:DFS, internal_free_call:DFS

# ----------------------------------------------------------------------------------------
# 019.0197-reverse-a-list.py
# ----------------------------------------------------------------------------------------
x = reversed(x) # assignment:reversed, assignment_lhs_identifier:x, assignment_rhs_atom:x, call_argument:x, external_free_call:reversed, free_call:reversed, single_assignment:x, whole_span:1

# ----------------------------------------------------------------------------------------
# 019.1983-reverse-a-list.py
# ----------------------------------------------------------------------------------------
y = x[::-1] # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:-1, assignment_rhs_atom:x, literal:-1, single_assignment:y, slice:::-1, slice_lower:, slice_step:-1, slice_upper:, whole_span:1

# ----------------------------------------------------------------------------------------
# 019.3164-reverse-a-list.py
# ----------------------------------------------------------------------------------------
x.reverse() # member_call:reverse, member_call_object:x, member_call_without_result:reverse, whole_span:1

# ----------------------------------------------------------------------------------------
# 020.0573-return-two-values.py
# ----------------------------------------------------------------------------------------
def search(m, x): # function:search (-> +3), function_argument:m, function_argument:x, function_argument_flavor:arg, function_returning_something:search (-> +3), whole_span:4 (-> +3)
    for idx, item in enumerate(m): # call_argument:m, external_free_call:enumerate, for:idx (-> +2), for:item (-> +2), for_indexes_elements (-> +2), free_call:enumerate, literal:Tuple, loop:for (-> +2), loop_with_early_exit:for:return (-> +2), loop_with_return:for (-> +2)
        if x in item: # comparison_operator:In, if (-> +1), if_test_atom:item, if_test_atom:x, if_without_else (-> +1)
            return idx, item.index(x) # call_argument:x, if_then_branch, literal:Tuple, member_call:index, return

# ----------------------------------------------------------------------------------------
# 021.0084-swap-values-of-variables-a-and-b.py
# ----------------------------------------------------------------------------------------
a, b = b, a # assignment, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:a, assignment_rhs_atom:b, literal:Tuple, parallel_assignment:2, swap, update:a:b, update:b:a, update_by_assignment:a:b, update_by_assignment:b:a, update_by_assignment_with, update_with, whole_span:1

# ----------------------------------------------------------------------------------------
# 022.0243-convert-string-to-integer.py
# ----------------------------------------------------------------------------------------
i = int(s) # assignment:int, assignment_lhs_identifier:i, assignment_rhs_atom:s, call_argument:s, external_free_call:int, free_call:int, single_assignment:i, whole_span:1

# ----------------------------------------------------------------------------------------
# 023.1102-convert-real-number-to-string-with-2-decimal-places.py
# ----------------------------------------------------------------------------------------
s = "{:.2f}".format(x) # assignment:format, assignment_lhs_identifier:s, assignment_rhs_atom:x, call_argument:x, literal:Str, member_call:format, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 024.0664-assign-to-string-the-japanese-word-.py
# ----------------------------------------------------------------------------------------
s = "ネコ" # assignment, assignment_lhs_identifier:s, literal:Str, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 025.0195-send-a-value-to-another-thread.py
# ----------------------------------------------------------------------------------------
import Queue # import:Queue, import_module:Queue, whole_span:6 (-> +5)
q = Queue() # assignment:Queue, assignment_lhs_identifier:q, external_free_call:Queue, free_call:Queue, free_call_without_arguments:Queue, single_assignment:q
t = Thread(target=worker) # assignment:Thread, assignment_lhs_identifier:t, assignment_rhs_atom:worker, external_free_call:Thread, free_call:Thread, single_assignment:t
t.daemon = True # assignment:True, assignment_lhs_identifier:t, assignment_rhs_atom:True, literal:True
t.start() # member_call:start, member_call_object:t, member_call_without_result:start
q.put("Alan") # call_argument:, literal:Str, member_call:put, member_call_object:q, member_call_without_result:put

# ----------------------------------------------------------------------------------------
# 026.0194-create-a-2-dimensional-array.py
# ----------------------------------------------------------------------------------------
x = [[0 for j in xrange(n)] for i in xrange(m)] # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:0, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:m, assignment_rhs_atom:n, call_argument:m, call_argument:n, comprehension:List, comprehension_for_count:1, external_free_call:xrange, free_call:xrange, literal:0, single_assignment:x, whole_span:1

# ----------------------------------------------------------------------------------------
# 027.0192-create-a-3-dimensional-array.py
# ----------------------------------------------------------------------------------------
x = [[[0 for k in xrange(p)] for j in xrange(n)] for i in xrange(m)] # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:0, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:k, assignment_rhs_atom:m, assignment_rhs_atom:n, assignment_rhs_atom:p, call_argument:m, call_argument:n, call_argument:p, comprehension:List, comprehension_for_count:1, external_free_call:xrange, free_call:xrange, literal:0, single_assignment:x, whole_span:1

# ----------------------------------------------------------------------------------------
# 027.0193-create-a-3-dimensional-array.py
# ----------------------------------------------------------------------------------------
import numpy # import:numpy, import_module:numpy, whole_span:2 (-> +1)
x = numpy.zeros((m, n, p)) # assignment:zeros, assignment_lhs_identifier:x, assignment_rhs_atom:m, assignment_rhs_atom:n, assignment_rhs_atom:numpy, assignment_rhs_atom:p, call_argument:, literal:Tuple, member_call:zeros, single_assignment:x

# ----------------------------------------------------------------------------------------
# 028.0350-sort-by-a-property.py
# ----------------------------------------------------------------------------------------
items = sorted(items, key=lambda x: x.p) # assignment:sorted, assignment_lhs_identifier:items, assignment_rhs_atom:items, assignment_rhs_atom:x, call_argument:items, external_free_call:sorted, free_call:sorted, function_argument:x, function_argument_flavor:arg, lambda_function, single_assignment:items, update:items:x, update_by_assignment:items:x, update_by_assignment_with:sorted, update_with:sorted, whole_span:1

# ----------------------------------------------------------------------------------------
# 029.0199-remove-item-from-list-by-its-index.py
# ----------------------------------------------------------------------------------------
del items[i] # index:i, whole_span:1

# ----------------------------------------------------------------------------------------
# 030.0189-parallelize-execution-of-1000-independent-tasks.py
# ----------------------------------------------------------------------------------------
from multiprocessing import Pool # import:multiprocessing:Pool, import_module:multiprocessing, import_name:Pool, whole_span:4 (-> +3)
pool = Pool() # assignment:Pool, assignment_lhs_identifier:pool, external_free_call:Pool, free_call:Pool, free_call_without_arguments:Pool, single_assignment:pool
for i in range(1, 1001): # call_argument:1, call_argument:1001, external_free_call:range, for:i (-> +1), for_range:1:1001 (-> +1), free_call:range, literal:1, literal:1001, loop:for (-> +1), loop_with_late_exit:for (-> +1), range:1:1001
    pool.apply_async(f, [i]) # call_argument:, call_argument:f, literal:List, member_call:apply_async, member_call_object:pool, member_call_without_result:apply_async

# ----------------------------------------------------------------------------------------
# 031.0188-recursive-factorial-simple.py
# ----------------------------------------------------------------------------------------
def f(i): # body_recursive_function:f (-> +4), function:f (-> +4), function_argument:i, function_argument_flavor:arg, function_returning_something:f (-> +4), recursive_function:f (-> +4), whole_span:5 (-> +4)
    if i == 0: # comparison_operator:Eq, if (-> +3), if_test_atom:0, if_test_atom:i, literal:0
        return 1 # if_then_branch, literal:1, return:1
    else:
        return i * f(i - 1) # binary_operator:Mult, binary_operator:Sub, call_argument:, free_call:f, if_else_branch, internal_free_call:f, literal:1, multiplication_operator, return

# ----------------------------------------------------------------------------------------
# 032.0196-integer-exponentiation-by-squaring.py
# ----------------------------------------------------------------------------------------
def exp(x, n): # function:exp (-> +1), function_argument:n, function_argument:x, function_argument_flavor:arg, function_returning_something:exp (-> +1), whole_span:2 (-> +1)
    return x ** n # binary_operator:Pow, return

# ----------------------------------------------------------------------------------------
# 033.1420-atomically-read-and-update-variable.py
# ----------------------------------------------------------------------------------------
import threading # import:threading, import_module:threading, whole_span:7 (-> +6)
lock = threading.Lock() # assignment:Lock, assignment_lhs_identifier:lock, assignment_rhs_atom:threading, member_call:Lock, single_assignment:lock
lock.acquire() # member_call:acquire, member_call_object:lock, member_call_without_result:acquire
try: # try (-> +3)
    x = f(x) # assignment:f, assignment_lhs_identifier:x, assignment_rhs_atom:x, call_argument:x, external_free_call:f, free_call:f, single_assignment:x
finally:
    lock.release() # member_call:release, member_call_object:lock

# ----------------------------------------------------------------------------------------
# 034.0625-create-a-set-of-objects.py
# ----------------------------------------------------------------------------------------
class T(object): # class:T (-> +1), whole_span:3 (-> +2)
    pass # null_operation
x = set(T()) # assignment:set, assignment_lhs_identifier:x, call_argument:, composition, external_free_call:T, external_free_call:set, free_call:T, free_call:set, free_call_without_arguments:T, single_assignment:x

# ----------------------------------------------------------------------------------------
# 035.0667-first-class-function--compose.py
# ----------------------------------------------------------------------------------------
def compose(f, g): # function:compose (-> +1), function_argument:f, function_argument:g, function_argument_flavor:arg, function_returning_something:compose (-> +1), higher_order_function:f (-> +1), higher_order_function:g (-> +1), whole_span:2 (-> +1)
    return lambda a: g(f(a)) # call_argument:, call_argument:a, composition, external_free_call:f, external_free_call:g, free_call:f, free_call:g, function_argument:a, function_argument_flavor:arg, lambda_function, return

# ----------------------------------------------------------------------------------------
# 036.0670-first-class-function--generic-composition.py
# ----------------------------------------------------------------------------------------
def compose(f, g): # function:compose (-> +1), function_argument:f, function_argument:g, function_argument_flavor:arg, function_returning_something:compose (-> +1), higher_order_function:f (-> +1), higher_order_function:g (-> +1), whole_span:2 (-> +1)
    return lambda x: g(f(x)) # call_argument:, call_argument:x, composition, external_free_call:f, external_free_call:g, free_call:f, free_call:g, function_argument:x, function_argument_flavor:arg, lambda_function, return

# ----------------------------------------------------------------------------------------
# 037.0671-currying.py
# ----------------------------------------------------------------------------------------
from functools import partial # import:functools:partial, import_module:functools, import_name:partial, whole_span:6 (-> +5)
def f(a): # closure:f (-> +3), function:f (-> +3), function_argument:a, function_argument_flavor:arg, function_returning_something:f (-> +3), nested_function:f (-> +3)
    def add(b): # function:add (-> +1), function_argument:b, function_argument_flavor:arg, function_returning_something:add (-> +1)
        return a + b # addition_operator, binary_operator:Add, return
    return add # return:add
print(f(2)(1)) # call_argument:, call_argument:1, call_argument:2, composition, external_free_call:print, free_call:f, free_call:print, free_call_without_result:print, internal_free_call:f, literal:1, literal:2

# ----------------------------------------------------------------------------------------
# 038.0186-extract-a-substring.py
# ----------------------------------------------------------------------------------------
t = s[i:j] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:s, single_assignment:t, slice:i:j:, slice_lower:i, slice_step:, slice_upper:j, whole_span:1

# ----------------------------------------------------------------------------------------
# 039.0571-check-if-string-contains-a-word.py
# ----------------------------------------------------------------------------------------
ok = word in s # assignment, assignment_lhs_identifier:ok, assignment_rhs_atom:s, assignment_rhs_atom:word, comparison_operator:In, single_assignment:ok, whole_span:1

# ----------------------------------------------------------------------------------------
# 040.2279-graph-with-adjacency-lists.py
# ----------------------------------------------------------------------------------------
from collections import defaultdict # import:collections:defaultdict, import_module:collections, import_name:defaultdict, whole_span:13 (-> +12)
class Vertex(set): # class:Vertex (-> +1)
    pass # null_operation
class Graph(defaultdict): # class:Graph (-> +8)
    def __init__(self, *paths): # function:__init__ (-> +3), function_argument:paths, function_argument:self, function_argument_flavor:arg, function_argument_flavor:vararg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), method:__init__ (-> +3)
        self.default_factory = Vertex # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:Vertex
        for path in paths: # for:path (-> +1), for_each (-> +1), loop:for (-> +1), loop_with_late_exit:for (-> +1)
            self.make_path(path) # call_argument:path, member_call:make_path, member_call_object:self, member_call_without_result:make_path
    def make_path(self, labels): # function:make_path (-> +3), function_argument:labels, function_argument:self, function_argument_flavor:arg, function_returning_nothing:make_path (-> +3), instance_method:make_path (-> +3), method:make_path (-> +3)
        for l1, l2 in zip(labels, labels[1:]): # call_argument:, call_argument:labels, external_free_call:zip, for:l1 (-> +2), for:l2 (-> +2), free_call:zip, literal:1, literal:Tuple, loop:for (-> +2), loop_with_late_exit:for (-> +2), slice:1::, slice_lower:1, slice_step:, slice_upper:
            self[l1].add(l2) # call_argument:l2, index:l1, member_call:add, member_call_without_result:add
            self[l2].add(l1) # call_argument:l1, index:l2, member_call:add, member_call_without_result:add
G = Graph((0, 1, 2, 3), (1, 4, 2)) # assignment:Graph, assignment_lhs_identifier:G, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:2, assignment_rhs_atom:3, assignment_rhs_atom:4, call_argument:, external_free_call:Graph, free_call:Graph, literal:0, literal:1, literal:2, literal:3, literal:4, literal:Tuple, single_assignment:G

# ----------------------------------------------------------------------------------------
# 041.0187-reverse-a-string.py
# ----------------------------------------------------------------------------------------
t = s.decode("utf8")[::-1].encode("utf8") # assignment:encode, assignment_lhs_identifier:t, assignment_rhs_atom:-1, assignment_rhs_atom:s, call_argument:, literal:-1, literal:Str, member_call:decode, member_call:encode, member_call_object:s, single_assignment:t, slice:::-1, slice_lower:, slice_step:-1, slice_upper:, whole_span:1

# ----------------------------------------------------------------------------------------
# 041.2714-reverse-a-string.py
# ----------------------------------------------------------------------------------------
t = s[::-1] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:-1, assignment_rhs_atom:s, literal:-1, single_assignment:t, slice:::-1, slice_lower:, slice_step:-1, slice_upper:, whole_span:1

# ----------------------------------------------------------------------------------------
# 042.1264-continue-outer-loop.py
# ----------------------------------------------------------------------------------------
for v in a: # for:v (-> +7), for_each (-> +7), loop:for (-> +7), loop_with_early_exit:for:raise (-> +7), loop_with_raise:for (-> +7), whole_span:8 (-> +7)
    try: # try (-> +6), try_except:Exception (-> +6), try_raise:Exception (-> +6)
        for u in b: # for:u (-> +2), for_each (-> +2), loop:for (-> +2), loop_with_early_exit:for:raise (-> +2), loop_with_raise:for (-> +2), nested_for:1 (-> +2)
            if v == u: # comparison_operator:Eq, if (-> +1), if_test_atom:u, if_test_atom:v, if_without_else (-> +1)
                raise Exception() # external_free_call:Exception, free_call:Exception, free_call_without_arguments:Exception, if_then_branch, raise:Exception
        print(v) # call_argument:v, external_free_call:print, free_call:print, free_call_without_result:print
    except Exception: # except:Exception
        continue # continue

# ----------------------------------------------------------------------------------------
# 042.3168-continue-outer-loop.py
# ----------------------------------------------------------------------------------------
for v in a: # for:v (-> +4), for_each (-> +4), loop:for (-> +4), loop_with_late_exit:for (-> +4), whole_span:5 (-> +4)
    for v_ in b: # for:v_ (-> +3), for_each (-> +3), loop:for (-> +3), loop_with_late_exit:for (-> +3), nested_for:1 (-> +3)
        if v == v_: # comparison_operator:Eq, if (-> +1), if_test_atom:v, if_test_atom:v_, if_without_else (-> +1)
            continue # continue, if_then_branch
        print(v) # call_argument:v, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 043.0676-break-outer-loop.py
# ----------------------------------------------------------------------------------------
class BreakOuterLoop(Exception): # class:BreakOuterLoop (-> +1), whole_span:11 (-> +10)
    pass # null_operation
try: # try (-> +8), try_except:BreakOuterLoop (-> +8), try_raise:BreakOuterLoop (-> +8)
    position = None # assignment:None, assignment_lhs_identifier:position, assignment_rhs_atom:None, literal:None, single_assignment:position
    for row in m: # for:row (-> +4), for_each (-> +4), loop:for (-> +4), loop_with_early_exit:for:raise (-> +4), loop_with_raise:for (-> +4)
        for column in m[row]: # for:column (-> +3), index:row, loop:for (-> +3), loop_with_early_exit:for:raise (-> +3), loop_with_raise:for (-> +3), nested_for:1 (-> +3)
            if m[row][column] == v: # comparison_operator:Eq, if (-> +2), if_test_atom:column, if_test_atom:m, if_test_atom:row, if_test_atom:v, if_without_else (-> +2), index:column, index:row, nested_index:2
                position = (row, column) # assignment, assignment_lhs_identifier:position, assignment_rhs_atom:column, assignment_rhs_atom:row, if_then_branch (-> +1), literal:Tuple, single_assignment:position
                raise BreakOuterLoop # raise:BreakOuterLoop
except BreakOuterLoop: # except:BreakOuterLoop
    pass # null_operation

# ----------------------------------------------------------------------------------------
# 043.2733-break-outer-loop.py
# ----------------------------------------------------------------------------------------
def loop_breaking(m, v): # function:loop_breaking (-> +5), function_argument:m, function_argument:v, function_argument_flavor:arg, function_returning_something:loop_breaking (-> +5), whole_span:7 (-> +6)
    for i, row in enumerate(m): # call_argument:m, external_free_call:enumerate, for:i (-> +3), for:row (-> +3), for_indexes_elements (-> +3), free_call:enumerate, literal:Tuple, loop:for (-> +3), loop_with_early_exit:for:return (-> +3), loop_with_return:for (-> +3)
        for j, value in enumerate(row): # call_argument:row, external_free_call:enumerate, for:j (-> +2), for:value (-> +2), for_indexes_elements (-> +2), free_call:enumerate, literal:Tuple, loop:for (-> +2), loop_with_early_exit:for:return (-> +2), loop_with_return:for (-> +2), nested_for:1 (-> +2)
            if value == v: # comparison_operator:Eq, if (-> +1), if_test_atom:v, if_test_atom:value, if_without_else (-> +1)
                return (i, j) # if_then_branch, literal:Tuple, return
    return None # literal:None, return:None
print(loop_breaking(([1, 2, 3], [4, 5, 6], [7, 8, 9]), 6)) # call_argument:, call_argument:6, composition, external_free_call:print, free_call:loop_breaking, free_call:print, free_call_without_result:print, internal_free_call:loop_breaking, literal:1, literal:2, literal:3, literal:4, literal:5, literal:6, literal:7, literal:8, literal:9, literal:List, literal:Tuple

# ----------------------------------------------------------------------------------------
# 044.0190-insert-element-in-list.py
# ----------------------------------------------------------------------------------------
s.insert(i, x) # call_argument:i, call_argument:x, member_call:insert, member_call_object:s, member_call_without_result:insert, update:s:i, update:s:x, update_by_member_call:s:i, update_by_member_call:s:x, update_by_member_call_with:insert, update_with:insert, whole_span:1

# ----------------------------------------------------------------------------------------
# 045.0570-pause-execution-for-5-seconds.py
# ----------------------------------------------------------------------------------------
import time # import:time, import_module:time, whole_span:2 (-> +1)
time.sleep(5) # call_argument:5, literal:5, member_call:sleep, member_call_object:time, member_call_without_result:sleep

# ----------------------------------------------------------------------------------------
# 046.0191-extract-beginning-of-string-prefix.py
# ----------------------------------------------------------------------------------------
t = s[:5] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:5, assignment_rhs_atom:s, literal:5, single_assignment:t, slice::5:, slice_lower:, slice_step:, slice_upper:5, whole_span:1

# ----------------------------------------------------------------------------------------
# 047.0198-extract-string-suffix.py
# ----------------------------------------------------------------------------------------
t = s[-5:] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:-5, assignment_rhs_atom:s, literal:-5, single_assignment:t, slice:-5::, slice_lower:-5, slice_step:, slice_upper:, whole_span:1

# ----------------------------------------------------------------------------------------
# 048.0210-multi-line-string-literal.py
# ----------------------------------------------------------------------------------------
s = """Huey # assignment, assignment_lhs_identifier:s, single_assignment:s, whole_span:3 (-> +2)
Dewey
Louie""" # literal:Str

# ----------------------------------------------------------------------------------------
# 049.0242-split-a-space-separated-string.py
# ----------------------------------------------------------------------------------------
chunks = s.split() # assignment:split, assignment_lhs_identifier:chunks, assignment_rhs_atom:s, member_call:split, single_assignment:chunks, whole_span:1

# ----------------------------------------------------------------------------------------
# 050.0572-make-an-infinite-loop.py
# ----------------------------------------------------------------------------------------
while True: # infinite_while (-> +1), literal:True, loop:while (-> +1), loop_with_late_exit:while (-> +1), while (-> +1), whole_span:2 (-> +1)
    pass # null_operation

# ----------------------------------------------------------------------------------------
# 051.0230-check-if-map-contains-key.py
# ----------------------------------------------------------------------------------------
k in m # comparison_operator:In, whole_span:1

# ----------------------------------------------------------------------------------------
# 052.0666-check-if-map-contains-value.py
# ----------------------------------------------------------------------------------------
v in map.values() # comparison_operator:In, member_call:values, whole_span:1

# ----------------------------------------------------------------------------------------
# 053.0240-join-a-list-of-strings.py
# ----------------------------------------------------------------------------------------
y = ", ".join(x) # assignment:join, assignment_lhs_identifier:y, assignment_rhs_atom:x, call_argument:x, literal:Str, member_call:join, single_assignment:y, whole_span:1

# ----------------------------------------------------------------------------------------
# 053.1933-join-a-list-of-strings.py
# ----------------------------------------------------------------------------------------
y = ", ".join(map(str, x)) # assignment:join, assignment_lhs_identifier:y, assignment_rhs_atom:str, assignment_rhs_atom:x, call_argument:, call_argument:str, call_argument:x, composition, external_free_call:map, free_call:map, literal:Str, member_call:join, single_assignment:y, whole_span:1

# ----------------------------------------------------------------------------------------
# 054.0241-compute-sum-of-integers.py
# ----------------------------------------------------------------------------------------
s = sum(x) # assignment:sum, assignment_lhs_identifier:s, assignment_rhs_atom:x, call_argument:x, external_free_call:sum, free_call:sum, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 055.0575-convert-integer-to-string.py
# ----------------------------------------------------------------------------------------
s = str(i) # assignment:str, assignment_lhs_identifier:s, assignment_rhs_atom:i, call_argument:i, external_free_call:str, free_call:str, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 056.1424-launch-1000-parallel-tasks-and-wait-for-completion.py
# ----------------------------------------------------------------------------------------
from multiprocessing import Pool # import:multiprocessing:Pool, import_module:multiprocessing, import_name:Pool, whole_span:6 (-> +5)
def f(i): # function:f (-> +1), function_argument:i, function_argument_flavor:arg, function_returning_nothing:f (-> +1)
    i * i # binary_operator:Mult, multiplication_operator
with Pool(processes) as p: # call_argument:processes, external_free_call:Pool, free_call:Pool
    p.map(func=f, iterable=range(1, 1001)) # call_argument:1, call_argument:1001, external_free_call:range, free_call:range, literal:1, literal:1001, member_call:map, member_call_object:p, member_call_without_result:map, range:1:1001, suggest_constant_definition
print("Finished") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str

# ----------------------------------------------------------------------------------------
# 057.0260-filter-list.py
# ----------------------------------------------------------------------------------------
y = filter(p, x) # assignment:filter, assignment_lhs_identifier:y, assignment_rhs_atom:p, assignment_rhs_atom:x, call_argument:p, call_argument:x, external_free_call:filter, free_call:filter, single_assignment:y, whole_span:1

# ----------------------------------------------------------------------------------------
# 057.3173-filter-list.py
# ----------------------------------------------------------------------------------------
y = [element for element in x if p(element)] # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:element, assignment_rhs_atom:x, call_argument:element, comprehension:List, comprehension_for_count:1, external_free_call:p, filtered_comprehension, free_call:p, single_assignment:y, whole_span:1

# ----------------------------------------------------------------------------------------
# 058.0665-extract-file-content-to-a-string.py
# ----------------------------------------------------------------------------------------
lines = open(f).read() # assignment:read, assignment_lhs_identifier:lines, assignment_rhs_atom:f, call_argument:f, external_free_call:open, free_call:open, member_call:read, single_assignment:lines, whole_span:1

# ----------------------------------------------------------------------------------------
# 059.0668-write-to-standard-error-stream.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, whole_span:2 (-> +1)
print(x, "is negative", file=sys.stderr) # call_argument:, call_argument:x, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str

# ----------------------------------------------------------------------------------------
# 060.1084-read-command-line-argument.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, whole_span:2 (-> +1)
x = sys.argv[1] # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:1, assignment_rhs_atom:sys, index:1, literal:1, single_assignment:x

# ----------------------------------------------------------------------------------------
# 061.0576-get-current-date.py
# ----------------------------------------------------------------------------------------
import datetime # import:datetime, import_module:datetime, whole_span:2 (-> +1)
d = datetime.datetime.now() # assignment:now, assignment_lhs_identifier:d, assignment_rhs_atom:datetime, member_call:now, single_assignment:d

# ----------------------------------------------------------------------------------------
# 062.1091-find-substring-position.py
# ----------------------------------------------------------------------------------------
i = x.find(y) # assignment:find, assignment_lhs_identifier:i, assignment_rhs_atom:x, assignment_rhs_atom:y, call_argument:y, member_call:find, single_assignment:i, whole_span:1

# ----------------------------------------------------------------------------------------
# 063.1088-replace-fragment-of-a-string.py
# ----------------------------------------------------------------------------------------
x2 = x.replace(y, z) # assignment:replace, assignment_lhs_identifier:x2, assignment_rhs_atom:x, assignment_rhs_atom:y, assignment_rhs_atom:z, call_argument:y, call_argument:z, member_call:replace, single_assignment:x2, whole_span:1

# ----------------------------------------------------------------------------------------
# 064.0274-big-integer--value-3-power-247.py
# ----------------------------------------------------------------------------------------
x = 3 ** 247 # assignment:Pow, assignment_lhs_identifier:x, assignment_rhs_atom:247, assignment_rhs_atom:3, binary_operator:Pow, literal:247, literal:3, single_assignment:x, whole_span:1

# ----------------------------------------------------------------------------------------
# 065.1085-format-decimal-number.py
# ----------------------------------------------------------------------------------------
s = "{:.1%}".format(x) # assignment:format, assignment_lhs_identifier:s, assignment_rhs_atom:x, call_argument:x, literal:Str, member_call:format, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 066.0672-big-integer-exponentiation.py
# ----------------------------------------------------------------------------------------
z = x ** n # assignment:Pow, assignment_lhs_identifier:z, assignment_rhs_atom:n, assignment_rhs_atom:x, binary_operator:Pow, single_assignment:z, whole_span:1

# ----------------------------------------------------------------------------------------
# 067.1426-binomial-coefficient-n-choose-k.py
# ----------------------------------------------------------------------------------------
import math # import:math, import_module:math, whole_span:3 (-> +2)
def binom(n, k): # function:binom (-> +1), function_argument:k, function_argument:n, function_argument_flavor:arg, function_returning_something:binom (-> +1)
    return math.factorial(n) // math.factorial(k) // math.factorial(n - k) # binary_operator:FloorDiv, binary_operator:Sub, call_argument:, call_argument:k, call_argument:n, member_call:factorial, return

# ----------------------------------------------------------------------------------------
# 068.2271-create-a-bitset.py
# ----------------------------------------------------------------------------------------
from __future__ import division # import:__future__:division, import_module:__future__, import_name:division, whole_span:3 (-> +2)
import math # import:math, import_module:math
x = bytearray(int(math.ceil(n / 8.0))) # assignment:bytearray, assignment_lhs_identifier:x, assignment_rhs_atom:8.0, assignment_rhs_atom:math, assignment_rhs_atom:n, binary_operator:Div, call_argument:, composition, external_free_call:bytearray, external_free_call:int, free_call:bytearray, free_call:int, literal:8.0, member_call:ceil, single_assignment:x

# ----------------------------------------------------------------------------------------
# 069.1086-seed-random-generator.py
# ----------------------------------------------------------------------------------------
import random # import:random, import_module:random, whole_span:2 (-> +1)
rand = random.Random(s) # assignment:Random, assignment_lhs_identifier:rand, assignment_rhs_atom:random, assignment_rhs_atom:s, call_argument:s, member_call:Random, single_assignment:rand

# ----------------------------------------------------------------------------------------
# 070.1087-use-clock-as-random-generator-seed.py
# ----------------------------------------------------------------------------------------
import random # import:random, import_module:random, whole_span:2 (-> +1)
rand = random.Random() # assignment:Random, assignment_lhs_identifier:rand, assignment_rhs_atom:random, member_call:Random, single_assignment:rand

# ----------------------------------------------------------------------------------------
# 071.0379-echo-program-implementation.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, whole_span:2 (-> +1)
print(" ".join(sys.argv[1:])) # call_argument:, composition, external_free_call:print, free_call:print, free_call_without_result:print, literal:1, literal:Str, member_call:join, slice:1::, slice_lower:1, slice_step:, slice_upper:

# ----------------------------------------------------------------------------------------
# 073.0673-create-a-factory.py
# ----------------------------------------------------------------------------------------
def fact(a_class, str_): # function:fact (-> +2), function_argument:a_class, function_argument:str_, function_argument_flavor:arg, function_returning_something:fact (-> +2), higher_order_function:a_class (-> +2), whole_span:3 (-> +2)
    if issubclass(a_class, Parent): # call_argument:Parent, call_argument:a_class, external_free_call:issubclass, free_call:issubclass, if (-> +1), if_test_atom:Parent, if_test_atom:a_class, if_without_else (-> +1)
        return a_class(str_) # call_argument:str_, external_free_call:a_class, free_call:a_class, free_tail_call:a_class, if_then_branch, return

# ----------------------------------------------------------------------------------------
# 074.0674-compute-gcd.py
# ----------------------------------------------------------------------------------------
from fractions import gcd # import:fractions:gcd, import_module:fractions, import_name:gcd, whole_span:2 (-> +1)
x = gcd(a, b) # assignment:gcd, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:b, call_argument:a, call_argument:b, external_free_call:gcd, free_call:gcd, single_assignment:x

# ----------------------------------------------------------------------------------------
# 075.0675-compute-lcm.py
# ----------------------------------------------------------------------------------------
from fractions import gcd # import:fractions:gcd, import_module:fractions, import_name:gcd, whole_span:2 (-> +1)
x = (a * b) // gcd(a, b) # assignment:FloorDiv, assignment_lhs_identifier:x, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:FloorDiv, binary_operator:Mult, call_argument:a, call_argument:b, external_free_call:gcd, free_call:gcd, multiplication_operator, single_assignment:x

# ----------------------------------------------------------------------------------------
# 076.1083-binary-digits-from-an-integer.py
# ----------------------------------------------------------------------------------------
s = "{:b}".format(x) # assignment:format, assignment_lhs_identifier:s, assignment_rhs_atom:x, call_argument:x, literal:Str, member_call:format, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 077.1093-complex-number.py
# ----------------------------------------------------------------------------------------
x = 3j - 2 # assignment:Sub, assignment_lhs_identifier:x, assignment_rhs_atom:2, assignment_rhs_atom:3j, binary_operator:Sub, literal:2, literal:3j, single_assignment:x, whole_span:2 (-> +1)
y = x * 1j # assignment:Mult, assignment_lhs_identifier:y, assignment_rhs_atom:1j, assignment_rhs_atom:x, binary_operator:Mult, literal:1j, multiplication_operator, single_assignment:y

# ----------------------------------------------------------------------------------------
# 078.1089-do-while-loop.py
# ----------------------------------------------------------------------------------------
while True: # infinite_while (-> +3), literal:True, loop:while (-> +3), loop_with_break:while (-> +3), loop_with_early_exit:while:break (-> +3), while (-> +3), whole_span:4 (-> +3)
    do_something() # external_free_call:do_something, free_call:do_something, free_call_without_arguments:do_something, free_call_without_result:do_something
    if not c: # if (-> +1), if_test_atom:c, if_without_else (-> +1), unary_operator:Not
        break # break, if_then_branch

# ----------------------------------------------------------------------------------------
# 079.1090-convert-integer-to-floating-point-number.py
# ----------------------------------------------------------------------------------------
y = float(x) # assignment:float, assignment_lhs_identifier:y, assignment_rhs_atom:x, call_argument:x, external_free_call:float, free_call:float, single_assignment:y, whole_span:1

# ----------------------------------------------------------------------------------------
# 080.1092-truncate-floating-point-number-to-integer.py
# ----------------------------------------------------------------------------------------
y = int(x) # assignment:int, assignment_lhs_identifier:y, assignment_rhs_atom:x, call_argument:x, external_free_call:int, free_call:int, single_assignment:y, whole_span:1

# ----------------------------------------------------------------------------------------
# 081.2270-round-floating-point-number-to-integer.py
# ----------------------------------------------------------------------------------------
y = int(x + 0.5) # addition_operator, assignment:int, assignment_lhs_identifier:y, assignment_rhs_atom:0.5, assignment_rhs_atom:x, binary_operator:Add, call_argument:, external_free_call:int, free_call:int, literal:0.5, single_assignment:y, whole_span:1

# ----------------------------------------------------------------------------------------
# 082.1096-count-substring-occurrences.py
# ----------------------------------------------------------------------------------------
count = s.count(t) # assignment:count, assignment_lhs_identifier:count, assignment_rhs_atom:s, assignment_rhs_atom:t, call_argument:t, member_call:count, single_assignment:count, whole_span:1

# ----------------------------------------------------------------------------------------
# 083.1805-regex-with-character-repetition.py
# ----------------------------------------------------------------------------------------
import re # import:re, import_module:re, whole_span:2 (-> +1)
r = re.compile(r"htt+p") # assignment:compile, assignment_lhs_identifier:r, assignment_rhs_atom:re, call_argument:, literal:Str, member_call:compile, single_assignment:r

# ----------------------------------------------------------------------------------------
# 084.1940-count-bits-set-in-integer-binary-representation.py
# ----------------------------------------------------------------------------------------
c = bin(i).count("1") # assignment:count, assignment_lhs_identifier:c, assignment_rhs_atom:i, call_argument:, call_argument:i, external_free_call:bin, free_call:bin, literal:Str, member_call:count, single_assignment:c, whole_span:1

# ----------------------------------------------------------------------------------------
# 085.1003-check-if-integer-addition-will-overflow.py
# ----------------------------------------------------------------------------------------
def adding_will_overflow(x, y): # function:adding_will_overflow (-> +1), function_argument:x, function_argument:y, function_argument_flavor:arg, function_returning_something:adding_will_overflow (-> +1), whole_span:2 (-> +1)
    return False # literal:False, return:False

# ----------------------------------------------------------------------------------------
# 086.1004-check-if-integer-multiplication-will-overflow.py
# ----------------------------------------------------------------------------------------
def multiplyWillOverflow(x, y): # function:multiplyWillOverflow (-> +1), function_argument:x, function_argument:y, function_argument_flavor:arg, function_returning_something:multiplyWillOverflow (-> +1), whole_span:2 (-> +1)
    return False # literal:False, return:False

# ----------------------------------------------------------------------------------------
# 087.1139-stop-program.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, whole_span:2 (-> +1)
sys.exit(1) # call_argument:1, literal:1, member_call:exit, member_call_object:sys, member_call_without_result:exit

# ----------------------------------------------------------------------------------------
# 088.2143-allocate-1m-bytes.py
# ----------------------------------------------------------------------------------------
buf = bytearray(1000000) # assignment:bytearray, assignment_lhs_identifier:buf, assignment_rhs_atom:1000000, call_argument:1000000, external_free_call:bytearray, free_call:bytearray, literal:1000000, single_assignment:buf, whole_span:1

# ----------------------------------------------------------------------------------------
# 089.1097-handle-invalid-argument.py
# ----------------------------------------------------------------------------------------
raise ValueError("x is invalid") # call_argument:, external_free_call:ValueError, free_call:ValueError, literal:Str, raise:ValueError, whole_span:1

# ----------------------------------------------------------------------------------------
# 090.1099-read-only-outside.py
# ----------------------------------------------------------------------------------------
class Foo(object): # class:Foo (-> +5), whole_span:6 (-> +5)
    def __init__(self): # function:__init__ (-> +1), function_argument:self, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +1), instance_method:__init__ (-> +1), method:__init__ (-> +1)
        self._x = 0 # assignment:0, assignment_lhs_identifier:self, assignment_rhs_atom:0, literal:0
    @property # decorated_function:x (-> +2), function:x (-> +2), function_decorator:property (-> +2), function_returning_something:x (-> +2), instance_method:x (-> +2), method:x (-> +2)
    def x(self): # function_argument:self, function_argument_flavor:arg
        return self._x # return

# ----------------------------------------------------------------------------------------
# 091.1098-load-json-file-into-struct.py
# ----------------------------------------------------------------------------------------
import json # import:json, import_module:json, whole_span:3 (-> +2)
with open("data.json", "r") as input: # call_argument:, external_free_call:open, free_call:open, literal:Str
    x = json.load(input) # assignment:load, assignment_lhs_identifier:x, assignment_rhs_atom:input, assignment_rhs_atom:json, call_argument:input, member_call:load, single_assignment:x

# ----------------------------------------------------------------------------------------
# 092.1100-save-object-into-json-file.py
# ----------------------------------------------------------------------------------------
import json # import:json, import_module:json, whole_span:3 (-> +2)
with open("data.json", "w") as output: # call_argument:, external_free_call:open, free_call:open, literal:Str
    json.dump(x, output) # call_argument:output, call_argument:x, member_call:dump, member_call_object:json, member_call_without_result:dump

# ----------------------------------------------------------------------------------------
# 093.1082-pass-a-runnable-procedure-as-parameter.py
# ----------------------------------------------------------------------------------------
from __future__ import print_function # import:__future__:print_function, import_module:__future__, import_name:print_function, whole_span:3 (-> +2)
def control(f): # function:control (-> +1), function_argument:f, function_argument_flavor:arg, function_returning_something:control (-> +1), higher_order_function:f (-> +1)
    return f() # external_free_call:f, free_call:f, free_call_without_arguments:f, free_tail_call:f, return

# ----------------------------------------------------------------------------------------
# 094.1101-print-type-of-variable.py
# ----------------------------------------------------------------------------------------
print(type(x)) # call_argument:, call_argument:x, composition, external_free_call:print, external_free_call:type, free_call:print, free_call:type, free_call_without_result:print, whole_span:1

# ----------------------------------------------------------------------------------------
# 094.1864-print-type-of-variable.py
# ----------------------------------------------------------------------------------------
print(x.__class__) # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, whole_span:1

# ----------------------------------------------------------------------------------------
# 095.2140-get-file-size.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os, whole_span:2 (-> +1)
x = os.path.getsize(path) # assignment:getsize, assignment_lhs_identifier:x, assignment_rhs_atom:os, assignment_rhs_atom:path, call_argument:path, member_call:getsize, single_assignment:x

# ----------------------------------------------------------------------------------------
# 096.1094-check-string-prefix.py
# ----------------------------------------------------------------------------------------
b = s.startswith(prefix) # assignment:startswith, assignment_lhs_identifier:b, assignment_rhs_atom:prefix, assignment_rhs_atom:s, call_argument:prefix, member_call:startswith, single_assignment:b, whole_span:1

# ----------------------------------------------------------------------------------------
# 097.1095-check-string-suffix.py
# ----------------------------------------------------------------------------------------
b = s.endswith(suffix) # assignment:endswith, assignment_lhs_identifier:b, assignment_rhs_atom:s, assignment_rhs_atom:suffix, call_argument:suffix, member_call:endswith, single_assignment:b, whole_span:1

# ----------------------------------------------------------------------------------------
# 098.2142-epoch-seconds-to-date-object.py
# ----------------------------------------------------------------------------------------
import datetime # import:datetime, import_module:datetime, whole_span:2 (-> +1)
d = datetime.date.fromtimestamp(ts) # assignment:fromtimestamp, assignment_lhs_identifier:d, assignment_rhs_atom:datetime, assignment_rhs_atom:ts, call_argument:ts, member_call:fromtimestamp, single_assignment:d

# ----------------------------------------------------------------------------------------
# 099.1429-format-date-yyyy-mm-dd.py
# ----------------------------------------------------------------------------------------
from datetime import date # import:datetime:date, import_module:datetime, import_name:date, whole_span:3 (-> +2)
d = date(2016, 9, 28) # assignment:date, assignment_lhs_identifier:d, assignment_rhs_atom:2016, assignment_rhs_atom:28, assignment_rhs_atom:9, call_argument:2016, call_argument:28, call_argument:9, external_free_call:date, free_call:date, literal:2016, literal:28, literal:9, single_assignment:d
x = d.strftime("%Y-%m-%d") # assignment:strftime, assignment_lhs_identifier:x, assignment_rhs_atom:d, call_argument:, literal:Str, member_call:strftime, single_assignment:x

# ----------------------------------------------------------------------------------------
# 099.2693-format-date-yyyy-mm-dd.py
# ----------------------------------------------------------------------------------------
from datetime import date # import:datetime:date, import_module:datetime, import_name:date, whole_span:3 (-> +2)
d = date.today() # assignment:today, assignment_lhs_identifier:d, assignment_rhs_atom:date, member_call:today, single_assignment:d
x = d.isoformat() # assignment:isoformat, assignment_lhs_identifier:x, assignment_rhs_atom:d, member_call:isoformat, single_assignment:x

# ----------------------------------------------------------------------------------------
# 100.1142-sort-by-a-comparator.py
# ----------------------------------------------------------------------------------------
items.sort(c) # call_argument:c, member_call:sort, member_call_object:items, member_call_without_result:sort, whole_span:1

# ----------------------------------------------------------------------------------------
# 101.2172-load-from-http-get-request-into-a-string.py
# ----------------------------------------------------------------------------------------
import urllib.request # import:urllib.request, import_module:urllib.request, whole_span:3 (-> +2)
with urllib.request.urlopen(u) as f: # call_argument:u, member_call:urlopen
    s = f.read() # assignment:read, assignment_lhs_identifier:s, assignment_rhs_atom:f, member_call:read, single_assignment:s

# ----------------------------------------------------------------------------------------
# 102.2173-load-from-http-get-request-into-a-file.py
# ----------------------------------------------------------------------------------------
import urllib # import:urllib, import_module:urllib, whole_span:2 (-> +1)
filename, headers = urllib.request.urlretrieve(u, "result.txt") # assignment:urlretrieve, assignment_lhs_identifier:filename, assignment_lhs_identifier:headers, assignment_rhs_atom:u, assignment_rhs_atom:urllib, call_argument:, call_argument:u, literal:Str, literal:Tuple, member_call:urlretrieve, parallel_assignment:2

# ----------------------------------------------------------------------------------------
# 103.2276-load-xml-file-into-struct.py
# ----------------------------------------------------------------------------------------
import lxml.etree # import:lxml.etree, import_module:lxml.etree, whole_span:2 (-> +1)
x = lxml.etree.parse("data.xml") # assignment:parse, assignment_lhs_identifier:x, assignment_rhs_atom:lxml, call_argument:, literal:Str, member_call:parse, single_assignment:x

# ----------------------------------------------------------------------------------------
# 104.3264-save-object-into-xml-file.py
# ----------------------------------------------------------------------------------------
import pyxser as pyx # import:pyxser, import_module:pyxser, whole_span:12 (-> +11)
class TestClass(object): # class:TestClass (-> +7)
    a = None # assignment:None, assignment_lhs_identifier:a, assignment_rhs_atom:None, literal:None, single_assignment:a
    b = None # assignment:None, assignment_lhs_identifier:b, assignment_rhs_atom:None, literal:None, single_assignment:b
    c = None # assignment:None, assignment_lhs_identifier:c, assignment_rhs_atom:None, literal:None, single_assignment:c
    def __init__(self, a, b, c): # function:__init__ (-> +3), function_argument:a, function_argument:b, function_argument:c, function_argument:self, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), method:__init__ (-> +3)
        self.a = a # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:a
        self.b = b # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:b
        self.c = c # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:c
tst = TestClass("var_a", "var_b", "var_c") # assignment:TestClass, assignment_lhs_identifier:tst, call_argument:, external_free_call:TestClass, free_call:TestClass, literal:Str, single_assignment:tst
ser = pyx.serialize(obj=tst, enc="utf-8") # assignment:serialize, assignment_lhs_identifier:ser, assignment_rhs_atom:pyx, assignment_rhs_atom:tst, literal:Str, member_call:serialize, single_assignment:ser
print(ser) # call_argument:ser, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 105.1804-current-executable-name.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, whole_span:2 (-> +1)
s = sys.argv[0] # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:0, assignment_rhs_atom:sys, index:0, literal:0, single_assignment:s

# ----------------------------------------------------------------------------------------
# 106.2039-get-program-working-directory.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os, whole_span:2 (-> +1)
dir = os.getcwd() # assignment:getcwd, assignment_lhs_identifier:dir, assignment_rhs_atom:os, member_call:getcwd, single_assignment:dir

# ----------------------------------------------------------------------------------------
# 107.2139-get-folder-containing-current-program.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os, whole_span:2 (-> +1)
dir = os.path.dirname(os.path.abspath(__file__)) # assignment:dirname, assignment_lhs_identifier:dir, assignment_rhs_atom:__file__, assignment_rhs_atom:os, call_argument:, call_argument:__file__, composition, member_call:abspath, member_call:dirname, single_assignment:dir

# ----------------------------------------------------------------------------------------
# 108.1291-determine-if-variable-name-is-defined.py
# ----------------------------------------------------------------------------------------
if "x" in locals(): # comparison_operator:In, external_free_call:locals, free_call:locals, free_call_without_arguments:locals, if (-> +1), if_without_else (-> +1), literal:Str, whole_span:2 (-> +1), yoda_comparison:In
    print(x) # call_argument:x, external_free_call:print, free_call:print, free_call_without_result:print, if_then_branch

# ----------------------------------------------------------------------------------------
# 109.2280-number-of-bytes-of-a-type.py
# ----------------------------------------------------------------------------------------
import pympler.asizeof # import:pympler.asizeof, import_module:pympler.asizeof, whole_span:2 (-> +1)
n = pympler.asizeof.asizeof(t) # assignment:asizeof, assignment_lhs_identifier:n, assignment_rhs_atom:pympler, assignment_rhs_atom:t, call_argument:t, member_call:asizeof, single_assignment:n

# ----------------------------------------------------------------------------------------
# 110.1455-check-if-string-is-blank.py
# ----------------------------------------------------------------------------------------
blank = s.strip() == "" # assignment, assignment_lhs_identifier:blank, assignment_rhs_atom:s, comparison_operator:Eq, empty_literal:Str, literal:Str, member_call:strip, single_assignment:blank, whole_span:1

# ----------------------------------------------------------------------------------------
# 111.2168-launch-other-program.py
# ----------------------------------------------------------------------------------------
import subprocess # import:subprocess, import_module:subprocess, whole_span:2 (-> +1)
subprocess.call(["x", "a", "b"]) # call_argument:, literal:List, literal:Str, member_call:call, member_call_object:subprocess, member_call_without_result:call

# ----------------------------------------------------------------------------------------
# 112.2144-iterate-over-map-entries-ordered-by-keys.py
# ----------------------------------------------------------------------------------------
for k in sorted(mymap): # call_argument:mymap, external_free_call:sorted, for:k (-> +1), free_call:sorted, loop:for (-> +1), loop_with_late_exit:for (-> +1), whole_span:2 (-> +1)
    print(mymap[k]) # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, index:k

# ----------------------------------------------------------------------------------------
# 113.2157-iterate-over-map-entries-ordered-by-values.py
# ----------------------------------------------------------------------------------------
for x, k in sorted((x, k) for k, x in mymap.items()): # call_argument:, composition, comprehension:Generator, comprehension_for_count:1, external_free_call:sorted, for:k (-> +1), for:x (-> +1), free_call:sorted, literal:Tuple, loop:for (-> +1), loop_with_late_exit:for (-> +1), member_call:items, whole_span:2 (-> +1)
    print(k, x) # call_argument:k, call_argument:x, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 114.2273-test-deep-equality.py
# ----------------------------------------------------------------------------------------
b = x == y # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:x, assignment_rhs_atom:y, comparison_operator:Eq, single_assignment:b, whole_span:1

# ----------------------------------------------------------------------------------------
# 115.2138-compare-dates.py
# ----------------------------------------------------------------------------------------
import datetime # import:datetime, import_module:datetime, whole_span:2 (-> +1)
b = d1 < d2 # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:d1, assignment_rhs_atom:d2, comparison_operator:Lt, single_assignment:b

# ----------------------------------------------------------------------------------------
# 116.1257-remove-occurrences-of-word-from-string.py
# ----------------------------------------------------------------------------------------
s2 = s1.replace(w, "") # assignment:replace, assignment_lhs_identifier:s2, assignment_rhs_atom:s1, assignment_rhs_atom:w, call_argument:, call_argument:w, empty_literal:Str, literal:Str, member_call:replace, single_assignment:s2, whole_span:1

# ----------------------------------------------------------------------------------------
# 117.1297-get-list-size.py
# ----------------------------------------------------------------------------------------
n = len(x) # assignment:len, assignment_lhs_identifier:n, assignment_rhs_atom:x, call_argument:x, external_free_call:len, free_call:len, single_assignment:n, whole_span:1

# ----------------------------------------------------------------------------------------
# 118.1254-list-to-set.py
# ----------------------------------------------------------------------------------------
y = set(x) # assignment:set, assignment_lhs_identifier:y, assignment_rhs_atom:x, call_argument:x, external_free_call:set, free_call:set, single_assignment:y, whole_span:1

# ----------------------------------------------------------------------------------------
# 118.3266-list-to-set.py
# ----------------------------------------------------------------------------------------
set(x) # call_argument:x, external_free_call:set, free_call:set, free_call_without_result:set, whole_span:1

# ----------------------------------------------------------------------------------------
# 119.1253-deduplicate-list.py
# ----------------------------------------------------------------------------------------
x = list(set(x)) # assignment:list, assignment_lhs_identifier:x, assignment_rhs_atom:x, call_argument:, call_argument:x, composition, external_free_call:list, external_free_call:set, free_call:list, free_call:set, single_assignment:x, whole_span:1

# ----------------------------------------------------------------------------------------
# 119.3263-deduplicate-list.py
# ----------------------------------------------------------------------------------------
elements = ["b", "a", "b", "c"] # assignment, assignment_lhs_identifier:elements, literal:List, literal:Str, single_assignment:elements, whole_span:8 (-> +7)
unique_set = set() # assignment:set, assignment_lhs_identifier:unique_set, external_free_call:set, free_call:set, free_call_without_arguments:set, single_assignment:unique_set
elements_unique = [] # assignment, assignment_lhs_identifier:elements_unique, empty_literal:List, literal:List, single_assignment:elements_unique
for i in elements: # accumulate_elements:add (-> +3), accumulate_elements:append (-> +3), accumulate_some_elements:add (-> +3), accumulate_some_elements:append (-> +3), for:i (-> +3), for_each (-> +3), loop:for (-> +3), loop_with_late_exit:for (-> +3)
    if i not in unique_set: # comparison_operator:NotIn, if (-> +2), if_test_atom:i, if_test_atom:unique_set, if_without_else (-> +2)
        unique_set.add(i) # call_argument:i, if_then_branch (-> +1), member_call:add, member_call_object:unique_set, member_call_without_result:add, update:unique_set:i, update_by_member_call:unique_set:i, update_by_member_call_with:add, update_with:add
        elements_unique.append(i) # call_argument:i, member_call:append, member_call_object:elements_unique, member_call_without_result:append, update:elements_unique:i, update_by_member_call:elements_unique:i, update_by_member_call_with:append, update_with:append
print(elements_unique) # call_argument:elements_unique, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 120.1479-read-integer-from-stdin.py
# ----------------------------------------------------------------------------------------
input_var = int(raw_input("Input Prompting String: ")) # assignment:int, assignment_lhs_identifier:input_var, call_argument:, composition, external_free_call:int, external_free_call:raw_input, free_call:int, free_call:raw_input, literal:Str, single_assignment:input_var, whole_span:1

# ----------------------------------------------------------------------------------------
# 121.3029-udp-listen-and-read.py
# ----------------------------------------------------------------------------------------
import socket # import:socket, import_module:socket, whole_span:7 (-> +6)
UDP_IP = "127.0.0.1" # assignment, assignment_lhs_identifier:UDP_IP, literal:Str, single_assignment:UDP_IP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # assignment:socket, assignment_lhs_identifier:sock, assignment_rhs_atom:socket, call_argument:, member_call:socket, single_assignment:sock
sock.bind((UDP_IP, p)) # call_argument:, literal:Tuple, member_call:bind, member_call_object:sock, member_call_without_result:bind
while True: # infinite_while (-> +2), literal:True, loop:while (-> +2), loop_with_late_exit:while (-> +2), while (-> +2)
    data, addr = sock.recvfrom(1024) # assignment:recvfrom, assignment_lhs_identifier:addr, assignment_lhs_identifier:data, assignment_rhs_atom:1024, assignment_rhs_atom:sock, call_argument:1024, literal:1024, literal:Tuple, member_call:recvfrom, parallel_assignment:2, suggest_constant_definition
    print("received message:", data) # call_argument:, call_argument:data, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str

# ----------------------------------------------------------------------------------------
# 122.1453-declare-enumeration.py
# ----------------------------------------------------------------------------------------
class Suit: # class:Suit (-> +1), whole_span:2 (-> +1)
    SPADES, HEARTS, DIAMONDS, CLUBS = range(4) # assignment:range, assignment_lhs_identifier:CLUBS, assignment_lhs_identifier:DIAMONDS, assignment_lhs_identifier:HEARTS, assignment_lhs_identifier:SPADES, assignment_rhs_atom:4, call_argument:4, external_free_call:range, free_call:range, literal:4, literal:Tuple, parallel_assignment:4, range:4, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# 122.1454-declare-enumeration.py
# ----------------------------------------------------------------------------------------
from enum import Enum # import:enum:Enum, import_module:enum, import_name:Enum, whole_span:6 (-> +5)
class Suit(Enum): # class:Suit (-> +4)
    SPADES = 1 # assignment:1, assignment_lhs_identifier:SPADES, assignment_rhs_atom:1, literal:1, single_assignment:SPADES
    HEARTS = 2 # assignment:2, assignment_lhs_identifier:HEARTS, assignment_rhs_atom:2, literal:2, single_assignment:HEARTS
    DIAMONDS = 3 # assignment:3, assignment_lhs_identifier:DIAMONDS, assignment_rhs_atom:3, literal:3, single_assignment:DIAMONDS, suggest_constant_definition
    CLUBS = 4 # assignment:4, assignment_lhs_identifier:CLUBS, assignment_rhs_atom:4, literal:4, single_assignment:CLUBS, suggest_constant_definition

# ----------------------------------------------------------------------------------------
# 123.2146-assert-condition.py
# ----------------------------------------------------------------------------------------
assert isConsistent # assertion, whole_span:1

# ----------------------------------------------------------------------------------------
# 124.2152-binary-search-for-a-value-in-sorted-array.py
# ----------------------------------------------------------------------------------------
import bisect # import:bisect, import_module:bisect, whole_span:4 (-> +3)
def binarySearch(a, x): # function:binarySearch (-> +2), function_argument:a, function_argument:x, function_argument_flavor:arg, function_returning_something:binarySearch (-> +2)
    i = bisect.bisect_left(a, x) # assignment:bisect_left, assignment_lhs_identifier:i, assignment_rhs_atom:a, assignment_rhs_atom:bisect, assignment_rhs_atom:x, call_argument:a, call_argument:x, member_call:bisect_left, single_assignment:i
    return i if i != len(a) and a[i] == x else -1 # boolean_operator:And, call_argument:a, comparison_operator:Eq, comparison_operator:NotEq, conditional_expression, external_free_call:len, free_call:len, index:i, literal:-1, return

# ----------------------------------------------------------------------------------------
# 125.2167-measure-function-call-duration.py
# ----------------------------------------------------------------------------------------
import time # import:time, import_module:time, whole_span:5 (-> +4)
t1 = time.perf_counter() # assignment:perf_counter, assignment_lhs_identifier:t1, assignment_rhs_atom:time, member_call:perf_counter, single_assignment:t1
foo() # external_free_call:foo, free_call:foo, free_call_without_arguments:foo, free_call_without_result:foo
t2 = time.perf_counter() # assignment:perf_counter, assignment_lhs_identifier:t2, assignment_rhs_atom:time, member_call:perf_counter, single_assignment:t2
print("Seconds:", t2 - t1) # binary_operator:Sub, call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str

# ----------------------------------------------------------------------------------------
# 126.2137-multiple-return-values.py
# ----------------------------------------------------------------------------------------
def foo(): # function:foo (-> +1), function_returning_something:foo (-> +1), function_without_arguments:foo (-> +1), whole_span:2 (-> +1)
    return "string", True # literal:Str, literal:True, literal:Tuple, return

# ----------------------------------------------------------------------------------------
# 127.2274-source-code-inclusion.py
# ----------------------------------------------------------------------------------------
import imp # import:imp, import_module:imp, whole_span:2 (-> +1)
foo = imp.load_module("foobody", "foobody.txt").foo # assignment, assignment_lhs_identifier:foo, assignment_rhs_atom:imp, call_argument:, literal:Str, member_call:load_module, member_call_object:imp, single_assignment:foo

# ----------------------------------------------------------------------------------------
# 128.2085-breadth-first-traversing-of-a-tree.py
# ----------------------------------------------------------------------------------------
def BFS(f, root): # function:BFS (-> +8), function_argument:f, function_argument:root, function_argument_flavor:arg, function_returning_nothing:BFS (-> +8), higher_order_function:f (-> +8), whole_span:9 (-> +8)
    Q = [root] # assignment, assignment_lhs_identifier:Q, assignment_rhs_atom:root, literal:List, single_assignment:Q
    while Q: # loop:while (-> +6), loop_with_late_exit:while (-> +6), while (-> +6)
        n = Q.pop(0) # assignment:pop, assignment_lhs_identifier:n, assignment_rhs_atom:0, assignment_rhs_atom:Q, call_argument:0, literal:0, member_call:pop, single_assignment:n
        f(n) # call_argument:n, external_free_call:f, free_call:f, free_call_without_result:f
        for child in n: # for:child (-> +3), for_each (-> +3), loop:for (-> +3), loop_with_late_exit:for (-> +3)
            if not n.discovered: # if (-> +2), if_test_atom:n, if_without_else (-> +2), unary_operator:Not
                n.discovered = True # assignment:True, assignment_lhs_identifier:n, assignment_rhs_atom:True, if_then_branch (-> +1), literal:True
                Q.append(n) # call_argument:n, member_call:append, member_call_object:Q, member_call_without_result:append, update:Q:n, update_by_member_call:Q:n, update_by_member_call_with:append, update_with:append

# ----------------------------------------------------------------------------------------
# 129.2282-breadth-first-traversing-in-a-graph.py
# ----------------------------------------------------------------------------------------
from collections import deque # import:collections:deque, import_module:collections, import_name:deque, whole_span:9 (-> +8)
def breadth_first(start, f): # function:breadth_first (-> +7), function_argument:f, function_argument:start, function_argument_flavor:arg, function_returning_nothing:breadth_first (-> +7), higher_order_function:f (-> +7)
    seen = set() # assignment:set, assignment_lhs_identifier:seen, external_free_call:set, free_call:set, free_call_without_arguments:set, single_assignment:seen
    q = deque([start]) # assignment:deque, assignment_lhs_identifier:q, assignment_rhs_atom:start, call_argument:, external_free_call:deque, free_call:deque, literal:List, single_assignment:q
    while q: # loop:while (-> +4), loop_with_late_exit:while (-> +4), while (-> +4)
        vertex = q.popleft() # assignment:popleft, assignment_lhs_identifier:vertex, assignment_rhs_atom:q, member_call:popleft, single_assignment:vertex
        f(vertex) # call_argument:vertex, external_free_call:f, free_call:f, free_call_without_result:f
        seen.add(vertex) # call_argument:vertex, member_call:add, member_call_object:seen, member_call_without_result:add, update:seen:vertex, update_by_member_call:seen:vertex, update_by_member_call_with:add, update_with:add
        q.extend(v for v in vertex.adjacent if v not in seen) # call_argument:, comparison_operator:NotIn, comprehension:Generator, comprehension_for_count:1, filtered_comprehension, member_call:extend, member_call_object:q, member_call_without_result:extend

# ----------------------------------------------------------------------------------------
# 130.2283-depth-first-traversing-in-a-graph.py
# ----------------------------------------------------------------------------------------
def depth_first(start, f): # function:depth_first (-> +7), function_argument:f, function_argument:start, function_argument_flavor:arg, function_returning_nothing:depth_first (-> +7), higher_order_function:f (-> +7), whole_span:8 (-> +7)
    seen = set() # assignment:set, assignment_lhs_identifier:seen, external_free_call:set, free_call:set, free_call_without_arguments:set, single_assignment:seen
    stack = [start] # assignment, assignment_lhs_identifier:stack, assignment_rhs_atom:start, literal:List, single_assignment:stack
    while stack: # loop:while (-> +4), loop_with_late_exit:while (-> +4), while (-> +4)
        vertex = stack.pop() # assignment:pop, assignment_lhs_identifier:vertex, assignment_rhs_atom:stack, member_call:pop, single_assignment:vertex
        f(vertex) # call_argument:vertex, external_free_call:f, free_call:f, free_call_without_result:f
        seen.add(vertex) # call_argument:vertex, member_call:add, member_call_object:seen, member_call_without_result:add, update:seen:vertex, update_by_member_call:seen:vertex, update_by_member_call_with:add, update_with:add
        stack.extend(v for v in vertex.adjacent if v not in seen) # call_argument:, comparison_operator:NotIn, comprehension:Generator, comprehension_for_count:1, filtered_comprehension, member_call:extend, member_call_object:stack, member_call_without_result:extend

# ----------------------------------------------------------------------------------------
# 131.2083-successive-conditions.py
# ----------------------------------------------------------------------------------------
f1 if c1 else f2 if c2 else f3 if c3 else None # conditional_expression, literal:None, whole_span:1

# ----------------------------------------------------------------------------------------
# 131.2766-successive-conditions.py
# ----------------------------------------------------------------------------------------
if c1: # if (-> +5), whole_span:6 (-> +5)
    f1() # external_free_call:f1, free_call:f1, free_call_without_arguments:f1, free_call_without_result:f1, if_then_branch
elif c2: # if (-> +3)
    f2() # external_free_call:f2, free_call:f2, free_call_without_arguments:f2, free_call_without_result:f2, if_elif_branch
elif c3: # if (-> +1)
    f3() # external_free_call:f3, free_call:f3, free_call_without_arguments:f3, free_call_without_result:f3, if_elif_branch

# ----------------------------------------------------------------------------------------
# 132.2040-measure-duration-of-procedure-execution.py
# ----------------------------------------------------------------------------------------
import timeit # import:timeit, import_module:timeit, whole_span:2 (-> +1)
duration = timeit.timeit("f()", setup="from __main__ import f") # assignment:timeit, assignment_lhs_identifier:duration, assignment_rhs_atom:timeit, call_argument:, literal:Str, member_call:timeit, single_assignment:duration

# ----------------------------------------------------------------------------------------
# 133.2160-case-insensitive-string-contains.py
# ----------------------------------------------------------------------------------------
ok = word.lower() in s.lower() # assignment, assignment_lhs_identifier:ok, assignment_rhs_atom:s, assignment_rhs_atom:word, comparison_operator:In, member_call:lower, single_assignment:ok, whole_span:1

# ----------------------------------------------------------------------------------------
# 134.1850-create-a-new-list.py
# ----------------------------------------------------------------------------------------
items = [a, b, c] # assignment, assignment_lhs_identifier:items, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:c, literal:List, single_assignment:items, whole_span:1

# ----------------------------------------------------------------------------------------
# 135.2158-remove-item-from-list-by-its-value.py
# ----------------------------------------------------------------------------------------
items.remove(x) # call_argument:x, member_call:remove, member_call_object:items, member_call_without_result:remove, update:items:x, update_by_member_call:items:x, update_by_member_call_with:remove, update_with:remove, whole_span:1

# ----------------------------------------------------------------------------------------
# 136.2141-remove-all-occurrences-of-a-value-from-a-list.py
# ----------------------------------------------------------------------------------------
newlist = [item for item in items if item != x] # assignment, assignment_lhs_identifier:newlist, assignment_rhs_atom:item, assignment_rhs_atom:items, assignment_rhs_atom:x, comparison_operator:NotEq, comprehension:List, comprehension_for_count:1, filtered_comprehension, single_assignment:newlist, whole_span:1

# ----------------------------------------------------------------------------------------
# 137.1823-check-if-string-contains-only-digits.py
# ----------------------------------------------------------------------------------------
b = s.isdigit() # assignment:isdigit, assignment_lhs_identifier:b, assignment_rhs_atom:s, member_call:isdigit, single_assignment:b, whole_span:1

# ----------------------------------------------------------------------------------------
# 138.2161-create-temp-file.py
# ----------------------------------------------------------------------------------------
import tempfile # import:tempfile, import_module:tempfile, whole_span:2 (-> +1)
file = tempfile.TemporaryFile() # assignment:TemporaryFile, assignment_lhs_identifier:file, assignment_rhs_atom:tempfile, member_call:TemporaryFile, single_assignment:file

# ----------------------------------------------------------------------------------------
# 139.2162-create-temp-directory.py
# ----------------------------------------------------------------------------------------
import tempfile # import:tempfile, import_module:tempfile, whole_span:2 (-> +1)
td = tempfile.TemporaryDirectory() # assignment:TemporaryDirectory, assignment_lhs_identifier:td, assignment_rhs_atom:tempfile, member_call:TemporaryDirectory, single_assignment:td

# ----------------------------------------------------------------------------------------
# 140.2156-delete-map-entry.py
# ----------------------------------------------------------------------------------------
m.pop(k, None) # call_argument:None, call_argument:k, literal:None, member_call:pop, member_call_object:m, member_call_without_result:pop, update:m:None, update:m:k, update_by_member_call:m:None, update_by_member_call:m:k, update_by_member_call_with:pop, update_with:pop, whole_span:1

# ----------------------------------------------------------------------------------------
# 141.2159-iterate-in-sequence-over-two-lists.py
# ----------------------------------------------------------------------------------------
for x in items1 + items2: # addition_operator, binary_operator:Add, for:x (-> +1), loop:for (-> +1), loop_with_late_exit:for (-> +1), whole_span:2 (-> +1)
    print(x) # call_argument:x, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 142.2151-hexadecimal-digits-of-an-integer.py
# ----------------------------------------------------------------------------------------
s = hex(x) # assignment:hex, assignment_lhs_identifier:s, assignment_rhs_atom:x, call_argument:x, external_free_call:hex, free_call:hex, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 143.2256-iterate-alternatively-over-two-lists.py
# ----------------------------------------------------------------------------------------
for pair in zip(item1, item2): # call_argument:item1, call_argument:item2, external_free_call:zip, for:pair (-> +1), free_call:zip, loop:for (-> +1), loop_with_late_exit:for (-> +1), whole_span:2 (-> +1)
    print(pair) # call_argument:pair, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 144.2145-check-if-file-exists.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os, whole_span:2 (-> +1)
b = os.path.exists(fp) # assignment:exists, assignment_lhs_identifier:b, assignment_rhs_atom:fp, assignment_rhs_atom:os, call_argument:fp, member_call:exists, single_assignment:b

# ----------------------------------------------------------------------------------------
# 144.2915-check-if-file-exists.py
# ----------------------------------------------------------------------------------------
from pathlib import Path # import:pathlib:Path, import_module:pathlib, import_name:Path, whole_span:2 (-> +1)
b = Path(fp).exists() # assignment:exists, assignment_lhs_identifier:b, assignment_rhs_atom:fp, call_argument:fp, external_free_call:Path, free_call:Path, member_call:exists, single_assignment:b

# ----------------------------------------------------------------------------------------
# 145.1822-print-log-line-with-datetime.py
# ----------------------------------------------------------------------------------------
import sys, logging # import:logging, import:sys, import_module:logging, import_module:sys, whole_span:6 (-> +5)
logging.basicConfig( # member_call:basicConfig, member_call_object:logging, member_call_without_result:basicConfig
    stream=sys.stdout, level=logging.DEBUG, format="%(asctime)-15s %(message)s" # literal:Str
)
logger = logging.getLogger("NAME OF LOGGER") # assignment:getLogger, assignment_lhs_identifier:logger, assignment_rhs_atom:logging, call_argument:, literal:Str, member_call:getLogger, single_assignment:logger
logger.info(msg) # call_argument:msg, member_call:info, member_call_object:logger, member_call_without_result:info

# ----------------------------------------------------------------------------------------
# 146.1825-convert-string-to-floating-point-number.py
# ----------------------------------------------------------------------------------------
import locale # import:locale, import_module:locale, whole_span:4 (-> +3)
s = u"545,2222" # assignment, assignment_lhs_identifier:s, literal:Str, single_assignment:s
locale.setlocale(locale.LC_ALL, "de") # call_argument:, literal:Str, member_call:setlocale, member_call_object:locale, member_call_without_result:setlocale
f = locale.atof(s) # assignment:atof, assignment_lhs_identifier:f, assignment_rhs_atom:locale, assignment_rhs_atom:s, call_argument:s, member_call:atof, single_assignment:f

# ----------------------------------------------------------------------------------------
# 146.1826-convert-string-to-floating-point-number.py
# ----------------------------------------------------------------------------------------
f = float(s) # assignment:float, assignment_lhs_identifier:f, assignment_rhs_atom:s, call_argument:s, external_free_call:float, free_call:float, single_assignment:f, whole_span:1

# ----------------------------------------------------------------------------------------
# 146.2739-convert-string-to-floating-point-number.py
# ----------------------------------------------------------------------------------------
float("1.3") # call_argument:, external_free_call:float, free_call:float, free_call_without_result:float, literal:Str, whole_span:1

# ----------------------------------------------------------------------------------------
# 147.2171-remove-all-non-ascii-characters.py
# ----------------------------------------------------------------------------------------
import re # import:re, import_module:re, whole_span:2 (-> +1)
t = re.sub("[^\u0000-\u007f]", "", s) # assignment:sub, assignment_lhs_identifier:t, assignment_rhs_atom:re, assignment_rhs_atom:s, call_argument:, call_argument:s, empty_literal:Str, literal:Str, member_call:sub, single_assignment:t

# ----------------------------------------------------------------------------------------
# 148.1829-read-list-of-integer-numbers-from-stdin.py
# ----------------------------------------------------------------------------------------
list(map(int, input().split())) # call_argument:, call_argument:int, composition, external_free_call:input, external_free_call:list, external_free_call:map, free_call:input, free_call:list, free_call:map, free_call_without_arguments:input, free_call_without_result:list, member_call:split, whole_span:1

# ----------------------------------------------------------------------------------------
# 150.2154-remove-trailing-slash.py
# ----------------------------------------------------------------------------------------
p = p.rstrip("/") # assignment:rstrip, assignment_lhs_identifier:p, assignment_rhs_atom:p, call_argument:, literal:Str, member_call:rstrip, single_assignment:p, whole_span:1

# ----------------------------------------------------------------------------------------
# 151.2166-remove-string-trailing-path-separator.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os, whole_span:3 (-> +2)
if p.endswith(os.sep): # call_argument:, if (-> +1), if_test_atom:os, if_test_atom:p, if_without_else (-> +1), member_call:endswith
    p = p[:-1] # assignment, assignment_lhs_identifier:p, assignment_rhs_atom:-1, assignment_rhs_atom:p, if_then_branch, literal:-1, single_assignment:p, slice::-1:, slice_lower:, slice_step:, slice_upper:-1, update:p:-1, update_by_assignment:p:-1, update_by_assignment_with, update_with

# ----------------------------------------------------------------------------------------
# 152.2153-turn-a-character-into-a-string.py
# ----------------------------------------------------------------------------------------
s = c # assignment, assignment_lhs_identifier:s, assignment_rhs_atom:c, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 153.1980-concatenate-string-with-integer.py
# ----------------------------------------------------------------------------------------
t = "{}{}".format(s, i) # assignment:format, assignment_lhs_identifier:t, assignment_rhs_atom:i, assignment_rhs_atom:s, call_argument:i, call_argument:s, literal:Str, member_call:format, single_assignment:t, whole_span:1

# ----------------------------------------------------------------------------------------
# 154.2155-halfway-between-two-hex-color-codes.py
# ----------------------------------------------------------------------------------------
r1, g1, b1 = [int(c1[p : p + 2], 16) for p in range(1, 6, 2)] # addition_operator, assignment, assignment_lhs_identifier:b1, assignment_lhs_identifier:g1, assignment_lhs_identifier:r1, assignment_rhs_atom:1, assignment_rhs_atom:16, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:c1, assignment_rhs_atom:p, binary_operator:Add, call_argument:, call_argument:1, call_argument:16, call_argument:2, call_argument:6, comprehension:List, comprehension_for_count:1, external_free_call:int, external_free_call:range, free_call:int, free_call:range, literal:1, literal:16, literal:2, literal:6, literal:Tuple, parallel_assignment:3, range:1:6:2, slice:p:_:, slice_lower:p, slice_step:, slice_upper:_, whole_span:3 (-> +2)
r2, g2, b2 = [int(c2[p : p + 2], 16) for p in range(1, 6, 2)] # addition_operator, assignment, assignment_lhs_identifier:b2, assignment_lhs_identifier:g2, assignment_lhs_identifier:r2, assignment_rhs_atom:1, assignment_rhs_atom:16, assignment_rhs_atom:2, assignment_rhs_atom:6, assignment_rhs_atom:c2, assignment_rhs_atom:p, binary_operator:Add, call_argument:, call_argument:1, call_argument:16, call_argument:2, call_argument:6, comprehension:List, comprehension_for_count:1, external_free_call:int, external_free_call:range, free_call:int, free_call:range, literal:1, literal:16, literal:2, literal:6, literal:Tuple, parallel_assignment:3, range:1:6:2, slice:p:_:, slice_lower:p, slice_step:, slice_upper:_
c = "#{:02x}{:02x}{:02x}".format((r1 + r2) // 2, (g1 + g2) // 2, (b1 + b2) // 2) # addition_operator, assignment:format, assignment_lhs_identifier:c, assignment_rhs_atom:2, assignment_rhs_atom:b1, assignment_rhs_atom:b2, assignment_rhs_atom:g1, assignment_rhs_atom:g2, assignment_rhs_atom:r1, assignment_rhs_atom:r2, binary_operator:Add, binary_operator:FloorDiv, call_argument:, literal:2, literal:Str, member_call:format, single_assignment:c

# ----------------------------------------------------------------------------------------
# 154.2292-halfway-between-two-hex-color-codes.py
# ----------------------------------------------------------------------------------------
import numpy # import:numpy, import_module:numpy, whole_span:15 (-> +14)
class RGB(numpy.ndarray): # class:RGB (-> +8)
    @classmethod # class_method:from_str (-> +4), decorated_function:from_str (-> +4), function:from_str (-> +4), function_decorator:classmethod (-> +4), function_returning_something:from_str (-> +4), method:from_str (-> +4)
    def from_str(cls, rgbstr): # function_argument:cls, function_argument:rgbstr, function_argument_flavor:arg
        return numpy.array( # composition, member_call:array, member_call:view, member_call_object:numpy, method_chaining, return
            [int(rgbstr[i : i + 2], 16) for i in range(1, len(rgbstr), 2)] # addition_operator, binary_operator:Add, call_argument:, call_argument:1, call_argument:16, call_argument:2, call_argument:rgbstr, composition, comprehension:List, comprehension_for_count:1, external_free_call:int, external_free_call:len, external_free_call:range, free_call:int, free_call:len, free_call:range, literal:1, literal:16, literal:2, range:1:_:2, slice:i:_:, slice_lower:i, slice_step:, slice_upper:_, suggest_constant_definition
        ).view(cls) # call_argument:cls
    def __str__(self): # function:__str__ (-> +2), function_argument:self, function_argument_flavor:arg, function_returning_something:__str__ (-> +2), instance_method:__str__ (-> +2), method:__str__ (-> +2)
        self = self.astype(numpy.uint8) # assignment:astype, assignment_lhs_identifier:self, assignment_rhs_atom:numpy, assignment_rhs_atom:self, call_argument:, member_call:astype, single_assignment:self, update:self:numpy, update_by_assignment:self:numpy, update_by_assignment_with:astype, update_with:astype
        return "#" + "".join(format(n, "x") for n in self) # binary_operator:Add, call_argument:, call_argument:n, composition, comprehension:Generator, comprehension_for_count:1, concatenation_operator:Str, empty_literal:Str, external_free_call:format, free_call:format, literal:Str, member_call:join, return
c1 = RGB.from_str("#a1b1c1") # assignment:from_str, assignment_lhs_identifier:c1, assignment_rhs_atom:RGB, call_argument:, literal:Str, member_call:from_str, single_assignment:c1
print(c1) # call_argument:c1, external_free_call:print, free_call:print, free_call_without_result:print
c2 = RGB.from_str("#1A1B1C") # assignment:from_str, assignment_lhs_identifier:c2, assignment_rhs_atom:RGB, call_argument:, literal:Str, member_call:from_str, single_assignment:c2
print(c2) # call_argument:c2, external_free_call:print, free_call:print, free_call_without_result:print
print((c1 + c2) / 2) # addition_operator, binary_operator:Add, binary_operator:Div, call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:2

# ----------------------------------------------------------------------------------------
# 155.2147-delete-file.py
# ----------------------------------------------------------------------------------------
import pathlib # import:pathlib, import_module:pathlib, whole_span:3 (-> +2)
path = pathlib.Path(_filepath) # assignment:Path, assignment_lhs_identifier:path, assignment_rhs_atom:_filepath, assignment_rhs_atom:pathlib, call_argument:_filepath, member_call:Path, single_assignment:path
path.unlink() # member_call:unlink, member_call_object:path, member_call_without_result:unlink

# ----------------------------------------------------------------------------------------
# 156.2148-format-integer-with-zero-padding.py
# ----------------------------------------------------------------------------------------
s = format("03d", i) # assignment:format, assignment_lhs_identifier:s, assignment_rhs_atom:i, call_argument:, call_argument:i, external_free_call:format, free_call:format, literal:Str, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 157.2150-declare-constant-string.py
# ----------------------------------------------------------------------------------------
PLANET = "Earth" # assignment, assignment_lhs_identifier:PLANET, literal:Str, single_assignment:PLANET, whole_span:1

# ----------------------------------------------------------------------------------------
# 158.2163-random-sublist.py
# ----------------------------------------------------------------------------------------
import random # import:random, import_module:random, whole_span:2 (-> +1)
y = random.sample(x, k) # assignment:sample, assignment_lhs_identifier:y, assignment_rhs_atom:k, assignment_rhs_atom:random, assignment_rhs_atom:x, call_argument:k, call_argument:x, member_call:sample, single_assignment:y

# ----------------------------------------------------------------------------------------
# 159.2281-trie.py
# ----------------------------------------------------------------------------------------
class Trie: # class:Trie (-> +4), whole_span:5 (-> +4)
    def __init__(self, prefix, value=None): # function:__init__ (-> +3), function_argument:prefix, function_argument:self, function_argument:value, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +3), instance_method:__init__ (-> +3), literal:None, method:__init__ (-> +3)
        self.prefix = prefix # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:prefix
        self.children = [] # assignment, assignment_lhs_identifier:self, empty_literal:List, literal:List
        self.value = value # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:value

# ----------------------------------------------------------------------------------------
# 160.2165-detect-if-32-bit-or-64-bit-architecture.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, whole_span:5 (-> +4)
if sys.maxsize > 2 ** 32: # binary_operator:Pow, comparison_operator:Gt, if (-> +3), if_test_atom:2, if_test_atom:32, if_test_atom:sys, literal:2, literal:32
    f64() # external_free_call:f64, free_call:f64, free_call_without_arguments:f64, free_call_without_result:f64, if_then_branch
else:
    f32() # external_free_call:f32, free_call:f32, free_call_without_arguments:f32, free_call_without_result:f32, if_else_branch

# ----------------------------------------------------------------------------------------
# 161.2098-multiply-all-the-elements-of-a-list.py
# ----------------------------------------------------------------------------------------
elements = [c * x for x in elements] # assignment, assignment_lhs_identifier:elements, assignment_rhs_atom:c, assignment_rhs_atom:elements, assignment_rhs_atom:x, binary_operator:Mult, comprehension:List, comprehension_for_count:1, multiplication_operator, single_assignment:elements, update:elements:c, update:elements:x, update_by_assignment:elements:c, update_by_assignment:elements:x, update_by_assignment_with, update_with, whole_span:1

# ----------------------------------------------------------------------------------------
# 162.2164-execute-procedures-depending-on-options.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, whole_span:5 (-> +4)
if "b" in sys.argv[1:]: # comparison_operator:In, if (-> +1), if_test_atom:1, if_test_atom:sys, if_without_else (-> +1), literal:1, literal:Str, slice:1::, slice_lower:1, slice_step:, slice_upper:, yoda_comparison:In
    bat() # external_free_call:bat, free_call:bat, free_call_without_arguments:bat, free_call_without_result:bat, if_then_branch
if "f" in sys.argv[1:]: # comparison_operator:In, if (-> +1), if_test_atom:1, if_test_atom:sys, if_without_else (-> +1), literal:1, literal:Str, slice:1::, slice_lower:1, slice_step:, slice_upper:, yoda_comparison:In
    fox() # external_free_call:fox, free_call:fox, free_call_without_arguments:fox, free_call_without_result:fox, if_then_branch

# ----------------------------------------------------------------------------------------
# 163.2170-print-list-elements-by-group-of-2.py
# ----------------------------------------------------------------------------------------
for x in zip(list[::2], list[1::2]): # call_argument:, external_free_call:zip, for:x (-> +1), free_call:zip, literal:1, literal:2, loop:for (-> +1), loop_with_late_exit:for (-> +1), slice:1::2, slice:::2, slice_lower:, slice_lower:1, slice_step:2, slice_upper:, whole_span:2 (-> +1)
    print(x) # call_argument:x, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 163.3177-print-list-elements-by-group-of-2.py
# ----------------------------------------------------------------------------------------
from itertools import tee # import:itertools:tee, import_module:itertools, import_name:tee, whole_span:7 (-> +6)
def pairwise(iterable): # function:pairwise (-> +3), function_argument:iterable, function_argument_flavor:arg, function_returning_something:pairwise (-> +3)
    a, b = tee(iterable) # assignment:tee, assignment_lhs_identifier:a, assignment_lhs_identifier:b, assignment_rhs_atom:iterable, call_argument:iterable, external_free_call:tee, free_call:tee, literal:Tuple, parallel_assignment:2
    next(b, None) # call_argument:None, call_argument:b, external_free_call:next, free_call:next, free_call_without_result:next, literal:None
    return zip(a, b) # call_argument:a, call_argument:b, external_free_call:zip, free_call:zip, free_tail_call:zip, return
for a, b in pairwise(list): # call_argument:list, for:a (-> +1), for:b (-> +1), free_call:pairwise, internal_free_call:pairwise, literal:Tuple, loop:for (-> +1), loop_with_late_exit:for (-> +1)
    print(a, b) # call_argument:a, call_argument:b, external_free_call:print, free_call:print, free_call_without_result:print

# ----------------------------------------------------------------------------------------
# 164.2169-open-url-in-default-browser.py
# ----------------------------------------------------------------------------------------
import webbrowser # import:webbrowser, import_module:webbrowser, whole_span:2 (-> +1)
webbrowser.open(s) # call_argument:s, member_call:open, member_call_object:webbrowser, member_call_without_result:open

# ----------------------------------------------------------------------------------------
# 165.2149-last-element-of-list.py
# ----------------------------------------------------------------------------------------
x = items[-1] # assignment, assignment_lhs_identifier:x, assignment_rhs_atom:-1, assignment_rhs_atom:items, index:-1, literal:-1, negative_index:-1, single_assignment:x, whole_span:1

# ----------------------------------------------------------------------------------------
# 166.2272-concatenate-two-lists.py
# ----------------------------------------------------------------------------------------
ab = a + b # addition_operator, assignment:Add, assignment_lhs_identifier:ab, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:Add, single_assignment:ab, whole_span:1

# ----------------------------------------------------------------------------------------
# 167.2611-trim-prefix.py
# ----------------------------------------------------------------------------------------
t = s[s.startswith(p) and len(p) :] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:p, assignment_rhs_atom:s, boolean_operator:And, call_argument:p, external_free_call:len, free_call:len, member_call:startswith, single_assignment:t, slice:_::, slice_lower:_, slice_step:, slice_upper:, whole_span:1

# ----------------------------------------------------------------------------------------
# 167.3175-trim-prefix.py
# ----------------------------------------------------------------------------------------
t = s.lstrip(p) # assignment:lstrip, assignment_lhs_identifier:t, assignment_rhs_atom:p, assignment_rhs_atom:s, call_argument:p, member_call:lstrip, single_assignment:t, whole_span:1

# ----------------------------------------------------------------------------------------
# 168.2277-trim-suffix.py
# ----------------------------------------------------------------------------------------
t = s.rsplit(w, 1)[0] # assignment, assignment_lhs_identifier:t, assignment_rhs_atom:0, assignment_rhs_atom:1, assignment_rhs_atom:s, assignment_rhs_atom:w, call_argument:1, call_argument:w, index:0, literal:0, literal:1, member_call:rsplit, member_call_object:s, single_assignment:t, whole_span:1

# ----------------------------------------------------------------------------------------
# 168.3174-trim-suffix.py
# ----------------------------------------------------------------------------------------
t = s.rstrip(w) # assignment:rstrip, assignment_lhs_identifier:t, assignment_rhs_atom:s, assignment_rhs_atom:w, call_argument:w, member_call:rstrip, single_assignment:t, whole_span:1

# ----------------------------------------------------------------------------------------
# 169.2233-string-length.py
# ----------------------------------------------------------------------------------------
n = len(s) # assignment:len, assignment_lhs_identifier:n, assignment_rhs_atom:s, call_argument:s, external_free_call:len, free_call:len, single_assignment:n, whole_span:1

# ----------------------------------------------------------------------------------------
# 170.2275-get-map-size.py
# ----------------------------------------------------------------------------------------
n = len(mymap) # assignment:len, assignment_lhs_identifier:n, assignment_rhs_atom:mymap, call_argument:mymap, external_free_call:len, free_call:len, single_assignment:n, whole_span:1

# ----------------------------------------------------------------------------------------
# 171.2446-add-an-element-at-the-end-of-a-list.py
# ----------------------------------------------------------------------------------------
s.append(x) # call_argument:x, member_call:append, member_call_object:s, member_call_without_result:append, update:s:x, update_by_member_call:s:x, update_by_member_call_with:append, update_with:append, whole_span:1

# ----------------------------------------------------------------------------------------
# 172.2442-insert-entry-in-map.py
# ----------------------------------------------------------------------------------------
m[k] = v # assignment, assignment_lhs_identifier:m, assignment_rhs_atom:v, index:k, whole_span:1

# ----------------------------------------------------------------------------------------
# 173.2427-format-a-number-with-grouped-thousands.py
# ----------------------------------------------------------------------------------------
print("f'{1000:,}'") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, whole_span:1

# ----------------------------------------------------------------------------------------
# 173.2428-format-a-number-with-grouped-thousands.py
# ----------------------------------------------------------------------------------------
print("format(1000, ',')") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, whole_span:1

# ----------------------------------------------------------------------------------------
# 173.2429-format-a-number-with-grouped-thousands.py
# ----------------------------------------------------------------------------------------
print("'{:,}'.format(1000)") # call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, literal:Str, whole_span:1

# ----------------------------------------------------------------------------------------
# 174.2687-make-http-post-request.py
# ----------------------------------------------------------------------------------------
from urllib import request, parse # import:urllib:parse, import:urllib:request, import_module:urllib, import_name:parse, import_name:request, whole_span:4 (-> +3)
data = parse.urlencode("<your data dict>").encode() # assignment:encode, assignment_lhs_identifier:data, assignment_rhs_atom:parse, call_argument:, literal:Str, member_call:encode, member_call:urlencode, member_call_object:parse, method_chaining, single_assignment:data
req = request.Request(u, data=data, method="POST") # assignment:Request, assignment_lhs_identifier:req, assignment_rhs_atom:data, assignment_rhs_atom:request, assignment_rhs_atom:u, call_argument:u, literal:Str, member_call:Request, single_assignment:req
resp = request.urlopen(req) # assignment:urlopen, assignment_lhs_identifier:resp, assignment_rhs_atom:req, assignment_rhs_atom:request, call_argument:req, member_call:urlopen, single_assignment:resp

# ----------------------------------------------------------------------------------------
# 175.2613-bytes-to-hex-string.py
# ----------------------------------------------------------------------------------------
s = a.hex() # assignment:hex, assignment_lhs_identifier:s, assignment_rhs_atom:a, member_call:hex, single_assignment:s, whole_span:1

# ----------------------------------------------------------------------------------------
# 176.2614-hex-string-to-byte-array.py
# ----------------------------------------------------------------------------------------
a = bytearray.fromhex(s) # assignment:fromhex, assignment_lhs_identifier:a, assignment_rhs_atom:bytearray, assignment_rhs_atom:s, call_argument:s, member_call:fromhex, single_assignment:a, whole_span:1

# ----------------------------------------------------------------------------------------
# 177.2709-find-files-with-a-given-list-of-filename-extensions.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os, whole_span:3 (-> +2)
extensions = [".jpg", ".jpeg", ".png"] # assignment, assignment_lhs_identifier:extensions, literal:List, literal:Str, single_assignment:extensions
L = [f for f in os.listdir(D) if os.path.splitext(f)[1] in extensions] # assignment, assignment_lhs_identifier:L, assignment_rhs_atom:1, assignment_rhs_atom:D, assignment_rhs_atom:extensions, assignment_rhs_atom:f, assignment_rhs_atom:os, call_argument:D, call_argument:f, comparison_operator:In, comprehension:List, comprehension_for_count:1, filtered_comprehension, index:1, literal:1, member_call:listdir, member_call:splitext, single_assignment:L

# ----------------------------------------------------------------------------------------
# 177.2725-find-files-with-a-given-list-of-filename-extensions.py
# ----------------------------------------------------------------------------------------
import re # import:re, import_module:re, whole_span:7 (-> +6)
import os # import:os, import_module:os
filtered_files = [ # assignment, assignment_lhs_identifier:filtered_files, single_assignment:filtered_files
    "{}/{}".format(dirpath, filename) # assignment_rhs_atom:dirpath, assignment_rhs_atom:filename, call_argument:dirpath, call_argument:filename, comprehension:List, comprehension_for_count:2, literal:Str, member_call:format
    for dirpath, _, filenames in os.walk(D) # assignment_rhs_atom:D, assignment_rhs_atom:_, assignment_rhs_atom:dirpath, assignment_rhs_atom:filenames, assignment_rhs_atom:os, call_argument:D, literal:Tuple, member_call:walk
    for filename in filenames # assignment_rhs_atom:filename, assignment_rhs_atom:filenames
    if re.match(r"^.*\.(?:jpg|jpeg|png)$", filename) # assignment_rhs_atom:filename, assignment_rhs_atom:re, call_argument:, call_argument:filename, filtered_comprehension, literal:Str, member_call:match
]

# ----------------------------------------------------------------------------------------
# 177.3241-find-files-with-a-given-list-of-filename-extensions.py
# ----------------------------------------------------------------------------------------
import glob # import:glob, import_module:glob, whole_span:3 (-> +2)
import itertools # import:itertools, import_module:itertools
list(itertools.chain(*(glob.glob("*/**.%s" % ext) for ext in ["jpg", "jpeg", "png"]))) # binary_operator:Mod, call_argument:, composition, comprehension:Generator, comprehension_for_count:1, external_free_call:list, free_call:list, free_call_without_result:list, literal:List, literal:Str, member_call:chain, member_call:glob, string_formatting_operator

# ----------------------------------------------------------------------------------------
# 178.2615-check-if-point-is-inside-rectangle.py
# ----------------------------------------------------------------------------------------
b = (x1 < x < x2) and (y1 < y < y2) # assignment, assignment_lhs_identifier:b, assignment_rhs_atom:x, assignment_rhs_atom:x1, assignment_rhs_atom:x2, assignment_rhs_atom:y, assignment_rhs_atom:y1, assignment_rhs_atom:y2, boolean_operator:And, chained_comparison:2, chained_inequalities:2, comparison_operator:Lt, single_assignment:b, whole_span:1

# ----------------------------------------------------------------------------------------
# 179.2688-get-center-of-a-rectangle.py
# ----------------------------------------------------------------------------------------
center = ((x1 + x2) / 2, (y1 + y2) / 2) # addition_operator, assignment, assignment_lhs_identifier:center, assignment_rhs_atom:2, assignment_rhs_atom:x1, assignment_rhs_atom:x2, assignment_rhs_atom:y1, assignment_rhs_atom:y2, binary_operator:Add, binary_operator:Div, literal:2, literal:Tuple, single_assignment:center, whole_span:1

# ----------------------------------------------------------------------------------------
# 179.2689-get-center-of-a-rectangle.py
# ----------------------------------------------------------------------------------------
from collections import namedtuple # import:collections:namedtuple, import_module:collections, import_name:namedtuple, whole_span:3 (-> +2)
Point = namedtuple("Point", "x y") # assignment:namedtuple, assignment_lhs_identifier:Point, call_argument:, external_free_call:namedtuple, free_call:namedtuple, literal:Str, single_assignment:Point
center = Point((x1 + x2) / 2, (y1 + y2) / 2) # addition_operator, assignment:Point, assignment_lhs_identifier:center, assignment_rhs_atom:2, assignment_rhs_atom:x1, assignment_rhs_atom:x2, assignment_rhs_atom:y1, assignment_rhs_atom:y2, binary_operator:Add, binary_operator:Div, call_argument:, external_free_call:Point, free_call:Point, literal:2, single_assignment:center

# ----------------------------------------------------------------------------------------
# 180.2612-list-files-in-directory.py
# ----------------------------------------------------------------------------------------
import os # import:os, import_module:os, whole_span:2 (-> +1)
x = os.listdir(d) # assignment:listdir, assignment_lhs_identifier:x, assignment_rhs_atom:d, assignment_rhs_atom:os, call_argument:d, member_call:listdir, single_assignment:x

# ----------------------------------------------------------------------------------------
# 182.2658-quine-program.py
# ----------------------------------------------------------------------------------------
s = "s = %r\nprint(s%%s)" # assignment, assignment_lhs_identifier:s, literal:Str, single_assignment:s, whole_span:2 (-> +1)
print(s % s) # binary_operator:Mod, call_argument:, external_free_call:print, free_call:print, free_call_without_result:print, modulo_operator

# ----------------------------------------------------------------------------------------
# 183.3025-make-http-put-request.py
# ----------------------------------------------------------------------------------------
requests # whole_span:7 (-> +6)
import requests # import:requests, import_module:requests
content_type = "text/plain" # assignment, assignment_lhs_identifier:content_type, literal:Str, single_assignment:content_type
headers = {"Content-Type": content_type} # assignment, assignment_lhs_identifier:headers, assignment_rhs_atom:content_type, literal:Dict, literal:Str, single_assignment:headers
data = {} # assignment, assignment_lhs_identifier:data, empty_literal:Dict, literal:Dict, single_assignment:data
r = requests.put(url, headers=headers, data=data) # assignment:put, assignment_lhs_identifier:r, assignment_rhs_atom:data, assignment_rhs_atom:headers, assignment_rhs_atom:requests, assignment_rhs_atom:url, call_argument:url, member_call:put, single_assignment:r
status_code, content = r.status_code, r.content # assignment, assignment_lhs_identifier:content, assignment_lhs_identifier:status_code, assignment_rhs_atom:r, literal:Tuple, parallel_assignment:2

# ----------------------------------------------------------------------------------------
# 184.2701-tomorrow.py
# ----------------------------------------------------------------------------------------
from datetime import date, timedelta # import:datetime:date, import:datetime:timedelta, import_module:datetime, import_name:date, import_name:timedelta, whole_span:2 (-> +1)
date.today() + timedelta(days=1) # addition_operator, binary_operator:Add, external_free_call:timedelta, free_call:timedelta, literal:1, member_call:today

# ----------------------------------------------------------------------------------------
# 185.2820-execute-function-in-30-seconds.py
# ----------------------------------------------------------------------------------------
import threading # import:threading, import_module:threading, whole_span:3 (-> +2)
timer = threading.Timer(30.0, f, args=(42,)) # assignment:Timer, assignment_lhs_identifier:timer, assignment_rhs_atom:30.0, assignment_rhs_atom:42, assignment_rhs_atom:f, assignment_rhs_atom:threading, call_argument:30.0, call_argument:f, literal:30.0, literal:42, literal:Tuple, member_call:Timer, single_assignment:timer
timer.start() # member_call:start, member_call_object:timer, member_call_without_result:start

# ----------------------------------------------------------------------------------------
# 186.2699-exit-program-cleanly.py
# ----------------------------------------------------------------------------------------
import sys # import:sys, import_module:sys, whole_span:2 (-> +1)
sys.exit(0) # call_argument:0, literal:0, member_call:exit, member_call_object:sys, member_call_without_result:exit

# ----------------------------------------------------------------------------------------
# 187.3261-disjoint-set.py
# ----------------------------------------------------------------------------------------
class UnionFind: # class:UnionFind (-> +14), whole_span:15 (-> +14)
    def __init__(self, size): # function:__init__ (-> +2), function_argument:self, function_argument:size, function_argument_flavor:arg, function_returning_nothing:__init__ (-> +2), instance_method:__init__ (-> +2), method:__init__ (-> +2)
        self.rank = [0] * size # assignment:Mult, assignment_lhs_identifier:self, assignment_rhs_atom:0, assignment_rhs_atom:size, binary_operator:Mult, literal:0, literal:List, replication_operator:List
        self.p = [i for i in range(size)] # assignment, assignment_lhs_identifier:self, assignment_rhs_atom:i, assignment_rhs_atom:size, call_argument:size, comprehension:List, comprehension_for_count:1, external_free_call:range, free_call:range, range:size
    def find_set(self, i): # function:find_set (-> +5), function_argument:i, function_argument:self, function_argument_flavor:arg, function_returning_something:find_set (-> +5), instance_method:find_set (-> +5), method:find_set (-> +5)
        if self.p[i] == i: # comparison_operator:Eq, if (-> +4), if_test_atom:i, if_test_atom:self, index:i
            return i # if_then_branch, return:i
        else:
            self.p[i] = self.find_set(self.p[i]) # assignment:find_set, assignment_rhs_atom:i, assignment_rhs_atom:self, call_argument:, if_else_branch (-> +1), index:i, member_call:find_set
            return self.p[i] # index:i, return
    def is_same_set(self, i, j): # function:is_same_set (-> +1), function_argument:i, function_argument:j, function_argument:self, function_argument_flavor:arg, function_returning_something:is_same_set (-> +1), instance_method:is_same_set (-> +1), method:is_same_set (-> +1)
        return self.find_set(i) == self.find_set(j) # call_argument:i, call_argument:j, comparison_operator:Eq, member_call:find_set, return
    def union_set(self, i, j): # function:union_set (-> +2), function_argument:i, function_argument:j, function_argument:self, function_argument_flavor:arg, function_returning_nothing:union_set (-> +2), instance_method:union_set (-> +2), method:union_set (-> +2)
        if not self.is_same_set(i, j): # call_argument:i, call_argument:j, if (-> +1), if_test_atom:i, if_test_atom:j, if_test_atom:self, if_without_else (-> +1), member_call:is_same_set, unary_operator:Not
            x, y = self.find_set(i), self.find_set(j) # assignment, assignment_lhs_identifier:x, assignment_lhs_identifier:y, assignment_rhs_atom:i, assignment_rhs_atom:j, assignment_rhs_atom:self, call_argument:i, call_argument:j, if_then_branch, literal:Tuple, member_call:find_set, parallel_assignment:2

# ----------------------------------------------------------------------------------------
# 188.3171-matrix-multiplication.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, whole_span:2 (-> +1)
c = a @ b # assignment:MatMult, assignment_lhs_identifier:c, assignment_rhs_atom:a, assignment_rhs_atom:b, binary_operator:MatMult, single_assignment:c

# ----------------------------------------------------------------------------------------
# 188.3284-matrix-multiplication.py
# ----------------------------------------------------------------------------------------
import numpy as np # import:numpy, import_module:numpy, whole_span:2 (-> +1)
c = np.matmul(a, b) # assignment:matmul, assignment_lhs_identifier:c, assignment_rhs_atom:a, assignment_rhs_atom:b, assignment_rhs_atom:np, call_argument:a, call_argument:b, member_call:matmul, single_assignment:c

# ----------------------------------------------------------------------------------------
# 189.3236-filter-and-transform-list.py
# ----------------------------------------------------------------------------------------
y = [T(e) for e in x if P(e)] # assignment, assignment_lhs_identifier:y, assignment_rhs_atom:e, assignment_rhs_atom:x, call_argument:e, comprehension:List, comprehension_for_count:1, external_free_call:P, external_free_call:T, filtered_comprehension, free_call:P, free_call:T, single_assignment:y, whole_span:1

# ----------------------------------------------------------------------------------------
# 191.3403-check-if-any-value-in-a-list-is-larger-than-a-limit.py
# ----------------------------------------------------------------------------------------
if any(v > x for v in a): # call_argument:, comparison_operator:Gt, comprehension:Generator, comprehension_for_count:1, external_free_call:any, free_call:any, if (-> +1), if_test_atom:a, if_test_atom:v, if_test_atom:x, if_without_else (-> +1), whole_span:2 (-> +1)
    f() # external_free_call:f, free_call:f, free_call_without_arguments:f, free_call_without_result:f, if_then_branch

# ----------------------------------------------------------------------------------------
# 197.3457-get-a-list-of-lines-from-a-file.py
# ----------------------------------------------------------------------------------------
with open(path) as f: # call_argument:path, external_free_call:open, free_call:open, whole_span:2 (-> +1)
    lines = f.readlines() # assignment:readlines, assignment_lhs_identifier:lines, assignment_rhs_atom:f, member_call:readlines, single_assignment:lines
