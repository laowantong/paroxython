"""Tomorrow.

Assign to variable _t a string representing the day, month and year of the day after the current date. 

Source: steenslag
"""

# Implementation author: citizenkong
# Created on 2019-09-26T13:50:47.638084Z
# Last modified on 2019-09-26T13:50:47.638084Z
# Version 1

from datetime import date, timedelta

date.today() + timedelta(days=1)
