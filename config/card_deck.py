import os, sys
import json
sys.path.append('.')

import unit_test as ut
from  data_processing.database import Card, CardDatabase
from  config import Config


def initialization(config: Config) -> CardDatabase:
    """Initialize the card deck and initial hand
    The users are able to specify the number of decks, whether or not to include jokers, and the order of the cards.
    Args:
        config (Config): The configuration of the game, which contains all of the configurations for the game.
    Return:
        CardDatabase: The card deck, and users will have their initial hands.
    """
    database=CardDatabase()
    return database

if __name__=='__main__':
    empty_config=json.load(open('save/empty_config.json'))
    ut.unit_test(initialization, (empty_config), CardDatabase(), 'Initialization')

