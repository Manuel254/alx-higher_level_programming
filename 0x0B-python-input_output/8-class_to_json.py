#!/usr/bin/python3

"""This module returns the dictionary description
of an object
"""


def class_to_json(obj):
    return obj.__dict__
