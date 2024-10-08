import os, sys
import json

sys.path.append(".")

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
    if database.players == []:
        raise ValueError("No players in the database.")

    if round == 0:
        for player in database.players:
            database.hands[player] = database.pop_from_deck(config.num_initial_hand)
    else:
        for player in database.players:
            database.hands[player].extend(
                database.pop_from_deck(config.num_cards_dealt_per_round)
            )

    return database


def draw_card(database: CardDatabase, player: str, config: Config) -> CardDatabase:
    """
    Draw a card from the deck.

    Args:
        database (CardDatabase): The card database.
        player (str): The player who draws the card.
        config (Config): The configuration settings.

    Return:
        CardDatabase: The updated card database.
    """
    if not config.draw_flag:
        return database

    database.hands[player].extend(database.pop_from_deck(config.num_draw))
    return database


if __name__ == "__main__":
    from card_deck import initialization  # type: ignore

    test_config_path = "save/test_config.json"
    config = Config(**json.load(open(test_config_path, "r")))

    # Test with test_config.json
    database = initialization(config)
    database.players = ["a", "b", "c", "d"]
    database.self_check()
    s1 = database.snapshots

    # Deal card for round 0
    # Visually check the cards dealt to each player
    database = deal_cards(database, 0, config)
    print(database.hands)

    # Deal card for round 1
    database = deal_cards(database, 1, config)
    print(database.hands)

    # Draw card for player a
    database = draw_card(database, "a", config)
    print(database.hands)

    print(database.self_check())  # Check the integrity of the database
