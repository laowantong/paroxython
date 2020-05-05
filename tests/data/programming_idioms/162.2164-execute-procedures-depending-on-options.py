"""Execute procedures depending on options.

execute _bat if _b is a program option and _fox if _f is a program option.

Source: Bzzzzzzzzzz
"""

# Implementation author: Oldboy
# Created on 2017-10-28T13:18:02.415672Z
# Last modified on 2017-10-28T13:18:02.415672Z
# Version 1

import sys

if "b" in sys.argv[1:]:
    bat()
if "f" in sys.argv[1:]:
    fox()
