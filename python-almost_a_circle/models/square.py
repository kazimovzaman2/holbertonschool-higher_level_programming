#!/usr/bin/python3
"""Square class that inherits from Rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.__x, self.__y, self.size)
