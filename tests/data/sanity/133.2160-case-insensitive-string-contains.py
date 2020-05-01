"""Case-insensitive string contains.

Set boolean _ok to _true if string _word is contained in string _s as a substring, even if the case doesn't match, or to _false otherwise.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T12:37:36.700086Z
# Last modified on 2017-10-28T12:37:36.700086Z
# Version 1

ok = word.lower() in s.lower()
