import pygame
import sys

sys.path.append('.')
from GUI.components import *

WIDTH, HEIGHT = 1000, 700

class Openning:
    def __init__(self):
        """
        Display the GUI for the game at the initial state. (Stage 0)
        It will display 3 buttons: create new templates, load templates, quit.
        Create new templates: users can create new templates for the game.
        Load templates: users can load the templates they have created before.
        """
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.all_sprites = pygame.sprite.Group()
        self.open_label = Label(240, 140, "Card Game Designer", 80)
        self.quit_button = Button(370, 530, 260, 60, "Quit")
        self.new_button = Button(370, 350, 260, 60, "Create New")
        self.load_button = Button(370, 440, 260, 60, "Load Templates")
        self.all_sprites.add(self.quit_button,self.new_button,self.load_button,self.open_label)
    
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.quit_button.rect.collidepoint(event.pos):
                print("Quit Clicked!")
                return -1
            elif self.new_button.rect.collidepoint(event.pos):
                print("Create new Clicked!")
                return 1
            elif self.load_button.rect.collidepoint(event.pos):
                print("Load Clicked!")
                return 2
        return 0
    
    def update(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen)
        pygame.display.flip()


class Setting:
    def __init__(self):
        """ 
        Take the user input and set up the game configuration.
        At the page of starting a new game, users have the option to save this configuration and start playing. 
        Return: 
            config (dict): all configurations for the game. (Detail in config/config.py)
        """
        self.width, self.height = WIDTH, HEIGHT
        self.new_config = dict()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.all_sprites = pygame.sprite.Group()
        self.quit_button = Button(370, 530, 260, 60, "Quit")
        self.all_sprites.add(self.quit_button)
    
    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.quit_button.rect.collidepoint(event.pos):
                print("Quit Clicked!")
                return -1
        return 1

    def update(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen)
        pygame.display.flip()

class Game:
    def __init__(self):
        pass
