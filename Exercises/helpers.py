#!/usr/bin/python3
def user_data_validation(user_data, message='You must specify a number to continue:'):

    while user_data == '':
        try:
            raise ValueError(message)
        except ValueError as err:
            print(err)
            user_data = input()

    if user_data == "exit":
        quit()

    return user_data



def turn_checker (user_data, message='You must specify a valid turn, Please enter either Rock, Paper or Scissors:'):
    while user_data not in ['Rock', 'Paper' 'Scissors']:
        try:
            raise NameError(message)
        except NameError as err:
            print(err)
            user_data = input()
