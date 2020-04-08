from functools import lru_cache
from typing import Tuple

import regex  # type: ignore

from user_types import JsonDatabase, ProgramName, ProgramNameSet, TaxonName, TaxonNameSet


@lru_cache(maxsize=None)
def compute_taxon_cost_zeno(start: int, stop: int) -> float:
    """Sum the slice [start : stop] of the infinite series [1/2 + 1/4 + 1/8 + ...]."""
    return sum(2 ** ~depth for depth in range(start, stop))


@lru_cache(maxsize=None)  # NB: memoization needed for consistency with mypy's typing
def compute_taxon_cost_length(start: int, stop: int) -> float:
    return float(stop - start)


class ProgramProcessor:
    def __init__(self, db: JsonDatabase):
        self.db = db
        self.old_program_names: ProgramNameSet = set()
        self.old_taxons: TaxonNameSet = set()

    def set_cost_computation_strategy(self, strategy: str) -> None:
        if strategy.lower() == "zeno":
            self.compute_taxon_cost = compute_taxon_cost_zeno
        elif strategy == "length":
            self.compute_taxon_cost = compute_taxon_cost_length
        else:
            raise NotImplementedError

    def init_old_programs(
        self,
        syllabus_text: str,
        path_prefix: str = "",
        search_pattern: str = r"(?sm)(.*)^ *# EOF",  # \1 match the useful part of the syllabus
        finditer_pattern: str = r"\+ *(?:\[.+?\] *)?(\w+\.py)\b",  # \1 match a program name
    ) -> None:
        """Retrieve the programs marked as already studied in the teacher's syllabus."""
        source = regex.search(search_pattern, syllabus_text)[1]
        matches = regex.finditer(finditer_pattern, source)
        syllabus_old_programs = {path_prefix + match[1] for match in matches}
        self.old_program_names = syllabus_old_programs.intersection(self.db["programs"])

    def init_old_taxons(self) -> None:
        """
        Construct the set of the notions covered by the programs already studied.

        Since a taxon has the form "segment_0/segment_1/.../segment_n", introducing it requires
        the introduction of all its "prefix" notions, namely:
            - "segment_0"
            - "segment_0/segment_1"
            - ...
            - "segment_0/segment_1/.../segment_n"
        """
        self.old_taxons.clear()
        for old_program_name in self.old_program_names:
            taxon_names = self.db["programs"][old_program_name]["taxons"]
            for taxon_name in taxon_names:
                segments = taxon_name.split("/")
                for i in range(len(segments)):
                    self.old_taxons.add(TaxonName("/".join(segments[: i + 1])))

    @lru_cache(maxsize=None)
    def compute_taxon_depth_range(self, taxon_name: TaxonName) -> Tuple[int, int]:
        """Evaluate the learning cost of a new taxon as a couple of depths in the taxonomy."""
        (start, stop) = (0, 0)
        if taxon_name not in self.old_taxons:
            segments = taxon_name.split("/")
            stop = len(segments)
            for start in range(stop - 1, -1, -1):
                if "/".join(segments[:start]) in self.old_taxons:
                    break
        return (start, stop)

    def compute_program_cost(self, program_name: ProgramName) -> float:
        """Sum the cost of all taxons in the given program."""
        return sum(
            self.compute_taxon_cost(*self.compute_taxon_depth_range(taxon_name))
            for taxon_name in self.db["programs"][program_name]["taxons"]
        )


if __name__ == "__main__":
    Path = __import__("pathlib").Path
    json = __import__("json")
    db = json.loads(Path("db.json").read_text())
    processor = ProgramProcessor(db)
    syllabus = Path("../algo/timeline.txt").read_text()
    processor.init_old_programs(syllabus, "../algo/programs/")
    processor.init_old_taxons()
