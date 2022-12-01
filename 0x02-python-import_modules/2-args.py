#!/usr/bin/python3

if __name__ == '__main__':
    import sys

    # Finds length of argv excluding file name
    length = len(sys.argv) - 1

    if length == 0:
        # Handles zero arguments
        print("{} arguments.".format(length))
    elif length == 1:
        # Handles one argument
        print("{} argument:".format(length))
    else:
        # Handles more than one argument
        print("{} arguments:".format(length))

    for index in range(1, length + 1):
        # Prints the arguments with their respective indexes
        print("{}: {}".format(index, sys.argv[index]))
