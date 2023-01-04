#!/usr/bin/python3

"""This module defines a class by a private instance attribute
and it must be an integer which greater thanor equal to 0"""


class Square:
    """This class creates a square of a defined size"""
    def __init__(self, size=0):
        """Initializes a square instance

        Args:
            size (int): Size of the square (Dimensions)

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
