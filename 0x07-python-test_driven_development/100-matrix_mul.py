#!/usr/bin/python3

"""
Matrix Multiplication
"""


def matrix_mul(m_a, m_b):
    """Multiplies Two matrix

    Args:
        m_a: list of lists of integers
        m_b: list of lists of integers

    Returns:
        New Matrix
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    if len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    for i in range(len(m_a)):
        row_a = m_a[i]

        if not isinstance(row_a, list):
            raise TypeError("m_a must be a list of lists")

        if len(row_a != m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

        for e in row_a:
            if not isinstance(e, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for i in range(len(m_b)):
        row_b = m_b[i]

        if not isinstance(row_b, list):
            raise TypeError("m_b must be a list of lists")

        if len(row_b != m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

        for e in row_a:
            if not isinstance(e, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    multiplied = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            mul = 0
            for k in range(len(m_b)):
                mul += m_a[i][k] * m_b[k][j]
            row.append(mul)
        multiplied.append(row)
    return multiplied
