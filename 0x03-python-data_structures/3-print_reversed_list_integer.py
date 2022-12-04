#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints a list in reverse"""
    new_list = [my_list.pop() for i in range(len(my_list))]

    for element in new_list:
        print("{:d}".format(element))

