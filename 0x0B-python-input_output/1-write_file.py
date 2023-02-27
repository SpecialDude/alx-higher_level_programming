#!/usr/bin/python3

"""
This module contains a single function to write
to a file

write_file()
"""


def write_file(filename="", text=""):
    """Writes to a file

    Args:
        filename: str - name of file with path
        text: Text content to write in

    Returns:
        None
    """

    with open(filename, mode='w', encoding='UTF-8') as fd:
        return fd.write(text)
