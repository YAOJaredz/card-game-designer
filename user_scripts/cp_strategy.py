import random

from data_processing.database import Card

class ComputerPlayer:
    def __init__(self) -> None:
        self.name = 'cp'
        self.hand: list[Card] = []
        self.played_cards: list[Card] = []

    def cp_play_card(
            self,
            round: int,
            hand: list[Card],
            community: list[Card],
            num_cards_played_per_round: int,
            cards_recently_played: list[Card],
    ) -> list[Card]:
        """
        The strategy of the computer player.
        User can use round, community, cards_recently_played to develop their own computer player strategy. 
        As a default in the program, the computer player will randomly choose cards to play.
        Args:
            round (int): The current round.
            hand (list[Card]): The cards in the hand.
            community (list[Card]): The community cards.
            num_cards_played_per_round (int): The number of cards to be played per round.
            cards_recently_played (list[Card]): The cards that are recently played.
        Return:
            list[Card]: The cards to be played.
        """
        self.hand = hand
        # num_cards_played_per_round == -1 means unlimited number of cards to play, then randomly choose a number of cards to play. 
        if num_cards_played_per_round == -1:
            num_play=random.randint(0, len(self.hand))
            card_to_play = random.sample(self.hand, num_play)
        else: 
            card_to_play = random.sample(self.hand, min(num_cards_played_per_round, len(self.hand)))
        self.played_cards.extend(card_to_play)
        return card_to_play