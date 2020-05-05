"""First-class function : generic composition.

Implement a function _compose which returns composition function _g ∘ _f  for any functions _f and _g having exactly 1 parameter.

Source: programming-idioms.org
"""

# Implementation author: cym13
# Created on 2016-02-18T16:57:58.963839Z
# Last modified on 2016-02-18T16:57:58.963839Z
# Version 1

# This is the same as for non-generic composition


def compose(f, g):
    return lambda x: g(f(x))
