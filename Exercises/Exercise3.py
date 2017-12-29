#!/usr/bin/python3
"""
Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
Instead of printing the elements one by one, make a new list that has all the elements
less than 5 from this list in it and print out this new list.
Write this in one line of Python.

Ask the user for a number and return a list that contains only elements from the original
list a that are smaller than that number given by the user.
"""
from helpers import error_checker

number_list = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def main():
    create_new_list()
    create_user_generated_list()


def create_new_list():
    new_number_list = []

    for number in number_list:
        if number < 5:
            print('index: {} value: {}'.format(number_list.index(number), number))
            new_number_list.append(number)

    print("original list: {}".format(number_list))
    print("new list with values less than 5: {}".format(new_number_list))


def create_user_generated_list():
    user_generated_list = []
    user_input_value = int(error_checker(input("Please provide a value: ")))

    for number in number_list:
        if number < user_input_value:
            user_generated_list.append(number)

    print("original list: {}".format(number_list))
    print("user generated list: {}".format(user_generated_list))


if __name__ == "__main__": main()
