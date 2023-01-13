#!/usr/bin/python3

"""This module contains a function that deserializes
a python string
"""
import json


def from_json_string(my_str):
    """Returns a python object"""
    return json.loads(my_str)
