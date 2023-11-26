import pygame
import pygame_menu as pm
import sys
import json

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
        try: 
            self.new_config = json.load(open('save/empty_config.json','r'))
        except FileNotFoundError:
            self.new_config = dict()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.ui = pygame_gui.UIManager((self.width, self.height))
        
        self.ui_config = json.load(open('GUI/setting_config.json', 'r'))

        self.dropdown = dict()
        for i in self.ui_config['DropDown']:
            # self.new_config[i] = 
            self.dropdown[i] = DropDown(*self.ui_config['DropDown'][i], ui_manager=self.ui,uid=i)
        
        self.textbox = dict()
        for i in self.ui_config['TextBox']:
            self.textbox[i] = TextBox(*self.ui_config['TextBox'][i][0], ui_manager=self.ui,uid=i)
            self.textbox[i].set_text(str(self.ui_config['TextBox'][i][1]))

        self.all_sprites = pygame.sprite.Group()
        self.quit_button = Button(290, 600, 200, 40, "Quit")
        self.save_button = Button(510, 600, 200, 40, "Save")
        self.all_sprites.add(self.quit_button, self.save_button)
    
    def handle_events(self, event):
        self.ui.process_events(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.quit_button.rect.collidepoint(event.pos):
                print("Quit Clicked!")
                return -1
            elif self.save_button.rect.collidepoint(event.pos):
                for key in self.dropdown.keys():
                    self.new_config[key] = self.dropdown[key].selected_option
                for key in self.textbox.keys():
                    self.new_config[key] = self.textbox[key].get_text()
                print(self.new_config)
        elif event.type == pygame.USEREVENT: 
            if event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED or \
            event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                self.new_config[event.ui_object_id] = event.text

        return 1

    def update(self):
        self.screen.fill((0, 0, 0))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen)

        self.ui.update(6e-2)
        self.ui.draw_ui(self.screen) 
        pygame.display.flip()

class Game:
    def __init__(self):
        pass

if __name__ == '__main__':
    from gui import GUI
    gui = GUI()
    while gui.running:
        gui.clock.tick(gui.fps)
        gui.events()
        gui.display_stage()
    pygame.quit()
    sys.exit()