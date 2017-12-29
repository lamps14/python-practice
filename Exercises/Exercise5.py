#!/usr/bin/python3
"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).

Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""

import random


def main():
    first_list = list(range(20))

    for num in list(range(10)):
        first_list.append(num)

    second_list = list(range(40))
    common_list = []

    print("Random List 1: {}".format(first_list))
    print("Random List 2: {}".format(second_list))

    for num_a in first_list:
        if num_a in second_list:
            if num_a not in common_list:
                common_list.append(num_a)

    print("The common values: {}". format(common_list))


if __name__ == '__main__': main()
