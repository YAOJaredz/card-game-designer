import json

class Config():
    """
    A class representing the configuration settings for a card game.
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
        try:
            self.num_rounds: int = kwargs['num_rounds']

            # Card deck
            self.num_decks: int = int(kwargs['num_decks'])
            self.joker: bool = bool(kwargs['joker'])
            self.order: int = int(kwargs['order'])

            # Card deal
            self.num_initial_hand: int = int(kwargs['num_initial_hand'])
            self.num_cards_dealt_per_round: int = int(kwargs['num_cards_dealt_per_round'])
            self.draw_flag: bool = bool(kwargs['draw_flag'])
            self.num_draw: int = int(kwargs['num_draw'])
            
            # Community cards
            self.comm_flag: bool = bool(kwargs['comm_flag'])
            self.first_round_of_comm: int = int(kwargs['first_round_of_comm'])
            self.first_round_num_comm: int = int(kwargs['first_round_num_comm'])
            self.num_added_comm_per_round: int = int(kwargs['num_added_comm_per_round'])

            # Card play
            self.play_flag: bool = bool(kwargs['play_flag'])
            self.num_cards_played_per_round: int = int(kwargs['num_cards_played_per_round'])

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
        

    def __str__(self) -> str:
        return str(self.__dict__)
    
    def save(self, path: str) -> None:
        """
        Save the configuration object to a JSON file.

        Args:
            path (str): The path to the JSON file.
        """
        json.dump(self.__dict__, open(path, 'w'))

if __name__ == '__main__':
    with open('save/test_config.json','r') as file:
        config = json.load(file)

    config_obj = Config(**config)
    print(config)
    print(config_obj)