#!/usr/bin/python3
def element_at(my_list, idx):
    """Finds element specified at a specific index"""
    for index, element in enumerate(my_list):
        if index == idx:
            return my_list[idx]
