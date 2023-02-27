"""
This module contains a function That says your name
"""


def say_my_name(first_name, last_name=""):
    """Prints first_name and last_name

    Args:
        first_name: str
        last_name: str

    Returns:
        None

    >>> say_my_name("Warith", "Adeoti")
    My name is Warith Adeoti
    >>> say_my_name("Warith") #doctest: +REPORT_NDIFF +NORMALIZE_WHITESPACE
    My name is Warith
    >>> say_my_name("Warith", 4)
    Traceback (most recent call last):
        ...
    TypeError: last_name must be a string
    >>> say_my_name(3)
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string
    >>> say_my_name("Jon", "Snow")
    My name is Jon Snow
    >>> say_my_name("Elon", "Musk")
    My name is Elon Musk
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
