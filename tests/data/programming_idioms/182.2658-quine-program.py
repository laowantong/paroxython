"""Quine program.

Output the source of the program.

Source: a
"""

# Implementation author: a
# Created on 2019-07-04T06:26:53.861091Z
# Last modified on 2019-07-04T06:26:53.861091Z
# Version 1

s = "s = %r\nprint(s%%s)"
print(s % s)
