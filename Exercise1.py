#!/usr/bin/python3
import datetime


def main():
    name = input("What is your name?")

    while name == '':
        try:
            raise NameError("You must specify a name to continue:")
        except NameError as err:
            print(err)
            name = input()

    age = input("Hello {}. What is your age?".format(name))

    while age == '':
        try:
            raise ValueError("you must provide an age to proceed:")
        except ValueError as err:
            print(err)
            age = (input())

    age = int(age)
    birth_year = datetime.datetime.now().year - age
    hundredth_birthday = birth_year + 100

    i = input("Can you provide a value between 1 - 10?")

    while i == '':
        try:
            raise ValueError("You must provide a valid integer to proceed:")
        except ValueError as err:
            print(err)
            i = input()
    while int(i) > 10:
        try:
            raise ValueError("I need a number between 1 and 10. Can you provide a value within that range?")
        except ValueError as err:
            print(err)
            i = input()
            while i == '':
                try:
                    raise ValueError("You must provide a valid integer to proceed:")
                except ValueError as err:
                    print(err)
                    i = input()
    i = int(i)

    while i > 0:
        if age < 100:
            print("The year {} will turn 100 is {}".format(name, hundredth_birthday))
        else:
            length_of_time = datetime.datetime.now().year - hundredth_birthday
            print("{} turned 100 {} years ago, in {}".format(name, length_of_time, hundredth_birthday))
        i -= 1


if __name__ == "__main__": main()