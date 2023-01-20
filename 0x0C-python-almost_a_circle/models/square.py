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

    def update(self, *args, **kwargs):
        """Updates attributes"""
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = kwargs[k]
                if k == "size":
                    self.size = kwargs[k]
                if k == "x":
                    self.x = kwargs[k]
                if k == "y":
                    self.y = kwargs[k]

    def to_dictionary(self):
        """Return dictionary representation of square"""
        return {
                "id": self.id,
                "x": self.x,
                "size": self.size,
                "y": self.y
                }

    def __str__(self):
        """Well-formatted square instance"""
        return "[{}] ({}) {}/{} - {}".format(
                                            self.__class__.__name__,
                                            self.id,
                                            self.x,
                                            self.y,
                                            self.width
                                            )
