#!/usr/bin/python3

def max_integer(my_list=[]):
    """Return max integer in list"""
    if my_list == []:
        return None
    else:
        my_list.sort()
        return my_list[-1]
