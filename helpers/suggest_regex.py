import regex  # type: ignore
import itertools

FIRST_PREFIX_MASK = r"\n(?:\1.+\n)*?\1/"
FIRST_PREFIX = " " * (len(FIRST_PREFIX_MASK) - len("^(.*)/")) + "^(.*)/"


class Suggestion:
    """Suggest a regex matching a selection of lines in a flat AST."""

    def __call__(self, source):
        self.s = source
        self.abstract_first_longest_prefix()
        self.abstract_position()
        for key in ("name", "id", "_hash", "_ids"):
            self.capture_and_match_key(key)
        self.abstract_body_prefix()
        self.restore_first_prefix()
        self.restore_greedy_quantifiers()
        return self.s

    def abstract_first_longest_prefix(self):
        rex = r"(?m)\A\s*(?P<PREFIX>(?:/(?:body|orelse)/\d+)+)/(?P<SUFFIX>.+\n)(?:\1/(?P<SUFFIXES>.+\n))+\Z"
        match = regex.search(rex, self.s)
        repl = [FIRST_PREFIX_MASK + match.captures("SUFFIX")[0]]
        for suffix in match.captures("SUFFIXES"):
            repl.append(FIRST_PREFIX_MASK + suffix)
        self.s = self.s[: match.start()] + "".join(repl) + self.s[match.end() :]

    def abstract_position(self):
        self.s = regex.sub(r"_pos=.+\n", r"_pos=(?P<POS>.+)\n", self.s)

    def capture_and_match_key(self, key):
        rex = fr"(?ms)/(?P<KEY>{key})=(?P<VALUE>['\"\w_]+)((?P<SKIPS>\n.+?)(?P<KEYS>{key})=\2)+"
        name = key.upper().replace("_", "")
        for i in itertools.count(1):
            match = regex.search(rex, self.s)
            if not match:
                break
            d = match.capturesdict()
            key = d["KEY"][0]
            repl = [fr"/{key}=(?P<{name}_{i}>.+) # capture {key} #{i}"]
            for (skip, key) in zip(d["SKIPS"], d["KEYS"]):
                repl.append(fr"{skip}{key}=(?P={name}_{i}) # match {key} #{i}")
            self.s = self.s[: match.start()] + "".join(repl) + self.s[match.end() :]
        if fr"(?P={name}_2)" not in self.s:  # no need for numeric suffix
            self.s = self.s.replace(fr"(?P<{name}_1>.+)", fr"(?P<{name}>.+)")
            self.s = self.s.replace(fr"(?P={name}_1)", fr"(?P={name})")
            self.s = self.s.replace(fr" {key} #1", fr" {key}")

    def abstract_body_prefix(self):
        rex = fr"(?m)^(?P<SKIP>.+?)/(?P<PREFIX>(?:body|orelse)/\d+)/(?P<SUFFIX>.+\n)(?:\1/\2/(?P<SUFFIXES>.+\n))+"
        for i in itertools.count(1):
            match = regex.search(rex, self.s)
            if not match:
                break
            d = match.capturesdict()
            prefix = fr"(?P<_{i}>(?:body|orelse)/\d+)"
            repl = [fr"{d['SKIP'][0]}/{prefix}/{d['SUFFIX'][0]}"]
            offset = " " * (len(r"(?:body|orelse)/\d+") + 1)
            for suffix in match.captures("SUFFIXES"):
                repl.append(fr"{d['SKIP'][0]}/(?P=_{i}){offset}/{suffix}")
            self.s = self.s[: match.start()] + "".join(repl) + self.s[match.end() :]

    def restore_greedy_quantifiers(self):
        result = []
        for line in self.s.split("\n"):
            if r"(?:body|orelse)/\d+" in line:
                result.append(line.replace("*?", "* ", 1))
            else:
                result.append(line)
        self.s = "\n".join(result)

    def restore_first_prefix(self):
        self.s = self.s.replace(FIRST_PREFIX_MASK, FIRST_PREFIX, 1)


if __name__ == "__main__":
    suggestion = Suggestion()
    source = __import__("pathlib").Path("sandbox/flat_ast_selection.txt").read_text()
    print(suggestion(source))
