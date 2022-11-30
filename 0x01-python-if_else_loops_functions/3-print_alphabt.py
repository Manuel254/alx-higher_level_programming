#!/usr/bin/python3

"""Program that prints ASCII
   alphabet in lowercase
"""

for unicode_value in range(ord('a'), ord('z') + 1):
    # Generates range of alphabet characters
    # and prints them except q and e
    alphabet = chr(unicode_value)

    if alphabet == 'q' or alphabet == 'e':
        continue

    print("{}".format(alphabet), end="")
