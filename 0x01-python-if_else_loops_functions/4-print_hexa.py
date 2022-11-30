#!/usr/bin/python3

"""Program that prints all numbers
   from 0 to 98 in decimal and in
   hexadecimal

   format:
   0 = 0x0
   ...
   98 = 0x62
"""

for decimal in range(0, 99):
    # Generates a range of numbers
    # from 0 to 98 and converts
    # them to hexadecimal
    hexadecimal = hex(decimal)
    print("{} = {}".format(decimal, hexadecimal))
