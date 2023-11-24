import os, sys
import json
sys.path.append('.')

from data_processing.database import Card, CardDatabase
from operations.config import Config

def update_community(database: CardDatabase, round: int, config: Config) -> CardDatabase:
    """
    Updates the community cards for each round.

    Args:
        database (CardDatabase): The card database.
        round (int): The current round.
        config (Config): The configuration settings.

    Return:
        CardDatabase: The updated card database.
    """
    if not config.comm_flag:
        return database
    
    if round == config.first_round_of_comm:
        database.community = database.pop_from_deck(config.first_round_num_comm)
    elif round > config.first_round_of_comm:
        database.community.extend(database.pop_from_deck(config.num_added_comm_per_round))
    return database

if __name__ == '__main__':
    from card_deck import initialization

    config = Config(**json.load(open('save/test_config.json','r')))

    print(config.first_round_of_comm)

    database = initialization(config)
    print(database.community)
    database = update_community(database, 1, config)
    print(database.community)
    database = update_community(database, 2, config)
    print(database.community)
    database = update_community(database, 3, config)
    print(database.community)