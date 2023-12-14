import pygame
import sys
import random

from data_processing.database import Card, CardDatabase
from operations import *
from GUI.gui import GUI
from user_scripts.cp_strategy import ComputerPlayer

class Controller():
    """
    The Controller class manages the game flow and player actions in the card game.
    """

    def __init__(self) -> None:
        self.running = True
        self.playing = False

        self.CP_WAIT_TIME = 60
        self.END_COUNTDOWN = 60

    def init_play(self, players: list[str]) -> None:
        """
        Initializes a new game round with the specified players.

        Args:
            players (list): A list of player names.
        """
        self.round = 0
        self.deal = False
        self.community = False
        self.play = dict()
        self.draw = dict()
        self.players = players
        for player in players:
            self.play[player] = False
            self.draw[player] = False
        self.current_player = players[0]
        
        self.playing = True

        self.cp_wait_time = self.CP_WAIT_TIME

        self.countdown = self.END_COUNTDOWN

        self.init = True
    
    def update_round(self) -> bool:
        """
        Updates the game round and checks if the round is complete.

        Returns:
            bool: True if the round is complete, False otherwise.
        """
        if self.deal and self.community and all(self.play.values()) and all(self.draw.values()):
            self.init = False
            self.round += 1
            self.deal = False
            self.community = False
            for player in self.players:
                self.play[player] = False
                self.draw[player] = False
            self.current_player = self.players[0]
            return True
        else:
            return False
        
    def init_end(self) -> None:
        """
        Initializes the end of the game.
        """
        self.countdown = self.END_COUNTDOWN
    
    def reset_cp_wait_time(self) -> None:
        """
        Resets the wait time for the computer player.
        """
        self.cp_wait_time = self.CP_WAIT_TIME

    def next_player(self) -> None:
        """
        Moves the game to the next player.
        """
        self.play[self.current_player] = True
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]

    def quit(self) -> None:
        """
        Quits the game.
        """
        self.running = False
        self.playing = False
    
    def quit_play(self):
        """
        Quits the current game round.
        """
        self.playing = False
    
    def __str__(self) -> str:
        return self.__dict__.__str__()


def main_loop():
    """
    The main loop of the program.
    """
    controller = Controller()

    gui = GUI()

    cp = ComputerPlayer()

    while controller.running:
        if not gui.events(): controller.quit()
        if gui.current_stage == 2:
            controller.config = Config(**gui.config)
            print(controller.config)
            Database = initialization(controller.config)
            print('database initialized')
            Database.add_players(['player1', 'cp'])
            controller.reset_cp_wait_time()
            controller.init_play(Database.players)
            print(Database)
        else:
            gui.display_stage()

        while controller.playing:
            #check if the game should continue or end
            if (gui.stages[2].is_end(Database) or \
                (controller.round >= controller.config.num_rounds and controller.config.num_rounds != -1))\
                and not controller.init:
                if gui.end_events():
                    gui.display_stage(Database, controller.config, game_end=True)
                    continue
                else:
                    controller.quit_play()
                    gui.current_stage = 0
            
            if not gui.events(): controller.quit()
            if gui.current_stage != 2: 
                controller.quit_play()
                break
            gui.display_stage(Database, controller.config)

            if not controller.community:
                Database = update_community(Database, controller.round, controller.config)
                controller.community = True

            if not controller.deal:
                Database = deal_cards(Database, controller.round, controller.config)
                controller.deal = True
            
            # Draw cards
            match controller.current_player:
                case 'cp':
                    if not controller.draw['cp']:
                        print("cp draw")
                        Database = draw_card(Database, controller.current_player, controller.config)
                        controller.draw['cp'] = True
                case player:
                    if (controller.config.repetitive_draw or not controller.draw[player]) and gui.stages[2].draw_flag and controller.config.draw_flag:
                        print(f"{player} draw")
                        Database = draw_card(Database, controller.current_player, controller.config)
                        controller.draw[player] = True
                        gui.stages[2].reset_draw_flag()

            # Play cards
            match controller.current_player:
                case 'cp':
                    controller.cp_wait_time -= 1
                    if random.random() > 0.2 or controller.cp_wait_time > 0:
                        continue
                    controller.reset_cp_wait_time()

                    if controller.config.play_flag:
                        # cp play cards
                        cp_played_cards = cp.cp_play_card(
                            controller.round,
                            Database.hands['cp'],
                            Database.community,
                            controller.config.num_cards_played_per_round,
                            Database.card_recently_played,
                        )
                        cp_played_cards = [card.identifier for card in cp_played_cards]
                        cp_played_cards_print = list(map(lambda x:Database.find_card(x), cp_played_cards))
                        print("cp played cards:")
                        for card in cp_played_cards_print:
                            print(card)
                        Database = play_cards('cp',cp_played_cards, Database)
                        
                    controller.next_player()
                case player:
                    # Player play cards
                    player_played_cards = gui.stages[2].get_played_cards()
                    if player_played_cards is not None:
                        # handle situation that the player played cards that are not in the hand
                        if controller.config.play_flag:
                            try: 
                                Database = play_cards(player, player_played_cards, Database)
                                controller.play[player] = True
                                print(f"{player} played cards:")
                                player_played_cards_print = list(map(lambda x:Database.find_card(x), player_played_cards))
                                for card in player_played_cards_print:
                                    print(card)
                                controller.next_player()    
                                gui.stages[gui.current_stage].clear_alert()
                            except ValueError:
                                gui.stages[gui.current_stage].display_alert("Invalid card identifiers.")
                        else:
                            if player_played_cards == []:
                                controller.next_player()

            if controller.config.sort_hands:
                for player in Database.players:
                    Database.sort_hand(player)
            
            if not Database.self_check():
                raise Exception("Database is not consistent.")
            
            controller.update_round()
            gui.stages[gui.current_stage].display_current_player(controller.current_player)


    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()