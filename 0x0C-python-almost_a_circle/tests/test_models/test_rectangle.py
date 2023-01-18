import unittest
from models.rectangle import Rectangle

"""This module performs tests for the Rectangle class"""


class TestRectangle(unittest.TestCase):
    """A class that tests the Rectangle class"""

    def setUp(self):
        """setUp function"""
        self.r1 = Rectangle(10, 2)
        self.r2 = Base(2, 10)
        self.r3 = Base(10, 2, 0, 0, 12)
