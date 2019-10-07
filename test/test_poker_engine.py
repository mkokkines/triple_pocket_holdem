import unittest
import src.hand_evaluator as poker
from src.card import Card

class PokerEngineTest(unittest.TestCase):
    def testIsRoyalFlush(self):
        card_one = Card('diamonds', 14)
        card_two = Card('diamonds', 13)
        card_three = Card('diamonds', 12)
        card_four = Card('diamonds', 11)
        card_five = Card('diamonds', 10)
        card_six = Card('diamonds', 9)
        card_seven = Card('spades', 11)
        
        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two = (card_one, card_two, card_three, card_four, card_six)
        hand_three = (card_one, card_two, card_three, card_seven, card_five)

        self.assertTrue(poker.is_royal_flush(hand_one))
        self.assertFalse(poker.is_royal_flush(hand_two))
        self.assertFalse(poker.is_royal_flush(hand_three))

    def test_is_straight_flush(self):
        card_one = Card('diamonds', 7)
        card_two = Card('diamonds', 6)
        card_three = Card('diamonds', 5)
        card_four = Card('diamonds', 4)
        card_five = Card('diamonds', 3)
        card_six = Card('diamonds', 2)
        card_seven = Card('spades', 3)
        
        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two = (card_one, card_two, card_three, card_four, card_six)
        hand_three = (card_one, card_two, card_three, card_four, card_seven)

        self.assertTrue(poker.is_straight_flush(hand_one))
        self.assertFalse(poker.is_straight_flush(hand_two))
        self.assertFalse(poker.is_straight_flush(hand_three))
    
    def test_is_four_of_a_kind(self):
        card_one = Card('diamonds', 12)
        card_two = Card('spades', 10)
        card_three = Card('hearts', 10)
        card_four = Card('spades', 10)
        card_five = Card('diamonds', 10)
        card_six = Card('spades', 12)
        card_seven = Card('spades', 9)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two = (card_one, card_two, card_three, card_four, card_six)
        hand_three = (card_one, card_two, card_three, card_four, card_seven)

        self.assertTrue(poker.is_four_of_a_kind(hand_one))
        self.assertFalse(poker.is_four_of_a_kind(hand_two))
        self.assertFalse(poker.is_four_of_a_kind(hand_three))

    def test_is_full_house(self):
        card_one = Card('diamonds', 12)
        card_two = Card('spades', 12)
        card_three = Card('spades', 10)
        card_four = Card('hearts', 10)
        card_five = Card('clubs', 10)
        card_six = Card('diamonds', 10)
        card_seven = Card('spades', 9)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two = (card_one, card_two, card_three, card_four, card_six)
        hand_three = (card_one, card_two, card_three, card_four, card_seven)

        self.assertTrue(poker.is_full_house(hand_one))
        self.assertTrue(poker.is_full_house(hand_two))
        self.assertFalse(poker.is_full_house(hand_three))

    def test_is_flush(self):
        card_one = Card('diamonds', 7)
        card_two = Card('diamonds', 6)
        card_three = Card('diamonds', 5)
        card_four = Card('diamonds', 4)
        card_five = Card('hearts', 3)
        card_six = Card('spades', 3)
        card_seven = Card('diamonds', 2)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two = (card_one, card_two, card_three, card_four, card_six)
        hand_three = (card_one, card_two, card_three, card_four, card_seven)

        self.assertFalse(poker.is_flush(hand_one))
        self.assertFalse(poker.is_flush(hand_two))
        self.assertTrue(poker.is_flush(hand_three))

    def test_is_straight(self):
        card_one = Card('diamonds', 7)
        card_two = Card('spades', 6)
        card_three = Card('clubs', 5)
        card_four = Card('hearts', 4)
        card_five = Card('diamonds', 3)
        card_six = Card('hearts', 3)
        card_seven = Card('diamonds', 2)
        
        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two = (card_one, card_two, card_three, card_four, card_six)
        hand_three = (card_one, card_two, card_three, card_four, card_seven)

        self.assertTrue(poker.is_straight(hand_one))
        self.assertTrue(poker.is_straight(hand_two))
        self.assertFalse(poker.is_straight(hand_three))

    def test_is_three_of_a_kind(self):
        card_one = Card('diamonds', 13)
        card_two = Card('spades', 12)
        card_three = Card('clubs', 11)
        card_four = Card('hearts', 11)
        card_five = Card('diamonds', 11)
        card_six = Card('hearts', 10)
        card_seven = Card('diamonds', 10)
        
        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two = (card_one, card_two, card_three, card_four, card_six)
        hand_three = (card_one, card_two, card_three, card_four, card_seven)

        self.assertTrue(poker.is_three_of_a_kind(hand_one))
        self.assertFalse(poker.is_three_of_a_kind(hand_two))
        self.assertFalse(poker.is_three_of_a_kind(hand_three))

    def test_is_two_pair(self):
        card_one = Card('diamonds', 13)
        card_two = Card('spades', 13)
        card_three = Card('clubs', 12)
        card_four = Card('hearts', 11)
        card_five = Card('diamonds', 11)
        card_six = Card('hearts', 10)
        card_seven = Card('diamonds', 10)
        
        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two = (card_one, card_two, card_three, card_four, card_six)
        hand_three = (card_one, card_two, card_three, card_four, card_seven)

        self.assertTrue(poker.is_two_pair(hand_one))
        self.assertFalse(poker.is_two_pair(hand_two))
        self.assertFalse(poker.is_two_pair(hand_three))
    
    def test_is_pair(self):
        card_one = Card('diamonds', 13)
        card_two = Card('spades', 12)
        card_three = Card('clubs', 11)
        card_four = Card('hearts', 10)
        card_five = Card('diamonds', 10)
        card_six = Card('hearts', 10)
        card_seven = Card('diamonds', 9)
        
        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two = (card_one, card_two, card_three, card_four, card_six)
        hand_three = (card_one, card_two, card_three, card_four, card_seven)

        self.assertTrue(poker.is_pair(hand_one))
        self.assertTrue(poker.is_pair(hand_two))
        self.assertFalse(poker.is_pair(hand_three))

    def test_break_tie_straight(self):
        card_one = Card('spades', 12)   
        card_two = Card('spades', 11)      
        card_three = Card('spades', 10)      
        card_four = Card('spades', 9)      
        card_five = Card('spades', 8)    

        card_six = Card('spades', 11)
        card_seven = Card('spades', 10)      
        card_eight = Card('spades', 9)      
        card_nine = Card('spades', 8)            
        card_ten = Card('spades', 7)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two =  (card_six, card_seven, card_eight, card_nine, card_ten)
        
        self.assertEqual(poker.break_tie_straight(hand_one, hand_two), 1)

    def test_break_tie_four_of_a_kind(self):
        card_one = Card('spades', 12)   
        card_two = Card('hearts', 12)      
        card_three = Card('diamonds', 12)      
        card_four = Card('clubs', 12)      
        card_five = Card('spades', 8)    

        card_six = Card('spades', 12)
        card_seven = Card('hearts', 12)      
        card_eight = Card('diamonds', 12)      
        card_nine = Card('clubs', 12)            
        card_ten = Card('spades', 9)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two =  (card_six, card_seven, card_eight, card_nine, card_ten)
        
        self.assertEqual(poker.break_tie_four_of_a_kind(hand_one, hand_two), 2)

    def test_break_tie_full_house(self):
        card_one = Card('spades', 12)   
        card_two = Card('hearts', 12)      
        card_three = Card('diamonds', 4)      
        card_four = Card('clubs', 4)      
        card_five = Card('spades', 4)    

        card_six = Card('spades', 9)
        card_seven = Card('hearts', 9)      
        card_eight = Card('diamonds', 9)      
        card_nine = Card('clubs', 2)            
        card_ten = Card('spades', 2)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two =  (card_six, card_seven, card_eight, card_nine, card_ten)
        
        self.assertEqual(poker.break_tie_full_house(hand_one, hand_two), 2)

    def test_break_tie_flush(self):
        card_one = Card('spades', 14)   
        card_two = Card('spades', 5)      
        card_three = Card('spades', 4)      
        card_four = Card('spades', 3)      
        card_five = Card('spades', 2)    

        card_six = Card('spades', 9)
        card_seven = Card('spades', 8)      
        card_eight = Card('spades', 7)      
        card_nine = Card('spades', 5)            
        card_ten = Card('spades', 4)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two =  (card_six, card_seven, card_eight, card_nine, card_ten)
        
        self.assertEqual(poker.break_tie_flush(hand_one, hand_two), 1)

    def test_break_tie_three_of_a_kind(self):
        card_one = Card('spades', 12)   
        card_two = Card('hearts', 12)      
        card_three = Card('diamonds', 12)      
        card_four = Card('clubs', 9)      
        card_five = Card('spades', 8)    

        card_six = Card('spades', 11)
        card_seven = Card('hearts', 11)      
        card_eight = Card('diamonds', 11)      
        card_nine = Card('clubs', 10)            
        card_ten = Card('spades', 9)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two =  (card_six, card_seven, card_eight, card_nine, card_ten)        
        self.assertEqual(poker.break_tie_three_of_a_kind(hand_one, hand_two), 1)

    def test_break_tie_two_pairs(self):
        card_one = Card('spades', 12)   
        card_two = Card('hearts', 12)      
        card_three = Card('diamonds', 4)      
        card_four = Card('clubs', 4)      
        card_five = Card('spades', 3)    

        card_six = Card('spades', 12)
        card_seven = Card('hearts', 12)      
        card_eight = Card('diamonds', 11)      
        card_nine = Card('clubs', 11)            
        card_ten = Card('spades', 2)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two =  (card_six, card_seven, card_eight, card_nine, card_ten)        
        self.assertEqual(poker.break_tie_two_pairs(hand_one, hand_two), 2)

    def test_break_tie_one_pair(self):
        card_one = Card('spades', 12)   
        card_two = Card('hearts', 11)      
        card_three = Card('diamonds', 4)      
        card_four = Card('clubs', 4)      
        card_five = Card('spades', 3)    

        card_six = Card('spades', 12)
        card_seven = Card('hearts', 12)      
        card_eight = Card('diamonds', 11)      
        card_nine = Card('clubs', 10)            
        card_ten = Card('spades', 2)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two =  (card_six, card_seven, card_eight, card_nine, card_ten)        
        self.assertEqual(poker.break_tie_one_pair(hand_one, hand_two), 2)

    def test_break_tie_high_card(self):
        card_one = Card('diamonds', 14)   
        card_two = Card('spades', 8)      
        card_three = Card('hearts', 4)      
        card_four = Card('spades', 3)      
        card_five = Card('clubs', 2)    

        card_six = Card('spades', 9)
        card_seven = Card('clubs', 8)      
        card_eight = Card('spades', 6)      
        card_nine = Card('hearts', 5)            
        card_ten = Card('hearts', 4)

        hand_one = (card_one, card_two, card_three, card_four, card_five)
        hand_two =  (card_six, card_seven, card_eight, card_nine, card_ten)
        
        self.assertEqual(poker.break_tie_high_card(hand_one, hand_two), 1)

    def test_get_wager_multiples(self):
        self.assertEqual(poker.get_wager_multiples(1, 10), (50, -50))
        self.assertEqual(poker.get_wager_multiples(1, 9), (20, -20))
        self.assertEqual(poker.get_wager_multiples(1, 8), (10, -10))
        self.assertEqual(poker.get_wager_multiples(1, 7), (4, -4))
        self.assertEqual(poker.get_wager_multiples(1, 6), (2, -2))
        self.assertEqual(poker.get_wager_multiples(1, 5), (1, -1))
        self.assertEqual(poker.get_wager_multiples(1, 2), (1, -1))
        self.assertEqual(poker.get_wager_multiples(2, 5), (-1, 1))
        self.assertEqual(poker.get_wager_multiples(2, 9), (-1, 1))
        self.assertEqual(poker.get_wager_multiples(0, 9), (0, 0))
    
    def test_determine_outcome_one(self):
        card_one = Card('diamonds', 14)   
        card_two = Card('spades', 8)      
        card_three = Card('hearts', 4)      
        card_four = Card('spades', 3)      
        card_five = Card('clubs', 2)    
        card_six = Card('clubs', 8)      
        card_seven = Card('spades', 6)      
        card_eight = Card('hearts', 5)            
        card_nine = Card('hearts', 4)
        card_ten = Card('spades', 9)
        card_eleven = Card('spades', 2)

        player_hand = (card_one, card_two)
        dealer_hand_one = (card_three, card_four)
        dealer_hand_two = (card_five, card_six)
        community_cards = (card_seven, card_eight, card_nine, card_ten, card_eleven)

        test_outcome = poker.determine_outcome(player_hand, dealer_hand_one, dealer_hand_two, community_cards)
        correct_outcome = ('high card', 'straight', -1, 1)
        self.assertEqual(test_outcome, correct_outcome)

    def test_determine_outcome_two(self):
        card_one = Card('diamonds', 14)   
        card_two = Card('spades', 6)      
        card_three = Card('hearts', 4)      
        card_four = Card('spades', 3)      
        card_five = Card('clubs', 2)    
        card_six = Card('clubs', 8)      
        card_seven = Card('hearts', 6)      
        card_eight = Card('spades', 5)            
        card_nine = Card('spades', 4)
        card_ten = Card('spades', 3)
        card_eleven = Card('spades', 2)

        player_hand = (card_one, card_two)
        dealer_hand_one = (card_three, card_four)
        dealer_hand_two = (card_five, card_six)
        community_cards = (card_seven, card_eight, card_nine, card_ten, card_eleven)
    
        test_outcome = poker.determine_outcome(player_hand, dealer_hand_one, dealer_hand_two, community_cards)
        correct_outcome = ('straight flush', 'flush', 20, -20)
        self.assertEqual(test_outcome, correct_outcome)

    def test_determine_outcome_three(self):
        card_one = Card('diamonds', 14)   
        card_two = Card('spades', 14)      
        card_three = Card('hearts', 4)      
        card_four = Card('spades', 14)      
        card_five = Card('clubs', 2)    
        card_six = Card('clubs', 8)      
        card_seven = Card('spades', 13)      
        card_eight = Card('spades', 12)            
        card_nine = Card('spades', 11)
        card_ten = Card('spades', 10)
        card_eleven = Card('spades', 2)

        player_hand = (card_one, card_two)
        dealer_hand_one = (card_three, card_four)
        dealer_hand_two = (card_five, card_six)
        community_cards = (card_seven, card_eight, card_nine, card_ten, card_eleven)
    
        test_outcome = poker.determine_outcome(player_hand, dealer_hand_one, dealer_hand_two, community_cards)
        correct_outcome = ('royal flush', 'royal flush', 0, 0)
        self.assertEqual(test_outcome, correct_outcome)
        

if __name__ == '__main__': 
    unittest.main() 