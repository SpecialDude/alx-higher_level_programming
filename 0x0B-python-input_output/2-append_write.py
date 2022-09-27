#!/usr/bin/python3

"""
This module contains a single function to append
to a file

append_write()
"""


def append_write(filename="", text=""):
    """Appends to a file

    Args:
        filename: str - name of file with path
        text: Text content to write in

    Returns:
        None
    """

    with open(filename, mode='a', encoding='UTF-8') as fd:
        return fd.write(text)
