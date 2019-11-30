import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

import regex

sys.path[0:0] = [str(Path(__file__).parent)]

from program_generator import generate_programs
from tag_generators import generate_lists_of_tags
from taxonomy import Taxonomy
from datetime import datetime

DIRECTORIES = [
    # "../Python/project_euler",
    # "../Python/maths",
    "../Algo/programs"
]

result = {"programs": {}, "tags": defaultdict(list), "taxons": defaultdict(list)}


def serialize_items(items):
    result = {}
    for (label, spots) in items:
        result[label] = [spot.to_couple() for spot in sorted(set(spots))]
    return result


def update_with_items(dictionary, items, path):
    for (label, _) in items:
        dictionary[label].append(str(path))


tag_dict = {}
for directory in DIRECTORIES:
    programs = list(generate_programs(directory))
    for (path, source) in programs:
        result["programs"][str(path)] = {
            "timestamp": str(datetime.fromtimestamp(path.stat().st_mtime)),
            "source": source,
        }
    for (path, tags) in generate_lists_of_tags(programs):
        tag_dict[path] = tags
        result["programs"][str(path)]["tags"] = serialize_items(tags.items())
        update_with_items(result["tags"], tags.items(), path)

taxonomy = Taxonomy()
for (path, taxons) in taxonomy(tag_dict):
    result["programs"][str(path)]["taxons"] = serialize_items(taxons)
    update_with_items(result["taxons"], taxons, path)

text = json.dumps(result, indent=2)
text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
Path("db.json").write_text(text)
