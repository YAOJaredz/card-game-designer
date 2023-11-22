import os, sys
import json
sys.path.append('.')

from data_processing.database import Card, CardDatabase
from operations.config import Config
import operations.card_deck as deck

def get_identifier(card_list:[Card]) -> set[int]:
    """Get identifiers of cards.
    Help to check if cards the user wants to play are valid.
    Args:
        card_list ([Card]): The list of cards in hands.
    Return:
        identifiers (set[int]): The set of identifiers of cards in hands.
    """
    identifiers=set()
    for card in card_list:
        identifiers.add(card.identifier)
    return identifiers
    

def play_cards(player: str, play_cards: list[int], database: CardDatabase, round: int, config: Config) -> CardDatabase:
    """
    Plays cards from the players for each round.

    Args:
        player (str): The player who is playing the cards.
        play_cards (list[int]): The unique identifiers of cards that the player going to play.
        database (CardDatabase): The card database.
        round (int): The current round.
        config (Config): The configuration settings.

    Return:
        CardDatabase: The updated card database.
    """
    #Check if cards they inputted are valid
    cards_in_hand=get_identifier(database.hands[player])
    #Check if the user is allowed to play all cards they listed
    num_cards=len(play_cards)
    if set(play_cards).issubset(cards_in_hand) == False: 
        raise ValueError('Invalid cards.')
    elif num_cards > config.num_cards_played_per_round:
        raise ValueError('Exceed the number of cards allowed to play.')
    else:
        #Remove cards from hand; Add cards to discard
        for card in database.hands[player]:
            database.hands[player].remove(card)
            database.discard.add(card)
    return database