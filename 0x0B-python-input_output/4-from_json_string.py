#!/usr/bin/python3

"""
This module contains a single function to return
the object representation of json strings

from_json_string()
"""


import json


def from_json_string(my_str):
    """Object representation of json strin

    Args:
        my_str: A python object

    Returns:
        A python object
    """

    return json.loads(my_str)
