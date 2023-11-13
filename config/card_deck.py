from  data_processing.database import Card, CardDatabase
def create_card_deck(decks:int, jokers:bool, order: int) -> CardDatabase:
    """Initialize the card deck
    The users are able to specify the number of decks, whether or not to include jokers, and the order of the cards.
    Args:
        decks (int): The number of decks to use.
        jokers (bool): Whether or not to include jokers.
        order (int): The order of the cards. eg. 0 = A is the smallest; 1 = 3 is the smallest...
    Return:
        CardDatabase: The card deck.
    """
    database=CardDatabase()
    return database
    