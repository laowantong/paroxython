import json
from collections import Counter, defaultdict
from pathlib import Path

import regex


class Taxonomy:
    """Translate labels into taxons on a list of program paths."""

    def __init__(self, taxonomy_path="taxonomies/default.tsv"):
        """Read the taxonomy specifications, and make some pre-processing."""
        is_literal = regex.compile(r"[\w:]+$").match
        tsv = Path(taxonomy_path).read_text()
        self.literal_label_names = defaultdict(list)
        self.compiled_label_names = []
        for line in tsv.split("\n"):
            line = line.strip()
            if not line or line == "-- EOF":
                break
            (taxon_name, label_pattern) = line.split("\t")
            if is_literal(label_pattern):
                self.literal_label_names[label_pattern].append(taxon_name)
            else:
                rex = regex.compile(label_pattern + "$")
                self.compiled_label_names.append((rex, taxon_name))

    cache = {}

    def get_taxon_name_list(self, label_name):
        """Translate a label name into a list of taxon names."""
        if label_name not in Taxonomy.cache:
            if label_name in self.literal_label_names:
                Taxonomy.cache[label_name] = self.literal_label_names[label_name]
            else:
                Taxonomy.cache[label_name] = []
                for (rex, taxon_name) in self.compiled_label_names:
                    if rex.match(label_name):
                        Taxonomy.cache[label_name].append(
                            rex.sub(taxon_name, label_name)
                        )
        return Taxonomy.cache[label_name]

    def to_taxons(self, labels):
        """Translate a dict of labels to a list of taxons with their spans in a bag."""
        result = defaultdict(Counter)
        for (label_name, spans) in labels.items():
            for taxon_name in self.get_taxon_name_list(label_name):
                result[taxon_name].update(Counter(spans))
        return sorted(result.items())

    def deduplicated_taxons(self, taxons):
        """For taxons t2 having a taxon t1 as a prefix, remove the common spans in t1."""
        previous_name = "dummy"
        for (name, span_bag) in taxons:
            if name.startswith(previous_name):
                previous_span_bag.subtract(span_bag)
            else:
                previous_name = name
                previous_span_bag = span_bag
        result = []
        for (name, span_bag) in taxons:
            cleaned_bag = +span_bag  # suppress items whose count == 0
            if cleaned_bag:  # if any item remains in the bag
                result.append((name, cleaned_bag))
        return result

    def __call__(self, paths_and_labels):
        """Translate labels into taxons on a list of program paths.

        Input: an iterator on label lists:

            (path_1, [
                (label_name_1, label_spans_1),
                (label_name_2, label_spans_2),
                ...
            ]), ...

        Output: an iterator of (program_path, taxons with their span bag)

                (program_1_path, [(taxon_1: span_bag_1), (taxon_2: span_bag_2), ...]),
                (program_2_path, [(taxon_1: span_bag_1), (taxon_2: span_bag_2), ...]),
                ...

            where each span bag is a collections.Counter of spans:

                {
                    span_1: count_1,
                    span_2: count_2,
                    ...
                }
        """
        for (program_path, labels) in paths_and_labels:
            taxons = self.to_taxons(labels)
            taxons = self.deduplicated_taxons(taxons)
            yield (program_path, taxons)


if __name__ == "__main__":
    generate_programs = __import__("program_generator").generate_programs
    generate_paths_and_labels = __import__("label_generators").generate_paths_and_labels
    chain = __import__("itertools").chain
    DIRECTORIES = [
        "../Python/project_euler",
        # "../Python/maths",
        # "../Algo/programs"
    ]
    paths_and_labels = chain.from_iterable(
        generate_paths_and_labels(generate_programs(directory))
        for directory in DIRECTORIES
    )
    taxonomy = Taxonomy()
    taxon_dict = {}
    for (program_path, taxons) in taxonomy(paths_and_labels):
        for (i, (name, spans)) in enumerate(taxons):
            taxons[i] = (name, " ".join(map(str, sorted(set(spans)))))
        taxon_dict[str(program_path)] = dict(taxons)
    output_path = Path("snapshots/taxon_db.json")
    output_path.write_text(json.dumps(taxon_dict, indent=2))
