"""
This file contains the game engine class that controls the flow
of the games, intakes user input, and integrates the business logic
with the GUI.
"""
import pygame, sys
from pygame.locals import *
import os

from src.gui import GUI
from src.player import Player
from src.deck import Deck
from src.hand_evaluator import determine_outcome

MENU_NOW = 'menu_clicked'
PLAY_NOW = 'play_clicked'
RULES_NOW = 'rules_clicked'
PLAY_AGAIN = 'play_again'
PLAY_ANOTHER_ROUND = 'play_another_round'

STARTING_CHIP_NUMBER = 1000
INITIAL_WAGER = 100
MIN_WAGER = 10
WAGER_INCREMENT = 10


class GameEngine:
    def __init__(self):
        self.gui = None
        self.mouse_x = 0
        self.mouse_y = 0
    
    def run_game(self):
        """
        Initializes the game, initializes the GUI, and calls the main game loop.
        """
        pygame.init()
        self.gui = GUI()
        self.gui.initialize_gui()
        self.run_main_game_loop()

    def run_main_game_loop(self):
        """
        The main game loop, based on an action variable, determines which 
        sub-loop to call.
        The action is initially set to the menu option, meaning that it will run
        the game logic for the opening menu screen.
        If the action is set to rules, it will run the logic for the rules screen (which
        specifies the rules of the game).
        If the action is set to the play option, it will run the logic for the game itself.
        """
        action = MENU_NOW
        
        while True:
            if action == MENU_NOW:
                action = self.run_menu_loop()
            elif action == PLAY_NOW:
                action = self.run_play_loop()
            elif action == RULES_NOW:
                action = self.run_rules_loop()
    
    def run_menu_loop(self):
        """
        Controls the application when the user is on the menu screen.
        Exit when the user quits the application.
        Register the position of the mouse on the screen when the user moves the mouse. 
        Change the color of buttons when the user hovers over them.
        When a user clicks the mouse, check if he/she has either clicked
        the play button or the rules button (the two menu options). If the user has,
        exit this loop and enter the play or rules loop (as appropriate).
        """
        self.gui.create_menu_screen()  

        while True: 
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == MOUSEMOTION:
                    next_mouse_x, next_mouse_y = event.pos
                    self.gui.update_menu_screen_mouse_motion(self.mouse_x, self.mouse_y, next_mouse_x, next_mouse_y)
                    self.mouse_x = next_mouse_x
                    self.mouse_y = next_mouse_y
                elif event.type == MOUSEBUTTONUP:
                    self.mouse_x, self.mouse_y = event.pos
                    if self.gui.mouse_on_play_button(self.mouse_x, self.mouse_y):
                        return PLAY_NOW
                    elif self.gui.mouse_on_rules_button(self.mouse_x, self.mouse_y):
                        return RULES_NOW

    def run_rules_loop(self):
        """
        Controls the application when the user is on the rules screen.
        Exit when the user quits the application.
        Register the position of the mouse on the screen when the user moves the mouse. 
        Change the color of buttons when the user hovers over them.
    
        Return to the menu screen when the user clicks the back button.  
        """
        self.gui.create_rules_screen()

        while True: 
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == MOUSEMOTION:
                    next_mouse_x, next_mouse_y = event.pos
                    self.gui.update_rules_screen_mouse_motion(self.mouse_x, self.mouse_y, next_mouse_x, next_mouse_y)
                    self.mouse_x = next_mouse_x
                    self.mouse_y = next_mouse_y
                elif event.type == MOUSEBUTTONUP:
                    if self.gui.mouse_on_back_button(self.mouse_x, self.mouse_y):
                        return MENU_NOW
    
    def run_play_loop(self):
        """
        Controls the application when the user is playing Triple Pocket Hold'Em.
        Start by intializing the players and the playing screen. Then enter the loop. 
        Each loop iteration carries the user through one round of the game. 
        More specifically:
        1) Initialize and shuffle a deck of cards.
        2) Prompt the user to place a wager.
        3) Present the pocket card options to the user.
        4) Determine the best poker hand held by each player and the outcome of the game.
        5) Add or deduct chips from the player and dealer accordingly
        """        
        player = Player('Player', STARTING_CHIP_NUMBER)
        dealer = Player('Dealer', STARTING_CHIP_NUMBER)
        self.gui.create_play_screen()
        self.pause(500)
        
        while True:
            deck = Deck()

            # Prompt the user to place a wager
            wager = self.get_wager(player, dealer)

            # Handle the card selection process in triple pocket holdem
            # Present the user with his/her options for cards and have him/her select the cards
            self.select_cards(deck, player, dealer)
            community_cards = deck.draw_five_community_cards()
            
            # Now, reveal the cards held by the user and the dealer, as well as the 
            # five community cards
            self.gui.explain_card_reveal()
            self.pause(2000)
            self.gui.reveal_player_cards(player, dealer)
            self.pause(2000)
            self.gui.reveal_common_cards(community_cards)
            self.pause(5000)

            # Determine the best hand held by each player and who won the round
            # Add or subtract chips from the player and dealer's totals depending on the outcome
            # Output to the user which poker hand the dealer had and what the consequent result was
            (player_hand, dealer_hand, player_wager_multiple, dealer_wager_multiple) = determine_outcome(
                player.hands[0], 
                dealer.hands[0], 
                dealer.hands[1], 
                community_cards
            )
            player.alter_chip_balance(player_wager_multiple * wager)
            dealer.alter_chip_balance(dealer_wager_multiple * wager)
            self.gui.explain_outcome(
                player_hand, 
                dealer_hand, 
                player_wager_multiple, 
                player.num_chips, 
                dealer.num_chips
            )
            self.pause(4000)
            
            # Get the next action from the user
            # If the game has ended (i.e. the user or dealer has run out of chips),
            # the user can elect to play again. Otherwise, the user can elect to continue with
            # another round in the current game or to exit
            next_action = self.get_action_at_round_end(player, dealer)
            if next_action == MENU_NOW:
                return next_action
            elif next_action == PLAY_AGAIN:
                player = Player('Player', STARTING_CHIP_NUMBER)
                dealer = Player('Dealer', STARTING_CHIP_NUMBER)
            else:
                player.clear_hands()
                dealer.clear_hands()

    
    def get_wager(self, player, dealer):
        """
        Implements the control logic that prompts the user to input an amount
        of chips to wager. Returns the wager.
        When the user clicks the plus button, increase the wager. When the user clicks the minus button,
        decrease the wager. When the  user clicks confirm, return the magnitude of their wager.
        Exit when the user quits the application.
        Register the position of the mouse on the screen when the user moves the mouse. 
        Change the color of buttons when the user hovers over them.
        """
        max_possible_wager = min(player.num_chips, dealer.num_chips)
        wager = min(INITIAL_WAGER, max_possible_wager)
        self.gui.ask_for_wager(wager, player.num_chips, dealer.num_chips)

        while True: 
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == MOUSEMOTION:
                    next_mouse_x, next_mouse_y = event.pos
                    self.gui.update_wager_screen_on_mouse_move(self.mouse_x, self.mouse_y, next_mouse_x, next_mouse_y)
                    self.mouse_x = next_mouse_x
                    self.mouse_y = next_mouse_y
                elif event.type == MOUSEBUTTONUP:
                    if self.gui.mouse_on_plus_button(self.mouse_x, self.mouse_y):
                        wager = min(wager + WAGER_INCREMENT, max_possible_wager)
                        self.gui.update_wager_amount(wager)
                    elif self.gui.mouse_on_minus_button(self.mouse_x, self.mouse_y):
                        wager = max(MIN_WAGER, wager - WAGER_INCREMENT)
                        self.gui.update_wager_amount(wager)
                    elif self.gui.mouse_on_confirm_button(self.mouse_x, self.mouse_y):
                        return wager
    
    def select_cards(self, deck, player, dealer):
        """
        Provides the game logic that presents the user with his/her (maximum) three options for pocket cards.
        Draw three sets of pocket cards. Show the first pair to the user. 
        Wait for the user to make a decision. If the user picks up the cards, assign the user the pocket cards 
        and return.
        Otherwise, present the user with the second pair of pocket cards. If the user
        does not pick up these cards, he/she is forced to accept the third pair of cards.
        """
        self.gui.show_hand_select_instructions()
        self.pause(2000)
        
        first_hand = deck.draw_two_card_hand()
        second_hand = deck.draw_two_card_hand()
        third_hand = deck.draw_two_card_hand()
        
        self.gui.show_first_hand(first_hand[0].img_path, first_hand[1].img_path)
        if self.picked_up_cards():
            player.add_hand(first_hand)
            dealer.add_hand(second_hand)
            dealer.add_hand(third_hand)
        else:
            dealer.add_hand(first_hand)
            self.gui.show_second_hand(second_hand[0].img_path, second_hand[1].img_path)

            if self.picked_up_cards():
                player.add_hand(second_hand)
                dealer.add_hand(third_hand)
            else:
                dealer.add_hand(second_hand)
                player.add_hand(third_hand)
                self.gui.alert_to_third_hand()
                self.pause(1500)
    
    def picked_up_cards(self):
        """
        Waits as the user decides whether to pick up a given pair of pocket cards.
        Return true if the user accepts the cards and false if the user rejects the cards.
        """
        while True: 
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == MOUSEMOTION:
                    next_mouse_x, next_mouse_y = event.pos
                    self.gui.update_hand_screen_on_mouse_move(self.mouse_x, self.mouse_y, next_mouse_x, next_mouse_y)
                    self.mouse_x = next_mouse_x
                    self.mouse_y = next_mouse_y
                elif event.type == MOUSEBUTTONUP:
                    if self.gui.mouse_on_accept_button(self.mouse_x, self.mouse_y):
                        return True
                    elif self.gui.mouse_on_reject_button(self.mouse_x, self.mouse_y):
                        return False                                   
    
    def get_action_at_round_end(self, player, dealer):
        """
        When a round finishes, the user is presented with the option of playing another round.
        If the user or dealer has no remaining chips, start a new game (i.e. reset the chip totals). 
        Otherwise, play another round with the current chip totals.
        
        Returns the user's decision on whether to exit or start another round. 
        """
        if dealer.no_chips_remaining():
            self.gui.show_victory(player.num_chips, dealer.num_chips)
            continue_action = PLAY_AGAIN
        elif player.no_chips_remaining():
            self.gui.show_defeat(player.num_chips, dealer.num_chips)
            continue_action = PLAY_AGAIN
        else:      
            self.gui.show_game_continuing(player.num_chips, dealer.num_chips)
            continue_action = PLAY_ANOTHER_ROUND  

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == MOUSEMOTION:
                    next_mouse_x, next_mouse_y = event.pos
                    self.gui.update_round_end_screen_mouse_move(
                        self.mouse_x, self.mouse_y, next_mouse_x, next_mouse_y
                    )
                    self.mouse_x = next_mouse_x
                    self.mouse_y = next_mouse_y
                elif event.type == MOUSEBUTTONUP:
                    if self.gui.mouse_on_play_again_button(self.mouse_x, self.mouse_y):
                        return continue_action
                    elif self.gui.mouse_on_back_button(self.mouse_x, self.mouse_y):
                        return MENU_NOW

    def pause(self, time_in_ms):
        """
        Pauses the user on a certain screen so they can read its content.
        This is preferrable to pausing the execution of the program because it
        still allows the user to quit/exit the application.
        """
        current_time = pygame.time.get_ticks()
        exit_time = current_time +  time_in_ms
        
        while current_time < exit_time:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
            current_time  = pygame.time.get_ticks()
    
    def terminate(self):
        pygame.quit()
        sys.exit()