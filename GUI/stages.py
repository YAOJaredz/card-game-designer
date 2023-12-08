import pygame
import sys
import json
import tkinter as tk
from tkinter import filedialog

tk.Tk().withdraw()

sys.path.append(".")
from GUI.components import *
from data_processing.database import Card, CardDatabase
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
        self.all_sprites.add(
            self.quit_button, self.new_button, self.load_button, self.open_label
        )

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
                file_path = filedialog.askopenfilename(
                    initialdir="save",
                    title="Select a File",
                    filetypes=(("Text files", "*.json"), ("all files", "*.*")),
                )
                try:
                    self.loaded_config = json.load(open(file_path, "r"))
                    return 2
                except FileNotFoundError:
                    print("No valid file selected.")

        return 0
    
    def get_config(self):
        return self.loaded_config

    def update(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen, pygame.mouse.get_pos())
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
            self.new_config = json.load(open("save/empty_config.json", "r"))
        except FileNotFoundError:
            self.new_config = dict()

        self.screen = pygame.display.set_mode((self.width, self.height))
        self.ui = pygame_gui.UIManager((self.width, self.height), "GUI/themes.json")

        self.ui_config = json.load(open("GUI/setting_config.json", "r"))

        self.dropdown = dict()
        for i in self.ui_config["DropDown"]:
            # self.new_config[i] =
            self.dropdown[i] = DropDown(
                *self.ui_config["DropDown"][i], ui_manager=self.ui, uid=i
            )

        self.textbox = dict()
        for i in self.ui_config["TextBox"]:
            self.textbox[i] = TextBox(
                *self.ui_config["TextBox"][i][0], ui_manager=self.ui, uid=i
            )
            self.textbox[i].set_text(str(self.ui_config["TextBox"][i][1]))

        self.labels = dict()
        for i in self.ui_config["Labels"]:
            self.labels[i] = Label_UI(
                *self.ui_config["Labels"][i], ui_manager=self.ui, uid=i
            )

        self.all_sprites = pygame.sprite.Group()
        self.setting_title = Label(420, 30, "Setting", 60)
        self.back_button = Button(170, 600, 200, 40, "Back")
        self.continue_button = Button(630, 600, 200, 40, "Continue")
        self.save_button = Button(400, 600, 200, 40, "Save")
        self.all_sprites.add(
            self.continue_button, self.save_button, self.setting_title, self.back_button
        )

    def handle_events(self, event):
        self.ui.process_events(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.continue_button.rect.collidepoint(event.pos):
                print("Continue Clicked!")
                return 2
            elif self.back_button.rect.collidepoint(event.pos):
                print("Back Clicked!")
                return 0
            elif self.save_button.rect.collidepoint(event.pos):
                # Save the config
                self.get_config()
                print(self.new_config)
                save_path = filedialog.asksaveasfile(
                    initialdir="IOTEDU",
                    title="Save template as",
                    mode="w",
                    defaultextension=json,
                    filetypes=(("Text files", "*.json"), ("all files", "*.*")),
                )
                if save_path is None:
                    print("No valid file path specified.")
                else:
                    json.dump(self.new_config, save_path)
                    save_path.close()
                    print("Config saved!")
        elif event.type == pygame.USEREVENT:
            if (
                event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED
                or event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED
            ):
                self.new_config[event.ui_object_id] = event.text

        return 1
    
    def get_config(self):
            """
            Retrieves the configuration settings from the setting page.

            Returns:
                dict: A dictionary containing the configuration settings.
            """
            for key in self.dropdown.keys():
                if self.dropdown[key].selected_option == "Yes":
                    self.new_config[key] = True
                elif self.dropdown[key].selected_option == "No":
                    self.new_config[key] = False
                else:
                    self.new_config[key] = self.dropdown[key].selected_option
            for key in self.textbox.keys():
                self.new_config[key] = self.textbox[key].get_text()
            return self.new_config


    def update(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen, pygame.mouse.get_pos())

        self.ui.update(6e-2)
        self.ui.draw_ui(self.screen)
        pygame.display.flip()


class Game:
    def __init__(self):
        """
        Display the Card Game playing GUI.
        """
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.all_sprites = pygame.sprite.Group()
        self.back_button = Button(10, 10, 80, 40, "Back")
        self.all_sprites.add(self.back_button)
        self.ui=pygame_gui.UIManager((self.width, self.height), "GUI/themes.json")
        
        #display the card table
        self.bg=pygame.transform.smoothscale(pygame.image.load('card_images/bg.jpg'), (self.width, self.height))
        
        #display the computer player
        self.cp_image=pygame.transform.smoothscale(pygame.image.load('card_images/cp.png'), (100, 120))
        
        #text box for playing cards
        self.played_card_text_box=TextBox(280, 450, 300, 40, ui_manager=self.ui, uid="played_card_text_box")
        
        #text box label
        self.played_card_text_box_label=Label_UI(325, 420, 300, 40, "Played Cards: (Separated by ,)", ui_manager=self.ui, uid="played_card_text_box_label")
        
        #record played card for this round
        self.played_cards = None
        
        #add play card button
        self.play_button=Button(600, 450, 70, 35, "Play!")  
        self.all_sprites.add(self.play_button)  
        
        # add card deck
        self.deck_image=pygame.transform.smoothscale(pygame.image.load('card_images/deck.png'), (150, 100))
        
    def handle_events(self, event):
        self.ui.process_events(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.rect.collidepoint(event.pos):
                print("Back Clicked!")
                return 1
            elif self.play_button.rect.collidepoint(event.pos):
                print("Play Card Clicked!")
                played_cards_str = self.played_card_text_box.get_text().split(",")
                self.played_cards = [int(card) for card in played_cards_str]
                # print(self.played_cards)
        return 2
    
    def display_player_cards(self, database: CardDatabase):
        """ Display the cards in player's hand.
        Args:
            database (CardDatabase): The card database.
                                    Get the cards in hand. 
        """
        cards=database.hands["player1"]
        num_cards=len(cards)
        display_range_width=(num_cards-1)*40+100
        start_x=(self.width-display_range_width)/2
        for card in cards:
            # display card image
            image=pygame.transform.smoothscale(pygame.image.load(card.image), (100, 150))
            self.screen.blit(image, (start_x, 520))
            # display card identifier
            identifier=pygame.font.Font(None, 24).render(str(card.identifier), True, (0, 0, 0))
            self.screen.blit(identifier, (start_x+10, 500))
            start_x+=40  
              
            
    def display_cp_cards(self, database: CardDatabase):
        """ Display the cards in cp's hand.
        Args:
            database (CardDatabase): The card database.
                                    Get the cards in hand. 
        """
        cards=database.hands["cp"]
        num_cards=len(cards)
        display_range_width=(num_cards-1)*40+60
        start_x=(self.width-display_range_width)/2
        image=pygame.transform.smoothscale(pygame.image.load("card_images/back.png"), (60, 100))
        for card in cards:
            # display card backs
            self.screen.blit(image, (start_x, 30))
            start_x+=20    
            
    def display_community_cards(self, database: CardDatabase):
        """ Display the cards in community.
        Args:
            database (CardDatabase): The card database.
                                    Get the cards in community. 
        """
        cards=database.community
        num_cards=len(cards)
        display_range_width=(num_cards-1)*20+60
        start_x=230
        for card in cards:
            # display card image
            image=pygame.transform.smoothscale(pygame.image.load(card.image), (60, 90))
            self.screen.blit(image, (start_x, 270))
            start_x+=20
            
    def update(self, database: CardDatabase): 
        self.screen.blit(self.bg, (0, 0))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen, pygame.mouse.get_pos())
        self.screen.blit(self.cp_image, (100, 20))
        self.screen.blit(self.deck_image, (30, 350))
        self.ui.update(6e-2)
        self.ui.draw_ui(self.screen)

        # if users have cards in hand, display them
        if len(database.hands.keys()) != 0:
            self.display_player_cards(database)
            self.display_cp_cards(database)
            # self.display_community_cards(database)
        pygame.display.flip()

    def get_played_cards(self) -> list[int] | None:
        """
        Retrieves the cards played by the user by inputing identifiers of the cards in the text box. 
        Returns:
            list: A list of cards played by the user.
        """
        if self.played_cards is None:
            return None
        else:
            played_cards = self.played_cards
            self.played_cards = None
            self.played_card_text_box.set_text("")
            return played_cards

    def is_end(self) -> bool:
        """
        Checks if the game has ended.

        Returns:
            bool: True if the game has ended. False otherwise.
        """
        return False
    

if __name__ == "__main__":
    from gui import GUI

    gui = GUI()
    while True:
        if not gui.events(): break
        gui.display_stage()
    pygame.quit()
    sys.exit()
