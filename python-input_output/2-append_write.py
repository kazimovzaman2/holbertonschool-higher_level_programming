#!/usr/bin/python3


"""Documented Module"""


def append_write(filename="", text=""):
    """Documented function"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
