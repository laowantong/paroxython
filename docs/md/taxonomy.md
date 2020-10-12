# Taxonomy

## Structure

In Paroxython, the default taxonomy is a [forest](https://en.wikipedia.org/wiki/Tree_(graph_theory)#Forest): a handful of separate trees with `flow`, `operator`, `meta`, `type`, etc. as their roots. We call **taxon**[^taxon] a path from a root node to a leaf node. Thus:

[^taxon]:
    This contrasts with the convention in biological classification, where the term [taxon](https://en.wikipedia.org/wiki/Taxon) refers to a taxonomic **unit** (a node of the tree). For instance, [African Elephant ](https://en.wikipedia.org/wiki/African_elephant) is classified under the taxon _Loxodonta_. However, a taxon (implicitely) “encompasses all included taxa of lower rank”, here:

    - Kingdom:	_Animalia_
    - Phylum:	_Chordata_
    - Class:	_Mammalia_
    - Order:	_Proboscidea_
    - Family:	_Elephantidae_
    - Subfamily:	_Elephantinae_
    - Genus:	_Loxodonta_

    Since our nodes are not uniquely named (e.g., there are several nodes `literal`), we make all the lower rank nodes explicit by concatenating them (i.e., `type/number/integer/literal` instead of simply `literal`, which would be ambiguous)🐘.

```plain
type/number/integer/literal
```

... describes, you know... this kind of literal which is a kind of integer which is a kind of number which is a kind of type (as an example, think of the answer to the ultimate question of life, the universe, and everything).

In the visualization below, we have introduced the pseudo-root “🐍” to gather all the trees into one:

<div id="tree" style="width: 100%; height: 1000px;"></div>

This comes[^tree_sql] straight from the tagging of the public repository [The Algorithms - Python](https://github.com/TheAlgorithms/Python). The size of a node is relative to the number of times the corresponding taxon's _prefix_ appears in these programs.

[^tree_sql]:
    More precisely, it is the result of executing
    ```
    SELECT taxon, count(*)
    FROM taxon
    WHERE taxon not LIKE 'meta/count/%'
    GROUP BY taxon
    ```
    on the SQLite tag database.

Hover over the nodes to see these numbers, or click them to navigate the tree. By the way, you may click on `type` to better follow the subsequent explanations.

## Mapping the labels onto taxa

Paroxython does not directly grow these forest of taxa. Remember, a program is first tagged with labels (as specified in `spec.md`). Those are then translated into taxa by a purely morphological operation (search and replace), without any more reference to the original source code.

### 1-1 mappings

Suppose a program has been tagged with the labels:

- `literal:True` (the constant `True`).
- `literal:False` (the constant `False`).
- `external_free_call:bool` (a call to the built-in function `bool()`).

[^compare]:
    On a side note: in the AST, an expression like `a < b < c` counts for **one** (chained) comparison.

The following conversion table (extracted from `taxonomy.tsv`) will then give the taxa seen above in the subtree `type/boolean`:

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`type/boolean/literal/True`	| `literal:True`
`type/boolean/literal/False` | `literal:False`
`type/boolean` | `external_free_call:bool`

Note that, somewhat counterintuitively, the conversion goes from right to left. Each line consists of a taxon tab-separated from a label. It is interpreted as “when a program features this label, create that taxon with the same spanning lines”.

All of these rows define 1-1 mappings: each one translates one label into one taxon.

### N-1 mappings

The previous table extract represents the simplest case, where both taxon and label patterns are literal. Below, the second label pattern is a non-literal [regular expression](https://en.wikipedia.org/wiki/Regular_expression):

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`type/sequence/list` | `external_free_call:list`
`type/sequence/list` | `member_call_method:(append|extend|insert|reverse|sort)`

It defines a 5-1 mapping, which converts five possible labels (`member_call_method:append`, `member_call_method:extend`, and so on) into a single taxon (the metacharacter `"|"` meaning “or”). These two rows thus constitute a 6-1 mapping.

### 1-N mapping

When a source code is, say, 42 lines long, it is tagged with the label `"whole_span:42"`. This is an example of a single label which produces two taxa: `"meta/program"` and `"meta/count/program/sloc/42"`. Both span the whole program and, although it is not obvious, both have their uses:

- The first one is common to all programs, and provides an invariable access key to an all-encompassing span. In a command pipeline, it can be used to [express the absence of a taxon](#expressing-the-absence-of-a-taxon).
- The second one has a variable part, and can be used to filter programs by [size](https://en.wikipedia.org/wiki/Source_lines_of_code) (for example, in `paroxython.recommend_programs`, the pattern `"meta/count/program/sloc/[1-4]?[0-9]"` will be used to filter out the programs that have 50 lines or more).

This conversions are triggered by the following rows in the default taxonomy:

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`meta/program` | `whole_span:.+`
`meta/count/program/sloc/\1` | `whole_span:(.+)`

On the first row, the sequence of metacharacters `".+"` means: “eat all you can up to the end of the line.” On the second row, the added parentheses also _captures_ these characters: they are restituted in the replacement pattern by `"\1"`, which denotes a [_backreference_](https://docs.python.org/3/library/re.html#re.sub) to the first captured group.

Another example could be:

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`type/sequence/list` | `member_call_method:(append|extend|insert|reverse|sort)`
`call/subroutine/method/sequence/list/\1` | `member_call_method:(append|extend|insert|reverse|sort)`

... which means: when you encounter a label `member_call_method:sort` (for instance), that means the program features a list and a call to the `sort()` method.

### 1-0 mapping

At first glance, some of the labels generated during the first tagging step seem redundant, e.g. `"binary_operator:Add"` and `"addition_operator"`. In fact, the former was used to calculate the latter. In `spec.md`, the definition of `"addition_operator"` is introduced by:

> An addition operator is a binary operator `Add` which has not be classified as a concatenation operator.

This is a good example of a label for internal use only. In the conversion step, it will be simply ignored (i.e., it has no entry in the taxonomy).


## Back to the roots

### Functional inspirations: `var`, `def`, `call` and `type`

What are the basic concepts on which computing can be built? As you know, [Alonso Church](https://en.wikipedia.org/wiki/Alonzo_Church) answered this very question as early as 1936 (years before the computers were even invented!). The three building blocks of his [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus), namely the concepts of **variable**, **abstraction** and **application**, provide us our first three taxonomic roots, which we will denote respectively by `var`, `def` and `call`. To these we can naturally add that of `type`, already shown above.

All of these could be enough to describe pure functional programs, at least theoretically. However:

1. Python is no Haskell. It is a multi paradigm language, with a strong emphasis on imperative programming. And its [zen](https://www.python.org/dev/peps/pep-0020/) famously holds that “practicality beats purity”.
2. Here, we are not interested in teaching generalized computability. Pedagogical considerations take precedence over a crippling respect for mathematical abstractions. For instance, we don't need to explain thoroughly the concepts of literal, string, type, built-in function and call for making our young students _feel_ they understand:

```python
print("hello, world")
```

For these reasons, choosing to root our taxonomy in the four basic notions of the typed lambda calculus should be seen more as a tribute than a formal commitment. More specifically:

- `var` will essentially bring together everything relating to the concept of assignment and scoping;
- `def` will accommodate not only lambda functions, but named ones, methods, generators and even classes. Note that this does _not_ include variable definitions.
- `call` will cover any call to anything with a `__call__()` method, which Python calls a callable (sorry);
- finally, `type` will welcome all types, no purity required.

### Imperative needs: `flow`

The imperative nature of Python demands that we introduce the concept of control `flow`, under which we put the loops, the conditionals, and some other animals[^sequence].

[^sequence]:
    The sequence control flow is an exception. As it characterizes the imperative paradigm more than this or that program, it will deliberately be excluded from the features searched by Paroxython.

### For your convenience: `operator`, `condition`, `subscript`

Again, those are mainly practical choices. After all, an `operator` is nothing more than an unassuming function call with a funny name and a funny syntax. And a `condition`[^condition], a combination of function calls which happens to evaluate to a particular `type`. As for the creation of the root `subscript`, it comes from the observation that an lot of exciting programs can be written with sequences before venturing out to direct access (that is, as long as we treat Python lists as [lists](https://en.wikipedia.org/wiki/List_(abstract_data_type)) and not [arrays](https://en.wikipedia.org/wiki/Array_data_structure)). Not that in our default taxonomy, `subscript` includes slicing and dictionary access too.

[^condition]:
    A _condition_ is a boolean expression, not to be confused with a _conditional_ (control structure).

### Importations

Previously classified under `def`, since version 0.6.0, the `import` statement has now its own root in the taxonomy.

### Zooming out: `pattern`

Now this is arguably the most interesting feature to tag in a beginner-level program. Under `pattern`, you will find numerous variants of the invaluable [accumulation pattern](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) (counting, summing, filtering, finding the “best” element, etc.), but also some early-exit patterns (testing for an universal or existential property, finding the first “good” element, etc.), whether by traversing a sequence or evolving a state. A (currently) small number of common expression patterns are also available. However, the common assignment idioms (such as incrementation, swap, slide, conditional  assignment) are classified under `var/assignment/explicit`.

Although the relative size of `pattern` is the smallest of the taxonomy, note that it is almost that of `meta/program` (which has one occurrence per program): in other words, almost all programs feature such a pattern (which spans several lines).

The loop patterns constitute an aspect of programming which is not always taught in a conscious and systematic way, and to which Paroxython intends to draw your attention.

..warning::
    For priority reasons, Paroxython searches for these loop patterns in “statement” loops only, not in “comprehension” loops. This may change in a future version.

### Tagging with `style`

#### Paradigms

Python allows you to mix freely multiple paradigms. However, for Paroxython, every program will fall into exactly one of the following four categories, always associated to the whole span:

1. `style/object_oriented` if it features at least one class definition;
2. `style/functional` if it is not object oriented, and features at least one function returning something, but no loop and no assignment;
3. `style/procedural` if it is neither object oriented or functional, and features at least one subroutine definition;
4. `style/imperative` if it features no subroutine or class definition.

Additionally, `style/imperative/flat` is the _no-indent_ version of the latter (no loop, conditional, etc.).

Functional _traits_ are also tagged. The corresponding taxa start with: `style/functional_trait/`, and are suffixed by `lambda`, `higher_order`, `pure_function`, `map`, `filter`, `reduce`, etc. Unlike `style/functional`, which spans the entire program, these taxa are located on certain lines. They can appear in a program of any (all-encompassing) style.

Independently of the 4-partition, `style/one_liner` denotes any program whose exactly one SLOC is neither a definition header, an importation or an assertion. For instance, the following program is considered a one-liner:

```python
from sum_proper_divisors_1 import sum_proper_divisors

def abundant_numbers_below(bound):
    # An abundant number is a number for which the sum of its proper divisors
    # is greater than the number itself (Wikipedia).
    return [n for n in range(1, bound) if sum_proper_divisors(n) > n]
```

#### Flawed styles

Although Paroxython is no linter, it may tag some unpythonic (i.e., non-idiomatic) or naive patterns, frequent in the beginners' code. For instance:

```python
aux = a
a = b
b = aux
```

... is tagged `style/unpythonic/swap`, and:

```python
if condition:
    return False
else:
    return True
```

is tagged `style/naive/return_condition`. Search `_unpythonic` and `_naive` in `spec.md` for the current list (which could of course be extended _ad libitum_).

### Going `meta`

Paroxython will store inside the `meta` tree some program metadata, such as the number of lines. Some children, such as `topic`, `technique`, `complexity`, are already provided, which you can fill in by adding a manual hint in the source code of the programs.

## Modifying the taxonomy

The definition of a taxonomy is, at least partly, a matter of pedagogical choices. You are encouraged to duplicate the default taxonomy, and replace or delete those taxa that do not fit your course purpose or logic.

Copy the default `taxonomy.tsv` at the same level as the `src` folder that contains your Python programs:

```plain
programming_101/
├── taxonomy.tsv
├── src/
│   ├── hello_world.py
│   ├── gob's_program.py
|   ├── ...
```

This way, omitting the option `--taxonomy` like in the command below will use your copy instead of the original.

```
paroxython collect programming_101/src
```

You can now freely experiment on this copy.
