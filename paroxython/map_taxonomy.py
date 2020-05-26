from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Optional
from os.path import commonpath, dirname
from functools import lru_cache

import regex  # type: ignore

from .user_types import (
    LabelName,
    Labels,
    Taxon,
    TaxonName,
    TaxonNames,
    Taxons,
    TaxonsSpans,
)

_sub_slash_sequences = regex.compile(r"//+").sub


class Taxonomy:
    """Translate labels into taxons on a list of program paths."""

    def __init__(self, taxonomy_path: Optional[Path] = None, *args, **kwargs) -> None:
        """Read the taxonomy specifications, and make some pre-processing."""
        is_literal = regex.compile(r"[\w:.]+").fullmatch
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

    cache: Dict[LabelName, TaxonNames] = {}

    @lru_cache(maxsize=None)
    def get_taxon_name_list(self, label_name: LabelName) -> TaxonNames:
        """Translate a label name into a list of taxon names."""
        result: TaxonNames = []
        if label_name in self.literal_label_names:
            result.extend(self.literal_label_names[label_name])
        for (rex, taxon_name) in self.compiled_label_names:
            if rex.match(label_name):
                s = rex.sub(taxon_name, label_name)  # cf. note above
                s = _sub_slash_sequences("/", s)
                result.append(s)
        return result

    def to_taxons(self, labels: Labels) -> Taxons:
        """Translate a list of labels to a list of taxons with their spans in a bag."""
        acc: TaxonsSpans = defaultdict(Counter)
        for (label_name, spans) in labels:
            for taxon_name in self.get_taxon_name_list(label_name):
                acc[taxon_name].update(spans)
        taxons = [Taxon(name, spans) for (name, spans) in sorted(acc.items())]
        return self.deduplicated_taxons(taxons)

    @staticmethod
    def deduplicated_taxons(taxons: Taxons) -> Taxons:
        """If taxon t2 has taxon t1 as a prefix, remove their common spans from t1."""
        if len(taxons) == 0:
            return []
        for (i, (name, spans)) in enumerate(taxons[1:], 1):
            for j in range(i - 1, -1, -1):
                (previous_name, previous_spans) = taxons[j]
                common_prefix = commonpath((name, previous_name))
                if not common_prefix:
                    break
                if previous_name == common_prefix:
                    difference = spans - previous_spans
                    previous_spans.subtract(spans)
                    spans = difference
        result = []
        for (name, spans) in taxons:
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
        taxons = taxonomy.to_taxons(program.labels)
        if not taxons:
            continue
        width = min(40, max(len(" ".join(map(str, taxon.spans))) for taxon in taxons))
        for (name, spans) in taxons:
            span_string = " ".join(map(couple_to_string, sorted(set(spans))))
            print(f"{span_string:>{width}}\t{name}")
