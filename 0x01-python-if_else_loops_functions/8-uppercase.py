#!/usr/bin/python3

"""A program that prints a
   string in uppercase
"""


def uppercase(str):
    """Returns a string in uppercase"""
    new_str = ''

    for character in str:
        # Checks whether character is alphabet
        if character.isalpha():
            # Converts character to unicode if alphabet
            unicode_value = ord(character)

            # Checks whether character is lowercase
            # and converts it to uppercase
            if unicode_value >= 97 and unicode_value <= 122:
                unicode_value -= 32

            # Converts unicode to character
            character = chr(unicode_value)
        new_str += character

    print("{}".format(new_str))
