#!/usr/bin/python3


"""Module doc"""


Rectangle = __import__('9-rectangle').Rectangle


class Square (Rectangle):
    """Square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
