#!/usr/bin/python3
"""
Write a program (function!) that takes a list and returns a new list that contains all the elements
of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""


def create_list_using_sets(list_to_pass):

    return list(set(list_to_pass))


def create_list_using_loop(list_to_pass):
    new_list = []

    for item in list_to_pass:
        if item not in new_list:
            new_list.append(item)

    return new_list


def main():
    list_one = [11, 11, 2, 4, 56, 78, 12, 11, 9, 99, 12]

    print("The orginal list is: {}".format(list_one))
    print("The new list constructed using sets is: {}".format(sorted(create_list_using_sets(list_one))))
    print("The new list constructed using a loop is: {}".format(sorted(create_list_using_loop(list_one))))


if __name__ == '__main__': main()
