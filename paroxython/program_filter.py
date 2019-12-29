import json
from pathlib import Path
from typing import Callable, Dict, List, Set

import regex  # type: ignore

ProgramPattern = str
ProgramPatterns = List[ProgramPattern]

ProgramName = str
ProgramNames = List[ProgramName]

TaxonName = str
TaxonNames = List[TaxonName]
TaxonNameMap = Dict[ProgramName, TaxonNames]

TaxonPattern = str
TaxonPatterns = List[TaxonPattern]
TaxonPatternMap = Dict[ProgramName, TaxonPatterns]


class ProgramFilter:
    def __init__(self, db: Dict) -> None:
        self.programs = db["programs"]
        self.taxons = db["taxons"]
        self.reset()

    def reset(self) -> None:
        self.result: Set[ProgramName] = set(self.programs.keys())
        self.counts = {"initially": len(self.programs)}

    def update(self, *programs: ProgramNames) -> None:
        "Update self.result, adding programs from all the given ones."
        self.result.update(*programs)

    def intersection_update(self, *programs: ProgramNames) -> None:
        "Update self.result, keeping only programs found in it and all the given ones."
        self.result.intersection_update(*programs)

    def difference_update(self, *programs: ProgramNames) -> None:
        "Update self.result, removing programs found in the given ones."
        self.result.difference_update(*programs)

    def symmetric_difference_update(self, programs: ProgramNames) -> None:
        "Update self.result, keeping only programs found in either set, but not in both."
        self.result.symmetric_difference_update(programs)

    def complement_update(self):
        "Update self.result, taking only programs filtered out so far."
        self.result = set(self.programs).difference(self.result)

    def filter_blacklisted_programs(self, programs: ProgramPatterns) -> None:
        """Suppress from self.result all programs whose name matches any
        blacklisted pattern."""
        count = len(self.result)
        if programs:
            match_program = regex.compile("|".join(programs)).match
            acc: Set[ProgramName] = set()
            for program_name in list(self.result):
                if match_program(program_name):
                    acc.add(program_name)
            self.result.difference_update(acc)
        self.counts["blacklisted"] = count - len(self.result)

    def filter_forbidden_taxons(self, taxons: TaxonPatterns) -> None:
        """Suppress from self.result all programs using any forbidden taxon."""
        count = len(self.result)
        if taxons:
            match_taxon = regex.compile("|".join(taxons)).match
            acc: Set[ProgramName] = set()
            for (taxon_name, program_names) in self.taxons.items():
                if match_taxon(taxon_name):  # this taxon is forbidden
                    acc.update(program_names)
            self.result.difference_update(acc)
        self.counts["tagged with a forbidden taxon"] = count - len(self.result)

    def filter_mandatory_taxons(self, taxons: TaxonPatterns) -> None:
        """Suppress from self.result all programs not using at least one mandatory taxon."""
        count = len(self.result)
        if taxons:
            match_taxons = [regex.compile(row).match for row in taxons]
            acc: Set[ProgramName] = set()
            for program_name in self.result:
                for match_taxon in match_taxons:
                    for taxon_name in self.programs[program_name]["taxons"]:
                        if match_taxon(taxon_name):  # this mandatory taxon is used
                            break  # no need to test the other taxons of this program
                    else:  # this mandatory taxon is not used by this program
                        acc.add(program_name)
                        break  # no need to test the other mandatory taxons
            self.result.difference_update(acc)
        self.counts["not tagged with a mandatory taxon"] = count - len(self.result)

    def get_taxons_in_programs(self, programs: ProgramPatterns) -> Set[TaxonName]:
        """Return all taxons included in at least one program of the given list."""
        result: Set[TaxonName] = set()
        if programs:
            match_program = regex.compile("|".join(programs)).match
            for program_name in self.result:
                if match_program(program_name):
                    result.update(self.programs[program_name]["taxons"])
        return result

    def get_taxons_not_in_programs(self, programs: ProgramPatterns) -> Set[TaxonName]:
        """Return all taxons not included in any program of the given list."""
        result: Set[TaxonName] = set(self.taxons.keys())
        if programs:
            match_program = regex.compile("|".join(programs)).match
            for program_name in self.result:
                if match_program(program_name):
                    result.difference_update(self.programs[program_name]["taxons"])
        return result

    def get_extra_taxon_names(self, taxons: TaxonPatterns) -> TaxonNameMap:
        """For each program, list those of its taxons which are not among the given taxons."""
        match_taxon = regex.compile("|".join(taxons)).match
        extra_taxons: TaxonNameMap = {}
        for program_name in self.result:
            extra_taxons[program_name] = []
            for taxon_name in self.programs[program_name]["taxons"]:
                if not match_taxon(taxon_name):
                    extra_taxons[program_name].append(taxon_name)
        return extra_taxons

    def get_lacking_taxon_patterns(self, taxons: TaxonPatterns) -> TaxonPatternMap:
        """For each program, list those of the given taxons that it does not include."""
        match_taxons = [regex.compile(row).match for row in taxons]
        lacking_taxons: TaxonPatternMap = {}
        for program_name in self.result:
            lacking_taxons[program_name] = []
            for (match_taxon, wanted_taxon) in zip(match_taxons, taxons):
                for taxon_name in self.programs[program_name]["taxons"]:
                    if match_taxon(taxon_name):  # this wanted taxon is used
                        break  # no need to test the other taxons of this program
                else:  # this wanted taxon is not used by this program
                    lacking_taxons[program_name].append(wanted_taxon)
        return lacking_taxons

    def sorted(self, key: Callable, reverse: bool) -> ProgramNames:
        """Generic sort. Use the following helpers instead."""
        return sorted(self.result, key=lambda p: (key(p), p), reverse=reverse)

    def sorted_by_taxon_count(self, reverse=False) -> ProgramNames:
        """Sort the programs by number of distinct taxons."""
        return self.sorted(lambda p: len(self.programs[p]["taxons"]), reverse)

    def sorted_by_line_count(self, reverse=False) -> ProgramNames:
        """Sort the programs by SLOC count."""
        return self.sorted(lambda p: self.programs[p]["source"].count("\n"), reverse)

    def sorted_by_extra_taxon_count(self, taxons: TaxonPatterns, reverse=False) -> ProgramNames:
        """Sort the programs by number of extra taxons wrt a given list."""
        extra_taxons = self.get_extra_taxon_names(taxons)
        return self.sorted(lambda p: len(extra_taxons[p]), reverse)

    def sorted_by_lacking_taxon_count(self, taxons: TaxonNames, reverse=False) -> ProgramNames:
        """Sort the programs by number of lacking taxons wrt a given list."""
        lacking_taxons = self.get_lacking_taxon_patterns(taxons)
        return self.sorted(lambda p: len(lacking_taxons[p]), reverse)

    def sorted_by_distance(self, taxons: TaxonPatterns, reverse=False) -> ProgramNames:
        """Sort the programs by number of extra and lacking taxons wrt a given list."""
        extra = self.get_extra_taxon_names(taxons)
        lacking = self.get_lacking_taxon_patterns(taxons)
        return self.sorted(lambda p: len(extra[p]) + len(lacking[p]), reverse)

    def __repr__(self):
        result: List[str] = []
        for program_name in self.result:
            program = self.programs[program_name]
            result.append("")
            result.append("-" * 80)
            result.append(program_name)
            result.append("-" * 80)
            result.append(program["source"])
            result.append("")
            for (other_name, spans) in program["taxons"].items():
                result.append(f"{len(spans):3}: {other_name}")
        result.append("-" * 80)
        self.counts["remaining"] = len(self.result)
        for (description, count) in self.counts.items():
            plural = "" if count == 1 else "s"
            result.append(f"{count:3} program{plural} {description}")
        return "\n".join(result)


if __name__ == "__main__":

    forbidden_taxon_patterns = r"""
        call/method/.*
    """.strip().split()

    mandatory_taxon_patterns = r"""
        function_definition/.*
        operator/addition/
    """.strip().split()

    blacklisted_program_patterns = r"""
        .+/problem_10/.+
    """.strip().split()

    db = json.loads(Path("db.json").read_text())
    f = ProgramFilter(db)
    f.filter_forbidden_taxons(forbidden_taxon_patterns)
    f.filter_mandatory_taxons(mandatory_taxon_patterns)
    f.filter_blacklisted_programs(blacklisted_program_patterns)
    print("\n".join(f.sorted_by_taxon_count()))
