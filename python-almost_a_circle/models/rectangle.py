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

        Raises:
            TypeError: If width, height, x, or y is not an integer.
            ValueError: If width, or height is less than or equal to 0.
            ValueError: If x, or y is less than 0.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """set/get methods for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """set/get method for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """set/get method for the x coordinate attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """set/get method for the y coordinate attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height
        )

    def area(self):
        """Returns the area of the Rectangle."""
        return self.__height * self.__width

    def display(self):
        """Display the rectangle by printing it to the console."""
        for _ in range(self.__y):
            print()

        for i in range(self.__height):
            for _ in range(self.__x):
                print(" ", end="")
            for _ in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print()
        print()

    def update(self, *args):
        """Updates the attributes of the Rectangle instance."""
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except Exception:
                pass
