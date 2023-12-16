import pygame
import sys
import os
import random
import importlib.util
import time

sys.path.append(".")
from data_processing.database import Card, CardDatabase
from operations import *
from GUI.gui import GUI
from operations.defaults.cp_strategy import ComputerPlayer as default_ComputerPlayer


class Controller:
    """
    The Controller class manages the game flow and player actions in the card game.
    """

    def __init__(self) -> None:
        self.running = True
        self.playing = False

        self.cp_wait_time_play = 3
        self.cp_wait_time_draw = 1

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

        self.cp_wait_current_time_play = None
        self.cp_wait_current_time_draw = None

        self.init = True

    def update_round(self) -> bool:
        """
        Updates the game round and checks if the round is complete.

        Returns:
            bool: True if the round is complete, False otherwise.
        """
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

    def reset_cp_wait_time(self, *args) -> None:
        """
        Resets the wait time for the computer player.
        """
        if 1 in args:
            self.cp_wait_current_time_play = None
        if 0 in args:
            self.cp_wait_current_time_draw = None

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

    def quit_play(self) -> None:
        """
        Quits the current game round.
        """
        self.playing = False

    def __str__(self) -> str:
        return self.__dict__.__str__()

    def check_user_script(self, config: dict) -> list[str] | None:
        """
        Check if the user scripts are valid.

        Args:
            config (dict): The configuration values.

        Returns:
            bool: True if the user scripts are valid, False otherwise.
        """
        alerts = []
        if "is_end_path" in config.keys():
            if not os.path.isfile(config["is_end_path"]):
                alerts.append("is_end_path")
        if "cp_strategy_path" in config.keys():
            if not os.path.isfile(config["cp_strategy_path"]):
                alerts.append("cp_strategy_path")
        if alerts != []:
            return alerts
        else:
            return None

def main_loop():
    """
    The main loop of the program.
    """
    controller = Controller()
    gui = GUI()
    cp = default_ComputerPlayer()

    while controller.running:
        if not gui.events():
            controller.quit()

        if gui.current_stage == 2:
            # Initialize the game
            controller.config = Config(**gui.config)
            print(controller.config)
            if controller.check_user_script(gui.config) is not None:
                gui.stages[0].display_alert("Invalid path to user script(s).")
                gui.current_stage = 0
                continue
            elif "cp_strategy_path" in gui.config.keys():
                try:
                    cp_strategy = importlib.util.spec_from_file_location("cp_strategy", gui.config["cp_strategy_path"])
                    custom_CP = importlib.util.module_from_spec(cp_strategy)
                    cp_strategy.loader.exec_module(custom_CP)
                    cp = custom_CP.ComputerPlayer()
                except AttributeError:
                    gui.stages[0].display_alert("Invalid cp_strategy script.")
                    gui.current_stage = 0
                    continue

            # Initialize the database
            Database = initialization(controller.config)
            print("database initialized")
            Database.add_players(["player1", "cp"])

            controller.reset_cp_wait_time(0, 1)
            controller.init_play(Database.players)
            print(Database)
        else:
            gui.display_stage()

        while controller.playing:
            # check if the game should continue or end
            if (
                gui.stages[2].is_end(Database)
                or (controller.round >= controller.config.num_rounds
                    and controller.config.num_rounds != -1)
            ) and not controller.init:
                next_stage = gui.end_events()
                if next_stage == -1:
                    controller.quit()
                elif next_stage == 0:
                    controller.quit_play()
                    gui.update_stage(next_stage)
                else:
                    gui.display_stage(Database, controller.config, game_end=True)
                    continue
            
            # Events handling
            if not gui.events():
                controller.quit()
            if gui.current_stage != 2:
                controller.quit_play()
                break
            gui.display_stage(Database, controller.config)

            # Community cards procedure
            if not controller.community:
                Database = update_community(
                    Database, controller.round, controller.config
                )
                controller.community = True

            # Cards dealing procedure
            if not controller.deal:
                Database = deal_cards(Database, controller.round, controller.config)
                controller.deal = True

            # Cards drawing procedure
            match controller.current_player:
                case "cp" if controller.config.draw_flag:
                    if not controller.draw["cp"]:
                        if controller.cp_wait_current_time_draw is None:
                            controller.cp_wait_current_time_draw = time.time()
                            continue
                        elif time.time() - controller.cp_wait_current_time_draw < controller.cp_wait_time_draw:
                            continue
                        controller.reset_cp_wait_time(0)
                        if controller.config.repetitive_draw:
                            # If repetitive draw is allowed, the computer player will draw cards until it cannot draw anymore.
                            while cp.cp_draw_card_repetitive(
                                controller.round,
                                Database.hands["cp"],
                                Database.community,
                                controller.config.num_draw,
                            ):
                                Database = draw_card(Database, controller.current_player, controller.config)
                            print("cp draw")
                        else:
                            # If repetitive draw is not allowed, the computer player will draw cards based on strategy.
                            cp_draw_times = cp.cp_draw_card(
                                controller.round,
                                Database.hands["cp"],
                                Database.community,
                                controller.config.num_draw,
                            )
                            for _ in range(cp_draw_times):
                                Database = draw_card(Database, controller.current_player, controller.config)
                            print("cp draw")
                        controller.draw["cp"] = True

                case player if controller.config.draw_flag:
                    if (
                        controller.config.repetitive_draw or not controller.draw[player]
                    ) and gui.stages[2].draw_flag:
                        print(f"{player} draw")
                        Database = draw_card(Database, controller.current_player, controller.config)
                        controller.draw[player] = True
                        gui.stages[2].reset_draw_flag()

            # Cards playing procedure
            match controller.current_player:
                case "cp":
                    if controller.config.play_flag:
                        if controller.cp_wait_current_time_play is None:
                            controller.cp_wait_current_time_play = time.time()
                            continue
                        elif time.time() - controller.cp_wait_current_time_play < controller.cp_wait_time_play or random.random() > 0.3:
                            continue
                        controller.reset_cp_wait_time(1)

                        # cp play cards based on strategy
                        cp_played_cards = cp.cp_play_card(
                            controller.round,
                            Database.hands["cp"],
                            Database.community,
                            controller.config.num_cards_played_per_round,
                            Database.card_recently_played,
                        )

                        cp_played_cards = [card.identifier for card in cp_played_cards]
                        cp_played_cards_print = list(
                            map(lambda x: Database.find_card(x), cp_played_cards)
                        )
                        print("cp played cards:")

                        for card in cp_played_cards_print:
                            print(card)
                        Database = play_cards("cp", cp_played_cards, Database)

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
                                player_played_cards_print = list(
                                    map(lambda x: Database.find_card(x),player_played_cards)
                                )
                                for card in player_played_cards_print:
                                    print(card)
                                controller.next_player()
                                gui.stages[gui.current_stage].clear_alert()
                            except ValueError:
                                gui.stages[gui.current_stage].display_alert("Invalid card identifiers.")
                        else:
                            if player_played_cards == []:
                                controller.next_player()

            # Sort hands in ascending order if configured
            if controller.config.sort_hands:
                for player in Database.players:
                    Database.sort_hand(player)

            # Check if the database is consistent.
            if not Database.self_check():
                print(Database.snapshots[-2] - Database.snapshots[-1])
                print("!!!Database is not consistent.")
                print(Database)
            
            # check if deck is empty
            if Database.deck == set():
                controller.config.draw_flag = False
                controller.config.deal_flag = False
                #display alert
                gui.stages[2].display_alert("Deck is empty.\nDealing and drawing are disabled.")

            controller.update_round()
            controller.init = False
            gui.stages[gui.current_stage].display_current_player(controller.current_player)
            
            
                

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main_loop()
