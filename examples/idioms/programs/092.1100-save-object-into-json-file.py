"""Save object into JSON file.

Write content of object _x into file _data._json. 

Source: programming-idioms.org
"""

# Implementation author: nickname
# Created on 2016-02-18T16:58:02.298929Z
# Last modified on 2016-02-18T16:58:02.298929Z
# Version 1

import json

with open("data.json", "w") as output:
    json.dump(x, output)
