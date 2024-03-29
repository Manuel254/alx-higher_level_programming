#!/usr/bin/python3

"""A script that adds arguments to a python list and
save them to a file
"""

import sys

save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load("add_item.json")
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
save(my_list, "add_item.json")
