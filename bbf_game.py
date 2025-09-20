"""
This module is responsible for applying the rules of the Birds, Beasts and
Fishes game, and maintaining the state of each game.
"""


class Game:
    """
    Represents one round of the Bird, Beasts and FIshes game. To play the game,
    follow this sequence:
    1. Create a new Game object.
    2. Call previous_guesses() to see previous guesses.
    3. Call guess() to make a new guess.
    4. Call over() to see if the game is over.
    5. Repeat 2 & 4 until the game is over.
    6. Call score() to get the game's final score.
    """

    def __init__(self):
        """
        Creates a new single-round game. Each game is initialised with an
        animal name and is ready for the player to make their first guess.
        """
        self.__word_to_guess = "Hippopotamus".upper()
        self.masked_word = self.initialise_masked_word()
        self.previous_guesses = []

    def initialise_masked_word(self):
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

    def guess(self, guess):
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
            self.previous_guesses.append(guess)
            if len(guess) == 1:
                return self.update_masked_word_for_letter(guess)
            else:
                return self.update_masked_word_for_word(guess)

    def update_masked_word_for_letter(self, guess):
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
                self.masked_word[i] = guess
        return guess_is_correct

    def update_masked_word_for_word(self, guess):
        """
        Updated the masked word based on a guess of the whole word.

        Args:
            guess (str): A guess of the whole word.

        Returns:
            bool: True if the guess was correct, otherwise False.
        """
        guess_is_correct = False

        if guess == self.__word_to_guess:
            self.masked_word = self.__word_to_guess
            guess_is_correct = True
        return guess_is_correct
