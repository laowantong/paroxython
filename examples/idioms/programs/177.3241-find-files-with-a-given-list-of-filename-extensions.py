"""Find files with a given list of filename extensions.

Construct a list _L that contains all filenames that have the extension ".jpg" , ".jpeg" or ".png" in directory _D and all it's subdirectories.

Source: Bart
"""

# Implementation author: charlax
# Created on 2019-09-27T11:33:27.420533Z
# Last modified on 2019-09-27T11:33:27.420533Z
# Version 1

import glob
import itertools

list(itertools.chain(*(glob.glob("*/**.%s" % ext) for ext in ["jpg", "jpeg", "png"])))
