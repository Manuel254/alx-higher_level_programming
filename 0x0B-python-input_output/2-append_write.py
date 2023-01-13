#!/usr/bin/python3

"""This module implements a function that appends a string
    to the end of the  text file and returns
    the number of characters written
"""


def append_write(filename="", text=""):
    """Appends to a file

    Args:
        filename (str): Name of file to append string
        text (str): String to be appended to file

    Returns:
        Number of characters appended to file

    """
    with open(filename, "a", encoding="utf-8") as f:
        char_count = f.write(text)
        return char_count
