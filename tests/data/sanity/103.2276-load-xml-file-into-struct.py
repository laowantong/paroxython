"""Load XML file into struct.

Read from file _data._xml and write its content into object _x.
Assume the XML data is suitable for the type of _x. 

Source: programming-idioms.org
"""

# Implementation author: bukzor
# Created on 2018-04-08T07:25:34.222994Z
# Last modified on 2018-04-08T07:25:34.222994Z
# Version 1

# Use "pip install" to get this third-party library. It's industry standard for python xml.

import lxml.etree

x = lxml.etree.parse("data.xml")
