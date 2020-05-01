"""First-class function : compose.

Implement a function _compose (_A -> _C) with parameters _f (_A -> _B) and _g (_B -> _C), which returns composition function _g ∘ _f

Source: programming-idioms.org
"""

# Implementation author: cym13
# Created on 2015-11-30T12:37:28.120844Z
# Last modified on 2015-11-30T12:37:28.120844Z
# Version 1

# We could have used a named function but a lambda is shorter


def compose(f, g):
    return lambda a: g(f(a))
