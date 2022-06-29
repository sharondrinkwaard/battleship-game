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


def create_computer_board():
    '''
    Prints the battleship board of the computer
    '''
    print('This is the computer board')


def create_player():
    '''
    Creates a username
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
    '''
    rules_answer = input('Would you like to read the rules? y/n \n')
    if rules_answer == 'y':
        print('These are the rules')
        print('-----------------------------------')
    elif rules_answer != 'n':
        print('Input is invalid, try again')
        game_rules()


def main():
    '''
    Main function where all other functions are being called from.
    This functions runs the game
    '''
    print('Welcome to the Battleships game!')
    print('-----------------------------------')
    game_rules()
    create_player()
    create_computer_board()
    create_player_board()


main()
