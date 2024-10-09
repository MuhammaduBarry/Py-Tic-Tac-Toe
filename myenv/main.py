# Import python module
import pyfiglet
from termcolor import colored

def intro():
    """Define Rules and Information needed to play"""

    # Create ASCII art
    intro_ascii_art = colored(pyfiglet.figlet_format('''Welcome to Tic-Tac-Toe''', font = "larry3d", width = 135, justify = "right"), color = "cyan")

    # Instructions
    intro_statement = f'''
    The rules are simple:

     1 | 2 | 3
    ---|---|---
     4 | 5 | 6 
    ---|---|---
     7 | 8 | 9  

    This is a turn based program, The first player that will start is the first player who inputs their name and symbol.

    1. After players and symbols have been selected, player 1 will choose a number between 1-9.
    2. Then player 2 will choose another number 1-9, until the players get three in a row, column, and diagonal.
    3. You will be prompted on how many games you would like to play, 1 up to infinity amount of games.
    4. Make sure you double check if the space number has been taken before inputting your number.
    5. Good luck and have fun :)
    '''

    # Introduction print statement
    print(f"\n{intro_ascii_art}")
    print(intro_statement)

# Game information
game_rounds = input("\nHow many rounds would you like to play? ")

player_one = input("\nWhat is your name Player one: ")
player_one_symbol = input("\nWhat symbol would you like to use: ")

player_two = input("\nWhat is your name Player two: ")
player_two_symbol = input("\nWhat symbol would you like to use: ")

print(f"\nPlayer one: {player_one}, {player_one_symbol}")
print(f"Player two: {player_two}, {player_two_symbol}")


def main():
    """Function to house and organize program"""
    intro()

main()