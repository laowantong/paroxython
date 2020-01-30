from typing import Dict, List, Tuple, Union


class Span:
    """Metadata associated with a tag (i.e., a label or a taxon).
    Currently, a span consists in:
    - a couple of line numbers delimiting a feature in a source,
    - the indentation level of the first line,
    - the path of the feature (useful for any nested expression)
    Implemented as a Registry of singletons (GoF's Design Patterns), or Multiton.
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
        self.length = self.end - self.start
        if self.length == 0:
            self.string = f"{self.start}"
            self.suffix = ""
        else:
            self.string = f"{self.start}-{self.end}"
            self.suffix = f" (-> +{self.length})"
        self.hash = hash((self.start, self.end, self.path))

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
