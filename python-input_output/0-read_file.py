#!/usr/bin/python3


"""Documented Module"""


def read_file(filename=""):
    """Documented function"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
