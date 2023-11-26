import pygame
import sys

sys.path.append('.')
from data_processing.database import Card, CardDatabase
from operations.config import Config
from GUI.components import *

class GUI():
    def __init__(self):
        """ 
        There are 3 stages of the GUI:
            1. title page
            2. configuration page
            3. game page
        """
        self.stage = 0
        pygame.init()
        self.width, self.height = 1000, 700
        self.fps = 60
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Card Game Designer")
        self.clock = pygame.time.Clock()
        self.running = True
        self.openning()
    
    def run(self):
        while self.running:
            self.clock.tick(60)
            self.events()
            self.display_stage()
        pygame.quit()
        sys.exit()
        
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.quit_button.rect.collidepoint(event.pos):
                    print("Quit Clicked!")
                    self.running = False
                elif self.new_button.rect.collidepoint(event.pos):
                    print("Create new Clicked!")
                    self.update_stage(1)
                elif self.load_button.rect.collidepoint(event.pos):
                    print("Load Clicked!")
                    self.update_stage(2)
        return True
    
    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def openning(self):
        """
        Display the GUI for the game at the initial state. (Stage 0)
        It will display 3 buttons: create new templates, load templates, quit.
        Create new templates: users can create new templates for the game.
        Load templates: users can load the templates they have created before.
        """
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.all_sprites = pygame.sprite.Group()
        self.open_label = Label(240, 140, "Card Game Designer", 80)
        self.quit_button = Button(370, 530, 260, 60, "Quit")
        self.new_button = Button(370, 350, 260, 60, "Create New")
        self.load_button = Button(370, 440, 260, 60, "Load Templates")
        self.all_sprites.add(self.quit_button,self.new_button,self.load_button,self.open_label)
        return True

    def setting(self):
        """ 
        Take the user input and set up the game configuration.
        At the page of starting a new game, users have the option to save this configuration and start playing. 
        Return: 
            config (dict): all configurations for the game. (Detail in config/config.py)
        """
        self.new_config = dict()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.all_sprites = pygame.sprite.Group()
        self.quit_button = Button(370, 530, 260, 60, "Quit")
        self.all_sprites.add(self.quit_button)

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
        self.screen.fill((0, 255, 255))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen)
        pygame.display.flip()



if __name__ == '__main__':
    gui = GUI()
    while gui.running:
        gui.clock.tick(gui.fps)
        gui.events()
        gui.display_stage()
    pygame.quit()
    sys.exit()