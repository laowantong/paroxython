"""Regex with character repetition.

Declare regular expression _r matching strings "http", "htttp", "httttp", etc.

Source: deleplace
"""

# Implementation author: iLoveTux
# Created on 2016-08-24T02:53:23.462835Z
# Last modified on 2016-08-24T02:53:23.462835Z
# Version 1

import re

r = re.compile(r"htt+p")
