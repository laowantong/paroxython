import json
from ast import literal_eval
from functools import lru_cache
from pathlib import Path
from typing import Dict, Tuple

import regex  # type: ignore

from filter_programs import DatabaseFilter
from user_types import (
    Configuration,
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


@lru_cache(maxsize=None)
def get_prefixes_of_taxon_names(taxon_name: TaxonName) -> TaxonNames:
    """
    Compute the whole set of the notions required by a taxon already studied.

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
    def __init__(self, configuration_path: Path):
        """
        Read a configuration file written as a Python dictionary.

        For security purposes, this expression is evaluated by ast.literal_eval
        Cf. https://docs.python.org/3/library/ast.html#ast.literal_eval).

        Main benefits over JSON:
        - with raw strings r"...", no need to double-escape backslashes in regexes;
        - trailing commas;
        - comments!
        """
        self.cfg: Configuration = literal_eval(configuration_path.read_text())
        self.base_path = configuration_path.parent

    def __call__(self):
        db_path = self.base_path / self.cfg["input_path"]
        self.dbf = DatabaseFilter(json.loads(db_path.read_text()))
        self.init_old_program_names(self.cfg["syllabus"])
        self.dbf.difference_update(self.old_program_names)
        self.init_old_taxon_names()
        self.dbf.filter_blacklisted_programs(self.cfg["blacklisted_program_patterns"])
        self.dbf.filter_forbidden_taxons(self.cfg["forbidden_taxon_patterns"])
        self.dbf.filter_mandatory_taxons(self.cfg["mandatory_taxon_patterns"])
        self.set_cost_computation_strategy(self.cfg["cost_computation_strategy"])
        self.dbf.sort(self.compute_program_cost)
        output_path = self.base_path / self.cfg["output_path"]
        print(f"Output path: {output_path.resolve()}")
        output_path.write_text(self.dbf.get_markdown())

    def init_old_program_names(self, syllabus):
        """Find the programs already studied."""
        self.old_program_names: ProgramNameSet = set()
        syllabus_path = self.base_path / syllabus["path"]
        source = regex.search(syllabus["search_pattern"], syllabus_path.read_text())[1]
        matches = regex.finditer(syllabus["finditer_pattern"], source)
        program_names = {ProgramName(m[1]) for m in matches}
        self.old_program_names = self.dbf.intersection(program_names)

    def init_old_taxon_names(self):
        """Find the taxons already studied."""
        self.old_taxon_names: TaxonNameSet = set()
        for program_name in self.old_program_names:
            taxon_names = self.dbf.program_taxons(program_name)
            for taxon_name in taxon_names:
                self.old_taxon_names.update(get_prefixes_of_taxon_names(taxon_name))

    def set_cost_computation_strategy(self, strategy) -> None:
        self.compute_taxon_cost.cache_clear()
        if strategy.lower() == "zeno":
            self.depths_to_cost = depths_to_cost_zeno
        elif strategy == "length":
            self.depths_to_cost = depths_to_cost_length
        else:
            raise NotImplementedError  # pragma: no cover
        self.depths_to_cost.cache_clear()

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
        return sum(map(self.compute_taxon_cost, self.dbf.program_taxons(program_name)))


if __name__ == "__main__":
    recommend_programs = ProgramAdvisor(Path("../algo/programs_cfg.py"))
    recommend_programs()
