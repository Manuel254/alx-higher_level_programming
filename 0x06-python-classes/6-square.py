#!/usr/bin/python3

"""This module defines a class by a private instance attribute
and it must be an integer which greater than or equal to 0"""


class Square:
    """This class creates a square of a defined size"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square instance

        Args:
            size (int): Size of the square (Dimensions)
            position (int): Tuple of two positive integers (Coordinates)

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns position of the square"""
        return self.__position

    @position.setter
    def position(self, position):
        """Sets position of a square"""
        if len(position) < 2 and not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with '#' character"""
        if self.__size == 0:
            print()
        else:
            x, y = self.__position
            for row in range(self.__size):
                for column in range(self.__size):
                    print("#", end="")
                print()
