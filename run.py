'''
Battleship game Portfolio Project 3
'''


def create_player_board():
    '''
    Prints the battleship board for the user
    On the user board is shown where his battleships are
    On the computer's board these are hidden for the user
    '''
    print('This is the player board')


# Creates an empty list which will be used later to create a board
board = []


def create_computer_board(board):
    '''
    Prints the battleship board of the computer
    Adds a space between the dots
    '''
    for x in range(5):
        board.append(['.'] * 5)
    
    for row in board:
        print(" ".join(row))


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
        print('Hi ' + username_input + ', Let\'s start the game')
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
    create_computer_board(board)
    create_player_board()
    restart_game()


main()
