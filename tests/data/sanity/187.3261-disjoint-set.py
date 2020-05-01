"""Disjoint Set.

Disjoint Sets hold elements that are partitioned into a number of disjoint (non-overlapping) sets.

Source: Shaftway
"""

# Implementation author: Fazel94
# Created on 2019-09-27T14:01:40.750605Z
# Last modified on 2019-09-27T14:01:40.750605Z
# Version 1


class UnionFind:
    def __init__(self, size):
        self.rank = [0] * size
        self.p = [i for i in range(size)]

    def find_set(self, i):
        if self.p[i] == i:
            return i
        else:
            self.p[i] = self.find_set(self.p[i])
            return self.p[i]

    def is_same_set(self, i, j):
        return self.find_set(i) == self.find_set(j)

    def union_set(self, i, j):
        if not self.is_same_set(i, j):
            x, y = self.find_set(i), self.find_set(j)
