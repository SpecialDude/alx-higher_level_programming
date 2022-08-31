#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple

    Args:
        my_list: List of tuples

    Returns:
        int
    """
    if not my_list:
        return 0

    return sum(map(lambda x: x[0] * x[1], my_list)) / \
        sum(map(lambda x: x[1], my_list))
