"""
This module manages the user's interaction with the game using a
text-based interface in the console.
"""

import art
from enum import Enum
from src.data import database
from src.game import Game
from src.tui import content
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

    _show_game_title()
    while game_is_running:
        option = _get_main_menu_option()
        if option == MenuItem.EXIT:
            _show_exit_message()
            break
        if option == MenuItem.INSTRUCTIONS:
            _show_instructions()
        if option == MenuItem.PLAY:
            _play_game()


def _show_exit_message():
    """
    Shows the user an exit message.
    """
    print(content.exit_message())


def _play_game():
    """
    Plays a single round of Birds, Beats and Fishes until the word is guessed.
    """
    try:
        game = Game()
        game_is_running = True
        while game_is_running:
            guess = _get_guess(game)
            guess_is_correct = game.make_guess(guess)
            _show_guess_feedback_message(guess_is_correct)
            if game.is_over():
                _show_game_over_message(game)
                _save_final_score(game)
                break
    except Exception:
        print(content.database_error_message())


def _save_final_score(game):
    """Saves the games final score to the database.

    Args:
        game (Game): The game whose final score we want to save.
    """
    database.save_score(game.masked_word, game.final_score())


def _show_game_over_message(game):
    """
    Shows a game over message the to user.

    Args:
        game (Game): The game that is now over.
    """
    print(content.game_over_message(game))
    input()


def _show_guess_feedback_message(guess_is_correct):
    """Tell the user if their guess was right or wrong.

    Args:
        guess_is_correct (bool): True if guess was correct, otherwise False.
    """
    if guess_is_correct:
        print(content.guess_correct_message())
    else:
        print(content.guess_incorrect_message())
    _pause()


def _pause():
    """
    Pause the interface to give the user time to read new content.
    """
    time.sleep(1)


def _get_guess(game):
    """
    Gets a valid letter or word guess from the user.

    Args:
        game (bbf_game.Game): The current game.
    Returns:
        str: A valid guess, either a letter or an animal name.
    """
    valid_input_required = True

    while valid_input_required:
        _show_masked_word(game)
        if game.previous_guesses:
            _show_previous_guesses(game.previous_guesses)
        guess = input(content.guess_prompt()).strip().upper()
        _pause()
        if guess in game.previous_guesses:
            _show_previously_guessed_message()
        elif _is_valid_guess(guess):
            return guess
        else:
            _show_invalid_guess_message()


def _show_previously_guessed_message():
    """
    Informs the user that they have already made this guess before.
    """
    print(content.guessed_previously_message())


def _show_invalid_guess_message():
    """
    Informs the user that their guess was invalid.
    """
    print(content.guess_invalid_message())


def _show_masked_word(game):
    """Show the user the masked word (i.e. the current state of play).

    Args:
        game (bbf_game.Game): The current game.
    """
    print(content.masked_word_message())
    print(" ".join(game.masked_word))
    _pause()


def _is_valid_guess(guess):
    """
    Validates the user's guess. Valid guesses contain only alpha characters
    and spaces.

    Args:
        guess (str): The user's guess.

    Returns:
        bool: True if the guess is valid, otherwise False.
    """
    return guess.replace(" ", "").isalpha()


def _show_previous_guesses(guesses):
    """Show the user information about their previous guesses.

    Args:
        guesses (List[str]): The previous guesses
    """
    print(content.previous_guesses_message(), ", ".join(guesses))


def _show_instructions():
    """
    Shows the game's instructions to the user and provides
    navigation back to the main menu.
    """
    input(content.instructions())
    _pause()


def _show_game_title():
    """
    Display the game's title.
    """
    art.tprint(content.game_title(), space=1)
    print(content.game_subtitle())
    _pause()


def _get_main_menu_option():
    """
    Get a valid main menu option from the user.

    Returns:
        int: From the MenuItem enum.
    """
    valid_input_required = True

    print(content.main_menu_heading())
    _pause()
    one, two, three = "1", "2", "3"
    while valid_input_required:
        option = input(content.main_menu_options(one, two, three)).strip()
        _pause()
        if option == one:
            return MenuItem.PLAY
        elif option == two:
            return MenuItem.INSTRUCTIONS
        elif option == three:
            return MenuItem.EXIT
        else:
            print(content.menu_option_invalid_message())
