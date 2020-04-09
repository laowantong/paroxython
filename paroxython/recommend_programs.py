from functools import lru_cache
from typing import Tuple

import regex  # type: ignore

from filter_programs import ProgramFilter
from user_types import (
    ProgramName,
    ProgramNames,
    ProgramNameSet,
    TaxonName,
    TaxonNames,
    TaxonNameSet,
)


@lru_cache(maxsize=None)
def depths_to_cost_zeno(start: int, stop: int) -> float:
    """Sum the slice [start : stop] of the infinite series [1/2 + 1/4 + 1/8 + ...]."""
    return sum(2 ** ~depth for depth in range(start, stop))


@lru_cache(maxsize=None)  # NB: memoization needed for consistency with mypy's typing
def depths_to_cost_length(start: int, stop: int) -> float:
    return float(stop - start)


def get_studied_programs_from_syllabus(
    syllabus: str,
    path_prefix: str = "",
    search_pattern: str = r"(?sm)(.*)^ *# EOF",  # \1 match the useful part of the syllabus
    finditer_pattern: str = r"\+ *(?:\[.+?\] *)?(\w+\.py)\b",  # \1 match a program name
) -> ProgramNameSet:
    """Retrieve the programs marked as already studied in the teacher's syllabus."""
    source = regex.search(search_pattern, syllabus)[1]
    matches = regex.finditer(finditer_pattern, source)
    return {ProgramName(path_prefix + m[1]) for m in matches}


@lru_cache(maxsize=None)
def get_prefixes_of_taxon_names(taxon_name: TaxonName) -> TaxonNames:
    """
    Compute the whole set of the notions required by a notion already studied.

    Since a taxon has the form "segment_0/segment_1/.../segment_n", introducing it requires
    the introduction of all its "prefix" notions, namely:
        - "segment_0"
        - "segment_0/segment_1"
        - ...
        - "segment_0/segment_1/.../segment_n"
    """
    segments = taxon_name.split("/")
    return [TaxonName("/".join(segments[: i + 1])) for i in range(len(segments))]


class ProgramAdvisor:
    def __init__(self, program_filter: ProgramFilter):
        self.program_filter = program_filter
        self.old_program_names: ProgramNameSet = set()
        self.old_taxon_names: TaxonNameSet = set()

    def set_cost_computation_strategy(self, strategy: str) -> None:
        self.compute_taxon_cost.cache_clear()
        depths_to_cost_zeno.cache_clear()
        if strategy.lower() == "zeno":
            self.depths_to_cost = depths_to_cost_zeno
        elif strategy == "length":
            self.depths_to_cost = depths_to_cost_length
        else:
            raise NotImplementedError  # type: ignore

    def init_old_programs(self, **kwargs):
        program_names = get_studied_programs_from_syllabus(**kwargs)
        self.old_program_names = self.program_filter.intersection(program_names)
        self.program_filter.difference_update(program_names)
        self.old_taxon_names.clear()
        for program_name in self.old_program_names:
            taxon_names = self.program_filter.db_program_taxon_names[program_name]
            for taxon_name in taxon_names:
                self.old_taxon_names.update(get_prefixes_of_taxon_names(taxon_name))

    @lru_cache(maxsize=None)
    def compute_taxon_cost(self, taxon_name: TaxonName) -> float:
        """Evaluate the learning cost of a given taxon name."""
        (start, stop) = (0, 0)
        if taxon_name not in self.old_taxon_names:
            segments = taxon_name.split("/")
            stop = len(segments)
            for start in range(stop - 1, -1, -1):
                if "/".join(segments[:start]) in self.old_taxon_names:
                    break
        return self.depths_to_cost(start, stop)

    def compute_program_cost(self, program_name: ProgramName) -> float:
        """Sum the cost of all taxons of the given program."""
        return sum(
            self.compute_taxon_cost(taxon_name)
            for taxon_name in self.program_filter.db_program_taxon_names[program_name]
        )

    def get_advice(self) -> str:
        self.program_filter.sort(self.compute_program_cost)
        return str(self.program_filter)


if __name__ == "__main__":
    Path = __import__("pathlib").Path
    json = __import__("json")
    db = json.loads(Path("db.json").read_text())
    advisor = ProgramAdvisor(ProgramFilter(db))
    syllabus = Path("../algo/timeline.txt").read_text()
    advisor.init_old_programs(syllabus=syllabus, path_prefix="../algo/programs/")
    advisor.set_cost_computation_strategy("zeno")
    print(advisor.get_advice())
