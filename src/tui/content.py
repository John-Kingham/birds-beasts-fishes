"""
This module is responsible for providing the text interface's content.
"""

from src.data import data_manager


def bordered_text(text, symbol):
    """Wraps a border around text using a repeating symbol.

    Args:
        text (str): The text to be wrapped.
        symbol (str): A single character.

    Returns:
        str: The text wrapped in a border of symbols.
    """
    border_width = 3
    padding = 1
    top = symbol * (len(text) + border_width * 2 + padding * 2)
    bottom = top
    left = (symbol * border_width) + (" " * padding)
    right = (" " * padding) + (symbol * border_width)
    return f"{top}\n{left}{text}{right}\n{bottom}"


def exit_message():
    """
    Returns an exit message to the user.

    Returns:
        str: The game's exit message.
    """
    message = "Thank you for playing BIRDS, BEASTS AND FISHES!"
    return f"\n{bordered_text(message, "!")}\n"


def instructions():
    """Returns the game's instruction text.

    Returns:
        str: The game's instructions.
    """
    return (
        "\nINSTRUCTIONS:\n"
        "- An animal name will be picked at random and shown to you.\n"
        "- All letters will be blanked out, except the first and last.\n"
        "- You'll be asked to guess a single letter or the whole word.\n"
        "- If your guess is wrong, you'll be asked to guess again.\n"
        "- If you correctly guess a single letter, it will become visible.\n"
        "- If you correctly guess the whole word, you've won that round!\n"
        "- You'll then be congratulated and shown your score for that word.\n"
        "\nSCORE:\n"
        "- Your score will be saved for each animal name.\n"
        "- The score is calculated as:\n"
        "- Number of letters divided by number of guesses, times 100.\n\n"
    ) + bordered_text("Press enter to return to the main menu", "!") + "\n"


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
    high_score = data_manager.get_high_score_for(game.masked_word)
    high_score_message = None
    if score > high_score:
        high_score_message = "That is better than the previous high score of:"
    elif score == high_score:
        high_score_message = "That equals the current high score of:"
    else:
        high_score_message = "That is worse than the current high score of:"
    return (
        "\nWell done! "
        f"You guessed that the word was: {" ".join(word)}\n"
        f"The number of letters in that word was: {num_letters}\n"
        f"The number of guesses you made was: {num_guesses}\n"
        f"This gives you a score for this word of: {score}\n"
        f"{high_score_message} {high_score}\n\n"
    ) + bordered_text("Press ENTER to return to the main menu", "!")


def guess_correct_message():
    """Returns a message informing the user their guess was correct.

    Returns:
        str: The guess-was-correct message.
    """
    return "\n" + bordered_text("Your guess was CORRECT!", "!")


def guess_incorrect_message():
    """
    Returns a message informing the user their guess was incorrect.

    Returns:
        str: The guess-was-incorrect message.
    """
    return "\n" + bordered_text("Your guess was WRONG!", "X")


def guess_invalid_message():
    """
    Returns a message informing the user their guess was invalid.

    Returns:
        str: The guess-invalid message.
    """
    return "\n" + bordered_text(
        "Your guess contained non-alphabetic characters. Try again", "!"
    )


def guessed_previously_message():
    """
    Returns a message informing the user they have made this guess before.

    Returns:
        str: The guessed-previously message.
    """
    return "\n" + bordered_text(
        "Your guess matches an existing guess. Try again", "!"
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


def game_subtitle():
    """
    Returns the game's subtitle.

    Returns:
        str: The game's subtitle.
    """
    return (
        "Welcome to Birds, Beasts and Fishes, the word game for "
        "animal lovers and puzzle lovers everywhere!\n"
    )


def main_menu_heading():
    """Returns a heading for the main menu.

    Returns:
        str: The main menu's heading.
    """
    return bordered_text("Are you ready to start a new game", "?")


def menu_option_invalid_message():
    return bordered_text("Your entry was invalid", "!")


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
        "\nPlease choose from one of these options...\n"
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
    return bordered_text("ERROR: UNABLE TO ACCESS DATABASE!", "*")
