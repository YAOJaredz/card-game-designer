class Config():
    def __init__(self, **kwargs) -> None:
        self.num_rounds = kwargs['num_rounds']

        # Card deck
        self.num_decks = kwargs['num_decks']
        self.joker = kwargs['joker']
        self.order = kwargs['order']

        # Card deal
        self.initial_hand = kwargs['initial_hand']
        self.num_cards_per_round = kwargs['num_cards_per_round']
        self.draw_flag = kwargs['draw_flag']
        self.num_draw = kwargs['num_draw']
        
        # Community cards
        self.comm_flag = kwargs['comm_flag']
        self.first_round = kwargs['first_round']
        self.first_round_num = kwargs['first_round_num']
        self.num_added_per_round = kwargs['num_added_per_round']

        # Card play
        self.play_flag = kwargs['play_flag']
        self.num_cards_played_per_round = kwargs['num_cards_played_per_round']

        # Multiuser
        self.multiuser_flag = False

        # Bid
        self.bid_flag = False