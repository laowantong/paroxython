from functools import lru_cache

from .user_types import TaxonName, TaxonNameSet, ProgramTaxonNames, AssessedPrograms


@lru_cache(maxsize=None)
def depths_to_cost_zeno(start: int, stop: int) -> float:
    """Sum the slice [start : stop] of the infinite series [1/2 + 1/4 + 1/8 + ...]."""
    return sum(2 ** ~depth for depth in range(start, stop))


@lru_cache(maxsize=None)  # NB: memoization needed for consistency with mypy's typing
def depths_to_cost_length(start: int, stop: int) -> float:
    return float(stop - start)


class LearningCostAssessor:
    def __init__(self, imparted_knowledge: TaxonNameSet) -> None:
        self.imparted_knowledge = imparted_knowledge

    def set_cost_assessment_strategy(self, strategy: str) -> None:
        if strategy.lower() == "zeno":
            self.depths_to_cost = depths_to_cost_zeno
        elif strategy == "length":
            self.depths_to_cost = depths_to_cost_length
        else:
            raise NotImplementedError
        self.depths_to_cost.cache_clear()
        self.taxon_cost.cache_clear()

    @lru_cache(maxsize=None)
    def taxon_cost(self, taxon: TaxonName) -> float:
        """Evaluate the learning cost of a given taxon name."""
        (start, stop) = (0, 0)
        if taxon not in self.imparted_knowledge:
            segments = taxon.split("/")
            stop = len(segments)
            for start in range(stop - 1, -1, -1):
                if "/".join(segments[:start]) in self.imparted_knowledge:
                    break
        return self.depths_to_cost(start, stop)

    def __call__(self, programs: ProgramTaxonNames) -> AssessedPrograms:
        """Evaluate the learning costs of the given programs wrt the imparted knowledge."""
        return sorted(
            (sum(map(self.taxon_cost, taxon_names)), program_name)
            for (program_name, taxon_names) in programs.items()
        )
