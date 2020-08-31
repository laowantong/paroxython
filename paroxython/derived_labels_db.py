"""An in-memory database collecting the labels of a given program.

### Main table

The database is not really relational. It merely consists in a table `t` where each row is a
distinct occurrence of every label featured by a given program. Initially, `t` is populated with
the labels found by the queries specified by a regular expression of `spec.md`.

The SQL queries are then executed, and the resulting labels (known as _derived_) inserted into `t`
as they are found.

Note that the results of a given SQL query may themselves be required by a subsequent SQL query.

#### Example

The following simple SQL query of `spec.md` finds the loops of a program. The resulting label names
(e.g., `"loop:while"`) consist in a fixed prefix `"loop"` and a suffix denoting the category of
the loop (either `"for"` or `"while"`).

```sql
SELECT "loop",
    name_prefix,
    span,
    path
FROM t
WHERE name_prefix IN ("for", "while")
GROUP BY path
```

The execution of this query comes after the evaluation of all regular expressions, in particular
those collecting the features `"for"` and `"while"`. It simply gathers them under the prefix
`"loop"`, and qualifies them by their category.

The resulting labels will later be used by other SQL queries to search for features such as
`"loop_with_break"`, `"loop_with_late_exit"`, `"loop_with_else"`, and so on.

### Subtables

For simplicity and performance reasons, a bunch of subtables are extracted on the fly from `t`.
Actually, every time a query relies on a non-existing table named `t_PREFIX`, this table is
dynamically created as the set of rows of `t` whose value on column `name_prefix` is `PREFIX`.

#### Example

The following SQL query of `spec.md` relies on the previous one to find the loops featuring a
`break` statement. It is more complicated, since it suffixes `"loop_with_break"` with the span of
the smallest enclosing loop. Anyway, it relies on the results of both the previous SQL query and a
trivial regular expression matching the `break` statements.

```sql
SELECT "loop_with_break",
    l.name_suffix,
    max(l.span_start) || "-" || min(l.span_end),
    max(l.path)
FROM t_loop l
JOIN t_break b ON (b.path GLOB l.path || "*-")
GROUP BY b.rowid
```

Instead of referring the corresponding rows in `t` (which would complicate the query), two
subtables restricted to them are referred, `t_loop` and `t_break`. For example, if a `t_loop`
subtable does not exist yet, the system extracts it from `t` by executing:

```sql
CREATE TABLE t_loop AS
SELECT *
FROM t
WHERE name_prefix = 'loop'
```

The newly created table is then available for all subsequent queries that may need it, which can
significantly speed up their execution.

### Note

Using views instead of tables turns out to be slightly slower. Also, for whatever mysterious
reason, several queries produce an incorrect result.
"""

import sqlite3
from collections import defaultdict
from typing import Any, Set, Callable, Dict

import regex  # type: ignore

from .goodies import couple_to_string, print_warning
from .user_types import Label, LabelName, Labels, Query, Span


class DerivedLabelsDatabase:

    columns = (
        # use rowid as primary key:
        "name TEXT",
        "name_prefix TEXT",
        "name_suffix TEXT",
        "span TEXT",
        "span_start INT",
        "span_end INT",
        "path TEXT",
    )
    """The structure of the main table `t`, consisting of the following columns:

    Column        | Type   | Description and example
    :-------------|:-------|:----------------------------------------------
    `rowid`       | `INT`  | Primary key (automatically generated)
    `name`        | `TEXT` | Complete name of the label, e.g.
                  |        | `"loop_with_early_exit:for:break"`
    `name_prefix` | `TEXT` | Its prefix (part before the first colon, here
                  |        | `"loop_with_early_exit"`
    `name_suffix` | `TEXT` | Its suffix (may contain one or more colons),
                  |        | here `"for:break"`
    `span`        | `TEXT` | Numbers of the first and last lines of the
                  |        | feature as a hyphen-separated string, e.g. `"2-8"`
    `span_start`  | `INT`  | Its first line number, here `2`
    `span_end`    | `INT`  | Its first line number, here `8`
    `path`        | `TEXT` | String encoding the beginning of the feature
                  |        | as its path from the root of the AST, e.g.
                  |        | `"3-5-3-0-1-2-2-1-"`
    """

    def __init__(self):
        self.c = sqlite3.connect(":memory:")
        self.c.create_function("regexp", narg=2, func=lambda rex, s: bool(regex.match(rex, s)))
        # References:
        # - https://www.sqlite.org/inmemorydb.html
        # - https://www.sqlite.org/lang_expr.html#regexp
        # - https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.create_function

    def create(
        self,
        labels: Labels,
        create_main_table: str = f"CREATE TABLE t ({','.join(columns)})",  # never provided
    ) -> None:
        """Create the main table and populate it with regex-specified labels.

        Args:
            labels (Labels): The label names and spans featured by a certain program. Only those
                specified by a regular expression in `spec.md` are included. It is the very purpose
                of this module to add the remaining ones, specified by a SQL query.
            create_main_table (str, optional): The SQL query creating the table. Not to be
                explicitly provided. Defaults to `f"CREATE TABLE t ({','.join(columns)})"`.
        """
        self.c.execute(create_main_table)
        self.update(labels)
        self.subtables: Set[LabelName] = set()

    def read(
        self,
        query: Query,
        prerequisites: Callable = regex.compile(r"(?m)\b(?:FROM|JOIN) t_(\w+)").findall,
        create_subtable: str = "CREATE TABLE t_{0} AS SELECT * FROM t WHERE name_prefix = '{0}'",
    ) -> Labels:
        r"""Apply the given SQL query to the currently known labels, and returns the new labels.

        Args:
            query (Query): The SQL specification of a certain feature, as defined in `spec.md`.
            prerequisites (Callable, optional): A function taking an SQL query, and returning the
                table names referred to in the FROM clause.
                [Not to be explicitly provided.](developer_manual/index.html#default-argument-trick)
                Defaults to `regex.compile(r"(?m)\b(?:FROM|JOIN) t_(\w+)").findall`.
            create_subtable (str, optional): The SQL query creating a subtable from a label prefix.
                Not to be explicitly provided.
                Defaults to `"CREATE TABLE t_{0} AS SELECT * FROM t WHERE name_prefix = '{0}'"`.

        Returns:
            Labels: The additional labels found by the given SQL query.

        Note:
            As a side-effect, create in the database any non-existing subtable of `t` referred to
            as a prerequisite.
        """
        # Parse the prerequisites of the query, and create the corresponding subtables if needed.
        for label_name in prerequisites(query):
            if label_name not in self.subtables:
                self.c.execute(create_subtable.format(label_name))
            self.subtables.add(label_name)
        self.c.commit()
        # Execute the query and return the resulting labels, deduplicated by (label_name, path).
        labels_spans: Dict[LabelName, Dict[Span, Any]] = defaultdict(dict)
        try:
            row_iterator = self.c.execute(query)
        except Exception as exception:  # pragma: no cover
            print_warning(f"problem in the following query:\n\n{query}\n")
            raise exception
        for (name_prefix, name_suffix, span_string, path) in row_iterator:
            label_name = f"{name_prefix}:{name_suffix}" if name_suffix != "" else name_prefix
            span = span_string.split("-")
            labels_spans[label_name][Span(int(span[0]), int(span[-1]), path)] = None
        return [Label(name, list(spans)) for (name, spans) in labels_spans.items()]

    def update(
        self,
        labels: Labels,
        update_query: str = f"INSERT INTO t VALUES ({','.join('?' * len(columns))})",
    ) -> None:
        """Insert a set of labels into the main table `t`.

        Args:
            labels (Labels): The labels to be inserted.
            update_query (str, optional): The SQL query inserting a row in `t`. Not to be
                explicitly provided. Defaults to `f"INSERT INTO t VALUES ({','.join('?' *
                len(columns))})"`.
        """
        rows = []
        for (name, spans) in labels:
            for span in spans:
                (prefix, _, suffix) = name.partition(":")  # split on the first colon
                span_string = couple_to_string(span)
                rows.append((name, prefix, suffix, span_string, span.start, span.end, span.path))
        self.c.executemany(update_query, rows)

    def delete(self) -> None:
        """Empty the database after having executed all the SQL queries."""
        self.c.execute("DROP TABLE t")
        for label_name in self.subtables:
            self.c.execute(f"DROP TABLE t_{label_name}")

    def __str__(self) -> str:  # pragma: no cover
        rows = ["name name_prefix name_suffix span span_start span_end path".split()]
        rows.extend(sorted(list(map(str, row)) for row in self.c.execute("SELECT * FROM t")))
        widths = list(map(len, [max(column, key=len) for column in zip(*rows)]))
        result = [""]
        for row in rows:
            result.append(" | ".join(s + " " * (w - len(s)) for (w, s) in zip(widths, row)))
        result[1:1] = ["-+-".join("-" * w for w in widths)]
        return "\n".join(result)
