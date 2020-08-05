r"""
Translate labels into taxa.

## Description

This translation comes after `paroxython.label_programs` has tagged a program with the **labels**
defined in [`spec.md`](https://repo/paroxython/resources/spec.md). Its purpose is to convert these
labels into the **taxa** defined (by default) in
[`taxonomy.tsv`](https://repo/paroxython/resources/taxonomy.tsv).

## Example

Let's return to the Jupyter notebook's cell given in the introduction:

```python
1   %%paroxython labels
2   def fibonacci(n):
3       result = []
4       (a, b) = (0, 1)
5       while a < n:
6           result.append(a)
7           (a, b) = (b, a + b)
8       return result
```

Note that the magic cell-command `%%paroxython` has now a `labels` argument. This produces the
following output (limited to the first four rows):

| Label | Lines |
|:--|:--|
| `addition_operator` | 7 |
| `assignment` | 3, 4, 7 |
| `assignment_lhs_identifier:a` | 4, 7 |
| `assignment_lhs_identifier:b` | 4, 7 |

These labels are low-level tags, intended for internal use only. The tags of interest to the end
user, the taxons, are calculated from these by the present module. Let us provide some examples of
such translations.

### 1-1 mapping

- Label: `("addition_operator", [(7, 7, "...")])`.
- Taxon: `("operator/arithmetic/addition", {(7, 7, "..."): 1})`.

Note that, unlike a label, a taxon may feature one or several slashes, which indicate the nesting
of notions. Taxa are relevant for the teacher precisely because they offer a first structuration of
otherwise scattered knowledge.

Both label and taxon are couples. The second member is slightly more complicated than a list of
line numbers. For a label, it is a list of triples consisting of the start and end of the spanning
lines, and a third member, the path, which identifies unambiguously the start of the span. For a
taxon, it is a **bag**, i.e. a dictionary associating such triples with the count of their
occurrences in the program. The paths being left untouched by the conversion, we will omit them
from now on.

The actual conversion was done because the taxonomy contains the row:

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`operator/arithmetic/addition` | `addition_operator`

This is the simplest case, where both taxon and label patterns are literal (they don't contain
any metacharacter, more on that below).

### 1-0 mapping

- Label: `("binary_operator:Add", [(7, 7)])`.
- Taxon: none.

At first glance, the label `"binary_operator:Add"` may seem redundant with `"addition_operator"`,
and one may wonder why it was generated at all. In fact, the former was used to calculate the
latter.
In [`spec.md`](https://repo/paroxython/resources/spec.md),
the definition of `"addition_operator"` is introduced by these words: “An addition operator is a
binary operator `Add` which has not be classified as a concatenation operator”.

This is a good example of label for internal use only. In the present stage, it is simply ignored
(i.e., it has no entry in the taxonomy).

### 1-N mapping

- Label: `("whole_span:8", [(2, 8)])`.
- Taxa:
    - `("metadata/program", {(2, 8): 1})`.
    - `("metadata/sloc/8", {(2, 8): 1})`.

This is an example of a label which produces two taxa. Although it is not obvious, both have their
uses. The first one is common to all programs, and provides an invariable access key to an
all-encompassing span. The second one has a variable part, and can be used to filter programs by
[size](https://en.wikipedia.org/wiki/Source_lines_of_code) (for example, in
`paroxython.recommend_programs`, the pattern `metadata/sloc/[1-5]` will be used to filter out the
programs that have more than 5 lines).

This conversions are triggered by the following rows in the default taxonomy:

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`metadata/program` | `whole_span:.+`
`metadata/sloc/\1` | `whole_span:(.+)`

Note that, in the replacement pattern, `"\1"` is a
[_backreference_](https://docs.python.org/3/library/re.html#re.sub) to the first captured group
(in parentheses).

### Deduplication

- Labels:
    - `("assignment", [(3, 3), (4, 4), (7, 7)])`.
    - `("single_assignment:result", [(3, 3)])`.
    - `("parallel_assignment", [(4, 4), (7, 7)])`.
    - `("slide", [(7, 7)])`.
- Taxa:
    - `("variable/assignment/single", {(3, 3): 1})`.
    - `("variable/assignment/parallel", {(4, 4): 1})`.
    - `("variable/assignment/parallel/slide", {(7, 7): 1})`.

The example program features three distinct assignments. They can be categorized into:

- A single assignment on line 3  (`result = []`).
- A parallel assignment on line 4 (`(a, b) = (0, 1)`).
- A parallel assignment where a couple is updated by “sliding” the value of its second member to the
first position, on line 7 (`(a, b) = (b, a + b)`).

As you can see, labelling all these produces a lot of span redundancies. For instance, the
assignment of line 7 is labelled three times, as `"assignment"`, `"parallel_assignment"` and
`"slide"`. Since the labels are not structured, this is the best that we can do.

Enter the taxa, whose production is triggered by the following taxonomy rows:

Taxa (replacement patterns)    | Labels (search patterns)
:------------------------------|:-----------------------
`variable/assignment` | `assignment\b.*`
`variable/assignment/parallel` | `parallel_assignment:\d+`
`variable/assignment/parallel/slide` | `slide`
`variable/assignment/single` | `single_assignment:.+`

Initially, the conversion produces as many redundant spans as for the labels:

- Taxa:
    - `("variable/assignment", {(3, 3): 1, (4, 4): 1, (7, 7): 1})`.
    - `("variable/assignment/single", {(3, 3): 1})`.
    - `("variable/assignment/parallel", {(4, 4): 1, (7, 7): 1})`.
    - `("variable/assignment/parallel/slide", {(7, 7): 1})`.

However, because of the tree-like structuring of taxa, it is possible to remove those occurrences
that are subject to further characterization (e.g., `variable/assignment/parallel` on line 7 is
further characterized as `variable/assignment/parallel/slide`), resulting in the list of taxa
given at the start of the section.

Note that the removal of spans has finally led to the elimination of the overly generic taxon
`variable/assignment`.
"""


from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple
from typing import Pattern as RegexPattern
from os.path import commonpath, dirname
from functools import lru_cache

import regex  # type: ignore

from .user_types import (
    LabelName,
    LabelPattern,
    Labels,
    Taxon,
    TaxonName,
    TaxonNames,
    TaxonPattern,
    Taxa,
    TaxaSpans,
)

__pdoc__ = {
    "Taxonomy.__init__": True,
    "Taxonomy": "",
}


class Taxonomy:
    def __init__(
        self,
        taxonomy_path: Optional[Path] = None,
        is_literal: Callable = regex.compile(r"[\w:.]+").fullmatch,
        **kwargs,
    ) -> None:
        r"""Read and pre-process the taxonomy specifications.

        Args:
            taxonomy_path (Optional[Path], optional): The path of a two-columns TSV file
                associating label (search) patterns with taxon (replacement) patterns. For better
                readability, the taxa are listed on the first column, and the corresponding labels
                (sometimes very long) on the second column. If not specified, the
                [default taxonomy](https://repo/paroxython/resources/taxonomy.tsv)
                is used. Defaults to `None`.
            is_literal (Callable, optional): A predicate telling whether a given regular expression
                pattern is literal or not. It will be matched successively against every label
                pattern of the taxonomy TSV file (second column). For instance, the label pattern
                `"external_free_call:print"` is literal, and then matches only itself. Conversely,
                the label pattern `"internal_free_call:[[:upper:]].*"` contains some non-literal
                characters such as `"["` and `"*"`, and then must be compiled into a regular
                expression. By default, a pattern is considered to be literal if it contains only
                letters, digits, underscores, hyphens, colons and **dots**.

                ..note::
                    The latter actually goes against the semantics of regular expressions. In case
                    that's a problem, it is always possible to force the interpretation of a pattern
                    as non-literal by enclosing it in parentheses.

                [Not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)
                Defaults to `regex.compile(r"[\w:.]+").fullmatch`.

        Description:
            1. Read the taxonomy, falling back to the provided default
            [`taxonomy.tsv`](https://repo/paroxython/resources/taxonomy.tsv).
            2. Drop the part starting with the string `"-- EOF"`, if any (this pre-processing
            allows you to leave notes or drafts at the end of the file).
            3. Distribute the remaining rows into two different accumulators, depending on the
            “literality” of the label pattern:
                - `self.literal_labels` is a dictionary associating every **literal** label pattern,
                that it to say, a label name, with a list of taxon names. Most of these lists are
                singletons, but one can imagine that a unique label name could be associated with
                multiple taxon names. As a dictionary, it allows O(1) lookups of any given label
                pattern.
                - `self.compiled_labels` is a list of couples, of which the first member is a
                **compiled** label pattern, and the second member is a replacement pattern which may
                contain backreferences to one or several capture groups of the label pattern. For
                instance, it can include the couple `(regex.compile(r"nested_index:(\d+)$"),
                r"subscript/index/shape/\1")`, which will be used to “translate” any occurrence of
                the label name `"nested_index:3"` into the taxon name `"subscript/index/shape/3"`.
                As an associative list, it only allows O(n) lookups a given label pattern.
        """
        taxonomy_path = taxonomy_path or Path(dirname(__file__)) / "resources" / "taxonomy.tsv"
        tsv = taxonomy_path.read_text().partition("-- EOF")[0].strip()
        self.literal_labels: Dict[LabelName, TaxonNames] = defaultdict(list)
        self.compiled_labels: List[Tuple[RegexPattern, TaxonPattern]] = []
        for line in sorted(tsv.split("\n")[1:]):
            (taxon_value, label_value) = line.strip().split(maxsplit=1)
            (taxon_pattern, label_pattern) = (TaxonPattern(taxon_value), LabelPattern(label_value))
            if is_literal(label_pattern):
                self.literal_labels[LabelName(label_pattern)].append(TaxonName(taxon_pattern))
            else:
                self.compiled_labels.append((regex.compile(f"{label_pattern}$"), taxon_pattern))
                # note: "$" is necessary: regex.fullmatch() has no regex.fullsub() counterpart

    @lru_cache(maxsize=None)
    def get_taxon_name_list(self, label_name: LabelName) -> TaxonNames:
        r"""Translate a label name into a list of taxon names.

        Description:
            Most of the work was done during the initialization, by constructing the map
            `self.literal_labels` and the list `self.compiled_labels`. The given label pattern is
            first looked up in the map, then matched successively against every regular expression
            stored in the list.

            The second step may be useful even if the first one has already produced one or several
            translations. For instance, take a the taxonomy defining the following associations:

            Taxa (replacement patterns)        | Labels (search patterns)
            :----------------------------------|:-----------------------
            `call/function/builtin/casting/\1` | `free_call:(list|dict)`
            `type/sequence/list`               | `free_call:list`

            Suppose now that we pass the label `"free_call:list"`. The lookup in the map produces
            a first translation: `"type/sequence/list"`. However, the linear search in the list
            produces a second translation, namely: `"call/function/builtin/casting/list"`.

            >>> a_taxonomy_instance.get_taxon_name_list("free_call:list")
            [
                "type/sequence/list",
                "call/function/builtin/casting/list",
            ]

            Therefore, the complexity of this function is linear in every case. However, its
            [memoization](https://en.wikipedia.org/wiki/Memoization) avoids having to translate the
            same label more than one time
            (cf. [lru_cache](https://docs.python.org/3/library/functools.html#functools.lru_cache)).
        """
        result: TaxonNames = self.literal_labels.get(label_name, [])
        for (label_regex_pattern, taxon_pattern) in self.compiled_labels:
            if label_regex_pattern.match(label_name):
                result.append(label_regex_pattern.sub(taxon_pattern, label_name))
        return result

    def to_taxa(self, labels: Labels) -> Taxa:
        """Translate a list of labels to a list of taxa.

        Args:
            labels (Labels): A list of labels, each label consisting in a name and a **list** of
                spans.

        Returns:
            Taxa: A sorted list of taxa, each taxon consisting in a name and a **bag** of spans.

        Description:
            This simple method is the sole entry point of the object. It takes a list of labels,
            accumulates their translations into taxa (cf. `Taxonomy.get_taxon_name_list`) and
            returns them deduplicated (cf. `deduplicated_taxa`).
        """
        acc: TaxaSpans = defaultdict(Counter)
        for (label_name, spans) in labels:
            for taxon_name in self.get_taxon_name_list(label_name):
                acc[taxon_name].update(spans)
        taxa = [Taxon(name, spans) for (name, spans) in sorted(acc.items())]
        return deduplicated_taxa(taxa)


def deduplicated_taxa(taxa: Taxa) -> Taxa:
    """Remove from the given taxa those that are counted multiple times as prefixes of another ones.

    Description:
        Consider the following program:
        ```python
        1   while n != 1:
        2       if n % 2 == 0:
        3           n = n // 2
        4       else:
        5           n = 3 * n + 1
        ```
        It features exactly one literal integer on lines 1 and 3, and exactly two on lines 2 and 5.
        Moreover, one of the literals of line 2 is zero. Therefore, the program is originally tagged
        with the following two couples (among others):
        ```python
        [
            ...
            ("type/number/integer/literal",
                {
                    (1, 1): 1,
                    (2, 2): 2,
                    (3, 3): 1,
                    (5, 5): 2,
                }
            ),
            ("type/number/integer/literal/zero", {(2, 2): 1}),
            ...
        ]
        ```
        ..tip::
            In the dictionary above, `(5, 5): 2` means that the taxon `"type/number/integer/literal"`
            has 2 distinct occurrences spanning the lines 5 to 5 (namely, `3` and `1`). Such a
            “counter” dictionary is called a _bag_, or _multiset_.

        Now, every occurrence of a given taxon **is** an occurrence of any of its prefix. For
        instance, an occurrence of the literal integer `0` is obviously an occurrence of a literal
        integer. Currently, it is counted twice. The purpose of this function is to remove such
        redundant counts. The longest taxon will be kept, and its prefix count decreased. Finally,
        the following deduplicated list will be returned:
        ```python
        [
            ...
            ("type/number/integer/literal",
                {
                    (1, 1): 1,
                    (2, 2): 1, # decremented
                    (3, 3): 1,
                    (5, 5): 2,
                }
            ),
            ("type/number/integer/literal/zero", {(2, 2): 1}),
            ...
        ]
        ```
        Decrementing a span count may result in the deletion of a taxon. For instance, on the same
        program:
        ```python
        [
            ...
            ("flow/loop", {(1, 5): 1},
            ("flow/loop/exit/late", {(1, 5): 1},
            ("flow/loop/while", {(1, 5): 1},
            ...
        ]
        ```
        … becomes after deduplication:
        ```python
        [
            ...
            ("flow/loop/exit/late", {(1, 5): 1},
            ("flow/loop/while", {(1, 5): 1},
            ...
        ]
        ```

    Args:
        taxa (Taxa): A list of couples, sorted lexicographically and consisting of a taxon name and
            a bag (multiset) of its spans.

    Returns:
        Taxa: The same list, deduplicated.
    """
    if len(taxa) < 2:
        return taxa
    for (i, (name, spans)) in enumerate(taxa[1:], 1):
        for (previous_name, previous_spans) in reversed(taxa[:i]):
            # Since `"/"` happens to be a separator in both taxa and Unix-paths, `os.commonpath()`
            # comes in handy for extracting the common prefix of two taxa:
            common_prefix = commonpath((name, previous_name))
            if not common_prefix:
                break
            if previous_name == common_prefix:
                difference = spans - previous_spans
                previous_spans.subtract(spans)
                spans = difference
    result = []
    for (name, spans) in taxa:
        spans += Counter()  # suppress items whose count <= 0
        if spans:  # if any item remains in the bag
            result.append(Taxon(name, spans))
    return result


if __name__ == "__main__":
    from .goodies import couple_to_string
    from .label_programs import labelled_programs

    taxonomy = Taxonomy()
    for program in labelled_programs(Path("examples/simple/programs")):
        taxa = taxonomy.to_taxa(program.labels)
        if not taxa:
            continue
        width = min(40, max(len(" ".join(map(str, taxon.spans))) for taxon in taxa))
        for (name, spans) in taxa:
            span_string = " ".join(map(couple_to_string, sorted(set(spans))))
            print(f"{span_string:>{width}}\t{name}")
