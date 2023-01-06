#!/usr/bin/python3

"""This module defines a class by a private instance attribute
and it must be an integer which greater than or equal to 0"""


class Square:
    """This class creates a square of a defined size"""

    def __init__(self, size=0):
        """Initializes a square instance

        Args:
            size (int): Size of the square (Dimensions)

        """
        self.size = size

    @property
    def size(self):
        """This is a getter function that returns the size of a square"""
        return self.__size

    @size.setter
    def size(self, size):
        """This is a setter function that modifies size of square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
