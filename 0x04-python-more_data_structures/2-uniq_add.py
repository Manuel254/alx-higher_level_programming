#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Adds unique numbers in a list
    and return sum
    """
    sum_nums = 0
    for num in set(my_list):
        sum_nums += num

    return sum_nums
