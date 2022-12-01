#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == '__main__':
    # Prints add of a and b
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Prints sub of a and b
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Prints mul of a and b
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # prints div of a and b
    print("{} / {} = {}".format(a, b, div(a, b)))
