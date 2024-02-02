#!/usr/bin/python3

"""
A module that adds two integers
"""


def add_integer(a, b=98):
    """
    Basic 2 integer addition
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
