"""Trie.

Define a Trie data structure, where entries have an associated value.
(Not all nodes are entries)

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-08T19:10:28.833888Z
# Last modified on 2018-04-08T19:10:28.833888Z
# Version 1


class Trie:
    def __init__(self, prefix, value=None):
        self.prefix = prefix
        self.children = []
        self.value = value
