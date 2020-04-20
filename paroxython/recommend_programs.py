import json
import subprocess
from ast import literal_eval
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from assess_learning_costs import LearningCostAssessor
from filter_programs import ProgramFilter
from goodies import add_line_numbers, title_to_slug_factory, enumeration_to_txt_factory
from span import Span
from user_types import Pipeline, ProgramNames


class Recommendations:
    def __init__(self, pipeline_path: Path) -> None:

        # path to be passed to the shell commands, if any
        self.base_path = pipeline_path.parent

        # get data from the pipeline
        pipeline: Pipeline = literal_eval(pipeline_path.read_text())
        self.processes = pipeline["processes"]
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
        """Evolve recommended programs, imparted knowledge and log accross pipeline processes."""

        current = set(self.programs)
        print(len(current))

        # Execute sequentially all the processes of the pipeline
        for process in self.processes:

            # The names or patterns fed to a process can either be a list of strings...
            data = process["source"]
            if not isinstance(data, list):  # ... or a shell command printing them on stdout
                data = subprocess.run(
                    str(process["source"]).format(base_path=self.base_path),  # str() needed by mypy
                    capture_output=True,
                    encoding="utf-8",
                    shell=True,
                    check=True,
                ).stdout.split("\n")

            # If needed, replace the resulting strings by the matched names of programs or taxons
            if process["name_or_pattern"] == "pattern":
                data = self.method("patterns_to_{programs_or_taxons}".format(**process), data)

            # Apply to them a method whose name depends on both the operation and the name category
            self.method("{operation}_{programs_or_taxons}".format(**process), set(data))

            # Update the statistics of the filter state for the last operation
            (previous, current) = (current, set(self.selected_programs))
            process["filtered_out"] = sorted(previous - current)
            print(len(current))

        self.assessed_programs = self.assess_costs(self.selected_programs)

    def get_markdown(self, toc_group_limit=5, span_column_width=30) -> str:
        """Iterate on the processes, now populated by the results, and construct a string
        output."""

        title_to_slug = title_to_slug_factory()
        spans_to_html = enumeration_to_txt_factory(span_column_width, "_imported_")

        # Group resulting programs by cost

        toc_data: Dict[float, ProgramNames] = defaultdict(list)
        for (cost, program) in self.assessed_programs:
            toc_data[cost].append(program)

        # accumulate simultaneously the TOC and the contents

        def display_count(n):
            return f"{n} program" + ("" if n == 1 else "s")

        toc: List[str] = ["# Table of contents"]
        contents: List[str] = [f"# Recommended programs"]
        must_group_by_equal_costs = True
        remainder = len(self.selected_programs)

        for (cost, program_names) in toc_data.items():

            if must_group_by_equal_costs:
                if len(program_names) >= toc_group_limit:
                    title = f"{display_count(len(program_names))} of learning cost {cost}"
                    remainder -= len(program_names)
                else:
                    title = f"{display_count(remainder)} remaining"
                    must_group_by_equal_costs = False
                toc.append(f"- [`{title}`](#{title_to_slug(title)})")
                contents.append(f"\n## {title}")

            for program_name in program_names:
                program_info = self.programs[program_name]
                title = f"Program `{program_name}` (learning cost {cost})"
                loc = len(program_info["source"].split("\n"))
                toc.append(f"    - [`{program_name}` ({loc} lines)](#{title_to_slug(title)})")
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
        for process in self.processes:
            action = "{operation}/{programs_or_taxons}/{name_or_pattern}".format(**process)
            removed = len(process["filtered_out"])
            remainder -= removed
            summary.append(
                programs_to_html(
                    f"{remainder} remaining after {action} has filtered out {removed} programs",
                    process["filtered_out"],
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
