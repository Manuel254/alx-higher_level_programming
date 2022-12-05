#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Prints a list in reverse"""
    if my_list:
     count = 0
     for el in my_list:
         count += 1

     i = count - 1
     while i >= 0:
         print("{:d}".format(my_list[i]))
         i -= 1
