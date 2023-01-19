import unittest
from models.rectangle import Rectangle

"""This module performs tests for the Rectangle class"""


class TestRectangle(unittest.TestCase):
    """A class that tests the Rectangle class"""

    def test_width(self):
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
            Rectangle({}, 10)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
            Rectangle(0, 2)

    def test_height(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
            Rectangle(10, -10)

    def test_x(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "5", 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 5)

    def test_y(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 5, "4")
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -5)
