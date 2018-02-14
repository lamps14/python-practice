#!/usr/bin/python3

"""
Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.).
You can (and should!) use your answer to Exercise 4 to help you.
Take this opportunity to practice using functions, described below.
"""

from helpers import user_data_validation

# Globals
user_generated_value = int(user_data_validation(input('Please provide a number: ')))
calculations = []


def print_calculations():
    for l in calculations:
        print("{} / {} = {}".format(l[0], l[1], l[2]))


def is_prime_number():
    divisor = 1
    divisor_list = []

    while divisor <= user_generated_value:
        if user_generated_value % divisor == 0:
            divisor_list.append(divisor)
            result = int(user_generated_value / divisor)
            calculations.append((user_generated_value, divisor, result))
        divisor += 1

    if len(divisor_list) <= 2:
        print("{} is a prime number".format(user_generated_value))
    else:
        print("{} IS NOT a prime number".format(user_generated_value))


def main():
    is_prime_number()
    user_response = user_data_validation(input("would you like to see the calculations? (Y/N)"),
                                         "Please provide an answer: ").lower()
    if user_response == "y":
        print_calculations()


if __name__ == '__main__': main()
