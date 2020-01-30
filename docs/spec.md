- [Expressions](#expressions)
  - [Literals](#literals)
      - [Feature `literal`](#feature-literal)
      - [Feature `int_literal`](#feature-int_literal)
      - [Feature `float_literal`](#feature-float_literal)
      - [Feature `imaginary_literal`](#feature-imaginary_literal)
  - [Subscripts](#subscripts)
      - [Feature `index`](#feature-index)
      - [Feature `index_arithmetic`](#feature-index_arithmetic)
      - [Feature `negative_index`](#feature-negative_index)
      - [Feature `slice`](#feature-slice)
      - [Feature `slice_step`](#feature-slice_step)
  - [Operators](#operators)
      - [Feature `unary_operator`](#feature-unary_operator)
      - [Feature `binary_operator`](#feature-binary_operator)
      - [Feature `conditional_expression`](#feature-conditional_expression)
  - [Boolean expressions](#boolean-expressions)
      - [Feature `boolean_operator`](#feature-boolean_operator)
      - [Feature `comparison_operator`](#feature-comparison_operator)
      - [Feature `chained_comparison`](#feature-chained_comparison)
      - [Feature `chained_equalities|chained_inequalities` (SQL)](#feature-chained_equalitieschained_inequalities)
      - [Feature `divisibility_test`](#feature-divisibility_test)
      - [Feature `short_circuit`](#feature-short_circuit)
  - [Calls](#calls)
      - [Feature `function_call`](#feature-function_call)
      - [Feature `function_tail_call`](#feature-function_tail_call)
      - [Feature `call_argument`](#feature-call_argument)
      - [Feature `method_call`](#feature-method_call)
      - [Feature `method_call_object`](#feature-method_call_object)
      - [Feature `method_chaining`](#feature-method_chaining)
      - [Feature `composition`](#feature-composition)
  - [Anonymous functions](#anonymous-functions)
      - [Feature `lambda_function`](#feature-lambda_function)
  - [Iterables](#iterables)
      - [Feature `range` (SQL)](#feature-range)
      - [Feature `comprehension`](#feature-comprehension)
      - [Feature `comprehension_for_count`](#feature-comprehension_for_count)
      - [Feature `filtered_comprehension`](#feature-filtered_comprehension)
- [Statements](#statements)
  - [Assignments](#assignments)
      - [Feature `assignment`](#feature-assignment)
      - [Feature `augmented_assignment`](#feature-augmented_assignment)
      - [Feature `chained_assignment`](#feature-chained_assignment)
      - [Feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)
      - [Feature `assignment_rhs_identifier`](#feature-assignment_rhs_identifier)
    - [Assignment idioms](#assignment-idioms)
      - [Feature `swapping`](#feature-swapping)
      - [Feature `negation`](#feature-negation)
  - [Function definitions](#function-definitions)
    - [Interface](#interface)
      - [Feature `function`](#feature-function)
      - [Feature `return`](#feature-return)
      - [Feature `yield`](#feature-yield)
      - [Feature `generator` (SQL)](#feature-generator)
      - [Feature `function_returning_something` (SQL)](#feature-function_returning_something)
      - [Feature `function_returning_nothing` (SQL)](#feature-function_returning_nothing)
      - [Feature `function_with_default_positional_arguments`](#feature-function_with_default_positional_arguments)
    - [Nesting](#nesting)
      - [Feature `nested_function`](#feature-nested_function)
      - [Feature `closure` (SQL)](#feature-closure)
    - [Recursion](#recursion)
      - [Feature `recursive_function` (SQL)](#feature-recursive_function)
      - [Feature `deeply_recursive_function` (SQL)](#feature-deeply_recursive_function)
      - [Feature `body_recursive_function` (SQL)](#feature-body_recursive_function)
      - [Feature `tail_recursive_function` (SQL)](#feature-tail_recursive_function)
  - [Conditionals](#conditionals)
      - [Feature `if`](#feature-if)
      - [Feature `if_test_id`](#feature-if_test_id)
      - [Feature `if_then_branch`](#feature-if_then_branch)
      - [Feature `if_elif_branch`](#feature-if_elif_branch)
      - [Feature `if_else_branch`](#feature-if_else_branch)
      - [Feature `nested_if` (SQL)](#feature-nested_if)
  - [Iterations](#iterations)
      - [Feature `for`](#feature-for)
      - [Feature `for_each`](#feature-for_each)
      - [Feature `for_range` (SQL)](#feature-for_range)
      - [Feature `for_indexes_elements`](#feature-for_indexes_elements)
      - [Feature `for_indexes`](#feature-for_indexes)
      - [Feature `nested_for` (SQL)](#feature-nested_for)
      - [Feature `triangular_nested_for`](#feature-triangular_nested_for)
      - [Feature `square_nested_for`](#feature-square_nested_for)
      - [Feature `while`](#feature-while)
  - [Exceptions](#exceptions)
      - [Feature `assertion`](#feature-assertion)
      - [Feature `try`](#feature-try)
      - [Feature `raise`](#feature-raise)
      - [Feature `except`](#feature-except)
      - [Feature `try_raise|try_except` (SQL)](#feature-try_raisetry_except)
  - [Modules](#modules)
      - [Feature `import_module`](#feature-import_module)
      - [Feature `import_name`](#feature-import_name)
      - [Feature `import` (SQL)](#feature-import)
- [Code patterns](#code-patterns)
  - [Iterative patterns](#iterative-patterns)
    - [Sequential loops](#sequential-loops)
      - [Feature `accumulate_elements` (SQL)](#feature-accumulate_elements)
      - [Feature `filter_for`](#feature-filter_for)
      - [Feature `find_best_element`](#feature-find_best_element)
      - [Feature `universal_quantifier`](#feature-universal_quantifier)
      - [Feature `existential_quantifier`](#feature-existential_quantifier)
      - [Feature `find_first_element`](#feature-find_first_element)
    - [Non sequential finite loops](#non-sequential-finite-loops)
      - [Feature `evolve_state`](#feature-evolve_state)
    - [Non sequential infinite loops](#non-sequential-infinite-loops)
      - [Feature `accumulate_stream`](#feature-accumulate_stream)
- [Programs](#programs)
      - [Feature `category`](#feature-category)
- [Suggestions](#suggestions)
  - [Assignments](#assignments-1)
      - [Feature `suggest_conditional_expression`](#feature-suggest_conditional_expression)
      - [Feature `suggest_augmented_assignment`](#feature-suggest_augmented_assignment)
  - [Expressions](#expressions-1)
      - [Feature `suggest_comparison_chaining`](#feature-suggest_comparison_chaining)
      - [Feature `suggest_constant_definition`](#feature-suggest_constant_definition)
  - [Subroutines](#subroutines)
      - [Feature `suggest_condition_return`](#feature-suggest_condition_return)

# Expressions

## Literals

--------------------------------------------------------------------------------

#### Feature `literal`

##### Specification

```re
^(.*)
(   # match None, True and False
              /_type='NameConstant'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value=(?P<SUFFIX>None|True|False)
|   # match any other constant
              /_type='(?P<SUFFIX>Str|Num|Tuple|Dict|Set|List)'
\n(?:\1.+\n)*?\1/_ids=
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `int_literal`

Matching literal does not require to feature a sophisticated regular expression: the heavy lifting is already made in the given AST, which stores them in a normalized form. For instance, integer literals are just sequence of digits:

##### Specification

```re
           ^(.*)/_type='Num'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `float_literal`

In the AST, a floating point literal consists of digits and at least one symbol among `.` and `e`.

##### Specification

```re
           ^(.*)/_type='Num'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/n=.*?[e\.].*(?<!j)\n
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
| `float_literal` | 3, 3, 3, 3, 3, 3, 3 |

--------------------------------------------------------------------------------

#### Feature `imaginary_literal`

In the AST, an imaginary literal contains the same symbols as a floating point literal, plus a mandatory trailing symbol `j`.

##### Specification

```re
           ^(.*)/_type='Num'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/n=.*j\n
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
| `imaginary_literal` | 4, 4, 4, 4, 4, 4, 4 |

--------------------------------------------------------------------------------

## Subscripts

--------------------------------------------------------------------------------

#### Feature `index`

##### Specification

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `index_arithmetic`

##### Specification

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/slice/_type='Index'
\n(?:\1.+\n)*?\1/slice/value/_type='BinOp'
```

##### Example

```python
1   a[i + j]
2   a[i] # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `index_arithmetic` | 1 |

--------------------------------------------------------------------------------

#### Feature `negative_index`

##### Specification

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `slice`

##### Specification

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `slice_step`

##### Specification

```re
           ^(.*)/_type='Subscript'
\n(?:\1.+\n)*?\1/slice/_type='Slice'
\n(?:\1.+\n)*?\1/slice/step/_pos=(?P<POS>.+)
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

#### Feature `unary_operator`

##### Specification

```re
           ^(.*)/_type='UnaryOp'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `binary_operator`

##### Specification

```re
           ^(.*)/_type='BinOp'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `conditional_expression`

Match the so-called ternary operator.

##### Specification

```re
           ^(.*)/_type='IfExp'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `boolean_operator`

##### Specification

```re
           ^(.*)/_type='BoolOp'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

**Remark.** `Not` is not a boolean operator in Python. To match it, use [feature `unary_operator:Not`](#feature-unary_operator).

--------------------------------------------------------------------------------

#### Feature `comparison_operator`

##### Derivations

[🔽 feature `chained_equalities|chained_inequalities`](#feature-chained_equalitieschained_inequalities)  

##### Specification

```re
           ^(.*)/ops/        (?P<_1>\d+)/_type='(?P<SUFFIX>Eq|Lt|LtE|Gt|GtE|In|NotIn|NotEq|Is|IsNot)'
\n(?:\1.+\n)*?\1/comparators/(?P=_1)    /_pos=(?P<POS>.+)
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

#### Feature `chained_comparison`

##### Derivations

[🔽 feature `chained_equalities|chained_inequalities`](#feature-chained_equalitieschained_inequalities)  

##### Specification

```re
           ^(.*)/_type='Compare'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `chained_equalities|chained_inequalities`

##### Derivations

[🔼 feature `chained_comparison`](#feature-chained_comparison)  
[🔼 feature `comparison_operator`](#feature-comparison_operator)  

##### Specification

```sql
SELECT CASE op.name_suffix
           WHEN "Eq" THEN "chained_equalities"
           ELSE "chained_inequalities"
       END,
       count(*),
       cmp.span,
       cmp.path
FROM t cmp
JOIN t op ON (op.path GLOB cmp.path || "?*")
WHERE cmp.name_prefix = "chained_comparison"
  AND op.name REGEXP "comparison_operator:(Eq|Lt|LtE|Gt|GtE)"
GROUP BY cmp.path,
         op.name_suffix
HAVING count(*) > 1 -- a chain has at least two operators
ORDER BY cmp.path
```

##### Example

```python
1   a == 1                     # no match
2   a == b == c                # one chained equality with 2 = signs
3   a < b < c < d              # one chained inequality with 3 < signs
4   a == b == c and d < e      # one more chained equality with 2 = signs
5   a > b > c and d > e > f    # two chained inequalities with 2 > signs
6   a < b > c and a != b == c  # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `chained_equalities:2` | 2, 4 |
| `chained_inequalities:3` | 3 |
| `chained_inequalities:2` | 5, 5 |

--------------------------------------------------------------------------------

#### Feature `divisibility_test`

##### Specification

```re
           ^(.*)/_type='Compare'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/left/op/_type='Mod'
(   # try to match the % right operand with a number
\n(?:\1.+\n)*?\1/left/right/n=(?P<SUFFIX>.+)
)?
\n(?:\1.+\n)*?\1/ops/length=1
\n(?:\1.+\n)*?\1/ops/1/_type='(Eq|NotEq)'
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

#### Feature `short_circuit`

When the value of the left operand suffices to determine the value of a boolean expression, short-circuit evaluation skips the right operand. This behaviour is sometimes desirable or even required, but Paroxython currently cannot detect the case: so, when commutating the operands would result in an error or a performance penalty, you should add manually the hint `# paroxython: short_circuit` in the source-code.

##### Specification

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

#### Feature `function_call`

##### Derivations

[🔽 feature `body_recursive_function`](#feature-body_recursive_function)  
[🔽 feature `deeply_recursive_function`](#feature-deeply_recursive_function)  
[🔽 feature `range`](#feature-range)  
[🔽 feature `recursive_function`](#feature-recursive_function)  

##### Specification

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/func/_type='Name'
\n(?:\1.+\n)*?\1/func/id='(?P<SUFFIX>.+)'
```

##### Example

```python
1   foo(a, b, c)
2   bar()
3   buzz(x, 2)
4   fizz(foobar(x), 2)
5   baz.qux() # no match, see feature method_call
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

#### Feature `function_tail_call`

A tail-call is a call whose result is immediately returned, without any further calculation. This property is not interesting as such, but will be used below as a basis for the recognition of tail-recursive functions.

##### Derivations

[🔽 feature `body_recursive_function`](#feature-body_recursive_function)  

##### Specification

```re
           ^(.*)/_type='Return'
\n(?:\1.+\n)*?\1/value/( 
                       _type='Call'
\n(?:\1.+\n)*?\1/value/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value/func/_type='Name'
\n(?:\1.+\n)*?\1/value/func/id='(?P<SUFFIX>.+)'
                       |
                       _type='BoolOp'
\n(?:\1.+\n)*?\1/value/values/length=(?P<LENGTH>\d+)
\n(?:\1.+\n)*?\1/value/values/(?P=LENGTH)/_type='Call'
\n(?:\1.+\n)*?\1/value/values/(?P=LENGTH)/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value/values/(?P=LENGTH)/func/id='(?P<SUFFIX>.+)'
                       |
                       _type='IfExp'
(
\n(?:\1.+\n)*?\1/value/(?P<_1>body|orelse)/_type='Call'
\n(?:\1.+\n)*?\1/value/(?P=_1)            /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value/(?P=_1)            /func/_type='Name'
\n(?:\1.+\n)*?\1/value/(?P=_1)            /func/id='(?P<SUFFIX>.+)'
)+  # can match both branches
)
```

##### Example

```python
1   def foobar():
2       return foo(m-1, 1)                   # tail call
3       return foo(m-1, bar(m, n-1))         # tail call / no match
4       return c and foo(m)                  # tail call
5       return c1 and c2 and foo(m)          # tail call
6       return (42 if c else foo(m + 1))     # tail call
7       return (foo(m) if c else 42)         # tail call
8       return (foo(m) if c else foo(m + 1)) # tail call / tail_call
9       return bar(m) and c  # no match
10      return bar(m) + 1    # no match
11      return 1 + bar(m)    # no match
12      return bar(m)[-1]    # no match
13      return (1, bar())    # no match
14      return {1: bar()}    # no match
15      return {bar(): 1}    # no match
16  
17  def useless_assignment():
18      a = bar(n) 
19      return a # LIMITATION: no match
20  
21  def procedure():
22      if c1:
23          if c2:
24              bar(1) # LIMITATION: no match
25          else:
26              bar(2) # LIMITATION: no match
27      else:
28          bar(3) # LIMITATION: no match
```

**Remark.** Since the short-circuit expression `c and foo(m)` is equivalent to the conditional expression `if c then foo(m) else False`, `foo(m)` is actually a tail-call.

##### Matches

| Label | Lines |
|:--|:--|
| `function_tail_call:foo` | 2, 3, 4, 5, 6, 7, 8, 8 |

--------------------------------------------------------------------------------

#### Feature `call_argument`

Match any argument of a function or a method call. Suffix this argument when it is **atomic**, _i.e._ either:
- a simple identifier,
- a number literal,
- `True`, `False` or `None`.
Otherwise, suffix it with an empty string.

##### Derivations

[🔽 feature `accumulate_elements`](#feature-accumulate_elements)  
[🔽 feature `range`](#feature-range)  

##### Specification

```re
           ^(.*)/_type='Call'
(
\n(?:\1.+\n)*?\1/(?P<_1>args/\d+)/_pos=(?P<POS>.+)
\n            \1/(?P=_1)         /(   # the next line denotes either an atomic argument
                                    (value|n|id)?='?(?P<SUFFIX>.+?)\b'?$ # capture it as suffix
                                    | # or a non atomic argument
                                    (?P<SUFFIX>).+ # "capture" an empty suffix
                                  )
)+ # at least one argument
```

##### Example

```python
1   bar() # no match
2   foo("a string") # empty suffix
3   foo(None)
4   foo(True)
5   foo(42)
6   buzz(x, 42)
7   buzz((x, 42))
8   fizz(foobar(x), 42) # empty suffix for the first argument
9   foo(a, b, c)
10  foo.bar(bizz, buzz)
11  def fun_def(f, g): # no match
12      f(g)
```

##### Matches

| Label | Lines |
|:--|:--|
| `call_argument:` | 2, 7, 8 |
| `call_argument:None` | 3 |
| `call_argument:True` | 4 |
| `call_argument:42` | 5, 6, 8 |
| `call_argument:x` | 6, 8 |
| `call_argument:a` | 9 |
| `call_argument:b` | 9 |
| `call_argument:c` | 9 |
| `call_argument:bizz` | 10 |
| `call_argument:buzz` | 10 |
| `call_argument:g` | 12 |

--------------------------------------------------------------------------------

#### Feature `method_call`

##### Derivations

[🔽 feature `accumulate_elements`](#feature-accumulate_elements)  

##### Specification

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/func/_type='Attribute'
\n(?:\1.+\n)*?\1/func/_pos=(?P<POS>.+)
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

#### Feature `method_call_object`

##### Derivations

[🔽 feature `accumulate_elements`](#feature-accumulate_elements)  

##### Specification

```re
           ^(.*)/value/_type='Call'
\n(?:\1.+\n)*?\1/value/func/_type='Attribute'
\n(?:\1.+\n)*?\1/value/func/value/_pos=(?P<POS>.+)
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

#### Feature `method_chaining`

##### Specification

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `composition`

Apply a function or a method to an expression involving the result of another function or method application, without using an intermediate variable.

##### Specification

```re
           ^(.*)/_type='Call'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/args/.*/_type='Call'
```

##### Example

```python
1   print(len("hello, world"))
2   print("hello, world") # no match
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

#### Feature `lambda_function`

##### Specification

```re
           ^(.*)/_type='Lambda'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

## Iterables

--------------------------------------------------------------------------------

#### Feature `range`

Match a call to `range()` and suffix it by its [_atomic_](#feature-call_argument) arguments, separated by a colon. Non-atomic arguments are replaced by `_`.

##### Derivations

[🔼 feature `call_argument`](#feature-call_argument)  
[🔼 feature `function_call`](#feature-function_call)  
[🔽 feature `for_range`](#feature-for_range)  

##### Specification

```sql
SELECT "range",
       group_concat(name_suffix, ":"),
       span,
       path
FROM -- Only a subquery permits to sort the arguments before grouping them together.
  (SELECT range.rowid AS rowid,
          CASE arg.name_suffix
              WHEN "" THEN "_"
              ELSE arg.name_suffix
          END AS name_suffix,
          range.span AS span,
          range.path AS path
   FROM t range
   JOIN t arg ON (arg.path GLOB range.path || "?*")
   WHERE range.name = "function_call:range"
     AND arg.name_prefix = "call_argument"
     AND length(range.path) + 4 = length(arg.path) -- Ensure that arg is a (direct) argument of range().
   ORDER BY arg.path)-- Thanks to the subquery, this clause...
GROUP BY rowid -- will be executed before this one.
```

##### Example

```python
1   range(stop1)
2   range(start2, stop2)
3   range(start3, stop3, step3)
4   range(start4, stop4, -1)
5   range(foo(bar), fizz(buzz)) # bar and buzz are not direct arguments of range()
6   range(0, 2 * n, 100)
7   range(len(seq))
```

##### Matches

| Label | Lines |
|:--|:--|
| `range:stop1` | 1 |
| `range:start2:stop2` | 2 |
| `range:start3:stop3:step3` | 3 |
| `range:start4:stop4:-1` | 4 |
| `range:_:_` | 5 |
| `range:0:_:100` | 6 |
| `range:_` | 7 |

--------------------------------------------------------------------------------

#### Feature `comprehension`

##### Specification

```re
           ^(.*)/_type='((?P<SUFFIX>List|Dict|Set)Comp|(?P<SUFFIX>Generator)Exp)'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `comprehension_for_count`

Suffix the number of `for` clauses in a given comprehension.

##### Specification

```re
           ^(.*)/_type='(ListComp|DictComp|SetComp|GeneratorExp)'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `filtered_comprehension`

Match a comprehension with an `if` clause.

##### Specification

```re
/generators/\d+/ifs/1/_pos=(?P<POS>.+)
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

#### Feature `assignment`

##### Specification

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `augmented_assignment`

##### Derivations

[🔽 feature `accumulate_elements`](#feature-accumulate_elements)  

##### Specification

```re
           ^(.*)/_type='AugAssign'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `chained_assignment`

##### Specification

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `assignment_lhs_identifier`

Capture any identifier appearing on the left hand side of an assignment (possibly augmented).

##### Derivations

[🔽 feature `accumulate_elements`](#feature-accumulate_elements)  

##### Specification

```re
^(.*/assigntarget(s/\d+)?(|/value|/elts/\d+|/elts/\d+/value))/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1                                             /id='(?P<SUFFIX>.+)'
```

##### Example

```python
1   _ = 1
2   a = 1
3   (b, c) = (1, 1)
4   [d, e] = [1, 1]
5   f[g] = 1             # no match for g
6   if foo:
7       h = 1
8   def bar():
9       i = 1
10  j = k = 1
11  l.m = 1              # LIMITATION: no match for m
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

#### Feature `assignment_rhs_identifier`

Capture any identifier (variable or function) appearing on the right hand side of an assignment (possibly augmented).

##### Derivations

[🔽 feature `accumulate_elements`](#feature-accumulate_elements)  

##### Specification

```re
^(.*/assignvalue\b.*)/_pos=(?P<POS>.+)
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

#### Feature `swapping`

Swap two variables or two elements of an array with a 2-element tuple or list.

##### Specification

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/1/elts/1/_hash=(?P<HASH_A>.+)
\n(?:\1.+\n)*?\1/assigntargets/1/elts/2/_hash=(?P<HASH_B>.+)
\n(?:\1.+\n)*?\1/assignvalue/elts/1/_hash=(?P=HASH_B)
\n(?:\1.+\n)*?\1/assignvalue/elts/2/_hash=(?P=HASH_A)
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

#### Feature `negation`

Update a variable by negating it.

##### Specification

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/1/_hash=(?P<HASH>.+) # capture hash
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

### Interface

--------------------------------------------------------------------------------

#### Feature `function`

In Python, the term "function" encompasses any type of subroutine, be it a method, a procedure, a generator or a "pure" function.

##### Derivations

[🔽 feature `closure`](#feature-closure)  
[🔽 feature `deeply_recursive_function`](#feature-deeply_recursive_function)  
[🔽 feature `function_returning_nothing`](#feature-function_returning_nothing)  
[🔽 feature `function_returning_something`](#feature-function_returning_something)  
[🔽 feature `generator`](#feature-generator)  
[🔽 feature `recursive_function`](#feature-recursive_function)  

##### Specification

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)'
\n(?:\1.+\n)* \1/.+/_pos=(?P<POS>.+)
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
9   @decoration
10  def christmas_tree():
11      pass
12
13  def function_with_types(x: Int) -> Int:
14      return x + 1
15
16  class Foo:
17
18      def bar(self):
19          pass
20
21  def generator():
22      yield x
```

##### Matches

| Label | Lines |
|:--|:--|
| `function:foo` | 1-7 |
| `function:fizz` | 2-4 |
| `function:christmas_tree` | 9-11 |
| `function:function_with_types` | 13-14 |
| `function:bar` | 18-19 |
| `function:generator` | 21-22 |

--------------------------------------------------------------------------------

#### Feature `return`

Match `return` statements and, when the returned object is [_atomic_](#feature-call_argument), suffix it. Note that a `return` statement returning no value is denoted by `return:None`, not to be confounded with `return` (without suffix), which denotes the return of a non-atomic object.

##### Derivations

[🔽 feature `closure`](#feature-closure)  
[🔽 feature `function_returning_something`](#feature-function_returning_something)  

##### Specification

```re
           ^(.*)/_type='Return'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/value(/value|/n|/id)?='?(?P<SUFFIX>.+?)\b'?$
)?
```

##### Example

```python
1   def foobar():
2       return a
3       return (b, c) # no suffix
4       return d(e)   # no suffix
5       return f + g  # no suffix
6       return 2
7       return True
8       return None
9       return
10      return "foobar"
```

##### Matches

| Label | Lines |
|:--|:--|
| `return:a` | 2 |
| `return` | 3, 4, 5, 10 |
| `return:2` | 6 |
| `return:True` | 7 |
| `return:None` | 8, 9 |

--------------------------------------------------------------------------------

#### Feature `yield`

Match `yield` and `yieldfrom` _[expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions)_ (generally used as statements) and, when the yielded object is [_atomic_](#feature-call_argument), suffix it.

##### Derivations

[🔽 feature `generator`](#feature-generator)  

##### Specification

```re
           ^(.*)/_type='Yield(From)?'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/value(/value|/n|/id)?='?(?P<SUFFIX>.+?)\b'?$
)?
```

##### Example

```python
1   def foobar():
2       yield a
3       yield (b, c) # no suffix
4       yield d(e)   # no suffix
5       yield f + g  # no suffix
6       yield 2
7       yield True
8       yield None
9       yield
10      yield from seq
```

##### Matches

| Label | Lines |
|:--|:--|
| `yield:a` | 2 |
| `yield` | 3, 4, 5 |
| `yield:2` | 6 |
| `yield:True` | 7 |
| `yield:None` | 8, 9 |
| `yield:seq` | 10 |

--------------------------------------------------------------------------------

#### Feature `generator`

##### Derivations

[🔼 feature `function`](#feature-function)  
[🔼 feature `yield`](#feature-yield)  
[🔽 feature `function_returning_nothing`](#feature-function_returning_nothing)  

##### Specification

```sql
SELECT "generator",
       f.name_suffix,
       max(f.span_start) || "-" || min(f.span_end),
       max(f.path)
FROM t f
JOIN t y ON (y.path GLOB f.path || "?*")
WHERE f.name_prefix = "function"
  AND y.name_prefix = "yield"
GROUP BY y.rowid
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

#### Feature `function_returning_something`

A function returning at least one value distinct from `None` is the smallest `function` featuring `return_something`.

##### Derivations

[🔼 feature `function`](#feature-function)  
[🔼 feature `return`](#feature-return)  
[🔽 feature `function_returning_nothing`](#feature-function_returning_nothing)  

##### Specification

```sql
SELECT "function_returning_something",
       f.name_suffix,
       max(f.span_start) || "-" || min(f.span_end),
       max(f.path)
FROM t f
JOIN t r ON (r.path GLOB f.path || "?*")
WHERE f.name_prefix = "function"
  AND r.name_prefix = "return"
  AND r.name_suffix != "None"
GROUP BY r.rowid
```

##### Example

```python
1   def a():
2       return x
3
4   def b():
5       return
6
7   def c():
8       if foobar:
9           return 0
10      return
11
12  def d():
13      yield x
14
15  def e():
16      def f():
17          return x
18      pass
19
20  def g():
21      def h():
22          pass
23      return x
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_returning_something:a` | 1-2 |
| `function_returning_something:c` | 7-10 |
| `function_returning_something:f` | 16-17 |
| `function_returning_something:g` | 20-23 |

--------------------------------------------------------------------------------

#### Feature `function_returning_nothing`

A function returning nothing (aka procedure) is a function which is neither a generator or a function returning something.

##### Derivations

[🔼 feature `function`](#feature-function)  
[🔼 feature `function_returning_something`](#feature-function_returning_something)  
[🔼 feature `generator`](#feature-generator)  

##### Specification

```sql
SELECT "function_returning_nothing",
       name_suffix,
       span,
       path
FROM t
WHERE name_prefix = "function"
  AND span NOT IN
    (SELECT span
     FROM t
     WHERE name_prefix IN ("function_returning_something",
                           "generator") )
```

##### Example

```python
1   def a():
2       return x
3
4   def b():
5       return
6
7   def c():
8       if foobar:
9           return 0
10      return
11
12  def d():
13      yield x
14
15  def e():
16      def f():
17          return x
18      pass
19
20  def g():
21      def h():
22          pass
23      return x
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_returning_nothing:b` | 4-5 |
| `function_returning_nothing:e` | 15-18 |
| `function_returning_nothing:h` | 21-22 |

--------------------------------------------------------------------------------

#### Feature `function_with_default_positional_arguments`

##### Specification

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)'
\n(?:\1.+\n)*?\1/args/defaults/length=(?!0\n).+
\n(?:\1.+\n)* \1/.+/_pos=(?P<POS>.+)
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

### Nesting

--------------------------------------------------------------------------------

#### Feature `nested_function`

##### Specification

```re
           ^(.*)/_type='FunctionDef'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/name='(?P<SUFFIX>.+)'
\n(?:\1.+\n)*?\1/.+/_type='FunctionDef'
\n(?:\1.+\n)* \1/.+/_pos=(?P<POS>.+)
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

#### Feature `closure`

Function enclosing the definition of an inner function and returning it. Beware that the current definition does not check whether the inner function refers to a variable defined in the enclosing function.

##### Derivations

[🔼 feature `function`](#feature-function)  
[🔼 feature `return`](#feature-return)  

##### Specification

```sql
SELECT "closure",
       f.name_suffix,
       max(f.span_start) || "-" || min(f.span_end),
       max(f.path)
FROM t f
JOIN t c ON (c.path GLOB f.path || "?*")
JOIN t r ON (r.path GLOB f.path || "?*")
WHERE f.name_prefix = "function"
  AND c.name_prefix = "function"
  AND r.name = "return:" || c.name_suffix
GROUP BY c.rowid
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

### Recursion

--------------------------------------------------------------------------------

#### Feature `recursive_function`

##### Derivations

[🔼 feature `function`](#feature-function)  
[🔼 feature `function_call`](#feature-function_call)  
[🔽 feature `body_recursive_function`](#feature-body_recursive_function)  
[🔽 feature `tail_recursive_function`](#feature-tail_recursive_function)  

##### Specification

```sql
SELECT "recursive_function",
       f.name_suffix,
       f.span,
       f.path
FROM t f
JOIN t c ON (c.path GLOB f.path || "?*")
WHERE f.name_prefix = "function"
  AND c.name = "function_call:" || f.name_suffix
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

#### Feature `deeply_recursive_function`

Any function `f` which features a nested call to itself (`f(..., f(...), ...)`), e.g. the [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function).

##### Derivations

[🔼 feature `function`](#feature-function)  
[🔼 feature `function_call`](#feature-function_call)  

##### Specification

```sql
SELECT "deeply_recursive_function",
       f.name_suffix,
       f.span,
       f.path
FROM t f
JOIN t c1 ON (c1.path GLOB f.path || "?*")
JOIN t c2 ON (c2.path GLOB c1.path || "?*")
WHERE f.name_prefix = "function"
  AND c1.name = "function_call:" || f.name_suffix
  AND c2.name = "function_call:" || f.name_suffix
```

##### Example

```python
1   def gob_program():
2       print("PENUS")
3       gob_program(gob_program())
```

##### Matches

| Label | Lines |
|:--|:--|
| `deeply_recursive_function:gob_program` | 1-3 |

--------------------------------------------------------------------------------

#### Feature `body_recursive_function`

A function is body-recursive if and only if at least one of its recursive calls is not a tail call.

**BUG.** Since the procedure tail calls are not recognized by `function_tail_call`, the tail recursive procedures are incorrectly labelled as body recursive.

##### Derivations

[🔼 feature `function_call`](#feature-function_call)  
[🔼 feature `function_tail_call`](#feature-function_tail_call)  
[🔼 feature `recursive_function`](#feature-recursive_function)  
[🔽 feature `tail_recursive_function`](#feature-tail_recursive_function)  

##### Specification

```sql
SELECT "body_recursive_function",
       f.name_suffix,
       f.span,
       f.path
FROM t f
JOIN t any_call ON (any_call.path GLOB f.path || "?*")
WHERE f.name_prefix = "recursive_function"
  AND any_call.name = "function_call:" || f.name_suffix
  AND NOT EXISTS
    (SELECT 1
     FROM t tail_call
     WHERE tail_call.name_prefix = "function_tail_call"
       AND tail_call.path = any_call.path )
GROUP BY f.span
```

##### Example

```python
1   def gcd(a, b): # no match
2       if b == 0:
3           return a
4       else:
5           return gcd(b, a % b)
6   
7   def gcd(a, b): # no match
8       return (gcd(b, a % b) if b else a)
9   
10  def ack(m, n): # body-recursive
11      if m == 0:
12          return n + 1
13      elif n == 0:
14          return ack(m-1, 1)
15      else:
16          return ack(m-1, ack(m, n-1))
17  
18  def divisor_count(n): # no match (not recursive)
19      def recurs(candidates): # body_recursive
20          if len(candidates) == 0:
21              return 0
22          if n % candidates[0] == 0:
23              return 1 + recurs(candidates[1:])
24          return recurs(candidates[1:])
25      return recurs(range(1, n+1))
26  
27  def place(x = 1, y = 1, queens = []): # BUG: incorrectly labelled as body recursive
28      if x > SIZE:
29          print(queens)
30      else:
31          if possible(x, y, queens):
32              place(x + 1, 1, queens + [(x, y)])
33          if y < SIZE:
34              place(x, y + 1, queens)
```

##### Matches

| Label | Lines |
|:--|:--|
| `body_recursive_function:ack` | 10-16 |
| `body_recursive_function:place` | 27-34 |
| `body_recursive_function:recurs` | 19-24 |

--------------------------------------------------------------------------------

#### Feature `tail_recursive_function`

A function is tail-recursive if and only if all its recursive calls are tail calls.

**LIMITATION.** Currently, the tail recursive procedures (_i.e._, without `return`, e.g. the drawing of a fractal) are not recognized.

##### Derivations

[🔼 feature `body_recursive_function`](#feature-body_recursive_function)  
[🔼 feature `recursive_function`](#feature-recursive_function)  

##### Specification

```sql
SELECT "tail_recursive_function",
       f.name_suffix,
       f.span,
       f.path
FROM t f
WHERE f.name_prefix = "recursive_function" -- A recursive function...
  AND NOT EXISTS -- which is not...
    (SELECT 1
     FROM t body_rec
     WHERE body_rec.name_prefix = "body_recursive_function" -- body recursive.
       AND body_rec.span = f.span)
```

##### Example

```python
1   def gcd(a, b):
2       if b == 0:
3           return a
4       else:
5           return gcd(b, a % b)
6   
7   def gcd(a, b):
8       return (gcd(b, a % b) if b else a)
9   
10  def ack(m, n):
11      if m == 0:
12          return n + 1
13      elif n == 0:
14          return ack(m-1, 1)
15      else:
16          return ack(m-1, ack(m, n-1))
17  
18  def divisor_count(n):
19      def recurs(candidates):
20          if len(candidates) == 0:
21              return 0
22          if n % candidates[0] == 0:
23              return 1 + recurs(candidates[1:])
24          return recurs(candidates[1:])
25      return recurs(range(1, n+1))
26  
27  def place(x = 1, y = 1, queens = []):
28      if x > SIZE:
29          print(queens)
30      else:
31          if possible(x, y, queens):
32              place(x + 1, 1, queens + [(x, y)])
33          if y < SIZE:
34              place(x, y + 1, queens)
```

##### Matches

| Label | Lines |
|:--|:--|
| `tail_recursive_function:gcd` | 1-5, 7-8 |

--------------------------------------------------------------------------------

## Conditionals

--------------------------------------------------------------------------------

#### Feature `if`

Match an entire conditional (from the `if` clause to the last line of its body).

##### Derivations

[🔽 feature `nested_if`](#feature-nested_if)  

##### Specification

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/.+/_pos=(?P<POS>.+)
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

#### Feature `if_test_id`

Match any identifier present in the condition of an `if` statement.

##### Specification

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `if_then_branch`

Match the body of the branch “`then`” of an `if` statement.

##### Derivations

[🔽 feature `nested_if`](#feature-nested_if)  

##### Specification

```re
(^  # capture any body block
                   .*/body/\d+
|   # capture any orelse block whose length is greater than 1
    (?<!length=1\n).*/orelse/\d+
)
                /_type='If'
\n(?:\1.+\n)*?\1/body/1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)* \1/body/.*/_pos=(?P<POS>.+)
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

#### Feature `if_elif_branch`

Match the body of an `elif` clause, which is (or could be rewritten as) an `else` branch consisting in a single statement `if`.

##### Derivations

[🔽 feature `nested_if`](#feature-nested_if)  

##### Specification

```re
           ^(.*)/orelse/length=1
\n(?:\1.+\n)*?\1/orelse/1/_type='If'
\n(?:\1.+\n)*?\1/orelse/1/body/1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)* \1/orelse/1/body/.+/_pos=(?P<POS>.+)
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

#### Feature `if_else_branch`

Match the body of the possible `else` branch of an `if` statement.

##### Derivations

[🔽 feature `nested_if`](#feature-nested_if)  

##### Specification

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/orelse/
(   # there is at least two statements in the else branch,
                        length=\d+(?<![01])
\n(?:\1.+\n)*?\1/orelse/1/_pos=(?P<POS>.+)
|   # or only one, but distinct from If (otherwise, this is an elif)
                        length=1
\n(?:\1.+\n)*?\1/orelse/1/_type='.+?(?<!If)'
\n(?:\1.+\n)*?\1/orelse/1/_pos=(?P<POS>.+)
)
(
\n(?:\1.+\n)* \1/orelse/.+/_pos=(?P<POS>.+)
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

#### Feature `nested_if`

Match an `if` clause nested in _n_ other `if` clauses, suffixing it by _n_.

##### Derivations

[🔼 feature `if`](#feature-if)  
[🔼 feature `if_elif_branch`](#feature-if_elif_branch)  
[🔼 feature `if_else_branch`](#feature-if_else_branch)  
[🔼 feature `if_then_branch`](#feature-if_then_branch)  

##### Specification

```sql
SELECT "nested_if",
       count(*),
       inner_if.span,
       inner_if.path
FROM t outer_branch
JOIN t inner_if ON (outer_branch.span_start <= inner_if.span_start
                    AND inner_if.span_end <= outer_branch.span_end)
WHERE outer_branch.name_prefix IN ("if_then_branch",
                                   "if_else_branch",
                                   "if_elif_branch")
  AND inner_if.name_prefix = "if"
GROUP BY inner_if.span
ORDER BY inner_if.span_start
```

**Remark.** A join condition `(inner_if.path GLOB outer_branch.path || "?*")` would not work here, since an `else` branch has no specific path in the AST.

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

#### Feature `for`

Match sequential loops, along with their iteration variable(s).

##### Derivations

[🔽 feature `accumulate_elements`](#feature-accumulate_elements)  
[🔽 feature `for_range`](#feature-for_range)  
[🔽 feature `nested_for`](#feature-nested_for)  

##### Specification

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/target/_ids=(?P<SUFFIX>.+)
\n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
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

#### Feature `for_each`

Iterate over the elements of a (named) collection.

##### Specification

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/iter/_type='Name'
\n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
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

#### Feature `for_range`

Iterate over a range object.

##### Derivations

[🔼 feature `for`](#feature-for)  
[🔼 feature `range`](#feature-range)  

##### Specification

```sql
SELECT "for_range",
       range_expr.name_suffix,
       for_stmt.span,
       for_stmt.path
FROM t for_stmt
JOIN t range_expr ON (range_expr.path GLOB for_stmt.path || "?*")
WHERE for_stmt.name_prefix = "for"
  AND range_expr.name_prefix = "range"
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
9   for i in range(len(seq)):
10       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `for_range:stop` | 1-2 |
| `for_range:start:stop` | 3-4 |
| `for_range:start:stop:step` | 5-6 |
| `for_range:start:stop:-1` | 7-8 |
| `for_range:_` | 9-10 |

--------------------------------------------------------------------------------

#### Feature `for_indexes_elements`

Iterate over index numbers and elements of a collection.

##### Specification

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/iter/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/iter/func/id='enumerate'
\n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
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

#### Feature `for_indexes`

Iterate over index numbers of a collection.

##### Specification

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/iter/_type='Call'
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=1
\n(?:\1.+\n)*?\1/iter/args/1/_type='Call'
\n(?:\1.+\n)*?\1/iter/args/1/func/id='len'
\n(?:\1.+\n)*?\1/iter/keywords/length=0
\n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
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

#### Feature `nested_for`

Match a `for` statement nested in _n_ other `for` statements, suffixing it by _n_.

##### Derivations

[🔼 feature `for`](#feature-for)  

##### Specification

```sql
SELECT "nested_for",
       count(*),
       inner_loop.span,
       inner_loop.path
FROM t outer_loop
JOIN t inner_loop ON (inner_loop.path GLOB outer_loop.path || "?*")
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

#### Feature `triangular_nested_for`

A `for` loop with a counter `i` and a nested `for` loop which makes `i` iterations. The total number of iterations is a [triangular number](https://en.wikipedia.org/wiki/Triangular_number).

##### Specification

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/target/id=(?P<VAR>.+) # capture iteration variable
\n(?:\1.+\n)*?\1/iter/_type='Call'
\n(?:\1.+\n)*?\1/iter/func/id='range'
\n(?:\1.+\n)*?\1/iter/args/length=1 # only range(arg1)
(   # i goes from 0 to n, and j from 0 to i
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/func/id='range'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/args/length=1 # only range(arg1)
\n(?:\1.+\n)* \1/(?P=_1)                    /iter/args/1.*/id=(?P=VAR) # match iteration variable
|   # i goes from 0 to n, and j from i to n
\n(?:\1.+\n)*?\1/iter/args/1/_hash=(?P<STOP>.+) # capture stop expression
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/func/id='range'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/args/length=2 # only range(arg1, arg2)
\n(?:\1.+\n)* \1/(?P=_1)                    /iter/args/1(/.+)*/id=(?P=VAR) # match iteration variable
\n(?:\1.+\n)* \1/(?P=_1)                    /iter/args/2(/.+)*/_hash=(?P=STOP) # match stop expression
)
\n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
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

#### Feature `square_nested_for`

Two nested `for` loops doing the same number of iterations.

##### Specification

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/iter/_hash=(?P<HASH>.+) # capture _hash
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_hash=(?P=HASH) # match _hash
\n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
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

#### Feature `while`

##### Specification

```re
           ^(.*)/_type='While'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
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

#### Feature `assertion`

##### Specification

```re
           ^(.*)/_type='Assert'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `try`

##### Derivations

[🔽 feature `try_raise|try_except`](#feature-try_raisetry_except)  

##### Specification

```re
           ^(.*)/_type='Try'
\n(?:\1.+\n)* \1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/.*/_pos=(?P<POS>.+)
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

#### Feature `raise`

##### Derivations

[🔽 feature `try_raise|try_except`](#feature-try_raisetry_except)  

##### Specification

```re
           ^(.*)/_type='Raise'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `except`

##### Derivations

[🔽 feature `try_raise|try_except`](#feature-try_raisetry_except)  

##### Specification

```re
           ^(.*)/(?P<_1>handlers/\d+/(type/(func/|elts/\d+/)?)?)_pos=(?P<POS>.+)
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

#### Feature `try_raise|try_except`

##### Derivations

[🔼 feature `except`](#feature-except)  
[🔼 feature `raise`](#feature-raise)  
[🔼 feature `try`](#feature-try)  

##### Specification

```sql
SELECT "try_" || e.name_prefix,
       e.name_suffix,
       max(t.span_start) || "-" || min(t.span_end),
       max(t.path)
FROM t t
JOIN t e ON (e.path GLOB t.path || "?*")
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

#### Feature `import_module`

##### Derivations

[🔽 feature `import`](#feature-import)  

##### Specification

```re
           ^(.*)/_type='Import(From)?'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `import_name`

##### Derivations

[🔽 feature `import`](#feature-import)  

##### Specification

```re
           ^(.*)/_type='ImportFrom'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
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

#### Feature `import`

Suffixed by the imported module and, if any, the imported name. In most cases, could replace the two low-level features `import_module` and `import_name`.

##### Derivations

[🔼 feature `import_module`](#feature-import_module)  
[🔼 feature `import_name`](#feature-import_name)  

##### Specification

```sql
SELECT "import",
       m.name_suffix || (CASE
                             WHEN n.name_suffix IS NULL THEN ""
                             ELSE ":" || n.name_suffix
                         END),
       m.span,
       m.path
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

#### Feature `accumulate_elements`

An accumulator is iteratively updated from its previous value and those of the iteration variable.

##### Derivations

[🔼 feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[🔼 feature `assignment_rhs_identifier`](#feature-assignment_rhs_identifier)  
[🔼 feature `augmented_assignment`](#feature-augmented_assignment)  
[🔼 feature `call_argument`](#feature-call_argument)  
[🔼 feature `for`](#feature-for)  
[🔼 feature `method_call`](#feature-method_call)  
[🔼 feature `method_call_object`](#feature-method_call_object)  

##### Specification

```sql
SELECT "accumulate_elements",
       count(DISTINCT acc_left.name_suffix),
       for_loop.span,
       for_loop.path
FROM t for_loop
JOIN t iter_var ON (iter_var.path GLOB for_loop.path || "?*")-- Ensure iter_var is nested in the loop...
JOIN t acc_left ON (iter_var.span = acc_left.span)-- and has same span as both acc_left...
JOIN t acc_right ON (iter_var.span = acc_right.span)-- and acc_right.
WHERE for_loop.name_prefix = "for" -- A for loop...
  AND for_loop.name_suffix = iter_var.name_suffix -- whose iteration variable...
  AND ((iter_var.name_prefix = "assignment_rhs_identifier" -- either appears on the RHS of an assignment...
        AND (acc_left.name_prefix = "augmented_assignment" -- (which is either augmented...
             OR (acc_left.name_suffix = acc_right.name_suffix -- or references the same identifier...
                 AND acc_left.name_prefix = "assignment_lhs_identifier" -- on both left...
                 AND acc_right.name_prefix = "assignment_rhs_identifier")))-- and right hand size)...
       OR (iter_var.name_prefix = "call_argument" -- or appears as an argument...
           AND acc_right.name_prefix = "method_call" -- of a call to a method...
           AND acc_right.name_suffix REGEXP "(append|extend|insert|add|update)$" -- updating its object.
           AND acc_left.name_prefix = "method_call_object" -- Ensure that the suffix is the accumulator...
 ))
  AND for_loop.name_suffix != acc_left.name_suffix -- and is distinct from the iteration variable.
GROUP BY for_loop.span
ORDER BY for_loop.span_start
```

**Remark.** Note the user-defined function `REGEXP` in the `WHERE`clause. It calls the function `match()` of the third-party [`regex`](https://pypi.org/project/regex/) library.

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

#### Feature `filter_for`

An accumulation pattern that, from a given collection, returns a list containing only those elements that verify a certain condition.

##### Specification

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/target/id=(?P<ID_1>.+) # capture the iteration variable
\n(?:\1.+\n)*?\1/(?P<_1>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)* \1/(?P=_1)                /test/args/\d+/id=(?P=ID_1) # match it in an inner conditional test
\n(?:\1.+\n)* \1/(?P=_1)                /(?P<_2>(?:body|orelse)/\d+)/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_1)                /(?P=_2)                    /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)                /(?P=_2)                    /value/func/attr='append'
\n(?:\1.+\n)*?\1/(?P=_1)                /(?P=_2)                    /value/args/1/id=(?P=ID_1) # match it in an append()
\n(?:\1.+\n)* \1.*/_pos=(?P<POS>.+)
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

#### Feature `find_best_element`

An accumulation pattern that, from a given collection, returns the best element verifying a certain condition.

##### Specification

```re
           ^(.*)/(?P<_1>(?:body|orelse)/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_1)                /assigntargets/1/id='(?P<CANDIDATE>.+)' # capture candidate
\n(?:\1.+\n)* \1/(?P<_2>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_2)                /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_2)                /target/id='(?P<ITER_VAR>.+)' # capture iteration variable
\n(?:\1.+\n)* \1/(?P=_2)                /(?P<_3>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /test/_ids=(?=.*?\b(?P=ITER_VAR)\b)
                                                                               (?=.*?\b(?P=CANDIDATE)\b)
                                                                               .* # match both
\n(?:\1.+\n)* \1/(?P=_2)                /(?P=_3)                    /test/.*/id='(?P=CANDIDATE)' # match candidate
\n(?:\1.+\n)* \1/(?P=_2)                /(?P=_3)                    /(?P<_4>(?:body|orelse)/\d+)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /(?P=_4)                /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /(?P=_4)                /assigntargets/1/id='(?P=CANDIDATE)' # match candidate
\n(?:\1.+\n)*?\1/(?P=_2)                /(?P=_3)                    /(?P=_4)                /assignvalue/id='(?P=ITER_VAR)' # match iteration variable
(
\n(?:\1.+\n)* \1(?P=_2)                /(?P=_3).*/_pos=(?P<POS>.+)
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

#### Feature `universal_quantifier`

Check whether all elements of a collection satisfy a predicate.

##### Specification

```re
          ^(.*?)/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/(?P=_1)                    /(?P<_2>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)* \1/(?P=_1)                    /(?P=_2)                    /(?P<_3>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)                    /(?P=_2)                    /(?P=_3)                    /value/value=False
\n(?:\1.+\n)* \1/(?P<_4>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_4)                    /_pos=(?P<POS>.+)
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

#### Feature `existential_quantifier`

Check whether any element of a collection satisfies a predicate.

##### Specification

```re
          ^(.*?)/(?P<_1>(?:body|orelse)/\d+)/_type='For'
\n(?:\1.+\n)*?\1/(?P=_1)                    /_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/(?P=_1)                    /(?P<_2>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)* \1/(?P=_1)                    /(?P=_2)                    /(?P<_3>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)                    /(?P=_2)                    /(?P=_3)                    /value/value=True
\n(?:\1.+\n)* \1/(?P<_4>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_4)                    /_pos=(?P<POS>.+)
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

#### Feature `find_first_element`

Linear search. Return the first element of a sequence satisfying a predicate.

##### Specification

```re
           ^(.*)/_type='For'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/target/id=(?P<ITER_VAR>.+) # capture the name of the iteration variable
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/.+)/_type='If' # The If appears at any depth in the loop
\n(?:\1.+\n)* \1/(?P=_1)                   /test/.+/id=(?P=ITER_VAR) # The variable appears at any depth inside the condition
\n(?:\1.+\n)*?\1/(?P=_1)                   /(?P<_2>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)                   /(?P=_2)                    /_pos=(?P<POS>.+)
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

#### Feature `evolve_state`

Evolve the value of a variable until it reaches a desired state.

##### Specification

```re
           ^(.*)/_type='While'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/test/.*/id='(?P<STATE>.+)' # capture state variable
(   # the state variable either appears on both sides of a simple assignment
\n(?:\1.+\n)* \1/(?P<_1>body/.*)/_type='Assign'
\n(?:\1.+\n)*?\1/(?P=_1)        /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_1)        /assigntargets/1/id='(?P=STATE)' # it is updated somewhere in the loop
\n(?:\1.+\n)*?\1/(?P=_1)        /assignvalue/_ids=.*\b(?P=STATE)\b.* # from its current value
|   # or appears on LHS of an augmented assignement
\n(?:\1.+\n)* \1/(?P<_1>body/.*)/_type='AugAssign'
\n(?:\1.+\n)*?\1/(?P=_1)        /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_1)        /assigntarget/id='(?P=STATE)' # it is augmented somewhere in the loop
|   # or is mutated by calling a function or a method of this variable
\n(?:\1.+\n)* \1/(?P<_1>body/.*)/_type='Expr'
\n(?:\1.+\n)*?\1/(?P=_1)        /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_1)        /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_1)        /value/.*/id='(?P=STATE)' # it is mutated somewhere in the loop
)
(
\n(?:\1.+\n)* \1.*/_pos=(?P<POS>.+)
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

#### Feature `accumulate_stream`

Accumulate the inputs until a sentinel value is encountered (accumulation expressed by: `acc = combine(x, acc)`).

##### Specification

```re
           ^(.*)/_type='While'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/test/value=True
\n(?:\1.+\n)* \1/(?:body|orelse)/\d+/assigntargets/.+/id='(?P<INPUT>.+)' # capture the name of the input
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type='If'
\n(?:\1.+\n)*?\1/(?P=_1)                /test/_ids=.*?\b(?P=INPUT)\b.* # the input is tested
\n(?:\1.+\n)* \1/(?P=_1)                /(?P<_2>(?:body|orelse)/\d+)/_type='Return'
\n(?:\1.+\n)*?\1/(?P=_1)                /(?P=_2)                    /value/id='(?P<ACC>.+)' # capture the name of the accumulator
(   # the accumulator either appears on both sides of a simple assignment with the input
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='(?P<SUFFIX>Assign)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/(?P=_3)                    /assigntargets/.*/id='(?P=ACC)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /assignvalue/_ids=(?=.*\b(?P=INPUT)\b)
                                                        (?=.*\b(?P=ACC)\b)
                                                        .* # both appear in RHS
|   # or is on LHS of an augmented assignement with the input
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='(?P<SUFFIX>AugAssign)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_3)                    /assigntarget/id='(?P=ACC)'
\n(?:\1.+\n)* \1/(?P=_3)                    /assignvalue.*/id='(?P=INPUT)'
|   # or should be mutated by calling a function on this accumulator and the iteration variable
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_3)                    /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_ids=(?=.*\b(?P=INPUT)\b)
                                                        (?=.*\b(?P=ACC)\b)
                                                        .+ # both appear in RHS
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/_type='(?P<SUFFIX>Name)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/id='(?!(?P=ACC)|(?P=INPUT)|breakpoint|delattr|eval|exec|help|input|open|print|setattr|super).+'
|   # or should be mutated by calling a method of this accumulator, again on the iteration variable
\n(?:\1.+\n)* \1/(?P<_3>(?:body|orelse)/\d+)/_type='Expr' # the whole line consists in an expression
\n(?:\1.+\n)*?\1/(?P=_3)                    /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/_type='Call'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/_type='(?P<SUFFIX>Attribute)'
\n(?:\1.+\n)*?\1/(?P=_3)                    /value/func/value/id='(?P=ACC)' # a method of acc is called on...
\n(?:\1.+\n)* \1/(?P=_3)                    /value/args/\d+/id='(?P=INPUT)' # the iteration variable
)
(
\n(?:\1.+\n)* \1.*/_pos=(?P<POS>.+)
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

#### Feature `category`

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

##### Specification

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

These patterns match features that can be shortened.
It's up to you to decide if a rewriting would make the code clearer.

## Assignments

--------------------------------------------------------------------------------

#### Feature `suggest_conditional_expression`

When a conditional simply assigns different values to the same variable, it may be rewritten as a conditional expression.

##### Specification

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/body/length=1
\n(?:\1.+\n)*?\1/body/1/_type='Assign'
\n(?:\1.+\n)*?\1/body/1/assigntargets/1/_hash=(?P<HASH>.+)
\n(?:\1.+\n)*?\1/orelse/length=1
\n(?:\1.+\n)*?\1/orelse/1/_type='Assign'
\n(?:\1.+\n)*?\1/orelse/1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/orelse/1/assigntargets/1/_hash=(?P=HASH)
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

#### Feature `suggest_augmented_assignment`

When the RHS of an assignment consists in a binary operation whose left operand is the target (`a = a op expr`), the statement can be shortened as `a op= expr`.

##### Specification

```re
           ^(.*)/_type='Assign'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/length=1
\n(?:\1.+\n)*?\1/assigntargets/1/id=(?P<TARGET>.+)
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

#### Feature `suggest_comparison_chaining`

When the `else` branch of a conditional is another conditional, it can be rewritten with an `elif` branch.

##### Specification

```re
           ^(.*)/_type='BoolOp'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/op/_type='And'
\n(?:\1.+\n)*?\1/values/1/_type='Compare'
\n(?:\1.+\n)*?\1/values/1/comparators/1/_hash=(?P<HASH_1>.+) # capture the right operand of the left comparison
\n(?:\1.+\n)*?\1/values/2/_type='Compare'
\n(?:\1.+\n)*?\1/values/2/left/_hash=(?P=HASH_1) # match the left operand of the right comparison
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

#### Feature `suggest_constant_definition`

Match magic numbers (unnamed numerical constants) other than -1, 0, 1 and 2. A number in the RHS of an assignment to a constant is of course ignored.

##### Specification

```re
  ^(/(?:body|orelse)/\d+)
(   # indented lines
                /(?P<_1>(?:body|orelse)/.+)/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_1)                   /n=(?!(-1|0|1|2)\n)
|   # non indented lines
                /_type='Assign'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/1/id='.*?[a-z].*' # at least one lowercase letter
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

#### Feature `suggest_condition_return`

When a predicate ends with a conditional whose sole purpose is to return `True` or `False`, it is enough to return the condition.

##### Specification

```re
           ^(.*)/_type='If'
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/body/1/_type='Return'
\n(?:\1.+\n)*?\1/body/1/value/value=(?P<BOOL>True|False) # name BOOL the value used here
\n(?:\1.+\n)*?\1/orelse/1/_type='Return'
\n(?:\1.+\n)*?\1/orelse/1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/orelse/1/value/value=(True|False)(?<!(?P=BOOL)) # and check not BOOL is used there
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