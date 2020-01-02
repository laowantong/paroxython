import regex  # type: ignore

from declarations import Source

rex = regex.compile(r"(?m)^\s*# paroxython: (.+)\n")


def centrifugate_hints(source: Source) -> Source:
    """Transform the isolated hints into all-encompassing hints."""
    hint_strings = rex.findall(source)
    if not hint_strings:
        return source
    source = rex.sub("", source)
    lines = source.split("\n")
    for i in (0, -1):
        if " # paroxython:" not in lines[i]:
            lines[i] += " # paroxython:"
    for hint_string in hint_strings:
        for hint in hint_string.split():
            lines[0] += f" {hint}..."
            lines[-1] += f" ...{hint}"
    return Source("\n".join(lines))
