#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add First Two elemets of two tuples

    Args:
        tuple_a: First Tuple
        tuple_b: Second Tuple

    Returns:
        Tuple
    """

    num1 = 0
    num2 = 0

    if len(tuple_a) > 1:
        num1 += tuple_a[0]
        num2 += tuple_a[1]

    if len(tuple_b) > 1:
        num1 += tuple_b[0]
        num2 += tuple_b[1]

    return (num1, num2)
