#!/usr/bin/python3

def remove_char_at(str, n):
    """Removes a character at 
    a specified position
    """
    new_str = ""

    for i, c in enumerate(str):
        if i == n:
            continue
        new_str += c

    return new_str
