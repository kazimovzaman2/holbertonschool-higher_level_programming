#!/usr/bin/python3
"""Square class that inherits from Rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int, optional): The x-coordinate of the square's position. Defaults to 0.
            y (int, optional): The y-coordinate of the square's position. Defaults to 0.
            id (int, optional): The unique identifier of the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """set/get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.size,
        )

    def update(self, *args, **kwargs):
        """Updates the attributes of the Square instance."""
        if args:
            list_atr = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, list_atr[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
