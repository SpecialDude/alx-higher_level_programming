#!/usr/bin/python3

"""
This module contains a single function to return
the json representation of objects

to_json_string()
"""


import json


def to_json_string(my_obj):
    """Json representation of objects

    Args:
        my_obj: A python object

    Returns:
        JSON string
    """

    return json.dumps(my_obj)
