"""
"""

import subprocess
from collections import Counter as counter
from collections import defaultdict
from pathlib import Path
from typing import Counter, Dict, List, Optional, Tuple, Union

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
from .normalize_predicate import normalize_predicate
from .user_types import (
    AssessedPrograms,
    AssessmentStrategy,
    Command,
    JsonDatabase,
    Operation,
    ProgramName,
    ProgramNames,
    ProgramNameSet,
    TaxonNameSet,
)


class Recommendations:
    def __init__(
        self,
        db: JsonDatabase,
        commands: Optional[List[Command]] = None,
        base_path: Optional[Path] = None,
        cost_assessment_strategy: AssessmentStrategy = "zeno",
    ) -> None:

        self.commands = commands or []
        self.base_path = base_path

        # copy locally some attributes and methods or a ProgramFilter instance
        program_filter = ProgramFilter(db)
        self.programs = program_filter.db_programs
        self.selected_programs = program_filter.selected_programs
        self.imparted_knowledge = program_filter.imparted_knowledge
        self.get_programs_from_program_pattern = program_filter.get_programs_from_program_pattern
        self.get_taxons_from_taxon_pattern = program_filter.get_taxons_from_taxon_pattern
        self.taxons_of_programs = program_filter.taxons_of_programs
        self.programs_of_taxons = program_filter.programs_of_taxons
        self.programs_of_triple = program_filter.programs_of_triple
        self.programs_of_negated_triple = program_filter.programs_of_negated_triple
        self.update_filter = program_filter.update_filter

        # copy locally some attributes and methods or a LearningCostAssessor instance
        self.assess_costs = LearningCostAssessor(self.imparted_knowledge)
        self.assess_costs.set_cost_assessment_strategy(cost_assessment_strategy)
        self.taxon_cost = self.assess_costs.taxon_cost

    def run_pipeline(self) -> None:
        """Evolve recommended programs, imparted knowledge and log accross pipeline commands."""

        current = set(self.programs)
        print(f"\nProcessing {len(self.commands)} commands on {len(current)} programs.")

        # Execute sequentially all the commands of the pipeline
        for (i, command) in enumerate(self.commands, 1):

            # Retrieve the operation
            try:
                operation = command["operation"]
            except KeyError:
                print_warning(f"operation {i} is ignored (not specified).")
                continue
            (operation, n) = regex.subn(" all", "", operation)
            any_or_all = "all" if n == 1 else "any"
            operation = Operation(operation.replace(" any", ""))
            if operation not in ("include", "exclude", "impart"):
                print_warning(f"operation {i} ({operation}) is ignored (unknown).")
                continue

            # Retrieve the patterns
            patterns = self.retrieve_patterns_from_source(command.get("data", []), operation, i)
            if not patterns:
                print_warning(f"operation {i} ({operation}) is ignored (no data).")
                continue

            # Compute the sets from which the program selection and knowledge will be updated
            (taxons, programs) = self.new_taxons_and_programs(operation, patterns, i, any_or_all)

            # Update the selected programs and optionally impart the associated taxons
            self.update_filter(operation, taxons, programs)

            # Update the statistics of the filter state for the last operation
            (previous, current) = (current, set(self.selected_programs))
            command["filtered_out"] = sorted(previous - current)
            print(f"  {len(current)} programs remaining after operation {i} ({operation}).")

        self.assessed_programs = self.assess_costs(self.selected_programs)

    def retrieve_patterns_from_source(
        # fmt: off
        self,
        data: Union[str, List[str]],
        operation: Operation,
        i: int
        # fmt: on
    ) -> List[str]:
        """Retrieve the patterns on which the operation will be applied."""
        if isinstance(data, list):  # The JSON object can either be a list of strings...
            return data
        elif isinstance(data, str):  # ... or a shell command printing them on stdout
            result = (
                subprocess.run(
                    str(data).format(base_path=self.base_path),  # str() needed by mypy
                    stdout=subprocess.PIPE,  # From Python 3.7, these two arguments can be
                    stderr=subprocess.PIPE,  # ... replaced by: capture_output=True
                    encoding="utf-8",
                    shell=True,
                    check=True,
                )
                .stdout.strip()
                .split("\n")
            )
            return result
        else:
            print_warning(f"unable to interpret the pattern of operation {i} ({operation}).")
            return []

    def new_taxons_and_programs(
        # fmt: off
        self,
        operation: Operation,
        patterns: List[str],
        i: int,
        any_or_all="any"
        # fmt: on
    ) -> Tuple[TaxonNameSet, ProgramNameSet]:
        """Compute the programs and the taxons targeted by the operation application."""
        new_taxons: TaxonNameSet = set()
        new_programs: ProgramNameSet = set()
        pattern_count_by_program: Counter[ProgramName] = counter()
        for pattern in patterns:
            taxons: TaxonNameSet = set()
            programs: ProgramNameSet = set()
            if isinstance(pattern, str):
                if pattern.endswith(".py"):
                    programs = self.get_programs_from_program_pattern(pattern)
                    taxons = self.taxons_of_programs(programs, operation == "exclude")
                else:
                    taxons = self.get_taxons_from_taxon_pattern(pattern)
                    if operation != "impart":
                        programs = self.programs_of_taxons(taxons, operation == "exclude")
            elif isinstance(pattern, (list, tuple)) and len(pattern) == 3:
                if operation == "impart":
                    print_warning(f"operation {i} pattern '{pattern}' is ignored (imparted).")
                    continue
                (pattern_1, raw_predicate, pattern_2) = pattern
                (predicate, negated) = normalize_predicate(raw_predicate)
                f = self.programs_of_negated_triple if negated else self.programs_of_triple
                programs = f(pattern_1, predicate, pattern_2)
            else:
                print_warning(f"operation {i} pattern '{pattern}' is ignored (malformed).")
            new_taxons.update(taxons)
            new_programs.update(programs)
            pattern_count_by_program.update(programs)
        if any_or_all == "all":
            new_programs.difference_update(
                program
                for (program, count) in pattern_count_by_program.items()
                if len(patterns) != count
            )
        return (new_taxons, new_programs)

    def get_markdown(
        self,
        span_column_width=30,
        sorting_strategy="by_cost_and_sloc",
        grouping_strategy="by_cost_bucket",
    ) -> str:
        """Reiterate on the commands, now populated by the results, and output them."""

        # Define some helper functions.

        title_to_slug = title_to_slug_factory()
        spans_to_html = enumeration_to_txt_factory(span_column_width, "_imported_")
        display_count = lambda n: f"{n} program" + ("" if n == 1 else "s")

        sorting_key = None
        if sorting_strategy == "by_cost_and_sloc":
            sorting_key = lambda x: (x[0], len(self.programs[x[1]]["source"].split("\n")))
        elif sorting_strategy == "lexicographic":
            sorting_key = lambda x: x[1]

        grouping_key = lambda x: f"(default: no group)"
        if grouping_strategy == "by_cost_bucket":
            grouping_key = cost_bucket

        # Group resulting programs into cost buckets, and sort each group by increasing difficulty.

        toc_data: Dict[str, AssessedPrograms] = defaultdict(list)
        for (cost, program) in self.assessed_programs:
            toc_data[grouping_key(cost)].append((cost, program))
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
                program_info = self.programs[program_name]
                title = f"Program `{program_name}` (learning cost {cost})"
                toc.append(f"    - [`{program_name}`](#{title_to_slug(title)})")
                contents.append(f"\n### {title}")
                contents.append(f"\n```python\n{add_line_numbers(program_info['source'])}\n```")
                contents.append("\n| Cost  | Taxon | Location |")
                contents.append("|" + "----|" * 3)
                items = sorted(
                    program_info["taxons"].items(),
                    key=lambda x: f"~{x[0]}" if x[0].startswith("metadata/") else x[0],
                )
                for (taxon_name, spans) in items:
                    taxon_cost = self.taxon_cost(taxon_name)
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

        remainder = len(self.programs)
        summary: List[str] = [f"\n# Summary"]
        summary.append(programs_to_html(f"{remainder} initially", list(self.programs)))
        for (i, command) in enumerate(self.commands, 1):
            action = f"operation {i} ({command['operation']})"
            removed = len(command.get("filtered_out", []))
            remainder -= removed
            summary.append(
                programs_to_html(
                    f"{remainder} remaining after {action} has filtered out {removed} programs",
                    command.get("filtered_out", []),
                )
            )

        return "\n".join(toc + contents + summary)


if __name__ == "__main__":
    ast = __import__("ast")
    json = __import__("json")
    program_path = Path("../algo/programs")
    rec = Recommendations(
        commands=ast.literal_eval(Path(f"{program_path}_pipe.py").read_text()),
        db=json.loads(Path(f"{program_path}_db.json").read_text()),
        base_path=program_path.parent,
    )
    rec.run_pipeline()
    output_path = Path(f"{program_path}_recommendations.md")
    output_path.write_text(rec.get_markdown())
    print(f"Dumped: {output_path.resolve()}.\n")
