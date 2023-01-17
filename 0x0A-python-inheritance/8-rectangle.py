#!/usr/bin/python3

"""This module defines a class Rectangle that inherits
from BaseGeometry
"""


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
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
