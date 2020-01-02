import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Union

import regex  # type: ignore

from declarations import Labels, Program, PathTaxons, Taxons
from label_generators import generate_labeled_programs
from taxonomy import Taxonomy


def make_database(directories: List[str], *args, **kargs) -> str:
    """Construct a JSON object with the following schema:
    {
        "programs": {
            prg1_path: {
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
            label_1_name: [prg1_path, prg2_path, ...],
            ...
        },
        "taxons": {
            taxon_1_name: [prg1_path, prg2_path, ...],
            ...
        }
    }
    """
    programs: List[Program] = []
    for directory in directories:
        programs.extend(generate_labeled_programs(directory, *args, **kargs))
    taxonomy = Taxonomy()
    paths_taxons = list(taxonomy(programs))
    db = {
        "programs": get_program_infos(programs),
        "labels": get_label_infos(programs),
        "taxons": get_taxon_infos(paths_taxons),
    }
    inject_labels(db, programs)
    inject_taxons(db, paths_taxons)
    return to_Json(db)


def serialized(tags: Union[Taxons, Labels]) -> Dict[str, List[Tuple[int, int]]]:
    result: Dict[str, List[Tuple[int, int]]] = {}
    for (tag_name, spans) in tags:
        result[tag_name] = [span.to_couple() for span in sorted(set(spans))]
    return result


def get_program_infos(programs: List[Program]) -> Dict[str, Dict[str, str]]:
    result = {}
    for program in programs:
        result[str(program.path)] = {
            "timestamp": str(datetime.fromtimestamp(program.path.stat().st_mtime)),
            "source": program.source,
        }
    return result


def get_label_infos(programs: List[Program]) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = defaultdict(list)
    for program in programs:
        for label in program.labels:
            result[label.name].append(str(program.path))
    return dict(result)


def get_taxon_infos(paths_taxons: List[PathTaxons]) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = defaultdict(list)
    for (path, taxons) in paths_taxons:
        for taxon in taxons:
            result[taxon.name].append(str(path))
    return dict(result)


def inject_labels(db: Dict, programs: List[Program]) -> None:
    for program in programs:
        db["programs"][str(program.path)]["labels"] = serialized(program.labels)


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
