"""Graph with adjacency lists.

Declare a _Graph data structure in which each _Vertex has a collection of its neighbouring vertices. As an example, set _G to a representation of the "bull graph": https://en.wikipedia.org/wiki/Bull_graph

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-08T18:52:18.110083Z
# Last modified on 2018-04-08T18:52:18.110083Z
# Version 1

from collections import defaultdict


class Vertex(set):
    pass


class Graph(defaultdict):
    def __init__(self, *paths):
        self.default_factory = Vertex
        for path in paths:
            self.make_path(path)

    def make_path(self, labels):
        for l1, l2 in zip(labels, labels[1:]):
            self[l1].add(l2)
            self[l2].add(l1)


G = Graph((0, 1, 2, 3), (1, 4, 2))
