r"""Assess the learning cost associated with the introduction of the given programs.

Each program has been previously found to implement a number of notions represented by a list of
taxa of the form: \(\textrm{edge}_0/\textrm{edge}_1/.../\textrm{edge}_n\), e.g.,
`flow/loop/exit/early/break`.

Furthermore, the notions already imparted may cover a certain **prefix** of such a taxon, here, e.g.
`flow/loop`. The learning cost should therefore not take this into account.

The cost of the remaining edges, here `exit/early/break`, is approximated by a function taking
two zero-based indexes `start` (inclusive) and `stop` (exclusive), and returning a floating number. Currently, only two such functions are provided:

1. `range_to_cost_linear()`, which simply counts the number of edges;
2. `range_to_cost_zeno()`, which calculates the sum of a decreasing function of the positions
   (with the assumption that the introduction of a sub-concept costs half that of its parent concept).
"""

from functools import lru_cache

from .user_types import (
    AssessedPrograms,
    AssessmentStrategy,
    ProgramInfos,
    ProgramPathSet,
    TaxonName,
    TaxonNameSet,
)

__pdoc__ = {
    "LearningCostAssessor.__call__": True,
    "LearningCostAssessor.__init__": True,
    "LearningCostAssessor": "",
}


@lru_cache(maxsize=None)  # NB: memoization needed for consistency with mypy's typing
def range_to_cost_linear(start: int, stop: int) -> float:
    """Return the length of the slice between `start` (inclusive) and `stop` (exclusive)."""
    return float(stop - start)


@lru_cache(maxsize=None)
def range_to_cost_zeno(start: int, stop: int) -> float:
    r"""Calculate the sum of the given slice of a [Zeno's geometric series](https://en.wikipedia.org/wiki/Zeno%27s_paradoxes#Dichotomy_paradox).

    Specifically: $$\sum_{i=\textrm{start}}^{\textrm{stop}-1}{\frac{1}{2^{i+1}}}$$

    Since it converges absolutely towards 1, the returned value is in the interval \([0, 1[\).

    <center><a title="Jim.belk / Public domain" href="https://commons.wikimedia.org/wiki/File:Geometric_Segment.svg"><img width="256" alt="Geometric Segment" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Geometric_Segment.svg/256px-Geometric_Segment.svg.png"></a></center>

    Example:
        If `flow/loop` is already imparted, the learning cost of `flow/loop/exit/early/break` will
        be:

    >>> range_to_cost_zeno(2, 5)
    0.21875

    Indeed,
    \(\frac{1}{2^3}+\frac{1}{2^4}+\frac{1}{2^5}=\frac{1}{8}+\frac{1}{16}+\frac{1}{32}=0.21875\).

    """
    return sum(2 ** ~i for i in range(start, stop))


class LearningCostAssessor:
    """Evaluate the learning costs of programs with respect to the given imparted knowledge."""

    def __init__(self, programs: ProgramInfos, assessment_strategy: AssessmentStrategy = "zeno"):
        """Set the programs and the function to be used for the learning cost calculation.

        Args:
            assessment_strategy (str, optional): Either:

                - `"zeno"`: `range_to_cost_zeno` (default).
                - `"linear"`: `range_to_cost_linear`.

        Raises:
            NotImplementedError: Raised in case of unknown `assessment_strategy`.
        """
        self.programs = programs
        if assessment_strategy.lower() == "zeno":
            self.range_to_cost = range_to_cost_zeno
        elif assessment_strategy == "linear":
            self.range_to_cost = range_to_cost_linear
        else:
            raise NotImplementedError
        self.range_to_cost.cache_clear()
        self.taxon_cost.cache_clear()

    def set_imparted_knowledge(self, imparted_knowledge: TaxonNameSet) -> None:
        self.imparted_knowledge = imparted_knowledge

    @lru_cache(maxsize=None)
    def taxon_cost(self, taxon: TaxonName) -> float:
        """Evaluate the learning cost of a given taxon.

        The bounds of the not-yet-imparted suffix of the taxon are extracted and passed to the cost
        assessment function.

        .. note::
          The learning cost of a taxon prefixed by `"meta/"` is assumed to be zero.
        """
        if taxon.startswith("meta/"):
            return 0
        (start, stop) = (0, 0)
        if taxon not in self.imparted_knowledge:
            edges = taxon.split("/")
            stop = len(edges)
            for start in range(stop - 1, -1, -1):
                if "/".join(edges[:start]) in self.imparted_knowledge:
                    break
        return self.range_to_cost(start, stop)

    def __call__(self, selected_programs: ProgramPathSet) -> AssessedPrograms:
        """Associate the given selected programs with the total learning cost of their taxa.

        Args:
            selected_programs (ProgramPathSet): A set of program paths.

        Returns:
            AssessedPrograms: A list of tuples `(total_cost, ProgramPath)` sorted by increasing cost.
        """
        result = []
        for program_path in selected_programs:
            total_cost = 0.0
            for taxon_name in self.programs[program_path]["taxa"]:
                total_cost += self.taxon_cost(taxon_name)
            result.append((total_cost, program_path))
        return sorted(result)
