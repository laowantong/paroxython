import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Union, Any  # TypedDict (Python 3.8)

import regex  # type: ignore

from declarations import (
    Labels,
    Program,
    PathTaxons,
    Taxons,
    LabelName,
    TaxonName,
    ProgramName,
    ProgramNames,
)
from label_generators import generate_labeled_programs
from taxonomy import Taxonomy

Span = Tuple[int, int]
LabelsSpans = Dict[LabelName, List[Span]]
TaxonsSpans = Dict[TaxonName, List[Span]]

Tags = Union[Taxons, Labels]
TagName = Union[LabelName, TaxonName]
TagsSpans = Dict[TagName, List[Span]]

# class ProgramRecord(TypedDict):
#     timestamp: str
#     source: int
#     labels: LabelsSpans = {}
#     taxons: TaxonsSpans = {}

ProgramRecord = Any  # Workaround before Python 3.8

ProgramInfos = Dict[ProgramName, ProgramRecord]
LabelInfos = Dict[LabelName, List[ProgramName]]
TaxonInfos = Dict[TaxonName, List[ProgramName]]

# class DB(TypedDict):
#     programs: ProgramInfos
#     labels: LabelInfos
#     taxons: TaxonInfos

DB = Any  # Workaround before Python 3.8


def make_database(directories: List[str], *args, **kargs) -> DB:
    """Serialize all infos pertaining to the programs, the labels and the taxons."""
    programs: List[Program] = []
    for directory in directories:
        programs.extend(generate_labeled_programs(directory, *args, **kargs))
    taxonomy = Taxonomy()
    paths_taxons = list(taxonomy(programs))
    db: DB = {
        "programs": get_program_infos(programs),
        "labels": get_label_infos(programs),
        "taxons": get_taxon_infos(paths_taxons),
    }
    inject_labels(db, programs)
    inject_taxons(db, paths_taxons)
    return db


def get_program_infos(programs: List[Program]) -> ProgramInfos:
    result: ProgramInfos = {}
    for program in programs:
        result[ProgramName(str(program.path))] = {
            "timestamp": str(datetime.fromtimestamp(program.path.stat().st_mtime)),
            "source": program.source,
        }
    return result


def get_label_infos(programs: List[Program]) -> LabelInfos:
    result: LabelInfos = defaultdict(list)
    for program in programs:
        for label in program.labels:
            result[label.name].append(ProgramName(str(program.path)))
    return dict(result)


def get_taxon_infos(paths_taxons: List[PathTaxons]) -> TaxonInfos:
    result: TaxonInfos = defaultdict(list)
    for (path, taxons) in paths_taxons:
        for taxon in taxons:
            result[taxon.name].append(ProgramName(str(path)))
    return dict(result)


def serialized(tags: Tags) -> TagsSpans:
    result: TagsSpans = {}
    for (tag_name, spans) in tags:
        result[tag_name] = [span.to_couple() for span in sorted(set(spans))]
    return result


def inject_labels(db: DB, programs: List[Program]) -> None:
    for program in programs:
        db["programs"][ProgramName(str(program.path))]["labels"] = serialized(program.labels)


def inject_taxons(db: DB, paths_taxons: List[PathTaxons]) -> None:
    for (path, taxons) in paths_taxons:
        db["programs"][str(path)]["taxons"] = serialized(taxons)


def to_json(db: DB) -> str:
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
    Path("db.json").write_text(to_json(db))
