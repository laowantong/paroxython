import json
from bisect import insort
from collections import defaultdict
from functools import lru_cache
from typing import Callable, Dict, List, Set

import regex  # type: ignore

from title_to_slug import title_converter
from user_types import (
    JsonDatabase,
    ProgramName,
    ProgramNames,
    ProgramNameSet,
    ProgramPatterns,
    TaxonName,
    TaxonNames,
    TaxonNameSet,
    TaxonPatterns,
)

HORIZONTAL_RULE = "-" * 80


class DatabaseFilter:
    """
    Mutate a set of program names accross various operations, or filters.

    Initialized with a DB of tagged programs constructed by make_db.py.
    The attribute program_names is considered as public, and maintains
    the current set of filtered program names.
    """

    def __init__(self, db: JsonDatabase) -> None:
        self.db = db
        self.program_names: ProgramNameSet = set(db["programs"])
        self.counts = {"initially": len(self.program_names)}

    def program_taxons(self, program_name):
        """Return the dictionary of taxons associated with a given program name."""
        return self.db["programs"][program_name]["taxons"]

    def update(self, *program_names: ProgramNames) -> None:
        "Update self.program_names, adding programs from all the given ones."
        self.program_names.update(*program_names)

    def intersection_update(self, *program_names: ProgramNames) -> None:
        "Update self.program_names, keeping only programs found in it and all the given ones."
        self.program_names.intersection_update(*program_names)

    def difference_update(self, *program_names: ProgramNames) -> None:
        "Update self.program_names, removing programs found in the given ones."
        self.program_names.difference_update(*program_names)

    def symmetric_difference_update(self, *program_names: ProgramNames) -> None:
        "Update self.program_names, keeping only programs found in either set, but not in both."
        self.program_names.symmetric_difference_update(*program_names)

    def complement_update(self):
        "Update self.program_names, taking only programs filtered out so far."
        self.program_names = set(self.db["programs"]).difference(self.program_names)

    def intersection(self, *program_names: ProgramNames) -> ProgramNameSet:
        "Return those of the given program names which are present in self.program_names."
        return self.program_names.intersection(*program_names)

    def filter_blacklisted_programs(self, patterns: ProgramPatterns) -> None:
        """Suppress from self.program_names all programs whose name matches any blacklisted pattern."""
        count = len(self.program_names)
        if patterns:
            match = regex.compile("|".join(patterns)).match
            acc: ProgramNameSet = set()
            for program_name in list(self.program_names):
                if match(program_name):
                    acc.add(program_name)
            self.program_names.difference_update(acc)
        self.counts["blacklisted"] = count - len(self.program_names)

    def filter_forbidden_taxons(self, patterns: TaxonPatterns) -> None:
        """Suppress from self.program_names all programs using any forbidden taxon."""
        count = len(self.program_names)
        if patterns:
            match = regex.compile("|".join(patterns)).match
            acc: ProgramNameSet = set()
            for (taxon_name, program_names) in self.db["taxons"].items():
                if match(taxon_name):  # this taxon is forbidden
                    acc.update(program_names)
            self.program_names.difference_update(acc)
        self.counts["tagged with a forbidden taxon"] = count - len(self.program_names)

    def filter_mandatory_taxons(self, patterns: TaxonPatterns) -> None:
        """Suppress from self.program_names all programs not using at least one mandatory taxon."""
        count = len(self.program_names)
        if patterns:
            matches = [regex.compile(row).match for row in patterns]
            acc: ProgramNameSet = set()
            for program_name in self.program_names:
                for match in matches:
                    for taxon_name in self.program_taxons(program_name):
                        if match(taxon_name):  # this mandatory taxon is used
                            break  # no need to test the other taxons of this program
                    else:  # this mandatory taxon is not used by this program
                        acc.add(program_name)
                        break  # no need to test the other mandatory taxons
            self.program_names.difference_update(acc)
        self.counts["not tagged with a mandatory taxon"] = count - len(self.program_names)

    def get_taxons_in_programs(self, patterns: ProgramPatterns) -> TaxonNameSet:
        """Return all taxons included in at least one program of the given list."""
        result: TaxonNameSet = set()
        if patterns:
            match = regex.compile("|".join(patterns)).match
            for program_name in self.program_names:
                if match(program_name):
                    result.update(self.program_taxons(program_name))
        return result

    def get_taxons_not_in_programs(self, patterns: ProgramPatterns) -> TaxonNameSet:
        """Return all taxons not included in any program of the given list."""
        result: TaxonNameSet = set(self.db["taxons"])
        if patterns:
            match = regex.compile("|".join(patterns)).match
            for program_name in self.program_names:
                if match(program_name):
                    result.difference_update(self.program_taxons(program_name))
        return result

    def get_extra_taxons(self, patterns: TaxonPatterns) -> Dict[ProgramName, TaxonNames]:
        """For each program, list those of its taxons which are not among the given taxons."""
        match = regex.compile("|".join(patterns)).match
        extra_taxon_names: Dict[ProgramName, TaxonNames] = {}
        for program_name in self.program_names:
            extra_taxon_names[program_name] = []
            for taxon_name in self.program_taxons(program_name):
                if not match(taxon_name):
                    insort(extra_taxon_names[program_name], taxon_name)
        return extra_taxon_names

    def get_lacking_taxons(self, patterns: TaxonPatterns) -> Dict[ProgramName, TaxonPatterns]:
        """For each program, list those of the given taxons that it does not include."""
        matches = [regex.compile(row).match for row in patterns]
        lacking_taxon_patterns: Dict[ProgramName, TaxonPatterns] = {}
        for program_name in self.program_names:
            lacking_taxon_patterns[program_name] = []
            for (match, wanted_taxon) in zip(matches, patterns):
                for taxon_name in self.program_taxons(program_name):
                    if match(taxon_name):  # this wanted taxon is used
                        break  # no need to test the other taxons of this program
                else:  # this wanted taxon is not used by this program
                    insort(lacking_taxon_patterns[program_name], wanted_taxon)
        return lacking_taxon_patterns

    def sort(self, criterium: Callable, reverse=False):
        """Generic program sort. Use the following helpers instead."""
        self.sorted_programs = sorted((criterium(p), p) for p in self.program_names)

    def sort_by_taxon_count(self, reverse=False):
        """Sort the programs by number of distinct taxons."""
        self.sort(lambda p: len(self.program_taxons(p)), reverse)

    def sort_by_line_count(self, reverse=False):
        """Sort the programs by SLOC count."""
        self.sort(lambda p: self.db["programs"][p]["source"].count("\n"), reverse)

    def sort_by_extra_taxon_count(self, taxons: TaxonPatterns, reverse=False):
        """Sort the programs by number of extra taxons wrt a given list."""
        extra_taxons = self.get_extra_taxons(taxons)
        self.sort(lambda p: len(extra_taxons[p]), reverse)

    def sort_by_lacking_taxon_count(self, taxons: TaxonPatterns, reverse=False):
        """Sort the programs by number of lacking taxons wrt a given list."""
        lacking_taxons = self.get_lacking_taxons(taxons)
        self.sort(lambda p: len(lacking_taxons[p]), reverse)

    def sort_by_distance(self, taxons: TaxonPatterns, reverse=False):
        """Sort the programs by number of extra and lacking taxons wrt a given list."""
        extra_taxons = self.get_extra_taxons(taxons)
        lacking_taxons = self.get_lacking_taxons(taxons)
        self.sort(lambda p: len(extra_taxons[p]) + len(lacking_taxons[p]), reverse)

    def get_markdown(self, section_group_limit=5) -> str:
        display_count = lambda n: f"{n:3} program" + ("" if n == 1 else "s")
        n = len(self.program_names)
        title_to_slug = title_converter()
        toc_data: Dict[float, ProgramNames] = defaultdict(list)
        for (cost, program_name) in self.sorted_programs:
            toc_data[cost].append(program_name)
        toc: List[str] = ["# Table of contents"]
        contents: List[str] = [f"# {display_count(n)}"]
        must_detail = True
        remainder = len(self.program_names)
        for (cost, program_names) in toc_data.items():
            if must_detail:
                if len(program_names) >= section_group_limit:
                    title = f"{display_count(len(program_names))} of cost {cost}"
                    remainder -= len(program_names)
                else:
                    title = f"{display_count(remainder)} of greater costs"
                    must_detail = False
                toc.append(f"- [`{title}`](#{title_to_slug(title)})")
                contents.append(f"## {title}")
            for program_name in program_names:
                toc.append(f"    - [`{program_name}`](#{title_to_slug(program_name)})")
                contents.append(f"### `{program_name}`")
                program = self.db["programs"][program_name]
                contents.append(f"```python\n{program['source']}\n```")
                for (taxon_name, spans) in program["taxons"].items():
                    contents.append(f"- {len(spans):3}: `{taxon_name}`")
        summary: List[str] = ["# Quantitative summary"]
        self.counts["remaining"] = len(self.program_names)
        for (description, count) in self.counts.items():
            summary.append(f"- {display_count(count)} {description}.")
        return "\n".join(toc + contents + summary + [""])


if __name__ == "__main__":
    Path = __import__("pathlib").Path

    dbf = DatabaseFilter(json.loads(Path("../algo/programs_db.json").read_text()))

    forbidden_taxon_patterns = r"""
        call/method/.*
    """.strip().split()
    dbf.filter_forbidden_taxons(forbidden_taxon_patterns)

    mandatory_taxon_patterns = r"""
        subroutine_definition\b.*
        operator/addition\b.*
    """.strip().split()
    dbf.filter_mandatory_taxons(mandatory_taxon_patterns)

    blacklisted_program_patterns = r"""
        .+/euler_.+
    """.strip().split()
    dbf.filter_blacklisted_programs(blacklisted_program_patterns)

    dbf.sort_by_taxon_count()
    print(dbf.get_markdown())
