import json
from collections import Counter, defaultdict
from pathlib import Path

import regex


class Taxonomy:
    """Make a taxonomy from a list of maps associating program paths with tags."""

    def __init__(self, taxonomy_path="taxonomies/default.tsv"):
        """Read the taxonomy specifications, and make some pre-processing."""
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

    cache = {}

    def get_taxon_label_list(self, tag_label):
        """Translate a tag label into a list of taxon labels."""
        if tag_label not in Taxonomy.cache:
            if tag_label in self.literal_tag_labels:
                Taxonomy.cache[tag_label] = self.literal_tag_labels[tag_label]
            else:
                Taxonomy.cache[tag_label] = []
                for (rex, taxon_label) in self.compiled_tag_labels:
                    if rex.match(tag_label):
                        Taxonomy.cache[tag_label].append(
                            rex.sub(taxon_label, tag_label)
                        )
        return Taxonomy.cache[tag_label]

    def to_taxons(self, tags):
        """Translate a dict of tags to a list of taxons with their spots in a bag."""
        result = defaultdict(Counter)
        for (tag_label, spots) in tags.items():
            for taxon_label in self.get_taxon_label_list(tag_label):
                result[taxon_label].update(Counter(spots))
        return sorted(result.items())

    def deduplicated_taxons(self, taxons):
        """For taxons t2 having a taxon t1 as a prefix, remove the common spots in t1."""
        previous_label = "dummy"
        for (label, spot_bag) in taxons:
            if label.startswith(previous_label):
                previous_spot_bag.subtract(spot_bag)
            else:
                previous_label = label
                previous_spot_bag = spot_bag
        result = []
        for (label, spot_bag) in taxons:
            cleaned_bag = +spot_bag  # suppress items whose count == 0
            if cleaned_bag:  # if there remains any item
                result.append((label, cleaned_bag))
        return result

    def __call__(self, tag_dict):
        """Translate a map of lists of tags into a list of lists of taxons."""
        for (program_path, tags) in tag_dict.items():
            taxons = self.to_taxons(tags)
            taxons = self.deduplicated_taxons(taxons)
            yield (program_path, taxons)


if __name__ == "__main__":
    generate_programs = __import__("program_generator").generate_programs
    generate_lists_of_tags = __import__("tag_generators").generate_lists_of_tags
    tag_dict = {}
    DIRECTORIES = [
        "../Python/project_euler",
        # "../Python/maths",
        # "../Algo/programs"
    ]
    for directory in DIRECTORIES:
        programs = generate_programs(directory)
        tag_dict.update(generate_lists_of_tags(programs))
    taxonomy = Taxonomy()
    taxon_dict = {}
    for (program_path, taxons) in taxonomy(tag_dict):
        for (i, (label, spots)) in enumerate(taxons):
            taxons[i] = (label, " ".join(map(str, sorted(set(spots)))))
        taxon_dict[str(program_path)] = dict(taxons)
    output_path = Path("taxon_db.json")
    output_path.write_text(json.dumps(taxon_dict, indent=2))
