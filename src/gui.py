import pygame, sys
from pygame.locals import *
import os
from src.gui_constants import *

image_directory = os.path.join(os.path.dirname(__file__), '../img/')

class GUI:
    def __init__(self):
        self.game_display = None
        self.current_screen = None
        self.player_num_chips = 0
        self.dealer_num_chips = 0
    
    def fill_screen(self):
        self.game_display.fill(BG_COLOR)
        pygame.display.update()

    def render_text(self, text, font_size, location, color):
        font = pygame.font.Font(FONT, font_size)
        self.render_text_helper(text, font, location, color)
        pygame.display.update()

    def render_multiple_lines_of_text(self, text, font_size, x, start_y, interval_y, color):
        font = pygame.font.Font(FONT, font_size)
        y_location = start_y
        for line in text:
            self.render_text_helper(line, font, (x, y_location), color)
            y_location += interval_y
        pygame.display.update()

    def render_text_helper(self, text, font, location, color):
        text_surface = font.render(text, True, color)        
        self.game_display.blit(text_surface, location)

    def render_image(self, file_path, location):
        img = pygame.image.load(os.path.join(image_directory, file_path))
        self.game_display.blit(img, location)
        pygame.display.update()
    
    def render_box(self, color, location, text, text_location, text_color):
        """
        Renders a rectangular box with a border and text in it.
        These are often used as buttons.
        """
        pygame.draw.rect(self.game_display, color, location)
        pygame.draw.rect(self.game_display, BLACK, location, BUTTON_BORDER_WIDTH)
        font = pygame.font.Font(FONT, BUTTON_TEXT_SIZE)
        self.render_text_helper(text, font, text_location, text_color)
        pygame.display.update()

    def update_button_on_hover(
        self, 
        mouse_x, 
        mouse_y, 
        next_mouse_x, 
        next_mouse_y, 
        button_location, 
        button_text, 
        button_text_location,
        normal_color,
        hover_color,
        text_color
    ):
        """
        Changes the color of a rectanglular button when the user hovers over it
        or stops hovering over it
        """
        over_button = self.is_mouse_over_button(mouse_x, mouse_y, button_location)
        will_be_over_button = self.is_mouse_over_button(next_mouse_x, next_mouse_y, button_location)

        if not over_button and will_be_over_button:
            self.render_box(hover_color, button_location, button_text, button_text_location, text_color)
        elif over_button and not will_be_over_button:
            self.render_box(normal_color, button_location, button_text, button_text_location, text_color)

    def is_mouse_over_button(self, mouse_x, mouse_y, button_location):
        """
        Returns true if the user is currently hovering over the
        specified button.
        """
        button_pos_left = button_location[0]
        button_pos_right = button_location[0] + button_location[2]
        button_pos_top = button_location[1]
        button_pos_bottom = button_location[1] + button_location[3]
        return (mouse_x >= button_pos_left 
            and mouse_x <= button_pos_right
            and mouse_y >= button_pos_top
            and mouse_y <= button_pos_bottom)

    def initialize_gui(self):
        self.game_display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption(DISPLAY_NAME)

    def create_menu_screen(self):
        self.fill_screen()
        self.render_image(TITLE_IMG_PATH, TITLE_LOCATION)        
        self.render_box(RED, PLAY_BUTTON_LOCATION, 'Play', PLAY_TEXT_LOCATION, WHITE)
        self.render_box(RED, RULES_BUTTON_LOCATION, 'Rules', RULES_TEXT_LOCATION, WHITE)

    def update_menu_screen_mouse_motion(self, mouse_x, mouse_y, next_mouse_x, next_mouse_y):  
        """
        Updates the display of the buttons on the menu screen depdending on mouse location
        """
        self.update_button_on_hover(
            mouse_x, 
            mouse_y, 
            next_mouse_x, 
            next_mouse_y, 
            PLAY_BUTTON_LOCATION, 
            'Play', 
            PLAY_TEXT_LOCATION, 
            RED, 
            LIGHTRED,
            WHITE
        )  
        self.update_button_on_hover(
            mouse_x, 
            mouse_y, 
            next_mouse_x, 
            next_mouse_y, 
            RULES_BUTTON_LOCATION, 
            'Rules', 
            RULES_TEXT_LOCATION, 
            RED, 
            LIGHTRED,
            WHITE
        )
    
    def mouse_on_play_button(self, mouse_x, mouse_y):
        return self.is_mouse_over_button(mouse_x, mouse_y, PLAY_BUTTON_LOCATION)

    def mouse_on_rules_button(self, mouse_x, mouse_y):
        return self.is_mouse_over_button(mouse_x, mouse_y, RULES_BUTTON_LOCATION)

    def create_rules_screen(self):
        self.fill_screen()
        self.render_box(RED, BACK_BUTTON_LOCATION, 'Back', BACK_TEXT_LOCATION, WHITE)
        self.render_multiple_lines_of_text(RULES, RULES_FONT_SIZE, RULES_X, RULES_START_Y, RULES_Y_INTERVAL, WHITE)

    def update_rules_screen_mouse_motion(self, mouse_x, mouse_y, next_mouse_x, next_mouse_y):
        self.update_back_button_mouse_hover(mouse_x, mouse_y, next_mouse_x, next_mouse_y)      

    def update_back_button_mouse_hover(self, mouse_x, mouse_y, next_mouse_x, next_mouse_y):
        self.update_button_on_hover(
            mouse_x, 
            mouse_y, 
            next_mouse_x, 
            next_mouse_y, 
            BACK_BUTTON_LOCATION, 
            'Back', 
            BACK_TEXT_LOCATION, 
            RED, 
            LIGHTRED,
            BLACK
        )

    def mouse_on_back_button(self, mouse_x, mouse_y):
        return self.is_mouse_over_button(mouse_x, mouse_y, BACK_BUTTON_LOCATION)  
   
    def create_play_screen(self):
        self.fill_screen()
        self.render_text(WELCOME_MESSAGE, WELCOME_MESSAGE_FONT_SIZE, WELCOME_MESAGE_LOCATION, BLACK)

    def create_game_board(self):
        """
        Creates an empty game board and then adds the chip numbers and the deck image.
        """
        self.fill_screen()
        self.render_text(
            'Dealer Chip Number: ' + str(self.dealer_num_chips), 
            PLAYER_INFO_FONT_SIZE, 
            DEALER_INFO_LOCATION, 
            BLACK
        )
        self.render_text(
            'Your Chip Number: ' + str(self.player_num_chips),
            PLAYER_INFO_FONT_SIZE,
            PLAYER_INFO_LOCATION, 
            BLACK
        )
        self.render_image(DECK_IMG_PATH, DECK_IMG_LOCATION)

    def ask_for_wager(self, initial_wager, player_num_chips, dealer_num_chips):
        self.player_num_chips = player_num_chips
        self.dealer_num_chips = dealer_num_chips
        self.create_game_board()
        self.render_text(
            'How much would you like to wager?',
            WAGER_FONT_SIZE,
            WAGER_QUESTION_LOCATION,
            WHITE
        )
        self.render_box(SILVER, WAGER_BOX_LOCATION, str(initial_wager), WAGER_NUMBER_LOCATION, BLACK)
        self.render_box(SILVER, WAGER_PLUS_BUTTON_LOCATION, '+', WAGER_PLUS_TEXT_LOCATION, BLACK)
        self.render_box(SILVER, WAGER_MINUS_BUTTON_LOCATION, '-', WAGER_MINUS_TEXT_LOCATION, BLACK)
        self.render_box(LIGHTGREEN, CONFIRM_BUTTON_LOCATION, 'Confirm', CONFIRM_TEXT_LOCATION, BLACK)

    def update_wager_amount(self, wager):
        self.render_box(SILVER, WAGER_BOX_LOCATION, str(wager), WAGER_NUMBER_LOCATION, BLACK)

    def update_wager_screen_on_mouse_move(self, mouse_x, mouse_y, next_mouse_x, next_mouse_y):
        self.update_button_on_hover(
            mouse_x, 
            mouse_y, 
            next_mouse_x, 
            next_mouse_y, 
            WAGER_PLUS_BUTTON_LOCATION, 
            '+', 
            WAGER_PLUS_TEXT_LOCATION, 
            SILVER, 
            GRAY,
            BLACK
        )
        self.update_button_on_hover(
            mouse_x, 
            mouse_y, 
            next_mouse_x, 
            next_mouse_y, 
            WAGER_MINUS_BUTTON_LOCATION, 
            '-', 
            WAGER_MINUS_TEXT_LOCATION, 
            SILVER, 
            GRAY,
            BLACK
        )
        self.update_button_on_hover(
            mouse_x, 
            mouse_y, 
            next_mouse_x, 
            next_mouse_y, 
            CONFIRM_BUTTON_LOCATION, 
            'Confirm', 
            CONFIRM_TEXT_LOCATION, 
            LIGHTGREEN, 
            GREEN,
            BLACK
        )

    def mouse_on_plus_button(self, mouse_x, mouse_y):
        return self.is_mouse_over_button(mouse_x, mouse_y, WAGER_PLUS_BUTTON_LOCATION)
    
    def mouse_on_minus_button(self, mouse_x, mouse_y):
        return self.is_mouse_over_button(mouse_x, mouse_y, WAGER_MINUS_BUTTON_LOCATION)

    def mouse_on_confirm_button(self, mouse_x, mouse_y):
        return self.is_mouse_over_button(mouse_x, mouse_y, CONFIRM_BUTTON_LOCATION)
    
    def show_hand_select_instructions(self):
        """
        Present instructions to the user on how the hand selection process works in triple pocket holdem.
        Clear the game board and then render the instructions
        """
        self.create_game_board()
        self.render_multiple_lines_of_text(
            HAND_INSTRUCTION_TEXT, 
            HAND_INSTRUCTION_FONT_SIZE, 
            HAND_INSTRUCTION_START_X,
            HAND_INSTRUCTION_START_Y,
            HAND_INSTRUCTION_STEP_Y,
            BLACK
        )
    
    def show_hand(self, card_one_img_path, card_two_img_path, label):
        """
        Shows the user the hands they have an opportunity to pick up.
        """
        self.create_game_board()
        self.render_text(label, HAND_LABEL_FONT_SIZE,HAND_LABEL_POSITION, BLACK)
        self.render_image(card_one_img_path, FIRST_CARD_POSITION)
        self.render_image(card_two_img_path, SECOND_CARD_POSITION)
        self.render_box(LIGHTGREEN, ACCEPT_BUTTON_LOCATION, 'Accept', ACCEPT_TEXT_LOCATION, BLACK)
        self.render_box(LIGHTRED, REJECT_BUTTON_LOCATION, 'Reject', REJECT_TEXT_LOCATION, BLACK)

    def show_first_hand(self, card_one_img_path, card_two_img_path):
        self.show_hand(card_one_img_path, card_two_img_path, 'First Hand:')
    
    def show_second_hand(self, card_one_img_path, card_two_img_path):
        self.show_hand(card_one_img_path, card_two_img_path, 'Second Hand:')

    def update_hand_screen_on_mouse_move(self, mouse_x, mouse_y, next_mouse_x, next_mouse_y):
        self.update_button_on_hover(
            mouse_x, 
            mouse_y, 
            next_mouse_x, 
            next_mouse_y, 
            ACCEPT_BUTTON_LOCATION, 
            'Accept', 
            ACCEPT_TEXT_LOCATION, 
            LIGHTGREEN, 
            GREEN,
            BLACK
        )
        self.update_button_on_hover(
            mouse_x, 
            mouse_y, 
            next_mouse_x, 
            next_mouse_y, 
            REJECT_BUTTON_LOCATION, 
            'Reject', 
            REJECT_TEXT_LOCATION, 
            LIGHTRED, 
            RED, 
            BLACK           
        )
    
    def mouse_on_accept_button(self, mouse_x, mouse_y):
        return self.is_mouse_over_button(mouse_x, mouse_y, ACCEPT_BUTTON_LOCATION)
    
    def mouse_on_reject_button(self, mouse_x,  mouse_y):
        return self.is_mouse_over_button(mouse_x, mouse_y, REJECT_BUTTON_LOCATION)

    def alert_to_third_hand(self):
        """
        When the user rejects the first two hands, we alert them that they have
        no choice but to accept the third hand dealt to them.
        """
        self.create_game_board()
        self.render_multiple_lines_of_text(
            THIRD_HAND_TEXT, 
            THIRD_HAND_TEXT_FONT_SIZE, 
            THIRD_HAND_TEXT_START_X,
            THIRD_HAND_TEXT_START_Y,
            THIRD_HAND_TEXT_STEP_Y,
            BLACK
        )
    
    def explain_card_reveal(self):
        """
        Explains that the dealer's cards and the community cards will be 
        shown consecutively.
        """
        self.create_game_board()
        self.render_multiple_lines_of_text(
            CARD_REVEAL_TEXT, 
            CARD_REVEAL_TEXT_FONT_SIZE, 
            CARD_REVEAL_TEXT_START_X,
            CARD_REVEAL_TEXT_START_Y,
            CARD_REVEAL_TEXT_STEP_Y,
            BLACK
        )
    
    def reveal_player_cards(self, player, dealer):
        """
        Shows the cards held by the player and the dealer.
        """
        self.create_game_board()
        self.render_image(player.hands[0][0].img_path, PLAYER_FIRST_CARD_LOCATION)
        self.render_image(player.hands[0][1].img_path, PLAYER_SECOND_CARD_LOCATION)
        self.render_image(dealer.hands[0][0].img_path, DEALER_FIRST_CARD_LOCATION)
        self.render_image(dealer.hands[0][1].img_path, DEALER_SECOND_CARD_LOCATION)
        self.render_image(dealer.hands[1][0].img_path, DEALER_THIRD_CARD_LOCATION)
        self.render_image(dealer.hands[1][1].img_path, DEALER_FOURTH_CARD_LOCATION)
        self.render_image(DECK_IMG_PATH, FIRST_COMMON_CARD_LOCATION)
        self.render_image(DECK_IMG_PATH, SECOND_COMMON_CARD_LOCATION)
        self.render_image(DECK_IMG_PATH, THIRD_COMMON_CARD_LOCATION)
        self.render_image(DECK_IMG_PATH, FOURTH_COMMON_CARD_LOCATION)
        self.render_image(DECK_IMG_PATH, FIFTH_COMMON_CARD_LOCATION)
    
    def reveal_common_cards(self, community_cards):
        self.render_image(community_cards[0].img_path, FIRST_COMMON_CARD_LOCATION)
        self.render_image(community_cards[1].img_path, SECOND_COMMON_CARD_LOCATION)
        self.render_image(community_cards[2].img_path, THIRD_COMMON_CARD_LOCATION)
        self.render_image(community_cards[3].img_path, FOURTH_COMMON_CARD_LOCATION)
        self.render_image(community_cards[4].img_path, FIFTH_COMMON_CARD_LOCATION)

    def explain_outcome(self, player_hand, dealer_hand, wager_multiple, player_num_chips, dealer_num_chips):
        self.player_num_chips = player_num_chips
        self.dealer_num_chips = dealer_num_chips
        self.create_game_board()
        
        if wager_multiple > 0:
            winner = 'you'
        elif wager_multiple < 0:
            winner = "the dealer"
        else:
            winner = "neither of you"
        explanation = [
            "Your best hand was {}.".format(player_hand),
            "The dealer's best hand was {}.".format(dealer_hand),
            "{} won, and the multiple was {}.".format(winner, abs(wager_multiple))
        ]
        self.render_multiple_lines_of_text(
            explanation, 
            OUTCOME_EXPLAIN_TEXT_FONT_SIZE, 
            OUTCOME_EXPLAIN_TEXT_START_X,
            OUTCOME_EXPLAIN_TEXT_START_Y,
            OUTCOME_EXPLAIN_TEXT_STEP_Y,
            BLACK
        )

    def show_round_end_screen(self, text, player_num_chips, dealer_num_chips):
        self.create_game_board()
        self.render_multiple_lines_of_text(
            text,
            ROUND_END_TEXT_FONT_SIZE,
            ROUND_END_TEXT_START_X,
            ROUND_END_TEXT_START_Y,
            ROUND_END_TEXT_STEP_Y,
            BLACK
        )
        self.render_box(LIGHTGREEN, PLAY_AGAIN_BUTTON_LOCATION, 'Play Again', PLAY_AGAIN_TEXT_LOCATION, BLACK)
        self.render_box(RED, BACK_BUTTON_LOCATION, 'Back', BACK_TEXT_LOCATION, WHITE)

    def show_victory(self, player_num_chips, dealer_num_chips):
        self.show_round_end_screen(VICTORY_TEXT, player_num_chips, dealer_num_chips)

    def show_defeat(self, player_num_chips, dealer_num_chips):
        self.show_round_end_screen(DEFEAT_TEXT, player_num_chips, dealer_num_chips)

    def show_game_continuing(self, player_num_chips, dealer_num_chips):
        self.show_round_end_screen(PLAY_ANOTHER_ROUND_TEXT, player_num_chips, dealer_num_chips)

    def update_round_end_screen_mouse_move(self, mouse_x, mouse_y, next_mouse_x, next_mouse_y):
        self.update_back_button_mouse_hover(mouse_x, mouse_y, next_mouse_x, next_mouse_y)      
        self.update_button_on_hover(
            mouse_x, 
            mouse_y, 
            next_mouse_x, 
            next_mouse_y, 
            PLAY_AGAIN_BUTTON_LOCATION, 
            'Play Again', 
            PLAY_AGAIN_TEXT_LOCATION, 
            LIGHTGREEN, 
            GREEN,
            BLACK
        )
    
    def mouse_on_play_again_button(self, mouse_x, mouse_y):
        return self.is_mouse_over_button(mouse_x, mouse_y, PLAY_AGAIN_BUTTON_LOCATION)
