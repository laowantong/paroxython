class Span:
    """Metadata associated with a tag (i.e., a label or a taxon).
    Currently, a span is a couple of line numbers delimiting a construct in a source.
    Implemented as a Registry of singletons (GoF's Design Patterns), or Multiton.
    """

    existing_instances = {}

    def __new__(cls, line_numbers):
        """Prevent the creation of distinct instances for identical spans.
        It avoids wasting memory and facilitates the deduplication of a list of spans.
        Reference: https://stackoverflow.com/a/50820933
        """
        key = (int(line_numbers[0]), int(line_numbers[-1]))
        if key in cls.existing_instances:
            return cls.existing_instances[key]
        self = super().__new__(cls)
        # __init__ logic goes here  -- will only run once
        (self.start, self.end) = key
        self.length = self.end - self.start
        if self.length == 0:
            self.string = f"{self.start}"
            self.suffix = ""
        else:
            self.string = f"{self.start}-{self.end}"
            self.suffix = f" (-> +{self.length})"
        # __init__ logic ends here
        cls.existing_instances[key] = self
        return self

    def __str__(self):
        return self.string

    def __repr__(self):
        return self.string

    def to_couple(self):
        return (self.start, self.end)

    def __lt__(self, other):
        return (self.start, self.end) < (other.start, other.end)
