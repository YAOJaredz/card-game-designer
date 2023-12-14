"""
This is a exmple customized script paried with poker game.
Game will end when any player has no cards in hand.
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
    for hand in database.hands.values():
        if len(hand) == 0:
            return True
    return False
    