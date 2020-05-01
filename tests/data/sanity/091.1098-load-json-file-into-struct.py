"""Load JSON file into struct.

Read from file _data._json and write its content into object _x.
Assume the JSON data is suitable for the type of _x. 

Source: programming-idioms.org
"""

# Implementation author: nickname
# Created on 2016-02-18T16:58:02.260166Z
# Last modified on 2016-02-18T16:58:02.260166Z
# Version 1

import json

with open("data.json", "r") as input:
    x = json.load(input)
