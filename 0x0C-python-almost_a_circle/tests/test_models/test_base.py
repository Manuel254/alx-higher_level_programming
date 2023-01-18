import unittest
from models.base import Base

"""This module performs tests for the Base class"""


class TestBase(unittest.TestCase):
    """A class that tests the Base class"""

    def setUp(self):
        """setUp function"""
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()
