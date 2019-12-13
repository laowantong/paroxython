from pathlib import Path
import json
from regex import compile
import sys

sys.path[0:0] = [str(Path(__file__).parent)]

from set_list import SetList


class ProgramFilter:
    def __init__(self, db):
        self.programs = db["programs"]
        self.taxons = db["taxons"]
        self.reset()

    def reset(self):
        self.result = SetList(self.programs.keys())
        self.counts = {"initially": len(self.result)}

    def filter_blacklisted_programs(self, program_names):
        """Suppress from self.result all programs whose name matches any
        blacklisted pattern."""
        count = len(self.result)
        if program_names:
            match_program = compile("|".join(program_names)).match
            for program_name in list(self.result):
                if match_program(program_name):
                    self.result.discard(program_name)
        self.counts["blacklisted"] = count - len(self.result)

    def filter_forbidden_taxons(self, taxon_names):
        """Suppress from self.result all programs using any forbidden taxon."""
        count = len(self.result)
        if taxon_names:
            match_taxon = compile("|".join(taxon_names)).match
            for (taxon_name, program_names) in self.taxons.items():
                if match_taxon(taxon_name):  # this taxon is forbidden
                    self.result = self.result.difference(program_names)
        self.counts["tagged with a forbidden taxon"] = count - len(self.result)

    def filter_mandatory_taxons(self, taxon_names):
        """Suppress from self.result all programs not using at least one
        mandatory taxon."""
        count = len(self.result)
        if taxon_names:
            match_taxons = [compile(row).match for row in taxon_names]
            for program_name in list(self.result):
                for match_taxon in match_taxons:
                    for taxon_name in self.programs[program_name]["taxons"]:
                        if match_taxon(taxon_name):  # this mandatory taxon is used
                            break  # no need to test the other taxons of this program
                    else:  # this mandatory taxon is not used by this program
                        self.result.discard(program_name)
                        break  # no need to test the other mandatory taxons
        self.counts["not tagged with a mandatory taxon"] = count - len(self.result)

    def get_taxons_in_programs(self, program_names):
        """Return all taxons included in at least one program of the given list."""
        result = set()
        if program_names:
            match_program = compile("|".join(program_names)).match
            for program_name in self.result:
                if match_program(program_name):
                    result.update(self.programs[program_name]["taxons"])
        return "\n".join(sorted(result))

    def get_taxons_not_in_programs(self, program_names):
        """Return all taxons not included in any program of the given list."""
        result = set(self.taxons.keys())
        if program_names:
            match_program = compile("|".join(program_names)).match
            for program_name in self.result:
                if match_program(program_name):
                    result.difference_update(self.programs[program_name]["taxons"])
        return "\n".join(sorted(result))

    def get_extra_taxons(self, taxon_names):
        """For each program, list those of its taxons which are not among the given taxons."""
        match_taxon = compile("|".join(taxon_names)).match
        extra_taxons = {}
        for program_name in self.result:
            extra_taxons[program_name] = []
            for taxon_name in self.programs[program_name]["taxons"]:
                if not match_taxon(taxon_name):
                    extra_taxons[program_name].append(taxon_name)
        return extra_taxons

    def get_lacking_taxons(self, taxon_names):
        """For each program, list those of the given taxons that it does not include."""
        match_taxons = [compile(row).match for row in taxon_names]
        lacking_taxons = {}
        for program_name in self.result:
            lacking_taxons[program_name] = []
            for (match_taxon, wanted_taxon_name) in zip(match_taxons, taxon_names):
                for taxon_name in self.programs[program_name]["taxons"]:
                    if match_taxon(taxon_name):  # this wanted taxon is used
                        break  # no need to test the other taxons of this program
                else:  # this wanted taxon is not used by this program
                    lacking_taxons[program_name].append(wanted_taxon_name)
        return lacking_taxons

    def sort(self, key, reverse):
        """Generic sort. Use the following helpers instead."""
        self.result.sort(key=key, reverse=reverse)

    def sort_by_taxon_count(self, reverse=False):
        """Sort the programs by number of distinct taxons."""
        self.sort(lambda p: len(self.programs[p]["taxons"]), reverse)

    def sort_by_line_count(self, reverse=False):
        """Sort the programs by SLOC count."""
        self.sort(lambda p: self.programs[p]["source"].count("\n"), reverse)

    def sort_by_extra_taxon_count(self, taxon_names, reverse=False):
        """Sort the programs by number of extra taxons wrt a given list."""
        extra_taxons = self.get_extra_taxons(taxon_names)
        self.sort(lambda p: len(extra_taxons[p]), reverse)

    def sort_by_lacking_taxon_count(self, taxon_names, reverse=False):
        """Sort the programs by number of lacking taxons wrt a given list."""
        lacking_taxons = self.get_lacking_taxons(taxon_names)
        self.sort(lambda p: len(lacking_taxons[p]), reverse)

    def sort_by_distance(self, taxon_names, reverse=False):
        """Sort the programs by number of exta and lacking taxons wrt a given list."""
        extra_taxons = self.get_extra_taxons(taxon_names)
        lacking_taxons = self.get_lacking_taxons(taxon_names)
        self.sort(lambda p: len(extra_taxons[p]) + len(lacking_taxons[p]), reverse)

    def __repr__(self):
        result = []
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

    forbidden_patterns = r"""
        call/method/.*
    """.strip().split()

    mandatory_patterns = r"""
        function_definition/.*
        operator/percent/modulo/.*
    """.strip().split()

    blacklisted_patterns = r"""
        .+/problem_10/.+
    """.strip().split()

    db = json.loads(Path("db.json").read_text())
    f = ProgramFilter(db)
    f.filter_forbidden_taxons(forbidden_patterns)
    f.filter_mandatory_taxons(mandatory_patterns)
    f.filter_blacklisted_programs(blacklisted_patterns)
    f.sort_by_taxon_count()
    print(f)
