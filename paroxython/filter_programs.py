from itertools import permutations, product
from typing import Iterator

import regex  # type: ignore

from .user_types import (
    JsonDatabase,
    Operation,
    Predicate,
    ProgramInfos,
    ProgramNameSet,
    ProgramTaxonNames,
    ProgramToPrograms,
    TaxonInfos,
    TaxonName,
    TaxonNameSet,
    TaxonsPoorSpans,
)
from .goodies import print_warning


class ProgramFilter:
    """Evolve a set of selected programs and a set of imparted knowledge."""

    def __init__(self, db: JsonDatabase) -> None:
        """Initialize the state of the filter (selected programs + imparted knowledge).

        During the evolution of the filter, the set of the selected programs (initially all of
        them) can only shrink, and the imparted knowledge (initially empty) can only increase.
        """

        # Create some shortcuts to the database.
        self.db_programs: ProgramInfos = db["programs"]
        self.db_taxons: TaxonInfos = db["taxons"]
        self.db_importations: ProgramToPrograms = db["importations"]
        self.db_exportations: ProgramToPrograms = db["exportations"]

        # Complete self.db_programs with imported taxons (denoted by an empty span list)
        for (exporter, importers) in self.db_exportations.items():
            exported_taxons = list(self.db_programs[exporter]["taxons"])
            for exported_taxon in exported_taxons:
                if exported_taxon.startswith("metadata/"):
                    continue
                for importer in importers:
                    importer_taxons = self.db_programs[importer]["taxons"]
                    if exported_taxon not in importer_taxons:
                        importer_taxons[exported_taxon] = []

        # Initialize the state of the filter.
        self.imparted_knowledge: TaxonNameSet = set()
        self.selected_programs: ProgramTaxonNames = {
            program_name: list(program_info["taxons"])
            for (program_name, program_info) in self.db_programs.items()
        }

    # Get the set of taxon names or program names matching the given pattern.

    def get_taxons_from_taxon_pattern(self, pattern: str) -> TaxonNameSet:
        """Enumerate all the existing taxons matching the given pattern."""
        result: TaxonNameSet = set()
        match = regex.compile(fr"{pattern}\b").match
        no_match = True
        for taxon_name in self.db_taxons:
            if match(taxon_name):
                result.add(taxon_name)
                no_match = False
        if no_match:
            print_warning(f"the pattern '{pattern}' doesn't match any existing taxon.")
        return result

    def get_programs_from_program_pattern(self, pattern: str) -> ProgramNameSet:
        """Enumerate all the existing programs matching the given pattern."""
        result: ProgramNameSet = set()
        match = regex.compile(fr"{pattern}").match
        no_match = True
        for program_name in self.db_programs:
            if match(program_name):
                result.add(program_name)
                no_match = False
        if no_match:
            print_warning(f"the pattern '{pattern}' doesn't match any existing program.")
        return result

    # Select programs from the taxons they feature, and vice versa.

    def taxons_of_programs(self, programs: ProgramNameSet, follow: bool = False) -> TaxonNameSet:
        """Return the taxons featured (or optionally imported) by any given program."""
        taxons: TaxonNameSet = set()
        for program in programs:
            if program in self.db_programs:
                for (taxon, spans) in self.db_programs[program]["taxons"].items():
                    if spans or follow:
                        taxons.add(taxon)
        return taxons

    def programs_of_taxons(self, taxons: TaxonNameSet, follow: bool = False) -> ProgramNameSet:
        """Return the programs featuring (or optionally exporting) any given taxon."""
        programs: ProgramNameSet = set()
        for taxon in taxons:
            programs.update(self.db_taxons.get(taxon, []))
        if follow:
            for program in list(programs):
                programs.update(self.db_exportations[program])
        return programs

    # Deal with semantic triples of the form (taxon_pattern_1, taxon_pattern_2, predicate)

    @staticmethod
    def _iterate_on_spans(
        # fmt: off
        spans: TaxonsPoorSpans,
        taxons_1: TaxonNameSet,
        taxons_2: TaxonNameSet
        # fmt: on
    ) -> Iterator:
        for (taxon_1, taxon_2) in product(taxons_1, taxons_2):
            if taxon_1 in spans and taxon_2 in spans:
                if taxon_1 == taxon_2:  # exclude diagonal from iteration
                    yield from permutations(spans[taxon_1], 2)
                else:
                    yield from product(spans[taxon_1], spans[taxon_2])

    def programs_of_triple(
        # fmt: off
        self,
        taxon_pattern_1: str,
        predicate: Predicate,
        taxon_pattern_2: str,
        # fmt: on
    ) -> ProgramNameSet:
        """Return the programs where two given taxons satisfy a given predicate."""
        result: ProgramNameSet = set()
        taxons_1 = self.get_taxons_from_taxon_pattern(taxon_pattern_1)
        taxons_2 = self.get_taxons_from_taxon_pattern(taxon_pattern_2)
        programs_1 = self.programs_of_taxons(taxons_1)
        programs_2 = self.programs_of_taxons(taxons_2)
        for program in programs_1 & programs_2:  # for each program featuring both taxon sets
            spans = self.db_programs[program]["taxons"]
            for (span_1, span_2) in self._iterate_on_spans(spans, taxons_1, taxons_2):
                if predicate(span_1, span_2):
                    result.add(program)
                    break
        return result

    # Update the state of the filter by applying set operations with the given programs.

    def exclude_programs(self, programs: ProgramNameSet, follow: bool) -> None:
        """Deselect the programs found among the given ones or optionally imported by them."""
        for program in programs:
            self.selected_programs.pop(program, None)
        if follow:
            for program in list(self.selected_programs):
                if programs.intersection(self.db_importations[program]):
                    self.selected_programs.pop(program, None)

    def include_programs(self, programs: ProgramNameSet) -> None:
        """Deselect the programs not found among the given ones."""
        for selected_program in list(self.selected_programs):
            if selected_program not in programs:
                self.selected_programs.pop(selected_program, None)

    # Update the state of the imparted knowledge.

    def impart_taxons(self, taxons: TaxonNameSet) -> None:
        """Enrich the imparted knowledge with all the prefixes of the given taxons."""
        for taxon in taxons:
            edges = taxon.split("/")
            for i in range(len(edges)):
                prefix = "/".join(edges[: i + 1])
                self.imparted_knowledge.add(TaxonName(prefix))

    # Dispatch the update to one of the three above methods

    def update_filter(
        # fmt: off
        self,
        operation: Operation,
        taxons: TaxonNameSet,
        programs: ProgramNameSet,
        # fmt: on
    ) -> None:
        """Update the selected programs and optionally impart the associated taxons."""
        if operation == "include":
            self.include_programs(programs)
        elif operation == "exclude":
            self.exclude_programs(programs, follow=True)
        elif operation == "impart":
            self.exclude_programs(programs, follow=False)
            self.impart_taxons(taxons)
