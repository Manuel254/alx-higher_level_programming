#!/usr/bin/python3

"""This module checks whether an object is an instance of a
class that inherited from the specified class
"""


def inherits_from(obj, a_class):
    """Returns True if object is an instance of a class
    that inherited from a specified class else False

    Args:
        obj (object): An object
        a_class (object) : A Class
    Returns:
        True if obj is instance of a class that inherited from a_class
        else False
    """
    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
