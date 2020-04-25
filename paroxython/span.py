from typing import List, Tuple

from goodies import couple_to_string


class Span:
    """Metadata associated with a tag (i.e., a label or a taxon).

    Currently, a span consists in:
    - a couple of line numbers delimiting a feature in a source,
    - the path of the feature (useful for any nested expression).
    """

    def __init__(self, pos: List) -> None:
        data = (pos[0], pos[-1])  # keep only the both ends of the position data
        try:
            (start, self.path) = data[0].split(":")
            self.start = int(start)
            self.end = int(data[1].partition(":")[0])
        except (TypeError, ValueError, AttributeError):  # for testing purpose only
            self.start = int(data[0])
            self.end = int(data[1])
            self.path = ""
        couple = (self.start, self.end)
        self.hash = hash(couple)
        self.string = couple_to_string(couple)
        self.length = self.end - self.start
        self.suffix = f" (-> +{self.length})" if self.length else ""

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return self.string

    def to_couple(self) -> Tuple[int, int]:
        return (self.start, self.end)

    def __lt__(self, other) -> bool:
        return (self.start, self.end) < (other.start, other.end) or (
            (self.start, self.end) == (other.start, other.end) and self.path < other.path
        )

    def __eq__(self, other):
        if self.path and other.path:
            return (self.start, self.end) == (other.start, other.end) and self.path == other.path
        else:
            return (self.start, self.end) == (other.start, other.end)

    def __hash__(self):
        return self.hash
