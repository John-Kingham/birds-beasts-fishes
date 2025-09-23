"""
This module is responsible for storing and retrieving high scores using
Google Sheets.
"""

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SCORES = GSPREAD_CLIENT.open("birds_beasts_fishes").worksheet("scores")


def save_score(word, score):
    """Saves the final score for a word.

    Args:
        word (str): The word.
        score (int): The score.
    """
    SCORES.append_row([word, score])
