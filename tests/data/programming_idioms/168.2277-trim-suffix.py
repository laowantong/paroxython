"""Trim suffix.

Create string _t consisting of string _s with its suffix _w removed (if _s ends with _w).

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-08T07:26:47.248912Z
# Last modified on 2018-04-08T07:26:47.248912Z
# Version 1

t = s.rsplit(w, 1)[0]
