"""Create a Binary Tree data structure.

The structure must be recursive because _left child and _right child are binary trees too. A node has access to children nodes, but not to its parent.

Source: programming-idioms.org
"""

# Implementation author: atdt
# Created on 2019-09-27T03:58:30.712754Z
# Last modified on 2019-09-27T03:58:30.712754Z
# Version 1


class Node:
    def __init__(self, data, left_child, right_child):
        self.data = data
        self._left_child = left_child
        self._right_child = right_child
