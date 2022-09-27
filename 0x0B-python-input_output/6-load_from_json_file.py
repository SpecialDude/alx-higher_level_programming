#!/usr/bin/python3

"""
This module contains a single function to load
a json file

load_from_json_file()
"""


import json


def load_from_json_file(filename):
    """loads a json file

    Args:
        filename: str

    Returns:
        Python object
    """

    with open(filename, mode='r') as fd:
        return json.load(fd)
