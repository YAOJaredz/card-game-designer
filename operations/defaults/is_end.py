"""
This is a template user customized script that adds additional requirement to end the game by modifying end_game.
The function will take the Database object that contains all the information of the game.
The function should return True if the game should end, False otherwise.

If you want to use non-default scripts, please include the path to your file under "is_end_path" in the configuration file.
"""

from data_processing.database import Card, CardDatabase
from operations.config import Config

def end_game(database: CardDatabase) -> bool:
    """
    User customized scirpts to add additional conditions to end the game.

    Args:
        database (CardDatabase): The database object.
    
    Returns:
        bool: True if the game should end, False otherwise.
    """
    return False
    