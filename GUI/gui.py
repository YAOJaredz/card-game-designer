import pygame
import sys

sys.path.append(".")
from data_processing.database import Card, CardDatabase
from operations.config import Config
from GUI.components import *
from GUI.stages import *


class GUI:
    """
    The GUI class represents the graphical user interface for the Card Game Designer.
    It coordinates the different stages of the GUI and handles the events generated by the user.

    Attributes:
        current_stage (int): The current stage of the GUI.
        width (int): The width of the GUI window.
        height (int): The height of the GUI window.
        fps (int): The frames per second for the GUI.
        screen (pygame.Surface): The surface representing the GUI window.
        font (pygame.font.Font): The font used for text in the GUI.
        clock (pygame.time.Clock): The clock used to control the frame rate.
        running (bool): Flag indicating if the GUI is running.
        stages (list): List of stages in the GUI.
        database (CardDatabase): The card database used in the GUI.

    Methods:
        __init__(): Initializes the GUI object.
        events(): Process the events in the game.
        update_stage(stage: int): Update the stage of the GUI.
        display_stage(): Display the current stage of the GUI.
    """
    def __init__(self) -> None:
        """
        Initializes the GUI object.
        There are 3 stages of the GUI:
            1. Title page
            2. Setting page
            3. Game page
        """
        self.current_stage = 0
        pygame.init()
        self.width, self.height = 1000, 700
        self.fps = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Card Game Designer")
        self.font = pygame.font.Font(None, 30)
        self.clock = pygame.time.Clock()
        self.running = True
        self.stages = [Openning(), Setting(), Game()]
        self.database = CardDatabase()

    def events(self) -> int | bool:
        """
        Process the events in the game.

        This method handles the events generated by the user, such as mouse clicks or keyboard inputs.
        It checks for the quit event to exit the game, and delegates the handling of other events to the
        current stage of the game.

        Returns:
            bool: False if the operation is quit. True otherwise.
        """
        next_stage = self.current_stage
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            else:
                next_stage = self.stages[self.current_stage].handle_events(event)

            if next_stage == -1:
                return False
            elif next_stage != self.current_stage:
                self.update_stage(next_stage)
        return True
    
    def end_events(self) -> int:
            """
            Handle the end events of the game.

            Returns:
                int: The result of the end events. 
                        -1 if the game should be quit.
                        0 if the game should direct to title page.
                        2 if the game should keep still.
            """
            if self.current_stage != 2:
                raise ValueError("end_events() can only be called in the game stage.")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -1
                if event.type == pygame.KEYDOWN:
                    return 0
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return 0
                else:
                    self.stages[self.current_stage].handle_events(event)
            return 2

    def update_stage(self, stage: int) -> None:
        """
        Update the stage of the GUI.

        Args:
            stage (int): The new stage to set.
        """
        if stage == 2:
            self.config = self.stages[self.current_stage].get_config()
            try:
                Config(**self.config)
            except ValueError:
                self.stages[self.current_stage].display_alert("Invalid configuration values.")
                return None
            except KeyError:
                self.stages[self.current_stage].display_alert("Broken configuration values.")
                return None
            self.stages[2].config = self.config
            self.stages[2].reset(self.config)
        self.current_stage = stage

    def display_stage(self, database: CardDatabase = None, config: Config = None, game_end: bool = False, stage: int = None):
        """
        Display the current stage of the game.

        Args:
            database (CardDatabase): The card database used in the GUI.
            config (Config): The configuration of the game.
            game_end (bool): Whether or not the game has ended.
        """
        self.clock.tick(self.fps)
        if stage is not None:
            self.stages[stage].update(database, config)
        if self.current_stage != 2:
            self.stages[self.current_stage].update()
        elif game_end:
            self.stages[2].update(database, config, game_end=True)
        else:
            self.stages[self.current_stage].update(database, config)
            
        pygame.display.flip()



if __name__ == "__main__":
    from operations.controller import main_loop
    main_loop()