#!/usr/bin/python3

"""
This module defines MyList class extending
the builtin list class

>>> li = MyList([3, 0, 8])
>>> li
[3, 0, 8]
>>> li.print_sorted()
[0, 3, 8]
>>> li
[3, 0, 8]
"""


class MyList(list):
    """
    Extending a list class to
    print list elements sorted

    >>> myl = MyList([1, 4, 2, 3, 5])
    >>> myl
    [1, 4, 2, 3, 5]
    >>> myl.print_sorted()
    [1, 2, 3, 4, 5]
    >>> myl
    [1, 4, 2, 3, 5]
    """

    def print_sorted(self):
        """
        print list element sorted

        Args:
            None

        Returns:
            None

        >>> li = [3, 7, 5]
        >>> myli = MyList(li)
        >>> myli
        [3, 7, 5]
        >>> myli.print_sorted()
        [3, 5, 7]
        >>> myli
        [3, 7, 5]
        """

        print(sorted(self))
