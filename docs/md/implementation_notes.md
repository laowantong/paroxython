# Implementation notes

## User types

Paroxython makes heavy use of Python 3.5+ [type hints](https://docs.python.org/3/library/typing.html). They are documented directly in [user_types.py](https://repo/paroxython/user_types.py).

## Default argument trick

Several functions or methods declare a compiled and bound regex pattern as an optional argument (see `paroxython.normalize_predicate.normalize_predicate` for an example). Such arguments are not meant to be provided by the caller. Their default value will be used systematically, with the benefit of being evaluated only once. This is arguably better for both performance and encapsulation. More details on [Stack Overflow](https://stackoverflow.com/a/30688691/173003).
