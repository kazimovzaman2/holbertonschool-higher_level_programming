#!/usr/bin/python3


"""Module doc"""


class BaseGeometry:
    """Base class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greated than 0".format(name))
