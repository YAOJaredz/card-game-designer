class Card():
    """
    The object that stores the data of a card.

    Attributes:
        suit (str): The suit of the card.
        rank (str): The rank of the card.
        index (int): The index of the card in the deck for comparison.
        image (str): The image of the card.
    """
    def __init__(self, suit: str, rank: str, index: int, image) -> None:
        self.suit = suit
        self.rank = rank
        self.index = index
        self.image = image

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Card):
            return (self.suit, self.rank, self.index) == (other.suit, other.rank, other.index)
        else:
            raise TypeError("Cannot compare Card with non-Card object.")
        
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
    
    def card_print(self) -> None:
        """Print the card.
        This function will print the card's suit, rank and index.
        Args:
            card (Card): The card to be printed.
        Return:
            None
        """
        print("suit = "+self.suit+"; rank = "+self.rank+"; index= "+str(self.index) +"\n")
        return None
    


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
        self.deck: set[Card] = set()
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
    
if __name__ == '__main__':
    print(CardDatabase())