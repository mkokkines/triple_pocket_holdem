"""
This file specifies the Card class.
The card class  is very rudimentary: it consists solely of three properties:
a suite, a value (2-14, where 11-14 represent jack, queen, king, and ace respectively),
and a path to an image of that respective card.
The image path dictionary below specifies the paths.
"""

image_paths = {
    'diamonds': {
        2: 'cards/2_of_diamonds.png',
        3: 'cards/3_of_diamonds.png',
        4: 'cards/4_of_diamonds.png',
        5: 'cards/5_of_diamonds.png',
        6: 'cards/6_of_diamonds.png',
        7: 'cards/7_of_diamonds.png',
        8: 'cards/8_of_diamonds.png',
        9: 'cards/9_of_diamonds.png',
        10: 'cards/10_of_diamonds.png',
        11: 'cards/jack_of_diamonds.png',
        12: 'cards/queen_of_diamonds.png',
        13: 'cards/king_of_diamonds.png',
        14: 'cards/ace_of_diamonds.png'
    },
    'hearts': {
        2: 'cards/2_of_hearts.png',
        3: 'cards/3_of_hearts.png',
        4: 'cards/4_of_hearts.png',
        5: 'cards/5_of_hearts.png',
        6: 'cards/6_of_hearts.png',
        7: 'cards/7_of_hearts.png',
        8: 'cards/8_of_hearts.png',
        9: 'cards/9_of_hearts.png',
        10: 'cards/10_of_hearts.png',
        11: 'cards/jack_of_hearts.png',
        12: 'cards/queen_of_hearts.png',
        13: 'cards/king_of_hearts.png',
        14: 'cards/ace_of_hearts.png'
    },
    'spades': {
        2: 'cards/2_of_spades.png',
        3: 'cards/3_of_spades.png',
        4: 'cards/4_of_spades.png',
        5: 'cards/5_of_spades.png',
        6: 'cards/6_of_spades.png',
        7: 'cards/7_of_spades.png',
        8: 'cards/8_of_spades.png',
        9: 'cards/9_of_spades.png',
        10: 'cards/10_of_spades.png',
        11: 'cards/jack_of_spades.png',
        12: 'cards/queen_of_spades.png',
        13: 'cards/king_of_spades.png',
        14: 'cards/ace_of_spades.png'
    },
    'clubs': {
        2: 'cards/2_of_clubs.png',
        3: 'cards/3_of_clubs.png',
        4: 'cards/4_of_clubs.png',
        5: 'cards/5_of_clubs.png',
        6: 'cards/6_of_clubs.png',
        7: 'cards/7_of_clubs.png',
        8: 'cards/8_of_clubs.png',
        9: 'cards/9_of_clubs.png',
        10: 'cards/10_of_clubs.png',
        11: 'cards/jack_of_clubs.png',
        12: 'cards/queen_of_clubs.png',
        13: 'cards/king_of_clubs.png',
        14: 'cards/ace_of_clubs.png'
    }

}

class Card:
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        self.img_path = image_paths[self.suite][self.value]
