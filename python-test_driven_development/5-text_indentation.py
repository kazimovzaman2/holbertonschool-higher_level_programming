#!/usr/bin/python3

"""
I love text indentation
"""


def text_indentation(text):
    """
    Print a text indentation
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] in [".", "?", ":"]:
            print(text[i], end="")
            print("\n")
        else:
            print(text[i], end="")
