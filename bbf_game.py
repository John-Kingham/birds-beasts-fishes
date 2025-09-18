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
        print("GAME RUNNING!")
