# Tag databases

Depending on the extension of `DB_NAME` (either `".json"` or `".sqlite"`), the command:

```
paroxython collect -o DB_NAME DIRECTORY
```

... will create two kinds of databases, each with their own purpose.

## The JSON tag database

It is this type of so-called NoSQL database that Paroxython draws upon to recommend programs. Its schema is:

```json
{
    "programs": {
        "program_1.py" : {
            "timestamp": "1970-01-01",
            "source": "print('hello')\nprint('world')\n",
            "labels": {
                "label_1": [[span_start_1, span_end_1], ...],
                ...
            },
            "taxa: {
                "taxon_1": [[span_start_1, span_end_1], ...],
                ...
            }
        },
        ...
    }
    "labels": {
        "label_1": ["program_1.py", "program_2.py", ...],
        ...
    },
    "taxa": {
        "taxon_1": ["program_1.py", "program_2.py", ...],
        ...
    },
    "importations": {
        "program_1.py": ["program_2.py", "program_3.py", ...],
        ...
    },
    "exportations": {
        "program_1.py": [],
        "program_2.py": ["program_1.py", ...],
        ...
    }
}
```

As an example, take a look on the [JSON tag database](https://repo/examples/simple/programs_db.json) of the Python Wiki's [21 simple programs](https://repo/examples/simple/programs).

## The SQLite tag database

This kind of database is fundamentally agnostic, but lends itself quite well to statistics. Its schema is:

```sql
CREATE TABLE program (
    program TEXT PRIMARY KEY,
    timestamp TEXT,
    source TEXT
);
CREATE TABLE label (
    -- use rowid as primary key
    label TEXT,
    label_prefix TEXT,
    label_suffix TEXT,
    span TEXT,
    span_start INTEGER,
    span_end INTEGER,
    program TEXT,
    FOREIGN KEY (program) REFERENCES program (program)
);
CREATE TABLE taxon (
    -- use rowid as primary key
    taxon TEXT,
    span TEXT,
    span_start INTEGER,
    span_end INTEGER,
    program TEXT,
    FOREIGN KEY (program) REFERENCES program (program)
);
```

Having a relational version of the tag database means that it can be queried with SQL. Here is an example which returns the 20 most frequent taxa:

```sql
SELECT taxon, count(*) AS occurrences
FROM taxon
GROUP BY taxon
ORDER BY occurrences DESC
LIMIT 20
```

More complex, a query comparing the number of occurrences of the loops `for` and `while`:

```sql
SELECT (CASE SUBSTR(taxon, 11, 3) -- extract either "for" or "whi"
            WHEN "for" THEN "for" -- and replace it either by... itself
            ELSE "while" -- or by the complete name of the loop
        END) AS loop,
       COUNT(*) AS occurrences
FROM taxon
WHERE taxon LIKE "flow/loop/for%"
   OR taxon LIKE "flow/loop/while%"
GROUP BY SUBSTR(taxon, 0, 14) -- cut the taxon three characters after "flow/loop/"
```

In theory, the relational database can also be used to select programs according to certain criteria:

```sql
SELECT
    taxon,
    program,
    group_concat(span, ", ") AS spans,
    source
FROM program
JOIN taxon USING (program)
WHERE taxon GLOB "type/non_sequence/dictionary/*"
GROUP BY taxon, program
```

On the provided [simple programs](https://repo/examples/simple/programs), the execution yields:

![](../resources/sql_query_example.png)

Note however that the same list of programs (with the nice addition of learning costs) could have been obtained by feeding the function `paroxython.recommend_programs.Recommendations.run_pipeline` with an elementary command:

```python
    {
        "operation": "include",
        "data": ["type/non_sequence/dictionary/"]
    }
```

So, although SQL should be familiar to almost everyone in our target audience, and might “make complex things possible”, as far as filtering is concerned, our minimalistic schema arguably does not ”make simple things simple” (to paraphrase Alan Kay). Some denormalization should ease the process, but so far we have prioritized the development of the pipeline system.

.. warning::
	Currently, the relational database is better suited for making statistics than recommendations.
