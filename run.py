'''
Battleship game Portfolio Project 3
'''

# Imports randint so a random integer can be used
from random import randint

# Index 0 are the 'row headings'
board = [
    ['+', '1', '2', '3', '4', '5'],
    ['1', '.', '.', '.', '.', '.'],
    ['2', '.', '.', '.', '.', '.'],
    ['3', '.', '.', '.', '.', '.'],
    ['4', '.', '.', '.', '.', '.'],
    ['5', '.', '.', '.', '.', '.'],
]
board_with_moves = [
    ['+', '1', '2', '3', '4', '5'],
    ['1', '.', '.', '.', '.', '.'],
    ['2', '.', '.', '.', '.', '.'],
    ['3', '.', '.', '.', '.', '.'],
    ['4', '.', '.', '.', '.', '.'],
    ['5', '.', '.', '.', '.', '.'],
]


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
        print('-----------------------------------')
        print('On the battleship board there are 4 hidden ships.')
        print('You have 10 bullets to find all of them.')
        print('When you find all 4 ships, you win.')
        print('If you run out of bullets, you lose.\n')
        print('Use number 1 2 3 4 or 5.\n')
        print('M = missed shot\n$ = Ship that sunk')
        print('-----------------------------------')
    elif rules_answer != 'n':
        print('Input is invalid, try again')
        game_rules()


def display_battleship_game(board):
    '''
    Prints the battleship game board
    On this board the ships will be placed
    The player will not see this board as the ships location is secret
    '''
    for row in board:
        print(" ".join(row))
    print('-----------------------------------')


def display_board_with_moves(board_with_moves):
    '''
    Prints the game board without the ships
    The input coordinates are being placed on this board
    And are shown to the player
    '''
    for row in board_with_moves:
        print(" ".join(row))
    print('-----------------------------------')


def place_random_ships(board):
    '''
    This function will place the ships.
    I'm using a for loop with range 4 because I want to place 4 ships
    '''
    # Starting from 1 instead of 0
    # beacuse I don't want to place a ship on the headings
    for ships in range(4):
        ships_row = randint(1, 5)
        ships_column = randint(1, 5)
        board[ships_row][ships_column] = 'X'
        print(ships_row, ships_column)


def turns_and_moves(board, board_with_moves):
    '''
    Mananges the input of the player with several if statements
    And a for loop
    '''
    # turn = 'player'
    points_player = int(0)

    for bullets in range(11):
        print('-----------------------------------')
        move_row = int(input('Choose your row number: 1 - 5\n'))
        move_column = int(input('Choose your column number: 1 - 5\n'))
        print('-----------------------------------')

        if board[move_row][move_column] == 'X':
            print('Hit! You sunk a battleship!')
            board[move_row][move_column] = '$'
            board_with_moves[move_row][move_column] = '$'
            points_player += 1
            print(f'Sunken ships: {points_player}')
            display_board_with_moves(board_with_moves)
        else:
            print('You missed... \nTry again')
            print(f'Sunken ships: {points_player}')
            board[move_row][move_column] = 'M'
            board_with_moves[move_row][move_column] = 'M'
            display_board_with_moves(board_with_moves)

        if points_player == 4:
            print('-----------------------------------')
            print('You sunk all the battleships and won this game!')
            print('Congratulations')  # add {username_input}
            break
        if bullets == 10:
            print('-----------------------------------')
            print('No more bullets left\nGame over!')
            display_battleship_game(board)
            break


def game():
    '''
    Runs the game
    '''


def restart_game():
    '''
    Restarts the game if input is 'y'
    '''
    print('-----------------------------------')
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
    print('\nWelcome to the Battleships game!')
    print('-----------------------------------')
    # game_rules()
    # create_player()
    # display_battleship_game(board)
    display_board_with_moves(board_with_moves)
    place_random_ships(board)
    turns_and_moves(board, board_with_moves)
    # restart_game()


main()
