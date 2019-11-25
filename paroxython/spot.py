class Spot:
    def __init__(self, line_numbers):
        if not (1 <= len(line_numbers) <= 2):
            raise NotImplementedError
        self.line_numbers = tuple(sorted(map(int, line_numbers)))
        self.start = self.line_numbers[0]
        if len(line_numbers) == 1:
            self.end = self.start
            self.length = 0
            self.string = f"{self.start}"
            self.suffix = ""
        else:
            self.end = self.line_numbers[1]
            self.length = self.end - self.start
            self.string = f"{self.start}-{self.end}"
            self.suffix = f" (-> +{self.length})"

    def __str__(self):
        return self.string
    
    def __lt__(self, other):
        return (self.start, self.end) < (other.start, other.end)
