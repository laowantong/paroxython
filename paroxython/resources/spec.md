- [AST](#ast)
      - [Feature `node`](#feature-node)
      - [Feature `value_attr`](#feature-value_attr)
      - [Feature `loaded_variable`](#feature-loaded_variable)
- [Expressions](#expressions)
  - [Literals](#literals)
      - [Feature `literal`](#feature-literal)
      - [Feature `empty_literal`](#feature-empty_literal)
      - [Feature `special_literal_string`](#feature-special_literal_string)
      - [Feature `magic_number` (SQL)](#feature-magic_number)
  - [Subscripts](#subscripts)
      - [Feature `index`](#feature-index)
      - [Feature `nested_index`](#feature-nested_index)
      - [Feature `index_shape` (SQL)](#feature-index_shape)
      - [Feature `index_arithmetic`](#feature-index_arithmetic)
      - [Feature `negative_index`](#feature-negative_index)
      - [Feature `slice_lower`](#feature-slice_lower)
      - [Feature `slice_upper`](#feature-slice_upper)
      - [Feature `slice_step`](#feature-slice_step)
      - [Feature `slice` (SQL)](#feature-slice)
  - [Operators](#operators)
      - [Feature `unary_operator`](#feature-unary_operator)
      - [Feature `binary_operator`](#feature-binary_operator)
      - [Feature `concatenation_operator|replication_operator` (SQL)](#feature-concatenation_operatorreplication_operator)
      - [Feature `string_formatting_operator` (SQL)](#feature-string_formatting_operator)
      - [Feature `addition_operator` (SQL)](#feature-addition_operator)
      - [Feature `multiplication_operator` (SQL)](#feature-multiplication_operator)
      - [Feature `modulo_operator` (SQL)](#feature-modulo_operator)
  - [Boolean expressions](#boolean-expressions)
      - [Feature `boolean_operator`](#feature-boolean_operator)
      - [Feature `comparison_operator`](#feature-comparison_operator)
      - [Feature `yoda_comparison_unpythonic` (SQL)](#feature-yoda_comparison_unpythonic)
      - [Feature `chained_comparison`](#feature-chained_comparison)
      - [Feature `chained_comparison_unpythonic`](#feature-chained_comparison_unpythonic)
      - [Feature `chained_equalities|chained_inequalities` (SQL)](#feature-chained_equalitieschained_inequalities)
      - [Feature `divisibility_test`](#feature-divisibility_test)
      - [Feature `short_circuit`](#feature-short_circuit)
  - [Calls](#calls)
    - [Generalities](#generalities)
      - [Feature `argument`](#feature-argument)
      - [Feature `keyword_argument`](#feature-keyword_argument)
      - [Feature `composition`](#feature-composition)
    - [Calls of the form `callable(arguments)`](#calls-of-the-form-callablearguments)
      - [Feature `free_call`](#feature-free_call)
      - [Feature `free_call_with_keyword_argument` (SQL)](#feature-free_call_with_keyword_argument)
      - [Feature `free_call_without_result`](#feature-free_call_without_result)
      - [Feature `free_call_no_arguments`](#feature-free_call_no_arguments)
      - [Feature `free_tail_call`](#feature-free_tail_call)
      - [Feature `internal_free_call` (SQL)](#feature-internal_free_call)
      - [Feature `external_free_call` (SQL)](#feature-external_free_call)
    - [Calls of the form `identifier.callable(arguments)`](#calls-of-the-form-identifiercallablearguments)
      - [Feature `member_call_method`](#feature-member_call_method)
      - [Feature `member_call_object`](#feature-member_call_object)
      - [Feature `member_call` (SQL)](#feature-member_call)
      - [Feature `method_chaining`](#feature-method_chaining)
  - [Iterables](#iterables)
      - [Feature `range` (SQL)](#feature-range)
      - [Feature `comprehension`](#feature-comprehension)
      - [Feature `comprehension_for_count`](#feature-comprehension_for_count)
      - [Feature `filtered_comprehension`](#feature-filtered_comprehension)
  - [Common expressions](#common-expressions)
      - [Feature `mid_value_naive`](#feature-mid_value_naive)
      - [Feature `mid_value_recommended`](#feature-mid_value_recommended)
      - [Feature `clamp_min_max`](#feature-clamp_min_max)
      - [Feature `clamp_ternary`](#feature-clamp_ternary)
- [Statements](#statements)
      - [Feature `no_operation`](#feature-no_operation)
  - [Bindings](#bindings)
      - [Feature `assignment`](#feature-assignment)
      - [Feature `subscript_assignment`](#feature-subscript_assignment)
      - [Feature `unbinding`](#feature-unbinding)
      - [Feature `subscript_deletion`](#feature-subscript_deletion)
      - [Feature `attribute_deletion`](#feature-attribute_deletion)
      - [Feature `single_assignment`](#feature-single_assignment)
      - [Feature `parallel_assignment`](#feature-parallel_assignment)
      - [Feature `assignment_expression`](#feature-assignment_expression)
      - [Feature `augmented_assignment`](#feature-augmented_assignment)
      - [Feature `augmented_assignment_unpythonic`](#feature-augmented_assignment_unpythonic)
      - [Feature `subscript_augmented_assignment`](#feature-subscript_augmented_assignment)
      - [Feature `chained_assignment`](#feature-chained_assignment)
      - [Feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)
      - [Feature `assignment_rhs_atom`](#feature-assignment_rhs_atom)
    - [Assignment idioms](#assignment-idioms)
      - [Feature `update_by_assignment` (SQL)](#feature-update_by_assignment)
      - [Feature `update_by_augmented_assignment` (SQL)](#feature-update_by_augmented_assignment)
      - [Feature `update_by_member_call` (SQL)](#feature-update_by_member_call)
      - [Feature `update` (SQL)](#feature-update)
      - [Feature `update_by_assignment_with` (SQL)](#feature-update_by_assignment_with)
      - [Feature `update_by_augmented_assignment_with` (SQL)](#feature-update_by_augmented_assignment_with)
      - [Feature `update_by_member_call_with` (SQL)](#feature-update_by_member_call_with)
      - [Feature `update_with` (SQL)](#feature-update_with)
      - [Feature `increment`](#feature-increment)
      - [Feature `swap_unpythonic`](#feature-swap_unpythonic)
      - [Feature `swap`](#feature-swap)
      - [Feature `slide`](#feature-slide)
      - [Feature `negate`](#feature-negate)
      - [Feature `verbose_conditional_assignment`](#feature-verbose_conditional_assignment)
      - [Feature `compact_conditional_assignment`](#feature-compact_conditional_assignment)
      - [Feature `corrective_conditional_assignment`](#feature-corrective_conditional_assignment)
  - [Function and class definitions](#function-and-class-definitions)
    - [Interface](#interface)
      - [Feature `function`](#feature-function)
      - [Feature `return`](#feature-return)
      - [Feature `class`](#feature-class)
      - [Feature `method` (SQL)](#feature-method)
      - [Feature `instance_method|class_method|static_method` (SQL)](#feature-instance_methodclass_methodstatic_method)
      - [Feature `yield`](#feature-yield)
      - [Feature `generator` (SQL)](#feature-generator)
      - [Feature `function_returning_something` (SQL)](#feature-function_returning_something)
      - [Feature `pure_function` (SQL)](#feature-pure_function)
      - [Feature `impure_function` (SQL)](#feature-impure_function)
      - [Feature `function_returning_nothing` (SQL)](#feature-function_returning_nothing)
      - [Feature `function_parameter`](#feature-function_parameter)
      - [Feature `function_parameter_flavor`](#feature-function_parameter_flavor)
      - [Feature `function_parameter_default`](#feature-function_parameter_default)
      - [Feature `function_without_parameters`](#feature-function_without_parameters)
      - [Feature `decorated_function`](#feature-decorated_function)
      - [Feature `function_decorator`](#feature-function_decorator)
    - [Nesting](#nesting)
      - [Feature `nested_function`](#feature-nested_function)
      - [Feature `closure` (SQL)](#feature-closure)
      - [Feature `higher-order function` (SQL)](#feature-higher-order-function)
    - [Recursion](#recursion)
      - [Feature `recursive_function` (SQL)](#feature-recursive_function)
      - [Feature `recursive_call_count` (SQL)](#feature-recursive_call_count)
      - [Feature `deeply_recursive_function` (SQL)](#feature-deeply_recursive_function)
      - [Feature `body_recursive_function` (SQL)](#feature-body_recursive_function)
      - [Feature `tail_recursive_function` (SQL)](#feature-tail_recursive_function)
  - [Conditionals](#conditionals)
      - [Feature `if` (SQL)](#feature-if)
      - [Feature `if_test_atom`](#feature-if_test_atom)
      - [Feature `if_then_branch`](#feature-if_then_branch)
      - [Feature `if_elif_branch`](#feature-if_elif_branch)
      - [Feature `if_else_branch`](#feature-if_else_branch)
      - [Feature `if_without_else` (SQL)](#feature-if_without_else)
      - [Feature `if_guard` (SQL)](#feature-if_guard)
      - [Feature `return_condition_naive`](#feature-return_condition_naive)
      - [Feature `nested_if` (SQL)](#feature-nested_if)
  - [Iterations](#iterations)
    - [Iteration keywords](#iteration-keywords)
      - [Feature `for`](#feature-for)
      - [Feature `iteration_variable`](#feature-iteration_variable)
      - [Feature `loop` (SQL)](#feature-loop)
      - [Feature `loop_else`](#feature-loop_else)
    - [Sequential loops](#sequential-loops)
      - [Feature `for_each`](#feature-for_each)
      - [Feature `for_range` (SQL)](#feature-for_range)
      - [Feature `for_indexes_elements`](#feature-for_indexes_elements)
      - [Feature `for_indexes`](#feature-for_indexes)
      - [Feature `nested_for` (SQL)](#feature-nested_for)
      - [Feature `triangular_nested_for`](#feature-triangular_nested_for)
      - [Feature `square_nested_for`](#feature-square_nested_for)
    - [Non-sequential loops](#non-sequential-loops)
      - [Feature `infinite_while`](#feature-infinite_while)
    - [Loop exit](#loop-exit)
      - [Feature `loop_with_raise` (SQL)](#feature-loop_with_raise)
      - [Feature `loop_with_return` (SQL)](#feature-loop_with_return)
      - [Feature `loop_with_break` (SQL)](#feature-loop_with_break)
      - [Feature `loop_with_early_exit` (SQL)](#feature-loop_with_early_exit)
      - [Feature `loop_with_else` (SQL)](#feature-loop_with_else)
      - [Feature `loop_with_late_exit` (SQL)](#feature-loop_with_late_exit)
    - [Exceptions](#exceptions)
      - [Feature `raise`](#feature-raise)
      - [Feature `except`](#feature-except)
      - [Feature `try_raise|try_except` (SQL)](#feature-try_raisetry_except)
  - [Modules](#modules)
      - [Feature `import_module`](#feature-import_module)
      - [Feature `import_name`](#feature-import_name)
      - [Feature `import` (SQL)](#feature-import)
- [Iterative patterns](#iterative-patterns)
  - [Loops](#loops)
      - [Feature `count_elements|count_states` (SQL)](#feature-count_elementscount_states)
      - [Feature `count_some_elements|count_some_states` (SQL)](#feature-count_some_elementscount_some_states)
  - [Sequential loops](#sequential-loops-1)
    - [Sequential loops with late exit](#sequential-loops-with-late-exit)
      - [Feature `accumulate_elements` (SQL)](#feature-accumulate_elements)
      - [Feature `accumulate_some_elements` (SQL)](#feature-accumulate_some_elements)
      - [Feature `accumulate_all_elements` (SQL)](#feature-accumulate_all_elements)
      - [Feature `find_best_element` (SQL)](#feature-find_best_element)
      - [Feature `find_best_element_index` (SQL)](#feature-find_best_element_index)
      - [Feature `find_best_element_index_unpythonic` (SQL)](#feature-find_best_element_index_unpythonic)
    - [Sequential loops with early exit](#sequential-loops-with-early-exit)
      - [Feature `universal_quantification|existential_quantification` (SQL)](#feature-universal_quantificationexistential_quantification)
      - [Feature `find_first_good_element` (SQL)](#feature-find_first_good_element)
      - [Feature `find_first_good_element_index` (SQL)](#feature-find_first_good_element_index)
      - [Feature `find_first_good_element_index_unpythonic` (SQL)](#feature-find_first_good_element_index_unpythonic)
  - [Non-sequential loops](#non-sequential-loops-1)
    - [Non-sequential infinite loops](#non-sequential-infinite-loops)
      - [Feature `get_valid_input` (SQL)](#feature-get_valid_input)
      - [Feature `count_inputs` (SQL)](#feature-count_inputs)
      - [Feature `accumulate_inputs` (SQL)](#feature-accumulate_inputs)
- [Programs](#programs)
  - [Spans](#spans)
      - [Feature `whole_span`](#feature-whole_span)
      - [Feature `scope` (SQL)](#feature-scope)
      - [Feature `local_scope` (SQL)](#feature-local_scope)
      - [Feature `global_scope` (SQL)](#feature-global_scope)
      - [Feature `shadowing_scope` (SQL)](#feature-shadowing_scope)
      - [Feature `access_outer_scope` (SQL)](#feature-access_outer_scope)
  - [Style](#style)
      - [Feature `object_oriented_style` (SQL)](#feature-object_oriented_style)
      - [Feature `functional_style` (SQL)](#feature-functional_style)
      - [Feature `procedural_style` (SQL)](#feature-procedural_style)
      - [Feature `imperative_style` (SQL)](#feature-imperative_style)
      - [Feature `flat_style` (SQL)](#feature-flat_style)
      - [Feature `one_liner_style` (SQL)](#feature-one_liner_style)
  - [Counts](#counts)
      - [Feature `class_method_count` (SQL)](#feature-class_method_count)
      - [Feature `function_line_count` (SQL)](#feature-function_line_count)
      - [Feature `variety` (SQL)](#feature-variety)
  - [Others](#others)
      - [Feature `topic|technique|complexity`](#feature-topictechniquecomplexity)

# AST

--------------------------------------------------------------------------------

#### Feature `node`

Match the name of every node of the AST. This covers most of the [Python keywords]((https://docs.python.org/3/reference/lexical_analysis.html#keywords)), and may avoid writing specialized definitions for some simple statements (e.g., `break`, `assert`), and some constructs spanning multiple lines (e.g., `if`, `while`).

##### Derivations

[⬇️ feature `if`](#feature-if)  
[⬇️ feature `imperative_style`](#feature-imperative_style)  
[⬇️ feature `loop`](#feature-loop)  
[⬇️ feature `loop_with_break`](#feature-loop_with_break)  
[⬇️ feature `one_liner_style`](#feature-one_liner_style)  
[⬇️ feature `pure_function`](#feature-pure_function)  
[⬇️ feature `try_raise|try_except`](#feature-try_raisetry_except)  

##### Specification

```re
           ^(.*)/_type=(?P<SUFFIX>.+)
\n(?:\1.+\n)*?\1/(\w+/)?_pos=(?P<POS>.+)
(
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
)?
```

##### Example

```python
1   from os import *
2   def k(z):
3       def c():
4           return None
5           nonlocal z
6   class F:
7       pass
8   global b
9   with open(devnull) as b:
10      while b:
11          if 1 and 0 is 0:
12              continue
13          elif 1:
14              0
15          else:
16              for d in []:
17                  yield not d
18                  del d
19                  break
20      try:
21          raise 1 or False
22      except:
23          assert True
24      finally:
25          (lambda j: 0)
26
27  fake = r"/_pos=\d+"
```

**Credit.** Zach Gates, _Minimal program using all Python 3.4 keywords_, Code Golf Stack Exchange, 2016 ([link](https://codegolf.stackexchange.com/a/75901/96158)).

##### Matches

| Label | Lines |
|:--|:--|
| `node:Assert` | 23 |
| `node:Assign` | 27 |
| `node:BoolOp` | 11, 21 |
| `node:Break` | 19 |
| `node:Call` | 9 |
| `node:ClassDef` | 6-7 |
| `node:Compare` | 11 |
| `node:Continue` | 12 |
| `node:Delete` | 18 |
| `node:ExceptHandler` | 22-23 |
| `node:Expr` | 14, 17, 25 |
| `node:For` | 16-19 |
| `node:FunctionDef` | 2-5, 3-5 |
| `node:Global` | 8 |
| `node:If` | 11-19, 13-19 |
| `node:ImportFrom` | 1 |
| `node:Lambda` | 25 |
| `node:List` | 16 |
| `node:Name` | 9, 9, 9, 10, 16, 17, 18, 27 |
| `node:NameConstant` | 4, 21, 23 |
| `node:Nonlocal` | 5 |
| `node:Num` | 11, 11, 11, 13, 14, 21, 25 |
| `node:Pass` | 7 |
| `node:Raise` | 21 |
| `node:Return` | 4 |
| `node:Str` | 27 |
| `node:Try` | 20-25 |
| `node:UnaryOp` | 17 |
| `node:While` | 10-19 |
| `node:With` | 9-25 |
| `node:Yield` | 17 |
| `node:arg` | 2, 25 |
| `node:withitem` | 9 |

--------------------------------------------------------------------------------

#### Feature `value_attr`

##### Specification

```re
     ^(.*/value)/_type=Attribute
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/attr=(?P<SUFFIX>.+)
```

##### Example

```python
1   a.b
2   c.d.e
3   (1j).imag
4   (1j).imag() # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `value_attr:b` | 1 |
| `value_attr:d` | 2 |
| `value_attr:e` | 2 |
| `value_attr:imag` | 3 |

--------------------------------------------------------------------------------

#### Feature `loaded_variable`

Name of a variable appearing in an expression.

##### Derivations

[⬇️ feature `access_outer_scope`](#feature-access_outer_scope)  

##### Specification

```re
           ^(.*)(?<!/func)/_type=Name
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/id=(?P<SUFFIX>.+)
\n(?:\1.+\n)* \1/ctx/_type=Load
```

##### Example

```python
1   a = b + c # no match for a, which is stored
2   foo(bar) # no match for foo
3   bizz.buzz # no match for buzz
4   def function(): # no match for function
5       pass
6   class Class(): # no match for Class
7       pass
8   for x in seq: # no match for x
9       pass
10  l.sorted(key=len) # LIMITATION: false positive for not called built-in functions
```

##### Matches

| Label | Lines |
|:--|:--|
| `loaded_variable:b` | 1 |
| `loaded_variable:c` | 1 |
| `loaded_variable:bar` | 2 |
| `loaded_variable:bizz` | 3 |
| `loaded_variable:seq` | 8 |
| `loaded_variable:l` | 10 |
| `loaded_variable:len` | 10 |

--------------------------------------------------------------------------------

# Expressions

## Literals

--------------------------------------------------------------------------------

#### Feature `literal`

Match `None`, `True`, `False`, and literal numbers, strings, tuples, dictionaries, sets and lists. For the first four, suffix with the literal value. For the others, there is no guarantee that the value is a constant.

Further categorization of numeric literals does not require to construct a sophisticated regular expression: the heavy lifting is already made in the given AST, which stores them under normalized form:
- integer literals are just sequences of digits, with an optional minus sign `-`;
- floating point literals consist of digits, minus signs and at least one symbol among `.` and `e`;
- imaginary literals contain the same symbols as floating point literals, plus a mandatory trailing symbol `j`.

##### Derivations

[⬇️ feature `concatenation_operator|replication_operator`](#feature-concatenation_operatorreplication_operator)  
[⬇️ feature `magic_number`](#feature-magic_number)  
[⬇️ feature `string_formatting_operator`](#feature-string_formatting_operator)  
[⬇️ feature `yoda_comparison_unpythonic`](#feature-yoda_comparison_unpythonic)  

##### Specification

```re
           ^(.*)/_type=
(   # match True, False and None
                       NameConstant
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value=(?P<SUFFIX>.+)
|   # match numbers
                       Num
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/n=(?P<SUFFIX>.+)
|   # match strings and containers
                       (?P<SUFFIX>Str|Tuple|Dict|Set|List)
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
10  {a, b, c}
11  [1, 2, 3]
12  -42
13  [1, {2, 3}, {"a": "b", "c": "d"}]
14  [foo(4)]
15  {"foo": "bar"}
16  l = [
17      first_line,
18      second_line,
19  ]
20  single_quotes = "rock'n'roll"
```

##### Matches

| Label | Lines |
|:--|:--|
| `literal:42` | 1 |
| `literal:42.0` | 2 |
| `literal:Str` | 3, 13, 13, 13, 13, 15, 15, 20 |
| `literal:1` | 4, 4, 7, 11, 13 |
| `literal:Tuple` | 4 |
| `literal:List` | 5, 11, 13, 14, 16 |
| `literal:Dict` | 6, 13, 15 |
| `literal:2` | 7, 11, 13 |
| `literal:3` | 7, 11, 13 |
| `literal:Set` | 7, 10, 13 |
| `literal:False` | 8 |
| `literal:True` | 8 |
| `literal:None` | 9 |
| `literal:-42` | 12 |
| `literal:4` | 14 |

--------------------------------------------------------------------------------

#### Feature `empty_literal`

Match `""` (empty string), `()` (empty tuple), `[]` (empty list) and `{}` (empty dictionary).

Generally speaking, all _falsey_ constants (i.e., whose [truth value](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) is `False`) can be recognized by an existing feature:
- `None`: `literal:None`;
- `False`: `literal:False`;
- null integer: `literal:0`;
- null floating-point number: `literal:0.0`;
- null complex number: `literal:0j`;
- empty string: `free_call_no_arguments:str` or `empty_literal:Str`;
- empty tuple: `free_call_no_arguments:tuple` or `empty_literal:Tuple`;
- empty list: `free_call_no_arguments:list` or `empty_literal:List`;
- empty dictionary: `free_call_no_arguments:dict` or `empty_literal:Dict`;
- empty set: `free_call_no_arguments:set`;
- empty range: `range:0`.

##### Specification

```re
           ^(.*)/_type=
(
                       (?P<SUFFIX>Str)
\n(?:\1.+\n)* \1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/s=(?=\n) # empty string
|
                       (?P<SUFFIX>Tuple|List|Dict)
\n(?:\1.+\n)* \1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/(elts|keys)/_length=0
)
```

##### Example

```python
1   ""
2   ()
3   []
4   {}
```

##### Matches

| Label | Lines |
|:--|:--|
| `empty_literal:Str` | 1 |
| `empty_literal:Tuple` | 2 |
| `empty_literal:List` | 3 |
| `empty_literal:Dict` | 4 |

--------------------------------------------------------------------------------

#### Feature `special_literal_string`

Capture any literal string containing at least one character whose codepoint is not between 32 (space) and 126 (tilde).

_Remark._ To match escape sequences in the pipeline, you must prefix the string with `r` **and** double the backslash. For instance, to keep only the programs featuring a literal `\n` (new line), write:

```python
    {
        'operation': 'include',
        'data': [
            r"type/sequence/string/literal/special/\\n",
        ],
    },
```

_Remark._ Due to a bug in third-party library `typed_ast` (corrected in Python 3.8 standard module `ast`), a multiline string is located on its last line, see example below, lines 6-9. There is no way to correct this at AST level since, apart from that, it is coded in exactly the same way as the string of line 10. The two possible resulting positions are separated by a slash in the Matches' table.

##### Specification

```re
           ^(.*)/_type=Str
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/s=(?P<SUFFIX>.*?(\\\w|[^ -~\n]).*)
```

##### Example

```python
1   emoji = "😍"
2   header = fr"Date\tStudent\tGrade\n"
3   pound = "£"
4   print("nothing special here!") # no match
5   print("\U0001F60D")
6   several_lines = """
7       first
8       second
9   """
10  several_lines_2 = "\n    first\n    second\n"
11  bytes = b"\x20" # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `special_literal_string:Date\\tStudent\\tGrade\\n` | 2 |
| `special_literal_string:£` | 3 |
| `special_literal_string:😍` | 1, 5 |
| `special_literal_string:\n    first\n    second\n` | 6, 10 / 9, 10 |

--------------------------------------------------------------------------------

#### Feature `magic_number`

Match magic numbers (unnamed numerical constants) other than -1, 0, 1 and 2. A number in the RHS of an assignment to a constant is of course ignored.

##### Derivations

[⬆️ feature `literal`](#feature-literal)  
[⬆️ feature `single_assignment`](#feature-single_assignment)  

##### Specification

```sql
SELECT "magic_number",
       n.name_suffix,
       n.span,
       n.path
FROM t_literal n
LEFT JOIN t_single_assignment a USING(span)
WHERE (a.rowid IS NULL
       OR a.name_suffix REGEXP ".*[a-z]")
  AND n.name_suffix REGEXP "(?!-1$|0$|1$|2$)-?\d+(.\d+)?(e[+-]\d+)?$"
```

##### Example

```python
1   NUMBER_OF_TEETH_OF_A_DOG = 42 # not a magic number
2   shoe_size = 42 # magic number
3   for a in s[::-1]:
4       if a == 42 and b % 2 == 0: # 42 is a magic number
5           pass
6   negative_number = -42
7
8   # May be rewritten as:
9
10  NUMBER_OF_TEETH_OF_A_DOG = 42
11  ANSWER_TO_THE_ULTIMATE_QUESTION_OF_LIFE_THE_UNIVERSE_AND_EVERYTHING = 42
12  shoe_size = ANSWER_TO_THE_ULTIMATE_QUESTION_OF_LIFE_THE_UNIVERSE_AND_EVERYTHING
13  for a in s[::-1]:
14      if a == ANSWER_TO_THE_ULTIMATE_QUESTION_OF_LIFE_THE_UNIVERSE_AND_EVERYTHING and b % 2 == 0:
15          pass
16  NEGATIVE_NUMBER = -42
```

##### Matches

| Label | Lines |
|:--|:--|
| `magic_number:-42` | 6 |
| `magic_number:42` | 2, 4 |

--------------------------------------------------------------------------------

## Subscripts

--------------------------------------------------------------------------------

#### Feature `index`

Match an index in a sequence type or a key in a dictionary type, and suffix it by either an integer or an identifier if it is atomic, or `"_"` otherwise.

##### Derivations

[⬇️ feature `find_best_element_index_unpythonic`](#feature-find_best_element_index_unpythonic)  
[⬇️ feature `find_first_good_element_index_unpythonic`](#feature-find_first_good_element_index_unpythonic)  

##### Specification

```re
           ^(.*)(?<!/annotation)/_type=Subscript
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/slice
(
                      /_type=Name
\n(?:\1.+\n)* \1/slice/id=(?P<SUFFIX>.+)
|
                      /_type=Num
\n(?:\1.+\n)* \1/slice/n=(?P<SUFFIX>.+)
|
                      /(?P<SUFFIX>_)type=(?!Slice).+
)$
```

##### Example

```python
1   a[42]
2   dictionary[key]
3   a[42:-1] # no match
4   a[i + 1]
5   def abs(l: List[int]) -> int: # no match
6       pass
7   a[i]
```

##### Matches

| Label | Lines |
|:--|:--|
| `index:42` | 1 |
| `index:key` | 2 |
| `index:_` | 4 |
| `index:i` | 7 |

--------------------------------------------------------------------------------

#### Feature `nested_index`

Count consecutive indexes, e.g. `...[i][j]...`.

##### Derivations

[⬇️ feature `index_shape`](#feature-index_shape)  

##### Specification

```re
           ^(.*)(?<!/annotation)/_type=Subscript
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value/_type=Subscript
\n(?:\1.+\n)*?\1/value/_pos=(?P<POS>.+)
```

##### Example

```python
1   a[i] # no match
2   a[i][j]
3   a[i][j][k:l]
4   a[i][j][k][l]
5   a[i][j][k][l][m]
6   a[i][j][k][l][m][n]
7   a[i][j] + b[i][j][k]
```

##### Matches

| Label | Lines |
|:--|:--|
| `nested_index` | 2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7 |

--------------------------------------------------------------------------------

#### Feature `index_shape`

In pure Python, multidimensionnal arrays are lists of lists. Thus, accessing a cell (_i_, _j_) of a matrix _m_ is done first by accessing the _i_-th list of _m_ (`m[i]`), then the _j_-th cell of this list (`m[i][j]`). The length of this index concatenation gives the dimension (or _shape_) of the array.

##### Derivations

[⬆️ feature `nested_index`](#feature-nested_index)  

##### Specification

```sql
SELECT "index_shape",
       count(*) + 1,
       i2.span,
       i2.path
FROM t_nested_index i1
JOIN t_nested_index i2 ON (i2.path GLOB i1.path || "*")
WHERE NOT EXISTS
    (SELECT *
     FROM t_nested_index i0
     WHERE (i1.path REGEXP i0.path || "\d+-$") )
GROUP BY i1.path
ORDER BY i1.path
```

##### Example

```python
1   a[i] # no match
2   a[i][j]
3   a[i][j][k:l]
4   a[i][j][k][l]
5   a[i][j][k][l][m]
6   a[i][j][k][l][m][n]
7   a[i][j] + b[i][j][k]
```

##### Matches

| Label | Lines |
|:--|:--|
| `index_shape:2` | 2, 7 |
| `index_shape:3` | 3, 7 |
| `index_shape:4` | 4 |
| `index_shape:5` | 5 |
| `index_shape:6` | 6 |

--------------------------------------------------------------------------------

#### Feature `index_arithmetic`

##### Specification

```re
           ^(.*)/_type=Subscript
\n(?:\1.+\n)*?\1/slice/_type=BinOp
\n(?:\1.+\n)*?\1/slice/_pos=(?P<POS>.+)
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
           ^(.*)/_type=Subscript
(   # A negative number
\n(?:\1.+\n)*?\1/slice/_type=Num
\n(?:\1.+\n)*?\1/slice/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/slice/n=(?P<SUFFIX>-\d+)
|   # A negated non-literal expression
\n(?:\1.+\n)*?\1/slice/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/slice/op/_type=USub
|   # A binary operation whose left operand is negated
\n(?:\1.+\n)*?\1/slice/_type=BinOp
\n(?:\1.+\n)*?\1/slice/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/slice/left/_type=UnaryOp
\n(?:\1.+\n)*?\1/slice/left/op/_type=USub
|   # A complemented expression
\n(?:\1.+\n)*?\1/slice/_type=UnaryOp
\n(?:\1.+\n)*?\1/slice/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/slice/op/_type=Invert
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

_Remark._ In line 4, `~i` evaluates to `-i - 1` (bitwise complement of `i`). Line 3 could be rewritten as `a[-i]`.

##### Matches

| Label | Lines |
|:--|:--|
| `negative_index:-1` | 1 |
| `negative_index` | 2, 4, 5 |

--------------------------------------------------------------------------------

#### Feature `slice_lower`

Match the lower bound of a slice, and suffix it by either `""` if it is omitted, an integer or an identifier if is is atomic, or `"_"` otherwise.

##### Derivations

[⬇️ feature `slice`](#feature-slice)  

##### Specification

```re
           ^(.*)/_type=Subscript
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/slice/lower
(
                            =None(?P<SUFFIX>)
|
                            /_type=Name
\n(?:\1.+\n)* \1/slice/lower/id=(?P<SUFFIX>.+)
|
                            /_type=Num
\n(?:\1.+\n)* \1/slice/lower/n=(?P<SUFFIX>.+)
|
                            /(?P<SUFFIX>_)type=.+
)$
```

##### Example

```python
1   a[:stop1]
2   a[start2:]
3   a[start3:stop3]
4   a[start4:stop4:step4]
5   a[foo(bar):fizz(buzz)]
6   a[0:2 * n:100]
7   a[:]
8   a[::2]
9   a[::-1]
```

##### Matches

| Label | Lines |
|:--|:--|
| `slice_lower:` | 1, 7, 8, 9 |
| `slice_lower:start2` | 2 |
| `slice_lower:start3` | 3 |
| `slice_lower:start4` | 4 |
| `slice_lower:_` | 5 |
| `slice_lower:0` | 6 |

--------------------------------------------------------------------------------

#### Feature `slice_upper`

Match the upper bound of a slice, and suffix it by either `""` if it is omitted, an integer or an identifier if it is atomic, or `"_"` otherwise.

##### Derivations

[⬇️ feature `slice`](#feature-slice)  

##### Specification

```re
           ^(.*)/_type=Subscript
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/slice/upper
(
                            =None(?P<SUFFIX>)
|
                            /_type=Name
\n(?:\1.+\n)* \1/slice/upper/id=(?P<SUFFIX>.+)
|
                            /_type=Num
\n(?:\1.+\n)* \1/slice/upper/n=(?P<SUFFIX>.+)
|
                            /(?P<SUFFIX>_)type=.+
)$
```

##### Example

```python
1   a[:stop1]
2   a[start2:]
3   a[start3:stop3]
4   a[start4:stop4:step4]
5   a[foo(bar):fizz(buzz)]
6   a[0:2 * n:100]
7   a[:]
8   a[::2]
9   a[::-1]
```

##### Matches

| Label | Lines |
|:--|:--|
| `slice_upper:stop1` | 1 |
| `slice_upper:` | 2, 7, 8, 9 |
| `slice_upper:stop3` | 3 |
| `slice_upper:stop4` | 4 |
| `slice_upper:_` | 5, 6 |

--------------------------------------------------------------------------------

#### Feature `slice_step`

Match the step of a slice, and suffix it by either `""` if it is omitted, an integer or an identifier if it is atomic, or `"_"` otherwise.

##### Derivations

[⬇️ feature `slice`](#feature-slice)  

##### Specification

```re
           ^(.*)/_type=Subscript
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/slice/step
(
                            =None(?P<SUFFIX>)
|
                            /_type=Name
\n(?:\1.+\n)* \1/slice/step/id=(?P<SUFFIX>.+)
|
                            /_type=Num
\n(?:\1.+\n)* \1/slice/step/n=(?P<SUFFIX>.+)
|
                            /(?P<SUFFIX>_)type=.+
)$
```

##### Example

```python
1   a[:stop1]
2   a[start2:]
3   a[start3:stop3]
4   a[start4:stop4:step4]
5   a[foo(bar):fizz(buzz)]
6   a[0:2 * n:100]
7   a[:]
8   a[::2]
9   a[::-1]
```

##### Matches

| Label | Lines |
|:--|:--|
| `slice_step:` | 1, 2, 3, 5, 7 |
| `slice_step:step4` | 4 |
| `slice_step:100` | 6 |
| `slice_step:2` | 8 |
| `slice_step:-1` | 9 |

--------------------------------------------------------------------------------

#### Feature `slice`

Match a slice, and suffix it with three parts, either empty, atomic or replaced by an underscore: the lower bound, the upper bound and the step.

##### Derivations

[⬆️ feature `slice_lower`](#feature-slice_lower)  
[⬆️ feature `slice_step`](#feature-slice_step)  
[⬆️ feature `slice_upper`](#feature-slice_upper)  

##### Specification

```sql
SELECT "slice",
       lo.name_suffix || ":" || up.name_suffix || ":" || st.name_suffix,
       lo.span,
       lo.path
FROM t_slice_lower lo
JOIN t_slice_upper up USING (path)
JOIN t_slice_step st USING (path)
```

##### Example

```python
1   a[:stop1]
2   a[start2:]
3   a[start3:stop3]
4   a[start4:stop4:step4]
5   a[foo(bar):fizz(buzz)]
6   a[0:2 * n:100]
7   a[:]
8   a[::2]
9   a[::-1]
```

##### Matches

| Label | Lines |
|:--|:--|
| `slice::stop1:` | 1 |
| `slice:start2::` | 2 |
| `slice:start3:stop3:` | 3 |
| `slice:start4:stop4:step4` | 4 |
| `slice:_:_:` | 5 |
| `slice:0:_:100` | 6 |
| `slice:::` | 7 |
| `slice:::2` | 8 |
| `slice:::-1` | 9 |

--------------------------------------------------------------------------------

## Operators

--------------------------------------------------------------------------------

#### Feature `unary_operator`

##### Specification

```re
           ^(.*)/_type=UnaryOp
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/op/_type=(?P<SUFFIX>.+)
```

##### Example

```python
1   a = -b
2   b = not c
3   c = -1 # no match
```

_Remark._ A negative literal is represented in the AST by a node `UnaryOp` with `USub` and `Num` children, and a _positive_ value for `n`. Our pre-processing of the AST simplifies this into a node `Num` and a _negative_ value for `n`.

##### Matches

| Label | Lines |
|:--|:--|
| `unary_operator:USub` | 1 |
| `unary_operator:Not` | 2 |

--------------------------------------------------------------------------------

#### Feature `binary_operator`

##### Derivations

[⬇️ feature `addition_operator`](#feature-addition_operator)  
[⬇️ feature `concatenation_operator|replication_operator`](#feature-concatenation_operatorreplication_operator)  
[⬇️ feature `modulo_operator`](#feature-modulo_operator)  
[⬇️ feature `multiplication_operator`](#feature-multiplication_operator)  
[⬇️ feature `string_formatting_operator`](#feature-string_formatting_operator)  

##### Specification

```re
           ^(.*)/_type=BinOp
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/op/_type=(?P<SUFFIX>.+)
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

#### Feature `concatenation_operator|replication_operator`

Match replication operators whose one operand is either a string, a list or a tuple **literal**. Match their augmented assignment version too (although it should belong to the [Statements section](#statements)).

##### Derivations

[⬆️ feature `augmented_assignment`](#feature-augmented_assignment)  
[⬆️ feature `binary_operator`](#feature-binary_operator)  
[⬆️ feature `literal`](#feature-literal)  
[⬇️ feature `addition_operator`](#feature-addition_operator)  
[⬇️ feature `multiplication_operator`](#feature-multiplication_operator)  

##### Specification

```sql
SELECT CASE op.name_suffix
           WHEN "Add" THEN "concatenation_operator"
           ELSE "replication_operator"
       END,
       lit.name_suffix,
       op.span,
       op.path
FROM
  (SELECT *
   FROM t_binary_operator
   UNION ALL SELECT *
   FROM t_augmented_assignment) op
JOIN t_literal lit ON (lit.path REGEXP op.path || "\d+-$")
WHERE op.name_suffix IN ("Mult",
                         "Add")
  AND lit.name_suffix IN ("List",
                          "Str",
                          "Tuple")
GROUP BY op.path
```

##### Example

```python
1   print("foo" + "bar")
2   l = l + [1]
3   l += [1]
4   print("-" * 80)
5   a = [0] * 80
6   b = 80 * [0]
7   c = (1, 2, 3) * n
8   print("Fizz" * (i % 3 == 0) + "Buzz" * (i % 5 == 0) or i)
```

##### Matches

| Label | Lines |
|:--|:--|
| `concatenation_operator:Str` | 1 |
| `concatenation_operator:List` | 2, 3 |
| `replication_operator:Str` | 4, 8, 8 |
| `replication_operator:List` | 5, 6 |
| `replication_operator:Tuple` | 7 |

--------------------------------------------------------------------------------

#### Feature `string_formatting_operator`

Match old-style `%` operators whose left operand is a string **literal**.

##### Derivations

[⬆️ feature `binary_operator`](#feature-binary_operator)  
[⬆️ feature `literal`](#feature-literal)  
[⬇️ feature `modulo_operator`](#feature-modulo_operator)  

##### Specification

```sql
SELECT "string_formatting_operator",
       "",
       op.span,
       op.path
FROM t_binary_operator op
JOIN t_literal lit ON (lit.path REGEXP op.path || "\d+-$")
WHERE op.name_suffix = "Mod"
  AND lit.name_suffix = "Str"
GROUP BY op.path
```

##### Example

```python
1   s = "hello, %s" % world
2   n = n % 10 # no match
3   print(a % b) # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `string_formatting_operator` | 1 |

--------------------------------------------------------------------------------

#### Feature `addition_operator`

An addition operator is a binary operator `Add` which has not be classified as a concatenation operator.

##### Derivations

[⬆️ feature `binary_operator`](#feature-binary_operator)  
[⬆️ feature `concatenation_operator|replication_operator`](#feature-concatenation_operatorreplication_operator)  

##### Specification

```sql
SELECT "addition_operator",
       "",
       op.span,
       op.path
FROM t_binary_operator op
LEFT JOIN t_concatenation_operator con ON (op.span = con.span)
WHERE op.name_suffix="Add"
  AND con.span IS NULL
```

##### Example

```python
1   print("foo" + "bar")
2   l = l + [1]
3   l += [1]
4   print(a + 1)
```

##### Matches

| Label | Lines |
|:--|:--|
| `addition_operator` | 4 |

--------------------------------------------------------------------------------

#### Feature `multiplication_operator`

A multiplication operator is a binary operator `Mult` which has not be classified as a replication operator.

##### Derivations

[⬆️ feature `binary_operator`](#feature-binary_operator)  
[⬆️ feature `concatenation_operator|replication_operator`](#feature-concatenation_operatorreplication_operator)  

##### Specification

```sql
SELECT "multiplication_operator",
       "",
       op.span,
       op.path
FROM t_binary_operator op
LEFT JOIN t_replication_operator rep ON (op.path = rep.path)
WHERE rep.span IS NULL
  AND op.name_suffix="Mult"
```

##### Example

```python
1   print("-" * 80)
2   print(a * b)
3   c = (1, 2, 3) * n
```

##### Matches

| Label | Lines |
|:--|:--|
| `multiplication_operator` | 2 |

--------------------------------------------------------------------------------

#### Feature `modulo_operator`

A modulo operator is a binary operator `Mod` which has not be classified as an old-style format operator.

##### Derivations

[⬆️ feature `binary_operator`](#feature-binary_operator)  
[⬆️ feature `string_formatting_operator`](#feature-string_formatting_operator)  

##### Specification

```sql
SELECT "modulo_operator",
       "",
       op.span,
       op.path
FROM t_binary_operator op
LEFT JOIN t_string_formatting_operator f ON (op.path = f.path)
WHERE f.span IS NULL
  AND op.name_suffix="Mod"
```

##### Example

```python
1   s = "hello, %s" % world
2   n = n % 10
3   print(a % b)
```

##### Matches

| Label | Lines |
|:--|:--|
| `modulo_operator` | 2, 3 |

--------------------------------------------------------------------------------

## Boolean expressions

--------------------------------------------------------------------------------

#### Feature `boolean_operator`

##### Specification

```re
           ^(.*)/_type=BoolOp
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/op/_type=(?P<SUFFIX>.+)
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

_Remark._ `Not` is not a boolean operator in Python. To match it, use [feature `unary_operator:Not`](#feature-unary_operator).

--------------------------------------------------------------------------------

#### Feature `comparison_operator`

##### Derivations

[⬇️ feature `chained_equalities|chained_inequalities`](#feature-chained_equalitieschained_inequalities)  
[⬇️ feature `yoda_comparison_unpythonic`](#feature-yoda_comparison_unpythonic)  

##### Specification

```re
           ^(.*)/ops/        (?P<_1>\d+)/_type=(?P<SUFFIX>Eq|Lt|LtE|Gt|GtE|In|NotIn|NotEq|Is|IsNot)
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

#### Feature `yoda_comparison_unpythonic`

The so-called Yoda style puts the literal operand on the left side of a comparison. Although generally not recommended, this order is sometimes natural or even mandatory for certain non-commutative operators (see examples below).

##### Derivations

[⬆️ feature `comparison_operator`](#feature-comparison_operator)  
[⬆️ feature `literal`](#feature-literal)  

##### Specification

```sql
SELECT "yoda_comparison_unpythonic",
       c.name_suffix,
       c.span,
       c.path
FROM t_comparison_operator c
JOIN t_literal lit ON (c.span = lit.span
                       AND c.path GLOB "*-2-1-"
                       AND lit.path GLOB "*-0-")
WHERE c.name_suffix NOT REGEXP "In|NotIn|Lt|LtE"
  AND substr(c.path, 1, length(c.path)-4) == substr(lit.path, 1, length(lit.path)-2)
  AND c.path NOT IN -- ensure that the RHS is not itself a literal
    (SELECT path
     FROM t_literal)
```

##### Example

```python
1   assert 0 == x # match
2   assert x == 0 # no match
3   if "A" <= symbol <= "Z": # no match
4       pass
5   assert (a, b) == (c, d) # no match, since the RHS is a literal too
6   assert "needle" not in haystack # no match: this is the only possible order
7   assert 5 > x # match: x < 5 would be more natural
8   assert 5 < x # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `yoda_comparison_unpythonic:Eq` | 1 |
| `yoda_comparison_unpythonic:Gt` | 7 |

--------------------------------------------------------------------------------

#### Feature `chained_comparison`

##### Derivations

[⬇️ feature `chained_equalities|chained_inequalities`](#feature-chained_equalitieschained_inequalities)  

##### Specification

```re
           ^(.*)/_type=Compare
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/comparators/_length=(?!1\n)(?P<SUFFIX>.+)
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

#### Feature `chained_comparison_unpythonic`

##### Specification

```re
           ^(.*)/_type=BoolOp
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/op/_type=And
\n(?:\1.+\n)*?\1/values/1/_type=Compare
\n(?:\1.+\n)*?\1/values/1/comparators/1/_hash=(?P<HASH_1>.+) # capture the right operand of the left comparison
\n(?:\1.+\n)*?\1/values/2/_type=Compare
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
| `chained_comparison_unpythonic` | 1, 2, 3, 4 |

--------------------------------------------------------------------------------

#### Feature `chained_equalities|chained_inequalities`

##### Derivations

[⬆️ feature `chained_comparison`](#feature-chained_comparison)  
[⬆️ feature `comparison_operator`](#feature-comparison_operator)  

##### Specification

```sql
SELECT CASE op.name_suffix
           WHEN "Eq" THEN "chained_equalities"
           ELSE "chained_inequalities"
       END,
       count(*),
       c.span,
       c.path
FROM t_chained_comparison c
JOIN t_comparison_operator op ON (op.path GLOB c.path || "*-")
WHERE op.name_suffix REGEXP "(Eq|Lt|LtE|Gt|GtE)$"
GROUP BY c.path,
         op.name_suffix
HAVING count(*) > 1 -- a chain has at least two operators
ORDER BY c.path
```

_Remark._ Note the user-defined function `REGEXP` in the `WHERE`clause. It calls the function `match()` of the third-party [`regex`](https://pypi.org/project/regex/) library.

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
           ^(.*)/_type=Compare
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/left/op/_type=Mod
(   # try to match the % right operand with a number
\n(?:\1.+\n)*?\1/left/right/n=(?P<SUFFIX>.+)
)?
\n(?:\1.+\n)*?\1/ops/_length=1
\n(?:\1.+\n)*?\1/ops/1/_type=(Eq|NotEq)
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

When the value of the left operand suffices to determine the value of a boolean expression, short-circuit evaluation skips the right operand. This behaviour is sometimes desirable or even required, but Paroxython currently cannot detect the case: so, when commutating the operands would result in an error or a performance penalty, you should add manually the hint `# paroxython: short_circuit` in the source code. The suffix shoud be either `And`, `Or` or omitted.

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

### Generalities

--------------------------------------------------------------------------------

#### Feature `argument`

Match any argument of a free call or a member call. Suffix this argument when it is **atomic**, i.e. either:
- an identifier,
- a number literal,
- `True`, `False` or `None`.
Otherwise, suffix it with an empty string.

##### Derivations

[⬇️ feature `range`](#feature-range)  
[⬇️ feature `update_by_member_call`](#feature-update_by_member_call)  

##### Specification

```re
           ^(.*)/_type=Call
(
\n(?:\1.+\n)*?\1/(?P<_1>(args/\d+|keywords/\d+/value))/_pos=(?P<POS>.+)
\n            \1/(?P=_1)         /(   # the next line denotes either an atomic argument
                                    (value|n|id)?=(?P<SUFFIX>.+) # capture it as suffix
                                    | # or a non-atomic argument
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
6   buzz(x, 42, foo=1)
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
| `argument:` | 2, 7, 8 |
| `argument:None` | 3 |
| `argument:True` | 4 |
| `argument:1` | 6 |
| `argument:42` | 5, 6, 8 |
| `argument:x` | 6, 8 |
| `argument:a` | 9 |
| `argument:b` | 9 |
| `argument:c` | 9 |
| `argument:bizz` | 10 |
| `argument:buzz` | 10 |
| `argument:g` | 12 |

--------------------------------------------------------------------------------

#### Feature `keyword_argument`

##### Derivations

[⬇️ feature `free_call_with_keyword_argument`](#feature-free_call_with_keyword_argument)  

##### Specification

```re
           ^(.*)/_type=Call
(
\n(?:\1.+\n)*?\1/(?P<_1>keywords/\d+)/arg=(?P<SUFFIX>.+)
\n(?:\1.+\n)*?\1/(?P=_1)             /value/_pos=(?P<POS>.+)
)+ # at least one keyword argument
```

##### Example

```python
1   print("hello", "world", sep=" ", end="\n", file=sys.stderr, flush=True)
```

##### Matches

| Label | Lines |
|:--|:--|
| `argument:` | 1, 1, 1, 1, 1 |
| `argument:True` | 1 |
| `keyword_argument:end` | 1 |
| `keyword_argument:file` | 1 |
| `keyword_argument:flush` | 1 |
| `keyword_argument:sep` | 1 |

--------------------------------------------------------------------------------

#### Feature `composition`

Apply a function or a method to an expression involving the result of another function or method application, without using an intermediate variable.

##### Specification

```re
           ^(.*)/_type=Call
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/args/[^=]+/_type=Call
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

### Calls of the form `callable(arguments)`

In Python, this form can denote:

- the application of a function (generator, etc.);
- the instanciation of a class (whose name should be CamelCased), including Exceptions;
- the invocation of the method `__call__` of an object.

We use the term _free call_, as opposed to _member call_ (dot notation).

--------------------------------------------------------------------------------

#### Feature `free_call`

##### Derivations

[⬇️ feature `body_recursive_function`](#feature-body_recursive_function)  
[⬇️ feature `deeply_recursive_function`](#feature-deeply_recursive_function)  
[⬇️ feature `external_free_call`](#feature-external_free_call)  
[⬇️ feature `free_call_with_keyword_argument`](#feature-free_call_with_keyword_argument)  
[⬇️ feature `higher-order function`](#feature-higher-order-function)  
[⬇️ feature `internal_free_call`](#feature-internal_free_call)  
[⬇️ feature `pure_function`](#feature-pure_function)  
[⬇️ feature `range`](#feature-range)  
[⬇️ feature `recursive_call_count`](#feature-recursive_call_count)  
[⬇️ feature `recursive_function`](#feature-recursive_function)  

##### Specification

```re
           ^(.*)/_type=Call
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/func/id=(?P<SUFFIX>.+)
```

##### Example

```python
1   foo(a, b, c)
2   bar()
3   buzz(x, 2)
4   fizz(foobar(x), 2)
5   baz.qux() # no match, see feature member_call_method
```

##### Matches

| Label | Lines |
|:--|:--|
| `free_call:foo` | 1 |
| `free_call:bar` | 2 |
| `free_call:buzz` | 3 |
| `free_call:fizz` | 4 |
| `free_call:foobar` | 4 |

--------------------------------------------------------------------------------

#### Feature `free_call_with_keyword_argument`

##### Derivations

[⬆️ feature `free_call`](#feature-free_call)  
[⬆️ feature `keyword_argument`](#feature-keyword_argument)  

##### Specification

```sql
SELECT "free_call_with_keyword_argument",
       f.name_suffix || ":" || k.name_suffix,
       f.span,
       f.path
FROM t_free_call f
JOIN t_keyword_argument k ON (k.path GLOB f.path || "*-")
```

##### Example

```python
1   print("hello", "world", sep=" ", end="\n", file=sys.stderr, flush=True)
```

##### Matches

| Label | Lines |
|:--|:--|
| `free_call_with_keyword_argument:print:end` | 1 |
| `free_call_with_keyword_argument:print:file` | 1 |
| `free_call_with_keyword_argument:print:flush` | 1 |
| `free_call_with_keyword_argument:print:sep` | 1 |

--------------------------------------------------------------------------------

#### Feature `free_call_without_result`

##### Specification

```re
^(.*/(?:body|orelse|loopelse)/\d+)/_type=Expr
\n(?:\1.+\n)*?\1                  /value/_type=Call
\n(?:\1.+\n)*?\1                  /value/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1                  /value/func/id=(?P<SUFFIX>.+)
```

##### Example

```python
1   a = foo(a, b, c) # no match
2   return bar() # no match
3   1 + buzz(x, 2) # no match
4   fizz(foobar(x), 2) # match for fizz, no match for foobar
5   baz.qux() # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `free_call_without_result:fizz` | 4 |

--------------------------------------------------------------------------------

#### Feature `free_call_no_arguments`

##### Specification

```re
           ^(.*)/_type=Call
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/func/id=(?P<SUFFIX>.+)
\n(?:\1.+\n)*?\1/args/_length=0
\n(?:\1.+\n)*?\1/keywords/_length=0
```

##### Example

```python
1   foo()
2   bar(x=1) # no match
3   baz.qux() # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `free_call_no_arguments:foo` | 1 |

--------------------------------------------------------------------------------

#### Feature `free_tail_call`

A tail call is a call whose result is immediately returned, without any further calculation. This property is not interesting as such, but will be used below as a basis for the recognition of tail recursive functions.

##### Derivations

[⬇️ feature `body_recursive_function`](#feature-body_recursive_function)  

##### Specification

```re
           ^(.*)/_type=Return
\n(?:\1.+\n)*?\1/value/(
                       _type=Call
\n(?:\1.+\n)*?\1/value/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value/func/_type=Name
\n(?:\1.+\n)*?\1/value/func/id=(?P<SUFFIX>.+)
                       |
                       _type=BoolOp
\n(?:\1.+\n)*?\1/value/values/_length=(?P<LENGTH>\d+)
\n(?:\1.+\n)*?\1/value/values/(?P=LENGTH)/_type=Call
\n(?:\1.+\n)*?\1/value/values/(?P=LENGTH)/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value/values/(?P=LENGTH)/func/id=(?P<SUFFIX>.+)
                       |
                       _type=IfExp
(
\n(?:\1.+\n)*?\1/value/(?P<_1>body|orelse)/_type=Call
\n(?:\1.+\n)*?\1/value/(?P=_1)            /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value/(?P=_1)            /func/_type=Name
\n(?:\1.+\n)*?\1/value/(?P=_1)            /func/id=(?P<SUFFIX>.+)
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

_Remark._ Since the short-circuit expression `c and foo(m)` is equivalent to the conditional expression `if c then foo(m) else False`, `foo(m)` is actually a tail call.

##### Matches

| Label | Lines |
|:--|:--|
| `free_tail_call:foo` | 2, 3, 4, 5, 6, 7, 8, 8 |

--------------------------------------------------------------------------------

#### Feature `internal_free_call`

##### Derivations

[⬆️ feature `free_call`](#feature-free_call)  
[⬆️ feature `function`](#feature-function)  
[⬇️ feature `external_free_call`](#feature-external_free_call)  

##### Specification

```sql
SELECT "internal_free_call",
       c.name_suffix,
       c.span,
       c.path
FROM t_function f
JOIN t_free_call c USING (name_suffix)
```

##### Example

```python
1   from external import bizz
2
3   def foo():
4       def buzz():
5           pass
6
7   foo()
8   bar()
9   buzz()
10  bizz()
11
12  def bar():
13      pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `internal_free_call:bar` | 8 |
| `internal_free_call:buzz` | 9 |
| `internal_free_call:foo` | 7 |

--------------------------------------------------------------------------------

#### Feature `external_free_call`

##### Derivations

[⬆️ feature `free_call`](#feature-free_call)  
[⬆️ feature `internal_free_call`](#feature-internal_free_call)  

##### Specification

```sql
SELECT "external_free_call",
       c.name_suffix,
       c.span,
       c.path
FROM t_free_call c
LEFT JOIN t_internal_free_call USING(name_suffix)
WHERE t_internal_free_call.name_suffix IS NULL
```

##### Example

```python
1   from external import bizz
2
3   def foo():
4       def buzz():
5           pass
6
7   foo()
8   bar()
9   buzz()
10  bizz()
11
12  def bar():
13      pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `external_free_call:bizz` | 10 |

--------------------------------------------------------------------------------

### Calls of the form `identifier.callable(arguments)`

In Python, `identifier` can be the name of:
- a class instance (here, `callable` is a method name);
- a module (inside which `callable(arguments)` would be a free call);
- a `namedtuple` instance (in the rare case where an element would be callable).

--------------------------------------------------------------------------------

#### Feature `member_call_method`

##### Derivations

[⬇️ feature `member_call`](#feature-member_call)  
[⬇️ feature `update_by_member_call`](#feature-update_by_member_call)  
[⬇️ feature `update_by_member_call_with`](#feature-update_by_member_call_with)  

##### Specification

```re
           ^(.*)/_type=Call
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/func/attr=(?P<SUFFIX>.+)
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
| `member_call_method:index` | 1 |

--------------------------------------------------------------------------------

#### Feature `member_call_object`

##### Derivations

[⬇️ feature `member_call`](#feature-member_call)  
[⬇️ feature `update_by_member_call`](#feature-update_by_member_call)  

##### Specification

```re
           ^(.*)/value/_type=Call
\n(?:\1.+\n)*?\1/value/func/_type=Attribute
\n(?:\1.+\n)*?\1/value/func/value/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/value/func/value/id=(?P<SUFFIX>.+)
```

##### Example

```python
1   seq.index(42)
2   foo(bar)  # no match
3   seq.index # no match
4   a.b.c() # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `member_call_object:seq` | 1 |

--------------------------------------------------------------------------------

#### Feature `member_call`

##### Derivations

[⬆️ feature `member_call_method`](#feature-member_call_method)  
[⬆️ feature `member_call_object`](#feature-member_call_object)  

##### Specification

```sql
SELECT "member_call",
       o.name_suffix || ":" || m.name_suffix,
       o.span,
       o.path
FROM t_member_call_object AS o
JOIN t_member_call_method AS m ON (o.span = m.span)
```

**Remark.** A first version of this query was joining on the paths. This resulted in false positives when a `member_call_method:(type):(method)` was manually hinted for duck-typing resolution (due to the fact that an added label lacks a path). Testing on the span is less accurate, but seems to work (cf. lines 3-4 below).

##### Example

```python
1   foo.add(a)
2   seq.append(int(s))
3   foo\
4       .add(a)
```

##### Matches

| Label | Lines |
|:--|:--|
| `member_call:foo:add` | 1, 3 |
| `member_call:seq:append` | 2 |

--------------------------------------------------------------------------------

#### Feature `method_chaining`

##### Specification

```re
           ^(.*)/_type=Call
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/func/_type=Attribute
\n(?:\1.+\n)*?\1/func/value/_type=Call
\n(?:\1.+\n)*?\1/func/value/func/_type=Attribute
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

## Iterables

--------------------------------------------------------------------------------

#### Feature `range`

Match a call to `range()` and suffix it by its [_atomic_](#feature-argument) arguments, separated by a colon. Non-atomic arguments are replaced by `_`.

##### Derivations

[⬆️ feature `argument`](#feature-argument)  
[⬆️ feature `free_call`](#feature-free_call)  
[⬇️ feature `for_range`](#feature-for_range)  

##### Specification

```sql
SELECT "range",
       group_concat(name_suffix, ":"),
       span,
       path
FROM -- Only a subquery permits to sort the arguments before grouping them together.
  (SELECT f.rowid AS rowid,
          CASE arg.name_suffix
              WHEN "" THEN "_"
              ELSE arg.name_suffix
          END AS name_suffix,
          f.span AS span,
          f.path AS path
   FROM t_free_call f
   JOIN t_argument arg ON (arg.path GLOB f.path || "*-")
   WHERE f.name_suffix = "range"
     AND length(f.path) + 4 = length(arg.path) -- Ensure that arg is a (direct) argument of range().
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

##### Derivations

[⬇️ feature `local_scope`](#feature-local_scope)  
[⬇️ feature `scope`](#feature-scope)  

##### Specification

```re
           ^(.*)/_type=((?P<SUFFIX>List|Dict|Set)Comp|(?P<SUFFIX>Generator)Exp)
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
           ^(.*)/_type=(ListComp|DictComp|SetComp|GeneratorExp)
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/generators/_length=(?P<SUFFIX>\d+)
```

##### Example

```python
1   print([x for x in seq])
2   seq1 = [2, 3, 5]
3   seq2 = [7, 11]
4   acc = [i * j for i in seq1 for j in seq2]
5   acc2 = [[x1 * x2 for x1 in seq1] for x2 in seq2]
```

_Remark._ Both lines 4 and 5 can be expressed with two nested `for` statements. However, the former uses one single accumulator and produces a list of numbers:

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

## Common expressions

--------------------------------------------------------------------------------

#### Feature `mid_value_naive`

Computing the middle value between two bounds is a basic step of both binary search and merge sort. The naive way to do this may overflow, as explained in [this famous blog post](https://ai.googleblog.com/2006/06/extra-extra-read-all-about-it-nearly.html). The recommended approach is given in the next subsection.

##### Specification

```re
^(.*/(assign)?value)/_type=BinOp
\n(?:\1.+\n)*?\1    /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1    /left/left/_type=Name
\n(?:\1.+\n)*?\1    /left/op/_type=Add
\n(?:\1.+\n)*?\1    /left/right/_type=Name
\n(?:\1.+\n)*?\1    /op/_type=(Floor)?Div
\n(?:\1.+\n)*?\1    /right/n=2
```

##### Example

```python
1   x = (lo + hi) / 2
2   (lo + hi) // 2
3   a + (b + c) / 2 # no match: the expression must be isolated
4   x = (lo + hi) * 0.5 # LIMITATION: no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `mid_value_naive` | 1, 2 |

--------------------------------------------------------------------------------

#### Feature `mid_value_recommended`

##### Specification

```re
^(.*/(assign)?value)/_type=BinOp
\n(?:\1.+\n)*?\1    /_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1    /left/_type=Name
\n(?:\1.+\n)*?\1    /left/_hash=(?P<HASH>.+) # capture _hash
\n(?:\1.+\n)*?\1    /op/_type=Add
\n(?:\1.+\n)*?\1    /right/left/left/_type=Name
\n(?:\1.+\n)*?\1    /right/left/op/_type=Sub
\n(?:\1.+\n)*?\1    /right/left/right/_hash=(?P=HASH) # match _hash
\n(?:\1.+\n)*?\1    /right/op/_type=(Floor)?Div
\n(?:\1.+\n)*?\1    /right/right/n=2
```

##### Example

```python
1   mid = low + (high - low) / 2
2   low + (high - low) // 2
3   (high - low) / 2 + low # LIMITATION: no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `mid_value_recommended` | 1, 2 |

--------------------------------------------------------------------------------

#### Feature `clamp_min_max`

##### Specification

```re
           ^(.*)/_type=Call
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/func/id=(?P<FN>(max|min))
\n(?:\1.+\n)*?\1/args/_length=2
\n(?:\1.+\n)*?\1/args/[12]/func/id=(?!(?P=FN))(max|min)
\n(?:\1.+\n)*?\1/args/[12]/args/_length=2
```

##### Example

```python
1   max(min(x, upper_bound), lower_bound)
2   max(lower_bound, min(upper_bound, x))
3   min(max(x, lower_bound), upper_bound)
4   min(upper_bound, max(lower_bound, x))
5   min(upper_bound, min(lower_bound, x)) # no match
6   x = max(min(x, upper_bound), lower_bound)
```

##### Matches

| Label | Lines |
|:--|:--|
| `clamp_min_max` | 1, 2, 3, 4, 6 |

--------------------------------------------------------------------------------

#### Feature `clamp_ternary`

##### Specification

```re
           ^(.*)/_type=IfExp
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/test/left/_hash=(?P<HASH_1>.+) # capture _hash #1
\n(?:\1.+\n)*?\1/test/ops/1/_type=(?P<OP>Lt|Gt)E?
\n(?:\1.+\n)*?\1/test/comparators/1/_hash=(?P<HASH_2>.+) # capture _hash #2
\n(?:\1.+\n)*?\1/body/_hash=(?P=HASH_2) # match _hash #2
\n(?:\1.+\n)*?\1/orelse/_type=IfExp
\n(?:\1.+\n)*?\1/orelse/test/left/_hash=(?P=HASH_1) # match _hash #1
\n(?:\1.+\n)*?\1/orelse/test/ops/1/_type=(?!(?P=OP))(Lt|Gt)E?
\n(?:\1.+\n)*?\1/orelse/test/comparators/1/_hash=(?P<HASH_3>.+) # capture _hash #3
\n(?:\1.+\n)*?\1/orelse/body/_hash=(?P=HASH_3) # match _hash #3
\n(?:\1.+\n)*?\1/orelse/orelse/_hash=(?P=HASH_1) # match _hash #1
```

##### Example

```python
1   a = upper_bound if x > upper_bound else (lower_bound if x < lower_bound else x)
2   upper_bound if x >= upper_bound else (lower_bound if x <= lower_bound else x)
3   lower_bound if x < lower_bound else (upper_bound if x >= upper_bound else x)
4   lower_bound if lower_bound > x else (upper_bound if upper_bound < x else x) # LIMITATION: no match
```

_Limitation._ The number to be clamped must appear on the left hand side of the comparison.

##### Matches

| Label | Lines |
|:--|:--|
| `clamp_ternary` | 1, 2, 3 |

--------------------------------------------------------------------------------

# Statements

--------------------------------------------------------------------------------

#### Feature `no_operation`

##### Specification

```re
^(.*/body/\d+(?:/value)?)/_type=(Ellipsis|Pass)
\n(?:\1.+\n)*?         \1/_pos=(?P<POS>.+)
```

##### Example

```python
1   pass
2   ...
3   [1, ..., 3] # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `no_operation` | 1, 2 |

--------------------------------------------------------------------------------

## Bindings

--------------------------------------------------------------------------------

#### Feature `assignment`

##### Derivations

[⬇️ feature `functional_style`](#feature-functional_style)  
[⬇️ feature `pure_function`](#feature-pure_function)  
[⬇️ feature `update_by_assignment`](#feature-update_by_assignment)  
[⬇️ feature `update_by_assignment_with`](#feature-update_by_assignment_with)  

##### Specification

```re
           ^(.*)/_type=Assign
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assignvalue/_type=
(
                                   BinOp
\n(?:\1.+\n)*?\1/assignvalue/op/_type=(?P<SUFFIX>.+)
|
                                   Call
\n(?:\1.+\n)*?\1/assignvalue/func/(attr|id)=(?P<SUFFIX>.+)
|
                                   Num
\n(?:\1.+\n)*?\1/assignvalue/n=(?P<SUFFIX>.+)
|
                                   NameConstant
\n(?:\1.+\n)*?\1/assignvalue/value=(?P<SUFFIX>.+)
|
)
```

##### Example

```python
1   a = 42
2   (a, b) = (1, 2)
3   a[0] = b[0]
4   a = foo(a, b)
5   a = b + c * d
6   a = foo.bar(b)
```

##### Matches

| Label | Lines |
|:--|:--|
| `assignment:42` | 1 |
| `assignment` | 2, 3 |
| `assignment:foo` | 4 |
| `assignment:Add` | 5 |
| `assignment:bar` | 6 |

--------------------------------------------------------------------------------

#### Feature `subscript_assignment`

##### Derivations

[⬇️ feature `scope`](#feature-scope)  

##### Specification

```re
           ^(.*)/_type=Assign
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/assigntargets/[^=]+/slice/_type=(?P<SUFFIX>.+)
)+
```

##### Example

```python
1   a[i] = 42
2   b[i][j] = 42
3   (c[i], d[i]) = foo
4   e[i:j] = bar
5   (f[i:j], h[i:j]) = bizz
6   a[5] = 42
7   a[i + 1] = 42
8   a[foo(bar)] = 42
```

##### Matches

| Label | Lines |
|:--|:--|
| `subscript_assignment:Name` | 1, 2, 2, 3, 3 |
| `subscript_assignment:Slice` | 4, 5, 5 |
| `subscript_assignment:Num` | 6 |
| `subscript_assignment:BinOp` | 7 |
| `subscript_assignment:Call` | 8 |

--------------------------------------------------------------------------------

#### Feature `unbinding`

Deleting a name removes the binding of that name from the local or global namespace. Not to be confused with the deletion of subscriptions (see [`subscript_deletion`](#feature-subscript_deletion)) and attribute references (see [`attribute_deletion`](#feature-attribute_deletion)).

##### Specification

```re
           ^(.*)/_type=Delete
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/(?P<_1>targets/\d+)/_type=Name
\n(?:\1.+\n)*?\1/(?P=_1)            /id=(?P<SUFFIX>.+)
)+
```

##### Example

```python
1   del a
2   del b, c, d
3   del array[1] # no match
4   del e, array[2], f # match only e and f
5   del array[3:4], array[3:4:5], array[:] # no match
6   del foo.bar # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `node:Delete` | 1, 2, 3, 4, 5, 6 |
| `unbinding:a` | 1 |
| `unbinding:b` | 2 |
| `unbinding:c` | 2 |
| `unbinding:d` | 2 |
| `unbinding:e` | 4 |
| `unbinding:f` | 4 |

--------------------------------------------------------------------------------

#### Feature `subscript_deletion`

##### Specification

```re
           ^(.*)/_type=Delete
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/(?P<_1>targets/\d+)/_type=Subscript
\n(?:\1.+\n)*?\1/(?P=_1)            /slice/_type=(?P<SUFFIX>.+)
)+
```

##### Example

```python
1   del a # no match
2   del b, c, d # no match
3   del array[1]
4   del e, array[2], f
5   del array[3:4], array[3:4:5], array[:]
6   del foo.bar # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `node:Delete` | 1, 2, 3, 4, 5, 6 |
| `subscript_deletion:Num` | 3, 4 |
| `subscript_deletion:Slice` | 5, 5, 5 |

--------------------------------------------------------------------------------

#### Feature `attribute_deletion`

##### Specification

```re
           ^(.*)/_type=Delete
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/(?P<_1>targets/\d+)/_type=Attribute
\n(?:\1.+\n)*?\1/(?P=_1)            /attr=(?P<SUFFIX>.+)
)+
```

##### Example

```python
1   del a # no match
2   del b, c, d # no match
3   del array[1]  # no match
4   del e, array[2], f  # no match
5   del array[3:4], array[3:4:5], array[:]  # no match
6   del foo.bar
```

##### Matches

| Label | Lines |
|:--|:--|
| `node:Delete` | 1, 2, 3, 4, 5, 6 |
| `attribute_deletion:bar` | 6 |

--------------------------------------------------------------------------------

#### Feature `single_assignment`

##### Derivations

[⬇️ feature `find_best_element`](#feature-find_best_element)  
[⬇️ feature `find_best_element_index`](#feature-find_best_element_index)  
[⬇️ feature `find_best_element_index_unpythonic`](#feature-find_best_element_index_unpythonic)  
[⬇️ feature `magic_number`](#feature-magic_number)  

##### Specification

```re
           ^(.*)/_type=Assign
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/_length=1
\n(?:\1.+\n)*?\1/assigntargets/1/id=(?P<SUFFIX>.+)
```

##### Example

```python
1   a = b
2   c = 42
3   d[0] = e # no match
4   (f, g) = divmod(42, 7) # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `single_assignment:a` | 1 |
| `single_assignment:c` | 2 |

--------------------------------------------------------------------------------

#### Feature `parallel_assignment`

Match a tuple unpacking assignment, and suffix it with the tuple size.

##### Specification

```re
           ^(.*)/_type=Assign
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/_length=1
\n(?:\1.+\n)*?\1/assigntargets/1/_type=Tuple
\n(?:\1.+\n)*?\1/assigntargets/1/elts/_length=(?P<SUFFIX>.+)
```

##### Example

```python
1   a = b # no match
2   c = 42 # no match
3   d[0] = e # no match
4   (f, g) = divmod(42, 7)
```

##### Matches

| Label | Lines |
|:--|:--|
| `parallel_assignment:2` | 4 |

--------------------------------------------------------------------------------

#### Feature `assignment_expression`

This is Python 3.8 specific and will raise a syntax error in older versions.

##### Specification

```re
           ^(.*)/_type=NamedExpr
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/target/id=(?P<SUFFIX>.+)
```

##### Example

```python
1   if (match := pattern.search(data)) is not None:
2       pass
3   while chunk := file.read(8192):
4      process(chunk)
5   [y := f(x), y**2, y**3]
6   filtered_data = [y for x in data if (y := f(x)) is not None]
```

##### Matches

| Label | Lines |
|:--|:--|
| `assignment_expression:match` | 1 / SyntaxError |
| `assignment_expression:chunk` | 3 / SyntaxError |
| `assignment_expression:y` | 5, 6 / SyntaxError |

--------------------------------------------------------------------------------

#### Feature `augmented_assignment`

##### Derivations

[⬇️ feature `concatenation_operator|replication_operator`](#feature-concatenation_operatorreplication_operator)  
[⬇️ feature `update_by_augmented_assignment`](#feature-update_by_augmented_assignment)  
[⬇️ feature `update_by_augmented_assignment_with`](#feature-update_by_augmented_assignment_with)  

##### Specification

```re
           ^(.*)/_type=AugAssign
\n            \1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/op/_type=(?P<SUFFIX>.+)
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
| `augmented_assignment:Add` | 1, 3, 5, 7 |
| `augmented_assignment:Mult` | 4 |
| `augmented_assignment:FloorDiv` | 6 |

--------------------------------------------------------------------------------

#### Feature `augmented_assignment_unpythonic`

When the RHS of an assignment consists in a binary operation whose left operand is the target (`a = a op expr`), the statement can be shortened as `a op= expr`.

##### Specification

```re
           ^(.*)/_type=Assign
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/_length=1
\n(?:\1.+\n)*?\1/assigntargets/1/id=(?P<TARGET>.+)
\n(?:\1.+\n)*?\1/assignvalue/_type=BinOp
\n(?:\1.+\n)*?\1/assignvalue/left/id=(?P=TARGET)\b
```

##### Example

```python
1   a = a + b
2   a = a + (b + c)
3   a = b + a # no match
4   a = a + b + c # LIMITATION: no match
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
| `augmented_assignment_unpythonic` | 1, 2 |

--------------------------------------------------------------------------------

#### Feature `subscript_augmented_assignment`

##### Specification

```re
           ^(.*)/_type=AugAssign
\n            \1/_pos=(?P<POS>.+)
\n(?:\1.+\n)* \1/assigntarget/_type=Subscript
\n(?:\1.+\n)* \1/op/_type=(?P<SUFFIX>.+)
```

##### Example

```python
1   a[i] += 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `subscript_augmented_assignment:Add` | 1 |

--------------------------------------------------------------------------------

#### Feature `chained_assignment`

##### Specification

```re
           ^(.*)/_type=Assign
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/_length=(?!1\n).+
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

[⬇️ feature `access_outer_scope`](#feature-access_outer_scope)  
[⬇️ feature `accumulate_inputs`](#feature-accumulate_inputs)  
[⬇️ feature `count_elements|count_states`](#feature-count_elementscount_states)  
[⬇️ feature `count_inputs`](#feature-count_inputs)  
[⬇️ feature `count_some_elements|count_some_states`](#feature-count_some_elementscount_some_states)  
[⬇️ feature `find_best_element`](#feature-find_best_element)  
[⬇️ feature `find_best_element_index`](#feature-find_best_element_index)  
[⬇️ feature `find_best_element_index_unpythonic`](#feature-find_best_element_index_unpythonic)  
[⬇️ feature `get_valid_input`](#feature-get_valid_input)  
[⬇️ feature `scope`](#feature-scope)  
[⬇️ feature `update_by_assignment`](#feature-update_by_assignment)  
[⬇️ feature `update_by_augmented_assignment`](#feature-update_by_augmented_assignment)  

##### Specification

```re
^(.*/assigntarget(s/\d+)?(|/value|/elts/\d+|/elts/\d+/value))/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1                                             /id=(?P<SUFFIX>.+)
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

#### Feature `assignment_rhs_atom`

Capture any [_atom_](#feature-argument) appearing on the right hand side of an assignment (possibly augmented), except the function names.

##### Derivations

[⬇️ feature `find_best_element`](#feature-find_best_element)  
[⬇️ feature `find_best_element_index`](#feature-find_best_element_index)  
[⬇️ feature `find_best_element_index_unpythonic`](#feature-find_best_element_index_unpythonic)  
[⬇️ feature `update_by_assignment`](#feature-update_by_assignment)  
[⬇️ feature `update_by_augmented_assignment`](#feature-update_by_augmented_assignment)  

##### Specification

```re
^(.*/assignvalue\b.*)/_pos=(?P<POS>.+)
\n                 \1/(value|n|(?<!func/)id)=(?P<SUFFIX>.+)
```

##### Example

```python
1   a = a + b + c
2   a += a + b + c
3   a = a[b[c]]
4   a += a[b[c]]
5   a = foo(bar()) # no match
6   a += foo(bar) # matches "bar" only
7   a = a + i
8   a += i
9   a[i] = b
10  first = second = third # matches "third" only
11  a = 42
12  a = True
13  a = None
14  a = [] # no match
15  a = foo.bar(fizz) # matches "foo" and "fizz" only
```

##### Matches

| Label | Lines |
|:--|:--|
| `assignment_rhs_atom:a` | 1, 2, 3, 4, 7 |
| `assignment_rhs_atom:b` | 1, 2, 3, 4, 9 |
| `assignment_rhs_atom:c` | 1, 2, 3, 4 |
| `assignment_rhs_atom:bar` | 6 |
| `assignment_rhs_atom:i` | 7, 8 |
| `assignment_rhs_atom:third` | 10 |
| `assignment_rhs_atom:42` | 11 |
| `assignment_rhs_atom:True` | 12 |
| `assignment_rhs_atom:None` | 13 |
| `assignment_rhs_atom:foo` | 15 |
| `assignment_rhs_atom:fizz` | 15 |

--------------------------------------------------------------------------------

### Assignment idioms

--------------------------------------------------------------------------------

#### Feature `update_by_assignment`

Match the reassignment of a variable `x` and capture its name in the first part of the suffix. In the second part, match any atom distinct from `x` and participating in the update (this excludes any function name).

##### Derivations

[⬆️ feature `assignment`](#feature-assignment)  
[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `assignment_rhs_atom`](#feature-assignment_rhs_atom)  
[⬇️ feature `update`](#feature-update)  
[⬇️ feature `update_by_assignment_with`](#feature-update_by_assignment_with)  

##### Specification

```sql
SELECT "update_by_assignment",
       lhs_acc.name_suffix || ":" || rhs_var.name_suffix,
       op.span,
       op.path
FROM t_assignment AS op
JOIN t_assignment_lhs_identifier AS lhs_acc ON (lhs_acc.path GLOB op.path || "*-")
JOIN t_assignment_rhs_atom AS rhs_acc ON (rhs_acc.path GLOB op.path || "*-")
JOIN t_assignment_rhs_atom AS rhs_var ON (rhs_var.path GLOB op.path || "*-")
WHERE rhs_acc.name_suffix = lhs_acc.name_suffix -- The same identifier must appear on both LHS and RHS...
  AND rhs_acc.name_suffix != rhs_var.name_suffix -- and an atom distinct from this identifier must appear on RHS.
GROUP BY op.span,
         lhs_acc.name,
         rhs_var.name
```

##### Example

```python
1   foo = foo + a
2   bar = bar.mult(5)
3   bar = mult(bar, 5)
4   (x, y) = (y, x)
5   (a, b) = (b, a + b)
```

##### Matches

| Label | Lines |
|:--|:--|
| `update_by_assignment:foo:a` | 1 |
| `update_by_assignment:bar:5` | 2, 3 |
| `update_by_assignment:x:y` | 4 |
| `update_by_assignment:y:x` | 4 |
| `update_by_assignment:a:b` | 5 |
| `update_by_assignment:b:a` | 5 |

--------------------------------------------------------------------------------

#### Feature `update_by_augmented_assignment`

Match the augmented assignment of a variable `x` and capture its name in the first part of the suffix. In the second part, match any atom participating to the update (this excludes any function name).

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `assignment_rhs_atom`](#feature-assignment_rhs_atom)  
[⬆️ feature `augmented_assignment`](#feature-augmented_assignment)  
[⬇️ feature `update`](#feature-update)  
[⬇️ feature `update_by_augmented_assignment_with`](#feature-update_by_augmented_assignment_with)  

##### Specification

```sql
SELECT "update_by_augmented_assignment",
       lhs_acc.name_suffix || ":" || rhs_var.name_suffix,
       op.span,
       op.path
FROM t_augmented_assignment AS op
JOIN t_assignment_lhs_identifier AS lhs_acc ON (lhs_acc.path GLOB op.path || "*-")
JOIN t_assignment_rhs_atom AS rhs_var ON (rhs_var.path GLOB op.path || "*-")
GROUP BY op.span,
         lhs_acc.name,
         rhs_var.name
```

##### Example

```python
1   foo += a
2   foo += [a]
3   buzz += a + b + c
4   s *= (x - 1) / x
5   c[j] += c[i- 1]
```

##### Matches

| Label | Lines |
|:--|:--|
| `update_by_augmented_assignment:foo:a` | 1, 2 |
| `update_by_augmented_assignment:buzz:a` | 3 |
| `update_by_augmented_assignment:buzz:b` | 3 |
| `update_by_augmented_assignment:buzz:c` | 3 |
| `update_by_augmented_assignment:s:1` | 4 |
| `update_by_augmented_assignment:s:x` | 4 |
| `update_by_augmented_assignment:c:1` | 5 |
| `update_by_augmented_assignment:c:c` | 5 |
| `update_by_augmented_assignment:c:i` | 5 |

--------------------------------------------------------------------------------

#### Feature `update_by_member_call`

The method must mutate the object it is applied on. Obviously, only a handful of such methods can be statically detected.

##### Derivations

[⬆️ feature `argument`](#feature-argument)  
[⬆️ feature `member_call_method`](#feature-member_call_method)  
[⬆️ feature `member_call_object`](#feature-member_call_object)  
[⬇️ feature `update`](#feature-update)  
[⬇️ feature `update_by_member_call_with`](#feature-update_by_member_call_with)  

##### Specification

```sql
SELECT "update_by_member_call",
       lhs_acc.name_suffix || ":" || rhs_var.name_suffix,
       op.span,
       op.path
FROM t_member_call_method AS op
JOIN t_member_call_object AS lhs_acc ON (lhs_acc.path GLOB op.path || "*-")
JOIN t_argument AS rhs_var ON (rhs_var.path GLOB op.path || "*-")
WHERE rhs_var.name_suffix != ""
  AND op.name_suffix REGEXP "(append|extend|insert|add|update|remove|pop)$"
GROUP BY op.span,
         lhs_acc.name,
         rhs_var.name
```

##### Example

```python
1   foo.append(a)
2   seq.append(int(s))
```

##### Matches

| Label | Lines |
|:--|:--|
| `update_by_member_call:foo:a` | 1 |
| `update_by_member_call:seq:s` | 2 |

--------------------------------------------------------------------------------

#### Feature `update`

Match the update of a variable `x` and capture its name in the first part of the suffix. In the second part, match any atom distinct from `x` and participating to the update (this excludes any function name).

##### Derivations

[⬆️ feature `update_by_assignment`](#feature-update_by_assignment)  
[⬆️ feature `update_by_augmented_assignment`](#feature-update_by_augmented_assignment)  
[⬆️ feature `update_by_member_call`](#feature-update_by_member_call)  
[⬇️ feature `accumulate_elements`](#feature-accumulate_elements)  
[⬇️ feature `accumulate_inputs`](#feature-accumulate_inputs)  
[⬇️ feature `accumulate_some_elements`](#feature-accumulate_some_elements)  
[⬇️ feature `functional_style`](#feature-functional_style)  
[⬇️ feature `pure_function`](#feature-pure_function)  

##### Specification

```sql
SELECT "update",
       t.name_suffix,
       t.span,
       t.path
FROM t
WHERE name_prefix IN ("update_by_assignment",
                      "update_by_augmented_assignment",
                      "update_by_member_call")
```

##### Example

```python
1   foo = foo + a
2   foo += a
3   foo.append(a)
4   foo += [a]
5
6   bar = bar.mult(5)
7   bar = mult(bar, 5)
8
9   fizz = fizz.upper() # no match
10  fizz.process(a) # no match
11
12  buzz += a + b + c
13  s *= (x - 1) / x
14  c[j] += c[i- 1]
15  (x, y) = (y, x)
16  (a, b) = (b, a + b)
17  seq.append(int(s))
```

##### Matches

| Label | Lines |
|:--|:--|
| `update:foo:a` | 1, 2, 4, 3 |
| `update:bar:5` | 6, 7 |
| `update:buzz:a` | 12 |
| `update:buzz:b` | 12 |
| `update:buzz:c` | 12 |
| `update:s:1` | 13 |
| `update:s:x` | 13 |
| `update:c:1` | 14 |
| `update:c:c` | 14 |
| `update:c:i` | 14 |
| `update:x:y` | 15 |
| `update:y:x` | 15 |
| `update:a:b` | 16 |
| `update:b:a` | 16 |
| `update:seq:s` | 17 |

--------------------------------------------------------------------------------

#### Feature `update_by_assignment_with`

##### Derivations

[⬆️ feature `assignment`](#feature-assignment)  
[⬆️ feature `update_by_assignment`](#feature-update_by_assignment)  
[⬇️ feature `update_with`](#feature-update_with)  

##### Specification

```sql
SELECT "update_by_assignment_with",
       op.name_suffix,
       op.span,
       op.path
FROM t_assignment AS op
JOIN t_update_by_assignment USING (path)
GROUP BY op.path
```

##### Example

```python
1   foo = foo + a
2   bar = bar.mult(5)
3   bar = mult(bar, 5)
4   (x, y) = (y, x)
5   (a, b) = (b, a + b)
```

##### Matches

| Label | Lines |
|:--|:--|
| `update_by_assignment_with:Add` | 1 |
| `update_by_assignment_with:mult` | 2, 3 |
| `update_by_assignment_with` | 4, 5 |

--------------------------------------------------------------------------------

#### Feature `update_by_augmented_assignment_with`

##### Derivations

[⬆️ feature `augmented_assignment`](#feature-augmented_assignment)  
[⬆️ feature `update_by_augmented_assignment`](#feature-update_by_augmented_assignment)  
[⬇️ feature `update_with`](#feature-update_with)  

##### Specification

```sql
SELECT "update_by_augmented_assignment_with",
       op.name_suffix,
       op.span,
       op.path
FROM t_augmented_assignment op
JOIN t_update_by_augmented_assignment USING (path)
GROUP BY path
```

##### Example

```python
1   foo += a
2   foo += [a]
3   buzz += a + b + c
4   s *= (x - 1) / x
5   c[j] += c[i- 1]
```

##### Matches

| Label | Lines |
|:--|:--|
| `update_by_augmented_assignment_with:Add` | 1, 2, 3, 5 |
| `update_by_augmented_assignment_with:Mult` | 4 |

--------------------------------------------------------------------------------

#### Feature `update_by_member_call_with`

##### Derivations

[⬆️ feature `member_call_method`](#feature-member_call_method)  
[⬆️ feature `update_by_member_call`](#feature-update_by_member_call)  
[⬇️ feature `update_with`](#feature-update_with)  

##### Specification

```sql
SELECT "update_by_member_call_with",
       op.name_suffix,
       op.span,
       op.path
FROM t_member_call_method AS op
JOIN t_update_by_member_call USING (path)
GROUP BY op.path
```

##### Example

```python
1   foo.append(a)
2   seq.append(int(s))
```

##### Matches

| Label | Lines |
|:--|:--|
| `update_by_member_call_with:append` | 1, 2 |

--------------------------------------------------------------------------------

#### Feature `update_with`

##### Derivations

[⬆️ feature `update_by_assignment_with`](#feature-update_by_assignment_with)  
[⬆️ feature `update_by_augmented_assignment_with`](#feature-update_by_augmented_assignment_with)  
[⬆️ feature `update_by_member_call_with`](#feature-update_by_member_call_with)  
[⬇️ feature `accumulate_elements`](#feature-accumulate_elements)  
[⬇️ feature `accumulate_some_elements`](#feature-accumulate_some_elements)  

##### Specification

```sql
SELECT "update_with",
       t.name_suffix,
       t.span,
       t.path
FROM t
WHERE name_prefix IN ("update_by_assignment_with",
                      "update_by_augmented_assignment_with",
                      "update_by_member_call_with")
```

##### Example

```python
1   foo = foo + a
2   foo += a
3   foo.append(a)
4   foo += [a]
5
6   bar = bar.mult(5)
7   bar = mult(bar, 5)
8
9   fizz = fizz.upper() # no match
10  fizz.process(a) # no match
11
12  buzz += a + b + c
13  s *= (x - 1) / x
14  c[j] += c[i- 1]
15  (x, y) = (y, x)
16  (a, b) = (b, a + b)
17  seq.append(int(s))
```

##### Matches

| Label | Lines |
|:--|:--|
| `update_with:Add` | 1, 14, 2, 4, 12 |
| `update_with:mult` | 6, 7 |
| `update_with:Mult` | 13 |
| `update_with` | 15, 16 |
| `update_with:append` | 17, 3 |

--------------------------------------------------------------------------------

#### Feature `increment`

##### Derivations

[⬇️ feature `count_elements|count_states`](#feature-count_elementscount_states)  
[⬇️ feature `count_inputs`](#feature-count_inputs)  
[⬇️ feature `count_some_elements|count_some_states`](#feature-count_some_elementscount_some_states)  

##### Specification

```re
               ^(.*)/_type=
(   # augmented assignment
                           AugAssign
    \n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
    (
        \n(?:\1.+\n)*?\1/assigntarget/id=(?P<SUFFIX>.+)
    )?
    \n(?:\1.+\n)*?\1/op/_type=Add
    \n(?:\1.+\n)*?\1/assignvalue/n=1
|   # simple assignment
                           Assign
    \n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
    \n(?:\1.+\n)*?\1/assigntargets/1/_hash=(?P<HASH>.+) # capture _hash
    \n(?:\1.+\n)*?\1/assignvalue/_type=BinOp
    \n(?:\1.+\n)*?\1/assignvalue/left/_hash=(?P=HASH) # match _hash
    (
        \n(?:\1.+\n)*?\1/assignvalue/left/id=(?P<SUFFIX>.+)
    )?
    \n(?:\1.+\n)*?\1/assignvalue/op/_type=Add
    \n(?:\1.+\n)*?\1/assignvalue/right/n=1
)
```

##### Example

```python
1   a = a + 1
2   a = 1 + a # LIMITATION: no match for Yoda style
3   b += 1
4   a[i+j] += 1
5   b[foo()] = b[foo()] + 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `increment:a` | 1 |
| `increment:b` | 3 |
| `increment` | 4, 5 |

--------------------------------------------------------------------------------

#### Feature `swap_unpythonic`

Swap two variables or two elements of an array with an auxiliary variable (unpythonic, but deserves at least a mention in an algorithmic course).

##### Specification

```re
          ^(?P<_1>.+)/_type=Assign
\n(?:(?P=_1).+\n)*?(?P=_1)/_pos=(?P<POS>.+)
\n(?:(?P=_1).+\n)*?(?P=_1)/assigntargets/1/_hash=(?P<HASH_1>.+) # capture _hash #1
\n(?:(?P=_1).+\n)*?(?P=_1)/assignvalue/_hash=(?P<HASH_2>.+) # capture _hash #2
\n(?:(?P=_1).+\n)*?(?P=_1)/.* # ensure the lines are consecutive
         \n(?P<_2>.+)/_type=Assign
\n(?:(?P=_2).+\n)*?(?P=_2)/assigntargets/1/_hash=(?P=HASH_2) # match _hash #2
\n(?:(?P=_2).+\n)*?(?P=_2)/assignvalue/_hash=(?P<HASH_3>.+) # capture _hash #3
\n(?:(?P=_2).+\n)*?(?P=_2)/.*
         \n(?P<_3>.+)/_type=Assign
\n(?:(?P=_3).+\n)*?(?P=_3)/_pos=(?P<POS>.+)
\n(?:(?P=_3).+\n)*?(?P=_3)/assigntargets/1/_hash=(?P=HASH_3) # match _hash #3
\n(?:(?P=_3).+\n)*?(?P=_3)/assignvalue/_hash=(?P=HASH_1) # match _hash #1
```

##### Example

```python
1   aux = a
2   a = b
3   b = aux
4   
5   aux = a[i]
6   a[i] = a[j]
7   a[j] = aux
```

##### Matches

| Label | Lines |
|:--|:--|
| `swap_unpythonic` | 1-3, 5-7 |

--------------------------------------------------------------------------------

#### Feature `swap`

Swap two variables or two elements of an array with a 2-element tuple or list.

##### Specification

```re
           ^(.*)/_type=Assign
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
| `swap` | 1, 2, 3, 4 |

--------------------------------------------------------------------------------

#### Feature `slide`

« Slide » a window on two variables, the value of the second one being copied in the first one.

##### Specification

```re
           ^(.*)/_type=Assign
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/1/elts/1/_hash=(?P<HASH_A>.+)
\n(?:\1.+\n)*?\1/assigntargets/1/elts/2/_hash=(?P<HASH_B>.+)
\n(?:\1.+\n)*?\1/assignvalue/elts/1/_hash=(?P=HASH_B)
\n(?:\1.+\n)*?\1/assignvalue/elts/2/_hash=(?!(?P=HASH_A)).+
```

##### Example

```python
1   (a, b) = (b, a + b) # cf. Fibonacci
2   (a, b) = (b, a % b) # cf. Greatest Common Divisor
3   (array[pivot_index], array[i]) = (array[i], pivot) # cf. Quicksort
4   (a, b) = (b, a) # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `slide` | 1, 2, 3 |

--------------------------------------------------------------------------------

#### Feature `negate`

Update a variable by negating it.

##### Specification

```re
           ^(.*)/_type=Assign
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/assigntargets/1/_hash=(?P<HASH>.+) # capture hash
\n(?:\1.+\n)*?\1/assignvalue/_type=UnaryOp
\n(?:\1.+\n)*?\1/assignvalue/op/_type=USub
\n(?:\1.+\n)*?\1/assignvalue/operand/_hash=(?P=HASH) # match hash
```

##### Example

```python
1   a = -a
2   numbers[i] = -numbers[i]
3   a -= 2 * a # LIMITATION: no match
4   a = -1 * a # LIMITATION: no match
5   a = -abs(a) # no match
```

##### Matches

| Label | Lines |
|:--|:--|
| `negate` | 1, 2 |

--------------------------------------------------------------------------------

#### Feature `verbose_conditional_assignment`

A conditional statement whose each branch consists solely in a assignment to the same variable (could be rewritten as a conditional expression).

##### Specification

```re
           ^(.*)/_type=If
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/body/_length=1
\n(?:\1.+\n)*?\1/body/1/_type=Assign
\n(?:\1.+\n)*?\1/body/1/assigntargets/1/_hash=(?P<HASH>.+)
\n(?:\1.+\n)*?\1/orelse/_length=1
\n(?:\1.+\n)*?\1/orelse/1/_type=Assign
\n(?:\1.+\n)*?\1/orelse/1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/orelse/1/assigntargets/1/_hash=(?P=HASH)
```

##### Example

```python
1   if condition:
2       a[i] = 1
3   else:
4       a[i] = 2
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

##### Matches

| Label | Lines |
|:--|:--|
| `verbose_conditional_assignment` | 1-4 |

--------------------------------------------------------------------------------

#### Feature `compact_conditional_assignment`

Assignment to the result of a conditional expression.

##### Specification

```re
           ^(.*)/assignvalue/_type=IfExp
\n(?:\1.+\n)*?\1/assignvalue/_pos=(?P<POS>.+)
```

##### Example

```python
1   a[i] = 1 if condition else 2
```

##### Matches

| Label | Lines |
|:--|:--|
| `compact_conditional_assignment` | 1 |

--------------------------------------------------------------------------------

#### Feature `corrective_conditional_assignment`

Assign a “default” value to a variable, then if a certain condition is satisfied, update it. This form is sometimes preferred, especially when the plain form would require the repetition of a complex sub-expression.

##### Specification

```re
           ^(.*)/(?P<_1>\d+)/_type=Assign
\n(?:\1/(?P=_1).+\n)*?\1/(?P=_1)/_pos=(?P<POS>.+)
\n(?:\1/(?P=_1).+\n)*?\1/(?P=_1)/assigntargets/1/_hash=(?P<HASH>.+)
\n(?:\1/(?P=_1).+\n)*?\1/(?P<_2>\d+)/_type=If
\n(?:\1/(?P=_2).+\n)*?\1/(?P=_2)    /body/_length=1
\n(?:\1/(?P=_2).+\n)*?\1/(?P=_2)    /body/1/_type=(?:Aug)?Assign
\n(?:\1/(?P=_2).+\n)*?\1/(?P=_2)    /body/1/_pos=(?P<POS>.+)
\n(?:\1/(?P=_2).+\n)*?\1/(?P=_2)    /body/1/assigntarget(s/1)?/_hash=(?P=HASH)
\n(?:\1/(?P=_2).+\n)*?\1/(?P=_2)    /orelse/_length=0
```

##### Example

```python
1   double = 2 * int(number[-i - 1])
2   if double > 9:
3       double -= 9
4
5   double = 2 * int(number[-i - 1])
6   if double > 9:
7       double = double - 9
```

##### Matches

| Label | Lines |
|:--|:--|
| `corrective_conditional_assignment` | 1-3, 5-7 |

--------------------------------------------------------------------------------

## Function and class definitions

### Interface

--------------------------------------------------------------------------------

#### Feature `function`

In Python, the term "function" encompasses any type of subroutine, be it a method, a procedure, a generator or a "pure" function. We follow this terminology in this specification. However, in the taxonomy, “function” is used as a category of “subroutine”, as well as “method”, “procedure”, “generator”, and so on.

##### Derivations

[⬇️ feature `access_outer_scope`](#feature-access_outer_scope)  
[⬇️ feature `closure`](#feature-closure)  
[⬇️ feature `deeply_recursive_function`](#feature-deeply_recursive_function)  
[⬇️ feature `function_line_count`](#feature-function_line_count)  
[⬇️ feature `function_returning_nothing`](#feature-function_returning_nothing)  
[⬇️ feature `function_returning_something`](#feature-function_returning_something)  
[⬇️ feature `generator`](#feature-generator)  
[⬇️ feature `higher-order function`](#feature-higher-order-function)  
[⬇️ feature `if_guard`](#feature-if_guard)  
[⬇️ feature `internal_free_call`](#feature-internal_free_call)  
[⬇️ feature `local_scope`](#feature-local_scope)  
[⬇️ feature `method`](#feature-method)  
[⬇️ feature `procedural_style`](#feature-procedural_style)  
[⬇️ feature `recursive_call_count`](#feature-recursive_call_count)  
[⬇️ feature `recursive_function`](#feature-recursive_function)  
[⬇️ feature `scope`](#feature-scope)  

##### Specification

```re
           ^(.*)/_type=FunctionDef
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/name=(?P<SUFFIX>.+)
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
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
| `function:christmas_tree` | 10-11 |
| `function:function_with_types` | 13-14 |
| `function:bar` | 18-19 |
| `function:generator` | 21-22 |

--------------------------------------------------------------------------------

#### Feature `return`

Match `return` statements and, when the returned object is an [_atom_](#feature-argument), suffix it. Note that a `return` statement returning no value is denoted by `return:None`, not to be confounded with `return` (without suffix), which denotes the return of a non-atomic object.

##### Derivations

[⬇️ feature `accumulate_inputs`](#feature-accumulate_inputs)  
[⬇️ feature `closure`](#feature-closure)  
[⬇️ feature `count_inputs`](#feature-count_inputs)  
[⬇️ feature `find_first_good_element`](#feature-find_first_good_element)  
[⬇️ feature `find_first_good_element_index`](#feature-find_first_good_element_index)  
[⬇️ feature `find_first_good_element_index_unpythonic`](#feature-find_first_good_element_index_unpythonic)  
[⬇️ feature `function_returning_something`](#feature-function_returning_something)  
[⬇️ feature `get_valid_input`](#feature-get_valid_input)  
[⬇️ feature `if_guard`](#feature-if_guard)  
[⬇️ feature `loop_with_return`](#feature-loop_with_return)  
[⬇️ feature `universal_quantification|existential_quantification`](#feature-universal_quantificationexistential_quantification)  

##### Specification

```re
           ^(.*)/_type=Return
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
)?
(
\n(?:\1.+\n)*?\1/value(/value|/n|/id)?=(?P<SUFFIX>.+)
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
11      return ( # several lines
12                a,
13                b,
14                c,
15      ) # BUG: last line incorrectly excluded
16      return foo( # several lines
17                a
18      ).bar() # BUG: last line incorrectly excluded
19      return foo( # several lines
20                a
21      ).bar(42) # last line correctly included
```

##### Matches

| Label | Lines |
|:--|:--|
| `return:a` | 2 |
| `return` | 3, 4, 5, 10, 11-14, 16-17, 19-21 |
| `return:2` | 6 |
| `return:True` | 7 |
| `return:None` | 8, 9 |

--------------------------------------------------------------------------------

#### Feature `class`

##### Derivations

[⬇️ feature `class_method_count`](#feature-class_method_count)  
[⬇️ feature `method`](#feature-method)  
[⬇️ feature `object_oriented_style`](#feature-object_oriented_style)  

##### Specification

```re
           ^(.*)/_type=ClassDef
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/name=(?P<SUFFIX>.+)
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
```

##### Example

```python
1   class MyClass:
2
3       def an_instance_method(self, a, b, c):
4           pass
5
6       @staticmethod
7       def a_static_method(f, g):
8           pass
9
10      @classmethod
11      def a_class_method(cls, d, e):
12          pass
13
14  @dataclass
15  class Point:
16      x: float
17      y: float
```

##### Matches

| Label | Lines |
|:--|:--|
| `node:ClassDef` | 1-12, 15-17 |
| `class:MyClass` | 1-12 |
| `class:Point` | 15-17 |

--------------------------------------------------------------------------------

#### Feature `method`

##### Derivations

[⬆️ feature `class`](#feature-class)  
[⬆️ feature `function`](#feature-function)  
[⬇️ feature `class_method_count`](#feature-class_method_count)  
[⬇️ feature `impure_function`](#feature-impure_function)  
[⬇️ feature `instance_method|class_method|static_method`](#feature-instance_methodclass_methodstatic_method)  
[⬇️ feature `pure_function`](#feature-pure_function)  

##### Specification

```sql
SELECT "method",
       f.name_suffix,
       f.span,
       f.path
FROM t_class c
JOIN t_function f ON (f.path GLOB c.path || "*-*-")
```

##### Example

```python
1   class MyClass:
2
3       def an_instance_method(self, a, b, c):
4           pass
5
6       @staticmethod
7       def a_static_method(f, g):
8           pass
9
10      @classmethod
11      def a_class_method(cls, d, e):
12          pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `method:an_instance_method` | 3-4 |
| `method:a_static_method` | 7-8 |
| `method:a_class_method` | 11-12 |

--------------------------------------------------------------------------------

#### Feature `instance_method|class_method|static_method`

##### Derivations

[⬆️ feature `function_parameter`](#feature-function_parameter)  
[⬆️ feature `method`](#feature-method)  

##### Specification

```sql
SELECT CASE a.name_suffix
           WHEN "self" THEN "instance_method"
           WHEN "cls" THEN "class_method"
           ELSE "static_method"
       END,
       m.name_suffix,
       m.span,
       m.path
FROM t_method m
LEFT JOIN t_function_parameter a ON (a.path GLOB m.path || "*-*-"
                                     AND a.name_suffix IN ("self",
                                                           "cls"))
```

_Remark._: the presence of a decorator `classmethod` or `staticmethod` is unchecked, nor is the flavor of the parameters `self` and `cls` (they should be positional parameters). In other words, it is enough that a method has an parameter `self` (resp. `cls`) for being categorized as an instance (resp. class) method, or else as a static method.

##### Example

```python
1   class MyClass:
2
3       def an_instance_method(self, a, b, c):
4           pass
5
6       @classmethod
7       def a_class_method(cls, d, e):
8           pass
9
10      @staticmethod
11      def a_static_method(f, g):
12          pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `instance_method:an_instance_method` | 3-4 |
| `class_method:a_class_method` | 7-8 |
| `static_method:a_static_method` | 11-12 |

--------------------------------------------------------------------------------

#### Feature `yield`

Match `yield` and `yieldfrom` _[expressions](https://docs.python.org/3/reference/expressions.html#yield-expressions)_ (generally used as statements) and, when the yielded object is an [atom](#feature-argument), suffix it.

##### Derivations

[⬇️ feature `generator`](#feature-generator)  

##### Specification

```re
           ^(.*)/_type=Yield(From)?
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/value(/value|/n|/id)?=(?P<SUFFIX>.+)
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

[⬆️ feature `function`](#feature-function)  
[⬆️ feature `yield`](#feature-yield)  
[⬇️ feature `function_returning_nothing`](#feature-function_returning_nothing)  

##### Specification

```sql
SELECT "generator",
       f.name_suffix,
       max(f.span_start) || "-" || min(f.span_end),
       max(f.path)
FROM t_function f
JOIN t_yield y ON (y.path GLOB f.path || "*-")
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

[⬆️ feature `function`](#feature-function)  
[⬆️ feature `return`](#feature-return)  
[⬇️ feature `function_returning_nothing`](#feature-function_returning_nothing)  
[⬇️ feature `functional_style`](#feature-functional_style)  
[⬇️ feature `impure_function`](#feature-impure_function)  
[⬇️ feature `pure_function`](#feature-pure_function)  

##### Specification

```sql
SELECT "function_returning_something",
       f.name_suffix,
       max(f.span_start) || "-" || min(f.span_end),
       max(f.path)
FROM t_function f
JOIN t_return r ON (r.path GLOB f.path || "*-")
WHERE r.name_suffix != "None"
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
24
25  def i(s, a):
26      if s == []:
27          return a
28      else:
29          return s[0]
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_returning_something:a` | 1-2 |
| `function_returning_something:c` | 7-10 |
| `function_returning_something:f` | 16-17 |
| `function_returning_something:g` | 20-23 |
| `function_returning_something:i` | 25-29 |

--------------------------------------------------------------------------------

#### Feature `pure_function`

A function (not a method) returning something, but featuring no assignment, no variable update, no loop, no printing.

##### Derivations

[⬆️ feature `assignment`](#feature-assignment)  
[⬆️ feature `free_call`](#feature-free_call)  
[⬆️ feature `function_returning_something`](#feature-function_returning_something)  
[⬆️ feature `method`](#feature-method)  
[⬆️ feature `node`](#feature-node)  
[⬆️ feature `update`](#feature-update)  
[⬇️ feature `impure_function`](#feature-impure_function)  

##### Specification

```sql
SELECT "pure_function",
       f.name_suffix,
       max(f.span_start) || "-" || min(f.span_end),
       max(f.path)
FROM t_function_returning_something f
WHERE NOT EXISTS
    (SELECT *
     FROM t
     WHERE ((t.name_prefix IN ("assignment",
                               "update")
             OR t.name IN ("node:For",
                           "node:While",
                           "free_call:print"))
            AND t.path GLOB f.path || "*-")
       OR (t.name_prefix = "method"
           AND t.path=f.path) )
GROUP BY f.rowid
```

##### Example

```python
1   def triangle_semi_perimeter(a, b, c): # pure
2       return (a + b + c) / 2
3   
4   def test_triangle_semi_perimeter(): # impure (the function returns nothing)
5       assert triangle_semi_perimeter(3, 4, 5) == 6
6   
7   def triangle_area(a, b, c): # impure (because of the assignment)
8       p = triangle_semi_perimeter(a, b, c)
9       return (p * (p-a) * (p-b) * (p-c)) ** 0.5
10  
11  def check_password(): # impure (because of the side effect)
12      if PASSWORD == input("Password? "):
13          print("You have successfully logged in on the NSA main server.")
14          return AUTHENTICATED
15      return WRONG_PASSWORD
16  
17  def dna_complement(dna): # pure (a comprehension is considered as pure)
18      return "".join(base_complements[base] for base in dna)
19  
20  def suffix_sequences(suffix, sequences): # impure
21      result = []
22      for sequence in sequences:
23          result.append(sequence + [suffix])
24      return result
25  
26  def power_list(sequence, result = [[]]): # pure
27      if sequence == []:
28          return result
29      else:
30          return power_list(sequence[1:], result + suffix_sequences(sequence[0], result))
31  
32  def belongs_to(seq, x): # impure (loop)
33      for candidate in seq:
34          if candidate == x:
35              return True
36      return False
37  
38  def accept(words, word, accumulator): # impure (because of the update)
39      if word in words:
40          accumulator.append(word)
41          return True
42      else:
43          return False
44
45  class BankAccount(object): # a method cannot be considered as pure
46      def __init__(self, initial_balance=0):
47          self.balance = initial_balance
48      def deposit(self, amount):
49          self.balance += amount
50      def withdraw(self, amount):
51          self.balance -= amount
52      def overdrawn(self): # ... even if it struggle for purity
53          return self.balance < 0
54
55  def poor_print(bar): # no match (returns nothing)
56      print(bar)
57  
58  def gray(n): # paroxython: -impure_function:gray... +pure_function:gray...
59      if n <= 0:
60          return [""]
61      else:
62          previous = gray(n - 1)
63          return prefix_all(previous, "0") + prefix_all(reversed(previous), "1")  # paroxython: ...impure_function:gray ...pure_function:gray
```

##### Matches

| Label | Lines |
|:--|:--|
| `pure_function:triangle_semi_perimeter` | 1-2 |
| `impure_function:triangle_area` | 7-9 |
| `impure_function:check_password` | 11-15 |
| `pure_function:dna_complement` | 17-18 |
| `impure_function:suffix_sequences` | 20-24 |
| `pure_function:power_list` | 26-30 |
| `impure_function:belongs_to` | 32-36 |
| `impure_function:accept` | 38-43 |
| `pure_function:gray` | 58-63 |

--------------------------------------------------------------------------------

#### Feature `impure_function`

A function (not a method) which returns something, but is not pure. Does not cover the procedures.

##### Derivations

[⬆️ feature `function_returning_something`](#feature-function_returning_something)  
[⬆️ feature `method`](#feature-method)  
[⬆️ feature `pure_function`](#feature-pure_function)  

##### Specification

```sql
SELECT "impure_function",
       f.name_suffix,
       f.span,
       f.path
FROM t_function_returning_something f
WHERE NOT EXISTS
    (SELECT *
     FROM t
     WHERE (t.name_prefix IN ("method",
                              "pure_function")
            AND t.path=f.path) )
GROUP BY f.rowid
```

##### Example

```python
1   def foo():
2       a = "see the examples for `pure_function` immediately above"
3       return a
4   
5   def gray(n): # paroxython: -impure_function:gray... +pure_function:gray...
6       if n <= 0:
7           return [""]
8       else:
9           previous = gray(n - 1)
10          return prefix_all(previous, "0") + prefix_all(reversed(previous), "1")  # paroxython: ...impure_function:gray ...pure_function:gray
```

##### Matches

| Label | Lines |
|:--|:--|
| `impure_function:foo` | 1-3 |

--------------------------------------------------------------------------------

#### Feature `function_returning_nothing`

A function returning nothing (_aka_ a procedure) is a function which is neither a generator or a function returning something.

##### Derivations

[⬆️ feature `function`](#feature-function)  
[⬆️ feature `function_returning_something`](#feature-function_returning_something)  
[⬆️ feature `generator`](#feature-generator)  
[⬇️ feature `functional_style`](#feature-functional_style)  

##### Specification

```sql
SELECT "function_returning_nothing",
       t_function.name_suffix,
       t_function.span,
       t_function.path
FROM t_function
LEFT JOIN t ON (t_function.span = t.span
                AND t.name_prefix IN ("function_returning_something",
                                      "generator"))
WHERE t.span IS NULL
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

#### Feature `function_parameter`

##### Derivations

[⬇️ feature `access_outer_scope`](#feature-access_outer_scope)  
[⬇️ feature `higher-order function`](#feature-higher-order-function)  
[⬇️ feature `instance_method|class_method|static_method`](#feature-instance_methodclass_methodstatic_method)  
[⬇️ feature `scope`](#feature-scope)  

##### Specification

```re
           ^(.*)/_type=arg
\n            \1/_pos=(?P<POS>.+)
\n            \1/arg=(?P<SUFFIX>.+)
```

##### Example

```python
1   def foobar(a, b, *c, d=42, e=None, **f):
2       pass
3   buzz(lambda g: g + 1)
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_parameter:a` | 1 |
| `function_parameter:b` | 1 |
| `function_parameter:c` | 1 |
| `function_parameter:d` | 1 |
| `function_parameter:e` | 1 |
| `function_parameter:f` | 1 |
| `function_parameter:g` | 3 |

--------------------------------------------------------------------------------

#### Feature `function_parameter_flavor`

Give the category of each function parameter among:
- `arg`: positional parameter;
- `vararg`: list of unnamed parameters;
- `kwonlyarg`: keyword parameter;
- `kwarg`: dictionary of named parameters.

_Remark._ The actual name of a parameter can be retrieved by joining with `function_parameter` using its `path`.

_Terminology._ We follow the official Python FAQ for the [difference between arguments and parameters](https://docs.python.org/3/faq/programming.html#faq-argument-vs-parameter):

> **Parameters** are defined by the names that appear in a function definition, whereas **arguments** are the values actually passed to a function when calling it.

##### Specification

```re
^(.*/(?P<SUFFIX>arg|vararg|kwonlyarg|kwarg)(s/\d+)?)/_type=arg
\n                                                \1/_pos=(?P<POS>.+)

```

##### Example

```python
1   def foobar(a, b, *c, d=42, e=None, **f):
2       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_parameter_flavor:arg` | 1, 1 |
| `function_parameter_flavor:kwarg` | 1 |
| `function_parameter_flavor:kwonlyarg` | 1, 1 |
| `function_parameter_flavor:vararg` | 1 |

--------------------------------------------------------------------------------

#### Feature `function_parameter_default`

##### Specification

```re
           ^(.*/args/(kw_)?defaults/\d+)/_type=(?P<SUFFIX>.+)
\n(?:\1.+\n)*?                        \1/_pos=(?P<POS>.+)
```

##### Example

```python
1   def foobar(a=1, b=foo, *c, d=42, e=None, **f):
2       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_parameter_default:Name` | 1 |
| `function_parameter_default:NameConstant` | 1 |
| `function_parameter_default:Num` | 1, 1 |

--------------------------------------------------------------------------------

#### Feature `function_without_parameters`

##### Specification

```re
           ^(.*)/_type=FunctionDef
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/name=(?P<SUFFIX>.+)
\n(?:\1.+\n)*?\1/args/args/_length=0
\n(?:\1.+\n)*?\1/args/vararg=None
\n(?:\1.+\n)*?\1/args/kwonlyargs/_length=0
\n(?:\1.+\n)*?\1/args/kwarg=None
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
```

##### Example

```python
1   def bizz():
2       pass
3
4   def foo(a, b="c"): # no match
5       pass
6
7   def bar(b="c"): # no match
8       pass
9
10  def qux(*args, **kwargs): # no match
11      pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `function_without_parameters:bizz` | 1-2 |

--------------------------------------------------------------------------------

#### Feature `decorated_function`

##### Specification

```re
           ^(.*)/_type=FunctionDef
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/name=(?P<SUFFIX>.+)
\n(?:\1.+\n)*?\1/decorator_list/_length=(?!0\n).+
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
```

##### Example

```python
1   @bizz
2   @foo
3   @bar
4   def qux(*args, **kwargs):
5       pass
```

_Remark._ The span starts from the first decorator.

##### Matches

| Label | Lines |
|:--|:--|
| `decorated_function:qux` | 4-5 |

--------------------------------------------------------------------------------

#### Feature `function_decorator`

##### Specification

```re
           ^(.*)/_type=FunctionDef
(
\n(?:\1.+\n)*?\1/(?P<_1>decorator_list/\d+)/_pos=(?P<POS>.+)  # force len(d["POS"]) != len(d["SUFFIX"])
\n(?:\1.+\n)*?\1/(?P=_1)                   /id=(?P<SUFFIX>.+)
)+
\n(?:\1.+\n)* \1/body/[^=]+/_pos=(?P<POS>.+)
```

##### Example

```python
1   @bizz
2   @foo
3   @bar
4   def qux(*args, **kwargs):
5       pass
6   @clip
7   @crap
8   def bang(*args, **kwargs):
9       pass
```

_Remark._ The span and the path start with the first decorator and end with the function.

##### Matches

| Label | Lines |
|:--|:--|
| `function_decorator:bar` | 1-5 |
| `function_decorator:bizz` | 1-5 |
| `function_decorator:foo` | 1-5 |
| `function_decorator:clip` | 6-9 |
| `function_decorator:crap` | 6-9 |

--------------------------------------------------------------------------------

### Nesting

--------------------------------------------------------------------------------

#### Feature `nested_function`

##### Specification

```re
           ^(.*)/_type=FunctionDef
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/name=(?P<SUFFIX>.+)
\n(?:\1.+\n)*?\1/[^=]+/_type=FunctionDef
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
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

[⬆️ feature `function`](#feature-function)  
[⬆️ feature `return`](#feature-return)  

##### Specification

```sql
SELECT "closure",
       f.name_suffix,
       max(f.span_start) || "-" || min(f.span_end),
       max(f.path)
FROM t_function f
JOIN t_function c ON (c.path GLOB f.path || "*-")
JOIN t_return r ON (r.path GLOB f.path || "*-")
WHERE r.name_suffix = c.name_suffix
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

#### Feature `higher-order function`

Match a function having another function as an argument, at least when the latter is called inside the former.

##### Derivations

[⬆️ feature `free_call`](#feature-free_call)  
[⬆️ feature `function`](#feature-function)  
[⬆️ feature `function_parameter`](#feature-function_parameter)  

##### Specification

```sql
SELECT "higher_order_function",
       a.name_suffix,
       f.span,
       f.path
FROM t_function f
JOIN t_function_parameter a ON (a.path GLOB f.path || "*-")
JOIN t_free_call c ON (c.name_suffix = a.name_suffix
                       AND c.path GLOB f.path || "*-")
GROUP BY f.path,
         a.name_suffix
```

##### Example

```python
1   def bar(f, g):
2       def foo(h, a, b):
3           x = h(a)
4           y = h(b)
5           z = g(a, b)
6           return x + y + z
7       foo(f, 1, 2)
```

##### Matches

| Label | Lines |
|:--|:--|
| `higher_order_function:g` | 1-7 |
| `higher_order_function:h` | 1-7, 2-6 |

--------------------------------------------------------------------------------

### Recursion

--------------------------------------------------------------------------------

#### Feature `recursive_function`

##### Derivations

[⬆️ feature `free_call`](#feature-free_call)  
[⬆️ feature `function`](#feature-function)  
[⬇️ feature `body_recursive_function`](#feature-body_recursive_function)  
[⬇️ feature `tail_recursive_function`](#feature-tail_recursive_function)  

##### Specification

```sql
SELECT "recursive_function",
       f.name_suffix,
       f.span,
       f.path
FROM t_function f
JOIN t_free_call c ON (c.path GLOB f.path || "*-")
WHERE c.name_suffix = f.name_suffix
GROUP BY f.path
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

#### Feature `recursive_call_count`

Count the number of times a function calls itself. Useful to distinguish between [single recursion and multiple recursion](https://en.wikipedia.org/wiki/Recursion_(computer_science)#Single_recursion_and_multiple_recursion).

##### Derivations

[⬆️ feature `free_call`](#feature-free_call)  
[⬆️ feature `function`](#feature-function)  

##### Specification

```sql
SELECT "recursive_call_count",
       count(*) AS call_count,
       f.span,
       f.path
FROM t_function f
JOIN t_free_call c ON (c.path GLOB f.path || "*-")
WHERE c.name_suffix = f.name_suffix
GROUP BY f.path
```

##### Example

```python
1   def fibonacci(i):
2       if i < 2:
3           return 1
4       else:
5           return fibonacci(i - 1) + fibonacci(i - 2)
6
7   def gob_program():
8       print("PENUS")
9       gob_program()
```

##### Matches

| Label | Lines |
|:--|:--|
| `recursive_call_count:2` | 1-5 |
| `recursive_call_count:1` | 7-9 |

--------------------------------------------------------------------------------

#### Feature `deeply_recursive_function`

Any function `f` which features a nested call to itself (`f(..., f(...), ...)`), e.g. the [Ackermann function](https://en.wikipedia.org/wiki/Ackermann_function).

##### Derivations

[⬆️ feature `free_call`](#feature-free_call)  
[⬆️ feature `function`](#feature-function)  

##### Specification

```sql
SELECT "deeply_recursive_function",
       f.name_suffix,
       f.span,
       f.path
FROM t_function f
JOIN t_free_call c1 ON (c1.path GLOB f.path || "*-")
JOIN t_free_call c2 ON (c2.path GLOB c1.path || "*-")
WHERE c1.name_suffix = f.name_suffix
  AND c2.name_suffix = f.name_suffix
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

A function is body recursive if and only if at least one of its recursive calls is not a tail call.

**BUG.** Since the procedure tail calls are not recognized by `free_tail_call`, the tail recursive procedures are incorrectly labelled as body recursive.

##### Derivations

[⬆️ feature `free_call`](#feature-free_call)  
[⬆️ feature `free_tail_call`](#feature-free_tail_call)  
[⬆️ feature `recursive_function`](#feature-recursive_function)  
[⬇️ feature `tail_recursive_function`](#feature-tail_recursive_function)  

##### Specification

```sql
SELECT "body_recursive_function",
       t_recursive_function.name_suffix,
       t_recursive_function.span,
       t_recursive_function.path
FROM t_recursive_function
JOIN t_free_call ON (t_free_call.path GLOB t_recursive_function.path || "*-")
WHERE t_free_call.name_suffix = t_recursive_function.name_suffix
  AND NOT EXISTS
    (SELECT 1
     FROM t_free_tail_call
     WHERE t_free_tail_call.path = t_free_call.path )
GROUP BY t_recursive_function.span
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
10  def ack(m, n): # body recursive
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

A function is tail recursive if and only if all its recursive calls are tail calls.

##### Derivations

[⬆️ feature `body_recursive_function`](#feature-body_recursive_function)  
[⬆️ feature `recursive_function`](#feature-recursive_function)  

##### Specification

```sql
SELECT "tail_recursive_function",
       f.name_suffix,
       f.span,
       f.path
FROM t_recursive_function f
LEFT JOIN t_body_recursive_function USING (span)
WHERE t_body_recursive_function.rowid IS NULL
```

_LIMITATION._ Currently, the tail recursive procedures (i.e., without `return`, e.g. the drawing of a fractal) are not recognized.

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

A synonym of feature `node:If`.

##### Derivations

[⬆️ feature `node`](#feature-node)  
[⬇️ feature `accumulate_inputs`](#feature-accumulate_inputs)  
[⬇️ feature `accumulate_some_elements`](#feature-accumulate_some_elements)  
[⬇️ feature `count_inputs`](#feature-count_inputs)  
[⬇️ feature `count_some_elements|count_some_states`](#feature-count_some_elementscount_some_states)  
[⬇️ feature `find_best_element`](#feature-find_best_element)  
[⬇️ feature `find_best_element_index`](#feature-find_best_element_index)  
[⬇️ feature `find_best_element_index_unpythonic`](#feature-find_best_element_index_unpythonic)  
[⬇️ feature `find_first_good_element`](#feature-find_first_good_element)  
[⬇️ feature `find_first_good_element_index`](#feature-find_first_good_element_index)  
[⬇️ feature `find_first_good_element_index_unpythonic`](#feature-find_first_good_element_index_unpythonic)  
[⬇️ feature `flat_style`](#feature-flat_style)  
[⬇️ feature `get_valid_input`](#feature-get_valid_input)  
[⬇️ feature `if_without_else`](#feature-if_without_else)  
[⬇️ feature `nested_if`](#feature-nested_if)  
[⬇️ feature `universal_quantification|existential_quantification`](#feature-universal_quantificationexistential_quantification)  

##### Specification

```sql
SELECT "if",
       "",
       t.span,
       t.path
FROM t
WHERE t.name = "node:If"
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
| `node:If` | 1-10, 2-3, 4-10, 5-6, 8-9 |

--------------------------------------------------------------------------------

#### Feature `if_test_atom`

Match and suffix any [atom](#feature-argument) present in the condition of an `if` statement.

##### Derivations

[⬇️ feature `accumulate_inputs`](#feature-accumulate_inputs)  
[⬇️ feature `count_inputs`](#feature-count_inputs)  
[⬇️ feature `find_best_element`](#feature-find_best_element)  
[⬇️ feature `find_best_element_index`](#feature-find_best_element_index)  
[⬇️ feature `find_best_element_index_unpythonic`](#feature-find_best_element_index_unpythonic)  
[⬇️ feature `find_first_good_element`](#feature-find_first_good_element)  
[⬇️ feature `get_valid_input`](#feature-get_valid_input)  
[⬇️ feature `universal_quantification|existential_quantification`](#feature-universal_quantificationexistential_quantification)  

##### Specification

```re
           ^(.*)/_type=If
(
\n(?:\1.+\n)*?\1/test(?P<_1>/.*)   /_pos=(?P<POS>.+)
\n            \1/test(?P=_1)       /(value|n|(?<!func/)id)=(?P<SUFFIX>.+)
)+
```

##### Example

```python
1   if foo(bar) == biz: # no match for "foo"
2       pass
3   if a.b(c) > (d + e) / 2: # no match for "b"
4       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `if_test_atom:bar` | 1 |
| `if_test_atom:biz` | 1 |
| `if_test_atom:2` | 3 |
| `if_test_atom:a` | 3 |
| `if_test_atom:c` | 3 |
| `if_test_atom:d` | 3 |
| `if_test_atom:e` | 3 |

--------------------------------------------------------------------------------

#### Feature `if_then_branch`

Match the body of the branch “`then`” of an `if` statement.

##### Derivations

[⬇️ feature `if_without_else`](#feature-if_without_else)  
[⬇️ feature `nested_if`](#feature-nested_if)  

##### Specification

```re
(^  # capture any body block
                   .*/body/\d+
|   # capture any orelse block whose length is greater than 1
    (?<!_length=1\n).*/orelse/\d+
)
                /_type=If
\n(?:\1.+\n)*?\1/body/1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)* \1/body/[^=]+/_pos=(?P<POS>.+)
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

[⬇️ feature `nested_if`](#feature-nested_if)  

##### Specification

```re
           ^(.*)/orelse/_length=1
\n(?:\1.+\n)*?\1/orelse/1/_type=If
\n(?:\1.+\n)*?\1/orelse/1/body/1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)* \1/orelse/1/body/[^=]+/_pos=(?P<POS>.+)
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

[⬇️ feature `nested_if`](#feature-nested_if)  

##### Specification

```re
           ^(.*)/_type=If
\n(?:\1.+\n)*?\1/orelse/
(   # there is at least two statements in the else branch,
                        _length=\d+(?<![01])
\n(?:\1.+\n)*?\1/orelse/1/_pos=(?P<POS>.+)
|   # or only one, but distinct from If (otherwise, this is an elif)
                        _length=1
\n(?:\1.+\n)*?\1/orelse/1/_type=.+?(?<!If)
\n(?:\1.+\n)*?\1/orelse/1/_pos=(?P<POS>.+)
)
(
\n(?:\1.+\n)* \1/orelse/[^=]+/_pos=(?P<POS>.+)
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

#### Feature `if_without_else`

##### Derivations

[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_then_branch`](#feature-if_then_branch)  
[⬇️ feature `if_guard`](#feature-if_guard)  

##### Specification

```sql
SELECT "if_without_else",
       "",
       t_if.span,
       t_if.path
FROM t_if
JOIN t_if_then_branch branch ON (t_if.span_start + 1 == branch.span_start
                                 AND t_if.span_end == branch.span_end)
```

##### Example

```python
1   if condition_1:         # no match ("else" on line 5)
2       if condition_2:     # match
3           if condition_3: # |        match
4               pass        # |        |
5   else:
6       if condition_4:     # match
7           pass            # |
8       if condition_5:     # match
9           pass            # |
10
11  if condition_6:         # no match ("elif" on line 13)
12      pass
13  elif condition_7:
14      pass
15
16  if condition_8:         # match
17      for foo in bar:     # |
18          if condition_9: # |        match
19              pass        # |        |
```

##### Matches

| Label | Lines |
|:--|:--|
| `if_without_else` | 2-4, 3-4, 6-7, 8-9, 16-19, 18-19 |

--------------------------------------------------------------------------------

#### Feature `if_guard`

A guard clause is a conditional which provides an early exit from a subroutine.

The heuristic ensures that:

1. it is at the first level of the subroutine;
2. it does not extend to the end of the subroutine;
3. it ends by a `return` clause that is not followed by an `else` or an `elif` branch.

Condition 2 is probably too weak in numerous situations, but in case of false positive, it is always possible for the programmer to make condition 3 fail by adding an `else`clause. As a general rule, this style may be recommended to highlight the difference between a guard and a simple returning conditional in the main treatment.

##### Derivations

[⬆️ feature `function`](#feature-function)  
[⬆️ feature `if_without_else`](#feature-if_without_else)  
[⬆️ feature `return`](#feature-return)  

##### Specification

```sql
SELECT "if_guard",
       "",
       guard.span,
       guard.path
FROM t_if_without_else guard
JOIN t_function f ON (guard.path GLOB f.path || "?-?-"
                      AND f.span_start < guard.span_start
                      AND guard.span_end < f.span_end)
JOIN t_return ret ON (guard.span_end == ret.span_end)
```

##### Example

```python
1   def foo():
2       if condition_1:     # match
3           return
4       if condition_2:     # match
5           return
6       pass # at least one line
7   def foo():
8       if condition_1:     # no match, since it is followed by an elif branch
9           return
10      elif condition_2:   # no match, since it is not on the first level
11          return
12      pass # at least one line
13  def foo():
14      if condition_1:     # match
15          return
16      if condition_2:     # no match, since this is the last line of the function
17          return
```

##### Matches

| Label | Lines |
|:--|:--|
| `if_guard` | 2-3, 4-5, 14-15 |

--------------------------------------------------------------------------------

#### Feature `return_condition_naive`

When a predicate ends with a conditional whose sole purpose is to return `True` or `False`, it is enough to return the condition.

##### Specification

```re
           ^(.*)/_type=If
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/body/1/_type=Return
\n(?:\1.+\n)*?\1/body/1/value/value=(?P<BOOL>True|False) # name BOOL the value used here
\n(?:\1.+\n)*?\1/orelse/1/_type=Return
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
| `return_condition_naive` | 2-5, 8-11 |

--------------------------------------------------------------------------------

#### Feature `nested_if`

Match an `if` clause nested in _n_ other `if` clauses, suffixing it by _n_.

##### Derivations

[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_elif_branch`](#feature-if_elif_branch)  
[⬆️ feature `if_else_branch`](#feature-if_else_branch)  
[⬆️ feature `if_then_branch`](#feature-if_then_branch)  

##### Specification

```sql
SELECT "nested_if",
       count(*),
       t_if.span,
       t_if.path
FROM t branch
JOIN t_if ON (branch.span_start <= t_if.span_start
              AND t_if.span_end <= branch.span_end)
WHERE branch.name_prefix IN ("if_then_branch",
                             "if_else_branch",
                             "if_elif_branch")
GROUP BY t_if.span
ORDER BY t_if.span_start
```

_Remark._ A join condition `(inner_if.path GLOB branch.path || "*-")` would not work here, since an `else` branch has no specific path in the AST.

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

### Iteration keywords

--------------------------------------------------------------------------------

#### Feature `for`

Match sequential loops, along with their iteration variable(s).

##### Derivations

[⬇️ feature `accumulate_elements`](#feature-accumulate_elements)  
[⬇️ feature `accumulate_some_elements`](#feature-accumulate_some_elements)  
[⬇️ feature `find_best_element`](#feature-find_best_element)  
[⬇️ feature `find_best_element_index`](#feature-find_best_element_index)  
[⬇️ feature `for_range`](#feature-for_range)  
[⬇️ feature `nested_for`](#feature-nested_for)  
[⬇️ feature `universal_quantification|existential_quantification`](#feature-universal_quantificationexistential_quantification)  

##### Specification

```re
           ^(.*)/_type=For
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/(?P<_1>target(/.+)?)/_pos=(?P<POS>.+) # force len(d["POS"]) != len(d["SUFFIX"])
\n(?:\1.+\n)*?\1/(?P=_1)             /id=(?P<SUFFIX>.+)
)+
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
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
8   for (i, j) in enumerate(seq):
9       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `for:x` | 1-7 |
| `for:y` | 2-3 |
| `for:a` | 4-7 |
| `for:b` | 4-7 |
| `for:c` | 4-7 |
| `for:i` | 8-9 |
| `for:j` | 8-9 |

--------------------------------------------------------------------------------

#### Feature `iteration_variable`

The same as above, but extended to comprehensions and spanning the iteration variable instead of the whole loop.

##### Derivations

[⬇️ feature `access_outer_scope`](#feature-access_outer_scope)  
[⬇️ feature `scope`](#feature-scope)  

##### Specification

```re
           ^(.*)/_type=(For|ListComp|DictComp|SetComp|GeneratorExp)
(
\n(?:\1.+\n)*?\1/(?P<_1>(generators/\d+/)?target(/.+)?)/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_1)                   /id=(?P<SUFFIX>.+)
)+
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
8   for (i, j) in enumerate(seq):
9       [z for z in seq]
```

##### Matches

| Label | Lines |
|:--|:--|
| `iteration_variable:x` | 1 |
| `iteration_variable:y` | 2 |
| `iteration_variable:a` | 4 |
| `iteration_variable:b` | 4 |
| `iteration_variable:c` | 4 |
| `iteration_variable:i` | 8 |
| `iteration_variable:j` | 8 |
| `iteration_variable:z` | 9 |

--------------------------------------------------------------------------------

#### Feature `loop`

##### Derivations

[⬆️ feature `node`](#feature-node)  
[⬇️ feature `count_elements|count_states`](#feature-count_elementscount_states)  
[⬇️ feature `count_some_elements|count_some_states`](#feature-count_some_elementscount_some_states)  
[⬇️ feature `flat_style`](#feature-flat_style)  
[⬇️ feature `functional_style`](#feature-functional_style)  
[⬇️ feature `loop_with_break`](#feature-loop_with_break)  
[⬇️ feature `loop_with_else`](#feature-loop_with_else)  
[⬇️ feature `loop_with_late_exit`](#feature-loop_with_late_exit)  
[⬇️ feature `loop_with_raise`](#feature-loop_with_raise)  
[⬇️ feature `loop_with_return`](#feature-loop_with_return)  

##### Specification

```sql
SELECT "loop",
       lower(name_suffix),
       span,
       path
FROM t
WHERE name IN ("node:For",
               "node:While")
GROUP BY path
```

##### Example

```python
1   while foo():
2       while bar():
3           pass
4       for x in s:
5           pass
6
7   for (i, x) in enumerate(seq):
8       if foo(x):
9           bar(i)
```

##### Matches

| Label | Lines |
|:--|:--|
| `loop:while` | 1-5, 2-3 |
| `loop:for` | 4-5, 7-9 |

--------------------------------------------------------------------------------

#### Feature `loop_else`

##### Derivations

[⬇️ feature `loop_with_else`](#feature-loop_with_else)  

##### Specification

```re
  ^(.*/loopelse)/1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)+ \1/.*_pos=(?P<POS>.+)
)*
```

##### Example

```python
1   for x in seq:
2       if foo():
3           break
4   else:
5       bar()
6       biz()
```

##### Matches

| Label | Lines |
|:--|:--|
| `loop_else` | 5-6 |

--------------------------------------------------------------------------------

### Sequential loops

--------------------------------------------------------------------------------

#### Feature `for_each`

Iterate over the elements of a (named) collection.

##### Derivations

[⬇️ feature `find_first_good_element`](#feature-find_first_good_element)  

##### Specification

```re
           ^(.*)/_type=For
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/(?P<_1>target\b.*)/_pos=(?P<POS>.+) # force len(d["POS"]) != len(d["SUFFIX"])
\n(?:\1.+\n)*?\1/(?P=_1)           /id=(?P<SUFFIX>.+)
)+
\n(?:\1.+\n)*?\1/iter/_type=Name
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
```

##### Example

```python
1   for x in seq_1:
2       for y in range(len(seq_3)): # no match
3           pass
4       for i in seq_2:
5           pass
6
7   for ticker, name, price, change, pct in stocks:
8       status = status_labels[cmp(float(change), 0.0)]
9       print("{} is {} ({:.2f})".format(name, status, float(pct)))
```

##### Matches

| Label | Lines |
|:--|:--|
| `for_each:x` | 1-5 |
| `for_each:i` | 4-5 |
| `for_each:ticker` | 7-9 |
| `for_each:name` | 7-9 |
| `for_each:price` | 7-9 |
| `for_each:change` | 7-9 |
| `for_each:pct` | 7-9 |

--------------------------------------------------------------------------------

#### Feature `for_range`

Iterate over a range object.

##### Derivations

[⬆️ feature `for`](#feature-for)  
[⬆️ feature `range`](#feature-range)  

##### Specification

```sql
SELECT "for_range",
       t_range.name_suffix,
       t_for.span,
       t_for.path
FROM t_for
JOIN t_range ON (t_range.path GLOB t_for.path || "*-")
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

##### Derivations

[⬇️ feature `find_best_element_index`](#feature-find_best_element_index)  
[⬇️ feature `find_first_good_element_index`](#feature-find_first_good_element_index)  

##### Specification

```re
           ^(.*)/_type=For
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/target/elts/1/id=(?P<SUFFIX>.+)
\n(?:\1.+\n)*?\1/iter/func/id=enumerate
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
```

##### Example

```python
1   for (i, element) in enumerate(elements):
2       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `for_indexes_elements:i` | 1-2 |

--------------------------------------------------------------------------------

#### Feature `for_indexes`

Iterate over index numbers of a collection.

##### Derivations

[⬇️ feature `find_best_element_index_unpythonic`](#feature-find_best_element_index_unpythonic)  
[⬇️ feature `find_first_good_element_index_unpythonic`](#feature-find_first_good_element_index_unpythonic)  

##### Specification

```re
           ^(.*)/_type=For
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/target/id=(?P<SUFFIX>.+)
\n(?:\1.+\n)*?\1/iter/func/id=range
\n(?:\1.+\n)*?\1/iter/args/[12]/func/id=len
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
```

##### Example

```python
1   for i in range(len(elements)):
2       for j in range(1, len(elements)):
3           pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `for_indexes:i` | 1-3 |
| `for_indexes:j` | 2-3 |

--------------------------------------------------------------------------------

#### Feature `nested_for`

Match a `for` statement nested in _n_ other `for` statements, suffixing it by _n_.

##### Derivations

[⬆️ feature `for`](#feature-for)  

##### Specification

```sql
SELECT "nested_for",
       count(DISTINCT outer_loop.span),
       inner_loop.span,
       inner_loop.path
FROM t_for outer_loop
JOIN t_for inner_loop ON (inner_loop.path GLOB outer_loop.path || "*-")
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
7   for (i1, i2) in enumerate(seq):
8       for (j1, j2) in enumerate(seq):
9           pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `nested_for:1` | 2-5, 8-9 |
| `nested_for:2` | 4-5 |

--------------------------------------------------------------------------------

#### Feature `triangular_nested_for`

A `for` loop with a counter `i` and a nested `for` loop which makes `i` iterations. The total number of iterations is a [triangular number](https://en.wikipedia.org/wiki/Triangular_number).

##### Specification

```re
           ^(.*)/_type=For
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/target/id=(?P<VAR>.+) # capture iteration variable
\n(?:\1.+\n)*?\1/iter/_type=Call
\n(?:\1.+\n)*?\1/iter/func/id=range
\n(?:\1.+\n)*?\1/iter/args/_length=1 # only range(arg1)
(   # i goes from 0 to n, and j from 0 to i
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type=For
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_type=Call
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/func/id=range
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/args/_length=1 # only range(arg1)
\n(?:\1.+\n)* \1/(?P=_1)                    /iter/args/1.*/id=(?P=VAR) # match iteration variable
|   # i goes from 0 to n, and j from i to n
\n(?:\1.+\n)*?\1/iter/args/1/_hash=(?P<STOP>.+) # capture stop expression
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type=For
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_type=Call
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/func/id=range
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/args/_length=2 # only range(arg1, arg2)
\n(?:\1.+\n)* \1/(?P=_1)                    /iter/args/1(/.+)*/id=(?P=VAR) # match iteration variable
\n(?:\1.+\n)* \1/(?P=_1)                    /iter/args/2(/.+)*/_hash=(?P=STOP) # match stop expression
)
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
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
           ^(.*)/_type=For
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/iter/_hash=(?P<HASH>.+) # capture _hash
\n(?:\1.+\n)* \1/(?P<_1>(?:body|orelse)/\d+)/_type=For
\n(?:\1.+\n)*?\1/(?P=_1)                    /iter/_hash=(?P=HASH) # match _hash
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
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

### Non-sequential loops

--------------------------------------------------------------------------------

#### Feature `infinite_while`

Match an infinite loop denoted by `while True` (preferred) or `while 1`.

##### Derivations

[⬇️ feature `accumulate_inputs`](#feature-accumulate_inputs)  
[⬇️ feature `count_inputs`](#feature-count_inputs)  
[⬇️ feature `get_valid_input`](#feature-get_valid_input)  

##### Specification

```re
           ^(.*)/_type=While
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/test/(value=True|n=1)
\n(?:\1.+\n)* \1/[^=]+/_pos=(?P<POS>.+)
```

##### Example

```python
1   while True:
2       while bar():
3           pass
4       while 1:
5           pass
6       else:
7           pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `infinite_while` | 1-7, 4-7 |

--------------------------------------------------------------------------------

### Loop exit

--------------------------------------------------------------------------------

#### Feature `loop_with_raise`

##### Derivations

[⬆️ feature `loop`](#feature-loop)  
[⬆️ feature `raise`](#feature-raise)  
[⬇️ feature `loop_with_early_exit`](#feature-loop_with_early_exit)  

##### Specification

```sql
SELECT "loop_with_raise",
       l.name_suffix,
       l.span,
       l.path
FROM t_loop l
JOIN t_raise r ON (r.path GLOB l.path || "*-")
GROUP BY l.rowid
```

##### Example

```python
1   def fail():
2       for x in seq:
3           if foobar(x):
4               raise ValueError
5
6   def fail_2():
7       for y in seq: # match: false positive
8           try:
9               for z in seq:
10                  if foobar(x):
11                      raise ValueError
12          except:
13              pass
```

_LIMITATION._ False positive when the exception is catch inside the outer loop.

##### Matches

| Label | Lines |
|:--|:--|
| `loop_with_raise:for` | 2-4, 7-13, 9-11 |

--------------------------------------------------------------------------------

#### Feature `loop_with_return`

##### Derivations

[⬆️ feature `loop`](#feature-loop)  
[⬆️ feature `return`](#feature-return)  
[⬇️ feature `loop_with_early_exit`](#feature-loop_with_early_exit)  

##### Specification

```sql
SELECT "loop_with_return",
       l.name_suffix,
       l.span,
       l.path
FROM t_loop l
JOIN t_return r ON (r.path GLOB l.path || "*-")
GROUP BY l.rowid
```

##### Example

```python
1   def func():
2       for x in seq_x:
3           for y in seq_y:
4               while foo():
5                   if bar():
6                       return
```

##### Matches

| Label | Lines |
|:--|:--|
| `loop_with_return:for` | 2-6, 3-6 |
| `loop_with_return:while` | 4-6 |

--------------------------------------------------------------------------------

#### Feature `loop_with_break`

##### Derivations

[⬆️ feature `loop`](#feature-loop)  
[⬆️ feature `node`](#feature-node)  
[⬇️ feature `loop_with_early_exit`](#feature-loop_with_early_exit)  

##### Specification

```sql
SELECT "loop_with_break",
       l.name_suffix,
       max(l.span_start) || "-" || min(l.span_end),
       max(l.path)
FROM t_loop l
JOIN t_node b ON (b.name_suffix="Break"
                  AND b.path GLOB l.path || "*-")
GROUP BY b.rowid
```

##### Example

```python
1   def func():
2       for x in seq_x:
3           for y in seq_y:
4               if foo():
5                   break
```

##### Matches

| Label | Lines |
|:--|:--|
| `loop_with_break:for` | 3-5 |

--------------------------------------------------------------------------------

#### Feature `loop_with_early_exit`

##### Derivations

[⬆️ feature `loop_with_break`](#feature-loop_with_break)  
[⬆️ feature `loop_with_raise`](#feature-loop_with_raise)  
[⬆️ feature `loop_with_return`](#feature-loop_with_return)  
[⬇️ feature `loop_with_late_exit`](#feature-loop_with_late_exit)  

##### Specification

```sql
SELECT "loop_with_early_exit",
       name_suffix || ":" || substr(name_prefix, 11), -- 11 == length("loop_with_") + 1
 span,
 path
FROM t
WHERE t.name_prefix IN ("loop_with_raise",
                        "loop_with_return",
                        "loop_with_break")
```

##### Example

```python
1   for x in seq_x:
2       for y in seq_y:
3           if foo():
4               break
5       else:
6           while True:
7               if bizz():
8                   break
9   def func():
10      for x in seq_x:
11          for y in seq_y:
12              if foo():
13                  return
14          while True:
15              if bizz():
16                  return
17  def fail():
18      for x in seq:
19          if foobar(x):
20              raise ValueError
```

##### Matches

| Label | Lines |
|:--|:--|
| `loop_with_early_exit:for:break` | 2-8 |
| `loop_with_early_exit:while:break` | 6-8 |
| `loop_with_early_exit:for:raise` | 18-20 |
| `loop_with_early_exit:for:return` | 10-16, 11-13 |
| `loop_with_early_exit:while:return` | 14-16 |

--------------------------------------------------------------------------------

#### Feature `loop_with_else`

##### Derivations

[⬆️ feature `loop`](#feature-loop)  
[⬆️ feature `loop_else`](#feature-loop_else)  

##### Specification

```sql
SELECT "loop_with_else",
       name_suffix,
       span,
       path
FROM t_loop
JOIN
  (SELECT max(l.span_start) AS span_start
   FROM t_loop l
   JOIN t_loop_else e ON (e.path GLOB l.path || "*-")
   GROUP BY e.rowid) USING (span_start)
```

##### Example

```python
1   for x in seq:
2       if foo():
3           break
4   else:
5       bar()
6       biz()
```

##### Matches

| Label | Lines |
|:--|:--|
| `loop_with_else:for` | 1-6 |

--------------------------------------------------------------------------------

#### Feature `loop_with_late_exit`

A loop without early exit.

##### Derivations

[⬆️ feature `loop`](#feature-loop)  
[⬆️ feature `loop_with_early_exit`](#feature-loop_with_early_exit)  

##### Specification

```sql
SELECT "loop_with_late_exit",
       l1.name_suffix,
       l1.span,
       l1.path
FROM t_loop l1
LEFT JOIN t_loop_with_early_exit l2 ON (l1.span = l2.span)
WHERE l2.span IS NULL
```

##### Example

```python
1   for x in seq:
2       if foo():
3           break
4   for x in seq:
5       if foo():
6           pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `loop_with_late_exit:for` | 4-6 |

--------------------------------------------------------------------------------

### Exceptions

--------------------------------------------------------------------------------

#### Feature `raise`

##### Derivations

[⬇️ feature `loop_with_raise`](#feature-loop_with_raise)  
[⬇️ feature `try_raise|try_except`](#feature-try_raisetry_except)  

##### Specification

```re
           ^(.*)/_type=Raise
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/exc(=(?P<SUFFIX>None)|/.*\bid=(?P<SUFFIX>.+))
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

[⬇️ feature `try_raise|try_except`](#feature-try_raisetry_except)  

##### Specification

```re
           ^(.*)/(?P<_1>handlers/\d+/(type/(func/|elts/\d+/)?)?)_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/(?P=_1)                                        (id=(?P<SUFFIX>.+)|type=(?P<SUFFIX>None))
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

[⬆️ feature `except`](#feature-except)  
[⬆️ feature `node`](#feature-node)  
[⬆️ feature `raise`](#feature-raise)  
[⬇️ feature `flat_style`](#feature-flat_style)  

##### Specification

```sql
SELECT "try_" || e.name_prefix,
       e.name_suffix,
       max(t.span_start) || "-" || min(t.span_end),
       max(t.path)
FROM t_node t
JOIN t e ON (e.path GLOB t.path || "*-")
WHERE t.name_suffix = "Try"
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

[⬇️ feature `import`](#feature-import)  

##### Specification

```re
           ^(.*)/_type=Import(From)?
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
(
\n(?:\1.+\n)*?\1/module=(?P<SUFFIX>.+)
|
(
\n(?:\1.+\n)*?\1/names/\d+/name=(?P<SUFFIX>.+)
)+
)
```

##### Example

```python
1   import m1, m2, m3
2   import m4
3   from m5 import n1, n2
4   from m6 import n3 as n4
5   from . import n5
6   from .m8 import n6
```

##### Matches

| Label | Lines |
|:--|:--|
| `import_module:None` | 5 |
| `import_module:m1` | 1 |
| `import_module:m2` | 1 |
| `import_module:m3` | 1 |
| `import_module:m4` | 2 |
| `import_module:m5` | 3 |
| `import_module:m6` | 4 |
| `import_module:m8` | 6 |

--------------------------------------------------------------------------------

#### Feature `import_name`

##### Derivations

[⬇️ feature `import`](#feature-import)  

##### Specification

```re
           ^(.*)/_type=ImportFrom
\n(?:\1.+\n)*?\1/_pos=(?P<POS>.+)
\n(?:\1.+\n)*?\1/module=.+
(
\n(?:\1.+\n)*?\1/names/\d+/name=(?P<SUFFIX>.+)
)+
```

##### Example

```python
1   import m1, m2, m3
2   import m4
3   from m5 import n1, n2
4   from m6 import n3 as n4
5   from . import n5
6   from .m8 import n6
```

##### Matches

| Label | Lines |
|:--|:--|
| `import_name:n1` | 3 |
| `import_name:n2` | 3 |
| `import_name:n3` | 4 |
| `import_name:n5` | 5 |
| `import_name:n6` | 6 |

--------------------------------------------------------------------------------

#### Feature `import`

Suffixed by the imported module and, if any, the imported name. In most cases, could replace the two low-level features `import_module` and `import_name`.

##### Derivations

[⬆️ feature `import_module`](#feature-import_module)  
[⬆️ feature `import_name`](#feature-import_name)  

##### Specification

```sql
SELECT "import",
       (CASE
            WHEN m.name_suffix = "None" THEN ""
            ELSE m.name_suffix
        END) || (CASE
                     WHEN n.name_suffix IS NULL THEN ""
                     ELSE ":" || n.name_suffix
                 END),
       m.span,
       m.path
FROM t_import_module m
LEFT JOIN t_import_name n ON (m.span = n.span)
```

##### Example

```python
1   import m1, m2, m3
2   import m4
3   from m5 import n1, n2
4   from m6 import n3 as n4
5   from . import n5
6   from .m8 import n6
```

##### Matches

| Label | Lines |
|:--|:--|
| `import::n5` | 5 |
| `import:m1` | 1 |
| `import:m2` | 1 |
| `import:m3` | 1 |
| `import:m4` | 2 |
| `import:m5:n1` | 3 |
| `import:m5:n2` | 3 |
| `import:m6:n3` | 4 |
| `import:m8:n6` | 6 |

--------------------------------------------------------------------------------

# Iterative patterns

## Loops

--------------------------------------------------------------------------------

#### Feature `count_elements|count_states`

Counting the elements of a sequence (`for`), or the states of an evolution (`while`) (all of them, or only those which satisfy a condition). Suffix with the name of the counter.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `increment`](#feature-increment)  
[⬆️ feature `loop`](#feature-loop)  

##### Specification

```sql
SELECT CASE t_loop.name_suffix
           WHEN "for" THEN "count_elements"
           ELSE "count_states"
       END,
       inc.name_suffix,
       min(t_loop.span_start) || "-" || max(t_loop.span_end), -- The biggest loop...
 t_loop.path
FROM t_loop
JOIN t_increment inc ON (inc.path GLOB t_loop.path || "*-")-- including the incrementation of a variable x...
WHERE NOT EXISTS -- which is not initialized in this loop.
    (SELECT * -- In other words, ensure there is no...
     FROM t_assignment_lhs_identifier x -- assignment...
     WHERE (x.name_suffix = inc.name_suffix -- to the same x...
            AND x.span != inc.span -- distinct from its incrementation...
            AND x.path GLOB t_loop.path || "*-") )-- and enclosed in the loop.
GROUP BY inc.path
```

##### Example

```python
1   for i1 in s1:
2       c1 = 0
3       c2 = 1
4       for i2 in s2:
5           c2 += 1
6           c3 = 0
7           for i3 in s3:
8               if foo(i2, i3):
9                   c3 += 1
10              c1 = c1 + 1
11  while foo(i):
12      i = 0
13      f1, f2 = f2, f
14      index += 1
15      for j in str(f):
16          i += 1
17  counts = [0] * 10
18  for i in x:
19      counts[i % 10] += 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `count_elements:c1` | 4-10 |
| `count_elements:c2` | 4-10 |
| `count_elements:c3` | 7-10 |
| `count_states:index` | 11-16 |
| `count_elements:i` | 15-16 |
| `count_elements` | 18-19 |

--------------------------------------------------------------------------------

#### Feature `count_some_elements|count_some_states`

Restriction of [feature `count_elements|count_states`](#feature-count_elementscount_states) . This time, the incrementation is enclosed in a conditional statement.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `increment`](#feature-increment)  
[⬆️ feature `loop`](#feature-loop)  

##### Specification

```sql
SELECT CASE t_loop.name_suffix
           WHEN "for" THEN "count_some_elements"
           ELSE "count_some_states"
       END,
       inc.name_suffix,
       min(t_loop.span_start) || "-" || max(t_loop.span_end), -- The biggest loop...
 t_loop.path
FROM t_loop
JOIN t_if ON (t_if.path GLOB t_loop.path || "*-")-- including a conditional statement
JOIN t_increment inc ON (inc.path GLOB t_if.path || "*-")-- including the incrementation of a variable x...
WHERE NOT EXISTS -- which is not initialized in this loop.
    (SELECT * -- In other words, ensure there is no...
     FROM t_assignment_lhs_identifier x -- assignment...
     WHERE (x.name_suffix = inc.name_suffix -- to the same x...
            AND x.span != inc.span -- distinct from its incrementation...
            AND x.path GLOB t_loop.path || "*-") )-- and enclosed in the loop.
GROUP BY inc.path
```

##### Example

```python
1   for i1 in s1:
2       c1 = 0
3       c2 = 1
4       for i2 in s2:
5           c2 += 1
6           c3 = 0
7           for i3 in s3:
8               if foo(i2, i3):
9                   c3 += 1
10              c1 = c1 + 1
11  index = 0
12  while foo(i):
13      i = 0
14      f1, f2 = f2, f    
15      if foobar(i):
16          index += 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `count_some_elements:c3` | 7-10 |
| `count_some_states:index` | 12-16 |

--------------------------------------------------------------------------------

## Sequential loops

### Sequential loops with late exit

--------------------------------------------------------------------------------

#### Feature `accumulate_elements`

An accumulator is iteratively updated from its previous value and that of the iteration variable. Suffixed by the name of this accumulator.

##### Derivations

[⬆️ feature `for`](#feature-for)  
[⬆️ feature `update`](#feature-update)  
[⬆️ feature `update_with`](#feature-update_with)  
[⬇️ feature `accumulate_all_elements`](#feature-accumulate_all_elements)  

##### Specification

```sql
SELECT "accumulate_elements",
       t_update_with.name_suffix,
       t_for.span,
       t_for.path
FROM t_for
JOIN t_update ON (t_update.path GLOB t_for.path || "*-")
JOIN t_update_with ON (t_update.path = t_update_with.path)
WHERE t_update.name_suffix GLOB "*:" || t_for.name_suffix
```

##### Example

```python
1   def accumulate_elements(elements):
2       acc = seed
3       for element in elements:
4           acc = element + acc
5           seed += 1
6       return acc
7
8   for i in range(10):
9       acc_1 = combine(acc_1, i)
10      if condition:
11          acc_2 += i
12      else:
13          acc_2 -= i
14
15  for element in elements:
16      print("foo")
17      if predicate(element):
18          print("bar")
19          acc.append(element)
20      print("fiz")
21
22  power = 1
23  for x1 in seq1:
24      acc = set()
25      for x2 in seq2:
26          acc.add(x2)
27          power *= 2 # LIMITATION: no match, since this update does not make use of the iteration variable
28
29  for i in range(10):
30      acc //= foo(bar, i)
31
32  for i in range(10): # no match
33      foo(acc, bar, i)
34
35  for i in range(10): # no match
36      print(foobar, i)
37
38  for c in string:
39      c = c.upper() # no match: this is the iteration variable, not an accumulator
40      print(c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `accumulate_elements:Add` | 3-5, 8-13 |
| `accumulate_elements:Sub` | 8-13 |
| `accumulate_elements:combine` | 8-13 |
| `accumulate_elements:append` | 15-20 |
| `accumulate_elements:add` | 25-27 |
| `accumulate_elements:FloorDiv` | 29-30 |

--------------------------------------------------------------------------------

#### Feature `accumulate_some_elements`

Restriction of [feature `accumulate_elements`](#feature-accumulate_elements) . This time, the update statement is enclosed in a conditional statement.

##### Derivations

[⬆️ feature `for`](#feature-for)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `update`](#feature-update)  
[⬆️ feature `update_with`](#feature-update_with)  
[⬇️ feature `accumulate_all_elements`](#feature-accumulate_all_elements)  

##### Specification

```sql
SELECT "accumulate_some_elements",
       t_update_with.name_suffix,
       t_for.span,
       t_for.path
FROM t_for
JOIN t_if ON (t_if.path GLOB t_for.path || "*-")
JOIN t_update ON (t_update.path GLOB t_if.path || "*-")
JOIN t_update_with ON (t_update.path = t_update_with.path)
WHERE t_update.name_suffix GLOB "*:" || t_for.name_suffix
GROUP BY t_update.path
```

##### Example

```python
1   def accumulate_elements(elements):
2       acc = seed
3       for element in elements:
4           acc = element + acc
5           seed += 1
6       return acc
7
8   for i in range(10):
9       acc_1 = combine(acc_1, i)
10      if condition:
11          acc_2 += i
12      else:
13          acc_2 -= i
14
15  for element in elements:
16      print("foo")
17      if predicate_1(element):
18          print("bar")
19          if predicate_2(element):
20              acc.append(element)
21      print("fiz")
```

##### Matches

| Label | Lines |
|:--|:--|
| `accumulate_some_elements:Add` | 8-13 |
| `accumulate_some_elements:Sub` | 8-13 |
| `accumulate_some_elements:append` | 15-21 |

--------------------------------------------------------------------------------

#### Feature `accumulate_all_elements`

Difference between the set of the features [`accumulate_elements`](#feature-accumulate_elements) and those of [`accumulate_some_elements`](#feature-accumulate_some_elements).

##### Derivations

[⬆️ feature `accumulate_elements`](#feature-accumulate_elements)  
[⬆️ feature `accumulate_some_elements`](#feature-accumulate_some_elements)  

##### Specification

```sql
SELECT "accumulate_all_elements",
       acc.name_suffix,
       acc.span,
       acc.path
FROM t_accumulate_elements acc
WHERE NOT EXISTS
    (SELECT *
     FROM t_accumulate_some_elements
     WHERE path = acc.path
       AND name_suffix = acc.name_suffix)
```

##### Example

```python
1   def accumulate_elements(elements):
2       acc = seed
3       for element in elements:
4           acc = element + acc
5           seed += 1
6       return acc
7
8   for i in range(10):
9       acc_1 = combine(acc_1, i)
10      if condition:
11          acc_2 += i
12      else:
13          acc_2 -= i
14
15  for element in elements:
16      print("foo")
17      if predicate_1(element): # not match: the accumulation is conditioned
18          print("bar")
19          if predicate_2(element):
20              acc.append(element)
21      print("fiz")
```

##### Matches

| Label | Lines |
|:--|:--|
| `accumulate_all_elements:Add` | 3-5 |
| `accumulate_all_elements:combine` | 8-13 |

--------------------------------------------------------------------------------

#### Feature `find_best_element`

An accumulation pattern that, from a given collection, returns the best element verifying a certain condition.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `assignment_rhs_atom`](#feature-assignment_rhs_atom)  
[⬆️ feature `for`](#feature-for)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_test_atom`](#feature-if_test_atom)  
[⬆️ feature `single_assignment`](#feature-single_assignment)  

##### Specification

```sql
SELECT "find_best_element",
       elt.name_suffix || ":" || cnd.name_suffix,
       t_for.span,
       t_for.path
FROM t_for -- A foor loop...
JOIN t_if ON (t_if.path GLOB t_for.path || "*-")-- enclosing a conditional statement...
JOIN t_if_test_atom elt ON (elt.span_start = t_if.span_start -- (comparing...
                            AND elt.name_suffix = t_for.name_suffix)-- the iteration variable...
JOIN t_if_test_atom cnd ON (cnd.span_start = t_if.span_start
                            AND elt.rowid != cnd.rowid)-- to a candidate)...
JOIN t_single_assignment lhs ON (lhs.path GLOB t_if.path || "*-" -- enclosing...
                                 AND cnd.name_suffix = lhs.name_suffix)--  a single assignment of the candidate...
JOIN t_assignment_rhs_atom rhs ON (elt.name_suffix = rhs.name_suffix -- to the iteration variable.
                                   AND rhs.path GLOB lhs.path || "*-")
WHERE NOT EXISTS -- Ensure that there is no...
    (SELECT *
     FROM t_assignment_lhs_identifier -- other assignment...
     WHERE name_suffix == lhs.name_suffix -- of the candidate...
       AND span != lhs.span
       AND path GLOB t_for.path || "*-" ) -- INSIDE the loop.
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
9       candidate = elements[0]
10      for element in elements:
11          if candidate > element:
12              candidate = element
13      return candidate
14
15  def longest_progression(elements):
16      previous, *elements = elements
17      candidate = [previous]
18      best = [previous]
19      for element in elements: # paroxython: find_best_element:element:best...
20          if element <= previous:
21              candidate = [element]
22          else:
23              candidate += [element]
24              if len(candidate) > len(best):
25                  best = candidate
26          previous = element # paroxython: ...find_best_element:element:best
27      return best
28
29  greatest = 0
30  for (i, (a, b)) in enumerate(couples, 1):
31      if b * log(a) > greatest: # double match
32          greatest = b * log(a)
33
34  for digit in word:
35      if digit == previous_digit == "1":
36          previous_digit = None
37      else:
38          previous_digit = digit
```

_LIMITATION._ False negative when the iteration variable does not appear directly in the test of the conditional statement (cf. function `longest_progression()` above). Add a manual hint in such cases.

##### Matches

| Label | Lines |
|:--|:--|
| `find_best_element:element:candidate` | 3-5, 10-12 |
| `find_best_element:element:best` | 19-26 |
| `find_best_element:a:greatest` | 30-32 |
| `find_best_element:b:greatest` | 30-32 |

--------------------------------------------------------------------------------

#### Feature `find_best_element_index`

An accumulation pattern that, from a given collection, returns the index of the best element verifying a certain condition. It also necessarily includes the previous pattern.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `assignment_rhs_atom`](#feature-assignment_rhs_atom)  
[⬆️ feature `for`](#feature-for)  
[⬆️ feature `for_indexes_elements`](#feature-for_indexes_elements)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_test_atom`](#feature-if_test_atom)  
[⬆️ feature `single_assignment`](#feature-single_assignment)  

##### Specification

```sql
SELECT "find_best_element_index",
       elt.name_suffix || ":" || cnd.name_suffix,
       t_for.span,
       t_for.path
FROM t_for -- A foor loop...
JOIN t_for_indexes_elements idx USING (path)--iterating over index numbers and elements...
JOIN t_if ON (t_if.path GLOB t_for.path || "*-")-- enclosing a conditional statement...
JOIN t_if_test_atom elt ON (elt.span_start = t_if.span_start -- (comparing...
                            AND elt.name_suffix = t_for.name_suffix -- the iteration variable...
                            AND elt.name_suffix != idx.name_suffix)-- distinct from the index variable...
JOIN t_if_test_atom cnd ON (cnd.span_start = t_if.span_start
                            AND elt.rowid != cnd.rowid)-- to a candidate)...
JOIN t_single_assignment lhs ON (lhs.path GLOB t_if.path || "*-" -- enclosing...
                                 AND cnd.name_suffix = lhs.name_suffix)--  a single assignment of the candidate...
JOIN t_assignment_rhs_atom rhs ON (elt.name_suffix = rhs.name_suffix -- to the iteration variable...
                                   AND rhs.path GLOB lhs.path || "*-")
JOIN t_assignment_rhs_atom rhs_i ON (idx.name_suffix = rhs_i.name_suffix -- and an assignment of the iteration index.
                                     AND rhs_i.path GLOB t_if.path || "*-")
WHERE NOT EXISTS -- Ensure that there is no...
    (SELECT *
     FROM t_assignment_lhs_identifier -- other assignment...
     WHERE name_suffix == lhs.name_suffix -- of the candidate...
       AND span != lhs.span
       AND path GLOB t_for.path || "*-" ) -- INSIDE the loop.
```

##### Example

```python
1   def find_best_element_index(elements):
2       candidate = bad_value
3       candidate_index = None
4       for (i, element) in enumerate(elements):
5           if is_better(element, candidate):
6               candidate = element
7               candidate_index = i
8       return candidate_index
9   
10  def find_maximum_element_index(elements):
11      candidate = elements[0]
12      candidate_index = 0
13      for (i, element) in enumerate(elements):
14          if candidate > element:
15              candidate = element
16              candidate_index = i
17      return candidate_index
18  
19  greatest = 0
20  result = None
21  for (i, (a, b)) in enumerate(couples, 1):
22      if b * log(a) > greatest: # double match
23          greatest = b * log(a)
24          result = i
25  
26  candidate = elements[0]
27  candidate_index = 0
28  i = 0
29  for element in elements: # LIMITATION: no match
30      if candidate > element:
31          candidate = element
32          candidate_index = i
33      i += 1
34  
35  candidate = elements[0]
36  candidate_index = 0
37  for i in range(1, len(elements)): # LIMITATION: no match, but see the next feature
38      if candidate > elements[i]:
39          candidate = elements[i]
40          candidate_index = i
```

_LIMITATION._ In addition to the limitations of the feature `find_best_element`, this one does not match the non idiomatic variants of the pattern (cf. the latter two examples).

##### Matches

| Label | Lines |
|:--|:--|
| `find_best_element:a:greatest` | 21-24 |
| `find_best_element_index:a:greatest` | 21-24 |
| `find_best_element:b:greatest` | 21-24 |
| `find_best_element_index:b:greatest` | 21-24 |
| `find_best_element:element:candidate` | 4-7, 13-16, 29-33 |
| `find_best_element_index:element:candidate` | 4-7, 13-16 |

--------------------------------------------------------------------------------

#### Feature `find_best_element_index_unpythonic`

A variant of the previous pattern with direct access.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `assignment_rhs_atom`](#feature-assignment_rhs_atom)  
[⬆️ feature `for_indexes`](#feature-for_indexes)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_test_atom`](#feature-if_test_atom)  
[⬆️ feature `index`](#feature-index)  
[⬆️ feature `single_assignment`](#feature-single_assignment)  

##### Specification

```sql
SELECT "find_best_element_index_unpythonic",
       "", -- elt.name_suffix || ":" || cnd.name_suffix,
 idx.span,
 idx.path
FROM t_for_indexes idx-- A foor loop iterating over index numbers...
JOIN t_if ON (t_if.path GLOB idx.path || "*-")-- enclosing a conditional statement...
JOIN t_index elt ON (elt.span_start = t_if.span_start -- (comparing something indexed...
                     AND elt.name_suffix = idx.name_suffix)-- by the index variable...
JOIN t_if_test_atom cnd ON (cnd.span_start = t_if.span_start
                            AND elt.rowid != cnd.rowid)-- to a candidate)...
JOIN t_single_assignment lhs ON (lhs.path GLOB t_if.path || "*-" -- enclosing...
                                 AND cnd.name_suffix = lhs.name_suffix)--  a single assignment of the candidate...
JOIN t_index rhs ON (elt.name_suffix = rhs.name_suffix -- to something indexed by the index variable...
                     AND rhs.path GLOB lhs.path || "*-")
JOIN t_assignment_rhs_atom rhs_i ON (idx.name_suffix = rhs_i.name_suffix -- and an assignment of the iteration variable.
                                     AND rhs_i.path GLOB t_if.path || "*-")
WHERE NOT EXISTS -- Ensure that there is no...
    (SELECT *
     FROM t_assignment_lhs_identifier -- other assignment...
     WHERE name_suffix == lhs.name_suffix -- of the candidate...
       AND span != lhs.span
       AND path GLOB idx.path || "*-" ) -- INSIDE the loop.
```

##### Example

```python
1   candidate = elements[0]
2   candidate_index = 0
3   for i in range(1, len(elements)): # LIMITATION: no match
4       if candidate > elements[i]:
5           candidate = elements[i]
6           candidate_index = i
```

##### Matches

| Label | Lines |
|:--|:--|
| `find_best_element:i:candidate` | 3-6 |
| `find_best_element_index_unpythonic` | 3-6 |

--------------------------------------------------------------------------------

### Sequential loops with early exit

--------------------------------------------------------------------------------

#### Feature `universal_quantification|existential_quantification`

Check whether all elements of a collection satisfy a predicate (universal quantification) or at least one element satisfies a predicate (existential quantification).

##### Derivations

[⬆️ feature `for`](#feature-for)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_test_atom`](#feature-if_test_atom)  
[⬆️ feature `return`](#feature-return)  

##### Specification

```sql
SELECT CASE ret.name_suffix
           WHEN "False" THEN "universal_quantification"
           ELSE "existential_quantification"
       END,
       t_for.name_suffix,
       t_for.span,
       t_for.path
FROM t_for -- A for loop...
JOIN t_if ON (t_if.path GLOB t_for.path || "*-")-- enclosing an if statement...
JOIN t_if_test_atom x ON (x.span_start = t_if.span_start
                          AND x.name_suffix = t_for.name_suffix)-- which tests the iteration variable...
JOIN t_return ret ON (ret.path GLOB t_if.path || "*-" -- and returns...
                      AND ret.name_suffix IN ("True",
                                              "False"))-- a boolean
```

_Remark._ The `return` statement following the loop is untested, which allows to catch some “hidden” quantification patterns. For instance, in `is_prime()` (below), an integer _n_ is prime iff it is coprime with **all** the integers of [2, _n_[ and greater than 1).

##### Example

```python
1   def all_elements_satisfy(elements):
2       for element in elements:
3           if not is_good(element):
4               return False
5       return True
6
7   def some_elements_satisfy(elements):
8       for element in elements:
9           if is_good(element):
10              return True
11      return False
12
13  def is_prime(n):
14      for candidate in range(2, n):
15          if n % candidate == 0:
16              return False
17      return n > 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `universal_quantification:element` | 2-4 |
| `existential_quantification:element` | 8-10 |
| `universal_quantification:candidate` | 14-16 |

--------------------------------------------------------------------------------

#### Feature `find_first_good_element`

Linear search. Return the first element of a sequence satisfying a predicate.

##### Derivations

[⬆️ feature `for_each`](#feature-for_each)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_test_atom`](#feature-if_test_atom)  
[⬆️ feature `return`](#feature-return)  

##### Specification

```sql
SELECT "find_first_good_element",
       lp.name_suffix,
       lp.span,
       lp.path
FROM t_for_each lp -- A for each loop...
JOIN t_if ON (t_if.path GLOB lp.path || "*-")-- enclosing an if statement...
JOIN t_if_test_atom x ON (x.span_start = t_if.span_start
                          AND x.name_suffix = lp.name_suffix)-- which tests the iteration variable...
JOIN t_return ret ON (ret.path GLOB t_if.path || "*-" -- and returns...
                      AND ret.name_suffix = x.name_suffix)-- it.
```

##### Example

```python
1   def search_element(iterable):
2       for element in iterable:
3           if is_good(element):
4                return element
```

##### Matches

| Label | Lines |
|:--|:--|
| `find_first_good_element:element` | 2-4 |

--------------------------------------------------------------------------------

#### Feature `find_first_good_element_index`

##### Derivations

[⬆️ feature `for_indexes_elements`](#feature-for_indexes_elements)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `return`](#feature-return)  

##### Specification

```sql
SELECT "find_first_good_element_index",
       lp.name_suffix,
       lp.span,
       lp.path
FROM t_for_indexes_elements lp -- A for loop on enumerate()...
JOIN t_if ON (t_if.path GLOB lp.path || "*-")-- enclosing an if statement...
JOIN t_return ret ON (ret.path GLOB t_if.path || "*-" -- which returns...
                      AND ret.name_suffix = lp.name_suffix)-- the index variable.
```

##### Example

```python
1   def search_index(sequence, x):
2       for (i, element) in enumerate(sequence):
3           if element == x:
4               return i
```

##### Matches

| Label | Lines |
|:--|:--|
| `find_first_good_element_index:i` | 2-4 |

--------------------------------------------------------------------------------

#### Feature `find_first_good_element_index_unpythonic`

##### Derivations

[⬆️ feature `for_indexes`](#feature-for_indexes)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `index`](#feature-index)  
[⬆️ feature `return`](#feature-return)  

##### Specification

```sql
SELECT "find_first_good_element_index_unpythonic",
       lp.name_suffix,
       lp.span,
       lp.path
FROM t_for_indexes lp -- A for loop on the indexes of a sequence...
JOIN t_if ON (t_if.path GLOB lp.path || "*-")-- enclosing an if statement...
JOIN t_index x ON (x.span_start = t_if.span_start
                   AND x.name_suffix = lp.name_suffix)-- which access to something with the iteration variable...
JOIN t_return ret ON (ret.path GLOB t_if.path || "*-" -- and returns...
                      AND ret.name_suffix = lp.name_suffix)-- the index variable.
```

##### Example

```python
1   def search_index(sequence, x):
2       for i in range(len(sequence)):
3           if sequence[i] == x:
4               return i
```

##### Matches

| Label | Lines |
|:--|:--|
| `find_first_good_element_index_unpythonic:i` | 2-4 |

--------------------------------------------------------------------------------

## Non-sequential loops

### Non-sequential infinite loops

--------------------------------------------------------------------------------

#### Feature `get_valid_input`

Interrogate a stream of inputs up to a valid value, and returning it.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_test_atom`](#feature-if_test_atom)  
[⬆️ feature `infinite_while`](#feature-infinite_while)  
[⬆️ feature `return`](#feature-return)  

##### Specification

```sql
SELECT "get_valid_input",
       ret.name_suffix,
       wt.span,
       wt.path
FROM t_infinite_while wt -- An infinite loop...
JOIN t_assignment_lhs_identifier x1 ON (x1.path GLOB wt.path || "*-")-- features the assignment of a variable...
JOIN t_if ON (t_if.path GLOB wt.path || "*-"
              AND t_if.span_start > x1.span_end)-- followed by a conditional statement...
JOIN t_if_test_atom x2 ON (x1.name_suffix = x2.name_suffix -- testing this variable...
                           AND x2.span_start = t_if.span_start)
JOIN t_return ret ON (ret.path GLOB t_if.path || "*-"
                      AND ret.name_suffix = x1.name_suffix)-- and returning it.
```

##### Example

```python
1   def input_number_between(prompt, lower_bound, upper_bound):
2       while True:
3           number = literal_eval(input(prompt))
4           if lower_bound <= number <= upper_bound:
5               return number
6           print(f"Your number should be between {lower_bound} and {upper_bound}!")
```

##### Matches

| Label | Lines |
|:--|:--|
| `get_valid_input:number` | 2-6 |

--------------------------------------------------------------------------------

#### Feature `count_inputs`

Count inputs until a sentinel value is encountered.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_test_atom`](#feature-if_test_atom)  
[⬆️ feature `increment`](#feature-increment)  
[⬆️ feature `infinite_while`](#feature-infinite_while)  
[⬆️ feature `return`](#feature-return)  

##### Specification

```sql
SELECT "count_inputs",
       ret.name_suffix,
       wt.span,
       wt.path
FROM t_infinite_while wt -- An infinite loop...
JOIN t_assignment_lhs_identifier x1 ON (x1.path GLOB wt.path || "*-")-- features the assignment of a variable...
JOIN t_if ON (t_if.path GLOB wt.path || "*-"
              AND t_if.span_start > x1.span_end)-- followed by a conditional statement...
JOIN t_if_test_atom x2 ON (x1.name_suffix = x2.name_suffix -- testing this variable...
                           AND x2.span_start = t_if.span_start)
JOIN t_return ret ON (ret.path GLOB t_if.path || "*-")-- and returning another variable (an accumulator)...
JOIN t_increment acc ON (acc.name_suffix = ret.name_suffix
                         AND acc.path GLOB wt.path || "*-" -- which is incremented somewhere in the loop...
                         AND acc.path NOT GLOB t_if.path || "*-" -- but not INSIDE the conditional statement.
)
```

##### Example

```python
1   def number_guessing(bound):
2       print("I'm thinking of an integer in [1, %s]." % bound)
3       number = randrange(bound) + 1
4       trial_count = 1
5       while True:
6           candidate = int(input("Your guess #%s? " % trial_count))
7           if candidate == number:
8               print("Yes!")
9               return trial_count
10          print("Too %s!" % ("low" if candidate < number else "high"))
11          trial_count += 1
```

##### Matches

| Label | Lines |
|:--|:--|
| `count_inputs:trial_count` | 5-11 |

--------------------------------------------------------------------------------

#### Feature `accumulate_inputs`

Accumulate a stream of inputs until a sentinel value is encountered.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `if`](#feature-if)  
[⬆️ feature `if_test_atom`](#feature-if_test_atom)  
[⬆️ feature `infinite_while`](#feature-infinite_while)  
[⬆️ feature `return`](#feature-return)  
[⬆️ feature `update`](#feature-update)  

##### Specification

```sql
SELECT "accumulate_inputs",
       ret.name_suffix,
       wt.span,
       wt.path
FROM t_infinite_while wt -- An infinite loop...
JOIN t_assignment_lhs_identifier x1 ON (x1.path GLOB wt.path || "*-")-- features the assignment of a variable...
JOIN t_if ON (t_if.path GLOB wt.path || "*-"
              AND t_if.span_start > x1.span_end)-- followed by a conditional statement...
JOIN t_if_test_atom x2 ON (x1.name_suffix = x2.name_suffix -- testing this variable...
                           AND x2.span_start = t_if.span_start)
JOIN t_return ret ON (ret.path GLOB t_if.path || "*-")-- and returning another variable (an accumulator)...
JOIN t_update acc ON (acc.span_start > t_if.span_start -- which is updated after the conditional...
                      AND acc.span_end <= wt.span_end -- but before the end of the loop...
                      AND acc.name_suffix = ret.name_suffix || ":" || x1.name_suffix) -- with the first variable.
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
23          foobar(acc, x) # paroxython: update:acc:x
24
25  def accumulate_inputs():
26      acc = []
27      while True:
28          x = read()
29          if x > y:
30              return acc
31          acc.append(x)
```

_Remark._
When the update is carried out by a function call, it must be indicated with a manual hint (see line 23).

##### Matches

| Label | Lines |
|:--|:--|
| `accumulate_inputs:acc` | 3-7, 11-15, 19-23, 27-31 |

--------------------------------------------------------------------------------

# Programs

## Spans

--------------------------------------------------------------------------------

#### Feature `whole_span`

Match a whole program, and suffix it by the number of its last line of code.

##### Derivations

[⬇️ feature `functional_style`](#feature-functional_style)  
[⬇️ feature `imperative_style`](#feature-imperative_style)  
[⬇️ feature `object_oriented_style`](#feature-object_oriented_style)  
[⬇️ feature `one_liner_style`](#feature-one_liner_style)  
[⬇️ feature `procedural_style`](#feature-procedural_style)  
[⬇️ feature `scope`](#feature-scope)  
[⬇️ feature `variety`](#feature-variety)  

##### Specification

```re
\A
/_type=Module
(\n.+?)+?
_pos=(?P<POS>.+:).+ # force the path to be empty
(
(?:\n.+)+
_pos=(?P<POS>(?P<SUFFIX>\d+):.+)
|
)
```

##### Example

```python
1   print("See if you can do this. Read each line aloud and press Return between.")
2   message = "this is how to keep an idiot busy for a while"
3   for word in message.split(" "):
4       # a comment
5       input(f"This is {word} cat.")
6   print("Now read the third word in each line from the top!")
7   # a final comment
```

_Remark._ Normally, a source code is stripped from all its comments during its pre-processing.

##### Matches

| Label | Lines |
|:--|:--|
| `whole_span:6` | 1-6 |

--------------------------------------------------------------------------------

#### Feature `scope`

The span of the smallest function (or, by default, of the whole program) enclosing the explicit or implicit assignment of a variable is defined as the scope of this variable.

_Limitation._ The keywords `global` and `nonlocal` are intentionally not taken into account for this feature and the next ones. Using them is not recommended, especially when learning how to program.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `comprehension`](#feature-comprehension)  
[⬆️ feature `function`](#feature-function)  
[⬆️ feature `function_parameter`](#feature-function_parameter)  
[⬆️ feature `iteration_variable`](#feature-iteration_variable)  
[⬆️ feature `subscript_assignment`](#feature-subscript_assignment)  
[⬆️ feature `whole_span`](#feature-whole_span)  
[⬇️ feature `access_outer_scope`](#feature-access_outer_scope)  
[⬇️ feature `global_scope`](#feature-global_scope)  
[⬇️ feature `local_scope`](#feature-local_scope)  
[⬇️ feature `shadowing_scope`](#feature-shadowing_scope)  

##### Specification

```sql
SELECT "scope",
       x.name_suffix,
       max(f.span_start) || "-" || min(f.span_end),
       max(f.path)
FROM t f
JOIN t x ON (x.path GLOB f.path || "*-")
WHERE f.name_prefix IN ("whole_span",
                        "function",
                        "comprehension")
  AND x.name_prefix IN ("function_parameter",
                        "assignment_lhs_identifier",
                        "iteration_variable")
  AND NOT EXISTS
    (SELECT *
     FROM t_subscript_assignment s
     WHERE x.span = s.span)
GROUP BY x.rowid
```

##### Example

```python
1   def foobar(a):
2       def buzz(x):
3           if x % 2:
4               y = 42 # appears twice in buzz, but is tagged only once
5           else:
6               y = 12
7           return x + y + c # c is defined in an outer scope (two levels)
8       b = 42 # local to foobar
9       y = None # local to foobar, shadowed in buzz
10      for i in seq: # seq is nowhere to be found, and certainly not in this scope
11          pass
12      return buzz(a) + b + c # c is defined in an outer scope (one level)
13  
14  c = 10 # global
15  y = 12 # global, shadowed in foobar
16  for j in range(10): # global
17      print(foobar(20) + c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `scope:a` | 1-12 |
| `scope:b` | 1-12 |
| `scope:c` | 1-17 |
| `scope:i` | 1-12 |
| `scope:j` | 1-17 |
| `scope:x` | 2-7 |
| `scope:y` | 2-7, 1-12, 1-17 |

--------------------------------------------------------------------------------

#### Feature `local_scope`

A scope coinciding with the span of a function or a comprehension.

##### Derivations

[⬆️ feature `comprehension`](#feature-comprehension)  
[⬆️ feature `function`](#feature-function)  
[⬆️ feature `scope`](#feature-scope)  
[⬇️ feature `global_scope`](#feature-global_scope)  

##### Specification

```sql
SELECT "local_scope",
       s.name_suffix,
       s.span,
       s.path
FROM t_scope s
JOIN t USING (span)
WHERE t.name_prefix IN ("function",
                        "comprehension")
```

##### Example

```python
1   def foobar(a):
2       def buzz(x):
3           if x % 2:
4               y = 42 # appears twice in buzz, but is tagged only once
5           else:
6               y = 12
7           return x + y + c # c is defined in an outer scope (two levels)
8       b = 42 # local to foobar
9       y = None # local to foobar, shadowed in buzz
10      for i in seq: # seq is nowhere to be found, and certainly not in this scope
11          pass
12      return buzz(a) + b + c # c is defined in an outer scope (one level)
13  
14  c = 10 # global
15  y = 12 # global, shadowed in foobar
16  for j in range(10): # global
17      print(foobar(20) + c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `local_scope:a` | 1-12 |
| `local_scope:b` | 1-12 |
| `local_scope:i` | 1-12 |
| `local_scope:x` | 2-7 |
| `local_scope:y` | 1-12, 2-7 |

--------------------------------------------------------------------------------

#### Feature `global_scope`

A non local scope: either the whole span or nothing.

##### Derivations

[⬆️ feature `local_scope`](#feature-local_scope)  
[⬆️ feature `scope`](#feature-scope)  

##### Specification

```sql
SELECT "global_scope",
       s.name_suffix,
       s.span,
       s.path
FROM t_scope s
LEFT JOIN t_local_scope l USING (span)
WHERE l.rowid IS NULL
```

##### Example

```python
1   def foobar(a):
2       def buzz(x):
3           if x % 2:
4               y = 42 # appears twice in buzz, but is tagged only once
5           else:
6               y = 12
7           return x + y + c # c is defined in an outer scope (two levels)
8       b = 42 # local to foobar
9       y = None # local to foobar, shadowed in buzz
10      for i in seq: # seq is nowhere to be found, and certainly not in this scope
11          pass
12      return buzz(a) + b + c # c is defined in an outer scope (one level)
13  
14  c = 10 # global
15  y = 12 # global, shadowed in foobar
16  for j in range(10): # global
17      print(foobar(20) + c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `global_scope:c` | 1-17 |
| `global_scope:j` | 1-17 |
| `global_scope:y` | 1-17 |

--------------------------------------------------------------------------------

#### Feature `shadowing_scope`

The scope `s` of a variable `x` is said to shadow any scope of `x` which encloses `s`.

##### Derivations

[⬆️ feature `scope`](#feature-scope)  

##### Specification

```sql
SELECT "shadowing_scope",
       enclosed.name_suffix,
       enclosed.span,
       enclosed.path
FROM t_scope enclosing
JOIN t_scope enclosed USING (name_suffix)
WHERE (enclosed.path GLOB enclosing.path || "*-")
```

##### Example

```python
1   def foobar(a):
2       def buzz(x):
3           if x % 2:
4               y = 42 # appears twice in buzz, but is tagged only once
5           else:
6               y = 12
7           return x + y + c # c is defined in an outer scope (two levels)
8       b = 42 # local to foobar
9       y = None # local to foobar, shadowed in buzz
10      for i in seq: # seq is nowhere to be found, and certainly not in this scope
11          pass
12      return buzz(a) + b + c # c is defined in an outer scope (one level)
13  
14  c = 10 # global
15  y = 12 # global, shadowed in foobar
16  for j in range(10): # global
17      print(foobar(20) + c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `shadowing_scope:y` | 2-7, 1-12 |

--------------------------------------------------------------------------------

#### Feature `access_outer_scope`

If a scope encloses a variable `x` without being a scope of `x`, the value of `x` needs to be accessed from an outer scope.

##### Derivations

[⬆️ feature `assignment_lhs_identifier`](#feature-assignment_lhs_identifier)  
[⬆️ feature `function`](#feature-function)  
[⬆️ feature `function_parameter`](#feature-function_parameter)  
[⬆️ feature `iteration_variable`](#feature-iteration_variable)  
[⬆️ feature `loaded_variable`](#feature-loaded_variable)  
[⬆️ feature `scope`](#feature-scope)  

##### Specification

```sql
SELECT "access_outer_scope",
       x.name_suffix,
       f.span,
       f.path
FROM t_function f
JOIN t_loaded_variable x ON (x.path GLOB f.path || "*-")
JOIN t y ON (x.name_suffix = y.name_suffix)
WHERE y.name_prefix IN ("function_parameter",
                        "assignment_lhs_identifier",
                        "iteration_variable")
  AND NOT EXISTS
    (SELECT *
     FROM t_scope s
     WHERE s.path GLOB f.path || "*" -- equal or inner span
       AND s.name_suffix = x.name_suffix )
```

##### Example

```python
1   def foobar(a):
2       def buzz(x):
3           if x % 2:
4               y = 42 # appears twice in buzz, but is tagged only once
5           else:
6               y = 12
7           return x + y + c # c is defined in an outer scope (two levels)
8       b = 42 # local to foobar
9       y = None # local to foobar, shadowed in buzz
10      for i in seq: # no match: seq is nowhere to be found
11          pass
12      return buzz(a) + b + c # c is defined in an outer scope (one level)
13  
14  c = 10 # global
15  y = 12 # global, shadowed in foobar
16  for j in range(10): # global
17      print(foobar(20) + c)
```

##### Matches

| Label | Lines |
|:--|:--|
| `access_outer_scope:c` | 1-12, 2-7 |

--------------------------------------------------------------------------------

## Style

With the exception of `n_liner_style`, the following features are just convenient shortcuts for pipelines combining `"include"` and/or `"exclude"` commands.

--------------------------------------------------------------------------------

#### Feature `object_oriented_style`

A program featuring at least one class definition is considered as object-oriented.

##### Derivations

[⬆️ feature `class`](#feature-class)  
[⬆️ feature `whole_span`](#feature-whole_span)  
[⬇️ feature `functional_style`](#feature-functional_style)  
[⬇️ feature `procedural_style`](#feature-procedural_style)  

##### Specification

```sql
SELECT "object_oriented_style",
       "",
       p.span,
       p.path
FROM t_whole_span p
CROSS JOIN t_class
LIMIT 1
```

##### Example

```python
1   class FooBar(object):
2       pass
3   
4   def foobar():
5       pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `object_oriented_style` | 1-5 |

--------------------------------------------------------------------------------

#### Feature `functional_style`

A program is considered as functional if and only if it features:

- at least one function returning something;
- no procedure definition;
- no class definition;
- no loop;
- no assignment;
- no variable update.

_Limitation._ Potential false negative when the right hand side of the assignment is a lambda function (which is generally considered as an [anti-pattern](https://docs.quantifiedcode.com/python-anti-patterns/correctness/assigning_a_lambda_to_a_variable.html), though).

##### Derivations

[⬆️ feature `assignment`](#feature-assignment)  
[⬆️ feature `function_returning_nothing`](#feature-function_returning_nothing)  
[⬆️ feature `function_returning_something`](#feature-function_returning_something)  
[⬆️ feature `loop`](#feature-loop)  
[⬆️ feature `object_oriented_style`](#feature-object_oriented_style)  
[⬆️ feature `update`](#feature-update)  
[⬆️ feature `whole_span`](#feature-whole_span)  
[⬇️ feature `procedural_style`](#feature-procedural_style)  

##### Specification

```sql
SELECT "functional_style",
       "",
       p.span,
       p.path
FROM t_whole_span p
CROSS JOIN t_function_returning_something
WHERE NOT EXISTS
    (SELECT *
     FROM t
     WHERE t.name_prefix IN ("function_returning_nothing",
                             "object_oriented_style",
                             "loop",
                             "assignment",
                             "update") )
LIMIT 1
```

##### Example

```python
1   from math import pi
2
3   def square_area(side):
4       return side * side
5
6   def circle_area(radius):
7       return pi * radius * radius
8
9   def difference(length):
10      return square_area(length) - circle_area(length / 2)
11
12  assert 0.2146 <= difference(1) <= 0.2147
```

##### Matches

| Label | Lines |
|:--|:--|
| `functional_style` | 1-12 |

--------------------------------------------------------------------------------

#### Feature `procedural_style`

A program is considered as procedural if and only if it is not in object-oriented or functional style, and features at least one function definition.

##### Derivations

[⬆️ feature `function`](#feature-function)  
[⬆️ feature `functional_style`](#feature-functional_style)  
[⬆️ feature `object_oriented_style`](#feature-object_oriented_style)  
[⬆️ feature `whole_span`](#feature-whole_span)  

##### Specification

```sql
SELECT "procedural_style",
       "",
       p.span,
       p.path
FROM t_whole_span p
CROSS JOIN t_function
WHERE NOT EXISTS
    (SELECT *
     FROM t
     WHERE t.name IN ("object_oriented_style",
                      "functional_style"))
LIMIT 1
```

##### Example

```python
1   from bisect import insort
2   def sort(a):
3       for i in range(1, len(a)):
4           insort(a, a.pop(i), hi=i)
5
6   def fibonacci(n):
7       result = []
8       (a, b) = (0, 1)
9       while a < n:
10          result.append(a)
11          (a, b) = (b, a + b)
12      return result
```

##### Matches

| Label | Lines |
|:--|:--|
| `procedural_style` | 1-12 |

--------------------------------------------------------------------------------

#### Feature `imperative_style`

A program is considered as imperative if and only if it features no function or class definition.

##### Derivations

[⬆️ feature `node`](#feature-node)  
[⬆️ feature `whole_span`](#feature-whole_span)  
[⬇️ feature `flat_style`](#feature-flat_style)  

##### Specification

```sql
SELECT "imperative_style",
       "",
       p.span,
       p.path
FROM t_whole_span p
WHERE NOT EXISTS
    (SELECT *
     FROM t
     WHERE t.name IN ("node:FunctionDef",
                      "node:ClassDef"))
```

##### Example

```python
1   for i in range(1, 101):
2       if i % 15 == 0:
3           print("FizzBuzz")
4       elif i % 3 == 0:
5           print("Fizz")
6       elif i % 5 == 0:
7           print("Buzz")
8       else:
9           print(i)
```

##### Matches

| Label | Lines |
|:--|:--|
| `imperative_style` | 1-9 |

--------------------------------------------------------------------------------

#### Feature `flat_style`

A program is considered as flat if and only if it features no conditional, no loop, no exception mechanism, no function definition and no class definition. Note that it is [imperative](#feature-imperative_style) too.

##### Derivations

[⬆️ feature `if`](#feature-if)  
[⬆️ feature `imperative_style`](#feature-imperative_style)  
[⬆️ feature `loop`](#feature-loop)  
[⬆️ feature `try_raise|try_except`](#feature-try_raisetry_except)  

##### Specification

```sql
SELECT "flat_style",
       "",
       p.span,
       p.path
FROM t_imperative_style p
WHERE NOT EXISTS
    (SELECT *
     FROM t
     WHERE t.name_prefix IN ("if",
                             "loop",
                             "try_except",
                             "try_raise"))
```

##### Example

```python
1   import numpy as np
2   m = np.arange(33)
3   n = np.arange(33)
4   a = np.subtract.outer(m ** 2, n ** 2)
5   b = 2 * np.multiply.outer(m, n)
6   c = np.add.outer(m ** 2, n ** 2)
7   i = np.where((a + b + c) == 1000)
8   print((a[i] * b[i] * c[i])[0])
```

##### Matches

| Label | Lines |
|:--|:--|
| `flat_style` | 1-8 |

--------------------------------------------------------------------------------

#### Feature `one_liner_style`

A program is considered a one-liner if and only if it has only one line which is not a definition header, an importation or an assertion.

##### Derivations

[⬆️ feature `node`](#feature-node)  
[⬆️ feature `whole_span`](#feature-whole_span)  

##### Specification

```sql
SELECT "one_liner_style",
       "",
       p.span,
       p.path
FROM t_whole_span p
WHERE cast(p.name_suffix AS INTEGER) - 1 =
    (SELECT count(*)
     FROM t
     WHERE t.name IN ("node:FunctionDef",
                      "node:ClassDef",
                      "node:Assert",
                      "node:Import",
                      "node:ImportFrom"))
```

##### Example

```python
1   from sum_proper_divisors_1 import sum_proper_divisors
2   def abundant_numbers_below(bound):
3       return [n for n in range(1, bound) if sum_proper_divisors(n) > n]
```

##### Matches

| Label | Lines |
|:--|:--|
| `one_liner_style` | 1-3 |

--------------------------------------------------------------------------------

## Counts

--------------------------------------------------------------------------------

#### Feature `class_method_count`

##### Derivations

[⬆️ feature `class`](#feature-class)  
[⬆️ feature `method`](#feature-method)  

##### Specification

```sql
SELECT "class_method_count",
       count(*),
       c.span,
       c.path
FROM t_method m
JOIN t_class c ON (m.path GLOB "*-")
GROUP BY c.rowid
```

##### Example

```python
1   class MyClass:
2
3       def an_instance_method(self, a, b, c):
4           pass
5
6       @staticmethod
7       def a_static_method(f, g):
8           pass
9
10      @classmethod
11      def a_class_method(cls, d, e):
12          pass
```

##### Matches

| Label | Lines |
|:--|:--|
| `class_method_count:3` | 1-12 |

--------------------------------------------------------------------------------

#### Feature `function_line_count`

##### Derivations

[⬆️ feature `function`](#feature-function)  

##### Specification

```sql
SELECT "function_line_count",
       f.span_end - f.span_start + 1,
       f.span,
       f.path
FROM t_function f
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
| `function_line_count:2` | 10-11, 13-14, 18-19, 21-22 |
| `function_line_count:3` | 2-4 |
| `function_line_count:7` | 1-7 |

--------------------------------------------------------------------------------

#### Feature `variety`

Ratio of the number of distinct features to the number of features, multiplied by the SLOC count. On a typical collection of educational programs, this formula should give a number between 1 and 10, with a median value of about 2.5. Programs that are neither too short nor too long, with as little duplication of concepts as possible, should hit the sweet spot (i.e., a large suffix number).

##### Derivations

[⬆️ feature `whole_span`](#feature-whole_span)  

##### Specification

```sql
SELECT "variety",
       cast(count(DISTINCT t.span_start) * count(DISTINCT t.name_prefix) / count(t.name_prefix) AS int),
       p.span,
       p.path
FROM t_whole_span p
CROSS JOIN t
WHERE t.name_prefix != "node"
```

##### Example

```python
1   def fibonacci(n):
2       result = []
3       (a, b) = (0, 1)
4       while a < n:
5           result.append(a)
6           (a, b) = (b, a + b)
7       return result
```

##### Matches

| Label | Lines |
|:--|:--|
| `variety:3` | 1-7 |

--------------------------------------------------------------------------------

## Others

--------------------------------------------------------------------------------

#### Feature `topic|technique|complexity`

These are just some examples of unspecified labels which can be provided in comments as manual hints. In fact, you can create any label you want; just don't forget to define their conversion in your taxonomy, or you can directly tag them with a final taxon.

##### Specification

```
```

##### Example

```python
1   print("See if you can do this. Read each line aloud and press Return between.")
2   message = "this is how to keep an idiot busy for a while"
3   for word in message.split(" "):
4       # paroxython: topic:text_processing
5       input(f"This is {word} cat.")
6   print("Now read the third word in each line from the top!")
7   # paroxython: topic:fun
```

_Remark._
- The location of an all-encompassing hint does not matter, as long as it is on its own line.
- Since all hints are stripped before labelling, the resulting source actually spans from line 1 to line 5.

##### Matches

| Label | Lines |
|:--|:--|
| `topic:fun` | 1-5 |
| `topic:text_processing` | 1-5 |
