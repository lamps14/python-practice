#!/usr/bin/python3
"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
 first and last elements of the given list. For practice, write this code inside a function.
"""
import random


def main():

    old_list = random.sample(range(1, 30), 12)
    print(old_list)
    print(create_new_list_from(old_list))


def create_new_list_from(list_to_parse):
    new_list = [list_to_parse[0], list_to_parse[-1]]

    return new_list


if __name__ == '__main__': main()
