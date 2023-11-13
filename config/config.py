class Config():
    def __init__(self, **kwargs) -> None:
        self.num_rounds: int = kwargs['num_rounds']

        # Card deck
        self.num_decks: int = kwargs['num_decks']
        self.joker: bool = kwargs['joker']
        self.order: int = kwargs['order']

        # Card deal
        self.num_initial_hand: int = kwargs['num_initial_hand']
        self.num_cards_dealt_per_round: int = kwargs['num_cards_dealt_per_round']
        self.draw_flag: bool = kwargs['draw_flag']
        self.num_draw: int = kwargs['num_draw']
        
        # Community cards
        self.comm_flag: bool = kwargs['comm_flag']
        self.first_round_of_comm: int = kwargs['first_round_of_comm']
        self.first_round_num_comm: int = kwargs['first_round_num_comm']
        self.num_added_comm_per_round: int = kwargs['num_added_comm_per_round']

        # Card play
        self.play_flag: bool = kwargs['play_flag']
        self.num_cards_played_per_round: int = kwargs['num_cards_played_per_round']

        # Multiuser
        self.multiuser_flag: bool = False

        # Bid
        self.bidding_flag: bool = False