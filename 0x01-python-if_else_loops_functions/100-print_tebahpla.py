#!/usr/bin/python3

for num in range(ord('Z'), ord('A') - 1, -1):
    if (num % 2 == 0):
        num += 32
    print("{}".format(chr(num)), end="")
