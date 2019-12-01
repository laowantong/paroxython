import json
import sys
from collections import Counter, defaultdict
from datetime import datetime
from itertools import chain
from pathlib import Path

import regex

sys.path[0:0] = [str(Path(__file__).parent)]

from program_generator import generate_programs
from tag_generators import generate_lists_of_tags
from taxonomy import Taxonomy



def serialize_items(items):
    result = {}
    for (label, spots) in items:
        result[label] = [spot.to_couple() for spot in sorted(set(spots))]
    return result


def get_program_infos(programs):
    result = {}
    for (path, source) in programs:
        result[str(path)] = {
            "timestamp": str(datetime.fromtimestamp(path.stat().st_mtime)),
            "source": source,
        }
    return result


def get_tag_infos(paths_and_tags):
    result = defaultdict(list)
    for (path, tags) in paths_and_tags.items():
        for label in tags:
            result[label].append(str(path))
    return result


def get_taxon_infos(taxonomy):
    result = defaultdict(list)
    for (path, taxons) in taxonomy:
        for (label, _) in taxons:
            result[label].append(str(path))
    return result


def inject_tags(db, paths_and_tags):
    for (path, tags) in paths_and_tags.items():
        db["programs"][str(path)]["tags"] = serialize_items(tags.items())


def inject_taxons(db, taxonomy):
    for (path, taxons) in taxonomy:
        db["programs"][str(path)]["taxons"] = serialize_items(taxons)


def to_Json(db):
    """Convert the DB into JSON and reduce to one line each list of spots."""
    text = json.dumps(db, indent=2)
    text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
    return text


def make_database(directories):
    programs = list(chain.from_iterable(generate_programs(d) for d in directories))
    paths_and_tags = dict(generate_lists_of_tags(programs))
    taxonomy = list(Taxonomy()(paths_and_tags))
    db = {
        "programs": get_program_infos(programs),
        "tags": get_tag_infos(paths_and_tags),
        "taxons": get_taxon_infos(taxonomy),
    }
    inject_tags(db, paths_and_tags)
    inject_taxons(db, taxonomy)
    return to_Json(db)


if __name__ == "__main__":
    directories = [
        "../Python/project_euler",
        "../Python/maths",
        "../Algo/programs"
    ]
    Path("db.json").write_text(make_database(directories))
