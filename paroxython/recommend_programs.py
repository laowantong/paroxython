"""
A wrapper around `paroxython.filter_programs.ProgramFilter`, feeding it with commands and assessing
the learning costs of its final state.

## Description

The recommendation system is initialized with a database created by `paroxython.make_db`. It parses
the given pipeline
([example](https://repo/examples/dummy/pipe.py)), checks
its commands and submits them to the filter, which in response updates three sets:

- `selected_programs`, the recommended programs;
- `imparted_knowledge`, the taxa modelizing the imparted knowledge;
- `hidden_taxa`, the taxa to be removed from the final output.

When the pipeline is exhausted, it retrieves their values, compute the associated learning costs,
and produces a Markdown report
([example](https://repo/examples/simple/programs_recommendations.md))
whose each section consists in:

- the name of a recommended program;
- its total learning cost;
- its source code;
- the table of its taxa, lexicographically sorted, and accompanied by their spans and individual
  learning cost.

To maximize their utility, these sections are grouped by cost range, and each group is sorted by
increasing total cost and [SLOC](https://en.wikipedia.org/wiki/Source_lines_of_code).
"""

import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

import regex  # type: ignore

from .assess_costs import LearningCostAssessor
from .filter_programs import ProgramFilter
from .goodies import (
    add_line_numbers,
    cost_bucket,
    couple_to_string,
    enumeration_to_txt_factory,
    print_warning,
    title_to_slug_factory,
)
from .user_types import (
    AssessedPrograms,
    Command,
    Criterion,
    JsonDatabase,
    Operation,
    ProgramNames,
)

__pdoc__ = {
    "MalformedData": False,
    "Recommendations": "",
    "Recommendations.__init__": True,
}


class MalformedData(Exception):
    ...


class Recommendations:
    def __init__(self, db: JsonDatabase, base_path: Optional[Path] = None, **kwargs,) -> None:
        """Initialize a recommendation system for the given database of programs tagged with taxa.

        Args:
            db (JsonDatabase): A Python dictionary containing the JSON structure constructed by
                `paroxython.make_db.Database`, i.e. the result of the parsing, labelling and
                taxon-ifying of a set of programs
                ([example](https://repo/examples/simple/programs_db.json)).
                The execution relies on the fields `programs`, `taxa`, `importations` and
                `exportations`, but ignores the field `labels`.
            base_path (Optional[Path], optional): A path, accessible from any optional shell command
                under the name `"{base_path}"`. Defaults to `None`.
            **kwargs: May include the keyword argument `assessment_strategy`, transmitted to
                `paroxython.assess_costs.LearningCostAssessor`.

        Warning:
            `db` is modified by side-effect. After initialization, the taxa of some programs have
            been augmented with the taxa of those they import, associated with an empty list of
            spans. Exception: the taxa starting with `"metadata/"` are not imported.
        """

        self.base_path = base_path

        # copy locally some attributes and methods of a ProgramFilter instance
        program_filter = ProgramFilter(db)
        self.db_programs = program_filter.db_programs
        self.selected_programs = program_filter.selected_programs
        self.imparted_knowledge = program_filter.imparted_knowledge
        self.hidden_taxa = program_filter.hidden_taxa
        self.hidden_programs = program_filter.hidden_programs
        self.update_filter = program_filter.update_filter

        self.assess = LearningCostAssessor(self.db_programs, **kwargs)
        self.result: List[Tuple[int, Operation, ProgramNames]] = []

    def run_pipeline(self, commands: Optional[List[Command]] = None) -> None:
        """Evolve the state of the filter accross pipeline commands.

        Description:
            Execute sequentially all the commands of the pipeline. For each command:

            1. Retrieve the operation (`"include"`, `"exclude"`, `"impart"` or `"hide"`, with an
              optional suffix `" any"` (implicit) or `" all"`).
            2. Retrieve the data by calling `Recommendations.parse_data`.
            3. Update the selected programs and/or impart the associated taxa and/or mark the
              programs or taxa as hidden.
            4. Log the newly filtered out programs in `self.result`.

            Finally, compute the learning costs of the remaining selected programs based on the
            imparted knowledge.

        Args:
            commands (Optional[List[Command]], optional): A list of dictionaries with two mandatory
                entries:

                - `"operation"`: a string among `"include"`, `"exclude"`, `"impart"` and `"hide"`,
                    with an optional suffix `" any"` (implicit) or `" all"`.
                - `"data"`: either a string consisting in a shell command, or an heterogeneous list
                    of _criteria_: patterns (matching either program names or taxon names) or
                    semantic triples (of the form subject, predicate, object).

                Defaults to `None`, which is treated as an empty list.
        """
        commands = commands or []
        current = set(self.db_programs)
        print(f"\nProcessing {len(commands)} commands on {len(current)} programs.")

        # Execute sequentially all the commands of the pipeline
        for (i, command) in enumerate(commands, 1):

            # Retrieve the operation
            try:
                operation = command["operation"]
            except KeyError:
                print_warning(f"operation {i} is ignored (not specified).")
                continue
            (operation, n) = regex.subn(" all", "", operation)
            quantifier = "all" if n == 1 else "any"
            operation = Operation(operation.replace(" any", ""))
            if operation not in ("include", "exclude", "impart", "hide"):
                print_warning(f"operation {i} ({operation}) is ignored (unknown).")
                continue

            # Retrieve the data
            try:
                data = self.parse_data(command.get("data", []), operation)
            except MalformedData:
                print_warning(f"unable to interpret the data of operation {i} ({operation}).")
                continue
            if not data:
                print_warning(f"operation {i} ({operation}) is ignored (no data).")
                continue

            # Update the state of the filter: selected / hidden programs, imparted / hidden taxa
            self.update_filter(data, operation, quantifier)

            # Log the statistics of the filter state for the last operation
            (previous, current) = (current, set(self.selected_programs))
            self.result.append((i, operation, sorted(previous - current)))
            print(f"  {len(current)} programs remaining after operation {i} ({operation}).")

        self.assess.set_imparted_knowledge(self.imparted_knowledge)
        self.assessed_programs = self.assess(self.selected_programs)

    def parse_data(
        # fmt: off
        self,
        data: Union[str, List[Criterion]],
        operation: Operation
        # fmt: on
    ) -> List[Criterion]:
        """Retrieve the list of criteria to which to apply the given operation.

        Description:
            In case `data` is a list of criteria, return it unchanged. Otherwise, if it is a string,
            execute it as a shell command, capture its output and return it as a list of strings.
            Otherwise, fail.

        Note:
            A shell command cannot produce semantic triples. Its output is necessarily interpreted
            as a list of patterns.

        Args:
            data (Union[str, List[Criterion]]): Either a shell command (`str`) or a list of
                criteria. A criterion is either a pattern (`str`) or a semantic triple
                (`Tuple[str, str, str]`) subject, predicate, object.
            operation (Operation): Either `"include"`, `"exclude"`, `"impart"` or `"hide"`
                (note that the optional suffix `" all"` has been previously suppressed).

        Raises:
            MalformedData: Indicates that the field `"data"` of a pipeline command cannot
                be interpreted.

        Returns:
            List[Criterion]: A list of criteria.
        """
        if isinstance(data, list):  # The object can either be a list of criteria...
            return data
        elif isinstance(data, str):  # ... or a shell command printing them on stdout
            criteria = subprocess.run(
                str(data).format(base_path=self.base_path),  # str() needed by mypy
                stdout=subprocess.PIPE,  # From Python 3.7, these two arguments can be
                stderr=subprocess.PIPE,  # ... replaced by: capture_output=True
                encoding="utf-8",
                shell=True,
                check=True,
            )
            return [criterion for criterion in criteria.stdout.strip().split("\n")]
        else:
            raise MalformedData

    def get_markdown(
        self,
        span_column_width: int = 30,
        sorting_strategy: str = "by_cost_and_sloc",
        grouping_strategy: str = "by_cost_bucket",
    ) -> str:
        """Iterate on the results. Group, sort and output them."""

        # Define some helper functions.

        title_to_slug = title_to_slug_factory()
        spans_to_html = enumeration_to_txt_factory(span_column_width, "_imported_")
        display_count = lambda n: f"{n} program" + ("" if n == 1 else "s")

        sorting_key = None
        if sorting_strategy == "by_cost_and_sloc":
            sorting_key = lambda x: (x[0], len(self.db_programs[x[1]]["source"].split("\n")))
        elif sorting_strategy == "lexicographic":
            sorting_key = lambda x: x[1]

        grouping_key = lambda x: f"(default: no group)"
        if grouping_strategy == "by_cost_bucket":
            grouping_key = cost_bucket

        # Group resulting programs into cost buckets, and sort each group by increasing difficulty.

        toc_data: Dict[str, AssessedPrograms] = defaultdict(list)
        for (cost, program_name) in self.assessed_programs:
            if program_name in self.hidden_programs:
                continue
            toc_data[grouping_key(cost)].append((cost, program_name))
        for costs_and_program_names in toc_data.values():
            costs_and_program_names.sort(key=sorting_key)

        # Accumulate simultaneously the TOC and the contents.

        toc: List[str] = ["# Table of contents"]
        contents: List[str] = [f"# Recommended programs"]

        for (bounds, costs_and_program_names) in toc_data.items():

            title = f"{display_count(len(costs_and_program_names))} of learning cost {bounds}"
            toc.append(f"- [`{title}`](#{title_to_slug(title)})")
            contents.append(f"\n## {title}")

            for (cost, program_name) in costs_and_program_names:
                program_info = self.db_programs[program_name]
                title = f"Program `{program_name}` (learning cost {cost})"
                toc.append(f"    - [`{program_name}`](#{title_to_slug(title)})")
                contents.append(f"\n### {title}")
                contents.append(f"\n```python\n{add_line_numbers(program_info['source'])}\n```")
                contents.append("\n| Cost  | Taxon | Location |")
                contents.append("|" + "----|" * 3)
                items = sorted(
                    program_info["taxa"].items(),
                    key=lambda x: f"~{x[0]}" if x[0].startswith("metadata/") else x[0],
                )
                for (taxon_name, spans) in items:
                    if taxon_name in self.hidden_taxa:
                        continue
                    taxon_cost = self.assess.taxon_cost(taxon_name)
                    s = spans_to_html(", ".join(map(couple_to_string, spans)))
                    contents.append(f"| {taxon_cost} | `{taxon_name}` | {s} |")
                contents.append("\n---")

        def programs_to_html(description: str, programs: ProgramNames) -> str:
            details = []
            if programs:
                description = description.replace(" 1 programs", " 1 program")
                details = ["<ol>"]
                for program in sorted(programs):
                    details.append(f"  <li><code>{program}</code></li>")
                details.append("</ol>")
            return (
                "<details>\n"
                + f"  <summary>{description}.</summary>\n  "
                + "\n  ".join(details)
                + "\n</details>\n"
            )

        n = len(self.db_programs)
        summary: List[str] = [f"\n# Summary"]
        summary.append(programs_to_html(f"{n} initially", list(self.db_programs)))
        for (i, operation, removed_programs) in self.result:
            n -= len(removed_programs)
            title = f"{n} remaining after operation {i} ({operation}) has filtered out {len(removed_programs)} programs"
            summary.append(programs_to_html(title, removed_programs))

        return "\n".join(toc + contents + summary)


if __name__ == "__main__":
    ast = __import__("ast")
    json = __import__("json")
    program_path = Path("../algo/programs")
    rec = Recommendations(
        db=json.loads(Path(f"{program_path}_db.json").read_text()), base_path=program_path.parent,
    )
    rec.run_pipeline(ast.literal_eval(Path(f"{program_path}_pipe.py").read_text()))
    output_path = Path(f"{program_path}_recommendations.md")
    output_path.write_text(rec.get_markdown())
    print(f"Dumped: {output_path.resolve()}.\n")
