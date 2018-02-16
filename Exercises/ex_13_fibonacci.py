#!/usr/bin/python3

"""
Write a program that asks the user how many Fibonacci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of
 numbers in the sequence to generate.(Hint: The Fibonacci sequence is a sequence of numbers where the next number in
 the sequence is the sum of the previous two numbers in the sequence.
 The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def generate_fibonacci_sequence(user_input):
    iterator = 1
    if user_input == 0:
        fibonacci_sequence = []
    elif user_input == 1:
        fibonacci_sequence = [1]
    elif user_input == 2:
        fibonacci_sequence = [1, 1]
    elif user_input > 2:
        fibonacci_sequence = [1, 1]
        while iterator < (user_input - 1):
            fibonacci_sequence.append(fibonacci_sequence[iterator] + fibonacci_sequence[iterator-1])
            iterator += 1

    print(fibonacci_sequence)


def main():
    user_input = int(input('How many numbers would you like to generate in the Fibonacci sequence?'))

    generate_fibonacci_sequence(user_input)


if __name__ == '__main__': main()
