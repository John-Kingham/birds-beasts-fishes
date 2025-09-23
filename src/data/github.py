"""
This module is responsible for retrieving animal names from GitHub.
"""

import requests


def _get_animal_names():
    """
    Gets a list of animal names.

    Raises:
        Exception: If there is a problem accessing the animal names database.

    Returns:
        List[str]: A list of animal names.
    """
    url = (
        "https://gist.githubusercontent.com/borlaym/585e2e09dd6abd9b0d0a/"
        "raw/6e46db8f5c27cb18fd1dfa50c7c921a0fbacbad0/animals.json"
    )
    response = requests.get(url, timeout=1)
    response.raise_for_status()
    return response.json()
