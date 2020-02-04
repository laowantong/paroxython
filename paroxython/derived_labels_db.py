import sqlite3
from collections import defaultdict
from contextlib import suppress

from regex import match, compile  # type: ignore

from span import Span
from user_types import Label, Labels, LabelsSpans, Query


class DB:

    columns = (
        # use rowid as primary key:
        "name TEXT",
        "name_prefix TEXT",
        "name_suffix TEXT",
        "span TEXT",
        "span_start INTEGER",
        "span_end INTEGER",
        "path TEXT",
    )
    creation_query = f"CREATE TABLE t ({','.join(columns)})"
    update_query = f"INSERT INTO t VALUES ({','.join('?' * len(columns))})"
    addition_query = "CREATE TABLE t_{0} AS SELECT * FROM t WHERE name_prefix = '{0}'"
    prerequisites = compile(r"(?m)\b(?:FROM|JOIN) t_(\w+)").findall

    def __init__(self):
        connexion = sqlite3.connect(":memory:")
        connexion.create_function("regexp", 2, lambda rex, s: bool(match(rex, s)))
        self.c = connexion.cursor()

    def create(self, labels: Labels) -> None:
        self.c.execute(DB.creation_query)
        self.update(labels)
        self.added_table_labels = defaultdict(int)

    def read(self, query: Query) -> Labels:
        groups: LabelsSpans = defaultdict(list)
        # Uncomment the following lines for executing multi-queries,
        # including for instance the creation of a temporary table.
        #
        # with suppress(ValueError):
        #     i = query.rindex("\n\nSELECT")
        #     self.c.executescript(query[:i])
        #     query = query[i:]
        for label_name in DB.prerequisites(query):
            if label_name not in self.added_table_labels:
                self.c.execute(DB.addition_query.format(label_name))
            self.added_table_labels[label_name] += 1
        for (name_prefix, name_suffix, span_string, path) in self.c.execute(query):
            label_name = f"{name_prefix}:{name_suffix}" if name_suffix != "" else name_prefix
            span = span_string.split("-")
            span[0] = f"{span[0]}:{path}"
            groups[label_name].append(Span(span))
        return [Label(*item) for item in groups.items()]

    def update(self, labels: Labels) -> None:
        values = []
        for (name, spans) in labels:
            for span in spans:
                (prefix, _, suffix) = name.partition(":")
                values.append((name, prefix, suffix, str(span), span.start, span.end, span.path))
        self.c.executemany(DB.update_query, values)

    def delete(self) -> None:
        self.c.execute("DROP TABLE t")
        for label_name in self.added_table_labels:
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
