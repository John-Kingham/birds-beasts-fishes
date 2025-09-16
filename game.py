# Write your code to expect a terminal of 80 characters wide and 24 rows high
import art
from enum import Enum


class MenuItem(Enum):
    """
    Constants representing menu items
    """

    EXIT = 1
    INSTRUCTIONS = 2
    PLAY = 3


def run():
    """
    Start the game and run the main game loop.
    """
    # show game title
    show_game_title()
    # while game is running:
    while True:
        # show main menu
        get_main_menu_option()
        # get a valid main menu option from user
        # if user option is exit:
        # show exit message and exit game
        # if user option is instructions:
        # show instructions
        # if user option is play game:
        # play game
        break  # for testing


def show_game_title():
    """
    Display the game's title.
    """
    art.tprint("Birds, Beasts", space=1)
    art.tprint("and Fishes!", space=1)


def get_main_menu_option():
    """
    Get a valid main menu option from the user.

    Returns:
        int: From the MenuItem enumeration.
    """
    # while the user hasn't made a valid selection:
    # display the main menu
    print("MAIN MENU: Select an option...")
    # get the user's input
    # if the user's input is valid:
    # return the valid value
    # else:
    # show an informative error message
