#  Provide constant tuples for the colors in the RGB color space
BG_COLOR = (71, 113, 72)
LIGHTGREEN = (50, 205, 50)
GREEN = (0, 128, 0)
RED = (220, 20, 60)
LIGHTRED = (240, 128, 128)
SILVER = (192, 192, 192)
GRAY = (169, 169, 169)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Overarching Display
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
DISPLAY_NAME = 'Triple Pocket Texas Hold\'Em'

# The image ont he menu page
TITLE_IMG_PATH = 'title.png'
TITLE_LOCATION = (220, 100)

# The font we are using
FONT = 'freesansbold.ttf'

# Overall Button Settings
BUTTON_TEXT_SIZE = 20
BUTTON_BORDER_WIDTH = 1

# Buttons on the menu screen
PLAY_BUTTON_LOCATION = (215, 450, 150, 50)
RULES_BUTTON_LOCATION = (415, 450, 150, 50)
PLAY_TEXT_LOCATION = (265, 465)
RULES_TEXT_LOCATION = (462, 465)

# Message when the user clicks play and the game is loading
WELCOME_MESSAGE = "Your game is starting up..."
WELCOME_MESAGE_LOCATION = (170, 250)
WELCOME_MESSAGE_FONT_SIZE = 30

# Number of remaining chips information for the dealer and player
PLAYER_INFO_FONT_SIZE = 30
DEALER_INFO_LOCATION = (200, 20)
PLAYER_INFO_LOCATION = (200,  550)

# Image for card backside
DECK_IMG_PATH = 'back-side.png'
DECK_IMG_LOCATION = (20, 260)

# Settings for the elements on the screen when the user is submitting
# a wager
WAGER_FONT_SIZE = 20
WAGER_QUESTION_LOCATION = (220, 240)
WAGER_BOX_LOCATION = (250, 280, 100, 60)
WAGER_NUMBER_LOCATION = (275, 300)
WAGER_PLUS_BUTTON_LOCATION = (350, 280, 50, 30)
WAGER_MINUS_BUTTON_LOCATION = (350, 310, 50, 30)
WAGER_PLUS_TEXT_LOCATION = (368, 285)
WAGER_MINUS_TEXT_LOCATION = (370, 315)
CONFIRM_BUTTON_LOCATION = (430, 280, 100, 60)
CONFIRM_TEXT_LOCATION = (440, 300)

# Instructions that are presented to the user on the pocket card selection process
HAND_INSTRUCTION_TEXT = [
    "You will now be shown up to three hands.", 
    "Once shown a hand, you must decide whether to pick it up."
]
HAND_INSTRUCTION_FONT_SIZE = 20
HAND_INSTRUCTION_START_X = 150
HAND_INSTRUCTION_START_Y = 280
HAND_INSTRUCTION_STEP_Y = 27

# Cards being shown as options to the user
HAND_LABEL_POSITION = (278, 220)
HAND_LABEL_FONT_SIZE = 25
FIRST_CARD_POSITION = (250, 260)
SECOND_CARD_POSITION = (375, 260)
ACCEPT_BUTTON_LOCATION = (500, 280, 80, 40)
ACCEPT_TEXT_LOCATION = (505, 290)
REJECT_BUTTON_LOCATION = (500, 330, 80, 40)
REJECT_TEXT_LOCATION = (507, 340)

# Text explaining to the user that they will be forced to accept
# the third pair of pocket cards
THIRD_HAND_TEXT = [
    "You did not pick up either of the first two hands.",
    "By default, you will receive the third hand."
]
THIRD_HAND_TEXT_FONT_SIZE = 20
THIRD_HAND_TEXT_START_X = 150
THIRD_HAND_TEXT_START_Y = 280
THIRD_HAND_TEXT_STEP_Y = 27

# Text displayed to the user before all of the community
# and opponent's cards are revealed
CARD_REVEAL_TEXT = [
    "We will now reveal your cards and the dealer's cards, ",
    "followed by the five community cards."
]
CARD_REVEAL_TEXT_FONT_SIZE = 20
CARD_REVEAL_TEXT_START_X = 150
CARD_REVEAL_TEXT_START_Y = 280
CARD_REVEAL_TEXT_STEP_Y = 27

# Community card locations on the screen
PLAYER_FIRST_CARD_LOCATION = (260, 400)
PLAYER_SECOND_CARD_LOCATION = (360, 400)
DEALER_FIRST_CARD_LOCATION = (160, 60)
DEALER_SECOND_CARD_LOCATION = (260, 60)
DEALER_THIRD_CARD_LOCATION = (400, 60)
DEALER_FOURTH_CARD_LOCATION = (500, 60)
FIRST_COMMON_CARD_LOCATION = (170, 240)
SECOND_COMMON_CARD_LOCATION = (270, 240)
THIRD_COMMON_CARD_LOCATION = (370, 240)
FOURTH_COMMON_CARD_LOCATION = (470, 240)
FIFTH_COMMON_CARD_LOCATION = (570, 240)

# Explanation text when the outcome of the hand is presented
# to the user
OUTCOME_EXPLAIN_TEXT_FONT_SIZE = 20
OUTCOME_EXPLAIN_TEXT_START_X = 150
OUTCOME_EXPLAIN_TEXT_START_Y = 280
OUTCOME_EXPLAIN_TEXT_STEP_Y = 27

# Text presented to the user at the end of the round
ROUND_END_TEXT_FONT_SIZE = 30
ROUND_END_TEXT_START_X = 120
ROUND_END_TEXT_START_Y = 150
ROUND_END_TEXT_STEP_Y = 35
VICTORY_TEXT = [
    "Congratulations! You have beaten the dealer.",
    "You are on your way to becoming a poker champion."
]
DEFEAT_TEXT = [
    "Shoot! The dealer emerged victorious this time.",
    "As is often said, failure is the mother of success."
]
PLAY_ANOTHER_ROUND_TEXT = [
    "You still have chips remaining!",
    "Would you like to continue playing?"
]

PLAY_AGAIN_BUTTON_LOCATION = (300, 275, 150, 50)
PLAY_AGAIN_TEXT_LOCATION = (325, 290)

BACK_BUTTON_LOCATION = (20, 20, 60, 35)
BACK_TEXT_LOCATION = (26, 28)


RULES_FONT_SIZE = 15
RULES_X = 50
RULES_START_Y = 80
RULES_Y_INTERVAL = 20
RULES = [ 
    "Triple pocket is a variation of Texas Hold'Em played between one player and the dealer. ",
    "",
    "In Triple Pocket, you get a hand with two cards (your “pocket cards”). The dealer gets two hands, ",
    "each with two cards. There are 5 community cards dealt to the middle of the poker table. You may ",
    "use any 5 of the 7 cards available to you -- your two pocket cards plus the 5 community cards — to ", 
    "create the strongest possible 5-card poker hand. To win at Triple Pocket, your hand must beat both ", 
    "of the dealer’s hands.",
    "",
    "Each round begins with you placing a bet. There will be no further betting for the remainder of the ", 
    "round (details on scoring to come).",
    "",
    "You will be given up to three chances to select your hand -- hence the name Triple Pocket. After ",
    "betting, you will be dealt a hand. If you like your first hand, you can keep it. If not, you can ",
    "pass the hand on to the dealer. The same process repeats for your second hand: keep it if you ",
    "like it, give it to the dealer if you do not. If you discard your first two hands, you will ",
    "be stuck with the third hand that you are dealt.",
    "",
    "Once you have selected your hand, the dealer will draw additional hands until he/she has ",
    "two hands. At this point, the five community cards will be placed down, the winner will be ", 
    "determined, and scoring will be assessed. In most cases, the payout will be one-to-one. ", 
    "However, you (and not the dealer), will receive bonus payouts for certain hands: ",
    "flush (2x payout), full house (4x payout), four of a kind (10x payout), straight flush (20x ",
    "payout), and  royal flush (50x payout).",
    "",
    "The game will continue until you quit, you run out of chips, or the dealer runs out of chips. "
]