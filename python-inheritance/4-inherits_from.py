#!/usr/bin/python3


"""Module doc"""


def inherits_from(obj, a_class):
    """
    Same
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    return False
