"""Create temp directory.

Create a new temporary folder on filesystem, for writing.

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2017-10-28T12:53:16.156619Z
# Last modified on 2017-11-18T23:25:38.458057Z
# Version 2

# tempfile._TemporaryDirectory() was added in Python 3.2 .
# It wraps lower-level function _mkdtemp() .

import tempfile

td = tempfile.TemporaryDirectory()
