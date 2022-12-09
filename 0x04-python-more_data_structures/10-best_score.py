#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return

    keys = a_dictionary.keys()
    values = a_dictionary.values()

    max_score = max(zip(keys, values))

    return max_score[0]
