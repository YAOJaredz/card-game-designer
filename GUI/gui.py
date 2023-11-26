import pygame
import sys

sys.path.append('.')
from data_processing.database import Card, CardDatabase
from operations.config import Config
from GUI.components import *
from GUI.stages import *

class GUI():
    def __init__(self):
        """ 
        There are 3 stages of the GUI:
            1. title page
            2. configuration page
            3. game page
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
        
    def events(self):
        next_stage = self.current_stage
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                next_stage = self.stages[self.current_stage].handle_events(event)
        
        if next_stage == -1:
            self.running = False
        elif next_stage != self.current_stage:
            self.update_stage(next_stage)
        return True
    
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()


    def update_stage(self, stage: int):
        """
        Update the stage of the gui. 
        """
        self.current_stage = stage
        pass
    
    def display_stage(self):
        """
        Display the current stage of the game.
        """
        self.stages[self.current_stage].update()
        pygame.display.flip()



if __name__ == '__main__':
    gui = GUI()
    while gui.running:
        gui.clock.tick(gui.fps)
        gui.events()
        gui.display_stage()
    pygame.quit()
    sys.exit()