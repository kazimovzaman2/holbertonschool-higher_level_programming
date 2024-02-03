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
            print()
        elif text[i] == " ":
            continue
        else:
            while i < len(text) and text[i] not in [".", "?", ":", " "]:
                print(text[i], end="")
                i += 1
            i -= 1
