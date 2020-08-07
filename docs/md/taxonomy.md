# Taxonomy

## Structure

In Paroxython, the default taxonomy is a [forest](https://en.wikipedia.org/wiki/Tree_(graph_theory)#Forest): a dozen of separate trees with `flow`, `operator`, `meta`, `type`, etc. as their roots. We call **taxon**[^taxon] a path from a root node to a leaf node. Thus:

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

... describes this kind of literal which is a kind of integer which is a kind of number which is a kind of type (as an example, think of the answer to the ultimate question of life, the universe, and everything). Such a nesting makes the taxa especially relevant for the teacher, in that it offers a first structuration of an otherwise scattered knowledge.

An instance of tree rooted in `type` is shown below:

<!-- Here comes the tree -->

This comes[^tree_sql] straight from the tagging of the public repository [The Algorithms - Python](https://github.com/TheAlgorithms/Python). The size of a node is relative to the number of times the corresponding taxon's _prefix_ appears in the programs. Hover over the nodes to see these numbers, or click them to navigate the tree.

[^tree_sql]:
    More precisely, it is the result of
    ```
    SELECT taxon, count(*)
    FROM taxon
    WHERE taxon LIKE 'type/%'
    GROUP BY taxon
    ```
    on the SQLite tag database.

## Mapping the labels onto taxa

Paroxython does not directly produce these taxa. Remember, a program is first tagged with labels (as specified in [`spec.md`](https://repo/paroxython/resources/spec.md)), which are then translated into taxa by a purely morphological operation (search and replace), without any more reference to the original source code.

### 1-1 and N-1 mappings

Suppose a program has been tagged with the labels:

- `literal:True` (the constant `True`).
- `literal:False` (the constant `False`).
- `external_free_call:bool` (a call to the built-in function `bool()`).
- `node:Compare` (a comparison[^compare] expression).

[^compare]:
    On a side note: in the AST, an expression like `a < b < c` counts for **one** (chained) comparison.

The following conversion table (extracted from [`taxonomy.tsv`](https://repo/paroxython/resources/taxonomy.tsv)) will then give the taxa seen above in the subtree `type/boolean`:

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`type/boolean/literal/True`	| `literal:True`
`type/boolean/literal/False` | `literal:False`
`type/boolean` | `external_free_call:bool`
`type/boolean` | `node:Compare`

Note that, somewhat counterintuitively, the conversion goes from right to left. Each line consists of a taxon tab-separated from a label. It is interpreted as “when a program features this label, create that taxon with the same spanning lines”.

- The first two rows are 1-1 mappings: each one translates one label into one taxon.
- The last two rows constitute an N-1 mapping: they translate two distinct labels into a single taxon.

The previous table extract represents the simplest case, where both taxon and label patterns are literal (they don't contain any metacharacter, more on that below).

### 1-0 mapping

At first glance, some of the labels generated during the first step seem redundant, e.g. `"binary_operator:Add"` and `"addition_operator"`. In fact, the former was used to calculate the latter. In [`spec.md`](https://repo/paroxython/resources/spec.md), the definition of `"addition_operator"` is introduced by:

> An addition operator is a binary operator `Add` which has not be classified as a concatenation operator.

This is a good example of a label for internal use only. In the conversion step, it will be simply ignored (i.e., it has no entry in the taxonomy).

### 1-N mapping

When a source code is, say, 42 lines long, it is tagged with the label `"whole_span:42"`. This is an example of a label which produces two taxa: `"meta/program"` and `"meta/sloc/42"`. Both span the whole program and, although it is not obvious, both have their uses:

- The first one is common to all programs, and provides an invariable access key to an all-encompassing span. In a command pipeline, it can be used to [express the absence of a taxon](#expressing-the-absence-of-a-taxon).
- The second one has a variable part, and can be used to filter programs by [size](https://en.wikipedia.org/wiki/Source_lines_of_code) (for example, in `paroxython.recommend_programs`, the pattern `"meta/sloc/[1-4]?[0-9]"` will be used to filter out the programs that have 50 lines or more).

This conversions are triggered by the following rows in the default taxonomy:

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`meta/program` | `whole_span:.+`
`meta/sloc/\1` | `whole_span:(.+)`

As you may have guessed, the right colum can contain [regular expressions](https://en.wikipedia.org/wiki/Regular_expression). On the first row, the sequence of _metacharacters_ `".+"` means: “eat all the characters up to the end of the line.” On the second row, the added parentheses also _captures_ these characters: they are restituted in the replacement pattern by `"\1"`, which denotes a [_backreference_](https://docs.python.org/3/library/re.html#re.sub) to the first captured group.

## Back to the roots

### Functional inspirations: `var`, `abstr`, `appli` and `type`

What are the basic concepts on which programming can be built? As you know, [Alonso Church](https://en.wikipedia.org/wiki/Alonzo_Church) answered this question as early as 1936 (years before the computers were even invented!). The three building blocks of his [lambda calculus](https://en.wikipedia.org/wiki/Lambda_calculus), namely the concepts of **variable**, **abstraction** and **application**, provide us our first three taxonomic roots, which we will denote respectively by `var`, `abstr` and `appli`. To these we can naturally add that of [`type`](https://en.wikipedia.org/wiki/Lambda_calculus#Typed_lambda_calculus), already seen above.

All of these could be enough to describe pure functional programs, at least theoretically. However:

1. Python is no Haskell. It is a multi-paradigm language, with a strong emphasis on imperative programming. Moreover, its [zen](https://www.python.org/dev/peps/pep-0020/) famously holds that “practicality beats purity”.
2. We are not interested in teaching computability theory. Pedagogical considerations take precedence over a crippling respect for mathematical abstractions. We don't need to explain thoroughly the concepts of literal, string, type, built-in function and call for making our young students _feel_ they understand:

```python
print("hello, world")
```

For these reasons, choosing to root our taxonomy in the four basic notions of the typed lambda calculus should be seen more as a tribute than a formal commitment. For instance, like it or not, `var` will essentially bring together everything relating to the concept of assignment; `abstr` will accommodate not only lambda functions, but named ones, methods, generators and even classes; `appli` will cover any call to anything with a `__call__()` method, which Python calls a callable (sorry); finally, `type` will welcome all types, without distinction of mutability.

### Imperative needs: `flow`

The imperative nature of Python requires us to introduce the concept of control `flow`, under which we put the loops, the conditionals, and some other animals[^sequence].

[^sequence]
    The sequence control flow is an exception. As it characterizes the imperative paradigm more than this or that program, it will deliberately be excluded from the features searched by Paroxython.

### For your convenience: `operator`, `condition`, `subscript`

Again, those are mainly practical choices. After all, an `operator` is nothing more than an unassuming function (`abstr`) with a funny name and a funny syntax. And a `condition`[^condition], a combination of function applications (`appli`) which happens to evaluate to a particular `type`. As for the creation of the root `subscript`, it comes from the observation that an awful lot of exciting programs can be written with sequences before venturing out to direct access (e.g., treating the Python lists as [lists](https://en.wikipedia.org/wiki/List_(abstract_data_type)) and not [arrays](https://en.wikipedia.org/wiki/Array_data_structure)). Not that in our default taxonomy, `subscript` includes slicing and dictionary access too.

[^condition]:
    A _condition_ is a boolean expression, not to be confused with a _conditional_ (control structure).

### Imports: `library`

Everything that's imported goes here. Paroxython can tell the difference between standard, third-party and homemade modules.

### Zooming out: `pattern`

Now this is probably the most interesting feature to tag in a beginner-level program. Under `pattern`, you will find numerous variants of the invaluable [accumulation pattern](https://en.wikipedia.org/wiki/Fold_(higher-order_function)) (counting, summing, filtering, finding the “best” element, etc.), but also some early-exit patterns (testing for an universal or existential property, finding the first “good” element), whether by traversing a sequence or evolving a state. This is an aspect of programming which is rarely taught in a conscious and systematic way, and to which Paroxython intends to draw your attention.

### Going `meta`



## Modifying the taxonomy

We suggest you start by copying the default [`taxonomy.tsv`](https://repo/paroxython/resources/taxonomy.tsv) at the same level as the `src` folder that contains your Python programs:

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

You are encouraged to experiment on this copy according to your requirements and your taste.