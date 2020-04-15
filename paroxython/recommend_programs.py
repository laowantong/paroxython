import json
import subprocess
from ast import literal_eval
from pathlib import Path

from filter_programs import ProgramFilter
from user_types import Pipeline


def recommend_programs(pipeline_path: Path):
    """Read and execute a pipeline of processes and dump the resulting recommendations."""
    pipe: Pipeline = literal_eval(pipeline_path.read_text())
    base_path = pipeline_path.parent  # to be passed to the shell commands
    dbf = ProgramFilter(json.loads(Path(base_path / pipe["input_path"]).read_text()))
    current_count = len(dbf.recommended_programs)

    # Execute sequentially all the processes in the pipeline
    for process in pipe["processes"]:

        # Hide the ugliness of dynamic method calls by defining an ad hoc function
        method_call = lambda template, *args: getattr(dbf, template.format(**process))(*args)

        # The names or patterns fed to a process can either be a list of strings...
        strings = process["source"]
        if not isinstance(strings, list):  # ... or a shell command printing them on stdout
            strings = subprocess.run(
                str(process["source"]).format(base_path=base_path),  # str() makes mypy happy
                capture_output=True,
                encoding="utf-8",
                shell=True,
            ).stdout.split("\n")

        # If needed, replace the resulting strings by the matched names of programs or taxons
        if process["name_or_pattern"] == "pattern":
            strings = method_call("patterns_to_{programs_or_taxons}", strings)

        # Apply to them a method whose name depends on both the operation and the name category
        method_call("{operation}_{programs_or_taxons}", strings)

        # Update the statistics of the filter state for the last operation
        (previous_count, current_count) = (current_count, len(dbf.recommended_programs))
        key = "filtered out by {operation}/{programs_or_taxons}/{name_or_pattern}".format(**process)
        dbf.log[key] = previous_count - current_count

    # Sort the recommendations by increasing costs and dump them
    dbf.set_cost_computation_strategy(pipe["cost_computation_strategy"])
    result = dbf.get_markdown()
    if pipe.get("output_path"):
        output_path = base_path / pipe["output_path"]
        print(f"Output path: {output_path.resolve()}")
        output_path.write_text(result)
    return result


if __name__ == "__main__":
    recommend_programs(Path("../algo/programs_pipe.py"))
