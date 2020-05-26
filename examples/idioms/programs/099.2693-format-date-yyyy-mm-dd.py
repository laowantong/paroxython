"""Format date YYYY-MM-DD.

Assign to string _x the value of fields (year, month, day) of date _d, in format _YYYY-_MM-_DD.

Source: programming-idioms.org
"""

# Implementation author: jessedhillon
# Created on 2019-09-26T13:46:18.91621Z
# Last modified on 2019-09-26T13:46:18.91621Z
# Version 1

from datetime import date

d = date.today()
x = d.isoformat()
