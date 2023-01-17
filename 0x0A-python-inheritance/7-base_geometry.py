#!/usr/bin/python3


"""Specifies a Base class for Geometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises:
            Exception: area() is not implemented

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is an integer and is greater than 0

        Args:
            name (str): A string
            value (any): Any type but must be an integer

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0

        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
