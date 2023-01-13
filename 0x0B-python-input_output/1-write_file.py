#!/usr/bin/python3

"""This module implements a function that writes a string
    to a text file and returns the number of characters written
"""


def write_file(filename="", text=""):
    """Writes to a file

    Args:
        filename (str): Name of file to be written to
        text (str): String to be written to file

    Returns:
        Number of characters written to file

    """
    with open(filename, "w", encoding="utf-8") as f:
        char_count = f.write(text)
        return char_count
