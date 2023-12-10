import pygame
import sys
import json
import tkinter as tk
from tkinter import filedialog

tk.Tk().withdraw()

sys.path.append(".")
from GUI.components import *
from data_processing.database import Card, CardDatabase
from operations.config import Config
WIDTH, HEIGHT = 1000, 700


class Openning:
    """
    Display the GUI for the game at the initial state. (Stage 0)
    It will display 3 buttons: create new templates, load templates, quit.
    Create new templates: users can create new templates for the game.
    Load templates: users can load the templates they have created before.

    Attributes:
        width (int): The width of the screen.
        height (int): The height of the screen.
        screen (pygame.Surface): The surface representing the game screen.
        all_sprites (pygame.sprite.Group): The group containing all the sprites in the game.
        open_label (Label): The label displaying the title of the game.
        quit_button (Button): The button for quitting the game.
        new_button (Button): The button for creating new templates.
        load_button (Button): The button for loading templates.
        loaded_config (dict): The loaded configuration.

    Methods:
        __init__(): Initializes the Openning object.
        handle_events(event: pygame.event.Event) -> int: Handles the events generated by user interactions.
        get_config() -> dict: Returns the loaded configuration.
        update(): Updates the display of the GUI.
    """
    def __init__(self):
        """
        Initializes the Openning object.
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

    def handle_events(self, event: pygame.event.Event) -> int:
        """
        Handles the events generated by user interactions.

        Args:
            event (pygame.event.Event): The event generated by user interaction.

        Returns:
            int: The value indicating the action to be taken based on the event.
                -1: Quit button clicked.
                 1: New button clicked.
                 2: Load button clicked and a valid file selected.
                 0: No action required.
        """
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
    
    def get_config(self) -> Config:
        """
        Returns the loaded configuration.

        Returns:
            Config: The loaded configuration.
        """
        return self.loaded_config

    def update(self) -> None:
        """
        Update the display of the GUI.
        """
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen, pygame.mouse.get_pos())
        pygame.display.flip()


class Setting:
    """
    Take the user input and set up the game configuration.
    At the page of starting a new game, users have the option to save this configuration and start playing.

    Attributes:
        width (int): The width of the game screen.
        height (int): The height of the game screen.
        new_config (dict): The dictionary containing the new game configuration.
        screen (pygame.Surface): The game screen surface.
        ui (pygame_gui.UIManager): The UI manager for the game.
        ui_config (dict): The UI configuration dictionary.
        dropdown (dict): The dictionary containing the dropdown UI elements.
        textbox (dict): The dictionary containing the textbox UI elements.
        labels (dict): The dictionary containing the label UI elements.
        all_sprites (pygame.sprite.Group): The sprite group containing all the UI elements.
        setting_title (Label): The title label for the setting page.
        back_button (Button): The back button UI element.
        continue_button (Button): The continue button UI element.
        save_button (Button): The save button UI element.
    """

    def __init__(self) -> None:
            """
            Initializes the Stage class.
            """
            self.width, self.height = WIDTH, HEIGHT
            try:
                self.new_config = json.load(open("save/empty_config.json", "r"))
            except FileNotFoundError:
                self.new_config = dict()

            self.screen = pygame.display.set_mode((self.width, self.height))
            self.ui = pygame_gui.UIManager((self.width, self.height), "GUI/themes.json")

            ui_config = json.load(open("GUI/setting_config.json", "r"))
            self.ui_config = self.convert_config_grid(ui_config)

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

    def convert_config_grid(self, ui_config: set) -> set:
        """
        Convert the configuration grid coordinates in the UI configuration dictionary
        from their original string representation to their corresponding integer values.

        Args:
            ui_config (set): The UI configuration dictionary containing the grid coordinates.

        Returns:
            set: The updated UI configuration dictionary with converted grid coordinates.
        """
        for i in ui_config["DropDown"].keys():
            ui_config["DropDown"][i][0] = ui_config['Grid']['col'][str(ui_config["DropDown"][i][0])]
            ui_config["DropDown"][i][1] = ui_config['Grid']['row'][str(ui_config["DropDown"][i][1])]
        for i in ui_config["TextBox"].keys():
            ui_config['TextBox'][i][0][0] = ui_config['Grid']['col'][str(ui_config["TextBox"][i][0][0])]
            ui_config['TextBox'][i][0][1] = ui_config['Grid']['row'][str(ui_config["TextBox"][i][0][1])]
        for i in ui_config["Labels"].keys():
            ui_config['Labels'][i][0] = ui_config['Grid']['label_col'][str(ui_config["Labels"][i][0])] + ui_config['Labels'][i][5]
            ui_config['Labels'][i][1] = ui_config['Grid']['label_row'][str(ui_config["Labels"][i][1])]
            ui_config['Labels'][i].remove(ui_config['Labels'][i][5])
        return ui_config


    def handle_events(self, event: pygame.event.Event) -> int:
        """
        Handles the events for Setting stage.

        Args:
            event (pygame.event.Event): The event generated by the user.

        Returns:
            int: The value to be returned based on the event handling.
                 - 0: If the back button is clicked.
                 - 1: If any other event occurs.
                 - 2: If the continue button is clicked.
        """
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
    
    def get_config(self) -> Config:
        """
        Retrieves the configuration settings from the setting page.

        Returns:
            Config: A dictionary-like object containing the configuration settings.
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
        """
        Updates the display of the Setting stage.
        """
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen, pygame.mouse.get_pos())

        self.ui.update(6e-2)
        self.ui.draw_ui(self.screen)
        pygame.display.flip()


class Game:
    """
    Represents a card game.

    Attributes:
        width (int): The width of the game screen.
        height (int): The height of the game screen.
        screen (pygame.Surface): The game screen.
        all_sprites (pygame.sprite.Group): A group of all sprites in the game.
        back_button (Button): The back button sprite.
        ui (pygame_gui.UIManager): The user interface manager.
        bg (pygame.Surface): The background image of the game.
        cp_image (pygame.Surface): The image of the computer player.
        played_card_text_box (TextBox): The text box for playing cards.
        played_card_text_box_label (pygame.Surface): The label for the played card text box.
        played_cards (list[int] | None): The cards played for this round.
        play_button (Button): The play button sprite.
        deck_image (pygame.Surface): The image of the card deck.
    """

    def __init__(self) -> None:
        """
        Initializes the Game class.
        """
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.all_sprites = pygame.sprite.Group()
        self.back_button = Button(10, 10, 80, 40, "Back")
        self.all_sprites.add(self.back_button)
        self.ui = pygame_gui.UIManager((self.width, self.height), "GUI/themes.json")

        # display the card table
        self.bg = pygame.transform.smoothscale(pygame.image.load('card_images/bg.jpg'), (self.width, self.height))

        # display the computer player
        self.cp_image = pygame.transform.smoothscale(pygame.image.load('card_images/cp.png'), (100, 120))

        # text box for playing cards
        self.played_card_text_box = TextBox(280, 450, 300, 40, ui_manager=self.ui, uid="played_card_text_box")

        # text box label
        self.played_card_text_box_label = pygame.font.Font(None, 24).render(str("Please enter identifiers (separated by , ) "), True, (255, 255, 255))

        # alert label
        self.alert_label = Label(380, 395, "", 24, color=(255,69,69))

        # record played card for this round
        self.played_cards = None

        # add play card button
        self.play_button = Button(600, 450, 70, 35, "Play!")
        self.all_sprites.add(self.play_button, self.alert_label)

        # add card deck
        self.deck_image = pygame.transform.smoothscale(pygame.image.load('card_images/deck.png'), (150, 100))

    def handle_events(self, event: pygame.event.Event) -> int:
        """
        Handles the events in the game.

        Args:
            event (pygame.event.Event): The event to be handled.

        Returns:
            int: represent the next stage of the game.
        """
        self.ui.process_events(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.back_button.rect.collidepoint(event.pos):
                print("Back Clicked!")
                return 1
            elif self.play_button.rect.collidepoint(event.pos):
                print("Play Card Clicked!")
                played_cards = self.played_card_text_box.get_text()
                try:
                    played_cards_str = self.check_input(played_cards, self.config)
                    self.played_cards = [int(card) for card in played_cards_str]
                except ValueError:
                    self.display_alert(f"{' '*8}Invalid input !")
                    print(f"Invalid input!")
                except ImcompatibleConfigError:
                    self.display_alert("Too many cards played !")
                    print("Too many cards played!")
        return 2
    
    def display_player_cards(self, database: CardDatabase, player: str = "player1") -> None:
        """ 
        Display the cards in player's hand.

        Args:
            database (CardDatabase): The card database.
                                    Get the cards in hand. 
        """
        cards=database.hands[player]
        num_cards=len(cards)
        display_range_width=(num_cards-1)*40+100
        start_x=(self.width-display_range_width)/2
        for card in cards:
            # display card image
            image=pygame.transform.smoothscale(pygame.image.load(card.image), (100, 150))
            self.screen.blit(image, (start_x, 520))
            # display card identifier
            identifier=pygame.font.Font(None, 24).render(str(card.identifier), True, (255, 255, 255))
            self.screen.blit(identifier, (start_x+10, 500))
            start_x+=40  
              
            
    def display_cp_cards(self, database: CardDatabase) -> None:
        """ 
        Display the cards in cp's hand.

        Args:
            database (CardDatabase): The card database.
                                    Get the cards in hand. 
        """
        cards=database.hands["cp"]
        num_cards=len(cards)
        display_range_width=(num_cards-1)*20+60
        start_x=(self.width-display_range_width)/2
        image=pygame.transform.smoothscale(pygame.image.load("card_images/back.png"), (60, 100))
        for card in cards:
            # display card backs
            self.screen.blit(image, (start_x, 30))
            start_x+=20    
            
    def display_community_cards(self, database: CardDatabase) -> None:
        """ 
        Display the cards in community.

        Args:
            database (CardDatabase): The card database.
                                    Get the cards in community. 
        """
        cards=database.community
        num_cards=len(cards)
        display_range_width=num_cards*90
        start_x=(self.width-display_range_width)/2
        community_label=pygame.font.Font(None, 24).render(str("Community Cards:"), True, (255, 255, 255))
        self.screen.blit(community_label, (420, 240))
        for card in cards:
            # display card image
            image=pygame.transform.smoothscale(pygame.image.load(card.image), (60, 90))
            self.screen.blit(image, (start_x, 270))
            start_x+=90
             
    def display_recently_played_cards(self, database: CardDatabase) -> None:
        """ 
        Display the recently played cards.

        Args:
            database (CardDatabase): The card database.
                                    Get the recently played cards.
        """
        cards=database.card_recently_played['played_cards']
        player=database.card_recently_played['player']
        num_cards=len(cards)
        display_range_height=num_cards*100
        start_y=(self.height-display_range_height)/2
        played_card_label=pygame.font.Font(None, 24).render(player+str(" played:"), True, (255, 255, 255))
        self.screen.blit(played_card_label, (850, start_y-20))
        for card in cards:
            # display card image
            image=pygame.transform.scale(pygame.image.load(card.image), (80, 100))
            self.screen.blit(image, (880, start_y))
            start_y+=100
        return None
    
    def check_input(self, input: str, config: Config) -> list[str]:
            """
            Checks the validity of the played cards and converts it into a list of integers.

            Args:
                input (str): The input string to be checked.
                config (Config): The configuration object containing game settings.

            Returns:
                list: A list of integers representing the valid input.

            Raises:
                ValueError: If the input string is empty or contains non-numeric characters.
                ImcompatibleConfigError: If the number of cards played per round exceeds the configured limit.
            """
            input = input.replace(" ", "")
            inputs = input.split(",")
            if len(inputs) == 0:
                raise ValueError
            for i in inputs:
                if not i.isnumeric() or len(i) == 0:
                    raise ValueError
            if len(inputs) > int(config['num_cards_played_per_round']):
                raise ImcompatibleConfigError
            return inputs
    
    def display_alert(self, alert: str) -> None:
        self.alert_label.text = alert

    def clear_alert(self) -> None:
        self.alert_label.text = ""

            
    def update(self, database: CardDatabase) -> None: 
        """
        Updates the game display.

        Args:
            database (CardDatabase): The card database.
        """
        self.screen.blit(self.bg, (0, 0))
        self.all_sprites.draw(self.screen)
        self.all_sprites.update(self.screen, pygame.mouse.get_pos())
        self.screen.blit(self.cp_image, (100, 20))
        self.screen.blit(self.deck_image, (30, 350))
        self.screen.blit(self.played_card_text_box_label, (310, 425))
        self.ui.update(6e-2)
        self.ui.draw_ui(self.screen)

        # if users have cards in hand, display them
        if len(database.hands.keys()) != 0:
            self.display_player_cards(database)
            self.display_cp_cards(database)
        #display community cards
        if len(database.community) != 0:
            self.display_community_cards(database)
        if len(database.card_recently_played) != 0:
            self.display_recently_played_cards(database)
        pygame.display.flip()

    def get_played_cards(self) -> list[int] | None:
        """
        Retrieves the cards played by the user by inputing identifiers of the cards in the text box. 

        Returns:
            list: A list of cards played by the user. None if no cards have been played.
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
    from controller import main_loop
    main_loop()
