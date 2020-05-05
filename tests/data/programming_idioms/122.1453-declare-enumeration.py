"""Declare enumeration.

Create an enumerated type _Suit with 4 possible values _SPADES, _HEARTS, _DIAMONDS, _CLUBS.

Source: programming-idioms.org
"""

# Implementation author: TinyFawks
# Created on 2016-02-18T16:58:03.828361Z
# Last modified on 2016-02-18T16:58:03.828361Z
# Version 1

# Fake enum, works with any version of python.


class Suit:
    SPADES, HEARTS, DIAMONDS, CLUBS = range(4)
