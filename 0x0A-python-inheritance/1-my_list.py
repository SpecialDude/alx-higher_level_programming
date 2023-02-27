#!/usr/bin/python3

"""
This module defines MyList class extending
the builtin list class
"""


class MyList(list):
    """
    Extending a list class to
    print list elements sorted
    """

    def print_sorted(self):
        """
        print list element sorted

        Args:
            None

        Returns:
            None
        """

        print('{}'.format(sorted(self)))
