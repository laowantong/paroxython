# Deep in the pipeline

This part describes in some details how the recommendation system works. It assumes you've already read the [tutorial on recommendations](#getting-recommendations). First of all, let us recall the example of the pipeline we gave at the end.

>>> [
...     {
...         "operation": "impart",
...         "data": "python helpers/parse_syllabus.py {base_path}/timeline.txt",
...     },
...     {
...         "operation": "exclude",
...         "data": [
...             "foo.py",
...             "bar.py",
...             # "buzz.py",
...         ],
...     },
...     {
...         "operation": "include",
...         "data": [
...             "pattern/elements/accumulate",
...             "topic/game",
...             "type/sequence/list",
...         ],
...     },
... ]

## Regular expression patterns

The first thing to clarify is that the strings which constitute the `data` lists are not simple names, but “descriptions” of names. These descriptions, or **patterns**, are written in the language of regular expressions, and more precisely in the dialect implemented by the third-party module [regex](https://pypi.org/project/regex/)[^regex-credits].

[^regex-credits]:
    This module appears to be here to stay, since it is proeminently featured in the documentation of the more mundane standard library [re](https://docs.python.org/3/library/re.html).
    Thanks and kudos to the author, Matthew Barnett: without his awesome work, many parts of our code would have been much tougher to write, and much slower to execute.

..tip::
    If you don't know how to write regular expressions, the good news is that you don't have to worry. When they do not contain certain special characters, they are self-descriptive. That means, for instance, that the string `"type/sequence/list"` happens to be a regular expression which precisely describes (or ”matches”) the string `"type/sequence/list"`. This is the case for all strings that are only made up of so-called _literal_ characters.

    As a matter of fact, all the characters that can appear in a taxon are literal. We advise you to avoid non-literal characters in your program names as well. What are they? Essentially: `.^$*+?{}\[]`. Depending on your operating system, some are already illegal in filenames anyway. To tell the truth, the first one (the dot) is an integral part of most filenames, as an extension separator. However, it turns out that it basically means “any character”, which of course includes the dot itself. So, the regular expression `"hello_world.py"` matches the filename `"hello_world.py"`, and the fact that it matches `"hello_world/py"` and `"hello_worldapy"` shouldn't be a real problem. In any case, you can always prefix (or _escape_) a non-literal character with a backslash `"\"` to make it literal (here, `"hello_world\.py"`): that's all you'll need to know about regular expressions.

The second thing to clarify is that a given pattern will match any string **starting** with it. Thus, `"type/sequence/list"` will match not only `"type/sequence/list"`, but `"type/sequence/list/empty"` and `"type/sequence/list/supercalifragilisticexpialidocious"` too. The same applies to program names. For example, in our personal database, all programs from the Euler project start with `"euler_"`. The pattern `"euler_"` will then match all of them.

In terms of regular expressions, that means that, under the hood, Paroxython invokes [`match()` instead of `search()`](https://docs.python.org/3/library/re.html#search-vs-match). In the rare cases where you want to restrict the whole matching to the pattern itself, simply suffix it with a dollar sign, _i.e._, `"type/sequence/list$"`.

## Execution of a pipeline

A pipeline is a set (or list, but the order is not important) of commands which apply sequentially to a database of program tags. It returns:

- a list of recommended programs;
- an estimation of the learning cost of each concept (i.e., taxon) they implement.

The set of commands constitutes a pipeline that evolves both:

- a selection of programs (initially all those in the database);
- a body of imparted knowledge (initially empty).

.. note::
    During this process, the program selection can never increase, and the imparted knowledge can never decrease.

A command consists of:

- an operation among `"include"`, `"exclude"`, `"impart"` and `"hide"`, optionally suffixed by the quantifier (`" all"`);
- the data to which it applies. This data is (or can be interpreted to produce) a list of criteria, each criterion being:
    - either a program pattern,
    - or a taxon pattern,
    - or a relationship between two taxon patterns (more on this in the [Semantic triples](#semantic-triples) section).

Combining the operation with a criterion is done in four stages:

1. An auxiliary set of programs is calculated.
2. The set of recommended programs (the **selection**) is updated.
3. A new set of taxa may be “learned”, i.e., added to the body of imparted knowledge.
4. The set of taxa to hide in the final report may be updated.

Note that each stage depends on both the operation and the nature of the criterion to which it applies. Let us detail every possible case:

### `"include"` command

Its purpose is to keep only those selected programs that satisfy at least one given criterion.

1. The auxiliary set contains any program such that:
    - either its name matches the given pattern,
    - or its source code:
        - either features at least one taxon matching the given pattern,
        - or satisfies the given relationship.
2. The selection is then restricted to its **intersection** with the auxiliary set.
3. The imparted knowledge is unchanged.

**`"include all"` variant**

Its purpose is to keep only those selected programs that satisfy all given criteria.

```python
{
    "operation": "include all",
    "data": [
        criterion_1,
        criterion_2,
        ...,
        criterion_n
    ]
}
```

... is equivalent to:

```python
    {"operation": "include", "data": [criterion_1]},
    {"operation": "include", "data": [criterion_2]},
    ...,
    {"operation": "include", "data": [criterion_n]}
```

### `"exclude"` command

Its purpose is to filter out of the selection the programs which satisfy at least one given criterion.

1. The same auxiliary set of programs as above (`"include"`) is calculated, but further extended to the programs which import them  (either directly or indirectly). Indeed, when the teacher wants to exclude a certain program, any program that requires it should be excluded as well.
2. The selection is then restricted to its **difference** with the auxiliary set.
3. The imparted knowledge is unchanged.

**`"exclude all"` variant**

Unlike `"include all"`, this variant actually expands the semantics of the system.

```python
{
    "operation": "exclude all",
    "data": [
        criterion_1,
        criterion_2,
        ...,
        criterion_n
    ]
}
```

... excludes the programs satisfying **all** the criteria. This cannot be transformed into a sequence of `"exclude"` commands, which would exclude the programs satisfying **any** of the criteria.

### `"impart"` command

Its main purpose is to track the acquisition of new knowledge. However, if this knowledge is provided by a given set of programs, there is no more need to keep them in the selection of recommended programs.

1. The auxiliary set contains all programs whose name matches at least one of the given pattern (relationships are not supported), plus those which import (either directly or indirectly) at least one of them. In other words, it is the same as above (`"exclude"`), but only in the case where the criterion is a program pattern. In all other cases, this auxiliary set will be empty.
2. The selection is then restricted to its **difference** with the auxiliary set (same as above for `"exclude"`).
3. There are three cases:
    1. If the criterion is a program pattern, all the taxa featured in a program whose name matches this pattern are added to the body of imparted knowledge.
    2. If the criterion is a taxon pattern, all the taxa matching this pattern are added to the body of imparted knowledge.
    3. Otherwise, the body of imparted knowledge is unchanged.

**`"impart all"` variant**

Not supported.

### `"hide"` command

This is the simplest command of all. It merely accumulates the taxa matching the given patterns (relationships are not supported), without other effect on the filter. In the final stage, the accumulated taxa will be filtered out of the generated tables of recommended programs. Note that the learning costs are not affected whatsoever. Even if a taxon is hidden, its individual cost continues to contribute towards the total cost of a program.

**`"hide all"` variant**

Not supported.

## Semantic triples

### Span algebra

Being given a program \(p\) of \(n\) lines, a couple \((i_1, i_2) \) of line numbers such that \(1 \leq i_1 \leq i_2 \leq n\) represents a **span** of \(p\). When Paroxython finds a taxon \(t\) in \(p\), it doesn't just say whether \(p\) features \(t\) or not: it returns the list of spans where \(t\) occurs.

..note::
    Any taxon starting with `"metadata/"` is considered by convention to span the entire program.

It is sometimes interesting to know how the spans of two taxa of the same program are located relatively to each other.

- For instance, a `print()` statement whose span is inside the span of a function indicates that this function has a side-effect.
- A less trivial application stems from the fact that our taxonomy is multi-dimensional: each algorithmic feature can be associated with several taxa at the same time, characterizing it it along several dimensions. For instance, the taxa `flow/loop` and `flow/loop/while` describe the category of a loop; whereas the taxa `flow/loop/exit/early` and `flow/loop/exit/late` describe its exit behavior. These dimensions are independent and, although it is entirely possible to do so, our default taxonomy does not list the results of the cross-product (i.e., `flow/loop/exit/early`, `flow/loop/exit/late`, `flow/loop/while/exit/early` and `flow/loop/while/exit/late`). Querying an hypothetical taxon `flow/loop/exit/early` (or `flow/loop/exit/early/for`, by the way) comes down to querying the taxa `flow/loop` spanning the same lines as `flow/loop/exit/early`.

To express a relation \(\mathfrak{R}\) between the spans of two taxa, we start from the algebra devised in 1983 by James F. Allen in his seminal paper ([PDF](http://cse.unl.edu/~choueiry/Documents/Allen-CACM1983.pdf)) about temporal intervals[^Allen1983]. The so-called Allen's interval algebra defines 13 basic operators which capture all possible relations between two intervals \(X=(x_1, x_2)\) and \(Y=(y_1, y_2)\). The table below uses his terminology:

[^Allen1983]:
    Allen, James F. (26 Nov. 1983). _Maintaining knowledge about temporal intervals_. Communications of the ACM. 26 (11): 832–843. doi:10.1145/182.358434

| Examples | \(\mathfrak{R}\) on endpoints | \(X \mathbin{\mathfrak{R}} Y\)  | \(Y \mathbin{\mathfrak{R}} X\)  | Keys |
|:----:|:----:|:----:|:----:|:----:|
| `....XXXXX........` &nbsp; | | |
| `....YYYYY........` &nbsp; | \(x_1 = y_1 \leq x_2 = y_2\)       &nbsp; | \(X\) `equals` \(Y\)    &nbsp; | \(Y\) `equals` \(X\)        &nbsp; | `x=y≤x=y`
| `....YYYYYYYYY....` &nbsp; | \(x_1 = y_1 \leq x_2 \leq y_2\)    &nbsp; | \(X\) `starts` \(Y\)    &nbsp; | \(Y\) `started by` \(X\)    &nbsp; | `x=y≤x≤y`
| `..YYYYYYYYY......` &nbsp; | \(y_1 \leq x_1 \leq x_2 \leq y_2\) &nbsp; | \(X\) `during` \(Y\)    &nbsp; | \(Y\) `contains` \(X\)      &nbsp; | `y≤x≤x≤y`
| `.YYYYYYYY........` &nbsp; | \(y_1 \leq x_1 \leq x_2 = y_2\)    &nbsp; | \(X\) `finishes` \(Y\)  &nbsp; | \(Y\) `finished by` \(X\)   &nbsp; | `y≤x≤x=y`
| `....|...|..YYYYY.` &nbsp; | \(x_1 \leq x_2 \leq y_1 \leq y_2\) &nbsp; | \(X\) `before` \(Y\)    &nbsp; | \(Y\) `after` \(X\)         &nbsp; | `x≤x≤y≤y`
| `....|...|YYYYY...` &nbsp; | \(x_1 \leq x_2 = y_1 \leq y_2\)    &nbsp; | \(X\) `meets` \(Y\)     &nbsp; | \(Y\) `met by` \(X\)        &nbsp; | `x≤x=y≤y`
| `....|..YYYYY.....` &nbsp; | \(x_1 \leq y_1 \leq x_2 \leq y_2\) &nbsp; | \(X\) `overlaps` \(Y\)  &nbsp; | \(Y\) `overlapped by` \(X\) &nbsp; | `x≤y≤x≤y`

These well-known operators apply quite nicely to our spans, with the following adjustments:

**Synonyms.** The 13 operator names, whose some don't make much sense in a non-temporal context, are extended
with a number of synonyms, such as `"inside"` for `"during"`, and `"equal"` or `"is"` for
`"equals"`. The current list can be found
[here](https://github.com/laowantong/paroxython/blob/master/paroxython/compare_spans.py#L195).


**Non-strict inequalities.** In the above table, contrary to the convention on time intervals, we
consider the inequalities to be large. In a program, most features span exactly one (logical) line
(i.e., \(x_1=x_2\)): this is simply not possible with the original relations on endpoints. Besides,
when we look for a function which  **contains** a loop, we are generally not interested in whether
the loop **finishes** on the last line. Blind adherence to strictness convention would force us to
express our query as a disjunction of these two relations for the following program to be selected:

```python
1   def first_missing_non_negative(l):
2       elements = set(l)
3       for natural in range(len(elements) + 1):
4           if natural not in elements:
5               return natural
```

**Strict inequalities.** In addition to the existing relations, all combinations of strict and non-strict
conditions are generated, for instance \(x_1 < x_2 < y_1 \leq y_2\). That adds up to 162 in total[^predicate_count].

[^predicate_count]:
    \(162 = 6 \times 27\), where \(6\) is the number of distinct permutations of the quadruple \((x, x, y, y)\), and \(27=3^3\) the number of elements of the triple auto-product of \(3\) symbols (`=`, `≤` and `<`).

**Keys.** As we use many more operators than Allen, giving an English name to every single one is not an option. Paroxython actually identifies them by a unique key (see the last column of the table above) calculated like this:

1. Start from the chain of equalities and inequalities that defines the relations between the two spans' endpoints: \(y_1 < x_1 = y_2 \leq x_2\).
2. Drop the indices (since, for a given \(x\) or \(y\), indice \(1\) always comes before indice \(2\), no information is lost): \(y < x = y \leq x\).
3. Rewrite the formula using only the five characters `"="`, `"<"`, `"≤"`, `"x"` and `"y"`: `y<x=y≤x`.

**Key normalization.**
Paroxython tries (cf. `paroxython.normalize_predicate.normalize_predicate`) to be tolerant with the user input. The verb `"is"` is ignored, except when it constitutes the whole string (thus, `"is after"` comes down to `"after"`). When an operator is not an Allen's name or a predefined synonym, the following normalization process is applied:

1. Replace any `<=` by `≤`.
2. Replace any `==` by `=`.
3. Strip all characters distinct from `"="`, `"<"`, `"≤"`, `"x"` and `"y"`.
4. If the string is `"x=y"` or `"y=x"`, replace it by `"x=y≤x=y"`.
2. If the string contains only one `x` (resp. `y`), expand it into `x≤x` (resp. `y≤y`).

This allows the user to be understood when entering formulas like  `x == y`, `x <= y` or `y1 < x1 == x2 <= y2`.

### Positive semantic triples

A pipeline command can apply not only to patterns of programs and taxa, but also to relationships between two patterns of taxa. Being given an operator \(\mathfrak{R}\) and two taxon patterns \(t_1\) and \(t_2\), the statement \(t_1 \mathbin{\mathfrak{R}} t_2\) will be codified in the form of the _subject–predicate–object_ expression \((t_1, \mathfrak{R}, t_2)\), which can be entered as a mere Python tuple `(t1, R, t2)`. For instance, the following pipeline command will only keep programs featuring a conditional inside a loop **or** (inclusive) ended by a `return` statement (like the function `first_missing_non_negative()` given above).

```python
    {
        "operation": "include",
        "data": [
            ("flow/loop", "contains", "flow/conditional"),
            ("flow/conditional", "finished by", "subroutine/return"),
        ]
    },
```

It is currently not possible to chain several operators with shared operands, for example to keep only the programs that feature a conditional inside a loop **and** ended by a `return` statement: the quintuple `("flow/loop", "contains", "flow/conditional", "finished by", "subroutine/return")` would raise an error. As it stands, the best that we can do is to chain the commands themselves:

```python
    {
        "operation": "include",
        "data": [
            ("flow/loop", "contains", "flow/conditional"),
        ]
    },
    {
        "operation": "include",
        "data": [
            ("flow/conditional", "finished by", "subroutine/return"),
        ]
    },
    {
        "operation": "include",
        "data": [
            ("subroutine/return", "contains", "flow/loop"),
        ]
    },
```

This keeps only the programs that feature a conditional inside a loop **and** a conditional ended by a `return` statement **and** a `return` statement inside a loop. The result is a subset of the previous one, but may still include programs where the two loops, conditionals or `return` statements are distinct.

### Negative semantic triples

Our pipeline system takes a set of programs as input, and produces a subset of those programs as output.

With our pipeline system,

Avec notre système, certaines conditions ne peuvent être exprimées qu'en introduisant la possibilité de nier les relations.

Supposons que vous, en tant qu'enseignant, souhaitiez inclure dans votre cours sur l'affectation la notion d'affectation parallèle, par exemple pour introduire l'échange sans variable auxiliaire:

```python
(a, b) = (b, a)
```

Dans la taxonomie, cette notion est répertoriée à la fois comme cas particulier de l'affectation de variable (taxon \(t_1 = \) `variable/assignment/parallel`) et comme faisant appel à la notion de tuple: taxon (\(t_2 = \) `type/sequence/tuple`. Or, vous souhaitez n'introduire officiellement les tuples que bien plus tard dans votre cours. Vous souhaitez donc exclure des recommandations tout programme mettant en œuvre un tuple, sauf si celui-ci intervient dans une affectation parallèle. L'ensemble \(\mathcal{P}\) des programmes peut être partitionné en quatre sous-ensembles:

- \(\mathcal{P}_0\) l'ensemble des programmes ne mettant en œuvre aucun tuple (donc a fortiori aucune affectation parallèle).
- \(\mathcal{P}_1\) l'ensemble des programmes mettant en œuvre un ou plusieurs tuples, mais systématiquement dans le cadre d'une affectation parallèle.
- \(\mathcal{P}_2\) l'ensemble des programmes mettant en œuvre deux tuples ou plus, avec au moins un dans le cadre d'une affectation parallèle, et au moins un au-dehors.
- \(\mathcal{P}_3\) l'ensemble des programmes mettant en œuvre un ou plusieurs tuples, mais aucun dans le cadre d'une affectation parallèle.

Paroxython doit donc nous recommander tous les programmes de \(\mathcal{P}_0 \cup \mathcal{P}_1\), mais aucun de \(\mathcal{P}_2 \cup \mathcal{P}_3\).

Le pipeline suivant ne donne **pas** le résultat cherché. La première opération restreint la sélection à \(\mathcal{P}_1 \cup \mathcal{P}_2\). La seconde en retire \(\mathcal{P}_2\). Le résultat est donc \(\mathcal{P}_1\):

```python
    {
        "operation": "include",
        "data": [
            "variable/assignment/parallel",
        ]
    },
    {
        "operation": "exclude",
        "data": [
            "type/sequence/tuple",
        ]
    },
```

Dans cette deuxième tentative, le deuxième datum est un motif d'expression régulière qui couvre n'importe quel taxon ne commençant pas par `"type/sequence/tuple"`. Or, tout programme comporte au moins un taxon satisfaisant à cette propriété. Le résultat est donc \(\mathcal{P}\).

```python
    {
        "operation": "include",
        "data": [
            "variable/assignment/parallel",
            "(?!type/sequence/tuple)",
        ]
    },
```

Si l'on applique l'opération inverse sur la contraposée, le résultat est vide. En effet, le premier datum exclut tous les programmes qui comportent au moins un taxon qui n'est pas une affectation parallèle.

```python
    {
        "operation": "exclude",
        "data": [
            "(?!variable/assignment/parallel)",
            "type/sequence/tuple",
        ]
    },
```

Le pipeline suivant ne garde que les programmes comportant au moins un tuple qui est une affectation parallèle, soit \(\mathcal{P}_1\) \cup \mathcal{P}_2\):

```python
    {
        "operation": "include",
        "data": [
            ("type/sequence/tuple", "is", "variable/assignment/parallel"),
        ]
    },
```

Il est en fait équivalent à:

```python
    {
        "operation": "include",
        "data": [
            "variable/assignment/parallel",
        ]
    },
```



```python
    {
        "operation": "exclude",
        "data": [
            ("type/sequence/tuple", "is not", "variable/assignment/parallel"),
        ]
    },
```



Cependant, vous ne souhaitez introduire officiellement
