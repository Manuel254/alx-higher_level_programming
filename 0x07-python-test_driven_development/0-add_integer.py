#!/usr/bin/python3

"""Addition of two integers"""

def add_integer(a, b=98):
    """Adds two integers and returns the result.
    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: The addition of two integers

    """
    if type(a) is (float):
        a = int(a)
    if type(b) is (float):
        b = int(b)
    if type(a) is not (int):
        raise TypeError("a must be an integer")
    if type(b) is not (int):
        raise TypeError("b must be an integer")

    return a + b