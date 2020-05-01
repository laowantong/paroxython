"""Breadth-first traversing in a graph.

Call a function _f on every vertex accessible from vertex _start, in breadth-first prefix order

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-08T19:15:40.73175Z
# Last modified on 2018-04-08T19:15:40.73175Z
# Version 1

# It's best to not recurse in Python when the structure size is unknown, since we have a fixed, small stack size.

from collections import deque


def breadth_first(start, f):
    seen = set()
    q = deque([start])
    while q:
        vertex = q.popleft()
        f(vertex)
        seen.add(vertex)
        q.extend(v for v in vertex.adjacent if v not in seen)
