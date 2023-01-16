#!/usr/bin/python3

"""This module contains a class that inherits from list
class and prints a list in a sorted manner
"""


class MyList(list):
    """MyList class"""
    def print_sorted(self):
        """Prints the list in a sorted manner"""
        cpy = self[:]
        cpy.sort()
        print(cpy)
