#!/usr/bin/python3

"""A program that checks for lowercase
   character
"""


def islower(c):
    """Checks whether a character
       is lowercase and return True
       if correct else False"""
    unicode_value = ord(c)
    if unicode_value >= 97 and unicode_value <= 122:
        return True
    return False
