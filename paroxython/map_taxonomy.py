"""
Translate labels into taxa on a list of program paths.
"""

from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple
from typing import Pattern as RegexPattern
from os.path import commonpath, dirname
from functools import lru_cache

import regex  # type: ignore

from .user_types import (
    LabelPattern,
    Labels,
    Taxon,
    TaxonName,
    TaxonNames,
    TaxonPattern,
    TaxonPatterns,
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
        *args,
        **kwargs,
    ) -> None:
        r"""Read and pre-process the taxonomy specifications.

        Description:
            1. Read the taxonomy, falling back to the provided default
            [`taxonomy.tsv`](https://github.com/laowantong/paroxython/blob/master/paroxython/resources/taxonomy.tsv).
            2. Drop the part starting with the string `"-- EOF"`, if any (this pre-processing
            allows you to leave notes or drafts at the end of the file).
            3.

        Args:
            taxonomy_path (Optional[Path], optional): The path of a two-columns TSV file
                associating label (search) patterns with taxon (replacement) patterns. For better
                readability, the taxa are listed on the first column, and the corresponding labels
                (sometimes very long) on the second column. If not specified, the
                [default taxonomy](https://github.com/laowantong/paroxython/blob/master/paroxython/resources/taxonomy.tsv)
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

                Defaults to `regex.compile(r"[\w:.]+").fullmatch`.
        """
        taxonomy_path = taxonomy_path or Path(dirname(__file__)) / "resources" / "taxonomy.tsv"
        tsv = taxonomy_path.read_text().partition("-- EOF")[0].strip()
        self.literal_labels: Dict[LabelPattern, TaxonNames] = defaultdict(list)
        self.compiled_labels: List[Tuple[RegexPattern, TaxonPattern]] = []
        for line in sorted(tsv.split("\n")[1:]):
            (taxon_value, label_value) = line.strip().split(maxsplit=1)
            (taxon_pattern, label_pattern) = (TaxonPattern(taxon_value), LabelPattern(label_value))
            if is_literal(label_pattern):
                self.literal_labels[label_pattern].append(TaxonName(taxon_pattern))
            else:
                self.compiled_labels.append((regex.compile(f"{label_pattern}$"), taxon_pattern))
                # note: "$" is necessary: regex.fullmatch() has no regex.fullsub() counterpart

    @lru_cache(maxsize=None)
    def get_taxon_name_list(self, label_pattern: LabelPattern) -> TaxonNames:
        """Translate a label pattern into a list of taxon names."""
        result: TaxonNames = self.literal_labels.get(label_pattern, [])
        for (rex, taxon_pattern) in self.compiled_labels:
            if rex.match(label_pattern):
                result.append(rex.sub(taxon_pattern, label_pattern))
        return result

    def to_taxa(self, labels: Labels) -> Taxa:
        """Translate a list of labels to a list of taxa with their spans in a bag."""
        acc: TaxaSpans = defaultdict(Counter)
        for (label_pattern, spans) in labels:
            for taxon_name in self.get_taxon_name_list(label_pattern):
                acc[taxon_name].update(spans)
        taxa = [Taxon(name, spans) for (name, spans) in sorted(acc.items())]
        return deduplicated_taxa(taxa)


def deduplicated_taxa(taxa: Taxa) -> Taxa:
    """Remove from the given taxa those that are counted multiple times as prefixes of another ones.

    Description:
        Consider the following program (line numbers added for clarity):
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
    from .label_programs import ProgramLabeller

    labeller = ProgramLabeller()
    labeller.label_programs(Path("examples/simple/programs"))
    taxonomy = Taxonomy()
    for program in labeller.programs:
        taxa = taxonomy.to_taxa(program.labels)
        if not taxa:
            continue
        width = min(40, max(len(" ".join(map(str, taxon.spans))) for taxon in taxa))
        for (name, spans) in taxa:
            span_string = " ".join(map(couple_to_string, sorted(set(spans))))
            print(f"{span_string:>{width}}\t{name}")
