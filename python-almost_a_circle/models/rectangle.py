#!/usr/bin/python3
"""Rectangle class that inherits from Base class."""
from models.base import Base


class Rectangle(Base):
    """Represents the Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of the Rectangle class.

        Args:
            width (int): The width of the Rectangle.
            height (int): The height of the Rectangle.
            x (int): The x coordinate of the Rectangle.
            y (int): The y coordinate of the Rectangle.
            id (int): The identity of the new Rectangle.
        """
        super().__init__(id=id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """set/get methods for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """set/get method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """set/get method for the x coordinate attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """set/get method for the y coordinate attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
