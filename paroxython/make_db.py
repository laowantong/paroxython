import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple, overload

import regex  # type: ignore
from typing_extensions import TypedDict  # from Python 3.8, import directly from typing

from user_types import (
    LabelName,
    Labels,
    PathTaxons,
    Program,
    ProgramName,
    Source,
    TaxonName,
    Taxons,
)
from generate_labels import generate_labelled_programs
from map_taxonomy import Taxonomy

Span = Tuple[int, int]
LabelsSpans = Dict[LabelName, List[Span]]
TaxonsSpans = Dict[TaxonName, List[Span]]


class ProgramRecord(TypedDict):
    timestamp: str
    source: Source
    labels: LabelsSpans
    taxons: TaxonsSpans


ProgramInfos = Dict[ProgramName, ProgramRecord]
LabelInfos = Dict[LabelName, List[ProgramName]]
TaxonInfos = Dict[TaxonName, List[ProgramName]]


class Database:
    def __init__(self, directories: List[str], *args, **kargs) -> None:
        """collect all infos pertaining to the programs, the labels and the taxons."""
        programs: List[Program] = []
        for directory in directories:
            programs.extend(generate_labelled_programs(directory, *args, **kargs))

        taxonomy = Taxonomy()
        paths_taxons = list(taxonomy(programs))

        self.programs: ProgramInfos = {}
        for program in programs:
            self.programs[ProgramName(str(program.path))] = {
                "timestamp": str(datetime.fromtimestamp(program.path.stat().st_mtime)),
                "source": program.source,
                "labels": {},  # to be populated by inject_labels()
                "taxons": {},  # to be populated by inject_taxons()
            }

        self.labels: LabelInfos = defaultdict(list)
        for program in programs:
            for label in program.labels:
                self.labels[label.name].append(ProgramName(str(program.path)))
        for program in programs:
            self.programs[ProgramName(str(program.path))]["labels"] = prepared(program.labels)

        self.taxons: TaxonInfos = defaultdict(list)
        for (path, taxons) in paths_taxons:
            for taxon in taxons:
                self.taxons[taxon.name].append(ProgramName(str(path)))
        for (path, taxons) in paths_taxons:
            self.programs[ProgramName(str(path))]["taxons"] = prepared(taxons)

    def write_json(self, path: str) -> None:
        """Dump the data to JSON, reduce each list of spans to one line, write it."""
        data = {
            "programs": self.programs,
            "labels": self.labels,
            "taxons": self.taxons,
        }
        text = json.dumps(data, indent=2)
        text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
        Path(path).write_text(text)


# fmt: off
@overload
def prepared(tags: Labels) -> LabelsSpans:
    ...  # pragma: no cover
@overload
def prepared(tags: Taxons) -> TaxonsSpans:
    ...  # pragma: no cover
def prepared(tags):
    """Prepare the spans for serialization."""
    result: Any = {}
    for (tag_name, spans) in tags:
        result[tag_name] = [span.to_couple() for span in sorted(set(spans))]
    return result
# fmt: on


if __name__ == "__main__":
    directories = [
        "../Python/project_euler",
        # "../Python/maths",
        # "../Algo/programs"
    ]
    database = Database(directories)
    database.write_json("db.json")
