#!/usr/bin/python3

"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input),
compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""


def main():
    from helpers import turn_checker

    gameplay = True
    while gameplay:

        player_one_turn = turn_checker(input("Player one, Rock, Paper or Scissors? ").capitalize())
        player_two_turn = turn_checker(input("Player Two, Rock, Paper or Scissors? ").capitalize())

        # Key represents the turn. Value represents what the turn can beat
        winning_matrix = {'Rock': 'Scissors', 'Scissors': 'Paper', 'Paper': 'Rock'}

        player_one_to_win = winning_matrix[player_one_turn]
        player_two_to_win = winning_matrix[player_two_turn]

        if player_one_to_win == player_two_turn:
            print("{} beats {} therefore player one wins!".format(player_one_turn, player_two_turn))
        elif player_two_to_win == player_one_turn:
            print("{} beats {} therefore player two wins!".format(player_two_turn, player_one_turn))
        else:
            print("The game ended in a tie!")


        play_another_game = input("Do you wish to play another game? ").upper()
        if play_another_game == "Y" or play_another_game == "YES":
            continue
        else:
            gameplay = False


if __name__ == '__main__': main()
