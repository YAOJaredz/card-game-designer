import pygame
import sys

from data_processing.database import Card, CardDatabase
from operations import *
from GUI.gui import GUI
from cp_strategy import ComputerPlayer

def main_loop():
    """
    The main loop of the program.
    """
    running = True
    playing = False

    gui = GUI()

    cp = ComputerPlayer()

    while running:
        if not gui.events(): running = False
        gui.display_stage()
        if gui.current_stage == 2:
            config = Config(**gui.config)
            playing = True
            round_ = 0
            print(config)
            database = initialization(config)
            database.players = ['player1', 'cp']
            print(database)

        while playing:
            if gui.current_stage != 2: playing = False
            if not gui.events(): 
                running = False
                playing = False
            gui.display_stage()

            database = update_community(database, round_, config)

            database = deal_cards(database, round_, config)

            for player in database.players:
                database = draw_card(database, player, round_, config)
                if player == 'cp':
                    cp_played_cards = cp.cp_play_card(
                        round_,
                        database.hands[player],
                        database.community,
                        config.num_cards_played_per_round,
                        database.card_recently_played,
                    )
                    cp_played_cards = [card.identifier for card in cp_played_cards]
                    database.card_recently_played = cp_played_cards
                    print('cp:',cp_played_cards)
                    database = play_cards('cp',cp_played_cards, database, round_, config)
                else:
                    for card in database.hands[player]:
                        print(card)
                    cards = []
                    while len(cards) < config.num_cards_played_per_round:
                        ipt = input('Please enter the identifier of the card you want to play: (one at each time)')
                        if ipt == 'q': break
                        cards.append(int(ipt))
                    database.card_recently_played = cards
                    player_played_cards = gui.stages[gui.current_stage].get_played_cards()
                    database = play_cards(player, list(cards), database, round_, config)
            
            if not database.self_check():
                raise Exception("Database is not consistent.")
            
            round_ += 1

            if gui.stages[2].is_end():
                playing = False
                gui.current_stage = 0


    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_loop()