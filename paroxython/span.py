from typing import Dict, List, Tuple, Type, Union


class CachedSpan(type):
    """Prevent the creation of distinct instances for identical spans.
    It avoids wasting memory and facilitates the deduplication of a list of spans.
    References:
    - Code: https://stackoverflow.com/a/50821287/173003
    - Typing: https://mypy.readthedocs.io/en/latest/kinds_of_types.html#class-name-forward-references
    """

    existing_instances: Dict[Tuple[int, int], "CachedSpan"] = {}

    def __call__(cls, line_numbers):
        key = (int(line_numbers[0]), int(line_numbers[-1]))
        if key not in cls.existing_instances:
            cls.existing_instances[key] = super(CachedSpan, cls).__call__(line_numbers)
        return cls.existing_instances[key]


class Span(metaclass=CachedSpan):
    """Metadata associated with a tag (i.e., a label or a taxon).
    Currently, a span is a couple of line numbers delimiting a construct in a source.
    Implemented as a Registry of singletons (GoF's Design Patterns), or Multiton.
    """

    def __init__(self, line_numbers: Union[List[str], List[int]]) -> None:
        key = (int(line_numbers[0]), int(line_numbers[-1]))
        (self.start, self.end) = key
        self.length = self.end - self.start
        if self.length == 0:
            self.string = f"{self.start}"
            self.suffix = ""
        else:
            self.string = f"{self.start}-{self.end}"
            self.suffix = f" (-> +{self.length})"

    def __str__(self) -> str:
        return self.string

    def __repr__(self) -> str:
        return self.string

    def to_couple(self) -> Tuple[int, int]:
        return (self.start, self.end)

    def __lt__(self, other) -> bool:
        return (self.start, self.end) < (other.start, other.end)
