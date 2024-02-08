#!/usr/bin/python3


"""Documented Module"""


def write_file(filename="", text=""):
    """Documented function"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
