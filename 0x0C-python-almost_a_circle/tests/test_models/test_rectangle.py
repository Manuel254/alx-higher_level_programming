import unittest
from models.rectangle import Rectangle

"""This module performs tests for the Rectangle class"""


class TestRectangle(unittest.TestCase):
    """A class that tests the Rectangle class"""
    def setUp(self):
        self.r1 = Rectangle(3, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(8, 7, 0, 0, 12)
        self.r4 = Rectangle(4, 6, 2, 1, 12)

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

    def test_area(self):
        self.assertEqual(self.r1.area(), 6)
        self.assertEqual(self.r3.area(), 56)
