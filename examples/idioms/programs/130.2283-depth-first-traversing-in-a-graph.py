"""Depth-first traversing in a graph.

Call a function _f on every vertex accessible for vertex _v, in depth-first prefix order

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-08T19:17:47.214988Z
# Last modified on 2018-04-08T19:18:25.491984Z
# Version 2

# It's best to not recurse in Python when the structure size is unknown, since we have a fixed, small stack size.


def depth_first(start, f):
    seen = set()
    stack = [start]
    while stack:
        vertex = stack.pop()  # paroxython: -member_call_method:pop +member_call_method:list:pop
        f(vertex)
        seen.add(vertex)
        stack.extend(v for v in vertex.adjacent if v not in seen)
