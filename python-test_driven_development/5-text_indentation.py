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
    result = ""
    new_line = False

    for c in clean_text:
        result += c
        if c in ".?:":
            result += "\n\n"
            new_line = True
        elif c != " " and new_line:
            result += "\n"
            new_line = False

    print(result)
