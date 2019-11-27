
class Spot:

    existing_instances = {}

    def __new__(cls, line_numbers):
        """Prevent the creation of distinct instances for identical spots.
        
        It avoids wasting memory and facilitates the deduplication of a list of spots.
        Reference: https://stackoverflow.com/a/50820933
        """
        key = (int(line_numbers[0]), int(line_numbers[-1]))
        if key in cls.existing_instances:
            return cls.existing_instances[key]
        self = super().__new__(cls)
        # __init__ logic goes here  -- will only run once
        self.line_numbers = key
        (self.start, self.end) = self.line_numbers
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
        
    def __lt__(self, other):
        return (self.start, self.end) < (other.start, other.end)
