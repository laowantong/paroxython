"""
# Getting recommendations

## Teacher stories

### Covering your base(s)

Our simplest pipeline has no command: it just lists the programs of your database, without any
filter. This could produce a rather long document, since each source code is printed, along with a
list of each and every taxon it implements.

>>> []

.. tip::
    The point is that the resulting list is sorted by increasing learning cost. This should give
    you a rough idea of the angle of attack to adopt in your first classes.

### Imparted knowledge

In your first session, you introduced your students to the `hello_world.py`,
`wheat_and_chessboard.py` and `euler_005_smallest_multiple.py` programs. Not only Paroxython should
no longer recommend these programs, but the cost of learning the associated concepts should be
considered as zero when they are encountered again in the future.

>>> [
...     {
...         "operation": "impart",
...         "programs_or_taxons": "programs",
...         "source": [
...             "hello_world.py",
...             "wheat_and_chessboard.py",
...             "euler_005_smallest_multiple.py",
...         ],
...     },
... ]

You intervene after an introductory course given by a colleague. She gives you a folder (named
`"CS_101"`), which contains the programs she has studied with her class. Since you are secretly in
love, you assume, somewhat foolishly, that the concepts they implement are mastered by your new
students.

>>> [
...     {
...         "operation": "impart",
...         "programs_or_taxons": "programs",
...         "source": "find CS_101 -path '*.py'",
...     },
... ]

.. tip::
    As you can see, rather than maintaining a **list** of programs or concepts in the `"source"`
    field, you may provide a **string**. Paroxython will interpret it as a shell command, and
    expect it to display on `stdout` the required list of items, one per line.

### Blacklisted programs

You want to filter out all programs reserved for an exam, or too complex, or not pedagogically
interesting enough, or that could get you kicked out of your college, etc.

>>> [
...     {
...         "operation": "exclude",
...         "programs_or_taxons": "programs",
...         "source": [
...             "fizzbuzz.py",
...             "alpha_go.py",
...             "hello_world_of_pain.py",
...             "gob_s_program.py",
...         ],
...     },
... ]

### Concepts to be introduced later (or never)

For the time being, you don't want to be recommended any program requiring the concepts of
recursivity (`subroutine/recursive`), dictionary (`type/non_sequence/dictionary`) or set
(`type/non_sequence/set`).

>>> [
...     {
...         "operation": "exclude",
...         "programs_or_taxons": "taxons",
...         "source": [
...             "subroutine/recursive",
...             "type/non_sequence",
...         ],
...     },
... ]

.. tip::
    Since the two latter taxons share a common prefix and Python doesn't provide other non-sequence
    type, it is enough to exclude all taxons starting with `type/non_sequence`.

### Concepts to be introduced now

Your next class will be devoted to conditional constructs. Thus, you need to go through programs
featuring taxons prefixed by `flow/conditional` or even, why not, some conditional expressions
(`operator/ternary`). The suggested programs do not necessarily have to implement both concepts at
the same time, but at least one. Any other program will be rejected.

>>> [
...     {
...         "operation": "include",
...         "programs_or_taxons": "taxons",
...         "source": [
...             "flow/conditional",
...             "operator/ternary",
...         ],
...     },
... ]

### Preparing an assignment

Basically, you provide Paroxython with a list of programs already studied in class, and it suggests
new programs that implement only old concepts. This requires the exclusion of all programs
featuring at least one concept that has not been seen in any of the programs already seen. It may
sound a little complicated, because it is. But don't panic. Remember that Paroxython always
orders its recommendations by increasing cost. All you have to do is ask it to list all the
programs that have not been introduced. The programs you are interested in will appear at the top
of the results, under the zero-learning cost section. Moreover, inside each section, they will be
sorted by increasing size ([SLOC](https://en.wikipedia.org/wiki/Source_lines_of_code)), which can
be a reasonable proxy for their difficulty. But in the end, you, the teacher, are the judge.
Paroxython will not select the exercises for your exam, let alone correct them. It is just there to
remind you of some possibilities that might not have occurred to you at the right time, and to
ensure that your exam contains only algorithmic features that you introduced in class, which might
save you some awkward conversations with your students later on.

Since this is the last filter in our tutorial, let's summarize what we've seen by chaining several
commands together:

1. **Impart** the previous knowledge by extracting all the programs listed in the `"timeline.txt"`
   file that you update after each session. You can adapt the script
   [`parse_syllabus.py`](https://github.com/laowantong/paroxython/blob/master/paroxython/helpers/parse_syllabus.py)
   to your own needs. If you wish, you can use the `base_path` variable, which represents the
   parent of the directory containing the programs of your personal database.
2. **Exclude** some irrelevant programs.
3. **Include** the concepts that you want to test during your exam.

>>> [
...     {
...         "operation": "impart",
...         "programs_or_taxons": "programs",
...         "source": "python helpers/parse_syllabus.py {base_path}/timeline.txt",
...     },
...     {
...         "operation": "exclude",
...         "programs_or_taxons": "programs",
...         "source": [
...             "foo.py",
...             "bar.py",
...             # "buzz.py",
...         ],
...     },
...     {
...         "operation": "include",
...         "programs_or_taxons": "taxons",
...         "source": [
...             "pattern/elements/accumulate",
...             "topic/game",
...             "type/sequence/list",
...         ],
...     },
... ]

.. tip::
    This command pipeline is _not_ a JSON file, but a Python program, or more restrictively a
    Python **expression**. As such, it offers several amenities you surely know and love: comments,
    trailing commas, r-strings, etc.

This is the end of our pipeline tutorial. Read on for more advanced features (negations, regular
expressions, semantic triples, span algebra) in the next section (coming soon).
"""

import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional

from typing_extensions import Literal

from .assess_costs import LearningCostAssessor
from .filter_programs import ProgramFilter
from .goodies import (
    add_line_numbers,
    cost_bucket,
    couple_to_string,
    enumeration_to_txt_factory,
    title_to_slug_factory,
)
from .user_types import AssessedPrograms, Command, JsonDatabase, ProgramNames


class Recommendations:
    def __init__(
        self,
        db: JsonDatabase,
        commands: Optional[List[Command]] = None,
        base_path: Optional[Path] = None,
        cost_assessment_strategy: Literal["zeno", "linear"] = "zeno",
    ) -> None:

        self.commands = commands or []
        self.base_path = base_path

        # copy locally some attributes and methods or a ProgramFilter instance
        program_filter = ProgramFilter(db)
        self.programs = program_filter.db_programs
        self.selected_programs = program_filter.selected_programs
        self.imparted_knowledge = program_filter.imparted_knowledge

        # hide the ugliness of dynamic method calls by defining an ad hoc function
        self.method = lambda method_name, *args: getattr(program_filter, method_name)(*args)

        # copy locally some attributes and methods or a LearningCostAssessor instance
        self.assess_costs = LearningCostAssessor(self.imparted_knowledge)
        self.assess_costs.set_cost_assessment_strategy(cost_assessment_strategy)
        self.taxon_cost = self.assess_costs.taxon_cost

    def run_pipeline(self) -> None:
        """Evolve recommended programs, imparted knowledge and log accross pipeline commands."""

        current = set(self.programs)
        print(f"\nProcessing {len(self.commands)} commands on {len(current)} programs.")

        # Execute sequentially all the commands of the pipeline
        for command in self.commands:

            # The patterns fed to a command can either be a list of strings...
            data = command["source"]
            if not isinstance(data, list):  # ... or a shell command printing them on stdout
                data = (
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

            # If needed, replace the resulting strings by the matched names of programs or taxons
            data = self.method("preprocess_{programs_or_taxons}".format(**command), data)

            # Apply to them a method whose name depends on both the operation and the name category
            self.method("{operation}_{programs_or_taxons}".format(**command), set(data))

            # Update the statistics of the filter state for the last operation
            (previous, current) = (current, set(self.selected_programs))
            command["filtered_out"] = sorted(previous - current)
            action = "{operation}/{programs_or_taxons}".format(**command)
            print(f"  {len(current)} programs remaining after executing {action}.")

        self.assessed_programs = self.assess_costs(self.selected_programs)

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
                contents.append("\n| Cost  | Taxon | Lines |")
                contents.append("|" + "----|" * 3)
                items = sorted(
                    program_info["taxons"].items(),
                    key=lambda x: f"~{x[0]}" if x[0].startswith("metadata/") else x[0],
                )
                for (taxon_name, spans) in items:
                    taxon_cost = self.taxon_cost(taxon_name)
                    s = spans_to_html(", ".join(map(couple_to_string, spans)))
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
            action = "{operation}/{programs_or_taxons}".format(**command)
            removed = len(command["filtered_out"])
            remainder -= removed
            summary.append(
                programs_to_html(
                    f"{remainder} remaining after {action} has filtered out {removed} programs",
                    command["filtered_out"],
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
