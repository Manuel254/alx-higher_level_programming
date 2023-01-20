#!/usr/bin/python3

"""This is a module that defines a Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new square.

        Args:
            size (int): The width and height of square
            x (int): The x coordinate of square
            y (int): The y coordinate of square
            id (int): identity of a square

        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter method for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """Well-formatted square instance"""
        return "[{}] ({}) {}/{} - {}".format(
                                            self.__class__.__name__,
                                            self.id,
                                            self.x,
                                            self.y,
                                            self.width
                                            )
