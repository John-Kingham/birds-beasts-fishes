"""
This module is responsible for managing the storage and retrieval of
persistent data.
"""

from src.data import github_api
from src.data import google_api


def get_animal_names():
    """
    Gets a list of animal names.

    Raises:
        Exception: If there is a problem accessing the animal names database.

    Returns:
        List[str]: A list of animal names.
    """
    return github_api.get_animal_names()


def save_score(word, score):
    """Saves the final score for a word.

    Args:
        word (str): The word.
        score (int): The score.
    """
    google_api.save_score(word, score)
