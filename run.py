"""
This module manages the user's interaction with the game using a
text-based interface in the console.
"""

import art
from enum import Enum
from bbf_game import Game


class MenuItem(Enum):
    """
    Constants representing menu items.
    """

    EXIT = 1
    INSTRUCTIONS = 2
    PLAY = 3


def main():
    """
    Starts the game and responds to main menu input.
    """
    game_is_running = True

    show_game_title()
    while game_is_running:
        option = get_main_menu_option()
        if option == MenuItem.EXIT:
            print("\n!!! Goodbye !!!\n")
            break
        if option == MenuItem.INSTRUCTIONS:
            show_instructions()
        if option == MenuItem.PLAY:
            play()


def play():
    """
    Plays a single round of the game until the word is guessed.
    """
    game = Game()
    print("\nYour bird, beast or fish to guess is:")
    print(game.masked_word)
    if game.previous_guesses:
        print("Your previous guesses were:")
        print(", ".join(game.previous_guesses))
        print("Your last guess was:")
        print(game.previous_guesses[-1])
    guess = get_guess()
    print("your guess was", guess)


def get_guess():
    """
    Gets a valid letter or word guess from the user.

    Returns:
        str: A valid letter or animal name guess.
    """
    valid_input_required = True
    while valid_input_required:
        return input("Enter a letter or animal name as your guess: ")
        # if the guess consists of letters and spaces
        # return the guess
        # else
        # print an error message and try again


def show_instructions():
    """
    Shows the game's instructions to the user and provides
    navigation back to the main menu.
    """
    input(
        "INSTRUCTIONS:\n"
        "1. An animal name will be picked at random and shown to you "
        "with all the letters blanked out.\n"
        "2. You'll be asked to guess either a single letter or the whole \n"
        "word."
        "3. If your guess is wrong, you'll be asked to guess again.\n"
        "4. If you correctly guessed a single letter, that letter will become "
        "visible in the word.\n"
        "5. If you guess the whole word (either by guessing the whole word in "
        "one go, or by correctly guessing each letter) you'll be "
        "congratulated and shown your score for that word. You'll also see a "
        "fascinating description of the animal you just guessed.\n"
        "\nSCORE:\n"
        "Your score will be saved for each animal name and is calculated as "
        "the number of letters in the word divided by the number of attempts "
        "it took you to guess the word.\n"
        "\n!!! Press enter to return to the main menu !!!\n"
    )


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
            "1. Play game\n"
            "2. Read instructions\n"
            "3. Exit\n\n"
            "Enter your choice: \n"
        ).strip()
        if option == "1":
            return MenuItem.PLAY
        elif option == "2":
            return MenuItem.INSTRUCTIONS
        elif option == "3":
            return MenuItem.EXIT
        else:
            print("\n!!! Your entry was invalid !!!\n")


if __name__ == "__main__":
    main()
