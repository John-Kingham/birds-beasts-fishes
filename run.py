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
            show_exit_message()
            break
        if option == MenuItem.INSTRUCTIONS:
            show_instructions()
        if option == MenuItem.PLAY:
            play_game()


def show_exit_message():
    """
    Displays an exit message to the user.
    """
    print("\n!!! Goodbye !!!\n")


def play_game():
    """
    Plays a single round of Birds, Beats and Fishes until the word is guessed.
    """
    game = Game()
    game_is_running = True
    # while the user hasn't yet guessed the whole word
    while game_is_running:
        guess = get_guess(game)
        game.guess(guess)
        # if the whole word has been guessed
        # exit the loop and congratulate the user
        # if the user typed exit
        # exit the loop back to the main menu


def formatted_masked_word(game):
    """Format the masked word.

    Args:
        game (bbf_game.Game): The current game.
    Returns:
        string: The formatted masked word.
    """
    return "".join([char if char else "_" for char in game.masked_word])


def get_guess(game):
    """
    Gets a valid letter or word guess from the user.

    Args:
        game (bbf_game.Game): The current game.
    Returns:
        str: A valid guess, either a letter or an animal name.
    """
    valid_input_required = True

    show_masked_word(game)
    while valid_input_required:
        if game.previous_guesses:
            show_previous_guesses(game.previous_guesses)
        guess = input("\nGuess a letter or the animal's full name:\n")
        if is_valid_guess(guess):
            return guess
        else:
            show_invalid_guess_message()


def show_invalid_guess_message():
    print("\n!!! Your guess contained non-alphabetic characters! "
          "Please try again !!!")


def show_masked_word(game):
    """Show the user the masked word (i.e. the current state of play).

    Args:
        game (bbf_game.Game): The current game.
    """
    masked_word = formatted_masked_word(game)
    print("\nYour bird, beast or fish to guess is:", masked_word)


def is_valid_guess(guess):
    """
    Validates the user's guess. Valid guesses contain only alpha characters
    and spaces.

    Args:
        guess (str): The user's guess.

    Returns:
        bool: True if the guess is valid, otherwise False.
    """
    return guess.replace(" ", "").isalpha()


def show_previous_guesses(guesses):
    """Show the user information about their previous guesses.

    Args:
        guesses (List[str]): The previous guesses
    """
    print("\nYour previous guesses were:", ", ".join(guesses))
    print("\nYour last guess was:", guesses[-1])


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
