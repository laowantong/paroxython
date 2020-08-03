"""Collect all infos pertaining to the programs, labels and taxa, and dump them in a database."""

import json
import sqlite3
from bisect import insort
from collections import defaultdict
from datetime import datetime
from functools import lru_cache
from pathlib import Path
from typing import Callable, List, Optional, Tuple, Dict

import regex  # type: ignore

from paroxython.goodies import add_line_numbers
from paroxython.label_programs import labelled_programs, iterate_and_print_programs
from paroxython.map_taxonomy import Taxonomy
from paroxython.user_types import (
    LabelInfos,
    Labels,
    LabelsPoorSpans,
    ProgramInfos,
    ProgramName,
    ProgramNameSet,
    Programs,
    ProgramToPrograms,
    TaxonInfos,
    Taxa,
    TaxaPoorSpans,
)

__pdoc__ = {
    "Database": "",
    "Database.__init__": True,
}


class Database:
    def __init__(self, directory: Path, ignore_timestamps: bool = False, **kwargs) -> None:
        """Construct and populate the complete database of program features.

        Args:
            directory (Path): The directory to walk (by default, recursively), containing the
                Python programs of interest.
            ignore_timestamps (bool, optional): Don't store the last modification dates of these
                programms. Since the database snapshots generated by our tests are placed under
                version control, this prevents Git from tracking irrelevant differences. Defaults
                to `False`.
            **kwargs: May include the keyword arguments `cleanup_strategy`, `skip_pattern`,
                `glob_pattern`, transmitted to `paroxython.list_programs.list_programs` through
                `paroxython.label_programs.labelled_programs`, and `taxonomy_path`, transmitted to
                `paroxython.map_taxonomy.Taxonomy`.

        Description:
            1. Create a list `programs` of `Program` objects, labelled by
              `paroxython.label_programs.labelled_programs`.
            2. Create a dictionary `self.labels` mapping each label name to the names of the
              programs featuring it (`collect_labels`).
            3. Map the labels to taxa (`paroxython.map_taxonomy.Taxonomy`), and populate the field
              `taxa` of `programs` (`map_labels_on_taxa`).
            4. Create a dictionary `self.taxa` mapping each taxon name to the names of the
              programs featuring it (`collect_taxa`).
            5. Create a dictionary `self.importations` mapping each program name to the names
              of the programs importing it, both directly (`compute_direct_importations`) and
              indirectly (`complete_and_collect_importations`).
            6. Invert the previous dictionary to create a dictionary `self.exportations`
              (`compute_and_collect_exportations`).
            7. Gather in `self.programs_infos` each program timestamp, source, labels and taxa as
              a serialization-ready dictionary indexed by program names.
        """

        self.directory = directory
        programs: Programs = labelled_programs(directory, **kwargs)
        self.labels = collect_labels(programs)

        map_labels_on_taxa(programs, Taxonomy(**kwargs))
        self.taxa = collect_taxa(programs)

        importations = compute_direct_importations(programs)
        self.importations = complete_and_collect_importations(importations)
        self.exportations = compute_and_collect_exportations(programs, self.importations)

        get_timestamp = lambda path: str(datetime.fromtimestamp(path.stat().st_mtime))
        if ignore_timestamps:
            get_timestamp = lambda path: ""
        self.programs_infos: ProgramInfos = {}
        for program in programs:
            self.programs_infos[program.name] = {
                "timestamp": get_timestamp(directory / program.name),
                "source": program.source,
                "labels": prepared_labels(program.labels),
                "taxa": prepared_taxa(program.taxa),
            }

    def get_json(self) -> str:
        r"""Dump the constructed `Database` object as a JSON string.

        Description:
            The JSON schema is as follows:

            ```json
            {
                "programs": {
                    "program_1.py" : {
                        "timestamp": "1970-01-01",
                        "source": "print('hello')\nprint('world')\n",
                        "labels": {
                            "label_1": [[span_start_1, span_end_1], ...],
                            ...
                        },
                        "taxa: {
                            "taxon_1": [[span_start_1, span_end_1], ...],
                            ...
                        }
                    },
                    ...
                }
                "labels": {
                    "label_1": ["program_1.py", "program_2.py", ...],
                    ...
                },
                "taxa": {
                    "taxon_1": ["program_1.py", "program_2.py", ...],
                    ...
                },
                "importations": {
                    "program_1.py": ["program_2.py", "program_3.py", ...],
                    ...
                },
                "exportations": {
                    "program_1.py": [],
                    "program_2.py": ["program_1.py", ...],
                    ...
                }
            }
            ```

            All fields have already been calculated during the construction of the instance.

        Note:
            For readability purposes, the output of `json.dumps()` is reformatted to fit each span
            list on a single line, _e.g._:
            ```json
                        "flow/loop/exit/late": [
                            [
                                3,
                                8
                            ],
                            [
                                6,
                                7
                            ]
                        ],
            ```
            ... is unwrap as:
            ```json
                        "flow/loop/exit/late": [[3,8],[6,7]],
            ```

        Example:
            See the [JSON database](https://repo/examples/mini/programs_db.json) constructed from
            the programs of this [directory](https://repo/examples/mini/programs).
        """
        data = {
            "programs": self.programs_infos,
            "labels": dict(sorted(self.labels.items())),
            "taxa": dict(sorted(self.taxa.items())),
            "importations": dict(self.importations.items()),
            "exportations": dict(self.exportations.items()),
        }
        text = json.dumps(data, indent=2) + "\n"
        text = regex.sub(r"\s*\[\s+(\d+),\s+(\d+)\s+\](,?)\s+", r"[\1,\2]\3", text)
        return text

    def write_json(self, db_path: Optional[Path] = None) -> None:
        """Call `Database.get_json` and write the result to a file.

        Args:
            db_path (Optional[Path], optional): If not provided, and the directory provided to the
                class constructor is `"foobar"`, falls back to `"foobar_db.json"` in the same parent
                directory. Defaults to `None`.
        """
        db_path = db_path or self.directory.parent / f"{self.directory.name}_db.json"
        print(f"Writing {db_path}.")
        db_path.write_text(self.get_json())

    def write_sqlite(self, db_path: Optional[Path] = None) -> None:
        """Dump the constructed `Database` object as a SQLite database (experimental).

        Args:
            db_path (Optional[Path], optional): The path of the SQLite database. If not provided,
                and the directory provided to the class constructor is `"foobar"`, falls back to
                `"foobar_db.sqlite"` in the same parent directory. Defaults to `None`.

        Description:
            The relational schema is as follows:

            ```sql
            CREATE TABLE program (
                program TEXT PRIMARY KEY,
                timestamp TEXT,
                source TEXT
            );
            CREATE TABLE label (
                -- use rowid as primary key
                name TEXT,
                name_prefix TEXT,
                name_suffix TEXT,
                span TEXT,
                span_start INTEGER,
                span_end INTEGER,
                program TEXT,
                FOREIGN KEY (program) REFERENCES program (program)
            );
            CREATE TABLE taxon (
                -- use rowid as primary key
                name TEXT,
                span TEXT,
                span_start INTEGER,
                span_end INTEGER,
                program TEXT,
                FOREIGN KEY (program) REFERENCES program (program)
            );
            ```

            Having a relational version of the database means that it can be queried with SQL.
            Here is an example of such a query:

            ```sql
            SELECT
                name AS taxon,
                program,
                group_concat(span, ", ") AS spans,
                source
            FROM program
            JOIN taxon USING (program)
            WHERE name GLOB "type/non_sequence/dictionary/*"
            GROUP BY name, program
            ```

            On the provided
            [simple programs](https://repo/examples/simple/programs),
            its execution results in:

            ![](resources/sql_query_example.png)

        Note:
            The same list of programs can be obtained by feeding
            `paroxython.recommend_programs.Recommendations.run_pipeline`
            with the following command:

            ```python
                {
                    "operation": "include",
                    "data": ["type/non_sequence/dictionary/"]
                }
            ```

            Although SQL should be familiar to almost everyone in our target audience, and might
            “make complex things possible”, the current minimalistic schema arguably does not
            ”make simple things simple” (to paraphrase Alan Kay). Some denormalization should ease
            the process, but so far we have prioritized the development of the pipeline system. The
            relational database generation may be a dead-end, and is currently not used anywhere in
            Paroxython.
        """
        db_path = db_path or self.directory.parent / f"{self.directory.name}_db.sqlite"
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
            for (taxon_name, spans) in info["taxa"].items():
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

        if db_path.exists():  # pragma: no cover / Python 3.8: use missing_ok=True parameter
            db_path.unlink()
        connexion = sqlite3.connect(str(db_path))  # str() for Python 3.6 compatibility
        c = connexion.cursor()

        fill = lambda columns: ",".join("?" * len(columns))
        program_columns = (
            "program TEXT PRIMARY KEY",
            "timestamp TEXT",
            "source TEXT",
        )
        c.execute(f"CREATE TABLE program ({','.join(program_columns)})")
        c.executemany(f"INSERT INTO program VALUES ({fill(program_columns)})", program_rows)

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
        c.executemany(f"INSERT INTO label VALUES ({fill(label_columns)})", label_rows)

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
        c.executemany(f"INSERT INTO taxon VALUES ({fill(taxon_columns)})", taxon_rows)

        connexion.commit()
        connexion.close()


def collect_labels(programs: Programs) -> LabelInfos:
    """Iterate through the given programs to collect all their labels.

    Args:
        programs (Programs): A list of `Program` objects, with their `name` and `labels` fields
            already populated.

    Returns:
        LabelInfos: A dictionary mapping each label name to the names of the programs featuring it.
    """
    result: LabelInfos = defaultdict(list)
    for program in programs:
        for label in program.labels:
            result[label.name].append(program.name)
    return result


def map_labels_on_taxa(programs: Programs, taxonomy: Taxonomy) -> None:
    """Populate the `taxa` fields of the given `programs` with the translations of their labels.

    Args:
        programs (Programs): A list of `Program` objects with their `labels` field populated.
        taxonomy (Taxonomy): A “translator” of label names into taxon names.
    """
    print(f"Mapping taxonomy on {len(programs)} programs.")
    for program in iterate_and_print_programs(programs):
        program.taxa[:] = taxonomy.to_taxa(program.labels)
        # `program` being a tuple, modifying its fields can only be done in place.


def collect_taxa(programs: Programs) -> TaxonInfos:
    """Iterate through the given programs to collect all their taxa.

    Args:
        programs (Programs): A list of `Program` objects, with their `name` and `taxa` fields
            already populated.

    Returns:
        TaxonInfos: A dictionary mapping each taxon name to the names of the programs featuring it.
    """
    result: TaxonInfos = defaultdict(list)
    for program in programs:
        for taxon in program.taxa:
            result[taxon.name].append(program.name)
    return result


def compute_direct_importations(
    programs: Programs, match_import: Callable = regex.compile(r"import_internally:([^:]+)").match
) -> ProgramToPrograms:
    """Associate each given labelled program to the set of its direct internal imports.

    Description:
        Iterate through the programs, retrieve their labels starting with `"import_internally"`
        and collect the names of the involved programs.

    Args:
        programs (Programs): A list of labelled `Program` objects.
        match_import (Callable, optional):  A function taking a label name and, in
            the case it starts with `"import_internally:"`, returns a match object whose
            first group is the name of the imported program.
            [Not to be explicitly provided.](docs_developer_manual/index.html#default-argument-trick)

    Returns:
        ProgramToPrograms: A dictionary mapping every program name to the list of the names of
            the internal programs it imports directly.
    """
    importations: Dict = {program.name: set() for program in programs}
    for program in programs:
        for label in program.labels:
            match = match_import(label.name)
            if match:  # Python 3.8: use assignement-expression
                importations[program.name].add(f"{match[1]}.py")
    return importations


def complete_and_collect_importations(importations: ProgramToPrograms) -> ProgramToPrograms:
    """Complete the direct internal imports with indirect ones.

    Args:
        importations (ProgramToPrograms): A dictionary mapping every program name to the list
            of the names of the internal programs it imports directly.

    Returns:
        ProgramToPrograms: A dictionary mapping every program name to the sorted list of the
            names of the internal programs it imports either directly or indirectly.
    """

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


def compute_and_collect_exportations(
    programs: Programs, importations: ProgramToPrograms
) -> ProgramToPrograms:
    """Invert `importations` to construct `exportations`.

    Args:
        programs (Programs):  A list of named `Program` objects.
        importations (ProgramToPrograms): A dictionary mapping every program name to the list of
            the names of the internal programs it imports either directly or indirectly.

    Returns:
        ProgramToPrograms: A dictionary mapping every program name to the sorted list of the names
            of the internal programs it is imported by, either directly or indirectly.
    """
    exportations: ProgramToPrograms = {program.name: [] for program in programs}
    for (importing_name, imported_names) in importations.items():
        for imported_name in imported_names:
            if importing_name not in exportations[imported_name]:
                insort(exportations[imported_name], importing_name)
    return exportations


def prepared_labels(labels: Labels) -> LabelsPoorSpans:
    """Prepare the labels for serialization.

    Args:
        labels (Labels): The list of labels to be serialized. Each label consists in a name and a
            **list** of spans. Each span is a tuple starting by the actual range of line numbers.

    Returns:
        LabelPoorSpans:
            A dictionary mapping the label names with the list of their spans, transformed into
            simple couples of integers.

    Example:
        >>> prepared_labels([
        ...     ("name_1", [
        ...             Span(start=1, end=2, path="foo"),
        ...             Span(start=1, end=2, path="foo"),  # note the duplicate
        ...             Span(start=1, end=2, path="bar"),  # note the difference
        ...         ]),
        ...     ("name_2", [
        ...             Span(start=2, end=4, path="fizz"),
        ...             Span(start=6, end=7, path="buzz"),
        ...         ]),
        ...     ("name_3", [Span(start=5, end=5, path="foobar")]),
        ... ])
        {
            "name_1": [(1, 2), (1, 2)],  # deduplicated
            "name_2": [(2, 4), (6, 7)],
            "name_3": [(5, 5)],
        }
    """
    result: LabelsPoorSpans = {}
    for (label_name, spans) in labels:
        result[label_name] = [(span.start, span.end) for span in sorted(set(spans))]
    return result


def prepared_taxa(taxa: Taxa) -> TaxaPoorSpans:
    """Prepare the taxa for serialization.

    Args:
        taxa (Taxa): The list of taxa to be serialized. Each taxon consists in a name and a
            **bag** of spans. Each span is a tuple starting by the actual range of line numbers.

    Returns:
        TaxonPoorSpans:
            A dictionary mapping the taxon names with the list of their spans, transformed into
            simple couples of integers.

    Example:
        >>> prepared_taxa([
        ...     ("name_1", Counter({
        ...             Span(start=1, end=2, path="foo"): 2,  # note the duplicate
        ...             Span(start=1, end=2, path="bar"): 1,
        ...         })),
        ...     ("name_2", Counter({
        ...             Span(start=2, end=4, path="fizz"): 1,
        ...             Span(start=6, end=7, path="buzz"): 1,
        ...         })),
        ...     ("name_3", Counter({Span(start=5, end=5, path="foobar"): 1}))
        ... ])
        {
            "name_1": [(1, 2), (1, 2)],  # deduplicated
            "name_2": [(2, 4), (6, 7)],
            "name_3": [(5, 5)],
        }
    """
    result: TaxaPoorSpans = {}
    for (taxon_name, spans) in taxa:
        result[taxon_name] = [(span.start, span.end) for span in sorted(spans)]
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
        db = Database(Path(directory), ignore_timestamps=True)
        db.write_json()
        db.write_sqlite()
    print()
