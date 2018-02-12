#!/usr/bin/python3
"""
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Hint: how does an even / odd number react differently when divided by 2?

Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""
from helpers import user_data_validation


def main():
    user_input = (input('Please provide a number:'))
    user_input = user_data_validation(user_input)
    user_input = int(user_input)

    if (user_input % 4) == 0:
        print('This is divisible by 4')
    elif (user_input % 2) == 0:
        print('This is an even number')
    else:
        print('This is an odd number')

    num = int(user_data_validation(input('Provide another number:')))
    check = int(user_data_validation(input('Provide another number to do a calculation: ')))

    remainder = num % check

    if remainder == 0:
        print('{} successfully divides into {}'.format(check, num))
    else:
        print('There is {} remaining when dividing {} by {}'.format(remainder, check, num))


if __name__ == '__main__': main()
