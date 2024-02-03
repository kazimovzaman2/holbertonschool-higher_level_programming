#!/usr/bin/python3

"""
I love to print square
"""


def print_square(size):
    """
    Print a square
    """

    if not isinstance(size, int) or (isinstance(size, float) & size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end="")

        print()
