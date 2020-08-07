# Taxonomy

## Structure

In Paroxython, the default taxonomy is a [forest](https://en.wikipedia.org/wiki/Tree_(graph_theory)#Forest): a dozen of separate trees with `flow`, `operator`, `metadata`, `type`, etc. as their roots. We call **taxon**[^taxon] a path from a root node to a leaf node. Thus:

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

At first glance, some of the labels generated during the first step seem redundant. For instance, `"binary_operator:Add"` and `"addition_operator"`. In fact, the former was used to calculate the latter. In [`spec.md`](https://repo/paroxython/resources/spec.md), the definition of `"addition_operator"` is introduced by these words: “An addition operator is a binary operator `Add` which has not be classified as a concatenation operator”.

This is a good example of label for internal use only. In the conversion step, it will be simply ignored (i.e., it has no entry in the taxonomy).

### 1-N mapping

When a source code is, say, 8 lines long, it is tagged with the label `"whole_span:8"`. This is an example of a label which produces two taxa: `"metadata/program"` and `"metadata/sloc/8"`. Both span the whole program and, although it is not obvious, both have their uses.

The first one is common to all programs, and provides an invariable access key to an all-encompassing span. In a command pipeline, it can be used to [express the absence of a taxon](#expressing-the-absence-of-a-taxon).

The second one has a variable part, and can be used to filter programs by [size](https://en.wikipedia.org/wiki/Source_lines_of_code) (for example, in `paroxython.recommend_programs`, the pattern `"metadata/sloc/[1-5]"` will be used to filter out the programs that have more than 5 lines).

This conversions are triggered by the following rows in the default taxonomy:

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`metadata/program` | `whole_span:.+`
`metadata/sloc/\1` | `whole_span:(.+)`

As you may have guessed, the right colum can contain [regular expressions](https://en.wikipedia.org/wiki/Regular_expression). On the first row, the sequence of _metacharacters_ `".+"` means: “eat all the characters up to the end of the line.” On the second row, the added parentheses also _captures_ these characters: they are restituted in the replacement pattern by `"\1"`, which denotes a [_backreference_](https://docs.python.org/3/library/re.html#re.sub) to the first captured group.
