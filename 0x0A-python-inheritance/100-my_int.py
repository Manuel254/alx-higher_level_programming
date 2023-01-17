#!/usr/bin/python3

"""Module implements a modifiction of the int class"""


class MyInt(int):
    """MyInt class"""

    def __eq__(self, value):
        return int(self) != value

    def __ne__(self, value):
        return int(self) == value
