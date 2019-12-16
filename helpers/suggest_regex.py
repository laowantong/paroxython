import regex
import itertools

FIRST_PREFIX_MASK = r"\n(?:\1.+\n)*?\1/"
FIRST_PREFIX = " " * (len(FIRST_PREFIX_MASK) - len("^(.*?)/")) + "^(.*?)/"


class Suggestion:
    def __call__(self, source):
        self.source = source
        self.abstract_first_longest_prefix()
        self.abstract_line_numbers()
        return self.source

    def abstract_first_longest_prefix(self):
        rex = r"(?m)^(?P<PREFIX>.+)/(?P<SUFFIX>.+\n)(?:\1/(?P<SUFFIXES>.+\n))*"
        match = regex.search(rex, self.source)
        repl = [FIRST_PREFIX + match.captures("SUFFIX")[0]]
        for suffix in match.captures("SUFFIXES"):
            repl.append(FIRST_PREFIX_MASK + suffix)
        repl = "".join(repl)
        self.source = self.source[: match.start()] + repl + self.source[match.end() :]

    def abstract_line_numbers(self):
        self.source = regex.sub(r"lineno=\d+\n", r"lineno=(?P<LINE>\d+)\n", self.source)
