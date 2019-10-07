"""
This file specifies the deck class. 
Each deck object represents a deck of standard playing cards,
consisting of 52 card objects.
The deck class has methods to draw cards and shuffle the  deck.
"""

import random

from src.card import Card

# Note: the values 11-14 represent the Jack, Queen, King, and Ace respectively.
# Representing their values with numbers simplifies the logic for  determining
# which hands a player holds.
card_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suites = ['diamonds', 'hearts', 'spades', 'clubs']

class Deck:
    def __init__(self):
        self.cards = []
        self.create()
        self.shuffle()
    
    def create(self):
        for suite in suites:
            for value in card_values:
                self.cards.append(Card(suite, value))
        
    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def draw_two_card_hand(self):
        """
        Since the players are presented with two-card hands (the pocket cards),
        this method pops two card off the deck and returns them.

        Returns:
            A pair of card objects popped off the deck.
        """
        first_card = self.cards.pop()
        second_card = self.cards.pop()
        return (first_card, second_card)

    def draw_five_community_cards(self):
        """
        Since there are five community cards in Hold'Em,
        this methods pops five cards off the deck and returns
        them.

        Returns:
            A quintuple of card objects that were popped off the deck.
        """
        first_card = self.cards.pop()
        second_card = self.cards.pop()
        third_card = self.cards.pop()
        fourth_card = self.cards.pop()
        fifth_card = self.cards.pop()
        return (first_card, second_card, third_card, fourth_card, fifth_card)
