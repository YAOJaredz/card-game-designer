import json


class Config:
    """
    A class representing the configuration settings for a card game.

    Attributes:
        `num_rounds` (int): The number of rounds in the game.\n
        `num_decks` (int): The number of decks of cards to be used.\n
        `joker` (bool): Indicates whether jokers are included in the deck.\n
        `order` (int): The order in which the cards are arranged.\n
        `num_initial_hand` (int): The number of cards each player receives initially.\n
        `num_cards_dealt_per_round` (int): The number of cards dealt to each player per round.\n
        `draw_flag` (bool): Indicates whether drawing cards is allowed.\n
        `num_draw` (int): The number of cards a player can draw.\n
        `repetitive_draw` (bool): Indicates whether drawing cards can be repeated per round.\n
        `comm_flag` (bool): Indicates whether community cards are used.\n
        `first_round_of_comm` (int): The round number when community cards are first introduced.\n
        `first_round_num_comm` (int): The number of community cards in the first round.\n
        `num_added_comm_per_round` (int): The number of additional community cards added per round.\n
        `play_flag` (bool): Indicates whether playing cards is allowed.\n
        `num_cards_played_per_round` (int): The number of cards played by each player per round.\n
        `sort_hands` (bool): Indicates whether player hands should be sorted.\n
        `display_cp` (bool): Indicates whether the current player's hand should be displayed.\n
        `multiuser_flag` (bool): Indicates whether the game supports multiple users.\n
        `bidding_flag` (bool): Indicates whether bidding is enabled.\n
    """

    def __init__(self, **kwargs) -> None:
        """
        Initializes the Config object with the provided keyword arguments.

        Args:
            **kwargs: Keyword arguments containing the configuration values.

        Raises:
            KeyError: If a required key is not found in the configuration file.
            ValueError: If a value is not valid in the configuration file.
        """
        print(kwargs)
        try:
            self.num_rounds: int = int(kwargs["num_rounds"])

            # Card deck
            self.num_decks: int = int(kwargs["num_decks"])
            self.joker: bool = bool(kwargs["joker"])
            self.order: int = int(kwargs["order"])

            # Card deal
            self.num_initial_hand: int = int(kwargs["num_initial_hand"])
            self.num_cards_dealt_per_round: int = int(
                kwargs["num_cards_dealt_per_round"]
            )
            self.draw_flag: bool = bool(kwargs["draw_flag"])
            self.num_draw: int = int(kwargs["num_draw"])
            self.repetitive_draw: bool = bool(kwargs["repetitive_draw"])

            # Community cards
            self.comm_flag: bool = bool(kwargs["comm_flag"])
            self.first_round_of_comm: int = int(kwargs["first_round_of_comm"])
            self.first_round_num_comm: int = int(kwargs["first_round_num_comm"])
            self.num_added_comm_per_round: int = int(kwargs["num_added_comm_per_round"])

            # Card play
            self.play_flag: bool = bool(kwargs["play_flag"])
            self.num_cards_played_per_round: int = int(
                kwargs["num_cards_played_per_round"]
            )
            self.sort_hands: bool = bool(kwargs["sort_hands"])
            self.display_cp: bool = bool(kwargs["display_cp"])

            # Multiuser
            self.multiuser_flag: bool = False

            # Bid
            self.bidding_flag: bool = False
        except KeyError as e:
            print(f"Key {e} not found in the configuration file.")
            raise e
        except ValueError as e:
            print(f"Value {e} is not valid in the configuration file.")
            raise e
        
        # handle negative values: 
        non_negative_keys = self.__dict__.keys() - {'num_cards_played_per_round', 'num_rounds'}
        for key in non_negative_keys:
            if self.__dict__[key] < 0:
                raise ValueError(f"{key} cannot be negative.")
        
        # num of deck must be positive
        if self.num_decks <= 0:
            raise ValueError("Number of decks must be positive.")

    def __str__(self) -> str:
        return str(self.__dict__)

    def save(self, path: str) -> None:
        """
        Save the configuration object to a JSON file.

        Args:
            path (str): The path to the JSON file.
        """
        json.dump(self.__dict__, open(path, "w"))


if __name__ == "__main__":
    config = json.load(open("save/test_config.json", "r"))

    # Test how test_config.json are loaded
    config_obj = Config(**config)
    print(config)
    print(config_obj)
