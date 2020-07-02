"""
Translate labels into taxa on a list of program paths.
"""

from collections import Counter, defaultdict
from pathlib import Path
from typing import Callable, Dict, Optional
from os.path import commonpath, dirname
from functools import lru_cache

import regex  # type: ignore

from .user_types import (
    LabelName,
    Labels,
    Taxon,
    TaxonName,
    TaxonNames,
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
        """Read the taxonomy specifications, and make some pre-processing."""
        taxonomy_path = taxonomy_path or Path(dirname(__file__)) / "resources" / "taxonomy.tsv"
        tsv = taxonomy_path.read_text().partition("-- EOF")[0].strip()
        self.literal_label_names: Dict[LabelName, TaxonNames] = defaultdict(list)
        self.compiled_label_names = []
        for line in sorted(tsv.split("\n")[1:]):
            (taxon_name, label_pattern) = line.strip().split(maxsplit=1)
            if is_literal(label_pattern):
                self.literal_label_names[LabelName(label_pattern)].append(TaxonName(taxon_name))
            else:
                self.compiled_label_names.append((regex.compile(label_pattern + "$"), taxon_name))
                # note: "$" is necessary: regex.fullmatch() has no regex.fullsub() counterpart

    @lru_cache(maxsize=None)
    def get_taxon_name_list(
        # fmt: off
        self,
        label_name: LabelName,
        sub_slash_sequences: Callable=regex.compile(r"//+").sub,
        # fmt: on
    ) -> TaxonNames:
        """Translate a label name into a list of taxon names.
        """
        result: TaxonNames = []
        if label_name in self.literal_label_names:
            result.extend(self.literal_label_names[label_name])
        for (rex, taxon_name) in self.compiled_label_names:
            if rex.match(label_name):
                s = rex.sub(taxon_name, label_name)  # cf. note above
                s = sub_slash_sequences("/", s)
                result.append(s)
        return result

    def to_taxa(self, labels: Labels) -> Taxa:
        """Translate a list of labels to a list of taxa with their spans in a bag."""
        acc: TaxaSpans = defaultdict(Counter)
        for (label_name, spans) in labels:
            for taxon_name in self.get_taxon_name_list(label_name):
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
        Moreover, one of the literal of line 2 is zero. Therefore, the program is originally tagged
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
            In the dictionary above, `(5, 5): 2` reads: “the taxon `"type/number/integer/literal"`
            has 2 distinct occurrences spanning the lines 5 to 5” (namely, `3` and `1`). Such a
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
