'''
Battleship game Portfolio Project 3
'''

# Imports randint so a random integer can be used for the computer's turn
from random import randint

# ndex 0 are the 'row headings'
board = [
    ['A', '.', '.', '.', '.', '.'],
    ['B', '.', '.', '.', '.', '.'],
    ['C', '.', '.', '.', '.', '.'],
    ['D', '.', '.', '.', '.', '.'],
    ['E', '.', '.', '.', '.', '.'],
]
# Variables to control the game
# player_ships = [()]
# turn = 'player'
# round = 0  # of 10
# points_pc = 0  # increments by 1 each correct hit
# points_player = 0  # increments by 1 each correct hit


def create_player():
    '''
    Creates a username
    This is required
    '''
    username_input = input('Create your username: \n')
    if username_input == '':
        print('You need to fill in a name. Try again')
        create_player()
    else:
        print('\nHi ' + username_input + ', Let\'s start the game')
        print('-----------------------------------')


def game_rules():
    '''
    Displays the game rules if input answer is 'y'
    Continues without displaying the rules if answer is 'n'
    If answered otherwise, the user is asked to give valid input
    '''
    rules_answer = input('Would you like to read the rules? y/n \n')
    if rules_answer == 'y':
        print('These are the rules')
        print('-----------------------------------')
    elif rules_answer != 'n':
        print('Input is invalid, try again')
        game_rules()


def display_battleship_game(board):
    '''
    Prints the battleship game board
    Adds a space between the dots
    '''
    print('+ 1 2 3 4 5')
    for row in board:
        print(" ".join(row))
    print('-----------------------------------')


def place_random_ships(board):
    '''
    This function will place the ships.
    I'm using a for loop with range 4 because I want to place 4 ships
    '''
    # Starting from 1 instead of 0
    # beacuse I don't want to include the headings 'A' or 'B' etc
    # while using indexing to place ships
    for ships in range(4):
        ships_row = randint(1, 4)
        ships_column = randint(1, 4)
        board[ships_row][ships_column] = 'X'


def game():
    '''
    Runs the game board
    '''


def restart_game():
    '''
    Restarts the game if input is 'y'
    '''
    restart = input('Do you want to play again? y/n \n')
    if restart == 'y':
        main()
    elif restart != 'n':
        print('Invalid input, try again')
        restart_game()
    else:
        print('Good bye! See you next time.')


def main():
    '''
    Main function where all other functions are being called from.
    This functions runs the game
    '''
    print('Welcome to the Battleships game!')
    print('-----------------------------------')
    # game_rules()
    # create_player()
    display_battleship_game(board)
    place_random_ships(board)
    display_battleship_game(board)
    # restart_game()


main()
