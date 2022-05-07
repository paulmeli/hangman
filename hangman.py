# Author: Melissa Paul
# Creation Date: 2/5/20
# Last Modification Date: 2/8/20
# Purpose: To make a hangman game using functions.

import random # for random.choice()
import os # for clear terminal

def greet():
    '''Prints game heading at start of game'''
    greeting = "WELCOME TO HANGMAN"
    print(80 * "*"),
    print(greeting.center(80, ' ')),
    print(80 * "*")


def gallows(num_wrong):
    '''Prints gallows and body parts according to number of wrong guesses'''
    if num_wrong == 0:
        hang = '''              ___
             |   |
                 |
                 |
                 |
                 |
                 |
                 |
             ---------'''
    elif num_wrong == 1:
        hang = '''              ___
             |   |
             O   |
                 |
                 |
                 |
                 |
                 |
             ---------'''
    elif num_wrong == 2:
        hang = '''              ___
             |   |
             O   |
             |   |
             |   |
             |   |
                 |
                 |
             ---------'''
    elif num_wrong == 3:
        hang = '''              ___
             |   |
             O   |
             |   |
            /|   |
             |   |
                 |
                 |
             ---------'''
    elif num_wrong == 4:
        hang = '''              ___
             |   |
             O   |
             |   |
            /|\  |
             |   |
                 |
                 |
             ---------'''
    elif num_wrong == 5:
        hang = '''              ___
             |   |
             O   |
             |   |
            /|\  |
             |   |
            /    |
                 |
             ---------'''
    else:
        hang = '''              ___
             |   |
             O   |
             |   |
            /|\  |
             |   |
            / \  |
                 |
             ---------'''
    print(hang)


def blank_puzzle(puzzle, solving_puzzle):
    '''Prints blank puzzle'''
    for char in puzzle: # Print blank puzzle
        if char.isalpha():
            solving_puzzle.append('_')
        else:
            solving_puzzle.append(char)
    print('\n', ' '.join(solving_puzzle))

greet()

puzzle_list = ["HELLO/WORLD", "CAT/IN/THE/HAT", "IF/YOU/GIVE/A/MOUSE/A/COOKIE", "RAINBOW/FISH",
               "PERRY/THE/PLATYPUS", "TREASURE/ISLAND", "GREEN/EGGS/AND/HAM", "EL/DORADO", "BROTHER/BEAR",
               "MULAN", "THE/LION/KING", "MARY/POPPINS","THE/SOUND/OF/MUSIC", "MAGIC/TREEHOUSE", "TOY/STORY",
               "BILL/NYE/THE/SCIENCE/GUY", "FINDING/NEMO", "HOME/ALONE","REMEMBER/THE/TITANS", "ORANGE/MARMALADE",
               "A/SERIES/OF/UNFORTUNATE/EVENTS","THE/HUNGER/GAMES", "TANGERINE", "FLAPJACK",
               "TO/INFINITY/AND/BEYOND", "TOM/AND/JERRY", "PINK/PANTHER", "SCOOBY/DOO", "INSIDE/OUT",
               "THE/INCREDIBLES"]

computer_win = 0
player_win = 0

while True:
    num_wrong = 0
    gallows(num_wrong)    # Prints gallows based on number of wrong guesses
    
    # Reset lists
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z']
    wrong_guess = []
    solving_puzzle = []

    puzzle = random.choice(puzzle_list) # Returns random element from puzzle_list
    # print(puzzle)
    blank_puzzle(puzzle, solving_puzzle)

    while num_wrong < 6 and '_' in solving_puzzle: # Game
        while True: # Keep taking using guess until letter
            guess = input("\nWhat letter do you guess?: ")
            if guess.isalpha():
                break
        guess = guess.upper()

        if guess in alphabet: # If unique guess...
            os.system('cls') # Clear terminal
            if guess in puzzle: # If correct guess...
                gallows(num_wrong)
                for index in range(len(puzzle)):
                    if puzzle[index] == guess:
                        solving_puzzle[index] = guess
                print('\n', ' '.join(solving_puzzle))
            else: # If incorrect guess...
                num_wrong += 1
                gallows(num_wrong)
                wrong_guess.append(guess)
                wrong_guess.sort()
                print(guess, "is incorrect"),
                print("Incorrect guesses so far are:", ', '.join(wrong_guess))
                print("Puzzle so far is", ' '.join(solving_puzzle))

            alphabet.remove(guess)

    if num_wrong == 6: # If player loses...
        print("\nAnswer was:", puzzle)
        computer_win += 1
        print("Sorry, computer wins"),
        print("Computer has won", computer_win, "game(s) to your", player_win)
    else: # If player wins...
        player_win += 1
        print("\nCongratulations, you win!"),
        print("You have won", player_win, "game(s) to computer's", computer_win)

    while True: # Keep asking for response until 'Y' or 'N'
        response = input("Would you like to play again (Y/N)?: ")
        if response.upper() == 'Y' or response.upper() == 'N':
            break
    if response.upper() == 'N':
        break

