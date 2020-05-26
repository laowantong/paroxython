"""Hex string to byte array.

From hex string _s of _2n digits, build the equivalent array _a of _n bytes.
Each pair of hexadecimal characters (16 possible values per digit) is decoded into one byte (256 possible values).

Source: programming-idioms.org
"""

# Implementation author: Oldboy
# Created on 2019-02-11T20:01:36.48212Z
# Last modified on 2019-03-26T21:23:37.827454Z
# Version 2

a = bytearray.fromhex(s)
