"""Delete map entry.

Delete from map _m the entry having key _k.

Explain what happens if _k is not an existing key in _m.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T12:10:35.967798Z
# Last modified on 2017-10-28T12:13:29.517006Z
# Version 2

# A missing key will leave the map unchanged.
#
# If the second parameter is omitted, a missing key will raise the exception _KeyError

m.pop(k, None)
