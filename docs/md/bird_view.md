# Bird view

This section mainly describes how the different parts of Paroxython (code, data, results) are integrated. For details on the functioning of an individual module, click its name: it refers to the documentation page. The input and output files are linked to real examples.

..tip::
    On a sufficiently large screen, scroll the navigation panel until the whole program structure appears (depending on your browser, you may need to click it and use arrow keys). The following short descriptions aim to make the explanations a bit more fluid by roughly following the requirement order (imported modules and input data), from top to bottom in the diagram. Python modules appear in yellowish (extension `".py"` omitted), input files and folders in reddish, and output files and databases in green.

## First stage: tagging a collection of programs

[`source files`](https://repo/examples/simple/programs) (click to browse a copy of Python Wiki's [21 simple programs](https://wiki.python.org/moin/SimplePrograms) on GitHub)
:   It all starts with the folder you dig into when you need a Python program for your students, to use it either as an example or an exercise.

`paroxython.preprocess_source`
:   These programs are not parsed exactly as they are. The may contain textual metadata (comments, docstrings, blank lines) which are not useful for the purpose of tagging their algorithmic features, and can be suppressed. Conversely, some of their lines may entirely consist of a hint manually added by the user to denote an all-encompassing feature (e.g., `topic:cryptography`). Such manual hints need to be “centrifugated”, i.e. moved to both ends of the source, making them open on the first line and close on the last line of code. This module deals with the cleaning and the centrifugation of a given program.

`paroxython.list_programs`
:    We are now able to walk through the `source files` and return the list of their preprocessed source codes.

`paroxython.flatten_ast`
:   The first stage of [static analysis](https://en.wikipedia.org/wiki/Static_program_analysis) often consists in constructing the [Abstract Syntax Tree](https://en.wikipedia.org/wiki/Abstract_syntax_tree) of the code to parse. Here, we go a step further by transforming this AST into a sequence of text lines, each one consisting of the whole path from the tree root to the current node. Some additional transformations are made on the fly, in order to simplify, or even make possible, the writing of regular expressions that match the algorithmic features we are interested in.

`spec.md` (click to browse the default specifications on GitHub)
:   This input file is quite special. It serves three distinct roles:

:    1. As its name suggests, it specifies what features to look for, and how to find them in a given source code. The specifications are expressed either as [regular expressions](https://en.wikipedia.org/wiki/Regular_expression) on the flattened version of the AST, or as [SQL](https://en.wikipedia.org/wiki/SQL) queries on the features found so far (either as a regular expression match or in the table resulting from a previous query).
    2. The [Markdown](https://en.wikipedia.org/wiki/Markdown) format (extension `".md"`) is an unusual choice for a specification file. The reason for such a deviation is that this file also acts as documentation. Each formal specification is illustrated with numerous examples, and possibly with explanations, warnings, links to prerequisite or derived features, etc.
    3. Finally, this file is also used as a test base. When [`test_parse_program.py`](https://repo/tests/test_parse_program.py) is executed, each specification is tested on the examples provided, and its outcome checked against the expected results.

`paroxython.derived_labels_db`
:   As they are found in a given source code, the features described by `spec.md` are stored in an in-memory database, as labels with a prefix, possibly a suffix, and a span (consisting of their first and last line numbers, as well as a unique identifier to pinpoint their precise location within the AST). The storage of these labels is used dynamically to search for so-called derived features, which themselves are necessarily specified by SQL queries.

`paroxython.parse_program`
:   This module mainly consists of a function which flattens a given (preprocessed) program, parses it along the specifications defined in `spec.md`, and returns the list of its labels with their spans, plus/minus those scheduled for addition/deletion.

    **Warning.** The binding of a regular expression-specified multi-line feature with its spans may reveal somewhat tricky. Make sure to understand the explanations of `paroxython.parse_program.get_bindings` in case your home-made regular expression yields unexpected results.

`paroxython.label_programs`
:   The main function of this module not only maps `paroxython.parse_program` on the list returned by `paroxython.list_programs`, transforming it into a list of _labelled_ programs, but tweaks all the labels which mark an importation of an “internal” module, _i.e_, a program belonging to this very list. For instance, a label `"import:my_program"` would be transformed into `"import_internally:my_program"`, while `"import:itertools"` would be left untouched.

`taxonomy.tsv` (click to browse the default taxonomy on GitHub)
:   The labels produced so far are nothing more than an intermediate result. A number of them have only been useful for deriving other labels, and can now be ignored. Those that remain must be transformed into taxa.
    A taxon is the structured version of one or more labels. For instance, the label `"if_without_else"` will maps onto the taxon `"flow/conditional/no_else"`, which conveniently tells us that a conditional without an else branch (`no_else`) is a subcase of a conditional (`conditional`), itself being a subcase of a control flow (`flow`).

    The file `taxonomy.tsv` is a simple two-columns associative TSV array which maps label _patterns_ onto taxa. Since some label patterns are rather long regular expressions, the columns are swapped: the _second_ column lists the labels patterns to search; the _first_ columns, the taxa to be substituted. For instance, the row:

    | Taxa (replacement patterns) | Labels (search patterns) |
    |:--|:--|
    | `flow/loop/exit/early/\1`[^match_group]  | `loop_with_early_exit:.+:(.+)` |

    ... will trigger the following transformations into taxa:

    `loop_with_early_exit:for:break`       ->   `flow/loop/exit/early/break`
    `loop_with_early_exit:while:break`     ->   `flow/loop/exit/early/break`
    `loop_with_early_exit:for:return`      ->   `flow/loop/exit/early/return`
    `loop_with_early_exit:while:return`    ->   `flow/loop/exit/early/return`
    `loop_with_early_exit:for:raise`       ->   `flow/loop/exit/early/raise`
    `loop_with_early_exit:while:raise`     ->   `flow/loop/exit/early/raise`

[^match_group]:
    In the replacement pattern, `"\1"` denotes the 1st captured group (in parentheses) of the search pattern.

`paroxython.map_taxonomy`
:   In addition to applying the transformations defined in `taxonomy.tsv` to a given list of labels, the main method of this module, `paroxython.map_taxonomy.Taxonomy.to_taxa`, deduplicates the resulting taxa.

    Indeed, a same feature is often described by several labels, for instance, the `for` loop of the following program:

        for x in range(10):
            print("foo")
            if bar(x):
                break

:   ... will be associated with no less than six labels (remember that most of them were only useful during the execution of `paroxython.derived_labels_db`):

    1. `"for_range:10"`
    1. `"loop_with_early_exit:for:break"`
    1. `"loop:for"`
    1. `"for:x"`
    1. `"loop_with_break:for"`
    1. `"node:For"`

    The last three of these are ignored, since they do not define any mapping in `taxonomy.tsv`. The remaining three are mapped respectively onto:

    1. `"flow/loop/for/arithmetic"`
    1. `"flow/loop/exit/early/break"`
    1. `"flow/loop"`

    The latter is a prefix of (at least) another one: as an overly broad categorization of the feature, it can be discarded. Only the former two will go into the deduplicated result: they indeed categorize the feature along two partially distinct dimensions (the iteration domain and the nature of the exit).

`paroxython.make_db`
:   This is the main user-facing module of the first stage, invoked on command line by:

        paroxython collect DIRECTORY

:   It walks through the input directory, labels its programs and maps these labels onto the default taxonomy (or yours). Along this process, the labels `"import_internally"`, calculated by `paroxython.label_programs`, are used to list, for each program, those of the input directory that it imports or by which it is imported (either directly or indirectly).

    Finally, the results are stored as a NoSQL (JSON) or relational (SQLite) database.

[`*_db.json`](https://repo/examples/simple/programs_db.json) (click to browse the tag database of [21 simple programs](https://repo/examples/simple/programs)).
:   Generated by `paroxython.make_db.TagDatabase.get_json` as a dictionary (or, in JSON parlance, _object_) with the following keys:

    - `"programs"`: maps each program path to the timestamp of its last modification, its cleaned up source code, the list of its labels with their poor[^poor_span] spans, and that of its taxa with their poor spans;
    - `"labels"`: maps each label to the programs that feature it;
    - `"taxa"`: maps each taxon to the programs that feature it;
    - `"importations"`: maps each program to the programs that import it;
    - `"exportations"`: maps each program to the programs by which it is imported.

    Note that the labels are not used thereafter: they are stored only for logging purposes.

[^poor_span]:
    The _poor_ span of a feature's occurrence is its span, deprived from the last member (location in the AST).


`*_db.sqlite`
:   An experimental relational version of the above JSON tag database. Also generated by `paroxython.make_db`, but currently unused. See `paroxython.make_db.TagDatabase.write_sqlite` for its schema and an example query. Not under version control.

## Second stage: getting recommendations

[`*_pipe.py`](https://repo/examples/simple/programs_pipe.py) (click to browse an example pipeline to be executed on the [database](https://repo/examples/simple/programs_db.json) of [21 simple programs](https://repo/examples/simple/programs))
:   To get program recommendations, you first create a pipeline, i.e., a Python file consisting in a list of filtering commands to be applied on a JSON tag database generated by `paroxython.make_db`. Each command is a dictionary with two keys:

:   - `"operation"`: a string among `"include"`, `"exclude"`, `"impart"` and `"hide"`, with an optional suffix `" any"` (implicit) or `" all"`.
    - `"data"`: either a string consisting in a shell command, or an heterogeneous list of _criteria_: patterns (matching either program paths or taxon names) or semantic triples (of the form subject, predicate, object).

:   The interpretation of a predicate is not immediate, and is the object of the next two modules.

`paroxython.compare_spans`
:   A dictionary of predicates listing all possible relations between two intervals \((x_1, x_2)\) and \((y_1, y_2)\). The keys of these predicates are expected to be used as the second term of a semantic triple expressing a relationship between the spans of two features. Generated by [`make_compare_spans.py`](https://repo/helpers/make_compare_spans.py).

`paroxython.normalize_predicate`
:   A thin layer between `paroxython.compare_spans` and `paroxython.filter_programs`, this function tries to recognize as a key a predicate given by the user. In the case the predicate is negative (e.g., `"not inside"`), strip it from the predicate (`"inside`"). Returns the corresponding lambda function along with a boolean indicating whether it was negated or not.

`paroxython.filter_programs`
:   Probably the most complex part of Paroxython. A filter instance is initialized with a JSON tag database of tagged programs. It is characterized by the state of the following attributes:

    - `"selected_programs"`: the programs to be recommended, initially all of them.
    - `"imparted_knowledge"`: the concepts (i.e., taxa) that have already been presented to your students, and therefore have a learning cost of zero. Initially empty.
    - `"hidden_taxa"` / `"hidden_programs"`: the programs and/or taxa you are not interested in seeing in the resulting tables. It's just a display thing, with no effect on the actual filtering. Initially empty.

    The filter responds to the pipeline commands sent to `paroxython.filter_programs.ProgramFilter.update_filter` by evolving the contents of these three sets.

`paroxython.assess_costs`
:   The costs in question are the learning costs. The final state of the imparted knowledge calculated by `paroxython.filter_programs` is used to initialize the constructor after all the pipeline commands have been executed. The main method `paroxython.assess_costs.LearningCostAssessor.__call__` is then invoked with the remaining recommended programs.

`paroxython.recommend_programs`
:   The user-facing module of the second stage, called on command line by:

        paroxython recommend -p pipeline_path DB_PATH

:   A simple wrapper around `paroxython.filter_programs.ProgramFilter`, with report capabilities. For each command of the pipeline, it checks the validity of its operation and data, and sends them to `paroxython.filter_programs.ProgramFilter.update_filter`. When the pipeline is exhausted, it invokes `paroxython.assess_costs.LearningCostAssessor.__call__` to compute the relevant learning costs.

:   At the end, a call to `paroxython.recommend_programs.Recommendations.get_markdown` creates a report of the results.

[`*_recommendations.md`](https://repo/examples/simple/programs_recommendations.md) (click to browse the report of the execution of the above [pipeline](https://repo/examples/simple/programs_pipe.py))
:   The final report sorts the recommended programs by increasing learning cost and SLOC, and group them into predefined cost intervals[^cost_bucket]. It includes a table of contents, and a summary of which program has been filtered at what stage of the pipeline execution.

[^cost_bucket]:
    The intervals are predefined as \([0, 0], ]0, 0.25[, [2^{i-2}, 2^{i-1}[, \dots\) for all natural numbers \(i\).

<!-- Fake paragraph to avoid the footnote back button to be misplaced -->
