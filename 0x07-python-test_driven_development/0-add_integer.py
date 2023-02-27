#!/usr/bin/python3

"""
Add two integers, Example

>>> add_integer(10, 5)
15
"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a: integer
        b: also integer

    Returns:
        sum of a and b

    >>> add_integer(10, 5)
    15
    >>> add_integer(10, )
    108
    >>> add_integer(10, 19.45)
    29
    >>> add_integer(10, "19.45")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
