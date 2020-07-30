"""
## Bird view

First, scroll the navigation panel until the whole program structure appear (depending on your browser, you may need to click on it and use arrow keys).

navigation panel

In the diagram on the left, Python modules appear in yellowish (extension `".py"` omitted), input files and folders in reddish, and output files and databases in green.

### First step: tagging a collection of programs

`source files` (Browse a copy of [wiki.python.org simple programs](https://github.com/laowantong/paroxython/blob/master/examples/simple/programs) on GitHub)
:   It all starts with the folder you dig into when you need a Python program for your students, to use it either as an example or an exercise.

`paroxython.preprocess_source`
:   Takes a source code as an input and returns it without comments, docstrings, blank lines, etc.

`paroxython.list_programs`
:	Walks this folder and returns the list of its source codes, prepared with the help of:

`paroxython.flatten_ast`
:   todo

`spec.md` (Browse [default specifications](https://github.com/laowantong/paroxython/blob/master/paroxython/resources/spec.md) on GitHub)
:   todo

`paroxython.parse_program`
:   todo

`paroxython.label_programs`
:   todo

`taxonomy.tsv` (Browse [default taxonomy](https://github.com/laowantong/paroxython/blob/master/paroxython/resources/taxonomy.tsv) on GitHub)
:   todo

`paroxython.map_taxonomy`
:   todo

`paroxython.make_db`
:   todo

`*_db.json`
:   todo

`*_db.sqlite`
:   todo

### Second step: getting program recommendations

`paroxython.compare_spans`
:   todo

`paroxython.normalize_predicate`
:   todo

`*_pipe.py`
:   todo

`paroxython.filter_programs`
:   todo

`paroxython.assess_costs`
:   todo

`paroxython.recommend_programs`
:   todo

`*_recommendations.md`
:   todo

Over the years, you have accumulated dozens of programs, some suitable for beginners, others requiring more advanced knowledge.

to show or have your students write a program illustrating a particular concept.


a folder containing all the programs you have prepared for your students, and from which you would like to get recommendations.

## Glossary

- (Manual) hint:
- Label:
- Span:
- Tag:
- Taxon:
- Taxonomy:
- Criterion:
- Pattern:
- Data:
- (Semantic) triple:
- Predicate:
- Command:
- Pipeline:

## Helper programs

Currently, please don't expect the same level of code quality, documentation and testing than those of the user-facing parts of this package.

[`build_pdoc.py`](https://github.com/laowantong/paroxython/blob/master/helpers/build_pdoc.py)
:   Builds this documentation with the excellent [pdoc3](https://pdoc3.github.io/pdoc/), and applies a number of patches to tailor the result to our needs.

[`context.py`](https://github.com/laowantong/paroxython/blob/master/helpers/context.py)
:   todo

[`draw_flow.py`](https://github.com/laowantong/paroxython/blob/master/helpers/draw_flow.py)
:   Generates the diagrams on the present page and `paroxython.filter_programs`. Automatically called by `build_doc.py`.

[`example.sql`](https://github.com/laowantong/paroxython/blob/master/helpers/example.sql)
:   todo

[`make_compare_spans.py`](https://github.com/laowantong/paroxython/blob/master/helpers/make_compare_spans.py)
:   Generates the Python module `paroxython.compare_spans`. Must be launched manually.

[`make_dummy_db.py`](https://github.com/laowantong/paroxython/blob/master/helpers/make_dummy_db.py)
:   Generates [`taxa_and_programs.txt`](https://github.com/laowantong/paroxython/blob/master/examples/dummy/taxa_and_programs.txt) and, from this file, [`programs_db.json`](https://github.com/laowantong/paroxython/blob/master/examples/dummy/programs_db.json), used as a dummy example in various tests.

[`make_programming_idioms_folder.py`](https://github.com/laowantong/paroxython/blob/master/helpers/make_programming_idioms_folder.py)
:   Populates the example directory [`idioms/programs`](https://github.com/laowantong/paroxython/blob/master/examples/dummy/idioms/programs), with a broad variety of code snippets snapshotted from the amazing repository [Programming Idioms](https://www.programming-idioms.org) of Valentin Deleplace. More info in the directory [`read_me.md`](https://github.com/laowantong/paroxython/blob/master/examples/idioms/read_me.md).

[`parse_syllabus.py`](https://github.com/laowantong/paroxython/blob/master/helpers/parse_syllabus.py)
:   todo

[`print_taxon_patterns.py`](https://github.com/laowantong/paroxython/blob/master/helpers/print_taxon_patterns.py)
:   todo

[`reformat_spec.py`](https://github.com/laowantong/paroxython/blob/master/helpers/reformat_spec.py)
:   todo

[`suggest_regex.py`](https://github.com/laowantong/paroxython/blob/master/helpers/suggest_regex.py)
:   todo


## Implementation notes

### User types

Paroxython makes heavy use of Python 3.5+ [type hints](https://docs.python.org/3/library/typing.html). They are documented directly in the source code. Browse [user_types.py](https://github.com/laowantong/paroxython/blob/master/paroxython/user_types.py) on GitHub.

### Default argument trick

Several functions or methods declare a compiled and bound regex pattern as an optional argument (see `paroxython.normalize_predicate.normalize_predicate` for an example). Such arguments are not meant to be provided by the caller. Their default value will be used systematically, with the benefit of being evaluated only once. This is arguably better for both performance and encapsulation. More details on [Stack Overflow](https://stackoverflow.com/a/30688691/173003).
"""
