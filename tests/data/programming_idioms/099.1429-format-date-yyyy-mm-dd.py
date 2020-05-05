"""Format date YYYY-MM-DD.

Assign to string _x the value of fields (year, month, day) of date _d, in format _YYYY-_MM-_DD.

Source: programming-idioms.org
"""

# Implementation author: TinyFawks
# Created on 2016-02-18T16:58:02.675046Z
# Last modified on 2019-09-26T13:38:52.570471Z
# Version 3

from datetime import date

d = date(2016, 9, 28)
x = d.strftime("%Y-%m-%d")
