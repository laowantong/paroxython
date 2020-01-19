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
      - [Constructs `chained_equalities|chained_inequalities`](#constructs-chained_equalitieschained_inequalities)
      - [Construct `divisibility_test`](#construct-divisibility_test)
      - [Construct `short_circuit`](#construct-short_circuit)
  - [Calls](#calls)
      - [Construct `function_call`](#construct-function_call)
      - [Construct `call_parameter`](#construct-call_parameter)
      - [Construct `method_call`](#construct-method_call)
      - [Construct `method_call_object`](#construct-method_call_object)
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
      - [Construct `assignment`](#construct-assignment)
      - [Construct `augmented_assignment`](#construct-augmented_assignment)
      - [Construct `chained_assignment`](#construct-chained_assignment)
      - [Construct `assignment_lhs_identifier`](#construct-assignment_lhs_identifier)
      - [Construct `assignment_rhs_identifier`](#construct-assignment_rhs_identifier)
    - [Assignment idioms](#assignment-idioms)
      - [Construct `swapping`](#construct-swapping)
      - [Construct `negation`](#construct-negation)
  - [Function definitions](#function-definitions)
      - [Construct `function`](#construct-function)
      - [Construct `function_returning_a_value`](#construct-function_returning_a_value)
      - [Construct `procedure`](#construct-procedure)
      - [Construct `function_with_default_positional_arguments`](#construct-function_with_default_positional_arguments)
      - [Construct `recursive_function`](#construct-recursive_function)
      - [Construct `deeply_recursive_function`](#construct-deeply_recursive_function)
      - [Construct `body_recursive_function`](#construct-body_recursive_function)
      - [Construct `generator`](#construct-generator)
      - [Construct `nested_function`](#construct-nested_function)
      - [Construct `closure`](#construct-closure)
  - [Conditionals](#conditionals)
      - [Construct `if`](#construct-if)
      - [Construct `if_test_id`](#construct-if_test_id)
      - [Construct `if_then_branch`](#construct-if_then_branch)
      - [Construct `if_elif_branch`](#construct-if_elif_branch)
      - [Construct `if_else_branch`](#construct-if_else_branch)
      - [Construct `nested_if`](#construct-nested_if)
  - [Iterations](#iterations)
      - [Construct `for`](#construct-for)
      - [Construct `for_each`](#construct-for_each)
      - [Construct `for_range_stop`](#construct-for_range_stop)
      - [Construct `for_range_start`](#construct-for_range_start)
      - [Construct `for_range_step`](#construct-for_range_step)
      - [Construct `for_indexes_elements`](#construct-for_indexes_elements)
      - [Construct `for_indexes`](#construct-for_indexes)
      - [Construct `nested_for`](#construct-nested_for)
      - [Construct `triangular_nested_for`](#construct-triangular_nested_for)
      - [Construct `square_nested_for`](#construct-square_nested_for)
      - [Construct `while`](#construct-while)
  - [Exceptions](#exceptions)
      - [Construct `assertion`](#construct-assertion)
      - [Construct `try`](#construct-try)
      - [Construct `raise`](#construct-raise)
      - [Construct `except`](#construct-except)
      - [Constructs `try_raise|try_except`](#constructs-try_raisetry_except)
  - [Modules](#modules)
      - [Construct `import_module`](#construct-import_module)
      - [Construct `import_name`](#construct-import_name)
      - [Construct `import`](#construct-import)
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
- [Programs](#programs)
      - [Construct `category`](#construct-category)
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

##### Definition

```re
^(.*)
(   # match None, True and False
              /_type='NameConstant'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/value=(?P<SUFFIX>None|True|False)
|   # match any other constant
              /_type='(?P<SUFFIX>Str|Num|Tuple|Dict|Set|List)'
\n(?:\1.+\n)*?\1/_ids=
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

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/slice/_type='Slice'
\n(?:\1.+\n)*?\1/slice/step=None
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

##### Definition

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/slice/_type='Slice'
\n(?:\1.+\n)*?\1/slice/step/lineno=(?P<LINE>\d+)
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

##### Definition

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

##### Definition

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

Match the so-called ternary operator.

##### Definition

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

##### Definition

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

##### Definition

```re
           ^(.*)/ops/        (?P<_1>\d+)/_type='(?P<SUFFIX>Eq|Lt|LtE|Gt|GtE|In|NotIn|NotEq|Is|IsNot)'
\n(?:\1.+\n)*?\1/comparators/(?P=_1)    /lineno=(?P<LINE>\d+)
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
| `comparison_operator:Eq` | 1, 2, 2 |
| `comparison_operator:In` | 4 |

--------------------------------------------------------------------------------

#### Construct `chained_comparison`

##### Definition

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

#### Constructs `chained_equalities|chained_inequalities`

##### Definition

```sql
SELECT CASE b.name_suffix
           WHEN "Eq" THEN "chained_equalities"
           ELSE "chained_inequalities"
       END,
       count(*),
       span
FROM t a
JOIN t b USING (span)
WHERE a.name_prefix = "chained_comparison"
  AND b.name_prefix = "comparison_operator"
  AND b.name_suffix IN ("Eq",
                        "Lt",
                        "LtE",
                        "Gt",
                        "GtE")
GROUP BY span,
         b.name_suffix
HAVING count(*) > 1
ORDER BY span
```

##### Example

```python
1   a == 1
2   a == b == c
3   a < b < c < d
4   a == b == c and d < e
```

##### Matches

| Label | Lines |
|:--|:--|
| `chained_equalities:2` | 2, 4 |
| `chained_inequalities:3` | 3 |

--------------------------------------------------------------------------------

#### Construct `divisibility_test`

##### Definition

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

#### Construct `short_circuit`

When the value of the left operand suffices to determine the value of a boolean expression, short-circuit evaluation skips the right operand. This behaviour is sometimes desirable or even required, but Paroxython currently cannot detect the case: so, when commutating the operands would result in an error or a performance penalty, you should add manually the hint `# paroxython: short_circuit` in the source-code.

##### Definition

```
```

##### Example

```python
1   def insertion_sort(a):
2       for i in range(1, len(a)):
3           aux = a[i]
4           j = i
5           while j > 0 and a[j-1] > aux:  # paroxython: short_circuit:And
6               a[j] = a[j-1]
7               j -= 1
8           a[j] = aux
```

##### Matches

| Label | Lines |
|:--|:--|
| `short_circuit:And` | 5 |

--------------------------------------------------------------------------------

## Calls

--------------------------------------------------------------------------------

#### Construct `function_call`

##### Definition

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/func/_type='Name'
\n(?:\1.+\n)*?\1/func/id='(?P<SUFFIX>.+)'
```

##### Example

```python
1   foo(a, b, c)
2   bar()
3   buzz(x, 2)
4   fizz(foobar(x), 2)
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_call:bar` | 2 |
| `function_call:buzz` | 3 |
| `function_call:fizz` | 4 |
| `function_call:foo` | 1 |
| `function_call:foobar` | 4 |

--------------------------------------------------------------------------------

#### Construct `call_parameter`

##### Definition

```re
  ^(.*/args/\d+)/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/id='(?P<SUFFIX>.+)'
```

##### Example

```python
1   foo(a, b, c)
2   bar()
3   buzz(x, 2)
4   fizz(foobar(x), 2)
5   foo.bar(buzz, bizz)
```

##### Matches

| Label | Lines |
|:--|:--|
| `call_parameter:a` | 1 |
| `call_parameter:b` | 1 |
| `call_parameter:bizz` | 5 |
| `call_parameter:buzz` | 5 |
| `call_parameter:c` | 1 |
| `call_parameter:x` | 3, 4 |

--------------------------------------------------------------------------------

#### Construct `method_call`

##### Definition

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/func/_type='Attribute'
\n(?:\1.+\n)*?\1/func/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/func/attr='(?P<SUFFIX>.+)'
```

##### Example

```python
1   seq.index(42)
2   foo(bar)  # no match
3   seq.index # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `method_call:index` | 1 |

--------------------------------------------------------------------------------

#### Construct `method_call_object`

##### Definition

```re
           ^(.*)/value/_type='Call'
\n(?:\1.+\n)*?\1/value/func/_type='Attribute'
\n(?:\1.+\n)*?\1/value/func/value/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/value/func/value/id='(?P<SUFFIX>.+)'
```

##### Example

```python
1   seq.index(42)
2   foo(bar)  # no match
3   seq.index # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `method_call_object:seq` | 1 |

--------------------------------------------------------------------------------

#### Construct `method_chaining`

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

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

#### Construct `assignment`

##### Definition

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

##### Definition

```re
           ^(.*)/_type='AugAssign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   a += 1
2   a = a + 1
3   a += b
4   a *= foo(bar(a, b, c))
5   a[3] += 1
6   a[b] //= 2
7   a += [x]
```

##### Matches

| Label | Lines |
|:--|:--|
| `augmented_assignment` | 1, 3, 4, 5, 6, 7 |

--------------------------------------------------------------------------------

#### Construct `chained_assignment`

##### Definition

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/assigntargets/length=(?!1\n).+
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

#### Construct `assignment_lhs_identifier`

Capture any identifier appearing on the left hand side of an assignment (possibly augmented).

##### Definition

```re
^(.*/assigntarget(s/\d+)?(|/value|/elts/\d+|/elts/\d+/value))/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1                                             /id='(?P<SUFFIX>.+)'
```

##### Example

```python
1   _ = 1
2   a = 1
3   (b, c) = (1, 1)
4   [d, e] = [1, 1]
5   f[g] = 1            # no match for g
6   if foo:
7       h = 1
8   def bar():
9       i = 1
10  j = k = 1
11  l.m = 1             # LIMITATION: no match for m
12  (n, *o) = [1, 1, 1]
13  a += 1
14  f[g] += 1            # no match for g
15  for i in seq:        # no match for i
16      pass
17  del a                # no match for a
18  first = second = third
```

##### Matches

| Label | Lines |
|:--|:--|
| `assignment_lhs_identifier:_` | 1 |
| `assignment_lhs_identifier:a` | 2, 13 |
| `assignment_lhs_identifier:b` | 3 |
| `assignment_lhs_identifier:c` | 3 |
| `assignment_lhs_identifier:d` | 4 |
| `assignment_lhs_identifier:e` | 4 |
| `assignment_lhs_identifier:f` | 5, 14 |
| `assignment_lhs_identifier:h` | 7 |
| `assignment_lhs_identifier:i` | 9 |
| `assignment_lhs_identifier:j` | 10 |
| `assignment_lhs_identifier:k` | 10 |
| `assignment_lhs_identifier:l` | 11 |
| `assignment_lhs_identifier:n` | 12 |
| `assignment_lhs_identifier:o` | 12 |
| `assignment_lhs_identifier:first` | 18 |
| `assignment_lhs_identifier:second` | 18 |

--------------------------------------------------------------------------------

#### Construct `assignment_rhs_identifier`

Capture any identifier (variable or function) appearing on the right hand side of an assignment (possibly augmented).

##### Definition

```re
^(.*/assignvalue\b.*)/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1     /id='(?P<SUFFIX>.+)'
```

##### Example

```python
1   a = a + b + c
2   a += a + b + c
3   a = a[b[c]]
4   a += a[b[c]]
5   a = foo(bar())
6   a += foo(bar())
7   a = a + i
8   a += i
9   a[i] = b
10  first = second = third
```

##### Matches

| Label | Lines |
|:--|:--|
| `assignment_rhs_identifier:a` | 1, 2, 3, 4, 7 |
| `assignment_rhs_identifier:b` | 1, 2, 3, 4, 9 |
| `assignment_rhs_identifier:bar` | 5, 6 |
| `assignment_rhs_identifier:c` | 1, 2, 3, 4 |
| `assignment_rhs_identifier:foo` | 5, 6 |
| `assignment_rhs_identifier:i` | 7, 8 |
| `assignment_rhs_identifier:third` | 10 |

--------------------------------------------------------------------------------

### Assignment idioms

--------------------------------------------------------------------------------

#### Construct `swapping`

Swap two variables or two elements of an array with a 2-element tuple or list.

##### Definition

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/assigntargets/0/elts/length=2
\n(?:\1.+\n)*?\1/assigntargets/0/elts/0/_hash=(?P<HASH_A>.+)
\n(?:\1.+\n)*?\1/assigntargets/0/elts/1/_hash=(?P<HASH_B>.+)
\n(?:\1.+\n)*?\1/assignvalue/elts/length=2
\n(?:\1.+\n)*?\1/assignvalue/elts/0/_hash=(?P=HASH_B)
\n(?:\1.+\n)*?\1/assignvalue/elts/1/_hash=(?P=HASH_A)
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

##### Definition

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/assigntargets/0/_hash=(?P<HASH>.+) # capture hash
\n(?:\1.+\n)*?\1/assignvalue/_type='UnaryOp'
\n(?:\1.+\n)*?\1/assignvalue/op/_type='USub'
\n(?:\1.+\n)*?\1/assignvalue/operand/_hash=(?P=HASH) # match hash
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

##### Definition

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

#### Construct `function_returning_a_value`

A function returns a value iff it contains a statement `return` and the returned value is not `None`.

##### Definition

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)'
\n(?:\1.+\n)* \1/(?P<_1>.+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)   /value/lineno=(?P<LINE>\d+)
\n            \1/(?P=_1)   /value/.+(?<!value=None)$
(   # capture the line number of the last line of the function (it may appear before Return)
\n(?:\1.+\n)* \1.+/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   def foo(bar):
2       if a:
3           return b
4       print(c)
5       return None
6
7   def bar(foo):
8       if a:
9           return None
10      print(c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_returning_a_value:foo` | 1-5 |

--------------------------------------------------------------------------------

#### Construct `procedure`

##### Definition

```sql
SELECT "procedure",
       name_suffix,
       span
FROM t
WHERE name_prefix = "function"
  AND span NOT IN
    (SELECT span
     FROM t
     WHERE name_prefix = "function_returning_a_value" )
```

**Explanation.** Select all functions whose span is not that of a function returning a value.

##### Example

```python
1   def foo(bar):
2       if a:
3           return b
4       print(c)
5       return None
6
7   def bar(foo):
8       if a:
9           return None
10      print(c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `procedure:bar` | 7-10 |

--------------------------------------------------------------------------------

#### Construct `function_with_default_positional_arguments`

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

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
\n(?:\1.+\n)* \1/(?P=_1)                 /(?P=_2)    /(?P=_3)   /func/id='(?P=SUFFIX)'
\n(?:\1.+\n)*?\1/(?P=_1)                 /(?!(?P=_2)).+
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
14              return 1 + recurs(candidates[1:]) # body call
15          return recurs(candidates[1:]) # tail call
16      return recurs(range(1, n+1))
17
18  def place(x = 1, y = 1, queens = []):
19      if x > SIZE:
20          print(queens)
21      else:
22          if possible(x, y, queens):
23              place(x + 1, 1, queens + [(x, y)]) # body call
24          if y < SIZE:
25              place(x, y + 1, queens) # tail call
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

##### Definition

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

##### Definition

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

##### Definition

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

Match an entire conditional (from the `if` clause to the last line of its body).

##### Definition

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/.+/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   if condition_1:     # match
2       if condition_2: # |     match
3           pass        # |     |
4   elif condition_3:   # |     match: cf. remark
5       if condition_4: # |     |     match
6           pass        # |     |     |
7   else:               # |     |
8       if condition_5: # |     |     match
9           pass        # |     |     |
10      pass            # |     |
```

*Remark.* There is no such thing as an `elif` clause in the AST. Consequently, this code has the same representation as:

```python
if condition_1:
    if condition_2:
        pass
else:
    if condition_3:
        if condition_4:
            pass
    else:
        if condition_5:
            pass
        pass
```

... which should help figure out why the `elif` of line 4 counts as a regular `if`.

##### Matches

| Label | Lines |
|:--|:--|
| `if` | 1-10, 2-3, 4-10, 5-6, 8-9 |

--------------------------------------------------------------------------------

#### Construct `if_test_id`

Match any identifier present in the condition of an `if` statement.

##### Definition

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
(
\n(?:\1.+\n)*?\1/test/.+/id='(?P<SUFFIX>.+)'
)+
```

##### Example

```python
1   if foo(bar) == biz:
2       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `if_test_id:bar` | 1 |
| `if_test_id:biz` | 1 |
| `if_test_id:foo` | 1 |

--------------------------------------------------------------------------------

#### Construct `if_then_branch`

Match the body of the branch “`then`” of an `if` statement.

##### Definition

```re
(^  # capture any body block
                   .*/body/\d+
|   # capture any orelse block whose length is greater than 1
    (?<!length=1\n).*/orelse/\d+
)
                /_type='If'
\n(?:\1.+\n)*?\1/body/0/lineno=(?P<LINE>\d+)
(
\n(?:\1.+\n)* \1/body/.*/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   if condition_1:
2       pass             # match
3   elif condition_2:
4       pass             # no match: this is an elif branch
5   else:
6       pass             # no match: this is an else branch
7
8   if condition_3:
9       pass             # match
10  else:
11      if condition_4:
12          pass         # match: there are 2 statements in the else clause of line 10
13          pass         # |
14      pass
15
16  if condition_5:
17      pass             # match
18      pass             # |
19  else:
20      if condition_4:  # no match: this is an elif branch in disguise
21          pass
22          pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `if_then_branch` | 2, 9, 12-13, 17-18 |

--------------------------------------------------------------------------------

#### Construct `if_elif_branch`

Match the body of an `elif` clause, which is (or could be rewritten as) an `else` branch consisting in a single statement `if`.

##### Definition

```re
           ^(.*)/orelse/length=1
\n(?:\1.+\n)*?\1/orelse/0/_type='If'
\n(?:\1.+\n)*?\1/orelse/0/body/0/lineno=(?P<LINE>\d+)
(
\n(?:\1.+\n)* \1/orelse/0/body/.+/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   if condition_1:
2       if condition_2:
3           pass
4   elif condition_3:
5       if condition_4: # match
6           pass        # |
7   elif condition_5:
8       pass            # match
9       pass            # |
10  else:
11      if condition_6:
12          pass        # no match
13      pass            # ... since this else branch has more than one statement
14
15  if condition_7:
16      pass
17  else:
18      if condition_8:
19          pass        # match: this is an elif in disguise
20
21  for foo in bar:
22      if condition_9:
23          break
24  else:
25      if condition_10:
26          pass        # no match
```

*Remark.* Lines 17-18 could/should be rewritten as `elif condition_8`. This results in a span of `19` for the implicit `elif`.

##### Matches

| Label | Lines |
|:--|:--|
| `if_elif_branch` | 5-6, 8-9, 19 |

--------------------------------------------------------------------------------

#### Construct `if_else_branch`

Match the body of the possible branch `else` of an `if` statement.

##### Definition

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/orelse/length=
(   # there is at least two statements in the else branch,
                               \d+(?<![01])
\n(?:\1.+\n)*?\1/orelse/0/lineno=(?P<LINE>\d+)
|   # or only one, but distinct from If (otherwise, this is an elif)
                               1
\n(?:\1.+\n)*?\1/orelse/0/_type='.+?(?<!If)'
\n(?:\1.+\n)*?\1/orelse/0/lineno=(?P<LINE>\d+)
)
(
\n(?:\1.+\n)* \1/orelse/.+/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   if condition_1:
2       if condition_2:
3           pass
4   elif condition_3: # no match: this is an elif
5       if condition_4:
6           pass
7   else:
8       if condition_5: # match
9           pass        # |
10      else:           # |
11          pass        # |      match
12      pass            # |
13
14  for foo in bar:
15      if condition_6:
16          break
17  else:
18      pass # no match for a loop else
```

##### Matches

| Label | Lines |
|:--|:--|
| `if_else_branch` | 8-12, 11 |

--------------------------------------------------------------------------------

#### Construct `nested_if`

Match an `if` clause nested in _n_ other `if` clauses, suffixing it by _n_.

##### Definition

```sql
SELECT "nested_if",
       count(*),
       inner_if.span
FROM t outer_if
JOIN t inner_if ON (outer_if.span_start <= inner_if.span_start
                    AND inner_if.span_end <= outer_if.span_end)
WHERE outer_if.name_prefix IN ("if_then_branch",
                               "if_else_branch",
                               "if_elif_branch")
  AND inner_if.name_prefix = "if"
GROUP BY inner_if.span
ORDER BY inner_if.span_start
```

##### Example

```python
1   if condition_1:
2       if condition_2:     # match
3           if condition_3: # |        match (nesting depth = 2)
4               pass        # |        |
5   else:
6       if condition_4:     # match
7           pass            # |
8       if condition_5:     # match
9           pass            # |
10
11  if condition_6:
12      pass
13  elif condition_7:
14      pass
15
16  if condition_8:
17      for foo in bar:
18          if condition_9: # match
19              pass        # |
```

##### Matches

| Label | Lines |
|:--|:--|
| `nested_if:1` | 2-4, 6-7, 8-9, 18-19 |
| `nested_if:2` | 3-4 |

--------------------------------------------------------------------------------

## Iterations

--------------------------------------------------------------------------------

#### Construct `for`

Match sequential loops, along with their iteration variable(s).

##### Definition

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/target/_ids=(?P<SUFFIX>.+)
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   for x in seq_1:
2       for y in range(len(seq_3)):
3           pass
4       for (a, (b, c)) in seq_2:
5           pass
6       else:
7           pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `for:a:b:c` | 4-7 |
| `for:x` | 1-7 |
| `for:y` | 2-3 |

--------------------------------------------------------------------------------

#### Construct `for_each`

Iterate over the elements of a (named) collection.

##### Definition

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/iter/_type='Name'
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

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

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

##### Definition

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

Match a `for` statement nested in _n_ other `for` statements, suffixing it by _n_.

##### Definition

```sql
SELECT "nested_for",
       count(*),
       inner_loop.span
FROM t outer_loop
JOIN t inner_loop ON (outer_loop.span_start <= inner_loop.span_start
                      AND inner_loop.span_end <= outer_loop.span_end
                      AND inner_loop.rowid != outer_loop.rowid)
WHERE outer_loop.name_prefix = "for"
  AND inner_loop.name_prefix = "for"
GROUP BY inner_loop.span
ORDER BY inner_loop.span_start
```

##### Example

```python
1   for x_1 in seq_1:
2       for x_2 in seq_2:
3           pass
4           for x_3 in seq_3:
5               pass
6       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `nested_for:1` | 2-5 |
| `nested_for:2` | 4-5 |

--------------------------------------------------------------------------------

#### Construct `triangular_nested_for`

A `for` loop with a counter `i` and a nested `for` loop which makes `i` iterations. The total number of iterations is a [triangular number](https://en.wikipedia.org/wiki/Triangular_number).

##### Definition

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

##### Definition

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

#### Construct `while`

##### Definition

```re
           ^(.*)/_type='While'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   while foo():
2       while bar():
3           pass
4       while biz():
5           pass
6       else:
7           pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `while` | 1-7, 2-3, 4-7 |

--------------------------------------------------------------------------------

## Exceptions

--------------------------------------------------------------------------------

#### Construct `assertion`

##### Definition

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

#### Construct `try`

##### Definition

```re
           ^(.*)/_type='Try'
\n(?:\1.+\n)* \1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/.*/lineno=(?P<LINE>\d+)
```

##### Example

```python
1   try:
2       try:
3           raise e1
4       except e1:
5           raise e2
6   except e2:
7       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `try` | 1-7, 2-5 |

--------------------------------------------------------------------------------

#### Construct `raise`

##### Definition

```re
           ^(.*)/_type='Raise'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/exc(=(?P<SUFFIX>None)|/.*\bid='(?P<SUFFIX>.+)')
```

##### Example

```python
1   try:
2       if n < 0:
3           raise ValueLessThanZero
4       elif n < min_threshold:
5           raise ValueTooSmallError
6       elif n > max_threshold:
7           raise ValueTooLargeError(argument)
8       elif n == 0:
9           raise
10  except ValueLessThanZero:
11      pass
12  except ValueTooSmallError(a):
13      pass
14  except (e1, e2):
15      pass
16  except:
17      pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `raise:None` | 9 |
| `raise:ValueLessThanZero` | 3 |
| `raise:ValueTooLargeError` | 7 |
| `raise:ValueTooSmallError` | 5 |

--------------------------------------------------------------------------------

#### Construct `except`

##### Definition

```re
           ^(.*)/(?P<_1>handlers/\d+/(type/(func/|elts/\d+/)?)?)lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)                                        (id='(?P<SUFFIX>.+)'|type=(?P<SUFFIX>None))
```

##### Example

```python
1   try:
2       if n < 0:
3           raise ValueLessThanZero
4       elif n < min_threshold:
5           raise ValueTooSmallError
6       elif n > max_threshold:
7           raise ValueTooLargeError(argument)
8       elif n == 0:
9           raise
10  except ValueLessThanZero:
11      pass
12  except ValueTooSmallError(a):
13      pass
14  except (e1, e2):
15      pass
16  except:
17      pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `except:None` | 16 |
| `except:ValueLessThanZero` | 10 |
| `except:ValueTooSmallError` | 12 |
| `except:e1` | 14 |
| `except:e2` | 14 |

--------------------------------------------------------------------------------

#### Constructs `try_raise|try_except`

##### Definition

```sql
SELECT "try_" || e.name_prefix,
       e.name_suffix,
       max(t.span_start) || "-" || min(t.span_end)
FROM t t
JOIN t e ON (t.span_start <= e.span_start
             AND e.span_end <= t.span_end)
WHERE t.name_prefix = "try"
  AND e.name_prefix IN ("raise",
                        "except")
GROUP BY e.rowid
```

##### Example

```python
1   try:
2       try:
3           raise e1
4       except e1:
5           pass
6       raise e2
7   except e3:
8       pass
9   try:
10      raise e1
11  except e1:
12      pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `try_except:e1` | 2-5, 9-12 |
| `try_except:e3` | 1-8 |
| `try_raise:e1` | 2-5, 9-12 |
| `try_raise:e2` | 1-8 |

--------------------------------------------------------------------------------

## Modules

--------------------------------------------------------------------------------

#### Construct `import_module`

##### Definition

```re
           ^(.*)/_type='Import(From)?'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
(
\n(?:\1.+\n)*?\1/module='(?P<SUFFIX>.+)'
|
(
\n(?:\1.+\n)*?\1/names/\d+/name='(?P<SUFFIX>.+)'
)+
)
```

##### Example

```python
1   import m1, m2, m3
2   import m4
3   from m5 import n1, n2
4   from m6 import n3 as n4
5   from . import m7
6   from .m8 import n5
```

##### Matches

| Label | Lines |
|:--|:--|
| `import_module:m1` | 1 |
| `import_module:m2` | 1 |
| `import_module:m3` | 1 |
| `import_module:m4` | 2 |
| `import_module:m5` | 3 |
| `import_module:m6` | 4 |
| `import_module:m7` | 5 |
| `import_module:m8` | 6 |

--------------------------------------------------------------------------------

#### Construct `import_name`

##### Definition

```re
           ^(.*)/_type='ImportFrom'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/module='.+'
(
\n(?:\1.+\n)*?\1/names/\d+/name='(?P<SUFFIX>.+)'
)+
```

##### Example

```python
1   import m1, m2, m3
2   import m4
3   from m5 import n1, n2
4   from m6 import n3 as n4
5   from . import m7
6   from .m8 import n5
```

##### Matches

| Label | Lines |
|:--|:--|
| `import_name:n1` | 3 |
| `import_name:n2` | 3 |
| `import_name:n3` | 4 |
| `import_name:n5` | 6 |

--------------------------------------------------------------------------------

#### Construct `import`

Suffixed by the imported module and, if any, the imported name. In most cases, could replace the two low-level constructs `import_module` and `import_name`.

##### Definition

```sql
SELECT "import",
       m.name_suffix || (CASE
                             WHEN n.name_suffix IS NULL THEN ""
                             ELSE ":" || n.name_suffix
                         END),
       m.span
FROM t m
LEFT JOIN t n ON (m.span = n.span
                  AND n.name_prefix = "import_name")
WHERE m.name_prefix = "import_module"
```

##### Example

```python
1   import m1, m2, m3
2   import m4
3   from m5 import n1, n2
4   from m6 import n3 as n4
5   from . import m7
6   from .m8 import n5
```

##### Matches

| Label | Lines |
|:--|:--|
| `import:m1` | 1 |
| `import:m2` | 1 |
| `import:m3` | 1 |
| `import:m4` | 2 |
| `import:m5:n1` | 3 |
| `import:m5:n2` | 3 |
| `import:m6:n3` | 4 |
| `import:m7` | 5 |
| `import:m8:n5` | 6 |

--------------------------------------------------------------------------------

# Code patterns

## Iterative patterns

### Sequential loops

--------------------------------------------------------------------------------

#### Construct `accumulate_elements`

An accumulator is iteratively updated from its previous value and those of the iteration variable.

##### Definition

```sql
SELECT "accumulate_elements",
       count(DISTINCT acc_left.name_suffix),
       for_loop.span
FROM t for_loop -- Ensure iter_var, acc_left and acc_right have same span and are inside the loop.
JOIN t iter_var ON (for_loop.span_start <= iter_var.span_start
                    AND iter_var.span_end <= for_loop.span_end)
JOIN t acc_left ON (iter_var.span = acc_left.span)
JOIN t acc_right ON (acc_left.span = acc_right.span)
WHERE for_loop.name_prefix = "for" -- A for loop...
  AND for_loop.name_suffix = iter_var.name_suffix -- whose iteration variable...
  AND ((iter_var.name_prefix = "assignment_rhs_identifier" -- either appears on the RHS of an assignment...
        AND (acc_left.name_prefix = "augmented_assignment" -- (which is either augmented...
             OR (acc_left.name_suffix = acc_right.name_suffix -- or references the same identifier...
                 AND acc_left.name_prefix = "assignment_lhs_identifier" -- on both left...
                 AND acc_right.name_prefix = "assignment_rhs_identifier")))-- and right hand size)...
       OR (iter_var.name_prefix = "call_parameter" -- or appears as an argument...
           AND acc_right.name_prefix = "method_call" -- of a call to a method...
           AND acc_right.name_suffix IN ("append",
                                         "extend",
                                         "insert",
                                         "add",
                                         "update")-- updating its object.
           AND acc_left.name_prefix = "method_call_object" -- Ensure that the suffix is the accumulator...
 ))
  AND for_loop.name_suffix != acc_left.name_suffix -- and is distinct from the iteration variable.
GROUP BY for_loop.span
ORDER BY for_loop.span_start
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
8       acc_1 = combine(acc_1, i)
9       if condition:
10           acc_2 += i
11      else:
12          acc_2 *= i
13      pass
14  for i in range(10):
15      acc += foo(bar, i)
16  for i in range(10): # no match
17      foo(acc, bar, i)
18      pass
19  for i in range(10):
20      acc.append(i)
21      pass
22  for i in range(10): # no match
23      print(foobar, i)
24  for c in string:
25      c = c.upper() # no match: this is the iteration variable, not an accumulator
26      print(c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `accumulate_elements:1` | 3-5, 14-15, 19-21 |
| `accumulate_elements:2` | 7-13 |

--------------------------------------------------------------------------------

#### Construct `filter_for`

An accumulation pattern that, from a given collection, returns a list containing only those elements that verify a certain condition.

##### Definition

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

##### Definition

```re
           ^(.*)/(?P<_1>(?:body|orelse)/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_1)                /assigntargets/0/id='(?P<CANDIDATE>.+)' # capture candidate
\n(?:\1.+\n)* \1/(?P<_2>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_2)                /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_2)                /target/id='(?P<ITER_VAR>.+)' # capture iteration variable
\n(?:\1.+\n)* \1/(?P=_2)                /(?P<_3>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /test/_ids=(?=.*?\b(?P=ITER_VAR)\b)
                                                                               (?=.*?\b(?P=CANDIDATE)\b)
                                                                               .* # match both
\n(?:\1.+\n)* \1/(?P=_2)                /(?P=_3)                    /test/.*/id='(?P=CANDIDATE)' # match candidate
\n(?:\1.+\n)* \1/(?P=_2)                /(?P=_3)                    /(?P<_4>(?:body|orelse)/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /(?P=_4)                /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /(?P=_4)                /assigntargets/0/id='(?P=CANDIDATE)' # match candidate
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /(?P=_4)                /assignvalue/id='(?P=ITER_VAR)' # match iteration variable
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

Check whether all elements of a collection satisfy a predicate.

##### Definition

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

Check whether any element of a collection satisfies a predicate.

##### Definition

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

##### Definition

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

##### Definition

```re
           ^(.*)/_type='While'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/test/.*/id='(?P<STATE>.+)' # capture state variable
(   # the state variable either appears on both sides of a simple assignment
\n(?:\1.+\n)* \1/(?P<_1>body/.*)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_1)        /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)        /assigntargets/0/id='(?P=STATE)' # it is updated somewhere in the loop
\n(?:\1.+\n)*?\1/(?P=_1)        /assignvalue/_ids=.*\b(?P=STATE)\b.* # from its current value
|   # or appears on LHS of an augmented assignement
\n(?:\1.+\n)* \1/(?P<_1>body/.*)/_type='AugAssign'
\n(?:\1.+\n)*?\1/(?P=_1)        /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)        /assigntarget/id='(?P=STATE)' # it is augmented somewhere in the loop
|   # or is mutated by calling a function or a method of this variable
\n(?:\1.+\n)* \1/(?P<_1>body/.*)/_type='Expr'
\n(?:\1.+\n)*?\1/(?P=_1)        /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_1)        /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)        /value/.*/id='(?P=STATE)' # it is mutated somewhere in the loop
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

##### Definition

```re
           ^(.*)/_type='While'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/test/value=True
\n(?:\1.+\n)* \1/(?:body|orelse)/\d+/assigntargets/.+/id='(?P<INPUT>.+)' # capture the name of the input
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_1)                /test/_ids=.*?\b(?P=INPUT)\b.* # the input is tested
\n(?:\1.+\n)* \1/(?P=_1)                /(?P<_2>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)                /(?P=_2)                    /value/id='(?P<ACC>.+)' # capture the name of the accumulator
(   # the accumulator either appears on both sides of a simple assignment with the input
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='(?P<SUFFIX>Assign)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)* \1/(?P=_3)                    /assigntargets/.*/id='(?P=ACC)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /assignvalue/_ids=(?=.*\b(?P=INPUT)\b)
                                                        (?=.*\b(?P=ACC)\b)
                                                        .* # both appear in RHS
|   # or is on LHS of an augmented assignement with the input
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='(?P<SUFFIX>AugAssign)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_3)                    /assigntarget/id='(?P=ACC)'
\n(?:\1.+\n)* \1/(?P=_3)                    /assignvalue.*/id='(?P=INPUT)'
|   # or should be mutated by calling a function on this accumulator and the iteration variable
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_3)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_ids=(?=.*\b(?P=INPUT)\b)
                                                        (?=.*\b(?P=ACC)\b)
                                                        .+ # both appear in RHS
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/_type='(?P<SUFFIX>Name)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/id='(?!(?P=ACC)|(?P=INPUT)|breakpoint|delattr|eval|exec|help|input|open|print|setattr|super).+'
|   # or should be mutated by calling a method of this accumulator, again on the iteration variable
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_3)                    /lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/_type='(?P<SUFFIX>Attribute)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/value/id='(?P=ACC)' # a method of acc is called on...
\n(?:\1.+\n)* \1/(?P=_3)                    /value/args/\d+/id='(?P=INPUT)' # the iteration variable
)
(
\n(?:\1.+\n)* \1.*/lineno=(?P<LINE>\d+)
)?
```

##### Example

```python
1   def accumulate_inputs():
2       acc = seed
3       while True:
4           x = read()
5           if is_sentinel(x, y):
6               return acc
7           acc = combine(x, acc)
8
9   def accumulate_inputs():
10      acc = seed
11      while True:
12          x = read()
13          if x > y:
14              return acc
15          acc += abs(x)
16
17  def accumulate_inputs():
18      acc = seed
19      while True:
20          x = read()
21          if x > y:
22              return acc
23          foobar(acc, x)
24
25  def accumulate_inputs():
26      acc = seed
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

# Programs

--------------------------------------------------------------------------------

#### Construct `category`

It may be interesting to indicate the category of the program with an all-encompassing hint `# paroxython: category` placed on its own line. Examples of possible categories are:

- `abstract`: sorting, searching, algorithmic pattern, etc.
- `biology`
- `combinatorics`
- `computability`: cellular automata, tag-system, etc.
- `fractals`
- `fun`
- `game`
- `geography`
- `geometry`
- `number_theory`: gcd, sieve, most problems of [Project Euler](http://projecteuler.net), etc.
- `text_processing`
- ...

##### Definition

```
```

##### Example

```python
1   print("See if you can do this. Read each line aloud and press Return between.")
2   message = "this is how to keep an idiot busy for a while"
3   for word in message.split(" "):
4       # paroxython: category:text_processing
5       input(f"This is {word} cat.")
6   print("Now read the third word in each line from the top!")
7   # paroxython: category:fun
```

**Remarks.**
- The location of an all-encompassing hint does not matter, as long as it is on its own line.
- Since all hints are stripped before labelling, the resulting source actually spans from line 1 to line 5.

##### Matches

| Label | Lines |
|:--|:--|
| `category:fun` | 1-5 |
| `category:text_processing` | 1-5 |

--------------------------------------------------------------------------------

# Suggestions

These patterns match constructs that can be shortened.
It's up to you to decide if a rewriting would make the code clearer.

## Assignments

--------------------------------------------------------------------------------

#### Construct `suggest_conditional_expression`

When a conditional simply assigns different values to the same variable, it may be rewritten as a conditional expression.

##### Definition

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/body/length=1
\n(?:\1.+\n)*?\1/body/0/_type='Assign'
\n(?:\1.+\n)*?\1/body/0/assigntargets/0/_hash=(?P<HASH>.+)
\n(?:\1.+\n)*?\1/orelse/length=1
\n(?:\1.+\n)*?\1/orelse/0/_type='Assign'
\n(?:\1.+\n)*?\1/orelse/0/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/orelse/0/assigntargets/0/_hash=(?P=HASH)
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

##### Definition

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/assigntargets/length=1
\n(?:\1.+\n)*?\1/assigntargets/0/id=(?P<TARGET>.+)
\n(?:\1.+\n)*?\1/assignvalue/_type='BinOp'
\n(?:\1.+\n)*?\1/assignvalue/left/id=(?P=TARGET)
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

##### Definition

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

##### Definition

```re
  ^(/(?:body|orelse)/\d+)
(   # indented lines
              /(?P<_1>(?:body|orelse)/.+)/lineno=(?P<LINE>\d+)
\n          \1/(?P=_1)                   /n=(?!(-1|0|1|2)\n)
|   # non indented lines
              /_type='Assign'
\n(?:\1.+\n)*?\1/lineno=(?P<LINE>\d+)
\n(?:\1.+\n)*?\1/assigntargets/0/id='.*?[a-z].*' # at least one lowercase letter
\n(?:\1.+\n)*?\1/assignvalue/n=(?!(-1|0|1|2)\n)
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

##### Definition

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
