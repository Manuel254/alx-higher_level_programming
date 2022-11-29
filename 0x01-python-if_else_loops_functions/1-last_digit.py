#!/usr/bin/python3
"""
This program prints the last digit of a number
"""
import random

number = random.randint(-10000, 10000)

# Generates the last digit of a number
if number < 0:
    last_digit = abs(number) % 10
    last_digit = -last_digit
else:
    last_digit = number % 10

print(f"Last digit of {number} is {last_digit} ", end="")

if last_digit > 5:
    print(f"and is greater than 5")
elif last_digit == 0:
    print(f"and is 0")
elif last_digit < 6 and not 0:
    print(f"and is less than 6 and not 0")
