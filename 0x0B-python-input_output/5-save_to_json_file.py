#!/usr/bin/python3

"""
This module contains a single function to save
an object's json representation to file

save_to_json_file()
"""


import json


def save_to_json_file(my_obj, filename):
    """Object representation of json strin

    Args:
        my_obj: A python object
        filename: str

    Returns:
        None
    """

    with open(filename, mode='w', encoding="UTF-8") as fd:
        json.dump(my_obj, fd)
