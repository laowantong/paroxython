"""Create a Binary Tree data structure.

The structure must be recursive because _left child and _right child are binary trees too. A node has access to children nodes, but not to its parent.

Source: programming-idioms.org
"""

# Implementation author: TinyFawks
# Created on 2016-02-18T16:57:56.226523Z
# Last modified on 2016-02-18T16:57:56.226523Z
# Version 1


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
