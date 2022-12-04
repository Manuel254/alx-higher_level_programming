#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Finds replaces element specified at a specific index"""
    for i in range(len(my_list)):
        if i == idx:
            my_list[idx] = element
    return my_list
