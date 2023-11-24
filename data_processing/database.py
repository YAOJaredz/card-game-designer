class Card():
    """
    The object that stores the data of a card.

    Attributes:
        suit (str): The suit of the card.
        rank (str): The rank of the card.
        index (int): The index of the card in the deck for comparison.
        image (str): The image of the card.
        identifier (int): The unique identifier of the card.
    """
    def __init__(self, suit: str, rank: str, index: int, image:str, identifier:int) -> None:
        self.suit = suit
        self.rank = rank
        self.index = index
        self.image = image
        self.identifier = identifier

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Card):
            return (self.suit, self.rank, self.index) == (other.suit, other.rank, other.index)
        else:
            raise TypeError("Cannot compare Card with non-Card object.")
        
    def __hash__(self):
        # Hash based on the combination of suit, rank, and index
        return hash((self.suit, self.rank, self.index, self.identifier))
        
    def compare(self, other: object) -> int:
        if isinstance(other, Card):
            if self.index > other.index:
                return 1
            elif self.index < other.index:
                return -1
            else:
                return 0
        else:
            raise TypeError("Cannot compare Card with non-Card object.")
        return None
    
    def __str__(self) -> str:
        return f'suit = {self.suit}\trank = {self.rank}\tindex = {str(self.index)}\tidentifier = {str(self.identifier)}'
    


class CardDatabase():
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
        self.deck: list[Card] = list()
        self.discard: set[Card] = set()
        self.community: list[Card] = list()
        self.hands: dict[str, list[Card]] = dict()
        self.players: list[str] = list()
    
    def __eq__(self, other: object) -> bool:
        if isinstance(other, CardDatabase):
            return (self.deck, self.discard, self.community, self.hands, self.players) == (other.deck, other.discard, other.community, other.hands, other.players)
        else:
            raise TypeError("Cannot compare CardDatabase with non-CardDatabase object.")
        
    def __str__(self) -> str:
        return str(self.__dict__)
    
    def find_card(self, identifier: int) -> Card:
        """Find the card by identifier.
        This function will search for the card by identifier in the deck, discard, and player hands.
        Args:
            identifier (int): The identifier of the card.
        Return:
            card (Card): The card with the identifier.
        """
        # Search in the deck
        for card in self.deck:
            if card.identifier == identifier:
                return card
        # Search in the discard
        for card in self.discard:
            if card.identifier == identifier:
                return card
        # Search in the community
        for card in self.community:
            if card.identifier == identifier:
                return card
        # Search in player hands
        for hand in self.hands.values():
            for card in hand:
                if card.identifier == identifier:
                    return card
    
if __name__ == '__main__':
    print(CardDatabase())