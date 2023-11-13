from data_processing.database import Card, CardDatabase
from config.config import Config

def deal_cards(database: CardDatabase, round: int, config: Config) -> CardDatabase:
    """
    Deals cards to the players for each round.

    Args:
        database (CardDatabase): The card database.
        round (int): The current round.
        config (Config): The configuration settings.

    Return:
        CardDatabase: The updated card database.
    """
    return database