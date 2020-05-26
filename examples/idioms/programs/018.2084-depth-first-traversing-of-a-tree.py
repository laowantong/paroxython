"""Depth-first traversing of a tree.

Call a function _f on every node of a tree, in depth-first prefix order

Source: programming-idioms.org
"""

# Implementation author: cpoulet_42
# Created on 2017-08-09T09:20:28.30958Z
# Last modified on 2017-08-09T09:21:46.384451Z
# Version 2


def DFS(f, root):
    f(root)
    for child in root:
        DFS(f, child)
