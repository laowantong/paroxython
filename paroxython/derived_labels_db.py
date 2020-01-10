import sqlite3
from collections import defaultdict

from user_types import Label, Labels, LabelsSpans, Query
from span import Span


class DB:

    tables = ("main", "nest")
    main_columns = (
        # use rowid as primary key:
        "name TEXT",
        "name_prefix TEXT",
        "name_suffix TEXT",
        "span TEXT",
        "span_start INTEGER",
        "span_end INTEGER",
    )
    main_creation_query = f"CREATE TABLE main ({','.join(main_columns)})"
    main_update_query = f"INSERT INTO main VALUES ({','.join('?' * len(main_columns))})"
    nest_creation_query = """
        CREATE TABLE nest AS
        SELECT t1.name AS name_1,
               t1.name_prefix AS name_prefix_1,
               t1.name_suffix AS name_suffix_1,
               t1.span AS span_1,
               t1.span_start AS span_start_1,
               t1.span_end AS span_end_1,
               t2.name AS name_2,
               t2.name_prefix AS name_prefix_2,
               t2.name_suffix AS name_suffix_2,
               t2.span AS span_2,
               t2.span_start AS span_start_2,
               t2.span_end AS span_end_2
        FROM main t1
        JOIN main t2 ON (t1.rowid != t2.rowid
                        AND t1.span_start < t1.span_end
                        AND t1.span_start <= t2.span_start
                        AND t2.span_end <= t1.span_end)
    """

    def __init__(self):
        self.c = sqlite3.connect(":memory:")

    def create(self, labels: Labels) -> None:
        self.c.execute(DB.main_creation_query)
        self.update(labels)
        self.c.execute(DB.nest_creation_query)
        # for row in self.c.execute("SELECT * from main"):
        #     print(row)
        # print("-" * 80)
        # for row in self.c.execute("SELECT * FROM nest"):
        #     print(row)

    def read(self, query: Query) -> Labels:
        groups: LabelsSpans = defaultdict(list)
        for (label_name, start, end) in self.c.execute(query):
            groups[label_name].append(Span([start, end]))
        return [Label(*item) for item in groups.items()]

    def update(self, labels: Labels) -> None:
        values = []
        for (name, spans) in labels:
            for span in spans:
                (name_prefix, _, name_suffix) = name.partition(":")
                values.append(
                    (  # fmt: off
                        name,
                        name_prefix,
                        f":{name_suffix}",
                        str(span),
                        span.start,
                        span.end,
                    )  # fmt: on
                )
        self.c.executemany(DB.main_update_query, values)

    def delete(self) -> None:
        for table in DB.tables:
            self.c.execute(f"DROP TABLE {table}")
