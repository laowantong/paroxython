- [Introduction](#introduction)
- [Specifications](#specifications)
  - [Expressions](#expressions)
    - [Construct `builtin_function_call`](#construct-builtin_function_call)
    - [Construct `binary_operator`](#construct-binary_operator)
    - [Construct `unary_operator`](#construct-unary_operator)
    - [Construct `function_composition`](#construct-function_composition)
  - [Statements](#statements)
    - [Assignments](#assignments)
      - [Construct `global_constant_definition`](#construct-global_constant_definition)
      - [Construct `global_variable_definition`](#construct-global_variable_definition)
      - [Construct `assignment`](#construct-assignment)
      - [Construct `augmented_assignment`](#construct-augmented_assignment)
      - [Construct `swapping`](#construct-swapping)
      - [Construct `negation`](#construct-negation)
    - [Function definitions](#function-definitions)
      - [Construct `function_definition`](#construct-function_definition)
      - [Construct `recursive_function_definition`](#construct-recursive_function_definition)
      - [Construct `deeply_recursive_function_definition`](#construct-deeply_recursive_function_definition)
    - [Conditionals](#conditionals)
      - [Construct `if`](#construct-if)
      - [Construct `if_else`](#construct-if_else)
      - [Construct `if_elif`](#construct-if_elif)
    - [Iterations](#iterations)
      - [Construct `for_each`](#construct-for_each)
      - [Construct `for_range_stop`](#construct-for_range_stop)
      - [Construct `for_range_start`](#construct-for_range_start)
      - [Construct `for_range_step`](#construct-for_range_step)
      - [Construct `for_range_backwards`](#construct-for_range_backwards)
      - [Construct `for_index_values`](#construct-for_index_values)
  - [Code patterns](#code-patterns)
    - [Iterative patterns](#iterative-patterns)
      - [Sequential loops](#sequential-loops)
        - [Construct `accumulate_for_1`](#construct-accumulate_for_1)
        - [Construct `accumulate_for_2`](#construct-accumulate_for_2)
        - [Construct `universal_quantifier`](#construct-universal_quantifier)
        - [Construct `existential_quantifier`](#construct-existential_quantifier)
        - [Construct `find_first_element`](#construct-find_first_element)
      - [Non sequential loops](#non-sequential-loops)
        - [Construct `accumulate_until_1`](#construct-accumulate_until_1)
        - [Construct `accumulate_until_2`](#construct-accumulate_until_2)
  - [Suggestions](#suggestions)
    - [Assignments](#assignments-1)
      - [Construct `suggest_conditional_expression`](#construct-suggest_conditional_expression)
      - [Construct `suggest_augmented_assignment`](#construct-suggest_augmented_assignment)
    - [Conditionals](#conditionals-1)
      - [Construct `suggest_elif`](#construct-suggest_elif)
    - [Subroutines](#subroutines)
      - [Construct `suggest_condition_return`](#construct-suggest_condition_return)

# Introduction

# Specifications

## Expressions

--------------------------------------------------------------------------------

##### Construct `builtin_function_call`

###### Regex

```re
        ^(.*)/_type='Call'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/func/id='(?P<SUFFIX>.+)(?<=abs|delattr|hash|memoryview|set|all|dict|help|min|setattr|any|dir|hex|next|slice|ascii|divmod|id|object|sorted|bin|enumerate|input|oct|staticmethod|bool|eval|int|open|str|breakpoint|exec|isinstance|ord|sum|bytearray|filter|issubclass|pow|super|bytes|float|iter|print|tuple|callable|format|len|property|type|chr|frozenset|list|range|vars|classmethod|getattr|locals|repr|zip|compile|globals|map|reversed|__import__|complex|hasattr|max|round)'
```

###### Example

```python
1   print(len("hello, world"))
2   print(foobar((42)))
```

###### Matches

```markdown
builtin_function_call-len: 1
builtin_function_call-print: 1, 2
```

--------------------------------------------------------------------------------

##### Construct `binary_operator`

###### Regex

```re
        ^(.*)/_type='BinOp'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/op/_type='(?P<SUFFIX>.+)(?<=Add|Sub|Mult|MatMult|Div|Mod|Pow|LShift|RShift|BitOr|BitXor|BitAnd|FloorDiv)'
```

###### Example

```python
1   2**32768 - 1
```

###### Matches

```markdown
binary_operator-Pow: 1
binary_operator-Sub: 1
```

--------------------------------------------------------------------------------

##### Construct `unary_operator`

###### Regex

```re
        ^(.*)/_type='UnaryOp'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/op/_type='(?P<SUFFIX>.+)(?<=Invert|Not|UAdd|USub)'
```

###### Example

```python
1   a = -1
2   b = not c
```

###### Matches

```markdown
unary_operator-USub: 1
unary_operator-Not: 2
```

--------------------------------------------------------------------------------

##### Construct `function_composition`

Apply a function to an expression involving the result of another function application, without using an intermediate variable.

###### Regex

```re
        ^(.*)/_type='Call'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/args/.*/_type='Call'
```

###### Example

```python
1   print(len("hello, world"))
2   print("hello, world")
3   print(a + abs(b))
```

###### Matches

```markdown
function_composition: 1, 3
```

--------------------------------------------------------------------------------

## Statements

### Assignments

--------------------------------------------------------------------------------

##### Construct `global_constant_definition`

###### Regex

```re
 ^(/body/\d+)/_type='Assign' # no indentation
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/targets/.+/id='[A-Z0-9_]+' # all caps
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
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/targets/.+/id='.*?[a-z] # at least one lowercase letter
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
        ^(.*)/_type='Assign'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
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
        ^(.*)/_type='AugAssign'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
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

##### Construct `swapping`

Swap two variables or two elements of an array with a 2-element tuple or list.

###### Regex

```re
        ^(.*)/_type='Assign'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/targets/0/elts/length=2
\n(?:.+\n)*\1/targets/0/elts/0/hash=(?P<HASH_A>.+)
\n(?:.+\n)*\1/targets/0/elts/1/hash=(?P<HASH_B>.+)
\n(?:.+\n)*\1/value/elts/length=2
\n(?:.+\n)*\1/value/elts/0/hash=(?P=HASH_B)
\n(?:.+\n)*\1/value/elts/1/hash=(?P=HASH_A)
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
        ^(.*)/_type='Assign'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/targets/0/hash=(?P<HASH>.+)
\n(?:.+\n)*\1/value/_type='UnaryOp'
\n(?:.+\n)*\1/value/op/_type='USub'
\n(?:.+\n)*\1/value/operand/hash=(?P=HASH)
```

###### Example

```python
1   a = -a
2   numbers[i] = -numbers[i]
3   a -= 2 * a # LIMITATION
4   a = -1 * a # LIMITATION
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
        ^(.*)/_type='FunctionDef'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
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
        ^(.*)/_type='FunctionDef'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/name=(?P<NAME>.+) # capture the name of the function
\n(?:.+\n)*\1/body/(?P<_1>.*)/_type='Call'
\n(?:.+\n)*\1/body/(?P=_1)   /func/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/body/(?P=_1)   /func/id=(?P=NAME) # ensure it is called inside its own body
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
        ^(.*)/_type='FunctionDef'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/name=(?P<NAME>.+) # capture the name of the function
\n(?:.+\n)*\1/body/(?P<_1>.*)/_type='Call'
\n(?:.+\n)*\1/body/(?P=_1)   /func/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/body/(?P=_1)   /func/id=(?P=NAME) # ensure it is called inside its own body
\n(?:.+\n)*\1/body/(?P=_1)   /(?P<_2>args/.*)/_type='Call'
\n(?:.+\n)*\1/body/(?P=_1)   /(?P=_2)        /func/id=(?P=NAME)
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

### Conditionals

--------------------------------------------------------------------------------

##### Construct `if`

###### Regex

```re
        ^(.*)/_type='If'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/orelse/.*
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
        ^(.*)/_type='If'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/orelse/0/_type=.*
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
if_else: 1
```

--------------------------------------------------------------------------------

##### Construct `if_elif`

`if` statement with `elif`.

###### Regex

```re
        ^(.*)/_type='If'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/orelse/0/_type='If'
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
        ^(.*)/_type='For'
\n(?:.+\n)*\1/iter/_type='Name'
\n(?:.+\n)*\1/iter/lineno=(?P<LINE>\d+)
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
        ^(.*)/_type='For'
\n(?:.+\n)*\1/iter/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/iter/func/id='range'
\n(?:.+\n)*\1/iter/args/length=1
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
        ^(.*)/_type='For'
\n(?:.+\n)*\1/iter/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/iter/func/id='range'
\n(?:.+\n)*\1/iter/args/length=2
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
        ^(.*)/_type='For'
\n(?:.+\n)*\1/iter/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/iter/func/id='range'
\n(?:.+\n)*\1/iter/args/length=3
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
for_range_step: 5, 7
```

--------------------------------------------------------------------------------

##### Construct `for_range_backwards`

Iterate over a range with a negative step.

###### Regex

```re
        ^(.*)/_type='For'
\n(?:.+\n)*\1/iter/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/iter/func/id='range'
\n(?:.+\n)*\1/iter/args/length=3
\n(?:.+\n)*\1/iter/args/2/op/_type='USub'
```

###### Example

```python
1   for i in range(stop):
2       pass
3   for i in range(start, stop):
4       pass
5   step = -1
6   for i in range(start, stop, step): # LIMITATION: the step must be a negative literal
7       pass
8   for i in range(start, stop, -1):
9       pass
```

###### Matches

```markdown
for_range_backwards: 8
```

--------------------------------------------------------------------------------

##### Construct `for_index_values`

Iterate over index numbers and elements of a collection.

###### Regex

```re
        ^(.*)/_type='For'
\n(?:.+\n)*\1/iter/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/iter/func/id='enumerate'
```

###### Example

```python
1   for (i, element) in enumerate(elements):
2       pass
```

###### Matches

```markdown
for_index_values: 1
```

--------------------------------------------------------------------------------

## Code patterns

### Iterative patterns

#### Sequential loops

--------------------------------------------------------------------------------

##### Construct `accumulate_for_1`

An accumulation pattern where an augmented assignment is used to update the accumulator.

###### Regex

```re
        ^(.*)/_type='For'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/target/_type='Name'
\n(?:.+\n)*\1/target/id=(?P<ITER_VAR>.+)
\n(?:.+\n)*\1/(?P<_1>body/\d+)/_type='AugAssign'
\n(?:.+\n)*\1/(?P=_1)         /(?P<_2>value.*)/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/(?P=_1)         /(?P=_2)        /id=(?P=ITER_VAR)
```

###### Example

```python
1   def accumulate_elements(elements):
2       acc = seed
3       for element in elements:
4           acc += element
5       return acc
6   for i in range(10):
7       acc += i
```

###### Matches

```markdown
accumulate_for_1: 3-4, 6-7
```

--------------------------------------------------------------------------------

##### Construct `accumulate_for_2`

An accumulation pattern with an assignment whose RHS contains both the accumulator and the iteration variable.

###### Regex

```re
        ^(.*)/_type='For'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/target/_type='Name'
\n(?:.+\n)*\1/target/id=(?P<ITER_VAR>.+) # capture the name of the iteration variable
\n(?:.+\n)*\1/(?P<_1>body/\d+)/_type='Assign'
\n(?:.+\n)*\1/(?P=_1)         /lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/(?P=_1)         /targets/.*/id=(?P<ACC>.+) # capture the name of the accumulator
\n(?:.+\n)*\1/(?P=_1)         /value/.*/id=(?P<VAR>((?P=ITER_VAR)|(?P=ACC))) # name VAR the variable used here
\n(?:.+\n)*\1/(?P=_1)         /value/.*/id=((?P=ITER_VAR)|(?P=ACC))(?<!(?P=VAR)) # and check the other one is used there
```

###### Example

```python
1   def accumulate_elements(elements):
2       acc = seed
3       for element in elements:
4           acc = combine(element, acc)
5       return acc
6   for i in range(10):
7       acc = combine(i, acc)
```

###### Matches

```markdown
accumulate_for_2: 3-4, 6-7
```

--------------------------------------------------------------------------------

##### Construct `universal_quantifier`

Check if all the elements of a collection satisfy a predicate.

###### Regex

```re
        ^(.*)/(?P<_1>body/\d+)/_type='For'
\n(?:.+\n)*\1/(?P=_1)         /lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/(?P=_1)         /(?P<_2>body/\d+)/_type='If'
\n(?:.+\n)*\1/(?P=_1)         /(?P=_2)         /(?P<_3>body/\d+)/_type='Return'
\n(?:.+\n)*\1/(?P=_1)         /(?P=_2)         /(?P=_3)/value/value=False
\n(?:.+\n)*\1/(?P<_4_>body/\d+)/_type='Return'
\n(?:.+\n)*\1/(?P=_4_)         /lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/(?P=_4_)         /value/value=True
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
        ^(.*)/(?P<_1>body/\d+)/_type='For'
\n(?:.+\n)*\1/(?P=_1)         /lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/(?P=_1)         /(?P<_2>body/\d+)/_type='If'
\n(?:.+\n)*\1/(?P=_1)         /(?P=_2)         /(?P<_3>body/\d+)/_type='Return'
\n(?:.+\n)*\1/(?P=_1)         /(?P=_2)         /(?P=_3)/value/value=True
\n(?:.+\n)*\1/(?P<_4>body/\d+)/_type='Return'
\n(?:.+\n)*\1/(?P=_4)         /lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/(?P=_4)         /value/value=False
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
        ^(.*)/_type='For'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/target/id=(?P<ITER_VAR>.+) # capture the name of the iteration variable
\n(?:.+\n)*\1/(?P<_1>body/.+)/_type='If' # The If appears at any depth in the loop
\n(?:.+\n)*\1/(?P=_1)        /test/.+/id=(?P=ITER_VAR) # The variable appears at any depth inside the condition
\n(?:.+\n)*\1/(?P=_1)        /(?P<_2>body/\d+)/_type='Return'
\n(?:.+\n)*\1/(?P=_1)        /(?P=_2)         /lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/(?P=_1)        /(?P=_2)         /value/id=(?P=ITER_VAR) # ... and is returned
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

#### Non sequential loops

--------------------------------------------------------------------------------

##### Construct `accumulate_until_1`

Accumulate the inputs until a sentinel value is encountered (accumulation expressed by: `acc = combine(x, acc)`).

###### Regex

```re
        ^(.*)/_type='While'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/test/value=True
\n(?:.+\n)*\1/body/\d+/targets/.+/id=(?P<INPUT>.+) # capture the name of the input
\n(?:.+\n)*\1/(?P<_1>body/\d+)/_type='If'
\n(?:.+\n)*\1/(?P=_1)         /test/args/0/id=(?P=INPUT)
\n(?:.+\n)*\1/(?P=_1)         /(?P<_2>body/\d+)/_type='Return'
\n(?:.+\n)*\1/(?P=_1)         /(?P=_2)         /value/id=(?P<ACC>.+) # capture the name of the accumulator
\n(?:.+\n)*\1/(?P<_3>body/\d+)/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/(?P=_3)         /targets/.*/id=(?P=ACC)
\n(?:.+\n)*\1/(?P=_3)         /value.*/id=(?P<VAR>((?P=INPUT)|(?P=ACC))) # name VAR the variable used here
\n(?:.+\n)*\1/(?P=_3)         /value.*/id=((?P=INPUT)|(?P=ACC))(?<!(?P=VAR)) # and check the other one is used there
```

###### Example

```python
1   def accumulate_inputs():
2       acc = neutral
3       while True:
4           x = read()
5           if is_sentinel(x):
6               return acc
7           acc = combine(x, acc)
```

###### Matches

```markdown
accumulate_until_1: 3-7
```

--------------------------------------------------------------------------------

##### Construct `accumulate_until_2`

Accumulate the inputs until a sentinel value is encountered (accumulation expressed by: `acc += x`).

###### Regex

```re
        ^(.*)/_type='While'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/test/value=True
\n(?:.+\n)*\1/body/\d+/targets/.+/id=(?P<INPUT>.+) # capture the name of the input
\n(?:.+\n)*\1/(?P<_1>body/\d+)/_type='If'
\n(?:.+\n)*\1/(?P=_1)         /test/args/0/id=(?P=INPUT)
\n(?:.+\n)*\1/(?P=_1)         /(?P<_2>body/\d+)/_type='Return'
\n(?:.+\n)*\1/(?P=_1)         /(?P=_2)         /value/id=(?P<ACC>.+) # capture the name of the accumulator
\n(?:.+\n)*\1/(?P<_3>body/\d+)/_type='AugAssign'
\n(?:.+\n)*\1/(?P=_3)         /lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/(?P=_3)         /target/id=(?P=ACC)
\n(?:.+\n)*\1/(?P=_3)         /value.*/id=(?P=INPUT)
```

###### Example

```python
1   def accumulate_inputs():
2       acc = neutral
3       while True:
4           x = read()
5           if is_sentinel(x):
6               return acc
7           acc += abs(x)
```

###### Matches

```markdown
accumulate_until_2: 3-7
```

--------------------------------------------------------------------------------

## Suggestions

These patterns match constructs that can be shortened.
It's up to you to decide if a rewriting would make the code clearer.

### Assignments

--------------------------------------------------------------------------------

##### Construct `suggest_conditional_expression`

When a conditional consists solely in assigning different values to the same variable, it may be rewritten as a conditional expression.

###### Regex

```re
        ^(.*)/_type='If'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/body/length=1
\n(?:.+\n)*\1/body/0/_type='Assign'
\n(?:.+\n)*\1/body/0/targets/0/hash=(?P<HASH>.+)
\n(?:.+\n)*\1/orelse/length=1
\n(?:.+\n)*\1/orelse/0/_type='Assign'
\n(?:.+\n)*\1/orelse/0/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/orelse/0/targets/0/hash=(?P=HASH)
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
        ^(.*)/_type='Assign'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/targets/length=1
\n(?:.+\n)*\1/targets/0/id=(?P<TARGET>.+)
\n(?:.+\n)*\1/value/_type='BinOp'
\n(?:.+\n)*\1/value/left/id=(?P=TARGET)
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

### Conditionals

--------------------------------------------------------------------------------

##### Construct `suggest_elif`

When the `else` branch of a conditional is an other conditional, it can be rewritten with an `elif` branch.

###### Regex

```re
        ^(.*)/_type='If'
\n(?:.+\n)*\1/(?P<_1>orelse)/length=1
\n(?:.+\n)*\1/(?P=_1)       /(?P<_2>0)/_type='If'
\n(?:.+\n)*\1/(?P=_1)       /(?P=_2)  /lineno=(?P<LINE>\d+)
```

###### Example

```python
1   if condition_1:
2       pass
3   else:
4       if condition_2:
5           pass
6       else:
7           pass
8   
9   if condition_1:
10      pass
11  else:
12      if condition_2:
13          pass
14      else:
15          pass
16      print("hello, world")
```

The first conditional (only) may be rewritten as:

```python
1   if condition_1:
2       pass
3   elif condition_2:
4       pass
5   else:
6       pass
```

###### Matches

```markdown
suggest_elif: 4
```

--------------------------------------------------------------------------------

### Subroutines

--------------------------------------------------------------------------------

##### Construct `suggest_condition_return`

When a predicate ends with a conditional whose sole purpose is to return `True` or `False`, it is enough to return the condition.

###### Regex

```re
        ^(.*)/_type='If'
\n(?:.+\n)*\1/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/body/0/_type='Return'
\n(?:.+\n)*\1/body/0/value/value=(?P<BOOL>True|False) # name BOOL the value used here
\n(?:.+\n)*\1/orelse/0/_type='Return'
\n(?:.+\n)*\1/orelse/0/lineno=(?P<LINE>\d+)
\n(?:.+\n)*\1/orelse/0/value/value=(True|False)(?<!(?P=BOOL)) # and check not BOOL is used there
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
