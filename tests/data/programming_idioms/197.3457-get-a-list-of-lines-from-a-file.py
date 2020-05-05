"""Get a list of lines from a file.

Retrieve the contents of file at _path into a list of strings _lines, in which each element is a line of the file.

Source: Jadiker
"""

# Implementation author: Jadiker
# Created on 2019-09-28T17:00:28.690784Z
# Last modified on 2019-09-28T20:49:36.126049Z
# Version 3

with open(path) as f:
    lines = f.readlines()
