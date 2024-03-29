#!/usr/bin/python3

"""This module contains a function that writes
a python object to a text file using JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """Saves a python object to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
