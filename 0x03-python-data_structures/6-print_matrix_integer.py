#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Prints elements in matrix"""
    if matrix == [[]]:
        print()

    for index1, row in enumerate(matrix):
        for index2, column in enumerate(row):
            if index2 != len(row) - 1:
                print("{:d}".format(column), end=" ")
            else:
                print("{:d}".format(column))
