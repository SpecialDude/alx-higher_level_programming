#!/usr/bin/python3

"""
This module contains a single function to read
file and print out its content

read_file()
"""


def read_file(filename=""):
    """Reads a file and print its contents

    Args:
        filename: str - name of file with path

    Returns:
        None
    """

    with open(filename, mode='r', encoding='utf-8') as fd:
        print(fd.read())
