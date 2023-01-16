#!/usr/bin/python3

"""This module checks whether an object is an instance of a
specified class
"""


def is_kind_of_class(obj, a_class):
    """Returns True if object is ani instance of a_class
    or a super class else False

    Args:
        obj (object): An object
        a_class (object) : A Class
    Returns:
        True if obj is instance of a_class or super class
        else False

    """
    return isinstance(obj, a_class)
