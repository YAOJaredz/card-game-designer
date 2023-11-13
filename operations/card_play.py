import os, sys
import json
sys.path.append('.')

from data_processing.database import Card, CardDatabase
from operations.config import Config

def play_cards(player: str, played_cards: list[Card], database: CardDatabase, round: int, config: Config) -> CardDatabase:
    """
    Plays cards from the players for each round.

    Args:
        player (str): The player who is playing the cards.
        played_cards (list[Card]): The cards that the player going to play.
        database (CardDatabase): The card database.
        round (int): The current round.
        config (Config): The configuration settings.

    Return:
        CardDatabase: The updated card database.
    """
    return database