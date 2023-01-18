#!/usr/bin/python3

"""This module defines a Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiation"""
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter method for width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Setter method for width"""
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        self.__width = width

    @property
    def height(self):
        """Getter method for height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Setter method for height"""
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        self.__height = height

    @property
    def x(self):
        """Getter method for x"""
        return self.__x

    @x.setter
    def x(self, x):
        """Setter method for x"""
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        self.__x = x

    @property
    def y(self):
        """Getter method for y"""
        return self.__y

    @y.setter
    def y(self, y):
        """Setter method for y"""
        if y < 0:
            raise ValueError("y must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        self.__y = y
