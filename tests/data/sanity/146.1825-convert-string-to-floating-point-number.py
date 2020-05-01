"""Convert string to floating point number.

Extract floating point value _f from its string representation _s

Source: programming-idioms.org
"""

# Implementation author: cons0l3
# Created on 2016-09-14T08:41:41.829008Z
# Last modified on 2016-09-17T21:39:03.333125Z
# Version 2

# When working with different locale decimal and thousand separators you have to use _locale._atof

import locale

s = u"545,2222"
locale.setlocale(locale.LC_ALL, "de")
f = locale.atof(s)
