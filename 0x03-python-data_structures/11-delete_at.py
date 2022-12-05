#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes an item at a specific position"""
    i = 0
    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        while i < len(my_list):
            if i == idx:
                del my_list[idx:idx+1]
            i += 1
        return my_list
