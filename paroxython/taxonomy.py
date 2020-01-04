import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterator, List

import regex  # type: ignore

from declarations import (
    LabelName,
    Labels,
    Program,
    PathTaxons,
    Taxon,
    TaxonName,
    TaxonNames,
    Taxons,
    TaxonsSpans,
)


class Taxonomy:
    """Translate labels into taxons on a list of program paths."""

    def __init__(self, taxonomy_path: str = "taxonomies/default_taxonomy.tsv") -> None:
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
                self.compiled_label_names.append((regex.compile(label_pattern), taxon_name))

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
                    if rex.fullmatch(label_name):
                        cache[label_name].append(rex.sub(taxon_name, label_name))
        return cache[label_name]

    def to_taxons(self, labels: Labels) -> Taxons:
        """Translate a list of labels to a list of taxons with their spans in a bag."""
        result: TaxonsSpans = defaultdict(Counter)
        for (label_name, spans) in labels:
            for taxon_name in self.get_taxon_name_list(label_name):
                result[taxon_name].update(spans)
        return [Taxon(name, spans) for (name, spans) in sorted(result.items())]

    def deduplicated_taxons(self, taxons: Taxons) -> Taxons:
        """If taxon t2 has taxon t1 as a prefix, remove their common spans from t1."""
        if len(taxons) == 0:
            return []
        (previous_name, previous_spans) = taxons[0]
        for (name, spans) in taxons[1:]:
            if name.startswith(previous_name):
                previous_spans.subtract(spans)
            else:
                previous_name = name
                previous_spans = spans
        result = []
        for (name, spans) in taxons:
            spans = +spans  # Counter's special syntax: suppress items whose count == 0
            if spans:  # if any item remains in the bag
                result.append(Taxon(name, spans))
        return result

    def __call__(self, programs: List[Program]) -> Iterator[PathTaxons]:
        """Translate labels into taxons on a list of program paths."""
        for program in programs:
            taxons = self.to_taxons(program.labels)
            taxons = self.deduplicated_taxons(taxons)
            yield PathTaxons(program.path, taxons)


if __name__ == "__main__":
    generate_labeled_programs = __import__("label_generators").generate_labeled_programs
    chain = __import__("itertools").chain
    DIRECTORIES = [
        "../Python/project_euler",
        # "../Python/maths",
        # "../Algo/programs"
    ]
    programs = chain.from_iterable(
        generate_labeled_programs(directory) for directory in DIRECTORIES
    )
    taxonomy = Taxonomy()
    acc: Dict[str, Dict[str, str]] = {}
    for (path, taxons) in taxonomy(programs):
        acc[str(path)] = {name: " ".join(map(str, sorted(set(spans)))) for (name, spans) in taxons}
    output_path = Path("snapshots/taxon_db.json")
    output_path.write_text(json.dumps(acc, indent=2))
