"""Declare enumeration.

Create an enumerated type _Suit with 4 possible values _SPADES, _HEARTS, _DIAMONDS, _CLUBS.

Source: programming-idioms.org
"""

# Implementation author: TinyFawks
# Created on 2016-02-18T16:58:03.828361Z
# Last modified on 2016-11-06T23:13:31.574716Z
# Version 2

# New in Python 3.4

from enum import Enum


class Suit(Enum):
    SPADES = 1
    HEARTS = 2
    DIAMONDS = 3
    CLUBS = 4
