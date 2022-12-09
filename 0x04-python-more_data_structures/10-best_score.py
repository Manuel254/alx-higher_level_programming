#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return

    keys = sorted(list(a_dictionary.keys()))
    values = sorted(list(a_dictionary.values()))

    position = values.index(values[-1])

    return keys[position]
