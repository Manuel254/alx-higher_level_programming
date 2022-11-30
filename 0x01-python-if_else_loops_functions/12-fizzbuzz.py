#!/usr/bin/python3

""" Program that prints numbers 1 to 100
    and the 'fizzbuzz string
"""


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(number), end=" ")
