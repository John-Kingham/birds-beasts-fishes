"""
This module is responsible for providing the text interface's content.
"""

from src.data import database


def exit_message():
    """
    Returns an exit message to the user.

    Returns:
        str: The game's exit message.
    """
    return (
        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        "!!! Thank you for playing BIRDS, BEASTS AND FISHES! !!!\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    )


def instructions():
    """Returns the game's instruction text.

    Returns:
        str: The game's instructions.
    """
    return (
        "\nINSTRUCTIONS:\n"
        "1. An animal name will be picked at random and shown to you.\n"
        "All letters will be blanked out, except the first and last.\n"
        "2. You'll be asked to guess a single letter or the whole word.\n"
        "3. If your guess is wrong, you'll be asked to guess again.\n"
        "4. If you guess a single letter, the letter will become visible.\n"
        "5. If you guess the whole word, you've won that round of the game.\n"
        "You'll be congratulated and shown your score for that word.\n"
        "You'll also be shown a description of the animal you just guessed.\n"
        "\nSCORE:\n"
        "Your score will be saved for each animal name.\n"
        "The score is calculated as:\n"
        "The number of letters divided by the number of guesses.\n"
        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        "!!! Press enter to return to the main menu !!!\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    )


def game_over_message(game):
    """
    Returns the game over message.

    Args:
        game (Game): The game that is now over.

    Returns:
        str: The game over message.
    """
    word = game.masked_word
    num_letters = len(word)
    num_guesses = len(game.previous_guesses)
    score = game.final_score()
    high_score = database.get_high_score_for(game.masked_word)
    high_score_message = None
    if score > high_score:
        high_score_message = "That is better than your old high score of:"
    elif score == high_score:
        high_score_message = "That equals your previous high score of:"
    else:
        high_score_message = "That is worse than your previous high score of:"
    return (
        "\nWell done! "
        f"You guessed that the word was: {" ".join(word)}\n"
        f"The number of letters in that word was: {num_letters}\n"
        f"The number of guesses you made was: {num_guesses}\n"
        f"This gives you a score for this word of: {score}\n"
        f"{high_score_message} {high_score}\n"
        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        "!!! Press ENTER to return to the main menu! !!!\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    )


def guess_correct_message():
    """Returns a message informing the user their guess was correct.

    Returns:
        str: The guess-was-correct message.
    """
    return (
        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        "!!! Your guess was CORRECT! !!!\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    )


def guess_incorrect_message():
    """
    Returns a message informing the user their guess was incorrect.

    Returns:
        str: The guess-was-incorrect message.
    """
    return (
        "\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n"
        "XXX Your guess was WRONG! XXX\n"
        "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    )


def guess_invalid_message():
    """
    Returns a message informing the user their guess was invalid.

    Returns:
        str: The guess-invalid message.
    """
    return (
        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        "!!! Your guess contained non-alphabetic characters. Try again !!!\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    )


def guessed_previously_message():
    """
    Returns a message informing the user they have made this guess before.

    Returns:
        str: The guessed-previously message.
    """
    return (
        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        "!!! Your guess matches an existing guess. Try again !!!\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    )


def masked_word_message():
    """Returns a label to be displayed before the masked word.

    Returns:
        str: A label to be placed before the masked word on screen.
    """
    return "\nYour bird, beast or fish to guess is:\n"


def previous_guesses_message():
    """Returns a message to be displayed before the list of previous guesses.

    Returns:
        str: A message to be displayed before the list of previous guesses.
    """
    return "\nYour previous guesses were:"


def game_title():
    """
    Returns the game's title.

    Returns:
        str: The game's title.
    """
    return "Birds, Beasts\nand Fishes"


def main_menu_heading():
    """Returns a heading for the main menu.

    Returns:
        str: The main menu's heading.
    """
    return (
        "?????????????????????????????????????????\n"
        "??? Are you ready to start a new game ???\n"
        "?????????????????????????????????????????\n"
    )


def menu_option_invalid_message():
    return (
        "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        "!!! Your entry was invalid !!!\n"
        "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
    )


def guess_prompt():
    """Returns a message prompting the user to enter their guess.

    Returns:
        str: A prompt asking the user to enter their guess.
    """
    return "\nGuess a letter or the animal's full name:\n"


def main_menu_options(first, second, third):
    """
    Returns the main menu's text. Labels for each menu item are passed in
    so they can be matched up with the user's input in the calling function.

    Args:
        first (str): The label for the first menu item
        second (str): The label for the second menu item
        third (str): The label for the third menu item

    Returns:
        str: The main menu text.
    """
    return (
        "Please choose from one of these options...\n"
        f"{first}. Play game\n"
        f"{second}. Read instructions\n"
        f"{third}. Exit\n\n"
        "Enter your choice: \n"
    )


def database_error_message():
    """
    Returns a message informing the user there was an error accessing the
    database.

    Returns:
        str: The database error message.
    """
    return (
        "\n*****************************************\n"
        "*** ERROR: UNABLE TO ACCESS DATABASE! ***\n"
        "*****************************************\n"
    )
