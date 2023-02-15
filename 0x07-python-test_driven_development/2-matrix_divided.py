#!/usr/bin/python3

"""This module takes a matrix and divides the elements of a matrix
with a divisor then returns a new matrix.
"""


def matrix_divided(matrix, div):
    """Accepts a matrix of numbers and divides it by a number
    then returns a new matrix of the result.

    Args:
        matrix (int/float): A matrix of numbers
        div (int/ float): Divides each element of the matrix

    Returns:
        A new matrix

    Raises:
        TypeError: if matrix does not contain integers or floats
                    if matrix has rows of different sizes
                    if div is not a number
        ZeroDivisionError: if div is zero

    """
    new_matrix = []
    len_of_rows = []

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(div, int)) and (not isinstance(div, float)):
        raise TypeError("div must be a number")

    for row in matrix:
        new_row = []
        len_of_rows.append(len(row))
        for col in row:
            if (not isinstance(col, int)) and (not isinstance(col, float)):
                raise TypeError("matrix must be a matrix (list of lists) of\
                                integers/floats")
            result = round((col / div), 2)
            new_row.append(result)
        new_matrix.append(new_row)

    len_ofrows = set(len_of_rows)
    if len(len_of_rows) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    return new_matrix
