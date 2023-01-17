#!/usr/bin/python3

"""This module defines a class Rectangle that inherits"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a rectangle class"""

    def __init__(self, width, height):
        """Instantiates a rectangle object

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        self.__width = width
        self.__height = height
        Rectangle.integer_validator(self, "width", width)
        Rectangle.integer_validator(self, "height", height)

    def area(self):
        """Area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Print rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
