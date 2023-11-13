import gui
from data_processing.database import Card, CardDatabase
from config.config import Config

class GUI():
    def __init__(self):
        """ 
        There are 3 stages of the GUI:
            1. title page
            2. configuration page
            3. game page
        """
        self.stage = 0

    def initialize_gui(self):
        """
        Display the GUI for the game at the initial state. (title, start a new game, play an old game, quit...)
        """
        pass

    def setting(self)->dict:
        """ 
        Take the user input and set up the game configuration.
        At the page of starting a new game, users have the option to save this configuration and start playing. 
        Return: 
            config (dict): all configurations for the game. (Detail in config/config.py)
        """
        config={}
        return config

    def update_stage(self, stage: int):
        """
        Update the stage of the gui. 
        """
        self.stage = stage
        pass
    
    def display_stage(self):
        """
        Display the current stage of the game.
        """
        pass
    