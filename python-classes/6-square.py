#!/usr/bin/python3
"""Doc for top level"""


class Square:
    """Class doc"""

    def __init__(self, size=0, position=(0, 0)):
        """Doc for initialize"""

        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if not (
                isinstance(value, tuple)
                and len(value) == 2
                and all(i > 0 and isinstance(i, int)  for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
