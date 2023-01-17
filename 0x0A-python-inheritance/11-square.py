#!/usr/bin/python3

"""This module defines a square class"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Instantiates a square class.

        Args:
            size (int): size of square

        """
        self.__size = size
        Square.integer_validator(self, "size", size)

    def area(self):
        """Area of square"""
        return self.__size ** 2

    def __str__(self):
        """Prints Square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
