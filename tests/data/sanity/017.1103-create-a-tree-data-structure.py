"""Create a Tree data structure.

The structure must be recursive. A node may have zero or more children. A node has access to children nodes, but not to its parent.

Source: programming-idioms.org
"""

# Implementation author: nickname
# Created on 2016-02-18T16:57:57.310492Z
# Last modified on 2017-10-04T20:22:26.702125Z
# Version 2


class Node(object):
    def __init__(self, value, *children):
        self.value = value
        self.children = list(children)
