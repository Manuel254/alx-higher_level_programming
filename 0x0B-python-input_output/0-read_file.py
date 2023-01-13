#!/usr/bin/python3

"""This module implements a function that reads from a file
    and outputs the text to stdout
"""


def read_file(filename=""):
    """Reads a file and prints to stdout"""
    with open(filename, encoding="UTF8") as f:
        text = f.read()
        print(text)
