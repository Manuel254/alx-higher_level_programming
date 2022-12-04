#!/usr/bin/python3
def element_at(my_list, idx):
    """Finds element specified at a specific index"""
    if idx >= 0 and idx <= len(my_list):
        return my_list[idx]
