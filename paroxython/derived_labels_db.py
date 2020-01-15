import sqlite3
from collections import defaultdict

from user_types import Label, Labels, LabelsSpans, Query
from span import Span


class DB:

    columns = (
        # use rowid as primary key:
        "name TEXT",
        "name_prefix TEXT",
        "name_suffix TEXT",
        "span TEXT",
        "span_start INTEGER",
        "span_end INTEGER",
    )
    creation_query = f"CREATE TABLE t ({','.join(columns)})"
    update_query = f"INSERT INTO t VALUES ({','.join('?' * len(columns))})"

    def __init__(self):
        self.c = sqlite3.connect(":memory:")

    def create(self, labels: Labels) -> None:
        self.c.execute(DB.creation_query)
        self.update(labels)

    def read(self, query: Query) -> Labels:
        groups: LabelsSpans = defaultdict(list)
        for (name_prefix, name_suffix, span) in self.c.execute(query):
            label_name = f"{name_prefix}:{name_suffix}" if name_suffix != "" else name_prefix
            groups[label_name].append(Span(span.split("-")))
        return [Label(*item) for item in groups.items()]

    def update(self, labels: Labels) -> None:
        values = []
        for (name, spans) in labels:
            for span in spans:
                (name_prefix, _, name_suffix) = name.partition(":")
                values.append((name, name_prefix, name_suffix, str(span), span.start, span.end))
        self.c.executemany(DB.update_query, values)

    def delete(self) -> None:
        self.c.execute(f"DROP TABLE t")

    def __str__(self) -> str:  # pragma: no cover
        result = ["rowid\tname\tname_prefix\tname_suffix\tspan\tspan_start\tspan_end"]
        for row in self.c.execute("SELECT * FROM t"):
            result.append("\t".join(map(str, row)))
        return "\n".join(result)
