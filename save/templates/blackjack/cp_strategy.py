"""
This is a corresponding computer player strategy example for Blackjack.
"""

import random

from data_processing.database import Card

class ComputerPlayer:
    def __init__(self) -> None:
        self.name = 'cp'
        self.hand: list[Card] = []
        self.played_cards: list[Card] = []

    def cp_play_card(
            self,
            *args
    ):
        pass
    
    def cp_draw_card(
            self,
            *args
    ):
        pass
    
    def cp_draw_card_repetitive(
            self,
            round: int,
            hand: list[Card],
            community: list[Card],
            num_cards_drawn_per_time: int
    ) -> bool:
        """
        The draw card strategy of the computer player if repetitive card draw allowed.
        As a default in the program, the computer player will have 50% chance to draw card.

        Args:
            round (int): The current round.
            hand (list[Card]): The cards in the hand.
            community (list[Card]): The current community cards.
            repetitive_draw_flag (bool): Whether or not to allow repetitive draw.
            num_cards_drawn_per_time (int): The number of cards to be drawn per round.
        Return:
            list[Card]: The number of times to draw cards.
        """
        all_ranks = [str(card.rank) for card in hand]
        all_ranks = list(map(self.convert_card, all_ranks)) # type: ignore
        card_sum = sum(all_ranks) # type: ignore
        if random.random() < (21-card_sum)/10:
            return True
        else:
            return False
        
    def convert_card(self, rank: str) -> int:
            """
            Convert a card rank to its corresponding numerical value.

            Args:
                rank (str): The rank of the card.

            Returns:
                int: The numerical value of the card.
            """
            match rank:
                case 'A':
                    return 1
                case 'J':
                    return 11
                case 'Q':
                    return 12
                case 'K':
                    return 13
                case _:
                    return int(rank)
