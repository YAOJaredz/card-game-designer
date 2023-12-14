import os, sys
import json

sys.path.append(".")

from data_processing.database import Card, CardDatabase
from operations.config import Config


def create_one_deck(joker: bool, order: int) -> list[Card]:
    """
    Create one deck of cards.
    This function will create a deck of cards based on the input.

    Args:
        joker (bool): Whether or not to include jokers.
        order (int): The order of the cards.
                    0: A is the smallest
                    1: 3 is the smallest

    Return:
        list[Card]: The deck of cards.
    """

    suits = ["Spade", "Heart", "Club", "Diamond"]
    rank0 = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    rank1 = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
    deck = []
    index = 1
    identifier = 1

    if order == 0:
        for rank in rank0:
            for suit in suits:
                deck.append(Card(suit, rank, index, f"card_images/{rank}{suit[0]}.png", identifier))
            index += 1
    elif order == 1:
        for rank in rank1:
            for suit in suits:
                deck.append(Card(suit, rank, index, f"card_images/{rank}{suit[0]}.png", identifier))
            index += 1
    else:
        raise ValueError("Invalid order value.")
    if joker:
        deck.append(Card("Joker", "Black", index, "card_images/14.png", identifier))
        index += 1
        deck.append(Card("Joker", "Red", index, "card_images/15.png", identifier))
        index += 1
    return deck

def create_multiple_decks(num_decks: int, joker: bool, order: int) -> set[Card]:
    """
    Create multiple decks of cards.
    This function will create multiple decks of cards based on the input.

    Args:
        num_decks (int): The number of decks to be created.
        joker (bool): Whether or not to include jokers.
        order (int): The order of the cards.
                    0: A is the smallest
                    1: 3 is the smallest

    Return:
        list[Card]: The deck of cards.
    """
    deck = []
    for i in range(num_decks):
        deck += create_one_deck(joker, order)
    identifiers = set(range(len(deck)))
    for i in range(len(deck)):
        deck[i].identifier = identifiers.pop()
    return set(deck)


def card_print_all(deck: set[Card]) -> None:
    """
    Print all the cards in the deck.
    This function helps to print all the content of cards in the deck.
    Serve as a test function.

    Args:
        deck (list[Card]): A deck of cards
    """
    for card in deck:
        print(card)
    return None


def initialization(config: Config) -> CardDatabase:
    """
    Initialize the card deck and initial hand
    The users are able to specify the number of decks, whether or not to include jokers, and the order of the cards.

    Args:
        config (Config): The configuration of the game, which contains all of the configurations for the game.

    Return:
        CardDatabase: The card deck, and users will have their initial hands.
    """
    database = CardDatabase()
    # initialize the deck based on joker and order
    database.deck = create_multiple_decks(config.num_decks, config.joker, config.order)
    return database


if __name__ == "__main__":
    # test of empty config
    print("Test of empty config (nothing in deck); completed by unit_test function. \n")
    empty_config = json.load(open("save/empty_config.json"))
    empty_config = Config(**empty_config)
    print(initialization(empty_config).deck)

    # test config: num_decks=3, joker=true, order=1
    print(
        "Test of configuration: num_decks=3, joker=true, order=1 (3 has the smallest index)\n"
    )
    print("Desired output:")
    print("162 cards in total; with jokers; 3 has the smallest index. \n")
    test_config = json.load(open("save/test_config.json"))
    test_config = Config(**test_config)
    database = initialization(test_config)
    card_print_all(database.deck)
