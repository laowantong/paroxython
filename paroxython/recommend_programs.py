import json
import subprocess
from ast import literal_eval
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

from assess_learning_costs import LearningCostAssessor
from filter_programs import ProgramFilter
from goodies import add_line_numbers, title_to_slug
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
        self.recommended_programs = program_filter.recommended_programs
        self.imparted_knowledge = program_filter.imparted_knowledge

        # hide the ugliness of dynamic method calls by defining an ad hoc function
        self.method = lambda method_name, *args: getattr(program_filter, method_name)(*args)

        # copy locally some attributes and methods or a LearningCostAssessor instance
        self.assess_costs = LearningCostAssessor(self.imparted_knowledge)
        self.assess_costs.set_cost_assessment_strategy(pipeline["cost_assessment_strategy"])
        self.taxon_cost = self.assess_costs.taxon_cost

    def run_pipeline(self) -> None:
        """Evolve recommended programs, imparted knowledge and log accross pipeline processes."""

        current_count = len(self.recommended_programs)
        self.log = {"initially": current_count}

        # Execute sequentially all the processes of the pipeline
        for p in self.processes:

            # The names or patterns fed to a process can either be a list of strings...
            strings = p["source"]
            if not isinstance(strings, list):  # ... or a shell command printing them on stdout
                strings = subprocess.run(
                    str(p["source"]).format(base_path=self.base_path),  # str() needed by mypy
                    capture_output=True,
                    encoding="utf-8",
                    shell=True,
                ).stdout.split("\n")

            # If needed, replace the resulting strings by the matched names of programs or taxons
            if p["name_or_pattern"] == "pattern":
                strings = self.method("patterns_to_{programs_or_taxons}".format(**p), strings)

            # Apply to them a method whose name depends on both the operation and the name category
            self.method("{operation}_{programs_or_taxons}".format(**p), strings)

            # Update the statistics of the filter state for the last operation
            (previous_count, current_count) = (current_count, len(self.recommended_programs))
            key = "filtered out by {operation}/{programs_or_taxons}/{name_or_pattern}".format(**p)
            self.log[key] = previous_count - current_count

        self.log["remaining"] = len(self.recommended_programs)
        self.assessed_programs = self.assess_costs(self.recommended_programs)

    def get_markdown(self, section_group_limit=5) -> str:
        display_count = lambda n: f"{n:3} program" + ("" if n == 1 else "s")
        n = len(self.recommended_programs)
        toc_data: Dict[int, ProgramNames] = defaultdict(list)
        for (cost, program_name) in self.assessed_programs:
            toc_data[cost].append(program_name)
        toc: List[str] = ["# Table of contents"]
        contents: List[str] = [f"# {display_count(n)}"]
        must_detail = True
        remainder = len(self.recommended_programs)
        for (cost, program_names) in toc_data.items():
            if must_detail:
                if len(program_names) >= section_group_limit:
                    title = f"{display_count(len(program_names))} of learning cost {cost}"
                    remainder -= len(program_names)
                else:
                    title = f"{display_count(remainder)} of greater learning costs"
                    must_detail = False
                toc.append(f"- [`{title}`](#{title_to_slug(title)})")
                contents.append(f"\n## {title}")
            for program_name in program_names:
                title = f"Program `{program_name}` (learning cost {cost})"
                toc.append(f"    - [`{program_name}`](#{title_to_slug(title)})")
                contents.append(f"\n### {title}")
                program_info = self.programs[program_name]
                contents.append(f"\n```python\n{add_line_numbers(program_info['source'])}\n```")
                contents.append("\n| Cost  | Taxon | Lines |")
                contents.append("|" + "----|" * 3)
                for (taxon_name, spans) in program_info["taxons"].items():
                    cost = self.taxon_cost(taxon_name)
                    all_span_strings = [str(Span(list(span))) for span in spans]
                    if len(all_span_strings) > 7:
                        n = len(all_span_strings) - 4
                        span_string = ", ".join(all_span_strings[:4]) + f" and {n} more"
                    else:
                        span_string = ", ".join(all_span_strings)
                    contents.append(f"| {cost} | `{taxon_name}` | {span_string} |")
        summary: List[str] = ["\n# Quantitative summary"]
        for (description, count) in self.log.items():
            summary.append(f"- {display_count(count)} {description}.")
        return "\n".join(toc + contents + summary + [""])

    def dump(self, text):
        self.output_path.write_text(text)
        print(f"Dumped: {self.output_path.resolve()}")


if __name__ == "__main__":
    rec = Recommendations(Path("../algo/programs_pipe.py"))
    rec.run_pipeline()
    text = rec.get_markdown()
    rec.dump(text)
