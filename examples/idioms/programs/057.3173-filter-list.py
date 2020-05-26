"""Filter list.

Create list _y containing items from list _x satisfying predicate _p. Respect original ordering. Don't modify _x in-place.

Source: programming-idioms.org
"""

# Implementation author: sgdpk
# Created on 2019-09-27T03:28:06.687958Z
# Last modified on 2019-09-27T03:28:06.687958Z
# Version 1

# List comprehensions tend to be more readable than filter function

y = [element for element in x if p(element)]
