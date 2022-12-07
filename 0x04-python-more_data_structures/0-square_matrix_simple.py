#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Square element of a matrix

    Args:
        matrix: list of lists of integers

    Return:
        New Squared matrix
    """

    return [list(map(lambda x: x ** 2, row)) for row in matrix]
