- [Expressions](#expressions)
  - [Literals](#literals)
      - [Construct `literal`](#construct-literal)
      - [Construct `int_literal`](#construct-int_literal)
      - [Construct `float_literal`](#construct-float_literal)
      - [Construct `imaginary_literal`](#construct-imaginary_literal)
  - [Subscripts](#subscripts)
      - [Construct `index`](#construct-index)
      - [Construct `index_arithmetic`](#construct-index_arithmetic)
      - [Construct `negative_index`](#construct-negative_index)
      - [Construct `slice`](#construct-slice)
      - [Construct `slice_step`](#construct-slice_step)
  - [Operators](#operators)
      - [Construct `unary_operator`](#construct-unary_operator)
      - [Construct `binary_operator`](#construct-binary_operator)
      - [Construct `conditional_expression`](#construct-conditional_expression)
  - [Boolean expressions](#boolean-expressions)
      - [Construct `boolean_operator`](#construct-boolean_operator)
      - [Construct `comparison_operator`](#construct-comparison_operator)
      - [Construct `chained_comparison`](#construct-chained_comparison)
      - [Construct `divisibility_test`](#construct-divisibility_test)
  - [Calls](#calls)
      - [Construct `function_call`](#construct-function_call)
      - [Construct `method_call`](#construct-method_call)
      - [Construct `method_chaining`](#construct-method_chaining)
      - [Construct `composition`](#construct-composition)
  - [Anonymous functions](#anonymous-functions)
      - [Construct `lambda_function`](#construct-lambda_function)
  - [Comprehensions](#comprehensions)
      - [Construct `comprehension`](#construct-comprehension)
      - [Construct `comprehension_for_count`](#construct-comprehension_for_count)
      - [Construct `filtered_comprehension`](#construct-filtered_comprehension)
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
      - [Construct `function`](#construct-function)
      - [Construct `function_with_default_positional_arguments`](#construct-function_with_default_positional_arguments)
      - [Construct `recursive_function`](#construct-recursive_function)
      - [Construct `deeply_recursive_function`](#construct-deeply_recursive_function)
      - [Construct `body_recursive_function`](#construct-body_recursive_function)
      - [Construct `generator`](#construct-generator)
      - [Construct `nested_function`](#construct-nested_function)
      - [Construct `closure`](#construct-closure)
  - [Conditionals](#conditionals)
      - [Construct `if`](#construct-if)
      - [Construct `if_else`](#construct-if_else)
      - [Construct `if_elif`](#construct-if_elif)
  - [Iterations](#iterations)
      - [Construct `for_each`](#construct-for_each)
      - [Construct `for_range_stop`](#construct-for_range_stop)
      - [Construct `for_range_start`](#construct-for_range_start)
      - [Construct `for_range_step`](#construct-for_range_step)
      - [Construct `for_indexes_elements`](#construct-for_indexes_elements)
      - [Construct `for_indexes`](#construct-for_indexes)
      - [Construct `nested_for`](#construct-nested_for)
      - [Construct `triangular_nested_for`](#construct-triangular_nested_for)
      - [Construct `square_nested_for`](#construct-square_nested_for)
  - [Exceptions](#exceptions)
      - [Construct `assertion`](#construct-assertion)
      - [Construct `raise_exception`](#construct-raise_exception)
      - [Construct `catch_exception`](#construct-catch_exception)
  - [Modules](#modules)
      - [Construct `import`](#construct-import)
      - [Construct `import_from`](#construct-import_from)
      - [Construct `import_by_call`](#construct-import_by_call)
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

# Expressions

## Literals

--------------------------------------------------------------------------------

#### Construct `literal`

##### Regex

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

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `literal:Num` | 1, 2, 4, 4, 7, 7, 7, 11, 11, 11, 12 |
| `literal:Str` | 3 |
| `literal:Tuple` | 4 |
| `literal:List` | 5, 11 |
| `literal:Dict` | 6 |
| `literal:Set` | 7 |
| `literal:False` | 8 |
| `literal:True` | 8 |
| `literal:None` | 9 |

--------------------------------------------------------------------------------

#### Construct `int_literal`

Matching literal does not require to construct a sophisticated regular expression: the heavy lifting is already made in the given AST, which stores them in a normalized form. For instance, integer literals are just sequence of digits:

##### Regex

```re
           ^(.*)/_type='Num'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/n=-?\d+\n
```

##### Example

The following examples of numeric literals are taken from the [reference](https://docs.python.org/3/reference/lexical_analysis.html#integer-literals).

```python
1   7, 2147483647, 0o177, 0b100110111, 3, -79228162514264337593543950336
2   0o377, 0xdeadbeef, 100_000_000_000, 0b_1110_0101
3   3.14, 10., .001, 1e100, 3.14e-10, 0e0, 3.14_15_93
4   23.14j, 10.j, 10j, .001j, 1e100j, 3.14e-10j, 3.14_15_93j
```

##### Matches

| Label | Lines |
|:--|:--|
| `int_literal` | 1, 1, 1, 1, 1, 1, 2, 2, 2, 2 |

--------------------------------------------------------------------------------

#### Construct `float_literal`

In the AST, a floating point literal consists of digits and at least one symbol among `.` and `e`.

##### Regex

```re
           ^(.*)/_type='Num'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/n=-?[\de\.]*[e\.][\de\.]*\n
```

##### Example

```python
1   7, 2147483647, 0o177, 0b100110111, 3, -79228162514264337593543950336
2   0o377, 0xdeadbeef, 100_000_000_000, 0b_1110_0101
3   3.14, 10., .001, 1e100, 3.14e-10, 0e0, 3.14_15_93
4   23.14j, 10.j, 10j, .001j, 1e100j, 3.14e-10j, 3.14_15_93j
```

##### Matches

| Label | Lines |
|:--|:--|
| `float_literal` | 3, 3, 3, 3, 3 |

--------------------------------------------------------------------------------

#### Construct `imaginary_literal`

In the AST, an imaginary literal contains the same symbols as a floating point literal, plus a mandatory trailing symbol `j`.

##### Regex

```re
           ^(.*)/_type='Num'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/n=-?[\de\.]*j\n
```

##### Example

```python
1   7, 2147483647, 0o177, 0b100110111, 3, -79228162514264337593543950336
2   0o377, 0xdeadbeef, 100_000_000_000, 0b_1110_0101
3   3.14, 10., .001, 1e100, 3.14e-10, 0e0, 3.14_15_93
4   23.14j, 10.j, 10j, .001j, 1e100j, 3.14e-10j, 3.14_15_93j
```

##### Matches

| Label | Lines |
|:--|:--|
| `imaginary_literal` | 4, 4, 4, 4, 4 |

--------------------------------------------------------------------------------

## Subscripts

--------------------------------------------------------------------------------

#### Construct `index`

##### Regex

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/slice/_type='Index'
```

##### Example

```python
1   a[42]
2   dictionary[key]
3   a[42:-1] # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `index` | 1, 2 |

--------------------------------------------------------------------------------

#### Construct `index_arithmetic`

##### Regex

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/slice/_type='Index'
\n(?:\1.+\n)*?\1/slice/value/_type='BinOp'
```

##### Example

```python
1   a[i + j]
2   a[i]
```

##### Matches

| Label | Lines |
|:--|:--|
| `index_arithmetic` | 1 |

--------------------------------------------------------------------------------

#### Construct `negative_index`

##### Regex

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/slice/_type='Index'
(   # A negative number
\n(?:\1.+\n)*?\1/slice/value/_type='Num'
\n(?:\1.+\n)*?\1/slice/value/n=(?P<SUFFIX>-\d+)
|   # A negated non-literal expression
\n(?:\1.+\n)*?\1/slice/value/op/_type='USub'
|   # A binary operation whose left operand is negated
\n(?:\1.+\n)*?\1/slice/value/_type='BinOp'
\n(?:\1.+\n)*?\1/slice/value/left/_type='UnaryOp'
\n(?:\1.+\n)*?\1/slice/value/left/op/_type='USub'
|   # A complemented expression
\n(?:\1.+\n)*?\1/slice/value/_type='UnaryOp'
\n(?:\1.+\n)*?\1/slice/value/op/_type='Invert'
)
```

##### Example

```python
1   a[-1]
2   a[-i]
3   a[len(a) - i] # LIMITATION: no match
4   a[-i - 1]
5   a[~i]
```

**Remark.** In line 4, `~i` evaluates to `-i - 1` (bitwise complement of `i`). Line 3 could be rewritten as `a[-i]`.

##### Matches

| Label | Lines |
|:--|:--|
| `negative_index:-1` | 1 |
| `negative_index` | 2, 4, 5 |

--------------------------------------------------------------------------------

#### Construct `slice`

##### Regex

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P<_1>slice)/_type='Slice'
\n(?:\1.+\n)*?\1/(?P=_1)      /step=None
```

##### Example

```python
1   a[1] # no match
2   a[1:-1]
3   a[1:-1:2] # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `slice` | 2 |

--------------------------------------------------------------------------------

#### Construct `slice_step`

##### Regex

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/(?P<_1>slice)/_type='Slice'
\n(?:\1.+\n)*?\1/(?P=_1)      /step/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   a[1] # no match
2   a[1:-1] # no match
3   a[1:-1:2]
```

##### Matches

| Label | Lines |
|:--|:--|
| `slice_step` | 3 |

--------------------------------------------------------------------------------

## Operators

--------------------------------------------------------------------------------

#### Construct `unary_operator`

##### Regex

```re
           ^(.*)/_type='UnaryOp'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/op/_type='(?P<SUFFIX>.+)'
```

##### Example

```python
1   a = -b
2   b = not c
3   c = -1 # no match
```

**Remark.** A negative literal is represented in the AST by a node `UnaryOp` with `USub` and `Num` children, and a _positive_ value for `n`. Our pre-processing of the AST simplifies this into a node `Num` and a _negative_ value for `n`.

##### Matches

| Label | Lines |
|:--|:--|
| `unary_operator:USub` | 1 |
| `unary_operator:Not` | 2 |

--------------------------------------------------------------------------------

#### Construct `binary_operator`

##### Regex

```re
           ^(.*)/_type='BinOp'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/op/_type='(?P<SUFFIX>.+)'
```

##### Example

```python
1   2**32768 - 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `binary_operator:Pow` | 1 |
| `binary_operator:Sub` | 1 |

--------------------------------------------------------------------------------

#### Construct `conditional_expression`

##### Regex

```re
           ^(.*)/_type='IfExp'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   foo if c else bar
```

##### Matches

| Label | Lines |
|:--|:--|
| `conditional_expression` | 1 |

--------------------------------------------------------------------------------

## Boolean expressions

--------------------------------------------------------------------------------

#### Construct `boolean_operator`

##### Regex

```re
           ^(.*)/_type='BoolOp'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/op/_type='(?P<SUFFIX>.+)'
```

##### Example

```python
1   a and b
2   a or c
3   not x # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `boolean_operator:And` | 1 |
| `boolean_operator:Or` | 2 |

**Remark.** `Not` is not a boolean operator in Python. To match it, use the construct [`unary_operator:Not`](#construct-unary_operator).

--------------------------------------------------------------------------------

#### Construct `comparison_operator`

##### Regex

```re
           ^(.*)/_type='Compare'
\n(?:\1.+\n)*?\1/ops/0/_type='(?P<SUFFIX>.+)'
\n(?:\1.+\n)*?\1/comparators/0/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   print(a == 3)
2   if a == b == c:
3       pass
4   needle in haystack
5   3 + 4
```

##### Matches

| Label | Lines |
|:--|:--|
| `comparison_operator:Eq` | 1, 2 |
| `comparison_operator:In` | 4 |

--------------------------------------------------------------------------------

#### Construct `chained_comparison`

##### Regex

```re
           ^(.*)/_type='Compare'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/comparators/length=(?!1\n)(?P<SUFFIX>.+)
```

##### Example

```python
1   a == 1
2   a == b == c
3   a < b < c < d
```

##### Matches

| Label | Lines |
|:--|:--|
| `chained_comparison:2` | 2 |
| `chained_comparison:3` | 3 |

--------------------------------------------------------------------------------

#### Construct `divisibility_test`

##### Regex

```re
           ^(.*)/_type='Compare'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/left/op/_type='Mod'
(   # try to match the % right operand with a number
\n(?:\1.+\n)*?\1/left/right/n=(?P<SUFFIX>.+)
)?
\n(?:\1.+\n)*?\1/ops/length=1
\n(?:\1.+\n)*?\1/ops/0/_type='(Eq|NotEq)'
```

##### Example

```python
1   a % b == 0
2   a % 2 == 0
3   a % 3 != 0
4   a % 4 == 1
5   a % 5 != 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `divisibility_test` | 1 |
| `divisibility_test:2` | 2 |
| `divisibility_test:3` | 3 |
| `divisibility_test:4` | 4 |
| `divisibility_test:5` | 5 |

--------------------------------------------------------------------------------

## Calls

--------------------------------------------------------------------------------

#### Construct `function_call`

##### Regex

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/func/_type='Name'
\n(?:\1.+\n)*?\1/func/id='(?P<SUFFIX>.+)'
```

##### Example

```python
1   print(len("hello, world"))
2   print(foobar((42)))
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_call:len` | 1 |
| `function_call:print` | 1, 2 |
| `function_call:foobar` | 2 |

--------------------------------------------------------------------------------

#### Construct `method_call`

##### Regex

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/func/_type='Attribute'
\n(?:\1.+\n)*?\1/func/attr='(?P<SUFFIX>.+)'
```

##### Example

```python
1   seq.index(42)
2   foo.bar(42)
```

##### Matches

| Label | Lines |
|:--|:--|
| `method_call:index` | 1 |
| `method_call:bar` | 2 |

--------------------------------------------------------------------------------

#### Construct `method_chaining`

##### Regex

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/func/_type='Attribute'
\n(?:\1.+\n)*?\1/func/value/_type='Call'
\n(?:\1.+\n)*?\1/func/value/func/_type='Attribute'
```

##### Example

```python
1   s.strip().split()
```

##### Matches

| Label | Lines |
|:--|:--|
| `method_chaining` | 1 |

--------------------------------------------------------------------------------

#### Construct `composition`

Apply a function or a method to an expression involving the result of another function or method application, without using an intermediate variable.

##### Regex

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/args/.*/_type='Call'
```

##### Example

```python
1   print(len("hello, world"))
2   print("hello, world")
3   print(a + abs(b))
4   print(s.upper())
```

##### Matches

| Label | Lines |
|:--|:--|
| `composition` | 1, 3, 4 |

--------------------------------------------------------------------------------

## Anonymous functions

--------------------------------------------------------------------------------

#### Construct `lambda_function`

##### Regex

```re
           ^(.*)/_type='Lambda'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   lambda x: x + 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `lambda_function` | 1 |

--------------------------------------------------------------------------------

## Comprehensions

--------------------------------------------------------------------------------

#### Construct `comprehension`

##### Regex

```re
           ^(.*)/_type='((?P<SUFFIX>List|Dict|Set)Comp|(?P<SUFFIX>Generator)Exp)'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   my_list = [x for x in seq]
2   my_set = {x for x in seq}
3   my_dict = {x: y for (x, y) in seq}
4   my_generator = (x for x in seq)
5   print([x for x in seq])
6   print(x for x in seq)
```

##### Matches

| Label | Lines |
|:--|:--|
| `comprehension:List` | 1, 5 |
| `comprehension:Set` | 2 |
| `comprehension:Dict` | 3 |
| `comprehension:Generator` | 4, 6 |

--------------------------------------------------------------------------------

#### Construct `comprehension_for_count`

Suffix the number of `for` clauses in a given comprehension.

##### Regex

```re
           ^(.*)/_type='(ListComp|DictComp|SetComp|GeneratorExp)'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/generators/length=(?P<SUFFIX>\d+)
```

##### Example

```python
1   print([x for x in seq])
2   seq1 = [2, 3, 5]
3   seq2 = [7, 11]
4   acc = [i * j for i in seq1 for j in seq2]
5   acc2 = [[x1 * x2 for x1 in seq1] for x2 in seq2]
```

**Remark.** Both lines 4 and 5 can be expressed with two nested `for` statements. However, the former uses one single accumulator and produces a list of numbers:
```python
acc = []
for i in seq1:
    for j in seq2:
        acc.append(i * j)
assert acc == [14, 22, 21, 33, 35, 55]
```
... whereas the latter uses two accumulators and produces a list _of lists_ of numbers:
```python
acc2 = []
for j in seq2:
    acc1 = []
    for i in seq1:
        acc1.append(i * j)
    acc2.append(acc1)
assert acc2 == [[14, 21, 35], [22, 33, 55]]
```
Therefore, line 5 consists in two comprehensions, each with one `for` clause only.

##### Matches

| Label | Lines |
|:--|:--|
| `comprehension_for_count:1` | 1, 5, 5 |
| `comprehension_for_count:2` | 4 |

--------------------------------------------------------------------------------

#### Construct `filtered_comprehension`

Match a comprehension with an `if` clause.

##### Regex

```re
/generators/\d+/ifs/0/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   [x for x in seq if foo(x)]
2   acc = [i * j for i in seq1 if foo(i) for j in seq2 if foo(j)]
```

##### Matches

| Label | Lines |
|:--|:--|
| `filtered_comprehension` | 1, 2, 2 |

--------------------------------------------------------------------------------

# Statements

## Assignments

--------------------------------------------------------------------------------

#### Construct `global_constant_definition`

##### Regex

```re
 ^(/body/\d+)/_type='Assign' # no indentation
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/.+/id='[A-Z0-9_]+' # all caps
```

##### Example

```python
1   PATH = "foo/bar"
2   (a, B) = (0, 1)
3   (A, B) = (0, 1)
4   if condition:
5       PATH = "foo/bar" # BUG: no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `global_constant_definition` | 1, 2, 3 |

--------------------------------------------------------------------------------

#### Construct `global_variable_definition`

##### Regex

```re
  ^(/body/\d+)/_type='Assign' # no indentation
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/.+/id='.*?[a-z] # at least one lowercase letter
```

##### Example

```python
1   PATH = "foo/bar"
2   (a, B) = (0, 1)
3   (a, b) = (0, 1)
4   if condition:
5       path = "foo/bar" # BUG: no match
6   path = "foo/bar"
7   MyPath = "foo/bar"
```

##### Matches

| Label | Lines |
|:--|:--|
| `global_variable_definition` | 2, 3, 6, 7 |

--------------------------------------------------------------------------------

#### Construct `assignment`

##### Regex

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   a = 42
2   (a, b) = (1, 2)
3   a[0] = b[0]
```

##### Matches

| Label | Lines |
|:--|:--|
| `assignment` | 1, 2, 3 |

--------------------------------------------------------------------------------

#### Construct `augmented_assignment`

##### Regex

```re
           ^(.*)/_type='AugAssign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   a += 1
2   a = a + 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `augmented_assignment` | 1 |

--------------------------------------------------------------------------------

#### Construct `chained_assignment`

##### Regex

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/length=(?!1\n).+
```

##### Example

```python
1   a = 42
2   a = b = 42
3   a = b = c = 42
```

##### Matches

| Label | Lines |
|:--|:--|
| `chained_assignment` | 2, 3 |

--------------------------------------------------------------------------------

#### Construct `swapping`

Swap two variables or two elements of an array with a 2-element tuple or list.

##### Regex

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/0/elts/length=2
\n(?:\1.+\n)*?\1/targets/0/elts/0/_hash=(?P<HASH_A>.+)
\n(?:\1.+\n)*?\1/targets/0/elts/1/_hash=(?P<HASH_B>.+)
\n(?:\1.+\n)*?\1/value/elts/length=2
\n(?:\1.+\n)*?\1/value/elts/0/_hash=(?P=HASH_B)
\n(?:\1.+\n)*?\1/value/elts/1/_hash=(?P=HASH_A)
```

##### Example

```python
1   (a, b) = (b, a)
2   [a, b] = [b, a]
3   (a[0], a[1]) = (a[1], a[0])
4   (a[i], a[i + 1]) = (a[i + 1], a[i])
```

##### Matches

| Label | Lines |
|:--|:--|
| `swapping` | 1, 2, 3, 4 |

--------------------------------------------------------------------------------

#### Construct `negation`

Update a variable by negating it.

##### Regex

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/0/_hash=(?P<HASH>.+) # capture hash
\n(?:\1.+\n)*?\1/value/_type='UnaryOp'
\n(?:\1.+\n)*?\1/value/op/_type='USub'
\n(?:\1.+\n)*?\1/value/operand/_hash=(?P=HASH) # match hash
```

##### Example

```python
1   a = -a
2   numbers[i] = -numbers[i]
3   a -= 2 * a # LIMITATION
4   a = -1 * a # LIMITATION
5   a = -abs(a) # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `negation` | 1, 2 |

--------------------------------------------------------------------------------

## Function definitions

--------------------------------------------------------------------------------

#### Construct `function`

##### Regex

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)'
\n(?:\1.+\n)* \1/.+/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   def foo(bar):
2       def fizz(buzz):
3           a += 1
4           print(a)
5
6       bar += 1
7       print(bar)
8
9   foo(42)
```

**Limitation.** This regex and the next one do not work properly when the function is decorated or has type hints ([#4](https://github.com/laowantong/paroxython/issues/4)).

##### Matches

| Label | Lines |
|:--|:--|
| `function:foo` | 1-7 |
| `function:fizz` | 2-4 |

--------------------------------------------------------------------------------

#### Construct `function_with_default_positional_arguments`

##### Regex

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)'
\n(?:\1.+\n)*?\1/args/defaults/length=(?!0\n).+
\n(?:\1.+\n)* \1/.+/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   def foobar(a, b="c"):
2       c = a + b
3       print(c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_with_default_positional_arguments:foobar` | 1-3 |

--------------------------------------------------------------------------------

#### Construct `recursive_function`

##### Regex

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)' # capture the name of the function
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)                    (?P<_2>.*)/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                    (?P=_2)   /func/id='(?P=SUFFIX)' # ensure it is called inside its own body
(   # capture the line number of the last line of the function (it may appear before Call)
\n(?:\1.+\n)* \1.+/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   def gob_program():
2       print("PENUS")
3       gob_program()
```

##### Matches

| Label | Lines |
|:--|:--|
| `recursive_function:gob_program` | 1-3 |

--------------------------------------------------------------------------------

#### Construct `deeply_recursive_function`

Any function `f` which contains a nested call to itself (`f(..., f(...), ...)`), e.g. the [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function).

##### Regex

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)' # capture the name of the function
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)                    (?P<_2>.*)/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                    (?P=_2)   /func/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)                    (?P=_2)   /func/id='(?P=SUFFIX)' # ensure it is called inside its own body
\n(?:\1.+\n)* \1/(?P=_1)                    (?P=_2)   /(?P<_3>args/.*)/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                    (?P=_2)   /(?P=_3)        /func/id='(?P=SUFFIX)'
(   # capture the line number of the last line of the function (it may appear before Call)
\n(?:\1.+\n)* \1/.+/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   def gob_program():
2       print("PENUS")
3       gob_program(gob_program())
4
5   def gob_program_2():
6       gob_program_2(gob_program_2())
7       print("PENUS")
```

##### Matches

| Label | Lines |
|:--|:--|
| `deeply_recursive_function:gob_program` | 1-3 |
| `deeply_recursive_function:gob_program_2` | 5-7 |

--------------------------------------------------------------------------------

#### Construct `body_recursive_function`

A tail call is a subroutine call performed as the last action of a procedure. A body-recursive function includes at least one non-tail recursive call.

##### Regex

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)' # capture the name of the function
(   # recursive call as an argument, an element, an operand, etc.
\n(?:\1.+\n)* \1/(?P<_1>.+/(args|elts|keys|left|right)\b.*)/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                                   /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)                                   /func/id='(?P=SUFFIX)'
|   # recursive call followed by a statement
\n(?:\1.+\n)* \1/(?P<_1>.+?(body|orelse))/(?P<_2>\d+)/(?P<_3>.*)/_type='Call'
\n(?:\1.+\n)* \1/(?P=_1)                /(?P=_2)    /(?P=_3)   /func/id='(?P=SUFFIX)'
\n(?:\1.+\n)*?\1/(?P=_1)                /(?!(?P=_2)).+
)
(   # capture the line number of the last line of the function (it may appear before Call)
\n(?:\1.+\n)* \1/.+/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   def ack(m, n):
2       if m == 0:
3           return n + 1
4       elif n == 0:
5           return ack(m-1, 1)  # tail call
6       else:
7           return ack(m-1, ack(m, n-1))  # body call
8
9   def divisor_count(n):
10      def recurs(candidates):
11          if len(candidates) == 0:
12              return 0
13          if n % candidates[0] == 0:
14              return 1 + recurs(candidates[1:])
15          return recurs(candidates[1:])
16      return recurs(range(1, n+1))
17
18  def place(x = 1, y = 1, queens = []):
19      if x > SIZE:
20          print(queens)
21      else:
22          if possible(x, y, queens):
23              place(x + 1, 1, queens + [(x, y)])
24          if y < SIZE:
25              place(x, y + 1, queens)
26
27  def body_sequence():
28      return (1, body_sequence())
29
30  def body_dict():
31      return {1: body_dict()} # body call: TODO
32
33  def short_circuit_1():
34      return c and short_circuit_1() # tail call
32
33  def short_circuit_2():
34      return short_circuit_2() and c # body call: TODO
```

**Remark.** Since the short-circuit expression `c and foobar()` is equivalent to the conditional expression `if c then foobar() else False`, the function `foobar()` is actually tail recursive. This holds for `c or foobar()` too, which is equivalent to `if c then True else foobar()`.

##### Matches

| Label | Lines |
|:--|:--|
| `body_recursive_function:ack` | 1-7 |
| `body_recursive_function:recurs` | 10-15 |
| `body_recursive_function:place` | 18-25 |
| `body_recursive_function:body_sequence` | 27-28 |

--------------------------------------------------------------------------------

#### Construct `generator`

##### Regex

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)'
\n(?:\1.+\n)* \1/.+/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/.+/value/_type='Yield(From)?'
(   # capture the line number of the last line of the function (it may appear before Call)
\n(?:\1.+\n)* \1/.+/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   def foo():
2       for x in s:
3           yield bar
4
5   def energy():
6       yield from waste
```

##### Matches

| Label | Lines |
|:--|:--|
| `generator:foo` | 1-3 |
| `generator:energy` | 5-6 |

--------------------------------------------------------------------------------

#### Construct `nested_function`

##### Regex

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)'
\n(?:\1.+\n)*?\1/.+/_type='FunctionDef'
\n(?:\1.+\n)* \1/.+/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   def outer_function(a, b):
2   	c = a + b
3   	def inner_function(c):
4   		print(c)
5   	return inner_function(c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `nested_function:outer_function` | 1-5 |

--------------------------------------------------------------------------------

#### Construct `closure`

Function enclosing the definition of an inner function and returning it. Beware that the current regex does not check whether the inner function refers to a variable defined in the enclosing function.

##### Regex

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)'
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/(?P=_1)                    /name=(?P<NAME>.+) # capture inner function name
\n(?:\1.+\n)* \1/(?P<_2>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_2)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_2)                    /value/_type='Name'
\n(?:\1.+\n)*?\1/(?P=_2)                    /value/id=(?P=NAME) # match inner function name
```

##### Example

```python
1   def outer_function(a, b):
2       c = a + b
3       def inner_function():
4           print(c)
5       return inner_function
```

##### Matches

| Label | Lines |
|:--|:--|
| `closure:outer_function` | 1-5 |

--------------------------------------------------------------------------------

## Conditionals

--------------------------------------------------------------------------------

#### Construct `if`

##### Regex

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/.+/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   if condition_1:
2       if condition_2:
3           pass
4   else:
5       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `if` | 1-5, 2-3 |

--------------------------------------------------------------------------------

#### Construct `if_else`

`if` statement with `else`.

##### Regex

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/0/_type=(?!'If').+
\n(?:\1.+\n)* \1/orelse/.*/lineno=(?P<LINE>\d+)
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `if_else` | 1-5 |

--------------------------------------------------------------------------------

#### Construct `if_elif`

`if` statement with `elif`.

##### Regex

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/0/_type='If'
\n(?:\1.+\n)* \1/orelse/.*/lineno=(?P<LINE>\d+)
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `if_elif` | 1-4, 6-11 |

--------------------------------------------------------------------------------

## Iterations

--------------------------------------------------------------------------------

#### Construct `for_each`
Iterate over the elements of a (named) collection.

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/iter/_type='Name'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   for x in seq_1:
2       for y in range(len(seq_3)): # no match
3           pass
4       for i in seq_2:
5           pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `for_each` | 1-5, 4-5 |

--------------------------------------------------------------------------------

#### Construct `for_range_stop`

Iterate over a range with exactly 1 argument (stop).

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=1
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   for i in range(stop):
2       pass
3   for i in range(start, stop): # no match
4       pass
5   for i in range(start, stop, step): # no match
6       pass
7   for i in range(start, stop, -1): # no match
8       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `for_range_stop` | 1-2 |

--------------------------------------------------------------------------------

#### Construct `for_range_start`

Iterate over a range with exactly 2 arguments (start, stop).

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=2
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `for_range_start` | 3-4 |

--------------------------------------------------------------------------------

#### Construct `for_range_step`

Iterate over a range with 3 arguments (start, stop, step).

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=3
(   # If the step is a number, capture it as a suffix
\n(?:\1.+\n)*?\1/iter/args/2/_type='Num'
\n(?:\1.+\n)*?\1/iter/args/2/n=(?<SUFFIX>.+)
)?
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `for_range_step` | 5-6 |
| `for_range_step:-1` | 7-8 |
| `for_range_step:2` | 9-10 |

--------------------------------------------------------------------------------

#### Construct `for_indexes_elements`

Iterate over index numbers and elements of a collection.

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/iter/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/func/id='enumerate'
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   for (i, element) in enumerate(elements):
2       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `for_indexes_elements` | 1-2 |

--------------------------------------------------------------------------------

#### Construct `for_indexes`

Iterate over index numbers of a collection.

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/_type='Call'
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=1
\n(?:\1.+\n)*?\1/iter/args/0/_type='Call'
\n(?:\1.+\n)*?\1/iter/args/0/func/id='len'
\n(?:\1.+\n)*?\1/iter/keywords/length=0
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   for i in range(len(elements)):
2       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `for_indexes` | 1-2 |

--------------------------------------------------------------------------------

#### Construct `nested_for`

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   for x_1 in seq_1:
2       for x_2 in seq_2:
3           pass
4       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `nested_for` | 1-4 |

--------------------------------------------------------------------------------

#### Construct `triangular_nested_for`

A `for` loop with a counter `i` and a nested `for` loop which makes `i` iterations. The total number of iterations is a [triangular number](https://en.wikipedia.org/wiki/Triangular_number).

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/target/id=(?P<VAR>.+) # capture iteration variable
\n(?:\1.+\n)*?\1/iter/_type='Call'
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=1 # only range(arg1)
(   # i goes from 0 to n, and j from 0 to i
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/func/id='range'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/args/length=1 # only range(arg1)
\n(?:\1.+\n)* \1/(?P=_1)                    /iter/args/0.*/id=(?P=VAR) # match iteration variable
|   # i goes from 0 to n, and j from i to n
\n(?:\1.+\n)*?\1/iter/args/0/_hash=(?P<STOP>.+) # capture stop expression
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/func/id='range'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/args/length=2 # only range(arg1, arg2)
\n(?:\1.+\n)* \1/(?P=_1)                    /iter/args/0(/.+)*/id=(?P=VAR) # match iteration variable
\n(?:\1.+\n)* \1/(?P=_1)                    /iter/args/1(/.+)*/_hash=(?P=STOP) # match stop expression
)
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   for i in range(n):
2       for j in range(i - 1):
3           pass
4
5   for i in range(n):
6       for j in range(i+1, n):
7           pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `triangular_nested_for` | 1-3, 5-7 |

--------------------------------------------------------------------------------

#### Construct `square_nested_for`

Two nested `for` loops doing the same number of iterations.

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/_hash=(?P<HASH>.+) # capture _hash
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_hash=(?P=HASH) # match _hash
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   for i in range(1, 2 * n, step):
2       for j in range(1, 2 * n, step):
3           pass
4
5   for x in seq:
6       for y in seq:
7           pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `square_nested_for` | 1-3, 5-7 |

--------------------------------------------------------------------------------

## Exceptions

--------------------------------------------------------------------------------

#### Construct `assertion`

##### Regex

```re
           ^(.*)/_type='Assert'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   assert a == 42
```

##### Matches

| Label | Lines |
|:--|:--|
| `assertion` | 1 |

--------------------------------------------------------------------------------

#### Construct `raise_exception`

##### Regex

```re
           ^(.*)/_type='Raise'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/exc/_type='Call'
\n(?:\1.+\n)*?\1/exc/func/_type='Name'
\n(?:\1.+\n)*?\1/exc/func/id='(?P<SUFFIX>.+)'
```

##### Example

```python
1   x = input("Answer? ")
2   if x != 42:
3       raise Exception("Wrong answer!")
```

##### Matches

| Label | Lines |
|:--|:--|
| `raise_exception:Exception` | 3 |

--------------------------------------------------------------------------------

#### Construct `catch_exception`

##### Regex

```re
           ^(.*)/_type='Try'
\n(?:\1.+\n)* \1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P<_1>handlers/\d+)/_type='ExceptHandler'
(   # is the exception type specified ?
\n(?:\1.+\n)*?\1/(?P=_1)             /type/_type='Name'
\n(?:\1.+\n)*?\1/(?P=_1)             /type/id='(?P<SUFFIX>.+)'
)?
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   try:
2       with open(path) as opened_file:
3           data = opened_file.read()
4   except:
5       print(f"Could not open {path}")
6   try:
7       with open(path) as opened_file:
8           data = opened_file.read()
9   except FileNotFoundError:
10      print(f"Could not open {path}")
11  try:
12      with open(path) as opened_file:
13          data = opened_file.read()
14  except (IndexError, UnboundLocalError, ValueError): # BUG: no match
15      print(f"Could not open {path}")
```

##### Matches

| Label | Lines |
|:--|:--|
| `catch_exception` | 1-5, 11-15 |
| `catch_exception:FileNotFoundError` | 6-10 |

--------------------------------------------------------------------------------

## Modules

--------------------------------------------------------------------------------

#### Construct `import`

##### Regex

```re
           ^(.*)/_type='Import'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
(
\n(?:\1.+\n)*?\1/names/\d+/name='(?P<SUFFIX>.+)'
)+
```

##### Example

```python
1   import a, b, c
2   import d
```

##### Matches

| Label | Lines |
|:--|:--|
| `import:a` | 1 |
| `import:c` | 1 |
| `import:b` | 1 |
| `import:d` | 2 |

--------------------------------------------------------------------------------

#### Construct `import_from`

##### Regex

```re
           ^(.*)/_type='ImportFrom'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/module='(?P<SUFFIX>.+)'
```

##### Example

```python
1   from a import b, c
2   from d import e
```

##### Matches

| Label | Lines |
|:--|:--|
| `import_from:a` | 1 |
| `import_from:d` | 2 |

--------------------------------------------------------------------------------

#### Construct `import_by_call`

##### Regex

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/func/id='__import__'
(
\n(?:\1.+\n)*?\1/args/\d+/s='(?P<SUFFIX>.+)'
)+
```

##### Example

```python
1   foo, bar = __import__("a", "b")
```

##### Matches

| Label | Lines |
|:--|:--|
| `import_by_call:a` | 1 |
| `import_by_call:b` | 1 |

--------------------------------------------------------------------------------

# Code patterns

## Iterative patterns

### Sequential loops

--------------------------------------------------------------------------------

#### Construct `accumulate_elements`

An accumulator is iteratively updated from its previous value and the value of the iteration variable.

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/target/_type='Name'
\n(?:\1.+\n)*?\1/target/id=(?P<ITER_VAR>.+)
(   # the accumulator either appears on both sides of a simple assignment with the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>((?:body|orelse)/\d+/?)*)/_type='(?P<SUFFIX>Assign)'
\n(?:\1.+\n)*?\1/(?P=_1)                         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)                         /targets/.*/id=(?P<ACC>.+) # capture the name of the accumulator
\n(?:\1.+\n)*?\1/(?P=_1)                         /value/_ids=(?=.*?(?P=ACC))(?=.*?(?P=ITER_VAR)).* # both appear in RHS
|   # or should be on LHS of an augmented assignement with the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>((?:body|orelse)/\d+/?)*)/_type='(?P<SUFFIX>AugAssign)'
\n(?:\1.+\n)*?\1/(?P=_1)                         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)                         /value.*/id=(?P=ITER_VAR)
|   # or should be mutated by calling a function on this accumulator and the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>((?:body|orelse)/\d+/?)*)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_1)                         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)                         /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                         /value/func/_type='(?P<SUFFIX>Name)'
\n(?:\1.+\n)*?\1/(?P=_1)                         /value/func/id='(?!breakpoint|delattr|eval|exec|help|input|open|print|setattr|super).+'
\n(?:\1.+\n)*?\1/(?P=_1)                         /value/args/length=(?![01]\n)\d+ # the function has several arguments
\n(?:\1.+\n)* \1/(?P=_1)                         /value/args/\d+/id=(?P=ITER_VAR) # which include the iteration variable
|   # or should be mutated by calling a method of this accumulator, again on the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>((?:body|orelse)/\d+/?)*)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_1)                         /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)                         /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                         /value/func/_type='(?P<SUFFIX>Attribute)'
\n(?:\1.+\n)* \1/(?P=_1)                         /value/args/\d+/id=(?P=ITER_VAR) # the arguments include the iteration variable
)
(   # capture the line number of the last line of the function (it may appear before Call)
\n(?:\1.+\n)* \1.*/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   def accumulate_elements(elements):
2       acc = seed
3       for element in elements:
4           acc = element + acc
5           seed += 1
6       return acc
7   for i in range(10):
8       acc = combine(acc, i)
9   for i in range(10):
10      if condition:
11           acc += i
12      pass
13  for i in range(10):
14      acc += foo(bar, i)
15  for i in range(10):
16      foo(acc, bar, i)
17      pass
18  for i in range(10):
19      acc.foo(bar, i)
20      pass
21  for i in range(10): # no match (cf. remark)
22      print(foobar, i)
```

**Remark.**
The third alternative of the regex is experimental. It matches any one-line function call on the iteration variable and another argument, not only those which mutate one of their arguments (hopefully the accumulator). The built-in functions with side effects (such as `print()`) are explicitely excluded, but this may not be enough. The fourth alternative, too, is certainly broader than necessary. Handle with care.

##### Matches

| Label | Lines |
|:--|:--|
| `accumulate_elements:Assign` | 3-5, 7-8 |
| `accumulate_elements:Attribute` | 18-20 |
| `accumulate_elements:AugAssign` | 9-12, 13-14 |
| `accumulate_elements:Name` | 15-17 |

--------------------------------------------------------------------------------

#### Construct `filter_for`

An accumulation pattern that, from a given collection, returns a list containing only those elements that verify a certain condition.

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/target/id=(?P<ID_1>.+) # capture the iteration variable
\n(?:\1.+\n)*?\1/(?P<_1>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)* \1/(?P=_1)                /test/args/\d+/id=(?P=ID_1) # match it in an inner conditional test
\n(?:\1.+\n)* \1/(?P=_1)                /(?P<_2>(?:body|orelse)/\d+)/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)                /(?P=_2)                    /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                /(?P=_2)                    /value/func/attr='append'
\n(?:\1.+\n)*?\1/(?P=_1)                /(?P=_2)                    /value/args/0/id=(?P=ID_1) # match it in an append()
\n(?:\1.+\n)* \1.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   for element in elements:
2       print("foo")
3       if predicate(element):
4           print("bar")
5           acc.append(element)
6       print("fiz")
```

##### Matches

| Label | Lines |
|:--|:--|
| `filter_for` | 1-6 |

--------------------------------------------------------------------------------

#### Construct `find_best_element`

An accumulation pattern that, from a given collection, returns the best element verifying a certain condition.

##### Regex

```re
           ^(.*)/(?P<_1>(?:body|orelse)/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_1)                /targets/0/id=(?P<CANDIDATE>.+) # capture candidate
\n(?:\1.+\n)* \1/(?P<_2>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_2)                /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_2)                /target/id=(?P<ITER_VAR>.+) # capture iteration variable
\n(?:\1.+\n)* \1/(?P=_2)                /(?P<_3>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /test/_ids=(?=.*?(?P=ITER_VAR))(?=.*?(?P=CANDIDATE)).* # match both
\n(?:\1.+\n)* \1/(?P=_2)                /(?P=_3)                    /test/.*/id=(?P=CANDIDATE) # match candidate
\n(?:\1.+\n)* \1/(?P=_2)                /(?P=_3)                    /(?P<_4>(?:body|orelse)/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /(?P=_4)                /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /(?P=_4)                /targets/0/id=(?P=CANDIDATE) # match candidate
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /(?P=_4)                /value/id=(?P=ITER_VAR) # match iteration variable
(
\n(?:\1.+\n)* \1(?P=_2)                /(?P=_3).*/lineno=(?P<LINE>\d+)
)?
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `find_best_element` | 3-5, 10-12 |

--------------------------------------------------------------------------------

#### Construct `universal_quantifier`

Check if all the elements of a collection satisfy a predicate.

##### Regex

```re
          ^(.*?)/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)                    /(?P<_2>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)* \1/(?P=_1)                    /(?P=_2)                    /(?P<_3>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)                    /(?P=_2)                    /(?P=_3)                    /value/value=False
\n(?:\1.+\n)* \1/(?P<_4>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_4)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_4)                    /value/value=True
```

##### Example

```python
1   def all_elements_satisfy(elements):
2       for element in elements:
3           if not is_good(element):
4               return False
5       return True
```

##### Matches

| Label | Lines |
|:--|:--|
| `universal_quantifier` | 2-5 |

--------------------------------------------------------------------------------

#### Construct `existential_quantifier`

Check if any element of a collection satisfies a predicate.

##### Regex

```re
          ^(.*?)/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_1)                    /(?P<_2>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)* \1/(?P=_1)                    /(?P=_2)                    /(?P<_3>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)                    /(?P=_2)                    /(?P=_3)                    /value/value=True
\n(?:\1.+\n)* \1/(?P<_4>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_4)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_4)                    /value/value=False
```

##### Example

```python
2   def some_elements_satisfy(elements):
1       for element in elements:
3           if is_good(element):
4               return True
5       return False
```

##### Matches

| Label | Lines |
|:--|:--|
| `existential_quantifier` | 2-5 |

--------------------------------------------------------------------------------

#### Construct `find_first_element`

Linear search. Return the first element of a sequence satisfying a predicate.

##### Regex

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/target/id=(?P<ITER_VAR>.+) # capture the name of the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/.+)/_type='If' # The If appears at any depth in the loop
\n(?:\1.+\n)* \1/(?P=_1)                   /test/.+/id=(?P=ITER_VAR) # The variable appears at any depth inside the condition
\n(?:\1.+\n)*?\1/(?P=_1)                   /(?P<_2>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)                   /(?P=_2)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)                   /(?P=_2)                    /value/id=(?P=ITER_VAR) # ... and is returned
```

##### Example

```python
1   def search(seq, x):
2       for i in range(len(seq)):
3           if seq[i] == x:
4               return i
5       return None
```

##### Matches

| Label | Lines |
|:--|:--|
| `find_first_element` | 2-4 |

--------------------------------------------------------------------------------

### Non sequential finite loops

--------------------------------------------------------------------------------

#### Construct `evolve_state`

Evolve the value of a variable until it reaches a desired state.

##### Regex

```re
           ^(.*)/_type='While'
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
(
\n(?:\1.+\n)* \1.*/lineno=(?P<LINE>\d+)
)?
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `evolve_state` | 2-3, 6-7, 8-9, 10-11 |

--------------------------------------------------------------------------------

### Non sequential infinite loops

--------------------------------------------------------------------------------

#### Construct `accumulate_stream`

Accumulate the inputs until a sentinel value is encountered (accumulation expressed by: `acc = combine(x, acc)`).

##### Regex

```re
           ^(.*)/_type='While'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/test/value=True
\n(?:\1.+\n)* \1/(?:body|orelse)/\d+/targets/.+/id=(?P<INPUT>.+) # capture the name of the input
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_1)                /test/_ids=.*?(?P=INPUT).* # the input is tested
\n(?:\1.+\n)* \1/(?P=_1)                /(?P<_2>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)                /(?P=_2)                    /value/id=(?P<ACC>.+) # capture the name of the accumulator
(   # the accumulator either appears on both sides of a simple assignment with the input
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='(?P<SUFFIX>Assign)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_3)                    /targets/.*/id=(?P=ACC)
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_ids=(?=.*(?P=INPUT))(?=.*(?P=ACC)) # both appear in RHS
|   # or is on LHS of an augmented assignement with the input
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='(?P<SUFFIX>AugAssign)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_3)                    /target/id=(?P=ACC)
\n(?:\1.+\n)* \1/(?P=_3)                    /value.*/id=(?P=INPUT)
|   # or should be mutated by calling a function on this accumulator and the iteration variable
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_3)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_ids=(?=.*(?P=INPUT))(?=.*(?P=ACC)).+ # both appear in RHS
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/_type='(?P<SUFFIX>Name)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/id='(?!(?P=ACC)|(?P=INPUT)|breakpoint|delattr|eval|exec|help|input|open|print|setattr|super).+'
|   # or should be mutated by calling a method of this accumulator, again on the iteration variable
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_3)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/_type='(?P<SUFFIX>Attribute)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/value/id=(?P=ACC) # a method of acc is called on...
\n(?:\1.+\n)* \1/(?P=_3)                    /value/args/\d+/id=(?P=INPUT) # the iteration variable
)
(
\n(?:\1.+\n)* \1.*/lineno=(?P<LINE>\d+)
)?
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `accumulate_stream:Assign` | 3-7 |
| `accumulate_stream:AugAssign` | 11-15 |
| `accumulate_stream:Name` | 19-23 |
| `accumulate_stream:Attribute` | 27-31 |

--------------------------------------------------------------------------------

# Suggestions

These patterns match constructs that can be shortened.
It's up to you to decide if a rewriting would make the code clearer.

## Assignments

--------------------------------------------------------------------------------

#### Construct `suggest_conditional_expression`

When a conditional simply assigns different values to the same variable, it may be rewritten as a conditional expression.

##### Regex

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/body/length=1
\n(?:\1.+\n)*?\1/body/0/_type='Assign'
\n(?:\1.+\n)*?\1/body/0/targets/0/_hash=(?P<HASH>.+)
\n(?:\1.+\n)*?\1/orelse/length=1
\n(?:\1.+\n)*?\1/orelse/0/_type='Assign'
\n(?:\1.+\n)*?\1/orelse/0/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/0/targets/0/_hash=(?P=HASH)
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `suggest_conditional_expression` | 1-4 |

--------------------------------------------------------------------------------

#### Construct `suggest_augmented_assignment`

When the RHS of an assignment consists in a binary operation whose left operand is the target (`a = a op expr`), the statement can be shortened as `a op= expr`.

##### Regex

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/length=1
\n(?:\1.+\n)*?\1/targets/0/id=(?P<TARGET>.+)
\n(?:\1.+\n)*?\1/value/_type='BinOp'
\n(?:\1.+\n)*?\1/value/left/id=(?P=TARGET)
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `suggest_augmented_assignment` | 1, 2 |

--------------------------------------------------------------------------------

## Expressions

--------------------------------------------------------------------------------

#### Construct `suggest_comparison_chaining`

When the `else` branch of a conditional is another conditional, it can be rewritten with an `elif` branch.

##### Regex

```re
           ^(.*)/_type='BoolOp'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/op/_type='And'
\n(?:\1.+\n)*?\1/values/0/_type='Compare'
\n(?:\1.+\n)*?\1/values/0/comparators/0/_hash=(?P<HASH_1>.+) # capture the right operand of the left comparison
\n(?:\1.+\n)*?\1/values/1/_type='Compare'
\n(?:\1.+\n)*?\1/values/1/left/_hash=(?P=HASH_1) # match the left operand of the right comparison
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `suggest_comparison_chaining` | 1, 2, 3, 4 |

--------------------------------------------------------------------------------

#### Construct `suggest_constant_definition`

Match magic numbers (unnamed numerical constants) other than -1, 0, 1 and 2. A number in the RHS of an assignment to a constant is of course ignored.

##### Regex

```re
  ^(/(?:body|orelse)/\d+)
(   # indented lines
              /(?P<_1>(?:body|orelse)/.+)/lineno=(?P<LINE>\d+)
\n          \1/(?P=_1)                   /n=(?!(-1|0|1|2)\n)
|   # non indented lines
              /_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/targets/0/id='.*?[a-z].*' # at least one lowercase letter
\n(?:\1.+\n)*?\1/value/n=(?!(-1|0|1|2)\n)
)
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `suggest_constant_definition` | 2, 4, 6 |

--------------------------------------------------------------------------------

## Subroutines

--------------------------------------------------------------------------------

#### Construct `suggest_condition_return`

When a predicate ends with a conditional whose sole purpose is to return `True` or `False`, it is enough to return the condition.

##### Regex

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/body/0/_type='Return'
\n(?:\1.+\n)*?\1/body/0/value/value=(?P<BOOL>True|False) # name BOOL the value used here
\n(?:\1.+\n)*?\1/orelse/0/_type='Return'
\n(?:\1.+\n)*?\1/orelse/0/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/0/value/value=(True|False)(?<!(?P=BOOL)) # and check not BOOL is used there
```

##### Example

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

##### Matches

| Label | Lines |
|:--|:--|
| `suggest_condition_return` | 2-5, 8-11 |
