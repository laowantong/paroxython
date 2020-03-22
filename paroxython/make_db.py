import json
import sqlite3
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import List, Union, Tuple, overload

import regex  # type: ignore

from generate_labels import generate_labelled_programs
from map_taxonomy import Taxonomy
from user_types import (
    LabelInfos,
    LabelName,
    Labels,
    LabelsPoorSpans,
    PathTaxons,
    Program,
    ProgramInfos,
    ProgramName,
    ProgramRecord,
    Source,
    TaxonInfos,
    TaxonName,
    Taxons,
    TaxonsPoorSpans,
)


class Database:
    def __init__(self, directories: List[str], ignore_timestamps=False, *args, **kargs) -> None:
        """collect all infos pertaining to the programs, the labels and the taxons."""
        programs: List[Program] = []
        for directory in directories:
            programs.extend(generate_labelled_programs(directory, *args, **kargs))

        taxonomy = Taxonomy()
        paths_taxons = list(taxonomy(programs))

        get_timestamp = lambda program: str(datetime.fromtimestamp(program.path.stat().st_mtime))
        if ignore_timestamps:
            get_timestamp = lambda program: "ignored"

        self.programs: ProgramInfos = {}
        for program in programs:
            self.programs[ProgramName(str(program.path))] = {
                "timestamp": get_timestamp(program),
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

    def write_sqlite(self, db_path: str) -> None:
        program_rows: List[Tuple] = []
        label_rows: List[Tuple] = []
        taxon_rows: List[Tuple] = []
        for (path, info) in self.programs.items():
            source = f"{path}\n\n" + "\n".join(
                f"{line_number: <4}{line}"
                for (line_number, line) in enumerate(info["source"].split("\n"), 1)
            )
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

        if Path(db_path).exists():  # Python 3.8: use missing_ok=True parameter
            Path(db_path).unlink()
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
            # use rowid as primary key:
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
            # use rowid as primary key:
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
    directories = [
        # "../Python/project_euler",
        # "../Python/maths",
        "../algo/programs",
        # "paroxython"
    ]
    db = Database(directories)
    Path("db.json").write_text(db.get_json())
    db.write_sqlite("db.sqlite")
