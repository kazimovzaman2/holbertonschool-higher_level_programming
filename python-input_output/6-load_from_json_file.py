#!/usr/bin/python3


"""Documented Module"""


import json


def load_from_json_file(filename):
    """Documented function"""
    with open(filename, "r") as f:
        return json.load(f)
