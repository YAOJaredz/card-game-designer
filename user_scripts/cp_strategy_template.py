"""
Template for computer player strategy.
Users can use this template to develop their own computer player strategy by modifying the cp_play_card function.
The function will be called with the following information for users to use in the cp_play_card function:
1. round (int): The current round.
2. hand (list[Card]): The cards in the hand.
3. community (list[Card]): The current community cards.
4. num_cards_played_per_round (int): The number of cards to be played per round.
5. cards_recently_played (list[Card]): The cards that are recently played by other players.

To use non-default computer player strategy, users can specify "cp_strategy_path" in the configuration file.
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
    
    def cp_draw_card(
            self,
            round: int,
            hand: list[Card],
            community: list[Card],
            num_cards_drawn_per_time: int
    ) -> int:
        """
        The draw card strategy of the computer player if no repetitive card draw allowed.
        As a default in the program, the computer player will draw one card per round.

        Args:
            round (int): The current round.
            hand (list[Card]): The cards in the hand.
            community (list[Card]): The current community cards.
            repetitive_draw_flag (bool): Whether or not to allow repetitive draw.
            num_cards_drawn_per_time (int): The number of cards to be drawn per round.
        Return:
            int: The number of times to draw cards.
        """
        return 1
    
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
            bool: Whether or not to draw card or not. 
        """
        if random.random() > 0.5:
            return True
        else:
            return False