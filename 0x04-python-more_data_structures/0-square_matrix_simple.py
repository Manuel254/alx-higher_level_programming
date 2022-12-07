#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Returns a 2d matrix with each value squared"""
    outer_matrix = []
    inner_matrix = []

    for row in matrix:
        for column in row:
            inner_matrix.append(column ** 2)
        outer_matrix.append(inner_matrix)
        inner_matrix = []

    return outer_matrix
