#!/usr/bin/python3


"""Documented Module"""


import json


def save_to_json_file(my_obj, filename):
    """Documented function"""
    formated_text = json.dumps(my_obj)

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(formated_text)
