#!/usr/bin/python3

"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

def main():
    test_string = input("Please enter a string: ")

    reversed_string = test_string[::-1]

    if reversed_string == test_string:
        print("{} is a palindrome".format(test_string))
    else:
        print("{} is NOT a palindrome".format(test_string))


if __name__ == '__main__': main()
