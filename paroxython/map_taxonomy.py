from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List
from os.path import commonpath

import regex  # type: ignore

from goodies import iterate_and_print_programs
from user_types import (
    LabelName,
    Labels,
    Program,
    ProgramTaxons,
    Taxon,
    TaxonName,
    TaxonNames,
    Taxons,
    TaxonsSpans,
)

sub_slash_sequences = regex.compile(r"//+").sub
DEFAULT_TAXONOMY_PATH = Path("taxonomies/default_taxonomy.tsv")


class Taxonomy:
    """Translate labels into taxons on a list of program paths."""

    def __init__(self, taxonomy_path: Path = DEFAULT_TAXONOMY_PATH) -> None:
        """Read the taxonomy specifications, and make some pre-processing."""
        is_literal = regex.compile(r"[\w:]+").fullmatch
        tsv = taxonomy_path.read_text().partition("-- EOF")[0].strip()
        self.literal_label_names: Dict[LabelName, TaxonNames] = defaultdict(list)
        self.compiled_label_names = []
        for line in sorted(tsv.split("\n")):
            (taxon_name, label_pattern) = line.strip().split(maxsplit=1)
            if is_literal(label_pattern):
                self.literal_label_names[LabelName(label_pattern)].append(TaxonName(taxon_name))
            else:
                self.compiled_label_names.append((regex.compile(label_pattern + "$"), taxon_name))
                # note: "$" is necessary: regex.fullmatch() has no regex.fullsub() counterpart

    cache: Dict[LabelName, TaxonNames] = {}

    def get_taxon_name_list(self, label_name: LabelName) -> TaxonNames:
        """Translate a label name into a list of taxon names."""
        cache = Taxonomy.cache
        if label_name not in cache:
            if label_name in self.literal_label_names:
                cache[label_name] = self.literal_label_names[label_name]
            else:
                cache[label_name] = []
                for (rex, taxon_name) in self.compiled_label_names:
                    if rex.match(label_name):
                        s = rex.sub(taxon_name, label_name)  # cf. note above
                        s = sub_slash_sequences("/", s)
                        cache[label_name].append(s)
        return cache[label_name]

    def to_taxons(self, labels: Labels) -> Taxons:
        """Translate a list of labels to a list of taxons with their spans in a bag."""
        result: TaxonsSpans = defaultdict(Counter)
        for (label_name, spans) in labels:
            for taxon_name in self.get_taxon_name_list(label_name):
                result[taxon_name].update(spans)
        return [Taxon(name, spans) for (name, spans) in sorted(result.items())]

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

    def __call__(self, programs: List[Program]) -> ProgramTaxons:
        """Translate labels into taxons on a list of program names."""
        result: ProgramTaxons = {}
        print(f"Mapping labels of {len(programs)} programs onto taxonomy.")
        for program in iterate_and_print_programs(programs):
            result[program.name] = self.deduplicated_taxons(self.to_taxons(program.labels))
        return result


if __name__ == "__main__":
    list_labelled_programs = __import__("label_programs").list_labelled_programs
    chain = __import__("itertools").chain
    taxonomy = Taxonomy()
    programs = list_labelled_programs(Path("../Python/project_euler"))
    for (_, taxons) in taxonomy(programs).items():
        if not taxons:
            continue
        width = min(40, max(len(" ".join(map(str, taxon.spans))) for taxon in taxons))
        for (name, spans) in taxons:
            span_string = " ".join(map(str, sorted(set(spans))))
            print(f"{span_string:>{width}}\t{name}")
