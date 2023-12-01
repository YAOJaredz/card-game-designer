import pygame
import sys

from data_processing.database import Card, CardDatabase
from operations import *
from GUI.gui import GUI
from cp_strategy import ComputerPlayer

class Controller():
    def __init__(self) -> None:
        self.running = True
        self.playing = False

    def init_play(self, players):
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
    
    def update_round(self) -> bool:
        if self.deal and self.community and all(self.play.values()):
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
    
    def next_player(self):
        self.current_player = self.players[(self.players.index(self.current_player) + 1) % len(self.players)]

    def quit(self):
        self.running = False
        self.playing = False
    
    def quit_play(self):
        self.playing = False


def main_loop():
    """
    The main loop of the program.
    """
    controller = Controller()

    gui = GUI()

    cp = ComputerPlayer()

    while controller.running:
        if not gui.events(): controller.quit()
        gui.display_stage()
        if gui.current_stage == 2:
            config = Config(**gui.config)
            print(config)
            database = initialization(config)
            print('database initialized')
            database.players = ['player1', 'cp']
            controller.init_play(database.players)
            print(database)

        while controller.playing:
            if not gui.events(): controller.quit()
            if gui.current_stage != 2: 
                controller.quit_play()
                break
            gui.display_stage()

            if not controller.community:
                database = update_community(database, controller.round, config)
                controller.community = True

            if not controller.deal:
                database = deal_cards(database, controller.round, config)
                controller.deal = True

            if not controller.draw[controller.current_player]:
                database = draw_card(database, controller.current_player, controller.round, config)
                controller.draw[controller.current_player] = True

                print(controller.current_player,':')
                for card in database.hands[controller.current_player]:
                    print(card.identifier)

            match controller.current_player:
                case 'cp':
                    cp_played_cards = cp.cp_play_card(
                        controller.round,
                        database.hands['cp'],
                        database.community,
                        config.num_cards_played_per_round,
                        database.card_recently_played,
                    )
                    cp_played_cards = [card.identifier for card in cp_played_cards]
                    controller.play['cp'] = True
                    print('cp:',cp_played_cards)
                    database = play_cards('cp',cp_played_cards, database, controller.round, config)
                case player:
                    player_played_cards = gui.stages[gui.current_stage].get_played_cards()
                    if player_played_cards is not None:
                        controller.play[player] = True
                        print(player,':',player_played_cards)
                        database = play_cards(player, player_played_cards, database, controller.round, config)
                        controller.next_player()

            
            if not database.self_check():
                raise Exception("Database is not consistent.")
            
            controller.update_round()

            if gui.stages[2].is_end():
                controller.quit_play()
                gui.current_stage = 0


    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()