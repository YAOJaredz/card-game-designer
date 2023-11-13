class Card:
    """
    The object that stores the data of a card.

    Attributes:
        suit (str): The suit of the card.
        rank (str): The rank of the card.
        index (int): The index of the card in the deck for comparison.
    """
    def __init__(self, suit: str, rank: str, index: int) -> None:
        self.suit = suit
        self.rank = rank
        self.index = index

class CardDatabase:
    """
    The object that stores all the data of cards and players and coordinates the flow for each action.

    Attributes:
        deck (set): All the cards that have not been dealt yet.
        discard (set): All the cards that have been discarded.
        community (list): All the cards that are currently on the table.
        hands (dict): All the cards that each player has. The key is the player's name and the value is their hand.
        players (list): All the players in the game.
    """
    def __init__(self) -> None:
        self.deck: set[Card] = set()
        self.discard: set[Card] = set()
        self.community: list[Card] = list()
        self.hands: dict[str, list[Card]] = dict()
        self.players: list[str] = list()
    
    
    