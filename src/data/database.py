"""
This module is responsible for managing the storage and retrieval of
persistent data.
"""

from src.data import github_api


def get_animal_names():
    """
    Gets a list of animal names.

    Raises:
        Exception: If there is a problem accessing the animal names database.

    Returns:
        List[str]: A list of animal names.
    """
    return github_api.get_animal_names()
