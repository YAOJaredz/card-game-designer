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
        print(hand)
        card_to_play = random.sample(self.hand, min(num_cards_played_per_round, len(self.hand)))
        print(card_to_play)
        self.played_cards.extend(card_to_play)
        return card_to_play