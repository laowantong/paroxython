import json
import subprocess
from ast import literal_eval
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from assess_learning_costs import LearningCostAssessor
from filter_programs import ProgramFilter
from goodies import (
    add_line_numbers,
    title_to_slug_factory,
    enumeration_to_txt_factory,
    cost_interval,
    progress_printer,
)
from span import Span
from user_types import Pipeline, ProgramNames, AssessedPrograms, Tuple


class Recommendations:
    def __init__(self, pipeline_path: Path) -> None:

        # path to be passed to the shell commands, if any
        self.base_path = pipeline_path.parent

        # get data from the pipeline
        pipeline: Pipeline = literal_eval(pipeline_path.read_text())
        self.commands = pipeline["commands"]
        self.output_path = self.base_path / pipeline["output_path"]
        db = json.loads(Path(self.base_path / pipeline["input_path"]).read_text())

        # copy locally some attributes and methods or a ProgramFilter instance
        program_filter = ProgramFilter(db)
        self.programs = program_filter.db_programs
        self.selected_programs = program_filter.selected_programs
        self.imparted_knowledge = program_filter.imparted_knowledge

        # hide the ugliness of dynamic method calls by defining an ad hoc function
        self.method = lambda method_name, *args: getattr(program_filter, method_name)(*args)

        # copy locally some attributes and methods or a LearningCostAssessor instance
        self.assess_costs = LearningCostAssessor(self.imparted_knowledge)
        self.assess_costs.set_cost_assessment_strategy(pipeline["cost_assessment_strategy"])
        self.taxon_cost = self.assess_costs.taxon_cost

    def run_pipeline(self) -> None:
        """Evolve recommended programs, imparted knowledge and log accross pipeline commands."""

        current = set(self.programs)
        print(f"Processing {len(self.commands)} commands on {len(current)} programs.")

        # Execute sequentially all the commands of the pipeline
        for command in self.commands:

            # The names or patterns fed to a command can either be a list of strings...
            data = command["source"]
            if not isinstance(data, list):  # ... or a shell command printing them on stdout
                data = subprocess.run(
                    str(command["source"]).format(base_path=self.base_path),  # str() needed by mypy
                    capture_output=True,
                    encoding="utf-8",
                    shell=True,
                    check=True,
                ).stdout.split("\n")

            # If needed, replace the resulting strings by the matched names of programs or taxons
            if command["name_or_pattern"] == "pattern":
                data = self.method("patterns_to_{programs_or_taxons}".format(**command), data)

            # Apply to them a method whose name depends on both the operation and the name category
            self.method("{operation}_{programs_or_taxons}".format(**command), set(data))

            # Update the statistics of the filter state for the last operation
            (previous, current) = (current, set(self.selected_programs))
            command["filtered_out"] = sorted(previous - current)
            action = "{operation}/{programs_or_taxons}/{name_or_pattern}".format(**command)
            print(f"  {len(current)} programs remaining after executing {action}.")

        self.assessed_programs = self.assess_costs(self.selected_programs)

    def get_markdown(self, span_column_width=30) -> str:
        """Reiterate on the commands, now populated by the results, and output them."""

        # Define some helper functions.

        title_to_slug = title_to_slug_factory()
        spans_to_html = enumeration_to_txt_factory(span_column_width, "_imported_")
        by_cost_and_sloc = lambda x: (x[0], len(self.programs[x[1]]["source"].split("\n")))
        display_count = lambda n: f"{n} program" + ("" if n == 1 else "s")

        # Group resulting programs by cost interval, and sort each group by increasing difficulty.

        toc_data: Dict[str, AssessedPrograms] = defaultdict(list)
        for (cost, program) in self.assessed_programs:
            toc_data[cost_interval(cost)].append((cost, program))
        for costs_and_program_names in toc_data.values():
            costs_and_program_names.sort(key=by_cost_and_sloc)

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
                contents.append("\n| Cost  | Taxon | Lines |")
                contents.append("|" + "----|" * 3)
                for (taxon_name, spans) in sorted(program_info["taxons"].items()):
                    taxon_cost = self.taxon_cost(taxon_name)
                    s = spans_to_html(", ".join(str(Span(list(span))) for span in spans))
                    contents.append(f"| {taxon_cost} | `{taxon_name}` | {s} |")
                contents.append("---")

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
        for command in self.commands:
            action = "{operation}/{programs_or_taxons}/{name_or_pattern}".format(**command)
            removed = len(command["filtered_out"])
            remainder -= removed
            summary.append(
                programs_to_html(
                    f"{remainder} remaining after {action} has filtered out {removed} programs",
                    command["filtered_out"],
                )
            )

        return "\n".join(toc + contents + summary)

    def dump(self, text):
        self.output_path.write_text(text)
        print(f"Dumped: {self.output_path.resolve()}")


if __name__ == "__main__":
    rec = Recommendations(Path("../algo/programs_pipe.py"))
    rec.run_pipeline()
    text = rec.get_markdown()
    rec.dump(text)
