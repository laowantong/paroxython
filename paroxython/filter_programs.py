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
        self.db_programs: ProgramInfos = db["programs"]
        self.db_taxons: TaxonInfos = db["taxons"]
        self.recommended_programs: ProgramTaxonNames = {
            program_name: list(program_info["taxons"])
            for (program_name, program_info) in self.db_programs.items()
        }
        self.imparted_knowledge: TaxonNameSet = set()

    # Select programs from the taxons they cover, and vice versa.

    def programs_of_taxons(self, taxons: TaxonNames) -> ProgramNameSet:
        """Return the programs covering a given list of taxons."""
        programs: ProgramNameSet = set()
        for taxon in taxons:
            programs.update(self.db_taxons.get(taxon, []))
        return programs

    def taxons_of_program(self, program: ProgramName) -> TaxonNameSet:
        """Return the taxon names associated with a given program name (safe method)."""
        try:
            return set(self.db_programs[program]["taxons"])
        except KeyError:
            return set()

    def taxons_of_programs(self, programs: ProgramNameSet) -> TaxonNameSet:
        """Fold self.taxons_of_program on several program names."""
        taxons: TaxonNameSet = set()
        for program in programs:
            taxons.update(self.taxons_of_program(program))
        return taxons

    # Update the state of the filter by applying set operations with the given programs.

    def patterns_to_programs(self, patterns: ProgramPatterns) -> ProgramNameSet:
        """Return all the program names matching at least one of the given regex patterns."""
        return set(filter(regex.compile("|".join(patterns)).match, self.db_programs))

    def impart_programs(self, programs: ProgramNameSet) -> None:
        """
        Remove from the recommended programs those found in the given ones, and enrich the
        imparted knowledge with all the prefixes of the taxons covered by these programs.
        """
        self.impart_taxons(self.taxons_of_programs(programs))
        self.exclude_programs(programs)

    def exclude_programs(self, programs: ProgramNameSet) -> None:
        "Remove from the recommended programs those found in the given ones."
        for k in list(self.recommended_programs):
            if k in programs:
                del self.recommended_programs[k]

    def include_programs(self, programs: ProgramNameSet) -> None:
        "Remove from the recommended programs those not found in the given ones."
        for k in list(self.recommended_programs):
            if k not in programs:
                del self.recommended_programs[k]

    # Update the state of the filter by applying set operations with the given taxons.

    def patterns_to_taxons(self, patterns: TaxonPatterns) -> TaxonNameSet:
        """Return all the taxon names matching at least one of the given regex patterns."""
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
        """Remove from the recommended programs those covering at least one given taxon."""
        self.exclude_programs(self.programs_of_taxons(taxons))

    def include_taxons(self, taxons: TaxonNames) -> None:
        """Remove from the recommended programs those not covering any given taxon."""
        self.include_programs(self.programs_of_taxons(taxons))
