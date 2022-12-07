#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a sorted dictionary by keys"""
    new_dict = {}

    keys = sorted(a_dictionary.keys())
    new_dict = {k: a_dictionary[k] for k in keys}

    for k, v in new_dict.items():
        print("{}: {}".format(k, v))
