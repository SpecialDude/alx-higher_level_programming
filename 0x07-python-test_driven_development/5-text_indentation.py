#!/usr/bin/python3

"""
I don't even understand what this task is about
>>> text_indentation("Lorem ipsum dolor sit amet, contur adipisc elit.")
Lorem ipsum dolor sit amet, contur adipisc elit.
>>> text_indentation("Quonam modo?")
Quonam modo?
"""


def text_indentation(text):
    """Text Indentation: add new lines after some characters

    Args:
        text: str

    Returns:
        None

    >>> text_indentation("Lorem ipsum dolor sit amet, contur adipiscing elit.")
    Lorem ipsum dolor sit amet, contur adipiscing elit.
    >>> text_indentation("Quonam modo?")
    Quonam modo?
    >>> text_indentation(4)
    Traceback (most recent call last):
        ...
    TypeError: text must be a string
    >>> text_indentation(["consectetur adipiscing elit."])
    Traceback (most recent call last):
        ...
    TypeError: text must be a string
    >>> text_indentation("quam dico. Utinam quidem dicerent")
    quam dico.
    <BLANKLINE>
    Utinam quidem dicerent
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for d in ".?:":
        text = text.split(d)
        text = [line.strip() for line in text]
        text = (d + "\n\n").join(text)

    print(text)
