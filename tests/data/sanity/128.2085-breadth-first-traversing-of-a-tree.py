"""Breadth-first traversing of a tree.

Call a function _f on every node of a tree, in breadth-first prefix order

Source: programming-idioms.org
"""

# Implementation author: cpoulet_42
# Created on 2017-08-09T09:52:02.728772Z
# Last modified on 2017-08-09T22:27:55.685981Z
# Version 2


def BFS(f, root):
    Q = [root]
    while Q:
        n = Q.pop(0)
        f(n)
        for child in n:
            if not n.discovered:
                n.discovered = True
                Q.append(n)
