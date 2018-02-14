#!/usr/bin/python3

"""
Take two lists and write a program that returns a list that contains only the elements that are common between the lists
(without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python
using at least one list comprehension.

Extra:

Randomly generate two lists to test this
"""

import random


def main():
    list_one = random.sample(range(1, 30), 12)
    list_two = random.sample(range(1, 30), 16)
    new_list = [num_a for num_a in set(list_one) if num_a in list_two]
    print(new_list)


if __name__ == '__main__': main()
