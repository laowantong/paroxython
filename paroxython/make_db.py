import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from itertools import chain
from pathlib import Path

import regex

sys.path[0:0] = [str(Path(__file__).parent)]

from program_generator import generate_programs
from label_generators import generate_paths_and_labels
from taxonomy import Taxonomy


def make_database(directories):
    """Construct a JSON object with the following schema:
    {
        "programs": {
            program_1_name: {
                "timestamp": "...",
                "source": "...",
                "labels": {
                    label_1_name: [span_1, span_2, ...],
                    ...
                }
                "taxons: {
                    taxon_1_name: [span_1, span_2, ...],
                }
            },
            ...
        },
        "labels": {
            label_1_name: [program_1_name, program_2_name, ...],
            ...
        },
        "taxons": {
            taxon_1_name: [program_1_name, program_2_name, ...],
            ...
        }
    }
    """
    programs = list(chain.from_iterable(generate_programs(d) for d in directories))
    paths_and_labels = list(generate_paths_and_labels(programs))
    taxonomy = list(Taxonomy()(paths_and_labels))
    db = {
        "programs": get_program_infos(programs),
        "labels": get_label_infos(paths_and_labels),
        "taxons": get_taxon_infos(taxonomy),
    }
    inject_labels(db, paths_and_labels)
    inject_taxons(db, taxonomy)
    return to_Json(db)


def serialize_tags(tags):
    result = {}
    for (tag_name, spans) in tags:
        result[tag_name] = [span.to_couple() for span in sorted(set(spans))]
    return result


def get_program_infos(programs):
    result = {}
    for (path, source) in programs:
        result[str(path)] = {
            "timestamp": str(datetime.fromtimestamp(path.stat().st_mtime)),
            "source": source,
        }
    return result


def get_label_infos(paths_and_labels):
    result = defaultdict(list)
    for (path, labels) in paths_and_labels:
        for label_name in labels:
            result[label_name].append(str(path))
    return result


def get_taxon_infos(taxonomy):
    result = defaultdict(list)
    for (path, taxons) in taxonomy:
        for (taxon_name, _) in taxons:
            result[taxon_name].append(str(path))
    return result


def inject_labels(db, paths_and_labels):
    for (path, labels) in paths_and_labels:
        db["programs"][str(path)]["labels"] = serialize_tags(labels.items())


def inject_taxons(db, taxonomy):
    for (path, taxons) in taxonomy:
        db["programs"][str(path)]["taxons"] = serialize_tags(taxons)


def to_Json(db):
    """Convert the DB into JSON and reduce to one line each list of spans."""
    text = json.dumps(db, indent=2)
    text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
    return text


if __name__ == "__main__":
    directories = [
        "../Python/project_euler",
        # "../Python/maths",
        # "../Algo/programs"
    ]
    db = make_database(directories)
    Path("db.json").write_text(db)
