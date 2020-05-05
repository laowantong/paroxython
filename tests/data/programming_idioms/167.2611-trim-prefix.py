"""Trim prefix.

Create string _t consisting of string _s with its prefix _p removed (if _s starts with _p).

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2019-02-11T19:53:53.767084Z
# Last modified on 2019-02-11T19:53:53.767084Z
# Version 1

t = s[s.startswith(p) and len(p) :]
