#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    # Prints add of a and b
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))

    # Prints sub of a and b
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))

    # Prints mul of a and b
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))

    # prints div of a and b
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
