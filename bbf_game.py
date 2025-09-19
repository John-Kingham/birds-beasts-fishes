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
            letters are visible; all other letters are masked (as None).
        """
        first = self.__word_to_guess[0]
        last = self.__word_to_guess[-1]
        middle = self.__word_to_guess[1:-1]
        masked_char = None
        masked = [" " if char == " " else masked_char for char in middle]
        return [first] + masked + [last]
