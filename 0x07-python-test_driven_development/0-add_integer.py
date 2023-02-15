#!/usr/bin/python3

"""Addition of two integers"""


def add_integer(a, b=98):
    """Adds two integers and returns the result.
    Args:
        a (int): First integer
        b (int): Second integer

    Returns:
        int: The addition of two integers

    Raises:
        TypeError: if a or be is not integer

    """
    if (not isinstance(a, int)) and (not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int)) and (not isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
