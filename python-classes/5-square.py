#!/usr/bin/python3
"""Doc for top level"""


class Square:
    """Class doc"""

    def __init__(self, size=0):
        """Doc for initialize"""

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for i in range(self.size):
                    if i == self.size - 1:
                        print("#")
                    else:
                        print("#", end="")
