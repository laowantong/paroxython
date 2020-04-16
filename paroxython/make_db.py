import json
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple, Union, overload

import regex  # type: ignore

from generate_labels import generate_labelled_programs
from goodies import add_line_numbers
from map_taxonomy import Taxonomy
from user_types import (
    LabelInfos,
    Labels,
    LabelsPoorSpans,
    ProgramTaxons,
    Program,
    ProgramInfos,
    ProgramName,
    TaxonInfos,
    Taxons,
    TaxonsPoorSpans,
)


class Database:
    def __init__(self, directory: Path, ignore_timestamps=False, *args, **kargs) -> None:
        """collect all infos pertaining to the programs, the labels and the taxons."""
        self.default_json_db_path = directory.parent / f"{directory.name}_db.json"
        self.default_sqlite_db_path = directory.parent / f"{directory.name}_db.sqlite"
        programs: List[Program] = generate_labelled_programs(directory, *args, **kargs)
        program_taxons: ProgramTaxons = dict(Taxonomy()(programs))

        get_timestamp = lambda path: str(datetime.fromtimestamp(path.stat().st_mtime))
        if ignore_timestamps:
            get_timestamp = lambda path: "ignored"

        self.programs: ProgramInfos = {}
        for program in programs:
            self.programs[program.name] = {
                "timestamp": get_timestamp(directory / program.name),
                "links": sorted(ProgramName(link) for link in program.links),
                "source": program.source,
                "labels": {},  # to be populated by inject_labels()
                "taxons": {},  # to be populated by inject_taxons()
            }

        self.labels: LabelInfos = defaultdict(list)
        for program in programs:
            for label in program.labels:
                self.labels[label.name].append(program.name)
        for program in programs:
            self.programs[program.name]["labels"] = prepared(program.labels)

        self.taxons: TaxonInfos = defaultdict(list)
        for (program_name, taxons) in program_taxons.items():
            for taxon in taxons:
                self.taxons[taxon.name].append(program_name)
        for (program_name, taxons) in program_taxons.items():
            self.programs[program_name]["taxons"] = prepared(taxons)

    def get_json(self) -> str:
        """Dump the data to JSON, reduce each list of spans to one line."""
        data = {
            "programs": self.programs,
            "labels": self.labels,
            "taxons": self.taxons,
        }
        text = json.dumps(data, indent=2)
        text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
        return text

    def write_json(self, db_path: Optional[Path] = None) -> None:
        db_path = db_path or self.default_json_db_path
        db_path.write_text(self.get_json())

    def write_sqlite(self, db_path: Optional[Path] = None) -> None:
        db_path = db_path or self.default_sqlite_db_path
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
        "../Python/project_euler",
        "../Python/maths",
        "../algo/programs",
        # "paroxython"
    ]
    # fmt:on
    for directory in directories:
        db = Database(Path(directory))
        db.write_json()
        db.write_sqlite()
