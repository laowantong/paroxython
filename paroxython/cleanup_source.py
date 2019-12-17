from token import DEDENT, INDENT, NEWLINE, STRING
from tokenize import COMMENT, NL, generate_tokens

import regex


def cleanup_factory(cleanup_strategy):
    cleanup = lambda source: source
    if cleanup_strategy == "strip_docs":
        sub_main = regex.compile(r"(?ms)^if +__name__ *== *.__main__. *:.+").sub
        sub_decorator = regex.compile(r"(?m)^\s*@.+\n").sub
        cleanup = lambda source: sub_decorator("", sub_main("", strip_docs(source)))
    return cleanup


replace_first_comments = regex.compile(r"\A(#.*\n)*").sub
replace_blank_lines = regex.compile(r"\s*\n").sub
replace_pass = regex.compile(r"(?m)^( *)pass\n\1(?!\s)").sub
replace_final_pass = regex.compile(r"(?m)^ *pass\Z").sub


def strip_docs(source):
    source = replace_first_comments("", source)
    source = source.replace("\t", "    ")
    result = []
    previous_token = INDENT
    previous_end_row = -1
    previous_end_col = 0
    lines = iter(source.split("\n"))
    for token_info in generate_tokens(lambda: next(lines) + "\n"):
        (token, string, (start_row, start_col), (end_row, end_col), _) = token_info
        # print(token_info)
        if start_row > previous_end_row:
            previous_end_col = 0
        result.append(" " * max(0, start_col - previous_end_col))
        if token == COMMENT:
            continue
        elif token == STRING and previous_token in (INDENT, DEDENT, NEWLINE):
            result.append("pass\n")  # replace the docstring by a pass statement
        else:
            result.append(string)
        if (previous_token, token) == (NEWLINE, NL):
            previous_token = NEWLINE
        else:
            previous_token = token
        previous_end_col = end_col
        previous_end_row = end_row
    result = "".join(result).strip()
    result = replace_blank_lines("\n", result)
    result = replace_pass(r"\1", result)  # suppress most useless pass statements
    return result


if __name__ == "__main__":
    source = open("../Python/maths/matrix_exponentiation.py").read()
    print(source)
    print("-" * 80)
    print(strip_docs(source))
