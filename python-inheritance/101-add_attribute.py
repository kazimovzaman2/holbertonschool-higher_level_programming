#!/usr/bin/python3


"""Module doc"""


def add_attribute(obj, attr, value):
    """Documented function"""
    if "__dict__" not in dir(obj):
        raise TypeError("can't add new attribute")
    obj.__dict__[attr] = value
