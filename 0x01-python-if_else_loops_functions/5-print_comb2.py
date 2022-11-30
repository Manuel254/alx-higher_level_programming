#!/usr/bin/python3

"""A program that prints numbers
   from 0 to 99 in two digits
   separated by ', '
"""

for number in range(0, 100):
    # Generates number from 0 to 99
    # and puts 0 to 10 into 2 digits
    # then adds a comma and space
    if number != 99:
        print("{:02d}".format(number), end=", ")
    else:
        print("{}".format(number))
