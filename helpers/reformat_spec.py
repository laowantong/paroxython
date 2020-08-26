"""
Read the contents of resources/spec.md, normalize its formatting and write it back.

The following operations are carried out:

- The old clickable table of contents (if any) is replaced by a new one.
- The spaces and separators between sections are homogeneized.
- The SQL requests are reformatted (courtesy of the python-sqlparse library).
- The derivations of each feature (i.e., the features which it is derived from and into)
  are calculated and injected before its specification.

This code is executed each time tests/test_parse_program.py is called. Thus, although no
unit test is provided, any regression should be visible in the differences between two
versions of resources/spec.md.
"""

from collections import defaultdict
from functools import lru_cache

import regex  # type: ignore
import sqlparse

import context
from paroxython.goodies import title_to_slug_factory
from paroxython.parse_program import ProgramParser, find_all_features

title_to_slug = title_to_slug_factory()


def generate_toc(text):
    for match in regex.finditer(r"(?m)^(#{1,4}) (.+)", text):
        (hashtags, title) = match.groups()
        offset = "  " * (len(hashtags) - 1) + "- "
        slug = title_to_slug(title, deduplicate=True)
        yield f"{offset}[{title}](#{slug})"


def reformat_sql(match):
    s = sqlparse.format(
        match.group(1),
        reindent=True,
        keyword_case="upper",  # Limitation: https://github.com/andialbrecht/sqlparse/pull/501
        identifier_case="lower",
        indent_width=2,
    )
    s = s.replace("\n\n", "\n")
    s = regex.sub(r"\b(regexp|glob|inside)\b", lambda m: m.group().upper(), s)
    s = regex.sub(r"\b(PATH)\b", lambda m: m.group().lower(), s)
    return f"```sql\n{s}\n```"


def derivation_map(text):

    find_iter_derivations = regex.compile(
        r"""(?mx)
        name(_prefix)?\s(
            (=|==|REGEXP)\s"(?P<REQUIRED_LABEL_NAME>.+?\b)(:.*)?"
            |
            IN\s\(("(?P<REQUIRED_LABEL_NAME>.+?\b)(:.*)?"(.|\n)*?)+\)
            )
        |
        \b(FROM|JOIN)\st_(?P<REQUIRED_LABEL_NAME>\w+\b)
    """
    ).finditer

    def label_converter(label_patterns):
        @lru_cache(maxsize=None)
        def label_name_to_pattern(label_name):
            for label_pattern in label_patterns:
                if regex.fullmatch(label_pattern, label_name):
                    return label_pattern
            raise ValueError(
                f"Unable to match '{label_name}' with a known pattern. "
                f"If a section '#### Feature `{label_name}`' do exist in spec.md, "
                "check that the previous section has all the required subsections. "
                "If you have renamed this feature, check that you've thought to"
                f"rename its form `t_{label_name}` too."
            )

        return label_name_to_pattern

    derived_from = defaultdict(set)
    derived_into = defaultdict(set)
    all_features = find_all_features(text)
    label_name_to_pattern = label_converter([feature[0] for feature in all_features])
    sql_features = {
        label_pattern: i
        for (i, (label_pattern, language, _)) in enumerate(all_features)
        if language == "sql"
    }
    for (label_pattern, language, query) in all_features:
        if language != "sql":
            continue
        i = sql_features[label_pattern]
        for m in find_iter_derivations(query):
            derived_label_patterns = [
                label_name_to_pattern(x) for x in m.captures("REQUIRED_LABEL_NAME")
            ]
            derived_from[label_pattern].update(derived_label_patterns)
            for derived_label_pattern in derived_label_patterns:
                j = sql_features.get(derived_label_pattern)
                if j is not None and i < j:
                    raise ValueError(f"'{derived_label_pattern}' should precede '{label_pattern}'!")
                derived_into[derived_label_pattern].add(label_pattern)
    keys = set(derived_from).union(derived_into)
    result = {}
    for key in keys:
        result[key] = {}
        if key in derived_from:
            result[key]["⬆️"] = sorted(derived_from[key])
        if key in derived_into:
            result[key]["⬇️"] = sorted(derived_into[key])
    return result


def inject_derivations(text):
    for (key, entries) in derivation_map(text).items():
        new_section = [f"##### Derivations\n"]
        for (kind, features) in entries.items():
            for feature in features:
                slug = title_to_slug(f"Feature `{feature}`")
                new_section.append(f"[{kind} feature `{feature}`](#{slug})  ")
        new_section.append("\n")
        text = regex.sub(
            r"(?msx)^(\#{4}\s+Feature\s+`%s`.+?)^(?=\#{5}\s+Specification)" % regex.escape(key),
            r"\1" + "\n".join(new_section),
            text,
        )
    return text


def reformat_spec(spec_path):
    text = spec_path.read_text()
    toc = "\n".join(generate_toc(text))
    for m in regex.finditer(r"(?sm)^#### Feature (`.+?`).+?```(\w*)", text):
        if m[2] == "sql":
            toc = toc.replace(m[1], f"{m[1]} (SQL)")
    rule = "-" * 80 + "\n"
    text = regex.sub(r"(?m)^---+\n", "", text)
    text = regex.sub(r"(?m)^ +```", "```", text)
    text = regex.sub(r"(?ms).*?^(?=# )", fr"{toc}\n\n", text, count=1)
    text = regex.sub(r"(?m)\s+^(#+ .+)\s+", fr"\n\n\1\n\n", text)
    text = regex.sub(r"(?ms)^(\| Label \| .+?)(^\#{1,3} )", fr"\1{rule}\n\2", text)
    text = regex.sub(r"(?=\n\#{4} )", fr"\n{rule}", text)
    text = regex.sub(r"(?ms)^```sql\n(.+?)\n```", reformat_sql, text)
    text = regex.sub(r"(?ms)^\#{5} Derivations\n.+?^(?=\#{5} Specification)", "", text)
    text = inject_derivations(text)
    spec_path.write_text(text)


if __name__ == "__main__":
    reformat_spec(ProgramParser().spec_path)
