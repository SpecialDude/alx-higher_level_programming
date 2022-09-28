#!/usr/bin/python3

"""
Module contains a functiona to
do some file manipulation
"""


def append_after(filename="", search_string="", new_string=""):
    """Read file and append some lines after

    Args:
        filename: Name of file
        search_string: str
        new_string: tbr str

    Returns:
        None
    """

    lines = []

    with open(filename, mode="r") as fd:

        for line in fd:
            line = line.rstrip('\n')
            lines.append(line + '\n')
            if search_string.lower() in line.lower():
                lines.append(new_string + '\n')
    if lines:
        with open(filename, mode="w") as fd:
            fd.writelines(lines)
