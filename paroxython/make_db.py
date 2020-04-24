import json
import sqlite3
from collections import defaultdict
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import List, Optional, Tuple, Union, overload, Dict

import regex  # type: ignore

from goodies import add_line_numbers
from list_labels import ProgramLabeller
from map_taxonomy import Taxonomy
from user_types import (
    LabelInfos,
    Labels,
    LabelsPoorSpans,
    ProgramInfos,
    ProgramName,
    ProgramNameSet,
    Programs,
    ProgramTaxons,
    ProgramToPrograms,
    TaxonInfos,
    Taxons,
    TaxonsPoorSpans,
)


class Database:
    def __init__(self, directory: Path, ignore_timestamps=False, *args, **kargs) -> None:
        """Collect all infos pertaining to the programs, the labels and the taxons."""
        self.default_json_db_path = directory.parent / f"{directory.name}_db.json"
        self.default_sqlite_db_path = directory.parent / f"{directory.name}_db.sqlite"

        get_timestamp = lambda path: str(datetime.fromtimestamp(path.stat().st_mtime))
        if ignore_timestamps:
            get_timestamp = lambda path: "ignored"

        labeller = ProgramLabeller(directory, *args, **kargs)
        programs: Programs = labeller.list_labelled_programs()
        self.programs: ProgramInfos = {}
        for program in programs:
            self.programs[program.name] = {
                "timestamp": get_timestamp(directory / program.name),
                "source": program.source,
                "labels": {},  # to be populated by below
                "taxons": {},  # to be populated by below
            }

        self.initialize_labels(programs)
        self.initialize_taxons(programs)
        self.initialize_importations(programs)
        self.initialize_exportations(programs)

    def initialize_labels(self, programs: Programs) -> None:
        for program in programs:
            self.programs[program.name]["labels"] = prepared(program.labels)
        self.labels: LabelInfos = defaultdict(list)
        for program in programs:
            for label in program.labels:
                self.labels[label.name].append(program.name)

    def initialize_taxons(self, programs: Programs) -> None:
        program_taxons: ProgramTaxons = dict(Taxonomy()(programs))
        for (program_name, taxons) in program_taxons.items():
            self.programs[program_name]["taxons"] = prepared(taxons)
        self.taxons: TaxonInfos = defaultdict(list)
        for (program_name, taxons) in program_taxons.items():
            for taxon in taxons:
                self.taxons[taxon.name].append(program_name)

    def initialize_importations(self, programs) -> None:
        """Associate each program to the set of its internal imports (direct and indirect)."""

        # Starts with DIRECT internal imports.
        importations: Dict = {program.name: set() for program in programs}
        for program in programs:
            for label in program.labels:
                match = regex.match(r"import_internally:([^:]+)", label.name)
                if match:  # Python 3.8: use assignement-expression
                    importations[program.name].add(f"{match[1]}.py")

        # Complete them recursively with INDIRECT internal imports.
        @lru_cache(maxsize=None)
        def complete_internal_imports(program_name: ProgramName) -> ProgramNameSet:
            result: ProgramNameSet = importations.get(program_name, set())
            for imported in list(result):  # traverse a copy
                result.update(complete_internal_imports(imported))
            return result

        self.importations: ProgramToPrograms = {}
        for program_name in list(importations.keys()):
            self.importations[program_name] = sorted(complete_internal_imports(program_name))

    def initialize_exportations(self, programs) -> None:
        """Invert `importations` to construct `exportations`."""
        exportations: Dict = {program.name: set() for program in programs}
        for (importing_name, imported_names) in self.importations.items():
            for imported_name in imported_names:
                exportations[imported_name].add(importing_name)

        self.exportations: ProgramToPrograms = {}
        for (exporting_name, exported_names) in exportations.items():
            self.exportations[exporting_name] = sorted(exported_names)

    def get_json(self) -> str:
        """Dump the data to JSON, reduce each list of spans to one line."""
        data = {
            "programs": self.programs,
            "labels": dict(sorted(self.labels.items())),
            "taxons": dict(sorted(self.taxons.items())),
            "importations": dict(self.importations.items()),
            "exportations": dict(self.exportations.items()),
        }
        text = json.dumps(data, indent=2)
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
        for (path, info) in self.programs.items():
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
        connexion = sqlite3.connect(db_path)
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
    """Prepare the spans for serialization."""
    result: Union[LabelsPoorSpans, TaxonsPoorSpans] = {}
    for (tag_name, spans) in tags:
        result[tag_name] = [span.to_couple() for span in sorted(set(spans))]
    return result
# fmt: on


if __name__ == "__main__":
    # fmt:off
    directories = [
        # "../Python/project_euler",
        # "../Python/maths",
        "../algo/programs",
        # "paroxython"
    ]
    # fmt:on
    print()
    for directory in directories:
        db = Database(Path(directory))
        db.write_json()
        db.write_sqlite()
    print()
