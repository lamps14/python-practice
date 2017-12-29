#!/usr/bin/python3
def error_checker(user_data, message='You must specify a number to continue:'):

    while user_data == '':
        try:
            raise ValueError(message)
        except ValueError as err:
            print(err)
            user_data = input()

    return user_data
