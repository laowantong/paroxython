import sqlite3
from collections import defaultdict
from typing import Dict, Callable

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

    def __init__(self):
        self.c = sqlite3.connect(":memory:")
        self.c.create_function("regexp", 2, lambda rex, s: bool(regex.match(rex, s)))

    def create(
        self, labels: Labels, creation_query: str = f"CREATE TABLE t ({','.join(columns)})"
    ) -> None:
        self.c.execute(creation_query)
        self.update(labels)
        self.added_table_labels: Dict[LabelName, int] = defaultdict(int)

    def read(
        self,
        query: Query,
        prerequisites: Callable = regex.compile(r"(?m)\b(?:FROM|JOIN) t_(\w+)").findall,
        addition_query: str = "CREATE TABLE t_{0} AS SELECT * FROM t WHERE name_prefix = '{0}'",
    ) -> Labels:
        groups: LabelsSpans = defaultdict(list)
        for label_name in prerequisites(query):
            if label_name not in self.added_table_labels:
                self.c.execute(addition_query.format(label_name))
                self.c.commit()
            self.added_table_labels[label_name] += 1
        for (name_prefix, name_suffix, span_string, path) in self.c.execute(query):
            label_name = f"{name_prefix}:{name_suffix}" if name_suffix != "" else name_prefix
            span = span_string.split("-")
            groups[label_name].append(Span(int(span[0]), int(span[-1]), path))
        return [Label(*item) for item in groups.items()]

    def update(
        self,
        labels: Labels,
        update_query: str = f"INSERT INTO t VALUES ({','.join('?' * len(columns))})",
    ) -> None:
        values = []
        for (name, spans) in labels:
            for span in spans:
                (prefix, _, suffix) = name.partition(":")
                span_string = couple_to_string(span)
                values.append((name, prefix, suffix, span_string, span.start, span.end, span.path))
        self.c.executemany(update_query, values)

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
