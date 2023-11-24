import sys
from random import randint

# function to retrieve the provided input for number of games, and then validates the input
def get_number_of_games():
    args = sys.argv[1:]
    if len(args) != 1:
        print("Incorrect number arguments.")
        print("Please execute: python3 rock_paper_scissors.py <NUMBER OF GAMES>")
        exit()
    try:
        n = int(args[0])
        if n > 0:
            return n
        else:
            print("Incorrect number of games.")
            print("Please execute: python3 rock_paper_scissors.py <NUMBER OF GAMES>")
            print("Number of games must be a number greater than 0.")
            exit()
    except ValueError:
        print("Incorrect number of games.")
        print("Please execute: python3 rock_paper_scissors.py <NUMBER OF GAMES>")
        print("Number of games must be a valid integer.")
        exit()

# This function take input from the user for if they would like to play Rock, Paper or Scissors
def user_hand():
    print("Please choose a number from 0-2 to decide your hand:")
    print("0. Rock")
    print("1. Paper")
    print("2. Scissors")
    try:
        hand = int(input())
    except ValueError:
        print("Please provide a valid number from 0-2\n")
        hand = user_hand()
    if hand < 0 or hand > 2:
        print("Please provide a valid number from 0-2\n")
        hand = user_hand()
    print("")
    return hand

# returns a random hand for the computer
def game_hand():
    return randint(0, 2)

# determines who has won the current round or if it has resulted in a draw
def determine_winner(user, game):
    if user == game:
        return 1
    elif user == 0 and game == 2:
        return 0
    elif game == 0 and user == 2:
        return 2
    elif user > game:
        return 0
    else:
        return 2

# function that plays a single round
def play_round():
    # maps a number to each hand
    d = {
        0: "Rock",
        1: "Paper",
        2: "Scissors",
    }
    user = user_hand()
    print(f"You chose: {d[user]}")
    game = game_hand()
    print(f"The game chose: {d[game]}")
    winner = determine_winner(user, game)
    return winner # returns the winner of the round to update the score

# function that displays the winner of the game after N rounds
def game_winner(scores):
    [user_wins, ties, game_wins] = scores
    print("The game has ended.")
    print(f"You won {user_wins} rounds.")
    print(f"The computer won {game_wins} rounds.")
    print(f"You tied {ties} rounds.\n")
    if user_wins > game_wins:
        print("You have won the game!")
    elif user_wins < game_wins:
        print("The computer has won the game!")
    else:
        print("The game has ended a tie!")
    print("Thanks for playing.")

def main():
    N = get_number_of_games()
    games_played = 0

    # scores [user, draw, game]
    scores = [0, 0, 0] # tracks the scores
    while games_played < N:
        winner = play_round() # retrieves winner of the round
        # displays winner of current round
        match winner:
            case 0:
                print("You win the round!")
            case 1:
                print("This round ended a tie!")
            case 2:
                print("The computer won this round!")
        print("")
        scores[winner] += 1 #updates score
        games_played += 1

    game_winner(scores) # determines winner of the game


if __name__ == "__main__":
    main()