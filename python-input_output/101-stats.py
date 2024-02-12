#!/usr/bin/python3


"""Documented Module"""


def append_after(filename="", search_string="", new_string=""):
    """Doc for function"""
    text = ""
    with open(filename, "r", encoding="utf-8") as rf:
        for line in rf:
            text += line
            if search_string in line:
                text += new_string

    with open(filename, "w", encoding="utf-8") as wf:
        wf.write(text)
