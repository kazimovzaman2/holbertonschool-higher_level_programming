#!/usr/bin/python3


"""Module doc"""


def inherits_from(obj, a_class):
    """
    Same
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:  # noqa E721
        return True
    return False
