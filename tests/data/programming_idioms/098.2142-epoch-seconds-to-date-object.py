"""Epoch seconds to date object.

Convert a timestamp _ts (number of seconds in epoch-time) to a date with time _d. E.g. 0 -> 1970-01-01 00:00:00

Source: elbrujohalcon
"""

# Implementation author: Oldboy
# Created on 2017-10-28T10:26:36.890877Z
# Last modified on 2017-10-28T10:26:36.890877Z
# Version 1

import datetime

d = datetime.date.fromtimestamp(ts)
