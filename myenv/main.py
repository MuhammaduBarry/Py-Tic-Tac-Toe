# Import python module
import pyfiglet
from termcolor import colored


tic_tac_toe_board = [
    ['0','1','2'],
    ['3','4','5'],
    ['6','7','8']
] 

def get_main_board():
    main_board = f'''
        {tic_tac_toe_board[0][0]} | {tic_tac_toe_board[0][1]} | {tic_tac_toe_board[0][2]}
        ---|---|---
        {tic_tac_toe_board[1][0]} | {tic_tac_toe_board[1][1]} | {tic_tac_toe_board[1][2]}
        ---|---|---
        {tic_tac_toe_board[2][0]} | {tic_tac_toe_board[2][1]} | {tic_tac_toe_board[2][2]}
        '''
    print(main_board)

def intro():
    """Define Rules and Information needed to play"""

    # Create ASCII art
    intro_ascii_art = colored(pyfiglet.figlet_format('''Welcome to Tic-Tac-Toe''', font = "larry3d", width = 135, justify = "right"), color = "cyan")

    # Instructions
    intro_statement = f'''
    The rules are simple:
    {get_main_board()}
    This is a turn based program, The first player that will start is the first player who inputs their name and symbol.

    1. After players and symbols have been selected, player 1 will choose a number between 0-8.
    2. Then player 2 will choose another number 0-8, until the players get three in a row, column, and diagonal.
    3. You will be prompted on how many games you would like to play, 1 up to infinity amount of games.
    4. Make sure you double check if the space number has been taken before inputting your number.
    5. Good luck and have fun :)
    '''

    # Introduction print statement
    print(f"\n{intro_ascii_art}")
    print(intro_statement)

def display_current_board(input, player_symbol):
    """Function to display and track player game"""

    # Placing them accordingly
    if input <= 2:
        tic_tac_toe_board[0][input] = player_symbol
    elif 2 < input <= 5:
        # Removing index error
        tic_tac_toe_board[1][input - 3] = player_symbol
    elif 5 < input <= 8:
        # Removing index error
        tic_tac_toe_board[2][input - 6] = player_symbol
    else:
        print("Index out of bound wont work")

    get_main_board()
    

def game_logic():
    """Create logic that will house the core program functionality"""

    # Game information
    game_rounds = input("\nHow many rounds would you like to play? ")

    player_one = input("\nWhat is your name Player one: ")
    player_one_symbol = input("\nWhat symbol would you like to use: ")

    player_two = input("\nWhat is your name Player two: ")
    player_two_symbol = input("\nWhat symbol would you like to use: ")
    return game_rounds, player_one, player_one_symbol, player_two, player_two_symbol

def main():
    """Function to house and organize program"""

    intro()
    game_logic()
    display_current_board(2,"looking for me")
    display_current_board(5,"looking for me")


main()