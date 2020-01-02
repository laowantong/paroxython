import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterator, List

import regex  # type: ignore

from declarations import (
    LabelName,
    Labels,
    PathLabels,
    PathTaxons,
    Taxon,
    TaxonName,
    TaxonNames,
    Taxons,
    TaxonsSpans,
)


class Taxonomy:
    """Translate labels into taxons on a list of program paths."""

    def __init__(self, taxonomy_path: str = "taxonomies/default.tsv") -> None:
        """Read the taxonomy specifications, and make some pre-processing."""
        is_literal = regex.compile(r"[\w:]+$").match
        tsv = Path(taxonomy_path).read_text()
        self.literal_label_names: Dict[LabelName, TaxonNames] = defaultdict(list)
        self.compiled_label_names = []
        for line in tsv.split("\n"):
            line = line.strip()
            if not line or line == "-- EOF":
                break
            (taxon_name, label_pattern) = line.split("\t")
            if is_literal(label_pattern):
                self.literal_label_names[LabelName(label_pattern)].append(TaxonName(taxon_name))
            else:
                rex = regex.compile(label_pattern + "$")
                self.compiled_label_names.append((rex, taxon_name))

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
                        cache[label_name].append(rex.sub(taxon_name, label_name))
        return cache[label_name]

    def to_taxons(self, labels: Labels) -> Taxons:
        """Translate a list of labels to a list of taxons with their spans in a bag."""
        result: TaxonsSpans = defaultdict(Counter)
        for (label_name, spans) in labels:
            for taxon_name in self.get_taxon_name_list(label_name):
                result[taxon_name].update(Counter(spans))
        return [Taxon(name, span_bag) for (name, span_bag) in sorted(result.items())]

    def deduplicated_taxons(self, taxons: Taxons) -> Taxons:
        """If taxon t2 has taxon t1 as a prefix, remove their common spans from t1."""
        if len(taxons) == 0:
            return []
        (previous_name, previous_span_bag) = taxons[0]
        for (name, span_bag) in taxons[1:]:
            if name.startswith(previous_name):
                previous_span_bag.subtract(span_bag)
            else:
                previous_name = name
                previous_span_bag = span_bag
        result = []
        for (name, span_bag) in taxons:
            cleaned_bag = +span_bag  # suppress items whose count == 0
            if cleaned_bag:  # if any item remains in the bag
                result.append(Taxon(name, cleaned_bag))
        return result

    def __call__(self, programs_labels: List[PathLabels]) -> Iterator[PathTaxons]:
        """Translate labels into taxons on a list of program paths."""
        for (path, labels) in programs_labels:
            taxons = self.to_taxons(labels)
            taxons = self.deduplicated_taxons(taxons)
            yield PathTaxons(path, taxons)


if __name__ == "__main__":
    generate_programs = __import__("program_generator").generate_programs
    generate_programs_labels = __import__("label_generators").generate_programs_labels
    chain = __import__("itertools").chain
    DIRECTORIES = [
        "../Python/project_euler",
        # "../Python/maths",
        # "../Algo/programs"
    ]
    programs_labels = chain.from_iterable(
        generate_programs_labels(generate_programs(directory)) for directory in DIRECTORIES
    )
    taxonomy = Taxonomy()
    acc: Dict[str, Dict[str, str]] = {}
    for (path, taxons) in taxonomy(programs_labels):
        acc[str(path)] = {name: " ".join(map(str, sorted(set(spans)))) for (name, spans) in taxons}
    output_path = Path("snapshots/taxon_db.json")
    output_path.write_text(json.dumps(acc, indent=2))
