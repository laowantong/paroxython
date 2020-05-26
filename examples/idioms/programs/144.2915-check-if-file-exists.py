"""Check if file exists.

Set boolean _b to _true if file at path _fp exists on filesystem; _false otherwise.

Beware that you should never do this and then in the next instruction assume the result is still valid, this is a race condition on any multitasking OS.

Source: programming-idioms.org
"""

# Implementation author: ims
# Created on 2019-09-26T17:01:46.595718Z
# Last modified on 2019-09-26T17:02:43.549382Z
# Version 3

from pathlib import Path

b = Path(fp).exists()
