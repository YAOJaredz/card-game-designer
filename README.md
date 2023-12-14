# Card-Game-Designer

**Contributors**: Jared Yao, Simin Liu

## Description

The project will implement a tool for people to build their own card games. It will offer a series of options for people to specify their own game rules. For example, they can adjust the number of rounds, how the cards are distributed, etc. After the rules are determined, they can directly play the card game they designed via the interface we provide. Our aim is to provide multiplayer support by allowing players to hide their hands. For more advanced rules, users are also encouraged to write their own rules or computer strategy with Python scripts through our API. We will also include some sample card games for demonstration purposes, like Blackjack and Texas Hold’em.

## Features

1. A **GUI** that allows users to design the card game with a mouse. It contains an interface that provides options for users to specify their game rules and an actual card table that holds the game. The GUI will contain some degree of animation to simulate the card playing process.
2. **Configuration of card decks**. Users can specify the number of  decks of cards, how one deck constitutes (whether to exclude jokers, etc), the ranks of cards, etc.
3. **Configuration of card deals**. It includes the initial hands, the number of rounds, the number of cards dealt in one round, and whether the player wants to keep drawing cards. Each card will be assigned to a unique label working as an identifier.
4. **Community cards**, which are the cards in the middle of the card table shared across all players. Users can decide whether to have community cards and how they will be updated.
5. **Configuration of cards playing**. Rules include the number of cards played in a round, number of cards in hands, a choice of not playing in a round, etc. The strategy of computers will by default be random, but users are allowed to write Python script to instruct computers with certain strategies. Players will play in order. There will be a text box on the card table for the current player to enter the identifier of the cards they intend to play. 
6. **Configuration of bidding** (_Optional_). Users could choose whether to include a bidding system or not. The chip sets can be presets or determined arbitrarily by users. If choosing to include a bidding system, users can decide initial property for each player, how they can stake in the game, and how the winner will take the prize.
7. **Multiplayer support** (_Optional_). The tool supports games with up to 4 players. For games that require confidentiality of each player’s hands, we can use an alternative method to deal the cards. The current plan is using emails to send each player their hands. For each round of card dealing and playing, there will be a new email sent representing the updated hand. To support this feature, users need to enter a host email to send hands to other players. Other players will also need to enter a separate email address to receive the hands. 
8. **Central controller system**. It will load the configurations and assign corresponding values for each module. It decides how data is updated and how each round consists of.
9. **Sample card games** using this designer, like Blackjack, Texas Hold’em.


## Users & Stakeholders

### Users: 

- Software developers
- Everyone who is interested in designing their own card games
- Wesleyan students who are looking for a fun game when planning for a party
- Educators who want to show the danger of gambling
- Everyone who wants to play card games
- Open-source platform users
  
### Stakeholders: 

- Software developers
- Everyone who is interested in designing their own card games
- Wesleyan students who are looking for a fun game when planning for a party
- Educators and their students
- Everyone who wants to play card games
- Open-source platform users
- Any people around users


## Prerequisite & Installation:

### Prerequisite:

- Have `pygame` and `pygame.gui` packages installed
  
  ```
  pip install pygame
  pip install pygame.gui
  ```

### Installation:

- Download zip for the `main` branch and unzip it

## Instructions on how to run:

- Switch the current working directory to `card-game-designer-main`
- Open `controller.py` and run it.

### Opening page manual: 

**Buttons:**

- **Create New:** Create a new game configuration. Go to *Setting* stage. 
- **Load Templates:** Load existing configurations. Go to *Game* stage. 
- **Quit:** Quit the program. 


### Setting page manual:

**Buttons:**

- **Back:** Go back to the previous stage *Opening*.
- **Save:** Save the current configuation as a json file.
- **Continue:** Go the the next stage *Game*. 

**Configuration:**

Inputs for Textbox should be only integers. Other inputs are invalid. 

- Num Rounds: Set the number of rounds of the game. -1 means infinite rounds and is the default.
- Num Decks: Set the number of decks to use. 1 as default.
- Include Joker? : Choices to include jokers or not. Yes as default.
- Order: Order of ranks in the game. There are 2 options: 0 means A has the smallest rank, 1 means 3 has the smallest rank. 0 as default.
- Num Initial Hand: Set the number of initial hand for players. 0 as default.
- Num Cards Dealt Per Round: Set the number of cards to dealt in a round. 0 as default.
- Draw Cards? : Choices to allow players to draw cards or not. Yes as default. When draw_flag is false, `Draw!` button will not appear in the *Game* page. 
- Num Cards Drawn: Set the number of cards to draw. 1 as default.
- Community Cards? : Choices to include community cards or not. Yes as default.
- First Round of Comm: The first round to have community cards. 0 as default.
- Num Comm in Its Round: Set the number of cards in community cards in the first round of having community cards. 0 as default.
- Num Comm Added Per Round: Set the number of cards to add to the community cards later. -1 means unlimited number of cards. 0 as default.
- Play Cards? : Choices to play cards or not. Yes as default. When play_flag is false, `Play!` button will be replaced by `Finish` button in the *Game* page. 
- Num Cards Played Per Round: Set the number of cards to play. 1 as default.
- Multi-User? (Not implemented yet): Choices to allow multi-user or not. No is the only option for now.
- Bidding?  (Not implemented yet): Choices to allow bidding or not. No is the only option for now.
- Repetitive Draw? : Choices to allow draw cards multiple times in a round or not. Yes as default. 
- Sort Hands? : Choices to sort cards in hand or not. Yes as default.
- Display CP? : Choices to display computer player's cards or not. Yes as default.


### Game page manual: 

User can draw cards by clicking `Draw!` button and enter identifiers on the top of cards in the textbox, click `Play!` button to play the card. 

Card dealing is automatically done by the program. 

Game starts from the user. 

Game flow: current player: deal cards `->` draw cards `->` user play cards `->` next player. 

**Textbox:** 

Identifiers should be integers and separated by `,`. 

Input with letters, other symbols, or identifiers not in hands is considered as invalid input, so cards cannot be played. 

Empty input is only allowed when `Play Cards? = No` and `Num Cards Played Per Round = 0`. 

**Buttons:**

- **Back:** Go back to the previous stage *Setting*.
- **End:** End the game. The program will go back to *Opening* stage after ending. 
- **Draw!:** Draw cards. The user can draw cards before playing.
- **Play!:** Play cards. Play cards mentioned in the textbox.
- **Finish:** Finish player action in this round. This button appears when play_flag is false. 

## Sample game:

There are 2 sample games: poker and BlackJack. 

###

## Future directions:
- Support multiplayer
- Support bidding
