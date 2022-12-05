#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Replaces an element in a copied list"""
    new_list = my_list[:]

    for index, el in enumerate(new_list):
        if index == idx:
            new_list[idx] = element
    return new_list
