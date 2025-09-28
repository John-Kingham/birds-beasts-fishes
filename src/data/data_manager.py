"""
This module is responsible for managing the storage and retrieval of
persistent data.
"""

from src.data import github
from src.data import google_db


def get_animal_names():
    """
    Gets a list of animal names.

    Raises:
        Exception: If there is a problem accessing the animal names database.

    Returns:
        List[str]: A list of animal names.
    """
    return github.get_animal_names()


def save_score(word, score):
    """Saves the final score for a word.

    Args:
        word (str): The word.
        score (int): The score.
    """
    google_db.save_score(word, score)


def get_high_score_for(word):
    """
    Gets the previous high score for a word.

    Args:
        word (str): The word whose high score we are interested in.

    Returns:
        int: The high score if there is one, else zero.
    """
    records = google_db.get_all_records()
    high_score = 0

    for row in records:
        if row["word"] == word and row["score"] > high_score:
            high_score = row["score"]
    return high_score
