# Card-Game-Designer

**Contributors**: Jared Yao, Simin Liu

## Description

The project will implement a tool for people to build their own card games. It will offer a series of options for people to specify their own game rules. For example, they can adjust the number of rounds, how the cards are distributed, etc. After the rules are determined, they can directly play the card game they designed via the interface we provide. Our aim is to provide multiplayer support by allowing players to hide their hands. For more advanced rules, users are also encouraged to write their own rules or computer strategy with Python scripts through our API. We will also include some sample card games for demonstration purposes, like Blackjack and Texas Hold’em.

## Features

1. A **GUI** that allows users to design the card game with a mouse. It contains an interface that provides options for users to specify their game rules and an actual card table that holds the game. The GUI will contain some degree of animation to simulate the card playing process.
2. **Configuration of car decks**. Users can specify the number of  decks of cards, how one deck constitutes (whether to exclude jokers, etc), the ranks of cards, etc.
3. **Configuration of card deals**. It includes the initial hands, the number of rounds, the number of cards dealt in one round, and whether the player wants to keep drawing cards. Each card will be assigned to a unique label working as an identifier.
4. **Community cards**, which are the cards in the middle of the card table shared across all players. Users can decide whether to have community cards and how they will be updated.
5. **Configuration of cards playing**. Rules include the number of cards played in a round, number of cards in hands, a choice of not playing in a round, etc. The strategy of computers will by default be random, but users are allowed to write Python script to instruct computers with certain strategies. Players will play in order. There will be a text box on the card table for the current player to enter the identifier of the cards they intend to play. 
6. **Configuration of bidding**. Users could choose whether to include a bidding system or not. The chip sets can be presets or determined arbitrarily by users. If choosing to include a bidding system, users can decide initial property for each player, how they can stake in the game, and how the winner will take the prize.
7. **Multiplayer support**. The tool supports games with up to 4 players. For games that require confidentiality of each player’s hands, we can use an alternative method to deal the cards. The current plan is using emails to send each player their hands. For each round of card dealing and playing, there will be a new email sent representing the updated hand. To support this feature, users need to enter a host email to send hands to other players. Other players will also need to enter a separate email address to receive the hands. 
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
