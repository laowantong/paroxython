import json
import sqlite3
from collections import defaultdict
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import List, Optional, Tuple, Union, overload, Dict

import regex  # type: ignore

from .goodies import add_line_numbers
from .label_programs import ProgramLabeller, iterate_and_print_programs
from .map_taxonomy import Taxonomy
from .user_types import (
    LabelInfos,
    Labels,
    LabelsPoorSpans,
    ProgramInfos,
    ProgramName,
    ProgramNameSet,
    Programs,
    ProgramToPrograms,
    TaxonInfos,
    Taxons,
    TaxonsPoorSpans,
)


class Database:
    def __init__(self, directory: Path, ignore_timestamps=True, *args, **kwargs) -> None:
        """Collect all infos pertaining to the programs, the labels and the taxons."""

        self.default_json_db_path = directory.parent / f"{directory.name}_db.json"
        self.default_sqlite_db_path = directory.parent / f"{directory.name}_db.sqlite"

        labeller = ProgramLabeller()
        labeller.label_programs(directory, *args, **kwargs)
        programs: Programs = labeller.programs
        self.labels = collect_labels(programs)

        taxonomy = Taxonomy(*args, **kwargs)
        map_labels_on_taxons(programs, taxonomy)
        self.taxons = collect_taxons(programs)

        importations = compute_direct_importations(programs)
        self.importations = complete_and_collect_importations(importations)

        exportations = compute_exportations(programs, self.importations)
        self.exportations = collect_exportations(exportations)

        get_timestamp = lambda path: str(datetime.fromtimestamp(path.stat().st_mtime))
        if ignore_timestamps:
            get_timestamp = lambda path: "ignored"

        self.programs_infos: ProgramInfos = {}
        for program in programs:
            self.programs_infos[program.name] = {
                "timestamp": get_timestamp(directory / program.name),
                "source": program.source,
                "labels": prepared(program.labels),
                "taxons": prepared(program.taxons),
            }

    def get_json(self) -> str:
        """Dump the data to JSON, reduce each list of spans to one line."""
        data = {
            "programs": self.programs_infos,
            "labels": dict(sorted(self.labels.items())),
            "taxons": dict(sorted(self.taxons.items())),
            "importations": dict(self.importations.items()),
            "exportations": dict(self.exportations.items()),
        }
        text = json.dumps(data, indent=2) + "\n"
        text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
        return text

    def write_json(self, db_path: Optional[Path] = None) -> None:
        db_path = db_path or self.default_json_db_path
        print(f"Writing {db_path}.")
        db_path.write_text(self.get_json())

    def write_sqlite(self, db_path: Optional[Path] = None) -> None:
        db_path = db_path or self.default_sqlite_db_path
        print(f"Writing {db_path}.")
        program_rows: List[Tuple] = []
        label_rows: List[Tuple] = []
        taxon_rows: List[Tuple] = []
        for (path, info) in self.programs_infos.items():
            source = f"{path}\n\n" + add_line_numbers(info["source"])
            program_rows.append((path, info["timestamp"], source))
            for (label_name, spans) in info["labels"].items():
                (prefix, _, suffix) = label_name.partition(":")
                for span in spans:
                    label_rows.append(
                        (
                            label_name,
                            prefix,
                            suffix,
                            "-".join(map(str, span)) if span[0] != span[1] else str(span[0]),
                            span[0],
                            span[1],
                            path,
                        )
                    )
            for (taxon_name, spans) in info["taxons"].items():
                for span in spans:
                    taxon_rows.append(
                        (
                            taxon_name,
                            "-".join(map(str, span)) if span[0] != span[1] else str(span[0]),
                            span[0],
                            span[1],
                            path,
                        )
                    )

        if db_path.exists():  # Python 3.8: use missing_ok=True parameter
            db_path.unlink()
        connexion = sqlite3.connect(str(db_path))  # str() for Python 3.6 compatibility
        c = connexion.cursor()

        program_columns = (
            "program TEXT PRIMARY KEY",
            "timestamp TEXT",
            "source TEXT",
        )
        c.execute(f"CREATE TABLE program ({','.join(program_columns)})")
        c.executemany(
            f"INSERT INTO program VALUES ({','.join('?' * len(program_columns))})", program_rows,
        )

        label_columns = (
            # use rowid as primary key
            "name TEXT",
            "name_prefix TEXT",
            "name_suffix TEXT",
            "span TEXT",
            "span_start INTEGER",
            "span_end INTEGER",
            "program TEXT",
        )
        c.execute(
            f"CREATE TABLE label ({','.join(label_columns)},"
            "FOREIGN KEY (program) REFERENCES program (program))"
        )
        c.executemany(
            f"INSERT INTO label VALUES ({','.join('?' * len(label_columns))})", label_rows,
        )

        taxon_columns = (
            # use rowid as primary key
            "name TEXT",
            "span TEXT",
            "span_start INTEGER",
            "span_end INTEGER",
            "program TEXT",
        )
        c.execute(
            f"CREATE TABLE taxon ({','.join(taxon_columns)},"
            "FOREIGN KEY (program) REFERENCES program (program))"
        )
        c.executemany(
            f"INSERT INTO taxon VALUES ({','.join('?' * len(taxon_columns))})", taxon_rows,
        )

        connexion.commit()
        connexion.close()


# fmt: off
@overload
def prepared(tags: Labels) -> LabelsPoorSpans:
    ...  # pragma: no cover
@overload
def prepared(tags: Taxons) -> TaxonsPoorSpans:
    ...  # pragma: no cover
def prepared(tags):
    """Prepare the spans for serialization.

    Args:
        tags (Labels|Taxons): The tags or taxons to be serialized.

    Returns:
        LabelPoorSpans|TaxonsPoorSpans:
            A dictionary mapping tag names with the list of their spans, transformed into simple
            lists of two integers.

    .. note::
          Overloaded to support two different combinations of argument types: Mypy can check that
          passing `Labels` (resp. `Taxons`) to the function returns `LabelsPoorSpans` (resp.
          `TaxonsPoorSpans`). Browse GitHub to see the actual overloaded functions.
          See [the documentation](https://docs.python.org/3/library/typing.html#typing.overload).
    """
    result: Union[LabelsPoorSpans, TaxonsPoorSpans] = {}
    for (tag_name, spans) in tags:
        result[tag_name] = [span[:2] for span in sorted(set(spans))]
    return result
# fmt: on


def collect_labels(programs: Programs) -> LabelInfos:
    """Iterate through programs to collect all their labels."""
    result: LabelInfos = defaultdict(list)
    for program in programs:
        for label in program.labels:
            result[label.name].append(program.name)
    return result


def map_labels_on_taxons(programs: Programs, taxonomy: Taxonomy) -> None:
    """Translate labels into taxons on a list of program names."""
    print(f"Mapping taxonomy on {len(programs)} programs.")
    for program in iterate_and_print_programs(programs):
        program.taxons[:] = taxonomy.to_taxons(program.labels)


def collect_taxons(programs: Programs) -> TaxonInfos:
    """Iterate through programs to collect all their taxons."""
    result: TaxonInfos = defaultdict(list)
    for program in programs:
        for taxon in program.taxons:
            result[taxon.name].append(program.name)
    return result


def compute_direct_importations(programs: Programs) -> ProgramToPrograms:
    """Associate each program to the set of its direct internal imports."""
    importations: Dict = {program.name: set() for program in programs}
    for program in programs:
        for label in program.labels:
            match = regex.match(r"import_internally:([^:]+)", label.name)
            if match:  # Python 3.8: use assignement-expression
                importations[program.name].add(f"{match[1]}.py")
    return importations


def complete_and_collect_importations(importations: ProgramToPrograms) -> ProgramToPrograms:
    """Complete the direct internal imports with indirect ones."""

    @lru_cache(maxsize=None)
    def complete_internal_imports(program_name: ProgramName) -> ProgramNameSet:
        result: ProgramNameSet = set(importations.get(program_name, []))
        for imported in list(result):  # traverse a copy
            result.update(complete_internal_imports(imported))
        return result

    completed_importations: ProgramToPrograms = {}
    for program_name in list(importations.keys()):
        completed_importations[program_name] = sorted(complete_internal_imports(program_name))
    return completed_importations


def compute_exportations(programs: Programs, importations: ProgramToPrograms) -> ProgramToPrograms:
    """Invert `importations` to construct `exportations`."""
    exportations: Dict = {program.name: set() for program in programs}
    for (importing_name, imported_names) in importations.items():
        for imported_name in imported_names:
            exportations[imported_name].add(importing_name)
    return exportations


def collect_exportations(exportations: ProgramToPrograms) -> ProgramToPrograms:
    """Iterate through the exportations to collect them."""
    result: ProgramToPrograms = {}
    for (exporting_name, exported_names) in exportations.items():
        result[exporting_name] = sorted(exported_names)
    return result


if __name__ == "__main__":
    # fmt:off
    directories = [
        "examples/simple/programs",
        "../algo/programs",
    ]
    # fmt:on
    print()
    for directory in directories:
        db = Database(Path(directory))
        db.write_json()
        db.write_sqlite()
    print()
