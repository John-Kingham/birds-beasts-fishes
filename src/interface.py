"""
This module manages the user's interaction with the game using a
text-based interface in the console.
"""

# TODO: PUT A SPACE BETWEEN EACH CHARACTER IN THE MASKED WORD BECAUSE
# UNDERLINES LOOK LIKE ONE LONG LINE IN HEROKU

import art
from src import content
from enum import Enum
from src.game import Game
import time


class MenuItem(Enum):
    """
    Constants representing menu items.
    """

    EXIT = 1
    INSTRUCTIONS = 2
    PLAY = 3


def start_main_menu():
    """
    Starts the game by launching and managing the main menu.
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
    Shows the user an exit message.
    """
    print(content.exit_message())


def play_game():
    """
    Plays a single round of Birds, Beats and Fishes until the word is guessed.
    """
    try:
        game = Game()
        game_is_running = True
        while game_is_running:
            guess = get_guess(game)
            guess_is_correct = game.make_guess(guess)
            show_guess_feedback_message(guess_is_correct)
            if game.is_over():
                show_game_over_message(game.masked_word)
                break
    except Exception:
        print(content.animal_names_error_message())


def show_game_over_message(guessed_word):
    """
    Shows a game over message the to user.

    Args:
        guessed_word (str): The word correctly guessed by the user.
    """
    print(content.game_over_message(guessed_word))
    input()


def show_guess_feedback_message(guess_is_correct):
    """Tell the user if their guess was right or wrong.

    Args:
        guess_is_correct (bool): True if guess was correct, otherwise False.
    """
    if guess_is_correct:
        print(content.guess_correct_message())
    else:
        print(content.guess_incorrect_message())
    pause()


def pause():
    """
    Pause the interface to give the user time to read new content.
    """
    time.sleep(1)


def get_guess(game):
    """
    Gets a valid letter or word guess from the user.

    Args:
        game (bbf_game.Game): The current game.
    Returns:
        str: A valid guess, either a letter or an animal name.
    """
    valid_input_required = True

    while valid_input_required:
        show_masked_word(game)
        if game.previous_guesses:
            show_previous_guesses(game.previous_guesses)
        guess = input(content.guess_prompt()).strip().upper()
        pause()
        if guess in game.previous_guesses:
            show_previously_guessed_message()
        elif is_valid_guess(guess):
            return guess
        else:
            show_invalid_guess_message()


def show_previously_guessed_message():
    """
    Informs the user that they have already made this guess before.
    """
    print(content.guessed_previously_message())


def show_invalid_guess_message():
    """
    Informs the user that their guess was invalid.
    """
    print(content.guess_invalid_message())


def show_masked_word(game):
    """Show the user the masked word (i.e. the current state of play).

    Args:
        game (bbf_game.Game): The current game.
    """
    print(content.masked_word_message())
    print(game.masked_word)
    pause()


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
    print(content.previous_guesses_message(), ", ".join(guesses))


def show_instructions():
    """
    Shows the game's instructions to the user and provides
    navigation back to the main menu.
    """
    input(content.instructions())
    pause()


def show_game_title():
    """
    Display the game's title.
    """
    art.tprint(content.game_title(), space=1)
    pause()


def get_main_menu_option():
    """
    Get a valid main menu option from the user.

    Returns:
        int: From the MenuItem enum.
    """
    valid_input_required = True

    print(content.main_menu_heading())
    pause()
    one, two, three = "1", "2", "3"
    while valid_input_required:
        option = input(content.main_menu_options(one, two, three)).strip()
        pause()
        if option == one:
            return MenuItem.PLAY
        elif option == two:
            return MenuItem.INSTRUCTIONS
        elif option == three:
            return MenuItem.EXIT
        else:
            print(content.menu_option_invalid_message())
