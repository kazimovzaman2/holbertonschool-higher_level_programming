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

    clean_text = text.strip()
    new_line = False

    for c in clean_text:
        print(c, end="")
        if c in ".?:":
            print("\n\n", end="")
            new_line = True
        elif c != " " and new_line:
            print("\n", end="")
            new_line = False

    print()
