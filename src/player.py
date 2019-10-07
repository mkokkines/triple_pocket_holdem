""" 
This file specifies the Player class.
The Player class represents both the human player and the dealer.
Each player has a name, a number of chips currently held, and a list 
of hands (i.e. pairs of pocket cards) that the player holds.
"""

class Player:
    def __init__(self, name, starting_chip_number):
        self.name = name
        self.hands = []
        self.num_chips = starting_chip_number

    def alter_chip_balance(self, payout_amount):
        """
        Changes the chip balance by payout_amount. Payout amount can be
        positive or negative -- if it is negative, the numbers of 
        chips the player holds will decrease.
        Note that the player's chip balance cannot fall below 0.

        Params:
            payout_amount: the amount by which to change the player's num_chips attribute.
        """
        self.num_chips = max(self.num_chips + payout_amount, 0)
    
    def no_chips_remaining(self):
        """
        Returns:
            Outputs true if the  player has no remaining chips and false otherwise.
        """
        return self.num_chips == 0

    def add_hand(self, cards):
        """
        Each hand is a pair of cards.
        Add a pair of cards to the list of hands held by the player.

        Params:
            cards: a pair of card objects
        """
        self.hands.append(cards)

    def clear_hands(self):
        """
        Removes all two-card hands from player.
        """
        self.hands = []

