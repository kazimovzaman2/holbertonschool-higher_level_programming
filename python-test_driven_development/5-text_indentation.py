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
        elif text[i] == " ":
            for j in range(i, len(text)):
                if text[j] != " ":
                    continue
                elif text[j] in [".", "?", ":", " "]:
                    break
                else:
                    print(text[j], end="")
                    break
        else:
            print(text[i], end="")
