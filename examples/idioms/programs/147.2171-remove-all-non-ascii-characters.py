"""Remove all non-ASCII characters.

Create string _t from string _s, keeping only ASCII characters

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-29T09:50:15.686412Z
# Last modified on 2017-10-29T09:50:15.686412Z
# Version 1

import re

t = re.sub("[^\u0000-\u007f]", "", s)
