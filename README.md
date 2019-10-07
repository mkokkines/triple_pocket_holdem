# Triple Pocket Hold’em

### Description

Triple Pocket Hold'em is a variation of Texas Hold'em designed to be played with one player and a dealer (i.e. with one player). Most people have never heard of it, but it provides a relatively fun way of becoming more familiar with the probabilities involved in poker.

Each round of the game consists of the following steps:

1. The player places a wager for the round. The dealer will match it. The player will not be able to place any further wagers after this phase.
2. The player pseudo-selects a hand.
   1. The player will be shown an initial set of two cards. The player can either pickup the cards or pass on the cards.
   2. If the player passes on the first set of cards, the cards will be given to the dealer, and the player will be shown a second set of cards. Once again, the player can either pickup the cards or pass on the cards.
   3. If the player passes on the second set of cards, the second set will be given to the dealer, and the player will be given the next two cards from the top of the deck.
   4. Note: The game is called Triple Pocket (the two-card options are called pocket cards) because the player has some choice among a three-element set of card pairs.
3. Once the player has selected his/her hand, the dealer will draw any remaining cards necessary to have two sets of two pocket cards. 
4. Five community cards will then be drawn, and the hands of the player and the dealer will be evaluated.
5. The dealer has two sets of two cards, and player must beat both of the dealer's hands in order to win the round. The player has an important advantage, though. When the player wins with certain hands, the wager is multiplied -- and this is not the case for the dealer. The multiples are as follows:
   1. Royal Flush: 50x
   2. Straight Flush: 20x
   3. Four of a Kind: 10x
   4. Full House: 4x
   5. Flush: 2x



A description can be found here: https://www.allslotscasino.com/blog/triple-pocket-holdem-poker/

### Running

Run ```pip install requirements.txt``` to install the dependencies; there is only one dependency (pygame) that does not come with a standard python distribution.

The application can be run with ```python play.py```.

I cheated a tad when it comes to building a console-based game. The game runs with python from the terminal, and the application is technically running from the terminal (i.e. you are still in the terminal application according to the MacOS), but it opens a new 600 x 800 window. I thought that a very basic user interface (just being able to see images of the cards) could provide an order of magnitude improvement in the user experience without dramatically complicating the code (see design section below).

### Design Choices and Tooling

PyGame: I chose PyGame because I thought a very simple GUI that would allow me to render images of cards would greatly enhance the user experiences without leading to bloated code, and PyGame provided this. PyGame provides straightforward functions for rendering images, rectangles, and text -- as well as collecting user mouse and keyboard input. The GUI can be found in gui.py.

Game Engine: The game engine handles the control flow of the game. It takes user input, navigates between screens, and integrates the GUI with the business logic.

Hand Evaluator: The hand evaluator provides the business logic of the application. It includes functions to get all of the possible hands for a player, determine the highest possible poker hand the player's cards fulfill, and break ties between players. I assemble the possible hands into tuples of five cards and sort the tuples in descending order of card value to make the poker logic simpler.

Card, Deck, and Player Classes: I created three simple classes: Card, Deck, and Player. Card objects includes a suite, a value, and a link to an image of the card. The Card class makes tracking and passing card data simpler. Deck objects includes a list of cards, as well as a shuffle function. On an interface level, the deck allows for cards to be popped off -- like a deck of cards. A player object stores the number of chips a player has and the cards in the player's hand. The hands property of the player allows for multiple sets of two cards to be stored, so the Player class can represent both the user and the dealer.

Testing: I used unittest. unittest is included in python distributions and works out the box, allowing me to quickly write tests to validate my logic with simple syntax.

### Testing

I developed automated tests for the poker logic included in the application. These tests cover all of the functions involved in adjudicated whether a set of five cards fulfills a poker hand (i.e. do the cards form a straight), tiebreakers between cards fulfilling the same hand (i.e. which straight would win the round), and the overarching method that computes the result of a round of Triple Pocket Hold'em.

These tests can be run with ```python -m unittest test/test_poker_engine.py```.

The automated tests covered the business logic underpinning the application. I tested the user interface manually.
