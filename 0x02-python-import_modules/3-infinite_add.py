#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    length = len(sys.argv)
    arg_sum = 0

    for i in range(1, length):
        # Add the current argument with sum
        arg_sum += int(sys.argv[i])

    print("{}".format(arg_sum))
