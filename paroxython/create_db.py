import json
# import pickle
import sys
from collections import Counter, defaultdict
from pathlib import Path

import regex

from scanner import ScannerForDatabase


DIRECTORIES = [
    # "../Python/project_euler",
    # "../Python/maths",
    "../Algo/programs"
]


class Taxonomy:
    def __init__(self, taxonomy_path="taxonomies/default.tsv"):
        is_literal = regex.compile(r"[\w:]+$").match
        tsv = Path(taxonomy_path).read_text()
        self.literal_tag_labels = defaultdict(list)
        self.compiled_tag_labels = []
        for line in tsv.split("\n"):
            line = line.strip()
            if not line or line == "-- EOF":
                break
            (taxon_label, tag_pattern) = line.split("\t")
            if is_literal(tag_pattern):
                self.literal_tag_labels[tag_pattern].append(taxon_label)
            else:
                rex = regex.compile(tag_pattern + "$")
                self.compiled_tag_labels.append((rex, taxon_label))
        self.cache = {}

    def get_taxon_label_list(self, tag_label):
        if tag_label not in self.cache:
            if tag_label in self.literal_tag_labels:
                self.cache[tag_label] = self.literal_tag_labels[tag_label]
            else:
                self.cache[tag_label] = []
                for (rex, taxon_label) in self.compiled_tag_labels:
                    if rex.match(tag_label):
                        self.cache[tag_label].append(rex.sub(taxon_label, tag_label))
        return self.cache[tag_label]

    def to_taxons(self, tags):
        result = defaultdict(Counter)
        for (tag_label, spots) in tags.items():
            for taxon_label in self.get_taxon_label_list(tag_label):
                result[taxon_label].update(Counter(spots))
        return sorted(result.items())

    def deduplicated_taxons(self, taxons):
        previous_label = "dummy"
        for (label, spot_bag) in taxons:
            if label.startswith(previous_label):
                previous_spot_bag.subtract(spot_bag)
            else:
                previous_label = label
                previous_spot_bag = spot_bag
        return [(label, +spot_bag) for (label, spot_bag) in taxons if +spot_bag]

    def frozen_taxons(self, taxons):
        result = {}
        for (label, spot_bag) in taxons:
            result[label] = " ".join(dict.fromkeys((map(str, sorted(spot_bag)))))
        return result

    def inject_classification(self, db):
        db["taxon_paths"] = defaultdict(list)
        for (algo_path, algo_data) in db["algos"].items():
            taxons = self.to_taxons(algo_data["tags"])
            taxons = self.deduplicated_taxons(taxons)
            taxons = self.frozen_taxons(taxons)
            algo_data["tags"] = self.frozen_taxons(algo_data["tags"].items())
            algo_data["taxons"] = taxons
            for taxon in taxons:
                db["taxon_paths"][taxon].append(algo_path)


if __name__ == "__main__":
    # db_path = Path("db.pkl")
    scan = ScannerForDatabase()
    db = {}
    for directory in DIRECTORIES:
        path = Path(directory)
        db.update(scan(path))
    # with open(Path(db_path), mode="wb") as opened_file:
    #     pickle.dump(db, opened_file)
    # with open(db_path, mode="rb") as opened_file:
    #     db = pickle.load(opened_file)
    taxonomy = Taxonomy()
    taxonomy.inject_classification(db)
    output_path = Path("db.json")
    output_path.write_text(json.dumps(db, indent=2))
