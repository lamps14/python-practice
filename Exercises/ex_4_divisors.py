#!/usr/bin/python3
"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

from helpers import user_data_validation

# Globals
user_generated_value = int(user_data_validation(input('Please provide a number: ')))
calculations = []


def print_calculations():
    for l in calculations:
        print("{} / {} = {}".format(l[0], l[1], l[2]))


def print_divisors():
    divisor = 1
    divisor_list = []

    while divisor <= user_generated_value:
        if user_generated_value % divisor == 0:
            divisor_list.append(divisor)
            result = int(user_generated_value / divisor)
            calculations.append((user_generated_value, divisor, result))
        divisor += 1

    for num in divisor_list:
        print(num, end=' ')

    print('\n')


def main():
    print('divisors of the number {} are:'.format(user_generated_value))
    print_divisors()
    user_response = user_data_validation(input("would you like to see the calculations? (Y/N)"), "Please provide an answer: ").lower()
    if user_response == "y":
        print_calculations()


if __name__ == '__main__': main()
