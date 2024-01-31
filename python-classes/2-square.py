#!/usr/bin/python3
"""Doc for top level"""


class Square:
    """Class doc"""

    def __init__(self, size=0):
        """Doc for initialize"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
