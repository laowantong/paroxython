"""Extract file content to a string.

Create string _lines from the content of the file with filename _f.

Source: programming-idioms.org
"""

# Implementation author: cym13
# Created on 2016-02-18T16:58:00.469157Z
# Last modified on 2016-02-18T16:58:00.469157Z
# Version 1

# For more complicated file operations, use a context manager with "with"

lines = open(f).read()
