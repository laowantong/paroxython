"""Source code inclusion.

Import the source code for the function _foo body from a file  "foobody.txt" . The declaration must not reside in the external file.

Source: MLKo
"""

# Implementation author: bukzor
# Created on 2018-04-08T07:19:33.894869Z
# Last modified on 2018-04-08T07:20:06.900516Z
# Version 2

# To remove all side-effects: del sys.modules['foobody']

import imp

foo = imp.load_module("foobody", "foobody.txt").foo
