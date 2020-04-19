from collections import defaultdict

import regex  # type: ignore

from user_types import (
    JsonDatabase,
    ProgramInfos,
    ProgramName,
    ProgramNameSet,
    ProgramPatterns,
    ProgramTaxonNames,
    TaxonInfos,
    TaxonName,
    TaxonNames,
    TaxonNameSet,
    TaxonPatterns,
)


class ProgramFilter:
    """Evolve a set of recommended programs and a set of imparted knowledge."""

    def __init__(self, db: JsonDatabase) -> None:
        """
        Initialize the state of the filter (recommended programs + imparted knowledge).

        During the evolution of the filter, the recommended program set (initially that
        of the whole database) can only decrease, and the imparted knowledge (initially
        empty) can only increase.
        """

        # store some shortcuts to DB objects
        self.db_programs: ProgramInfos = db["programs"]
        self.db_taxons: TaxonInfos = db["taxons"]
        self.db_links = {
            program_name: list(program_info["links"])
            for (program_name, program_info) in self.db_programs.items()
        }

        # For every program P1 which imports another program P2, inject the taxons of P2
        # (associated to an empty list of spans) into those of P1. Additionally, construct a
        # dictionary associating to P1 each supplementary taxon featured by P2.
        self.imported_taxons: TaxonInfos = defaultdict(list)
        for (program_name, info) in self.db_programs.items():
            for link in info["links"]:
                for (taxon, spans) in self.db_programs[link]["taxons"].items():
                    if spans and not info["taxons"].get(taxon):
                        info["taxons"][taxon] = []
                        self.imported_taxons[taxon].append(program_name)

        # Initialize the state of the filter
        self.imparted_knowledge: TaxonNameSet = set()
        self.recommended_programs: ProgramTaxonNames = {
            program_name: list(program_info["taxons"])
            for (program_name, program_info) in self.db_programs.items()
        }

    # Select programs from the taxons they feature, and vice versa.

    def programs_of_taxons(self, taxons: TaxonNames, follow_import: bool) -> ProgramNameSet:
        """Return the programs featuring a given list of taxons, either directly or indirectly."""
        programs: ProgramNameSet = set()
        for taxon in taxons:
            programs.update(self.db_taxons.get(taxon, []))
            if follow_import:
                programs.update(self.imported_taxons.get(taxon, []))
        return programs

    def taxons_of_programs(self, programs: ProgramNameSet) -> TaxonNameSet:
        """Return the taxon names featured by the given programs, either directly or indirectly."""
        taxons: TaxonNameSet = set()
        for program in programs:
            if program in self.db_programs:
                taxons.update(self.db_programs[program]["taxons"])
        return taxons

    # Update the state of the filter by applying set operations with the given programs.

    def patterns_to_programs(self, patterns: ProgramPatterns) -> ProgramNameSet:
        """Return all the program names matching at least one of the given regex patterns."""
        return set(filter(regex.compile("|".join(patterns)).match, self.db_programs))

    def impart_programs(self, programs: ProgramNameSet) -> None:
        """
        Remove from the recommended programs those found in the given ones, and enrich the imparted
        knowledge with all the prefixes of the taxons featured by these programs, including the
        imported ones.
        """
        for program in programs:
            self.recommended_programs.pop(program, None)
            if program in self.db_programs:
                for imported_program in self.db_links[program]:
                    self.recommended_programs.pop(imported_program, None)
        self.impart_taxons(self.taxons_of_programs(programs))

    def exclude_programs(self, programs: ProgramNameSet) -> None:
        """
        Remove from the recommended programs those found in the given ones or imported by them.
        """
        for program in programs:
            self.recommended_programs.pop(program, None)
        for program in list(self.recommended_programs):
            if programs.intersection(self.db_links[program]):
                self.recommended_programs.pop(program, None)

    def include_programs(self, programs: ProgramNameSet) -> None:
        """
        Remove from the recommended programs those not found in the given ones or in those imported
        by them.
        """
        extended_programs: ProgramNameSet = set(programs)  # make a copy to ensure purity
        for program in programs:
            if program in self.db_programs:
                extended_programs.update(self.db_links[program])
        for program in list(self.recommended_programs):
            if program not in extended_programs:
                self.recommended_programs.pop(program, None)

    # Update the state of the filter by applying set operations with the given taxons.

    def patterns_to_taxons(self, patterns: TaxonPatterns) -> TaxonNameSet:
        """
        Return all the taxon names matching at least one of the given regex patterns.
        """
        return set(filter(regex.compile("|".join(patterns)).match, self.db_taxons))

    def impart_taxons(self, taxons: TaxonNameSet) -> None:
        """Enrich the imparted knowledge with all the prefixes of the given taxons."""
        for taxon in taxons:
            segments = taxon.split("/")
            for i in range(len(segments)):
                prefix = "/".join(segments[: i + 1])
                if prefix in self.db_taxons:
                    self.imparted_knowledge.add(TaxonName(prefix))

    def exclude_taxons(self, taxons: TaxonNames) -> None:
        """
        Remove from the recommended programs those covering at least one given taxon, either
        directly or by importation.
        """
        programs = self.programs_of_taxons(taxons, follow_import=True)
        for program in programs:
            self.recommended_programs.pop(program, None)

    def include_taxons(self, taxons: TaxonNames) -> None:
        """Remove from the recommended programs those not covering any given taxon."""
        programs = self.programs_of_taxons(taxons, follow_import=False)
        for program in list(self.recommended_programs):
            if program not in programs:
                self.recommended_programs.pop(program, None)


if __name__ == "__main__":
    Recommendations = __import__("recommend_programs").Recommendations
    Path = __import__("pathlib").Path
    rec = Recommendations(Path("../algo/programs_pipe.py"))
    rec.run_pipeline()
    text = rec.get_markdown()
    rec.dump(text)
