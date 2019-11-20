- [Introduction](#introduction)
- [Reference](#reference)
  - [Expressions](#expressions)
    - [Literals](#literals)
      - [Construct `literal`](#construct-literal)
    - [Subscripts](#subscripts)
      - [Construct `index`](#construct-index)
      - [Construct `index_arithmetic`](#construct-index_arithmetic)
      - [Construct `slice`](#construct-slice)
      - [Construct `slice_step`](#construct-slice_step)
    - [Arithmetic operators](#arithmetic-operators)
      - [Construct `binary_operator`](#construct-binary_operator)
      - [Construct `unary_operator`](#construct-unary_operator)
    - [Boolean expressions](#boolean-expressions)
      - [Construct `boolean_operator`](#construct-boolean_operator)
      - [Construct `comparison_operator`](#construct-comparison_operator)
      - [Construct `divisibility_test`](#construct-divisibility_test)
    - [Calls](#calls)
      - [Construct `function_call`](#construct-function_call)
      - [Construct `method_call`](#construct-method_call)
      - [Construct `method_chaining`](#construct-method_chaining)
      - [Construct `composition`](#construct-composition)
    - [Anonymous functions](#anonymous-functions)
      - [Construct `lambda_function`](#construct-lambda_function)
  - [Statements](#statements)
    - [Assignments](#assignments)
      - [Construct `global_constant_definition`](#construct-global_constant_definition)
      - [Construct `global_variable_definition`](#construct-global_variable_definition)
      - [Construct `assignment`](#construct-assignment)
      - [Construct `augmented_assignment`](#construct-augmented_assignment)
      - [Construct `chained_assignment`](#construct-chained_assignment)
      - [Construct `swapping`](#construct-swapping)
      - [Construct `negation`](#construct-negation)
    - [Function definitions](#function-definitions)
      - [Construct `function_definition`](#construct-function_definition)
      - [Construct `recursive_function_definition`](#construct-recursive_function_definition)
      - [Construct `deeply_recursive_function_definition`](#construct-deeply_recursive_function_definition)
      - [Construct `generator_definition`](#construct-generator_definition)
    - [Conditionals](#conditionals)
      - [Construct `if`](#construct-if)
      - [Construct `if_else`](#construct-if_else)
      - [Construct `if_elif`](#construct-if_elif)
    - [Iterations](#iterations)
      - [Construct `for_each`](#construct-for_each)
      - [Construct `for_range_stop`](#construct-for_range_stop)
      - [Construct `for_range_start`](#construct-for_range_start)
      - [Construct `for_range_step`](#construct-for_range_step)
      - [Construct `for_indexes_values`](#construct-for_indexes_values)
      - [Construct `for_indexes`](#construct-for_indexes)
      - [Construct `nested_for`](#construct-nested_for)
      - [Construct `triangular_nested_for`](#construct-triangular_nested_for)
  - [Code patterns](#code-patterns)
    - [Iterative patterns](#iterative-patterns)
      - [Sequential loops](#sequential-loops)
        - [Construct `accumulate_elements`](#construct-accumulate_elements)
        - [Construct `filter_for`](#construct-filter_for)
        - [Construct `find_best_element`](#construct-find_best_element)
        - [Construct `universal_quantifier`](#construct-universal_quantifier)
        - [Construct `existential_quantifier`](#construct-existential_quantifier)
        - [Construct `find_first_element`](#construct-find_first_element)
      - [Non sequential finite loops](#non-sequential-finite-loops)
        - [Construct `evolve_state`](#construct-evolve_state)
      - [Non sequential infinite loops](#non-sequential-infinite-loops)
        - [Construct `accumulate_stream`](#construct-accumulate_stream)
  - [Suggestions](#suggestions)
    - [Assignments](#assignments-1)
      - [Construct `suggest_conditional_expression`](#construct-suggest_conditional_expression)
      - [Construct `suggest_augmented_assignment`](#construct-suggest_augmented_assignment)
    - [Expressions](#expressions-1)
      - [Construct `suggest_comparison_chaining`](#construct-suggest_comparison_chaining)
      - [Construct `suggest_constant_definition`](#construct-suggest_constant_definition)
    - [Subroutines](#subroutines)
      - [Construct `suggest_condition_return`](#construct-suggest_condition_return)

# Introduction

# Reference

## Expressions

### Literals

--------------------------------------------------------------------------------

##### Construct `literal`

###### Regex

```re
^(.*)
(   # match None, True and False
              /_type='NameConstant'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/value=(?P<SUFFIX>None|True|False)
|   # match any other constant
              /_type='(?P<SUFFIX>Str|Num|Tuple|Dict|Set|List)'
\n(?:\1.+\n)*?\1/_ids=''
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
)
```

###### Example

```python
1   42
2   42.0
3   ""
4   (1, 1)
5   []
6   {}
7   {1, 2, 3}
8   True and False
9   None
10  {a, b, c} # no match
11  [1, 2, 3]
12  -42
```

###### Matches

```markdown
literal=Num: 1, 2, 4, 4, 7, 7, 7, 11, 11, 11, 12
literal=Str: 3
literal=Tuple: 4
literal=List: 5, 11
literal=Dict: 6
literal=Set: 7
literal=False: 8
literal=True: 8
literal=None: 9
```

--------------------------------------------------------------------------------

### Subscripts

--------------------------------------------------------------------------------

##### Construct `index`

###### Regex

```re
          ^(.*?)/_type='Subscript'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/slice/_type='Index'
```

###### Example

```python
1   a[42]
2   dictionary[key]
3   a[42:-1] # no match
```

###### Matches

```markdown
index: 1, 2
```

--------------------------------------------------------------------------------

##### Construct `index_arithmetic`

###### Regex

```re
          ^(.*?)/_type='Subscript'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/slice/_type='Index'
\n(?:\1.+\n)*?\1/slice/value/_type='BinOp'
```

###### Example

```python
1   a[i + j]
2   a[i]
```

###### Matches

```markdown
index_arithmetic: 1
```

--------------------------------------------------------------------------------

##### Construct `slice`

###### Regex

```re
          ^(.*?)/_type='Subscript'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P<_1>slice)/_type='Slice'
\n(?:\1.+\n)*?\1/(?P=_1)      /step=None
```

###### Example

```python
1   a[1] # no match
2   a[1:-1]
3   a[1:-1:2] # no match
```

###### Matches

```markdown
slice: 2
```

--------------------------------------------------------------------------------

##### Construct `slice_step`

###### Regex

```re
          ^(.*?)/_type='Subscript'
\n(?:\1.+\n)*?\1/(?P<_1>slice)/_type='Slice'
\n(?:\1.+\n)*?\1/(?P=_1)      /step/lineno=(?P<LINE>\d+)
```

###### Example

```python
1   a[1] # no match
2   a[1:-1] # no match
3   a[1:-1:2]
```

###### Matches

```markdown
slice_step: 3
```

--------------------------------------------------------------------------------

### Arithmetic operators

--------------------------------------------------------------------------------

##### Construct `binary_operator`

###### Regex

```re
          ^(.*?)/_type='BinOp'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/op/_type='(?P<SUFFIX>.+)'
```

###### Example

```python
1   2**32768 - 1
```

###### Matches

```markdown
binary_operator=Pow: 1
binary_operator=Sub: 1
```

--------------------------------------------------------------------------------

##### Construct `unary_operator`

###### Regex

```re
          ^(.*?)/_type='UnaryOp'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/op/_type='(?P<SUFFIX>.+)'
```

###### Example

```python
1   a = -b
2   b = not c
3   c = -1 # no match
```

**Remark.** Normally, a negative litteral is represented in the AST by a node `UnaryOp` with `USub` and `Num` children and a positive value for `n`. This is simplified into a node `Num` and a negative value for `n`.

###### Matches

```markdown
unary_operator=USub: 1
unary_operator=Not: 2
```

--------------------------------------------------------------------------------

### Boolean expressions

--------------------------------------------------------------------------------

##### Construct `boolean_operator`

###### Regex

```re
          ^(.*?)/_type='BoolOp'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/op/_type='(?P<SUFFIX>.+)'
```

###### Example

```python
1   a and b
2   a or c
3   not x # no match
```

###### Matches

```markdown
boolean_operator=And: 1
boolean_operator=Or: 2
```

**Remark.** `Not` is not a boolean operator in Python. To match it, use the [construct `unary_operator-Not`](#construct-unary_operator).

--------------------------------------------------------------------------------

##### Construct `comparison_operator`

###### Regex

```re
          ^(.*?)/_type='Compare'
\n(?:\1.+\n)*?\1/ops/0/_type='(?P<SUFFIX>.+)'
\n(?:\1.+\n)*?\1/comparators/0/lineno=(?P<LINE>\d+)
```

###### Example

```python
1   print(a == 3)
2   if a == b == c:
3       pass
4   needle in haystack
5   3 + 4
```

###### Matches

```markdown
comparison_operator=Eq: 1, 2
comparison_operator=In: 4
```

--------------------------------------------------------------------------------

##### Construct `divisibility_test`

###### Regex

```re
          ^(.*?)/_type='Compare'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/left/op/_type='Mod'
(   # try to match the % right operand with a number
\n(?:\1.+\n)*?\1/left/right/n=(?P<SUFFIX>.+)
)?
\n(?:\1.+\n)*?\1/ops/length=1
\n(?:\1.+\n)*?\1/ops/0/_type='(Eq|NotEq)'
```

###### Example

```python
1   a % b == 0
2   a % 2 == 0
3   a % 3 != 0
4   a % 4 == 1
5   a % 5 != 1
```

###### Matches

```markdown
divisibility_test: 1
divisibility_test=2: 2
divisibility_test=3: 3
divisibility_test=4: 4
divisibility_test=5: 5
```

--------------------------------------------------------------------------------

### Calls

--------------------------------------------------------------------------------

##### Construct `function_call`

###### Regex

```re
          ^(.*?)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/func/_type='Name'
\n(?:\1.+\n)*?\1/func/id='(?P<SUFFIX>.+)'
```

###### Example

```python
1   print(len("hello, world"))
2   print(foobar((42)))
```

###### Matches

```markdown
function_call=len: 1
function_call=print: 1, 2
function_call=foobar: 2
```

--------------------------------------------------------------------------------

##### Construct `method_call`

###### Regex

```re
          ^(.*?)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/func/_type='Attribute'
\n(?:\1.+\n)*?\1/func/attr='(?P<SUFFIX>.+)'
```

###### Example

```python
1   seq.index(42)
2   foo.bar(42)
```

###### Matches

```markdown
method_call=index: 1
method_call=bar: 2
```

--------------------------------------------------------------------------------

##### Construct `method_chaining`

###### Regex

```re
          ^(.*?)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/func/_type='Attribute'
\n(?:\1.+\n)*?\1/func/value/_type='Call'
\n(?:\1.+\n)*?\1/func/value/func/_type='Attribute'
```

###### Example

```python
1   s.strip().split()
```

###### Matches

```markdown
method_chaining: 1
```

--------------------------------------------------------------------------------

##### Construct `composition`

Apply a function or a method to an expression involving the result of another function or method application, without using an intermediate variable.

###### Regex

```re
          ^(.*?)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/args/.*/_type='Call'
```

###### Example

```python
1   print(len("hello, world"))
2   print("hello, world")
3   print(a + abs(b))
4.  print(s.upper())
```

###### Matches

```markdown
composition: 1, 3, 4
```

--------------------------------------------------------------------------------

### Anonymous functions

--------------------------------------------------------------------------------

##### Construct `lambda_function`

###### Regex

```re
          ^(.*?)/_type='Lambda'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

###### Example

```python
1   lambda x: x + 1
```

###### Matches

```markdown
lambda_function: 1
```

--------------------------------------------------------------------------------

## Statements

### Assignments

--------------------------------------------------------------------------------

##### Construct `global_constant_definition`

###### Regex

```re
 ^(/body/\d+)/_type='Assign' # no indentation
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/.+/id='[A-Z0-9_]+' # all caps
```

###### Example

```python
1   PATH = "foo/bar"
2   (a, B) = (0, 1)
3   (A, B) = (0, 1)
4   if condition:
5       PATH = "foo/bar" # BUG: no match
```

###### Matches

```markdown
global_constant_definition: 1, 2, 3
```

--------------------------------------------------------------------------------

##### Construct `global_variable_definition`

###### Regex

```re
  ^(/body/\d+)/_type='Assign' # no indentation
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/.+/id='.*?[a-z] # at least one lowercase letter
```

###### Example

```python
1   PATH = "foo/bar"
2   (a, B) = (0, 1)
3   (a, b) = (0, 1)
4   if condition:
5       path = "foo/bar" # BUG: no match
6   path = "foo/bar"
7   MyPath = "foo/bar"
```

###### Matches

```markdown
global_variable_definition: 2, 3, 6, 7
```

--------------------------------------------------------------------------------

##### Construct `assignment`

###### Regex

```re
          ^(.*?)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

###### Example

```python
1   a = 42
2   (a, b) = (1, 2)
3   a[0] = b[0]
```

###### Matches

```markdown
assignment: 1, 2, 3
```

--------------------------------------------------------------------------------

##### Construct `augmented_assignment`

###### Regex

```re
          ^(.*?)/_type='AugAssign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

###### Example

```python
1   a += 1
2   a = a + 1
```

###### Matches

```markdown
augmented_assignment: 1
```

--------------------------------------------------------------------------------

##### Construct `chained_assignment`

###### Regex

```re
          ^(.*?)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/length=(?!1\n).+
```

###### Example

```python
1   a = 42
2   a = b = 42
3   a = b = c = 42
```

###### Matches

```markdown
chained_assignment: 2, 3
```

--------------------------------------------------------------------------------

##### Construct `swapping`

Swap two variables or two elements of an array with a 2-element tuple or list.

###### Regex

```re
          ^(.*?)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/0/elts/length=2
\n(?:\1.+\n)*?\1/targets/0/elts/0/_hash=(?P<HASH_A>.+)
\n(?:\1.+\n)*?\1/targets/0/elts/1/_hash=(?P<HASH_B>.+)
\n(?:\1.+\n)*?\1/value/elts/length=2
\n(?:\1.+\n)*?\1/value/elts/0/_hash=(?P=HASH_B)
\n(?:\1.+\n)*?\1/value/elts/1/_hash=(?P=HASH_A)
```

###### Example

```python
1   (a, b) = (b, a)
2   [a, b] = [b, a]
3   (a[0], a[1]) = (a[1], a[0])
4   (a[i], a[i + 1]) = (a[i + 1], a[i])
```

###### Matches

```markdown
swapping: 1, 2, 3, 4
```

--------------------------------------------------------------------------------

##### Construct `negation`

Update a variable by negating it.

###### Regex

```re
          ^(.*?)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/0/_hash=(?P<HASH>.+) # capture hash
\n(?:\1.+\n)*?\1/value/_type='UnaryOp'
\n(?:\1.+\n)*?\1/value/op/_type='USub'
\n(?:\1.+\n)*?\1/value/operand/_hash=(?P=HASH) # match hash
```

###### Example

```python
1   a = -a
2   numbers[i] = -numbers[i]
3   a -= 2 * a # LIMITATION
4   a = -1 * a # LIMITATION
5   a = -abs(a) # no match
```

###### Matches

```markdown
negation: 1, 2
```

--------------------------------------------------------------------------------

### Function definitions

--------------------------------------------------------------------------------

##### Construct `function_definition`

###### Regex

```re
          ^(.*?)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

###### Example

```python
1   def foo(bar):
2       pass
```

###### Matches

```markdown
function_definition: 1
```

--------------------------------------------------------------------------------

##### Construct `recursive_function_definition`

###### Regex

```re
          ^(.*?)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name=(?P<NAME>.+) # capture the name of the function
\n(?:\1.+\n)* \1/body/(?P<_1>.*)/_type='Call'
\n(?:\1.+\n)*?\1/body/(?P=_1)   /func/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/body/(?P=_1)   /func/id=(?P=NAME) # ensure it is called inside its own body
```

###### Example

```python
1   def gob_program():
2       print("PENUS")
3       gob_program()
```

###### Matches

```markdown
recursive_function_definition: 1-3
```

--------------------------------------------------------------------------------

##### Construct `deeply_recursive_function_definition`

Any function `f` which contains a nested call to itself (`f(..., f(...), ...)`), e.g. the [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function).

###### Regex

```re
          ^(.*?)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name=(?P<NAME>.+) # capture the name of the function
\n(?:\1.+\n)* \1/body/(?P<_1>.*)/_type='Call'
\n(?:\1.+\n)*?\1/body/(?P=_1)   /func/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/body/(?P=_1)   /func/id=(?P=NAME) # ensure it is called inside its own body
\n(?:\1.+\n)* \1/body/(?P=_1)   /(?P<_2>args/.*)/_type='Call'
\n(?:\1.+\n)*?\1/body/(?P=_1)   /(?P=_2)        /func/id=(?P=NAME)
```

###### Example

```python
1   def gob_program():
2       print("PENUS")
3       gob_program(gob_program())
```

###### Matches

```markdown
deeply_recursive_function_definition: 1-3
```

--------------------------------------------------------------------------------

##### Construct `generator_definition`

###### Regex

```re
          ^(.*?)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/body/\d+/value/_type='(?P<SUFFIX>Yield(From)?)'
```

###### Example

```python
1   def foo():
2       yield bar
3
4   def energy():
5       yield from waste
```

###### Matches

```markdown
generator_definition=Yield: 1
generator_definition=YieldFrom: 4
```

--------------------------------------------------------------------------------

### Conditionals

--------------------------------------------------------------------------------

##### Construct `if`

###### Regex

```re
          ^(.*?)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/.*
```

###### Example

```python
1   if condition_1:
2       if condition_2:
3           pass
4   else:
5       pass
```

###### Matches

```markdown
if: 1, 2
```

--------------------------------------------------------------------------------

##### Construct `if_else`

`if` statement with `else`.

###### Regex

```re
          ^(.*?)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/0/_type=(?!'If')
```

###### Example

```python
1   if condition_1:
2       if condition_2:
3           pass
4   else:
5       pass
6   if condition_2:
7       pass
8   elif condition_3:
9       pass
```

###### Matches

```markdown
if_else: 1
```

--------------------------------------------------------------------------------

##### Construct `if_elif`

`if` statement with `elif`.

###### Regex

```re
          ^(.*?)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/0/_type='If'
```

###### Example

```python
1   if condition_1:
2       pass
3   elif condition_2:
4       pass
5   
6   if condition_3:
7       pass
8   elif condition_4:
9       pass
10  else:
11      pass
```

###### Matches

```markdown
if_elif: 1, 6
```

--------------------------------------------------------------------------------

### Iterations

--------------------------------------------------------------------------------

##### Construct `for_each`
Iterate over the elements of a (named) collection.

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/iter/_type='Name'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
```

###### Example

```python
1   for x in seq_1:
2       for y in range(len(seq_3)): # no match
3           pass
4       for i in seq_2:
5           pass
```

###### Matches

```markdown
for_each: 1, 4
```

--------------------------------------------------------------------------------

##### Construct `for_range_stop`

Iterate over a range with exactly 1 argument (stop).

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=1
```

###### Example

```python
1   for i in range(stop):
2       pass
3   for i in range(start, stop):
4       pass
5   for i in range(start, stop, step):
6       pass
7   for i in range(start, stop, -1):
8       pass
```

###### Matches

```markdown
for_range_stop: 1
```

--------------------------------------------------------------------------------

##### Construct `for_range_start`

Iterate over a range with exactly 2 arguments (start, stop).

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=2
```

###### Example

```python
1   for i in range(stop):
2       pass
3   for i in range(start, stop):
4       pass
5   for i in range(start, stop, step):
6       pass
7   for i in range(start, stop, -1):
8       pass
```

###### Matches

```markdown
for_range_start: 3
```

--------------------------------------------------------------------------------

##### Construct `for_range_step`

Iterate over a range with 3 arguments (start, stop, step).

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=3
(   # If the step is a number, capture it as a suffix
\n(?:\1.+\n)*?\1/iter/args/2/_type='Num'
\n(?:\1.+\n)*?\1/iter/args/2/n=(?<SUFFIX>.+)
)?
```

###### Example

```python
1   for i in range(stop):
2       pass
3   for i in range(start, stop):
4       pass
5   for i in range(start, stop, step):
6       pass
7   for i in range(start, stop, -1):
8       pass
9   for i in range(start, stop, 2):
10      pass
```

###### Matches

```markdown
for_range_step: 5
for_range_step=-1: 7
for_range_step=2: 9
```

--------------------------------------------------------------------------------

##### Construct `for_indexes_values`

Iterate over index numbers and elements of a collection.

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/func/id='enumerate'
```

###### Example

```python
1   for (i, element) in enumerate(elements):
2       pass
```

###### Matches

```markdown
for_indexes_values: 1
```

--------------------------------------------------------------------------------

##### Construct `for_indexes`

Iterate over index numbers of a collection.

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P<_1>iter)/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)     /func/id='range'
\n(?:\1.+\n)*?\1/(?P=_1)     /args/length=1
\n(?:\1.+\n)*?\1/(?P=_1)     /args/0/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)     /args/0/func/id='len'
\n(?:\1.+\n)*?\1/(?P=_1)     /keywords/length=0
```

###### Example

```python
1   for i in range(len(elements)):
2       pass
```

###### Matches

```markdown
for_indexes: 1
```

--------------------------------------------------------------------------------

##### Construct `nested_for`

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P<_1>body/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)         /lineno=(?P<LINE>\d+)
```

###### Example

```python
1   for x_1 in seq_1:
2       for x_2 in seq_2:
3           pass
```

###### Matches

```markdown
nested_for: 1-2
```

--------------------------------------------------------------------------------

##### Construct `triangular_nested_for`

A `for` loop with a counter `i` and a nested `for` loop which makes `i` iterations.

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/target/id=(?P<VAR>.+) # capture iteration variable
\n(?:\1.+\n)*?\1/iter/_type='Call'
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=1 # only range(arg1)
(   # i goes from 0 to n, and j from 0 to i
\n(?:\1.+\n)* \1/(?P<_1>body/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)         /iter/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)         /iter/func/id='range'
\n(?:\1.+\n)*?\1/(?P=_1)         /iter/args/length=1 # only range(arg1)
\n(?:\1.+\n)* \1/(?P=_1)         /iter/args/0.*/id=(?P=VAR) # match iteration variable
|   # i goes from 0 to n, and j from i to n
\n(?:\1.+\n)*?\1/iter/args/0/_hash=(?P<STOP>.+) # capture stop expression
\n(?:\1.+\n)* \1/(?P<_1>body/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)         /iter/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)         /iter/func/id='range'
\n(?:\1.+\n)*?\1/(?P=_1)         /iter/args/length=2 # only range(arg1, arg2)
\n(?:\1.+\n)* \1/(?P=_1)         /iter/args/0(/.+)*/id=(?P=VAR) # match iteration variable
\n(?:\1.+\n)* \1/(?P=_1)         /iter/args/1(/.+)*/_hash=(?P=STOP) # match stop expression
)
```

###### Example

```python
1   for i in range(n):
2       for j in range(i - 1):
3           pass
4   
5   for i in range(n):
6       for j in range(i+1, n):
7           pass
```

###### Matches

```markdown
triangular_nested_for: 1-2, 5-6
```

--------------------------------------------------------------------------------

## Code patterns

### Iterative patterns

#### Sequential loops

--------------------------------------------------------------------------------

##### Construct `accumulate_elements`

An accumulation pattern where a variable (the acumulator) is updated from its previous value and the value of the iteration variable.

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/target/_type='Name'
\n(?:\1.+\n)*?\1/target/id=(?P<ITER_VAR>.+)
(   # the accumulator either appears on both sides of a simple assignment with the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>(body/\d+/?)*)/_type='(?P<SUFFIX>Assign)'
\n(?:\1.+\n)*?\1/(?P=_1)              /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)              /targets/.*/id=(?P<ACC>.+) # capture the name of the accumulator
\n(?:\1.+\n)*?\1/(?P=_1)              /value/_ids=(?=.*?(?P=ACC))(?=.*?(?P=ITER_VAR)) # both appear in RHS
|   # or should be on LHS of an augmented assignement with the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>(body/\d+/?)*)/_type='(?P<SUFFIX>AugAssign)'
\n(?:\1.+\n)*?\1/(?P=_1)              /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)              /value.*/id=(?P=ITER_VAR)
|   # or should be mutated by calling a function on this accumulator and the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>(body/\d+/?)*)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_1)              /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)              /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)              /value/func/_type='(?P<SUFFIX>Name)'
\n(?:\1.+\n)*?\1/(?P=_1)              /value/func/id='(?!breakpoint|delattr|eval|exec|help|input|open|print|setattr|super).+'
\n(?:\1.+\n)*?\1/(?P=_1)              /value/args/length=(?![01]\n)\d+ # the function has several arguments
\n(?:\1.+\n)* \1/(?P=_1)              /value/args/\d+/id=(?P=ITER_VAR) # which include the iteration variable
|   # or should be mutated by calling a method of this accumulator, again on the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>(body/\d+/?)*)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_1)              /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)              /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)              /value/func/_type='(?P<SUFFIX>Attribute)'
\n(?:\1.+\n)* \1/(?P=_1)              /value/args/\d+/id=(?P=ITER_VAR) # the arguments include the iteration variable
)
```

###### Example

```python
1   def accumulate_elements(elements):
2       acc = seed
3       for element in elements:
4           acc = element + acc
5       return acc
6
7   for i in range(10):
8       acc = combine(acc, i)
9   for i in range(10):
10      if condition:
11           acc += i
12  for i in range(10):
13      acc += foo(bar, i)
14  for i in range(10):
15      foo(acc, bar, i)
16  for i in range(10):
17      acc.foo(bar, i)
18  for i in range(10): # no match (cf. remark)
19      print(foobar, i)
```

**Remark.**
The third alternative of the regex is experimental. It matches any one-line function call on the iteration variable and another argument, not only those which mutate one of their arguments (hopefully the accumulator). The built-in functions with side effects (such as `print()`) are explicitely excluded, but this may not be enough. The fourth alternative, too, is certainly broader than necessary. Handle with care.

###### Matches

```markdown
accumulate_elements=Assign: 3-4, 7-8
accumulate_elements=AugAssign: 9-11, 12-13
accumulate_elements=Name: 14-15
accumulate_elements=Attribute: 16-17
```

--------------------------------------------------------------------------------

##### Construct `filter_for`

An accumulation pattern that, from a given collection, returns a list containing only those elements that verify a certain condition.

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/target/id=(?P<ID_1>.+) # capture the iteration variable
\n(?:\1.+\n)*?\1/(?P<_1>body/\d+)/_type='If'
\n(?:\1.+\n)* \1/(?P=_1)         /test/args/\d+/id=(?P=ID_1) # match it in an inner conditional test
\n(?:\1.+\n)* \1/(?P=_1)         /(?P<_2>body/\d+)/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)         /(?P=_2)         /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)         /(?P=_2)         /value/func/attr='append'
\n(?:\1.+\n)*?\1/(?P=_1)         /(?P=_2)         /value/args/0/id=(?P=ID_1) # match it in an append()
```

###### Example

```python
1   for element in elements:
2       print("foo")
3       if predicate(element):
4           print("bar")
5           acc.append(element)
6       print("fiz")
```

###### Matches

```markdown
filter_for: 1-5
```

--------------------------------------------------------------------------------

##### Construct `find_best_element`

An accumulation pattern that, from a given collection, returns the best element verifying a certain condition.

###### Regex

```re
      ^(.*?)/(?P<_1>body/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_1)         /targets/0/id=(?P<CANDIDATE>.+) # capture candidate
\n(?:\1.+\n)*?\1/(?P<_2>body/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_2)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_2)         /target/id=(?P<ITER_VAR>.+) # capture iteration variable
\n(?:\1.+\n)* \1/(?P=_2)         /(?P<_3>body/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_2)         /(?P=_3)         /test/_ids=(?=.*?(?P=ITER_VAR))(?=.*?(?P=CANDIDATE)).* # match both
\n(?:\1.+\n)* \1/(?P=_2)         /(?P=_3)         /test/.*/id=(?P=CANDIDATE) # match candidate
\n(?:\1.+\n)* \1/(?P=_2)         /(?P=_3)         /(?P<_4>body/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_2)         /(?P=_3)         /(?P=_4)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_2)         /(?P=_3)         /(?P=_4)         /targets/0/id=(?P=CANDIDATE) # match candidate
\n(?:\1.+\n)*?\1/(?P=_2)         /(?P=_3)         /(?P=_4)         /value/id=(?P=ITER_VAR) # match iteration variable
```

###### Example

```python
1   def find_best_element(elements):
2       candidate = bad_value
3       for element in elements:
4           if is_better(element, candidate):
5               candidate = element
6       return candidate
7
8   def find_maximum_element(elements):
9       candidate = element[0]
10      for element in elements:
11          if candidate > element:
12              candidate = element
13      return candidate
```

###### Matches

```markdown
find_best_element: 3-5, 10-12
```

--------------------------------------------------------------------------------

##### Construct `universal_quantifier`

Check if all the elements of a collection satisfy a predicate.

###### Regex

```re
      ^(.*?)/(?P<_1>body/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)         /(?P<_2>body/\d+)/_type='If'
\n(?:\1.+\n)* \1/(?P=_1)         /(?P=_2)         /(?P<_3>body/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)         /(?P=_2)         /(?P=_3)         /value/value=False
\n(?:\1.+\n)* \1/(?P<_4_>body/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_4_)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_4_)         /value/value=True
```

###### Example

```python
1   def all_elements_satisfy(elements):
2       for element in elements:
3           if not is_good(element):
4               return False
5       return True
```

###### Matches

```markdown
universal_quantifier: 2-5
```

--------------------------------------------------------------------------------

##### Construct `existential_quantifier`

Check if any element of a collection satisfies a predicate.

###### Regex

```re
      ^(.*?)/(?P<_1>body/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)         /(?P<_2>body/\d+)/_type='If'
\n(?:\1.+\n)* \1/(?P=_1)         /(?P=_2)         /(?P<_3>body/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)         /(?P=_2)         /(?P=_3)         /value/value=True
\n(?:\1.+\n)* \1/(?P<_4>body/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_4)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_4)         /value/value=False
```

###### Example

```python
2   def some_elements_satisfy(elements):
1       for element in elements:
3           if is_good(element):
4               return True
5       return False
```

###### Matches

```markdown
existential_quantifier: 2-5
```

--------------------------------------------------------------------------------

##### Construct `find_first_element`

Linear search. Return the first element of a sequence satisfying a predicate.

###### Regex

```re
          ^(.*?)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/target/id=(?P<ITER_VAR>.+) # capture the name of the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>body/.+)/_type='If' # The If appears at any depth in the loop
\n(?:\1.+\n)* \1/(?P=_1)        /test/.+/id=(?P=ITER_VAR) # The variable appears at any depth inside the condition
\n(?:\1.+\n)*?\1/(?P=_1)        /(?P<_2>body/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)        /(?P=_2)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)        /(?P=_2)         /value/id=(?P=ITER_VAR) # ... and is returned
```

###### Example

```python
1   def search(seq, x):
2       for i in range(len(seq)):
3           if seq[i] == x:
4               return i
5       return None
```

###### Matches

```markdown
find_first_element: 2-4
```

--------------------------------------------------------------------------------

#### Non sequential finite loops

--------------------------------------------------------------------------------

##### Construct `evolve_state`

Evolve the value of a variable until it reaches a desired state.

###### Regex

```re
          ^(.*?)/_type='While'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/test/.*/id=(?P<STATE>'.+') # capture state variable
(   # the state variable either appears on both sides of a simple assignment
\n(?:\1.+\n)* \1/(?P<_1>body/.*)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_1)        /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)        /targets/0/id=(?P=STATE) # it is updated somewhere in the loop
\n(?:\1.+\n)*?\1/(?P=_1)        /value/_ids=.*(?P=STATE) # from its current value
|   # or appears on LHS of an augmented assignement
\n(?:\1.+\n)* \1/(?P<_1>body/.*)/_type='AugAssign'
\n(?:\1.+\n)*?\1/(?P=_1)        /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)        /target/id=(?P=STATE) # it is augmented somewhere in the loop
|   # or is mutated by calling a function or a method of this variable
\n(?:\1.+\n)* \1/(?P<_1>body/.*)/_type='Expr'
\n(?:\1.+\n)*?\1/(?P=_1)        /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)        /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)        /value/.*/id=(?P=STATE) # it is mutated somewhere in the loop
)
```

###### Example

```python
1   def square_digit_attractor(n):
2       while n != 1 and n != 89:
3           n = square_digit_sum(n)
4       return n
5
6   while predicate(x):
7       x += foo(bar)
8   while predicate(x):
9       x.foo(bar)
10  while predicate(x):
11      foo(x, bar)
```

###### Matches

```markdown
evolve_state: 2-3, 6-7, 8-9, 10-11
```

--------------------------------------------------------------------------------

#### Non sequential infinite loops

--------------------------------------------------------------------------------

##### Construct `accumulate_stream`

Accumulate the inputs until a sentinel value is encountered (accumulation expressed by: `acc = combine(x, acc)`).

###### Regex

```re
          ^(.*?)/_type='While'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/test/value=True
\n(?:\1.+\n)* \1/body/\d+/targets/.+/id=(?P<INPUT>.+) # capture the name of the input
\n(?:\1.+\n)* \1/(?P<_1>body/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_1)         /test/_ids=.*?(?P=INPUT).* # the input is tested
\n(?:\1.+\n)* \1/(?P=_1)         /(?P<_2>body/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)         /(?P=_2)         /value/id=(?P<ACC>.+) # capture the name of the accumulator
(   # the accumulator either appears on both sides of a simple assignment with the input
\n(?:\1.+\n)* \1/(?P<_3>body/\d+)/_type='(?P<SUFFIX>Assign)'
\n(?:\1.+\n)*?\1/(?P=_3)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_3)         /targets/.*/id=(?P=ACC)
\n(?:\1.+\n)*?\1/(?P=_3)         /value/_ids=(?=.*(?P=INPUT))(?=.*(?P=ACC)) # both appear in RHS
|   # or is on LHS of an augmented assignement with the input
\n(?:\1.+\n)* \1/(?P<_3>body/\d+)/_type='(?P<SUFFIX>AugAssign)'
\n(?:\1.+\n)*?\1/(?P=_3)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_3)         /target/id=(?P=ACC)
\n(?:\1.+\n)* \1/(?P=_3)         /value.*/id=(?P=INPUT)
|   # or should be mutated by calling a function on this accumulator and the iteration variable
\n(?:\1.+\n)* \1/(?P<_3>body/\d+)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_3)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_3)         /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_3)         /value/_ids=(?=.*(?P=INPUT))(?=.*(?P=ACC)).+ # both appear in RHS
\n(?:\1.+\n)*?\1/(?P=_3)         /value/func/_type='(?P<SUFFIX>Name)'
\n(?:\1.+\n)*?\1/(?P=_3)         /value/func/id='(?!(?P=ACC)|(?P=INPUT)|breakpoint|delattr|eval|exec|help|input|open|print|setattr|super).+'
|   # or should be mutated by calling a method of this accumulator, again on the iteration variable
\n(?:\1.+\n)* \1/(?P<_3>body/\d+)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_3)         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_3)         /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_3)         /value/func/_type='(?P<SUFFIX>Attribute)'
\n(?:\1.+\n)*?\1/(?P=_3)         /value/func/value/id=(?P=ACC) # a method of acc is called on...
\n(?:\1.+\n)* \1/(?P=_3)         /value/args/\d+/id=(?P=INPUT) # the iteration variable
)
```

###### Example

```python
1   def accumulate_inputs():
2       acc = neutral
3       while True:
4           x = read()
5           if is_sentinel(x, y):
6               return acc
7           acc = combine(x, acc)
8
9   def accumulate_inputs():
10      acc = neutral
11      while True:
12          x = read()
13          if x > y:
14              return acc
15          acc += abs(x)
16
17  def accumulate_inputs():
18      acc = neutral
19      while True:
20          x = read()
21          if x > y:
22              return acc
23          foobar(acc, x)
24
25  def accumulate_inputs():
26      acc = neutral
27      while True:
28          x = read()
29          if x > y:
30              return acc
31          acc.foobar(x)
```

###### Matches

```markdown
accumulate_stream=Assign: 3-7
accumulate_stream=AugAssign: 11-15
accumulate_stream=Name: 19-23
accumulate_stream=Attribute: 27-31
```

--------------------------------------------------------------------------------

## Suggestions

These patterns match constructs that can be shortened.
It's up to you to decide if a rewriting would make the code clearer.

### Assignments

--------------------------------------------------------------------------------

##### Construct `suggest_conditional_expression`

When a conditional simply assigns different values to the same variable, it may be rewritten as a conditional expression.

###### Regex

```re
          ^(.*?)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/body/length=1
\n(?:\1.+\n)*?\1/body/0/_type='Assign'
\n(?:\1.+\n)*?\1/body/0/targets/0/_hash=(?P<HASH>.+)
\n(?:\1.+\n)*?\1/orelse/length=1
\n(?:\1.+\n)*?\1/orelse/0/_type='Assign'
\n(?:\1.+\n)*?\1/orelse/0/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/0/targets/0/_hash=(?P=HASH)
```

###### Example

```python
1   if condition:
2       a = 1
3   else:
4       a = 2
5
6   if condition:
7       a = 1
8       b = 0
9   else:
10      a = 2
11
12  if condition:
13      a = 1
14  else:
15      b = 0
16      a = 2
```

The first conditional (only) may be rewritten as:

```python
1   a = (1 if condition else 2)
```

###### Matches

```markdown
suggest_conditional_expression: 1-4
```

--------------------------------------------------------------------------------

##### Construct `suggest_augmented_assignment`

When the RHS of an assignment consists in a binary operation whose left operand is the target (`a = a op expr`), the statement can be shortened as `a op= expr`.

###### Regex

```re
          ^(.*?)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/length=1
\n(?:\1.+\n)*?\1/targets/0/id=(?P<TARGET>.+)
\n(?:\1.+\n)*?\1/value/_type='BinOp'
\n(?:\1.+\n)*?\1/value/left/id=(?P=TARGET)
```

###### Example

```python
1   a = a + b
2   a = a + (b + c)
3   a = b + a
4   a = a + b + c # FIXME
```

May be rewritten as:

```python
1   a += b
2   a += b + c
```

- Line 3, note that the `+` binary operator is not necessarily commutative, e.g. on strings.
- Some cases like line 4 should be matched, check the associativity rules.

###### Matches

```markdown
suggest_augmented_assignment: 1, 2
```

--------------------------------------------------------------------------------

### Expressions

--------------------------------------------------------------------------------

##### Construct `suggest_comparison_chaining`

When the `else` branch of a conditional is another conditional, it can be rewritten with an `elif` branch.

###### Regex

```re
          ^(.*?)/_type='BoolOp'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/op/_type='And'
\n(?:\1.+\n)*?\1/values/0/_type='Compare'
\n(?:\1.+\n)*?\1/values/0/comparators/0/_hash=(?P<HASH_1>.+) # capture the right operand of the left comparison
\n(?:\1.+\n)*?\1/values/1/_type='Compare'
\n(?:\1.+\n)*?\1/values/1/left/_hash=(?P=HASH_1) # match the left operand of the right comparison
```

###### Example

```python
1   a < b and b < c
2   a <= b and b < c
3   a == b and b == c
4   a != b and b != c
```

May be rewritten as:

```python
1   a < b < c
2   a <= b < c
3   a == b == c
4   a != b != c
```

Note that the last simplification is rather confusing and should be avoided.

###### Matches

```markdown
suggest_comparison_chaining: 1, 2, 3, 4
```

--------------------------------------------------------------------------------

##### Construct `suggest_constant_definition`

Match magic numbers (unnamed numerical constants) other than -1, 0, 1 and 2. A number in the RHS of an assignment to a constant is of course ignored.

###### Regex

```re
  ^(/body/\d+)
(   # indented lines
              /(?P<_1>body/\d+.*)/lineno=(?P<LINE>\d+)
\n          \1/(?P=_1)           /n=(?!(-1|0|1|2)\n)
|   # non indented lines
              /_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/0/id='.*?[a-z].*' # at least one lowercase letter
\n(?:\1.+\n)*?\1/value/n=(?!(-1|0|1|2)\n)
)
```

###### Example

```python
1   NUMBER_OF_TEETH_OF_A_DOG = 42 # not a magic number
2   shoe_size = 42 # magic number
3   for a in s[::-1]:
4       if a == 42 and b % 2 == 0: # 42 is a magic number
5           pass
6   negative_number = -42
```

May be rewritten as:

```python
1   NUMBER_OF_TEETH_OF_A_DOG = 42
2   ANSWER_TO_THE_ULTIMATE_QUESTION_OF_LIFE_THE_UNIVERSE_AND_EVERYTHING = 42
3   shoe_size = ANSWER_TO_THE_ULTIMATE_QUESTION_OF_LIFE_THE_UNIVERSE_AND_EVERYTHING
4   for a in s[::-1]:
5       if a == ANSWER_TO_THE_ULTIMATE_QUESTION_OF_LIFE_THE_UNIVERSE_AND_EVERYTHING and b % 2 == 0:
6           pass
7   NEGATIVE_NUMBER = -42
```

###### Matches

```markdown
suggest_constant_definition: 2, 4, 6
```

--------------------------------------------------------------------------------

### Subroutines

--------------------------------------------------------------------------------

##### Construct `suggest_condition_return`

When a predicate ends with a conditional whose sole purpose is to return `True` or `False`, it is enough to return the condition.

###### Regex

```re
          ^(.*?)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/body/0/_type='Return'
\n(?:\1.+\n)*?\1/body/0/value/value=(?P<BOOL>True|False) # name BOOL the value used here
\n(?:\1.+\n)*?\1/orelse/0/_type='Return'
\n(?:\1.+\n)*?\1/orelse/0/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/0/value/value=(True|False)(?<!(?P=BOOL)) # and check not BOOL is used there
```

###### Example

```python
1   def foo():
2       if condition:
3           return True
4       else:
5           return False
6
7   def bar():
8       if condition:
9           return False
10      else:
11          return True
```

May be rewritten as:

```python
1   def foo():
2       return condition
3
4   def bar():
5       return not condition
```

###### Matches

```markdown
suggest_condition_return: 2-5, 8-11
```
