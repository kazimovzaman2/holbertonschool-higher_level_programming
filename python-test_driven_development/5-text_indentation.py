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

    punctuations = [".", "?", ":"]
    current_line = ""

    for char in text:
        current_line += char
        if char in punctuations:
            print(current_line.strip())
            print()  # Print an empty line
            current_line = ""

    if current_line:
        print(current_line.strip())
