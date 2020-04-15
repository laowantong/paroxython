from collections import defaultdict
from functools import lru_cache
from typing import Dict, List, Tuple

import regex  # type: ignore

from goodies import add_line_numbers, title_converter
from span import Span
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


@lru_cache(maxsize=None)
def depths_to_cost_zeno(start: int, stop: int) -> int:
    """Sum the slice [start : stop] of the infinite series [1/2 + 1/4 + 1/8 + ...]."""
    return int(1024 * sum(2 ** ~depth for depth in range(start, stop)))


@lru_cache(maxsize=None)  # NB: memoization needed for consistency with mypy's typing
def depths_to_cost_length(start: int, stop: int) -> int:
    return (stop - start) * 1000


class ProgramFilter:
    """Evolve a set of recommended programs and a set of imparted knowledge."""

    def __init__(self, db: JsonDatabase) -> None:
        """
        Initialize the state of the filter (recommended programs + imparted knowledge).

        During the evolution of the filter, the recommended program set (initially that
        of the whole database) can only decrease, and the imparted knowledge (initially
        empty) can only increase.
        """
        self.db = db
        self.recommended_programs: ProgramNameSet = set(db["programs"])
        self.imparted_knowledge: TaxonNameSet = set()
        self.log = {"initially": len(self.recommended_programs)}

    # Select programs from the taxons they cover, and vice versa.

    def programs_of_taxons(self, taxons: TaxonNames) -> ProgramNameSet:
        """Return the programs covering a given list of taxons."""
        programs = set()
        for taxon in taxons:
            programs.update(self.db["taxons"].get(taxon, []))
        return programs

    def taxons_of_program(self, program: ProgramName) -> TaxonNameSet:
        """Return the taxon names associated with a given program name (safe method)."""
        try:
            return set(self.db["programs"][program]["taxons"])
        except KeyError:
            return set()

    def taxons_of_programs(self, programs: ProgramNameSet) -> TaxonNameSet:
        """Fold self.taxons_of_program on several program names."""
        taxons: TaxonNameSet = set()
        for program in programs:
            taxons.update(self.taxons_of_program(program))
        return taxons

    # Update the state of the filter by applying set operations with the given taxons.

    def patterns_to_taxons(self, patterns: TaxonPatterns) -> TaxonNameSet:
        """Return all the taxon names matching at least one of the given regex patterns."""
        return set(filter(regex.compile("|".join(patterns)).match, self.db["taxons"]))

    def impart_taxons(self, taxons: TaxonNameSet) -> None:
        """Enrich the imparted knowledge with all the prefixes of the given taxons."""
        for taxon in taxons:
            segments = taxon.split("/")
            for i in range(len(segments)):
                prefix = "/".join(segments[: i + 1])
                if prefix in self.db["taxons"]:
                    self.imparted_knowledge.add(TaxonName(prefix))

    def exclude_taxons(self, taxons: TaxonNames) -> None:
        """Remove from the recommended programs those covering at least one given taxon."""
        programs = self.programs_of_taxons(taxons)
        self.recommended_programs.difference_update(programs)

    def include_taxons(self, taxons: TaxonNames) -> None:
        """Remove from the recommended programs those not covering any given taxon."""
        programs = self.programs_of_taxons(taxons)
        self.recommended_programs.intersection_update(programs)

    # Update the state of the filter by applying set operations with the given taxons.

    def patterns_to_programs(self, patterns: ProgramPatterns) -> ProgramNameSet:
        """Return all the program names matching at least one of the given regex patterns."""
        return set(filter(regex.compile("|".join(patterns)).match, self.db["programs"]))

    def impart_programs(self, programs: ProgramNameSet) -> None:
        """
        Remove from the recommended programs those found in the given ones, and enrich the
        imparted knowledge with all the prefixes of the taxons covered by these programs.
        """
        self.impart_taxons(self.taxons_of_programs(programs))
        self.recommended_programs.difference_update(programs)

    def exclude_programs(self, programs: ProgramNameSet) -> None:
        "Remove from the recommended programs those found in the given ones."
        self.recommended_programs.difference_update(programs)

    def include_programs(self, programs: ProgramNameSet) -> None:
        "Remove from the recommended programs those not found in the given ones."
        self.recommended_programs.intersection_update(programs)

    # Compute the learning cost of the recommended programs wrt the imparted knowledge.

    def set_cost_computation_strategy(self, strategy) -> None:
        self.compute_taxon_cost.cache_clear()
        if strategy.lower() == "zeno":
            self.depths_to_cost = depths_to_cost_zeno
        elif strategy == "length":
            self.depths_to_cost = depths_to_cost_length
        else:
            raise NotImplementedError
        self.depths_to_cost.cache_clear()

    @lru_cache(maxsize=None)
    def compute_taxon_cost(self, taxon: TaxonName) -> int:
        """Evaluate the learning cost of a given taxon name."""
        (start, stop) = (0, 0)
        if taxon not in self.imparted_knowledge:
            segments = taxon.split("/")
            stop = len(segments)
            for start in range(stop - 1, -1, -1):
                if "/".join(segments[:start]) in self.imparted_knowledge:
                    break
        return self.depths_to_cost(start, stop)

    def get_sorted_recommendations(self) -> List[Tuple[int, ProgramName]]:
        result: List[Tuple[int, ProgramName]] = []
        for program in self.recommended_programs:
            taxons = self.taxons_of_program(program)
            result.append((sum(map(self.compute_taxon_cost, taxons)), program))
        return sorted(result)

    def get_markdown(self, section_group_limit=5) -> str:
        display_count = lambda n: f"{n:3} program" + ("" if n == 1 else "s")
        n = len(self.recommended_programs)
        title_to_slug = title_converter()
        toc_data: Dict[int, ProgramNames] = defaultdict(list)
        for (cost, program_name) in self.get_sorted_recommendations():
            toc_data[cost].append(program_name)
        toc: List[str] = ["# Table of contents"]
        contents: List[str] = [f"# {display_count(n)}"]
        must_detail = True
        remainder = len(self.recommended_programs)
        for (cost, program_names) in toc_data.items():
            if must_detail:
                if len(program_names) >= section_group_limit:
                    title = f"{display_count(len(program_names))} of learning cost {cost}"
                    remainder -= len(program_names)
                else:
                    title = f"{display_count(remainder)} of greater learning costs"
                    must_detail = False
                toc.append(f"- [`{title}`](#{title_to_slug(title)})")
                contents.append(f"\n## {title}")
            for program_name in program_names:
                title = f"Program `{program_name}` (learning cost {cost})"
                toc.append(f"    - [`{program_name}`](#{title_to_slug(title)})")
                contents.append(f"\n### {title}")
                program_info = self.db["programs"][program_name]
                contents.append(f"\n```python\n{add_line_numbers(program_info['source'])}\n```")
                contents.append("\n| Cost  | Taxon | Lines |")
                contents.append("|" + "----|" * 3)
                for (taxon_name, spans) in program_info["taxons"].items():
                    cost = self.compute_taxon_cost(taxon_name)
                    all_span_strings = [str(Span(span)) for span in spans]
                    if len(all_span_strings) > 7:
                        n = len(all_span_strings) - 4
                        span_string = ", ".join(all_span_strings[:4]) + f" and {n} more"
                    else:
                        span_string = ", ".join(all_span_strings)
                    contents.append(f"| {cost} | `{taxon_name}` | {span_string} |")
        summary: List[str] = ["\n# Quantitative summary"]
        self.log["remaining"] = len(self.recommended_programs)
        for (description, count) in self.log.items():
            summary.append(f"- {display_count(count)} {description}.")
        return "\n".join(toc + contents + summary + [""])
