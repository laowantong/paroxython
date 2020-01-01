import json
from collections import defaultdict
from datetime import datetime
from itertools import chain
from pathlib import Path
from typing import Dict, List, Tuple, Union

import regex  # type: ignore

from declarations import Labels, PathLabels, PathTaxons, Programs, Taxons
from label_generators import generate_programs_labels
from program_generator import generate_programs
from taxonomy import Taxonomy


def make_database(directories: List[str]) -> str:
    """Construct a JSON object with the following schema:
    {
        "programs": {
            prg1_name: {
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
            label_1_name: [prg1_name, prg2_name, ...],
            ...
        },
        "taxons": {
            taxon_1_name: [prg1_name, prg2_name, ...],
            ...
        }
    }
    """
    programs = list(chain.from_iterable(generate_programs(d) for d in directories))
    programs_labels = list(generate_programs_labels(programs))
    taxonomy = Taxonomy()
    paths_taxons = list(taxonomy(programs_labels))
    db = {
        "programs": get_program_infos(programs),
        "labels": get_label_infos(programs_labels),
        "taxons": get_taxon_infos(paths_taxons),
    }
    inject_labels(db, programs_labels)
    inject_taxons(db, paths_taxons)
    return to_Json(db)


def serialized(tags: Union[Taxons, Labels]) -> Dict[str, List[Tuple[int, int]]]:
    result: Dict[str, List[Tuple[int, int]]] = {}
    for (tag_name, spans) in tags:
        result[tag_name] = [span.to_couple() for span in sorted(set(spans))]
    return result


def get_program_infos(programs: Programs) -> Dict[str, Dict[str, str]]:
    result = {}
    for (path, source) in programs:
        result[str(path)] = {
            "timestamp": str(datetime.fromtimestamp(path.stat().st_mtime)),
            "source": source,
        }
    return result


def get_label_infos(programs_labels: List[PathLabels]) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = defaultdict(list)
    for (path, labels) in programs_labels:
        for label in labels:
            result[label.name].append(str(path))
    return dict(result)


def get_taxon_infos(paths_taxons: List[PathTaxons]) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = defaultdict(list)
    for (path, taxons) in paths_taxons:
        for taxon in taxons:
            result[taxon.name].append(str(path))
    return dict(result)


def inject_labels(db: Dict, programs_labels: List[PathLabels]) -> None:
    for (path, labels) in programs_labels:
        db["programs"][str(path)]["labels"] = serialized(labels)


def inject_taxons(db: Dict, paths_taxons: List[PathTaxons]) -> None:
    for (path, taxons) in paths_taxons:
        db["programs"][str(path)]["taxons"] = serialized(taxons)


def to_Json(db: Dict) -> str:
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
