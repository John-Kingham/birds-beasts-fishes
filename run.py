"""
run.py

This module manages the user's interaction with the game using a
text-based interface in the console.
"""

import art
from enum import Enum

# import game


class MenuItem(Enum):
    """
    Constants representing menu items.
    """

    EXIT = 1
    INSTRUCTIONS = 2
    PLAY = 3


def main():
    """
    Controls the game's main loop and interactions with the user via a
    text-based interface.
    """
    game_is_running = True

    show_game_title()
    while game_is_running:
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
        int: From the MenuItem enum.
    """
    valid_input_required = True

    print("??? Are you ready to start a new game ???\n")
    while valid_input_required:
        option = input(
            "Please choose from one of these options...\n"
            "1. Read instructions\n"
            "2. Play game\n"
            "3. Exit\n\n"
            "Enter your choice: \n"
        )
        if option in ["1", "2", "3"]:
            return option
        else:
            print("\n!!! Your entry was invalid !!!\n")


if __name__ == "__main__":
    main()
