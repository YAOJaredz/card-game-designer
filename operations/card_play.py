import os, sys
import json
sys.path.append('.')

from data_processing.database import Card, CardDatabase
from operations.config import Config
import operations.card_deck as deck

def get_identifier(play_cards:list[int]) -> list[int]:
    """Get the identifiers of cards.
    Args:
        play_cards(list[Card]): The cards to be played.
    Return:
        list[int]: The identifiers of the cards to play.
    """
    identifiers=set()
    for card in play_cards:
        identifiers.add(card.identifier)
    return identifiers
        
def find_card(database: CardDatabase, player:str, identifier: int) -> Card:
    """Find the card according to the identifier.
    Assumption: The identifier is in hand. 
    Args:
        database (CardDatabase): The card database.
        player (str): The player who is playing the cards.
        identifier (int): The identifier of the card to be found.
    Return:
        Card: The card to be found.
    """
    for card in database.hands[player]:
        if card.identifier==identifier:
            return card

def play_cards(player: str, play_cards: list[int], database: CardDatabase, round: int, config: Config) -> CardDatabase:
    """
    Plays cards from the players for each round.

    Args:
        player (str): The player who is playing the cards.
        play_cards (list[int]): The identifiers of cards that the player going to play.
        database (CardDatabase): The card database.
        round (int): The current round.
        config (Config): The configuration settings.

    Return:
        CardDatabase: The updated card database.
    """
    if len(play_cards) > config.num_cards_played_per_round:
        raise ValueError('Exceeds the number of cards to be played.')
    elif set(play_cards).issubset(get_identifier(database.hands[player])) == False:
        raise ValueError('Cards not in hand.')
    else:
        for card_id in play_cards:
            card=find_card(database, player, card_id)
            database.discard.add(card)
            database.hands[player].remove(card)
    return database