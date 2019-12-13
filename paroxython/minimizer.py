"""
.. module:: minimizer
	:author: Alexander S. Groden (adaptated for Paroxython by Aristide Grange)
	:synopsis: Minimizes Python code using Python's lexical scanning tokenize module.
"""


from io import StringIO
from token import COMMENT, DEDENT, ENDMARKER, INDENT, NAME, NEWLINE, NL, OP, STRING
from tokenize import generate_tokens


# classes / helpers ############################################################
def enum(*sequential, **named):
    """Makes an enum type with a reverse mapping for lookup of the enum string.
	Included for portability sake.
	Taken from: https://stackoverflow.com/a/1695250
	"""
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.items())
    enums["reverse_mapping"] = reverse
    return type("Enum", (), enums)


class TokenGroup(object):
    """A class for keeping track of a group of tokens.
	Token groups are meant to be a collection of tokens that are lexicographically 
	adjacent on a line. This helps to easily remove comments, docstrings, and 
	blank lines.
	"""

    Type = enum(
        "UNKNOWN",
        "CODE",
        "CODE_INLINE_COMMENT",
        "COMMENT",
        "DOCSTRING",
        "BLANK_LINE",
        "SHEBANG",
        "INDENT",
        "DEDENT",
        "EOF",
    )

    _WORD_OPS = ("and", "or", "not", "is", "in", "for", "while", "return")

    def __init__(self):
        self._tokens = []
        self._finalized = False
        self.type = TokenGroup.Type.UNKNOWN

    def untokenize(self, rmwspace=False, wspace_char=" "):
        """Untokenize this group.
		"""
        ret = ""
        prev = None
        for tok in self._tokens:
            if tok[0] != NEWLINE and tok[0] != NL:
                if prev:
                    if rmwspace:
                        if (
                            (prev[0] in (NAME, NUMBER) and tok[0] in (NAME, NUMBER))
                            or (prev[0] == OP and tok[1] in self._WORD_OPS)
                            or (tok[0] in (OP, STRING) and prev[1] in self._WORD_OPS)
                        ):
                            ret = "".join([ret, wspace_char])
                    else:
                        # tok[2][1]: start column, prev[3][1]: end column
                        # the difference between the two indicates whitespace
                        if prev and tok[2][1] > prev[3][1]:
                            ret = "".join([ret, wspace_char * (tok[2][1] - prev[3][1])])
                ret = "".join([ret, tok[1].rstrip()])
                prev = tok
        return ret

    def append(self, tok):
        """Append a token to this group. Will update the group type as needed.
		"""

        def get_type(t):
            if t[0] == NAME or tok[0] == OP:
                return TokenGroup.Type.CODE
            elif t[0] == COMMENT:
                if t[1].startswith("#!"):
                    return TokenGroup.Type.SHEBANG
                return TokenGroup.Type.COMMENT
            elif t[0] == STRING:
                return TokenGroup.Type.DOCSTRING
            elif t[0] == NL:
                return TokenGroup.Type.BLANK_LINE
            elif t[0] == INDENT:
                return TokenGroup.Type.INDENT
            elif t[0] == DEDENT:
                return TokenGroup.Type.DEDENT
            elif t[0] == ENDMARKER:
                return TokenGroup.Type.EOF

        # function body #
        self._tokens.append(tok)
        if self.type == TokenGroup.Type.UNKNOWN:
            self.type = get_type(tok)
        elif self.type == TokenGroup.Type.CODE and tok[0] == COMMENT:
            self.type = TokenGroup.Type.CODE_INLINE_COMMENT
        elif self.type == TokenGroup.Type.BLANK_LINE:
            self.type = get_type(tok)
        elif self.type == TokenGroup.Type.DOCSTRING and tok[0] not in (STRING, NEWLINE):
            self.type = get_type(tok)

    def __str__(self):
        """Prints TokenGroup information for easier debugging.
		"""

        def readable_token(tok):
            return "({}, {}, {}, {}, {})".format(
                tok_name[tok[0]], repr(tok[1]), tok[2], tok[3], repr(tok[4])
            )

        # function body #
        return "TokenGroup {{ type: {}, tokens: [{}] }}".format(
            TokenGroup.Type.reverse_mapping[self.type],
            ", ".join([readable_token(tok) for tok in self._tokens]),
        )


# module functions #############################################################
def group_tokens(sbuf):
    """Groups tokens by line. Splits indents and dedents into their own group.
	"""
    io_wrapper = StringIO(sbuf)
    groups = []
    group = TokenGroup()
    bracket_ctr = 0
    for tok in generate_tokens(io_wrapper.readline):
        if tok[0] in (NEWLINE, NL, ENDMARKER, INDENT, DEDENT):
            group.append(tok)
            groups.append(group)
            group = TokenGroup()
        else:
            group.append(tok)
    return groups


def untokenize(tgroups, rmwspace=False, wspace_char=" ", indent_char="\t"):
    """Untokenizes groups of tokens into a string.
	Can optionally remove whitespace and change the whitespace and indent character.
	"""
    ret = []
    indent_lvl = 0
    for grp in tgroups:
        if grp.type == TokenGroup.Type.INDENT:
            indent_lvl += 1
            continue
        elif grp.type == TokenGroup.Type.DEDENT:
            indent_lvl -= 1
            continue
        elif grp.type == TokenGroup.Type.EOF:
            continue
        ret.append(
            "".join([indent_char * indent_lvl, grp.untokenize(rmwspace, wspace_char)])
        )
    return "\n".join(ret)


def remove_blank_lines(token_groups):
    """Removes blank lines from the token groups.
	"""
    return [grp for grp in token_groups if grp.type != TokenGroup.Type.BLANK_LINE]


def remove_docstrings(token_groups):
    """Removes docstrings from the token groups.
	"""
    return [grp for grp in token_groups if grp.type != TokenGroup.Type.DOCSTRING]


def remove_comments(token_groups):
    """Removes comment lines and inline comments from the token groups.
	"""
    inline_comment_ctr = 0
    tmp = []
    for grp in token_groups:
        if grp.type == TokenGroup.Type.CODE_INLINE_COMMENT:
            group = TokenGroup()
            for tok in grp._tokens:
                if tok[0] != COMMENT:
                    group.append(tok)
                    inline_comment_ctr += 1
            tmp.append(group)
        else:
            tmp.append(grp)
    ret = [grp for grp in tmp if grp.type != TokenGroup.Type.COMMENT]
    return ret


def minimize(
    sbuf,
    rm_blank_lines=True,
    rm_comments=True,
    rm_docstrings=True,
    rm_whitespace=False,
    whitespace_char=" ",
    indent_char=" " * 4,
):
    """Convenience function for performing all the possible minimization functions.
	"""
    grps = group_tokens(sbuf)
    if rm_blank_lines:
        grps = remove_blank_lines(grps)
    if rm_comments:
        grps = remove_comments(grps)
    if rm_docstrings:
        grps = remove_docstrings(grps)
    return untokenize(grps, rm_whitespace, whitespace_char, indent_char)


if __name__ == "__main__": # pragma: no cover
    from pathlib import Path

    source = Path("../Algo/programs/damm_checksum_0.py").read_text()
    print(minimize(source))
