"""Depth-first traversing of a binary tree.

Call a function _f on every node of binary tree _bt, in depth-first infix order

Source: programming-idioms.org
"""

# Implementation author: TinyFawks
# Created on 2016-02-18T08:50:27.130406Z
# Last modified on 2016-02-18T09:16:52.625429Z
# Version 2

# Recursive DFS.


def dfs(bt):
    if bt is None:
        return
    dfs(bt.left)
    f(bt)
    dfs(bt.right)
