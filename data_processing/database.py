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
    
    def __repr__(self) -> str:
        return f'Card({self.rank}, {self.suit})'
    
    def __hash__(self) -> int:
        return hash((self.suit, self.rank, self.index, self.identifier))
    

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Card):
            return self.index < other.index
        else:
            raise TypeError("Cannot compare Card with non-Card object.")


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
        self.snapshots: list[set] = list()

        self.card_recently_played: list[Card] = []

    def pop_from_deck(self, num_pop: int) -> list[Card]:
        """
        Pop specified number of cards from the deck.
        
        Args:
            num_pop (int): The number of cards to pop from the deck.

        Return:
            list[Card]: The popped cards.        
        """
        popped_cards = []
        for i in range(num_pop):
            popped_cards.append(self.deck.pop())
        return popped_cards

    def __eq__(self, other: object) -> bool:
        if isinstance(other, CardDatabase):
            return (self.deck, self.discard, self.community, self.hands, self.players) == (other.deck, other.discard, other.community, other.hands, other.players)
        else:
            raise TypeError("Cannot compare CardDatabase with non-CardDatabase object.")
        
    def __str__(self) -> str:
        return f'deck = {str(self.deck)}\ndiscard = {str(self.discard)}\ncommunity = {str(self.community)}\nhands = {str(self.hands)}\nplayers = {str(self.players)}'

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
        raise ValueError(f'Cannot find the card with identifier {identifier}.')
    
    def self_check(self) -> bool:
        """
        Check if the database is valid.
        """
        hands_set: set[Card] = set()
        for hand in self.hands.values():
            hands_set = hands_set.union(set(hand))
        snapshot = self.deck.union(self.discard).union(set(self.community)).union(hands_set)
        if self.snapshots == []:
            self.snapshots.append(snapshot)
            return True
        else:
            self.snapshots.append(snapshot)
            if self.snapshots[-2] == snapshot:
                return True
            else:
                return False
        
if __name__ == '__main__':
    print(CardDatabase())
    database = CardDatabase()
    database.self_check()
    print(database.snapshots)