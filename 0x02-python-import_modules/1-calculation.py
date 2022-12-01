#!/usr/bin/python3
import calculator_1 as calc

a = 10
b = 5

if __name__ == '__main__':
    # Prints add of a and b
    print("{} + {} = {}".format(a, b, calc.add(a, b)))

    # Prints sub of a and b
    print("{} - {} = {}".format(a, b, calc.sub(a, b)))

    # Prints mul of a and b
    print("{} * {} = {}".format(a, b, calc.mul(a, b)))

    # prints div of a and b
    print("{} / {} = {}".format(a, b, calc.div(a, b)))
