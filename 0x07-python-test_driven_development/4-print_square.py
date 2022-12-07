"""
This module contains a single function
print_square which prints a square with #

>>> print_square(4)
####
####
####
####
"""

def print_square(size):
    """Prints a square of size size

    Args:
        size: an int

    Returns:
        None

    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(2.4)
    Traceback (most recent call last):
        ...
    TypeError: size must be an integer
    >>> print_square(0)
    <BLANKLINE>
    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    >>> print_square(-30)
    Traceback (most recent call last):
        ...
    ValueError: size must be >= 0
    >>>
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    row = "#" * size
    square = (row + "\n") * size
    square = square.rstrip("\n")

    print(square)
