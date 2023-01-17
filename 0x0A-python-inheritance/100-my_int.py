#!/usr/bin/python3

"""Module implements a modifiction of the int class"""


class MyInt(int):
    """MyInt class"""
    def __init__(self, value):
        """__init__ method"""
        self.__value = value

    def __eq__(self, value):
        return value != self

    def _ne__(self, value):
        return value == self

    def __int__(self):
        return int(self.__value)
