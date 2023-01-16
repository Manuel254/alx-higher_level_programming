#!/usr/bin/python3

"""This module checks whether an object is an instance of a
specified class
"""


def is_same_class(obj, a_class):
    """Returns True if object is an instance of a_class
    else False

    Args:
        obj (object): An object
        a_class (object) : A Class
    Returns:
        True if obj is instance of a_class
        else False

    """
    if type(obj) == a_class:
        return True
    return False
