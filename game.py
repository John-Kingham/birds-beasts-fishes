# Write your code to expect a terminal of 80 characters wide and 24 rows high
import art


def run():
    """
    Start the game and run the main game loop.
    """
    # show game title
    show_game_title()
    # while game is running:
    # show main menu
    # get a valid main menu option from user
    # if user option is exit:
    # show exit message and exit game
    # if user option is instructions:
    # show instructions
    # if user option is play game:
    # play game


def show_game_title():
    """
    Display the game's title.
    """
    art.tprint("Birds, Beasts", space=1)
    art.tprint("and Fishes!", space=1)
