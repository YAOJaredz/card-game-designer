import os, sys
import json
sys.path.append('.')

from data_processing.database import Card, CardDatabase
from operations.config import Config

def get_identifier(play_cards:list[Card]) -> set[int]:
    """Get the identifiers of cards.
    Args:
        play_cards(list[Card]): The cards to be played.
    Return:
        set[int]: The identifiers of the cards to play.
    """
    identifiers=set()
    for card in play_cards:
        identifiers.add(card.identifier)
    return identifiers

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
    elif player not in database.players:
        raise ValueError('Player not in the game.')
    else:
        for card_id in play_cards:
            card=database.find_card(card_id)
            database.discard.add(card)
            database.hands[player].remove(card)
    return database

if __name__ == "__main__":
    from card_deck import initialization
    from card_deck import card_print_all

    test_config_path = 'save/test_config.json'
    config = Config(**json.load(open(test_config_path, 'r')))

    database = initialization(config)
    database.players = ['A']
    
    #Give a 3 cards
    database.hands['A']=[]
    database.hands['A'].append(database.deck.pop())
    database.hands['A'].append(database.deck.pop())
    database.hands['A'].append(database.deck.pop())
    print("A has cards:")
    card_print_all(database.hands["A"])
    print("Updated deck: ")
    card_print_all(database.deck)
    print("------ Card Play: A plays card 1 ------")
    play_cards("A", [160], database, 1, config)
    print("After play, A has cards:")
    card_print_all(database.hands["A"])
    print("Deck:")
    card_print_all(database.deck)
    print("Discard should have 1 card:")
    card_print_all(database.discard)