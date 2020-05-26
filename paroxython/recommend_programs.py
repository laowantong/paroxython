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
    you a rough idea of the pedagogical angle of attack to adopt in your first classes.

### Imparted knowledge

- Suppose that, in your first session, you introduced your students to the `hello_world.py`,
`wheat_and_chessboard.py` and `euler_005_smallest_multiple.py` programs. Not only Paroxython should
no longer recommend these programs, but the cost of learning the associated concepts should be
considered as zero when they are encountered again in the future.

>>> [
...     {
...         "operation": "impart",
...         "source": [
...             "hello_world.py",
...             "wheat_and_chessboard.py",
...             "euler_005_smallest_multiple.py",
...         ],
...     },
... ]

- Suppose that you intervene after an introductory course given by a colleague. She gives you a
  folder (named `"CS_101"`), which contains the programs she has studied with her class. Since you
  are secretly in love, you assume, somewhat foolishly, that the concepts they implement are
  mastered by your new students.

>>> [
...     {
...         "operation": "impart",
...         "source": "find CS_101 -path '*.py'",
...     },
... ]

.. tip::
    As you can see, rather than maintaining a **list** of programs or concepts in the `"source"`
    field, you may provide a **string**. Paroxython will interpret it as a shell command, and
    expect it to print on `stdout` the required list of items (programs or taxons), one per line.

### Blacklisted programs

You want to filter out all programs reserved for an exam, or too complex, or not pedagogically
interesting enough, or that could get you kicked out of your college, etc.

>>> [
...     {
...         "operation": "exclude",
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
...         "source": [
...             "subroutine/recursive",
...             "type/non_sequence",
...         ],
...     },
... ]

.. note::
    Paroxython relies on the last three characters of a `"source"` item to decide whether it is a
    Python program (ending with `".py"`) or a taxon (like here).

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
...         "source": [
...             "flow/conditional",
...             "operator/ternary",
...         ],
...     },
... ]

### Preparing an assignment

Basically, you provide Paroxython with a list of programs already studied in class, and it suggests
new programs that implement only old concepts. This requires the exclusion of all programs
featuring at least one concept that has not been seen in any of the programs already seen.

It may sound a little complicated, because it is. But don't panic. Remember that Paroxython always
orders its recommendations by increasing cost. Thus, all you have to do is ask it to list the
programs that have not been introduced yet. The programs you want to choose among will appear at
the top of the results, under the zero-learning cost section. Moreover, inside each section, they
will be sorted by increasing size ([SLOC](https://en.wikipedia.org/wiki/Source_lines_of_code)),
which can be a reasonable proxy for their difficulty.

But in the end, you, the teacher, are the judge. Paroxython is not going to set up a test for you,
let alone grade the answers. It is just here to remind you of some possibilities you might not have
thought of at the right time, and to give you some confidence that the exercises require no concept
you have not pre-introduced in class, which later on might save you some awkward conversations with
your dear students.

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
...         "source": "python helpers/parse_syllabus.py {base_path}/timeline.txt",
...     },
...     {
...         "operation": "exclude",
...         "source": [
...             "foo.py",
...             "bar.py",
...             # "buzz.py",
...         ],
...     },
...     {
...         "operation": "include",
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
from typing import Dict, List, Optional, Tuple, Union

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
            operation = command.get("operation")
            if operation not in ("include", "exclude", "impart"):
                print_warning(f"operation {i} ({operation}) is ignored (unknown).")
                continue

            # Retrieve the patterns
            patterns = self.retrieve_patterns_from_source(command.get("source", []), operation, i)
            if not patterns:
                print_warning(f"operation {i} ({operation}) is ignored (no data).")
                continue

            # Compute the sets from which the program selection and knowledge will be updated
            (taxons, programs) = self.compute_new_taxons_and_programs(operation, patterns, i)

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

    def compute_new_taxons_and_programs(
        # fmt: off
        self,
        operation: Operation,
        patterns: List[str],
        i: int,
        # fmt: on
    ) -> Tuple[TaxonNameSet, ProgramNameSet]:
        """Compute the programs and the taxons targeted by the operation application."""
        new_taxons: TaxonNameSet = set()
        new_programs: ProgramNameSet = set()
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
                else:
                    (pattern_1, raw_predicate, pattern_2) = pattern
                    (predicate, negated) = normalize_predicate(raw_predicate)
                    programs = self.programs_of_triple(pattern_1, predicate, pattern_2)
                    if negated:
                        taxons_1 = self.get_taxons_from_taxon_pattern(pattern_1)
                        programs_1 = self.programs_of_taxons(taxons_1)
                        programs = programs_1 - programs
            else:
                print_warning(f"operation {i} pattern '{pattern}' is ignored (malformed).")
            new_taxons.update(taxons)
            new_programs.update(programs)
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
