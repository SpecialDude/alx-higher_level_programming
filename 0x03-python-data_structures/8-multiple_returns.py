#!/usr/bin/python3
def multiple_returns(sentence):
    """Returs the length of a string and its first c

    Args:
        sentence: string

    Returns:
        Tuple
    """
    length = len(sentence)
    first = None if length == 0 else sentence[0]

    return length, first
