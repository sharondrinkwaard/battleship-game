
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


def game_rules():
    '''
    Displays the game rules
    '''
    rules_answer = input("Would you like to read the rules? y/n \n")
    if rules_answer == 'y':
        print('These are the rules')


def main():
    '''
    Main function where all other functions are being called from.
    This functions runs the game
    '''
    print("Welcome to the Battleships game!")
    game_rules()


    create_computer_board()
    create_player_board()


main()