from token import DEDENT, INDENT, NEWLINE, STRING
from tokenize import COMMENT, NL, generate_tokens
from typing import Callable

import regex  # type: ignore

from declarations import SourceText


def cleanup_factory(cleanup_strategy: str) -> Callable[[SourceText], SourceText]:
    cleanup = lambda source: source
    if cleanup_strategy == "strip_docs":
        sub_main = regex.compile(r"(?ms)^if +__name__ *== *.__main__. *:.+").sub
        sub_decorator = regex.compile(r"(?m)^\s*@.+\n").sub
        cleanup = lambda source: sub_decorator("", sub_main("", strip_docs(source)))
    return cleanup


sub_first_comments = regex.compile(r"\A(#.*\n)*").sub
sub_blank_lines = regex.compile(r"\s*\n").sub
sub_pass = regex.compile(r"(?m)^( *)pass\n\1(?!\s)").sub
sub_final_pass = regex.compile(r"(?m)^ *pass\Z").sub
subn_paroxython_comment = regex.compile(r"(?i)#\s*paroxython\s*:\s*").subn


def strip_docs(source: SourceText) -> SourceText:
    result = []
    previous_token = INDENT
    (previous_end_row, previous_end_col) = (-1, 0)
    lines = iter(sub_first_comments("", source).replace("\t", "    ").split("\n"))
    for token_info in generate_tokens(lambda: next(lines) + "\n"):
        (token, string, (start_row, start_col), (end_row, end_col), _) = token_info
        if start_row > previous_end_row:
            previous_end_col = 0
        result.append(" " * max(0, start_col - previous_end_col))
        if token == COMMENT:
            (string, n) = subn_paroxython_comment("# paroxython: ", string)
            if n == 0:
                continue
            result.append(string)
        elif token == STRING and previous_token in (INDENT, DEDENT, NEWLINE):
            result.append("pass\n")  # replace the docstring by a pass statement
        else:
            result.append(string)
        if (previous_token, token) == (NEWLINE, NL):
            previous_token = NEWLINE
        else:
            previous_token = token
        (previous_end_row, previous_end_col) = (end_row, end_col)
    text = "".join(result).strip()
    text = sub_blank_lines("\n", text)
    text = sub_pass(r"\1", text)  # suppress most useless pass statements
    return SourceText(text)


if __name__ == "__main__":
    source = open("../Python/maths/matrix_exponentiation.py").read()
    lines = source.split("\n")
    lines[13] += " # paroxython: test"
    source = SourceText("\n".join(lines))
    print(source)
    print("-" * 80)
    print(strip_docs(source))
