import os, sys
import json

sys.path.append(".")

from data_processing.database import Card, CardDatabase
from operations.config import Config


def get_identifier(play_cards: list[Card]) -> set[int]:
    """
    Get the identifiers of cards.

    Args:
        play_cards(list[Card]): The cards to be played.

    Return:
        set[int]: The identifiers of the cards to play.
    """
    identifiers = set()
    for card in play_cards:
        identifiers.add(card.identifier)
    return identifiers


def play_cards(player: str, play_cards: list[int], database: CardDatabase) -> CardDatabase:
    """
    Plays cards from the players for each round.

    Args:
        player (str): The player who is playing the cards.
        play_cards (list[int]): The identifiers of cards that the player going to play.
        database (CardDatabase): The card database.

    Return:
        CardDatabase: The updated card database.
    """
    # handle the case when the player does not play any card
    if play_cards == []:
        return database
    elif set(play_cards).issubset(get_identifier(database.hands[player])) == False:
        raise ValueError("Cards not in hand.")
    else:
        database.card_recently_played["player"] = player
        database.card_recently_played["played_cards"] = []
        for card_id in play_cards:
            card = database.find_card(card_id)
            database.discard.add(card)
            for hand_card in database.hands[player]:
                if hand_card.identifier == card_id:
                    database.hands[player].remove(hand_card)
                    break
            database.card_recently_played["played_cards"].append(card)
    return database


if __name__ == "__main__":
    from card_deck import initialization  # type: ignore
    from card_deck import card_print_all

    test_config_path = "save/test_config.json"
    config = Config(**json.load(open(test_config_path, "r")))

    database = initialization(config)
    database.players = ["A"]

    # Give a 3 cards
    # Check if the cards are played
    database.hands["A"] = []
    database.hands["A"].append(database.deck.pop())
    database.hands["A"].append(database.deck.pop())
    database.hands["A"].append(database.deck.pop())
    print("A has cards:")
    card_print_all(database.hands["A"])
    print("Updated deck: ")
    card_print_all(database.deck)
    print("------ Card Play: A plays card 1 ------")
    play_cards("A", [160], database)
    print("After play, A has cards:")
    card_print_all(database.hands["A"])
    print("Deck:")
    card_print_all(database.deck)
    print("Discard should have 1 card:")
    card_print_all(database.discard)
