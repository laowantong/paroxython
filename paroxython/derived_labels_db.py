import sqlite3
from collections import defaultdict
from typing import Dict

import regex  # type: ignore

from .goodies import couple_to_string
from .user_types import Label, LabelName, Labels, LabelsSpans, Query, Span


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
    prerequisites = regex.compile(r"(?m)\b(?:FROM|JOIN) t_(\w+)").findall

    def __init__(self):
        self.c = sqlite3.connect(":memory:")
        self.c.create_function("regexp", 2, lambda rex, s: bool(regex.match(rex, s)))

    def create(self, labels: Labels) -> None:
        self.c.execute(DB.creation_query)
        self.update(labels)
        self.added_table_labels: Dict[LabelName, int] = defaultdict(int)

    def read(self, query: Query) -> Labels:
        groups: LabelsSpans = defaultdict(list)
        for label_name in DB.prerequisites(query):
            if label_name not in self.added_table_labels:
                self.c.execute(DB.addition_query.format(label_name))
                self.c.commit()
            self.added_table_labels[label_name] += 1
        for (name_prefix, name_suffix, span_string, path) in self.c.execute(query):
            label_name = f"{name_prefix}:{name_suffix}" if name_suffix != "" else name_prefix
            span = span_string.split("-")
            groups[label_name].append(Span(int(span[0]), int(span[-1]), path))
        return [Label(*item) for item in groups.items()]

    def update(self, labels: Labels) -> None:
        values = []
        for (name, spans) in labels:
            for span in spans:
                (prefix, _, suffix) = name.partition(":")
                span_string = couple_to_string(span)
                values.append((name, prefix, suffix, span_string, span.start, span.end, span.path))
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
