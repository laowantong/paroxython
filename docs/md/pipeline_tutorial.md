# Pipeline tutorial

How to get recommendations? This tutorial walks you through a series of little “teacher stories” to introduce the pipeline of commands used by Paroxython's recommendation system.

You “execute” this pipeline on command line with:

```
paroxython recommend -p 'path/to/your/pipe.py' 'path/to/your/programs/db.json'
```

## Covering your base(s)

The simplest pipeline has no command: it just lists the programs of your database, without any filter. This could produce a rather long document, since each source code is printed, along with a list of each and every taxon it implements. Here is the content of your `pipe.py`:

```python
[]
```

.. tip::
    The point is that the resulting list is sorted by increasing learning cost. This should give you a rough idea of the pedagogical angle of attack to adopt in your first classes.

## Imparting knowledge

### Tracking the progress of your course

Suppose that, in your first session, you have introduced your students to the `hello_world.py`, `wheat_and_chessboard.py` and `euler_005_smallest_multiple.py` programs. Not only Paroxython should no longer recommend these programs, but the cost of learning the associated concepts should be considered as zero when they are encountered again in the future.

```python
[
  {
    "operation": "impart",
    "data": [
      "hello_world.py",
      "wheat_and_chessboard.py",
      "euler_005_smallest_multiple.py",
    ],
  },
]
```

### Coming after another course

Suppose instead that you intervene after an introductory course given by a colleague. She gives you a folder (named `"CS_101"`), which contains the programs she has studied with her class. Since you are secretly in love, you assume, somewhat foolishly, that the concepts they implement are mastered by your new students.

```python
[
  {
    "operation": "impart",
    "data": "find CS_101 -path '*.py'",
  },
]
```

.. tip::
    As you can see, rather than maintaining a **list** of programs or concepts in the `"data"` field, you may provide a **string**. Paroxython will interpret it as a shell command, and expect it to print on `stdout` the required list of items (programs or taxa), one per line.

## Blacklisting programs

You want to filter out all programs reserved for an exam, or too complex, or not pedagogically interesting enough, or that could get you kicked out of your college, etc.

```python
[
  {
    "operation": "exclude",
    "data": [
      "fizzbuzz.py",
      "alpha_go.py",
      "hello_world_of_pain.py",
      "gob_s_program.py",
    ],
  },
]
```

## Concepts to be introduced later (or never)

For the time being, you don't want to be recommended any program requiring the concepts of recursivity (`def/subroutine/recursive`), dictionary (`type/non_sequence/dictionary`) or set (`type/non_sequence/set`).

```python
[
  {
    "operation": "exclude",
    "data": [
      "def/subroutine/recursive",
      "type/non_sequence",
    ],
  },
]
```

.. note::
    Paroxython relies on the last three characters of a `"data"` item to decide whether it is a
    Python program (ending with `".py"`) or a taxon (like here).

.. tip::
    Since the two latter taxa share a common prefix and Python doesn't provide other non-sequence
    type, it is enough to exclude all taxa starting with `type/non_sequence`.

## Concepts to be introduced now

Your next class will be devoted to conditional constructs. Thus, you need to go through programs featuring taxa prefixed by `flow/conditional` or even, why not, some conditional expressions (`operator/ternary`). The suggested programs do not necessarily have to implement both concepts at the same time, but at least one. Any other program will be rejected.

```python
[
  {
    "operation": "include",
    "data": [
      "flow/conditional",
      "operator/ternary",
    ],
  },
]
```

## Preparing an assignment

Basically, you provide Paroxython with a list of programs already studied in class, and it suggests new programs that implement only old concepts. This requires the exclusion of all programs featuring at least one concept that has not been seen in any of the programs already seen.

It may sound a little complicated, because it is. But don't panic. Remember that Paroxython always orders its recommendations by increasing cost. Thus, all you have to do is ask it to list the programs that have not been introduced yet. The programs you want to choose among will appear at the top of the results, under the zero-learning cost section. Moreover, inside each section, they will be sorted by increasing size ([SLOC](https://en.wikipedia.org/wiki/Source_lines_of_code)), which can be a reasonable proxy for their difficulty.

But in the end, you, the teacher, are the judge. Paroxython is not going to set up a test for you, let alone grade the answers. It is just here to remind you of some possibilities you might not have thought of at the right time, and to give you some confidence that the exercises require no concept you have not pre-introduced in class, which later on might save you some awkward conversations with your dear students.

Since this is the last filter in our tutorial, let's summarize what we've seen by chaining several commands together:

1. **Impart** the previous knowledge by extracting all the programs listed in the `"timeline.txt"` file that you update after each session. You can adapt the script [`parse_syllabus.py`](https://repo/helpers/parse_syllabus.py) to your own needs. If you wish, you can use the `base_path` variable, which represents the parent of the directory containing the programs of your personal database.
2. **Exclude** some irrelevant programs.
3. **Include** the concepts that you want to test during your exam.

```python
[
  {
    "operation": "impart",
    "data": "python helpers/parse_syllabus.py {base_path}/timeline.txt",
  },
  {
    "operation": "exclude",
    "data": [
      "foo.py",
      "bar.py",
      # "buzz.py",
    ],
  },
  {
    "operation": "include",
    "data": [
      "pattern/elements/accumulate",
      "topic/game",
      "type/sequence/list",
    ],
  },
]
```

.. tip::
    This command pipeline is _not_ a JSON file, but a Python program, or more restrictively a Python **expression**. As such, it offers several amenities you surely know and love: comments, trailing commas, r-strings (no need to double-escape backslashes in regexes!), etc. For security purposes, this file is not imported, but read as a text and evaluated by [`ast.literal_eval()`](https://docs.python.org/3/library/ast.html#ast.literal_eval).

This is the end of our pipeline tutorial. If you dare, [read on](#pipeline-documentation) for more advanced features (regular expressions, span algebra, semantic triples, negations).
