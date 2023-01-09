#!/usr/bin/python3

"""This module defines a template for creating rectangle objects"""


class Rectangle:
    """This is a class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes rectangle instance with a width and height

        Args:
            width (int): The breadth of a rectangle
            height (int): The height of a rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width of a rectangle to a particular value

        Args:
            value (int): The width of the rectangle

        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height of a rectangle to a particular value

        Args:
            value (int): The height of the rectangle

        Raises:
            TypeError: If height is not an integer
            ValueError: If height is less than 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
