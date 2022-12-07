#!/usr/bin/python3

"""
Divides all elements of a matrix by a number

>>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number

    Args:
        matrix: list of lists of numbers
        div: number

    Returns:
        new matrix

    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided([[1, 2, 3], [4, 5, ]], 3)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size
    >>> matrix_divided([[1, 2, 3], [4, 5, '6']], 3)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[1, 2, 3], [4, 5, 7]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    >>> matrix_divided(4, '4')
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>>
    >>> matrix_divided([[120, 20, 33], [74, 25, 70]], 8)
    [[15.0, 2.5, 4.12], [9.25, 3.12, 8.75]]
    """

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        if not isinstance(row, (list, )):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) "
                    "of integers/floats"
                )

            new_row.append(round(i / div, 2))

        new_matrix.append(new_row)

    return new_matrix
