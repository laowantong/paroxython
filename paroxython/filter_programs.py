import sys
from itertools import product, permutations
from typing import Set

import regex  # type: ignore

from .compare_spans import compare_spans
from .user_types import (
    JsonDatabase,
    ProgramInfos,
    ProgramName,
    ProgramNames,
    ProgramNameSet,
    ProgramTaxonNames,
    ProgramToPrograms,
    TaxonInfos,
    TaxonName,
    TaxonNameOrTriple,
    TaxonNameSet,
    TaxonNamesOrTriples,
    TaxonTriple,
    TaxonTriplet,
)


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

        # Initialize the state of the filter.
        self.imparted_knowledge: TaxonNameSet = set()
        self.selected_programs: ProgramTaxonNames = {
            program_name: list(program_info["taxons"])
            for (program_name, program_info) in self.db_programs.items()
        }

    # Select programs from the taxons they feature, and vice versa.

    def taxons_of_programs(self, programs: ProgramNameSet) -> TaxonNameSet:
        """Return the taxon names featured (directly or not) by the given programs."""
        taxons: TaxonNameSet = set()
        for program in programs:
            if program in self.db_programs:
                taxons.update(self.db_programs[program]["taxons"])
        return taxons

    def programs_of_taxons(self, taxons: TaxonNamesOrTriples, follow: bool) -> ProgramNameSet:
        """Return the programs featuring (optionally by importation) any given taxon."""
        programs: ProgramNameSet = set()
        programs.update(*map(self.programs_of_taxon, taxons))
        if follow:
            programs.update(*(self.db_exportations[program] for program in programs))
        return programs

    @staticmethod
    def triple_to_triplet(name_1: TaxonName, predicate: str, name_2: TaxonName) -> TaxonTriplet:
        """Ensure that the given predicate is correct or can be salvaged, and return a triplet."""
        negated = True
        if predicate.startswith("!"):
            predicate = predicate[1:]
        elif regex.search(r"\bnot ", predicate):
            predicate = predicate.replace("not ", "")
        elif regex.search(r" not\b", predicate):
            predicate = predicate.replace(" not", "")
        else:
            negated = False
        s = predicate.lower().strip()
        if s not in compare_spans:
            # If there is only one x (resp. y), expand it into x≤x (resp. y≤y)
            s = regex.sub(r"^([^x]*)x([^x]*)$", r"\1x≤x\2", s)
            s = regex.sub(r"^([^y]*)y([^y]*)$", r"\1y≤y\2", s)
            # Convert usual comparison operators
            s = s.replace("<=", "≤").replace("==", "=")
            # Ignore all other characters
            s = regex.sub(r"[^xy<=≤]", "", s)
            if s != predicate:
                print(f"Warning: predicate '{predicate}' normalized into '{s}'.", file=sys.stderr)
            if s not in compare_spans:  # pragma: no cover
                raise ValueError(f"Malformed predicate '{predicate}' in the pipeline.")
        prebounded_predicate = compare_spans[s]
        if negated:
            bounded_predicate = lambda x, y: not (prebounded_predicate(x, y))
        else:
            bounded_predicate = prebounded_predicate
        return TaxonTriplet(name_1=name_1, predicate=bounded_predicate, name_2=name_2)

    def programs_of_taxon(self, taxon: TaxonNameOrTriple) -> ProgramNameSet:
        """Dispatch computation to the appropriate method, depending on the actual taxon type."""
        if isinstance(taxon, str):
            if taxon.startswith("!"):
                return set(self.db_programs) - set(self.db_taxons.get(TaxonName(taxon[1:]), []))
            else:
                return set(self.db_taxons.get(TaxonName(taxon), []))
        else:
            return self.programs_of_taxon_triplet(self.triple_to_triplet(*taxon))

    def programs_of_taxon_triplet(self, taxon: TaxonTriplet) -> ProgramNameSet:
        """Return the programs where two given taxons satisfy a given predicate."""
        # Compute the set of programs which feature both taxons
        programs_featuring_1 = set(self.db_taxons.get(taxon.name_1, []))
        programs_featuring_2 = set(self.db_taxons.get(taxon.name_2, []))
        # Keep only the subset of taxons which satisfy the predicate
        programs: ProgramNameSet = set()
        for program in programs_featuring_1 & programs_featuring_2:
            spans_1 = self.db_programs[program]["taxons"][taxon.name_1]
            spans_2 = self.db_programs[program]["taxons"][taxon.name_2]
            if taxon.name_1 == taxon.name_2:
                couples = permutations(spans_1, 2)  # = product(spans_1, spans_2) w/o diagonal
            else:
                couples = product(spans_1, spans_2)
            for (span_1, span_2) in couples:
                if taxon.predicate(span_1, span_2):
                    programs.add(program)
                    break
        return programs

    # Update the state of the filter by applying set operations with the given programs.

    def match_against_existing_programs(self, pattern: str) -> ProgramNameSet:
        """Enumerate all the existing programs matching the given pattern."""
        result: ProgramNameSet = set()
        match = regex.compile(fr"{pattern}\b").match
        no_match = True
        for program_name in self.db_programs:
            if match(program_name):
                result.add(program_name)
                no_match = False
        if no_match:
            print(
                f"Warning: the pattern '{pattern}' doesn't match any existing program.",
                file=sys.stderr,
            )
        return result

    def preprocess_programs(self, programs: ProgramNames) -> ProgramNames:
        """Return all the program names matching at least one of the given regex patterns."""
        result: Set[ProgramName] = set()
        for program in programs:
            if program in self.db_programs:
                result.add(program)
            else:
                result.update(self.match_against_existing_programs(program))
        return sorted(result)

    def impart_programs(self, programs: ProgramNameSet) -> None:
        """Deselect the programs found in the given ones.

        Additionally, enrich the imparted knowledge with all the prefixes of the taxons featured
        (directly or not) by these programs."""
        for program in programs:
            self.selected_programs.pop(program, None)
            if program in self.db_programs:
                for imported_program in self.db_importations[program]:
                    self.selected_programs.pop(imported_program, None)
        self.impart_taxons(self.taxons_of_programs(programs))  # type: ignore

    def exclude_programs(self, programs: ProgramNameSet) -> None:
        """Deselect the programs found among the given ones or imported by them."""
        for program in programs:
            self.selected_programs.pop(program, None)
        for program in list(self.selected_programs):
            if programs.intersection(self.db_importations[program]):
                self.selected_programs.pop(program, None)

    def include_programs(self, programs: ProgramNameSet) -> None:
        """Deselect the programs neither found among the given ones or those they import."""
        extended_programs: ProgramNameSet = set(programs)  # make a copy to ensure purity
        for program in programs:
            if program in self.db_programs:
                extended_programs.update(self.db_importations[program])
        for program in list(self.selected_programs):
            if program not in extended_programs:
                self.selected_programs.pop(program, None)

    # Update the state of the filter by applying set operations with the given taxons.

    def match_against_existing_taxons(self, pattern: str) -> TaxonNameSet:
        """Enumerate all the existing taxons matching the given pattern."""
        result: TaxonNameSet = set()
        match = regex.compile(fr"{pattern}\b").match
        no_match = True
        for taxon_name in self.db_taxons:
            if match(taxon_name):
                result.add(taxon_name)
                no_match = False
        if no_match:
            print(
                f"Warning: the pattern '{pattern}' doesn't match any existing taxon.",
                file=sys.stderr,
            )
        return result

    def preprocess_taxons(self, taxons: TaxonNamesOrTriples) -> TaxonNamesOrTriples:
        """Parse the taxons and the triples and try to match them with existing taxon names."""
        result: Set[TaxonNameOrTriple] = set()
        for taxon in taxons:
            if isinstance(taxon, str):
                # The taxon is a name or a pattern.
                negate = "!"
                if taxon.startswith("not "):
                    taxon = TaxonName(taxon[4:].strip())
                elif taxon.startswith("!"):
                    taxon = TaxonName(taxon[1:].strip())
                else:
                    negate = ""
                # Process it systymatically as a pattern, and add all its matches.
                result.update(
                    TaxonName(negate + s) for s in self.match_against_existing_taxons(taxon)
                )
            else:
                # The taxon is a triple.
                (name_1, predicate, name_2) = taxon
                # Process them systematically as patterns, and add the product of their matches.
                taxons_1 = self.match_against_existing_taxons(name_1)
                taxons_2 = self.match_against_existing_taxons(name_2)
                for (name_1, name_2) in product(taxons_1, taxons_2):
                    result.add(TaxonTriple(name_1, predicate, name_2))
        return sorted(result, key=str)

    def impart_taxon_name(self, taxon: TaxonName) -> None:
        """Enrich the imparted knowledge with all the prefixes of the given taxon."""
        segments = taxon.split("/")
        for i in range(len(segments)):
            prefix = "/".join(segments[: i + 1])
            self.imparted_knowledge.add(TaxonName(prefix))

    def impart_taxons(self, taxons: TaxonNamesOrTriples) -> None:
        """Enrich the imparted knowledge with all the prefixes of the given taxons."""
        for taxon in taxons:
            if isinstance(taxon, str):
                self.impart_taxon_name(taxon)
            else:  # ignore the predicate and impart the two taxons
                self.impart_taxon_name(taxon[0])
                print(f"Warning: predicate '{taxon[1]}' ignored.", file=sys.stderr)
                self.impart_taxon_name(taxon[2])

    def exclude_taxons(self, taxons: TaxonNamesOrTriples) -> None:
        """Deselect the programs featuring (directly or not) at least one given taxon."""
        programs = self.programs_of_taxons(taxons, follow=True)
        for program in programs:
            self.selected_programs.pop(program, None)

    def include_taxons(self, taxons: TaxonNamesOrTriples) -> None:
        """Deselect the programs not featuring any given taxon."""
        programs = self.programs_of_taxons(taxons, follow=False)
        for program in list(self.selected_programs):
            if program not in programs:
                self.selected_programs.pop(program, None)
