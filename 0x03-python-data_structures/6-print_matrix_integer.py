#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a list of list

    Args
        matrix: list of lists of integers

    Returns:
        None
    """

    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        col_str = ""
        for j in range(col):
            col_str += "{:d}".format(matrix[i][j])
            if j != col - 1:
                col_str += " "
        print(col_str)
