"""
This module is responsible for applying the rules of the Birds, Beasts and
Fishes game, and maintaining the state of each game.
"""

from src import database
import random


class Game:
    """
    Represents one round of the Bird, Beasts and Fishes game. To play the game,
    follow this sequence:
    1. Create a new Game object.
    2. Use .masked_word to see which letters have been correctly guessed.
    3. Use .previous_guesses to see previous guesses.
    4. Use .make_guess() to make a new guess.
    5. Use. is_over() to see if the game is over.
    6. Repeat 2 to 5 until the game is over.
    7. Use .score() to get the game's final score.
    """

    def __init__(self):
        """
        Creates a new single-round game. Each game is initialised with an
        animal name and is ready for the player to make their first guess.

        Raises:
            Exception: If there is a problem accessing the animal names data.
        """
        self.__word_to_guess = random.choice(
            database.get_animal_names()
        ).upper()
        self.__masked_word = self.__initialise_masked_word()
        self.__previous_guesses = []

    @property
    def masked_word(self):
        """
        Returns the masked word as a string. Masked letters are shown as "_".

        Returns:
            str: The masked word.
        """
        return "".join(self.__masked_word)

    @property
    def previous_guesses(self):
        """
        Returns a list of the player's previous guesses.

        Returns:
            List[str]: Previous guesses.
        """
        return self.__previous_guesses.copy()

    def is_over(self):
        """
        Returns whether the game is over. The game is over when all letters
        have been unmasked.

        Returns:
            bool: True if all letters have been unmasked, otherwise False.
        """
        return self.masked_word == self.__word_to_guess

    def __initialise_masked_word(self):
        """
        Initialises the masked word according to the game's rules.

        Returns:
            List: The masked word as a list of characters. The first and last
            letters are visible; all other letters are masked (as "_").
        """
        first = self.__word_to_guess[0]
        last = self.__word_to_guess[-1]
        middle = self.__word_to_guess[1:-1]
        masked_char = "_"
        masked = [" " if char == " " else masked_char for char in middle]
        return [first] + masked + [last]

    def make_guess(self, guess):
        """
        Update the game's state based on the player's guess.

        Args:
            guess (str): The player's guess (either a single letter
            or a whole word).

        Returns:
            bool: True if guess was correct, otherwise False.
        """
        guess = guess.strip().upper()
        guess_is_correct = False
        if len(guess) == 0:
            return guess_is_correct
        else:
            self.__previous_guesses.append(guess)
            if len(guess) == 1:
                return self.__update_masked_word_for_letter(guess)
            else:
                return self.__update_masked_word_for_word(guess)

    def __update_masked_word_for_letter(self, guess):
        """
        Updated the masked word based on a single letter guess.

        Args:
            guess (str): A single letter guess.

        Returns:
            bool: True if the guess was correct, otherwise False.
        """
        guess_is_correct = False

        for i in range(len(self.__word_to_guess)):
            if self.__word_to_guess[i] == guess:
                guess_is_correct = True
                self.__masked_word[i] = guess
        return guess_is_correct

    def __update_masked_word_for_word(self, guess):
        """
        Updated the masked word based on a guess of the whole word.

        Args:
            guess (str): A guess of the whole word.

        Returns:
            bool: True if the guess was correct, otherwise False.
        """
        guess_is_correct = False

        if guess == self.__word_to_guess:
            self.__masked_word = list(self.__word_to_guess)
            guess_is_correct = True
        return guess_is_correct
