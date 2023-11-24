import os, sys
import json
sys.path.append('.')

from data_processing.database import Card, CardDatabase
from operations.config import Config

def deal_cards(database: CardDatabase, round: int, config: Config) -> CardDatabase:
    """
    Deals cards to the players for each round. 
    If it is the first round, then the players will be dealt the initial hand.
    Otherwise, the players will be dealt the cards that are specified in the configuration.

    Args:
        database (CardDatabase): The card database.
        round (int): The current round.
        config (Config): The configuration settings.

    Return:
        CardDatabase: The updated card database.
    """
    if round == 0:
        for player in database.players:
            database.hands[player] = database.pop_from_deck(config.num_initial_hand)
    else:
        for player in database.players:
            database.hands[player].extend(database.pop_from_deck(config.num_cards_dealt_per_round))

    return database

def draw_card(database: CardDatabase, player: str, config: Config, round: int) -> CardDatabase:
    """
    Draw a card from the deck.

    Args:
        database (CardDatabase): The card database.
        player (str): The player who draws the card.
        config (Config): The configuration settings.
        round (int): The current round.
    Return:
        CardDatabase: The updated card database.
    """
    if config.draw_flag:
        return database
    
    database.hands[player].extend(database.pop_from_deck(config.num_draw))
    return database