#!/usr/bin/python3

"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number,
then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random
from helpers import user_data_validation


def main():
    random_number = random.randint(1, 9)
    user_guess = int(user_data_validation(
        input("Guess the number that the computer has generated between 1 and 9: ")))
    user_guess_not_equal_to_random_number = True
    number_of_guesses = 0

    while user_guess > 9 or user_guess < 1:
        try:
            raise ValueError("Guess is out of bounds:")
        except ValueError as err:
            print(err)
            print("please choose a value between 1 and 9")

        user_guess = int(user_data_validation(
            input("Guess the number that the computer has generated between 1 and 9: ")))

    while user_guess_not_equal_to_random_number:
        if user_guess > random_number:
            print("Your guess is too high")
            number_of_guesses += 1
            user_guess = int(user_data_validation(
                input("Guess the number that the computer has generated between 1 and 9: ")))
        elif user_guess < random_number:
            print("Your guess is too low")
            number_of_guesses += 1
            user_guess = int(user_data_validation(
                input("Guess the number that the computer has generated between 1 and 9: ")))
        else:
            number_of_guesses += 1
            print("your guess is correct! You took {} guesses".format(number_of_guesses))
            user_guess_not_equal_to_random_number = False


if __name__ == '__main__': main()
