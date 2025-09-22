"""
This module is automatically run by Heroku, the deployment platform.
"""

from src.interface import start_main_menu


def main():
    """
    This function is called automatically by Heroku. It starts the game.
    """
    start_main_menu()


if __name__ == "__main__":
    main()
