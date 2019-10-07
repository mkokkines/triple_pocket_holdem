"""
This file contains functions that fall into one of the following three categories:
1) Determine if a series of five cards fulfills the requirements of a poker hand 
   (i.e. is the series of five cards a royal flush?).
2) Break ties between 5 card sets -- i.e. which set of five cards is 
   victorious if they are both pairs?
3) Determine the outcome of a round of Triple Pocket Holdem, first adjudicating
   a winner and then determining what the wager multiple should be.
"""

import itertools

# Maps a poker hand to a ranking number
hand_ranking = {
    'royal flush': 10,
    'straight flush': 9,
    'four of a kind': 8,
    'full house': 7,
    'flush': 6,
    'straight': 5,
    'three of a kind': 4,
    'two pairs': 3,
    'one pair': 2,
    'high card': 1
}

# Maps one of the ranking numbers above back to its poker hand.
ranking_to_hand = {
    10: 'royal flush',
    9: 'straight flush', 
    8: 'four of a kind',
    7: 'full house',
    6: 'flush',
    5:'straight',
    4: 'three of a kind',
    3: 'two pairs',
    2: 'one pair',
    1: 'high card',
}

# Maps a poker hand to its wager multiple.
# In triple pocket hold'em, the player receives a 50x multiple on their wager
# if they get a royal flush, a 20x multiple if they get a straight flush, and so
# forth.
ranking_multiple = {
    'royal flush': 50,
    'straight flush': 20,
    'four of a kind': 10,
    'full house': 4,
    'flush': 2,
    'straight': 1,
    'three of a kind': 1,
    'two pairs': 1,
    'one pair': 1,
    'high card': 1
}


def determine_outcome(hand_one, hand_two, hand_three, community_cards):
    """
    Determines the outcome for a round between the player and the dealer.
    Determines which player won and what the multiples on the player's wager
    should be.

    Params:
        hand_one: the two-card hand for the player
        hand_two: the first two-card hand for the dealer
        hand_three: the second two-card hand for the dealer
        community_cards: the five communal cards
    Returns:
        1) the highest ranking card for the player
        2) the highest ranking card for the dealer
        3) the wager multiple for the player
        4) the wager multiple for the dealer
    """
    all_player_hands = get_all_possible_hands_sorted(hand_one, community_cards)
    (player_highest_value, player_best_hand) = get_best_hand(all_player_hands)

    all_hand_two_combos = get_all_possible_hands_sorted(hand_two, community_cards)
    all_hand_three_combos = get_all_possible_hands_sorted(hand_three, community_cards)
    all_dealer_hands =  all_hand_two_combos + all_hand_three_combos
    (dealer_highest_value, dealer_best_hand) = get_best_hand(all_dealer_hands)

    if player_highest_value > dealer_highest_value:
        winner = 1
    elif player_highest_value < dealer_highest_value:
        winner = 2
    else:
        winner = break_tie(player_best_hand, dealer_best_hand, player_highest_value)

    player_wager_multiple, dealer_wager_multiple = get_wager_multiples(winner, player_highest_value)
    return (
        ranking_to_hand[player_highest_value], 
        ranking_to_hand[dealer_highest_value], 
        player_wager_multiple, 
        dealer_wager_multiple
    )


def get_all_possible_hands_sorted(player_hand, community_cards):
    """
    Given a player's hand (will be 2 cards in our case, but could be any size) and 
    a set of community cards (will be 5 cards in our case), returns all of the possible five-card
    combinations. Each five card combination is also sorted in descending order of rank.

    Params:
        player_hand: the tuple of cards held in the player's hand
        community_card: the tuple of cards available to all players
    Returns:
        All possible five-card hand combinations, each of which is sorted in descending 
        order of rank.
    """
    all_cards = player_hand + community_cards
    all_combos = list(itertools.combinations(all_cards, 5))
    return [
        sorted(all_combos[i], key=lambda x: x.value, reverse=True) for i in range(len(all_combos))
    ]


def get_best_hand(hands): 
    """
    Given a list of five-card hands, determines which has the most value (i.e. would win)
    in poker. Iterates through the list of hands and keeps track of the maximum-value hand seen thus far.

    Params:
        hands: a list of quintuples consisting of cards
    Returns:
        A tuple consisting of the maximimum value (see dictionaries above) of any hand and the 
        actual five-card hand that corresponds said value.
    """       
    max_value = 0
    best_hand = None
    
    for hand in hands:
        value = get_hand_value(hand)
        
        if value > max_value:
            best_hand = hand
            max_value = value
        elif value == max_value:
            better_hand = break_tie(best_hand, hand, value)
            if better_hand == 2:
                best_hand = hand
                max_value = value
    
    return (max_value, best_hand)


def get_wager_multiples(winner, player_highest_value):
    """
    In triple pocket hold'em, the player -- but not the dealer -- has their wager
    multiplied if they win with certain hands (as shown in the dictionary above).
    Otherwise, the multiple is set to -1 for the losing player and 1 for 
    the winning player (or 0 for both if it is a tie).

    Params:
        winner: the winner (2 for the dealer, 1 for the player, and 0 for a tie)
        player_highest_value: The ranking of the player's best hand (see above dict)
    Returns:
        A tuple showing the multiples that should be applied to the wager for
        the player and the dealer. A multiple of one means the player will
        have the wager added to their number of chips, a multiple of two means
        the player will receive double their wager in chips, a multiple of 0
        means the player's chip count will not change, and a multiple of -1 means
        the player will lose chips. 
    """
    if winner == 2:
        return (-1, 1)
    elif winner == 0:
        return (0, 0)
    else:
        hand_type = ranking_to_hand[player_highest_value]
        return (ranking_multiple[hand_type], -ranking_multiple[hand_type])


def get_hand_value(hand):
    """
    Given a tuple of five cards, determines the highest-ranking poker hand that the set of cards
    satisfies.

    Params:
        hand: a tuple consisting of five card objects
    Returns:
        The numerical ranking (again, see dictionaries above) for the hand
    """
    if is_royal_flush(hand):
        return hand_ranking['royal flush']
    elif is_straight_flush(hand):
        return hand_ranking['straight flush']
    elif is_four_of_a_kind(hand):
        return hand_ranking['four of a kind']
    elif is_full_house(hand):
        return hand_ranking['full house']
    elif is_flush(hand):
        return  hand_ranking['flush']
    elif is_straight(hand):
        return hand_ranking['straight']
    elif is_three_of_a_kind(hand):
        return hand_ranking['three of a kind']
    elif is_two_pair(hand):
        return hand_ranking['two pairs']
    elif is_pair(hand):
        return hand_ranking['one pair']
    else:
        return hand_ranking['high card']


def is_royal_flush(hand):
    """
    Determines if a set of five cards is a royal flush.
    A set of cards is a royal flush if all cards have the same suite
    and have values of ace, king, queen, jack, and ten.

    Params:
        A tuple of five card objects, sorted in descending rank order.
    Returns:
        Whether the hand is a royal flush
    """
    return (
        hand[0].value == 14 
        and hand[1].value == 13 
        and hand[2].value == 12
        and hand[3].value == 11
        and hand[4].value == 10
        and hand[0].suite == hand[1].suite
        and hand[0].suite == hand[2].suite
        and hand[0].suite == hand[3].suite
        and hand[0].suite == hand[4].suite
    )


def is_straight_flush(hand):
    """
    Determines if a set of five cards is a straight flush.
    As the name would suggest, a hand is a straight flush if it is both
    a straight and a flush.

    Params:
        A tuple of five card objects, sorted in descending rank order.
    Returns:
        Whether the hand is a royal flush
    """
    return is_flush(hand) and is_straight(hand)


def is_four_of_a_kind(hand):
    """
    Determines if a set of five cards contains four cards of the same value.
    Since the hand is sorted, it contains four of a kind if either
    the first or second has the same rank as the three subsequent cards.

    Params:
        A tuple of five card objects, sorted in descending rank order.
    Returns:
        Whether the hand contains four of a kind.
    """
    return (
        (
            hand[0].value == hand[1].value 
            and hand[0].value == hand[2].value 
            and hand[0].value == hand[3].value
        ) or (
            hand[1].value == hand[2].value 
            and hand[1].value == hand[3].value 
            and hand[1].value == hand[4].value
        )
    )


def is_full_house(hand):
    """
    Determines if a set of five cards contains a full house.
    A set of cards contains a full house if it has three cards of one value
    and two cards of another value. The group of three can either begin
    on the first card or the third card, since the cards are sorted.

    Params:
        A tuple of five card objects, sorted in descending rank order.
    Returns:
        Whether the hand contains a full house.
    """
    return (
        (
            hand[0].value == hand[1].value 
            and hand[0].value == hand[2].value
            and hand[3].value == hand[4].value 
        ) or (
            hand[0].value == hand[1].value
            and hand[2].value == hand[3].value
            and hand[2].value == hand[4].value
        )
    )


def is_flush(hand):
    """
    Determines if a set of five cards contains a flish.
    If all five cards have the same suite, the hand contains a flush.

    Params:
        A tuple of five card objects, sorted in descending rank order.
    Returns:
        Whether the hand contains a full house.
    """
    return (
        hand[0].suite == hand[1].suite
        and hand[0].suite == hand[2].suite
        and hand[0].suite == hand[3].suite
        and hand[0].suite == hand[4].suite
    )


def is_straight(hand):
    """
    Determines if a set of five cards is a straight.
    We have a straight when the five cards have five consecutive values.
    Thus, since the cards are sorted in descending order, each card will
    have a value that  is one less than the previous card.

    Params:
        A tuple of five card objects, sorted in descending rank order.
    Returns:
        Whether the hand is a straight.
    """
    return (
        hand[0].value - 1  == hand[1].value
        and hand[1].value - 1  == hand[2].value
        and hand[2].value - 1  == hand[3].value
        and hand[3].value - 1  == hand[4].value
    )


def is_three_of_a_kind(hand):
    """
    Determines if a set of five cards contains three cards of the same value.
    Since the cards are pre-sorted, the three-of-a-kind will either consist
    of  the first three, second three, or third three cards.

    Params:
        A tuple of five card objects, sorted in descending rank order.
    Returns:
        Whether the hand contains three of a kind.
    """
    return (
        (
            hand[0].value == hand[1].value
            and hand[0].value == hand[2].value
        ) or (
            hand[1].value == hand[2].value
            and hand[1].value == hand[3].value
        ) or  (
            hand[2].value == hand[3].value
            and hand[2].value == hand[4].value
        )
    )


def is_two_pair(hand):
    """
    Determines whether the hand contains two pairs of cards that have the 
    same rank.

    Params:
        A tuple of five card objects, sorted in descending rank order.
    Returns:
        Whether the hand contains two pairs.
    """
    return (
        (
            hand[0].value == hand[1].value
            and hand[2].value == hand[3].value
        ) or (
            hand[0].value == hand[1].value
            and hand[3].value == hand[4].value 
        ) or (
            hand[1].value == hand[2].value
            and hand[3].value == hand[4].value
        )
    )


def is_pair(hand):
    """
    Determines whether  a five-card hand contains two cards of 
    the same rank.

    Params:
        A tuple of five card objects, sorted in descending rank order.
    Returns:
        Whether the hand contains a pair.
    """
    return (
        hand[0].value == hand[1].value 
        or hand[1].value == hand[2].value
        or hand[2].value == hand[3].value
        or hand[3].value == hand[4].value
    )


def break_tie(hand_one, hand_two, value):
    """
    Breaks ties between hands, meaning that if two hands have the same rank
    (i.e. both are flushes, both are straights), this function determines
    which is greater. Each type of hand has its own rules for tie breakers
    in poker.

    Params:
        hand_one: A tuple of five card objects, sorted in descending rank order.
        hand_two: A tuple of five card objects, sorted in descending rank order.
        value: The value of the given hands (see dictionary at the top of file)
    Returns:
        0 if the two hands have an exactly even poker value 
        1 if the first hand is greater
        2 if the second hand is greater
    """
    # If both hands are royal flushes, they are tied.
    if value == hand_ranking['royal flush']:
        return 0
    elif value == hand_ranking['straight flush']:
        return break_tie_straight(hand_one, hand_two)
    elif value == hand_ranking['four of a kind']:
        return break_tie_four_of_a_kind(hand_one, hand_two)
    elif value == hand_ranking['full house']:
        return break_tie_full_house(hand_one, hand_two)
    elif value == hand_ranking['flush']:
        return break_tie_flush(hand_one, hand_two)
    elif value == hand_ranking['straight']:
        return break_tie_straight(hand_one, hand_two)
    elif value == hand_ranking['three of a kind']:
        return break_tie_three_of_a_kind(hand_one, hand_two)
    elif value == hand_ranking['two pairs']:
        return break_tie_two_pairs(hand_one, hand_two)
    elif value == hand_ranking['one pair']:
        return break_tie_one_pair(hand_one, hand_two)
    else:
        return break_tie_high_card(hand_one, hand_two)


def break_tie_straight(hand_one, hand_two):
    """
    Given two straights, determines which has a higher value.
    The straight with the highest valued card is more valuable.
    If both straights cover the same values, they are equivalent.

    Params:
        hand_one: A tuple of five card objects, sorted in descending rank order.
        hand_two: A tuple of five card objects, sorted in descending rank order. 
    Returns:
        0 if the two hands have an exactly even poker value 
        1 if the first hand is greater
        2 if the second hand is greater         
    """
    if hand_one[0].value > hand_two[0].value:
        return 1
    elif hand_two[0].value >  hand_one[0].value:
        return 2
    else: 
        return 0


def break_tie_four_of_a_kind(hand_one, hand_two):
    """
    Given two hands containing four of a kind, determines which hand is more
    valuable in poker. The hand with the greater value for its set of four
    is greater (i.e. four 10s is greater than four 2s). 
    If both hands have the same value for their set of four
    (possible due to the community cards), the hand with the larger-value 
    fifth card is more valuable. If both hands of the same value for their
    set of four and the same fifth card, they are identical.

    Params:
        hand_one: A tuple of five card objects, sorted in descending rank order.
        hand_two: A tuple of five card objects, sorted in descending rank order. 
    Returns:
        0 if the two hands have an exactly even poker value 
        1 if the first hand is greater
        2 if the second hand is greater  
    """
    if hand_one[0].value == hand_one[1].value:
        four_card_value_hand_one = hand_one[0].value
        kicker_hand_one = hand_one[4].value
    else:
        four_card_value_hand_one = hand_one[1].value
        kicker_hand_one = hand_one[0].value
    
    if hand_two[0].value == hand_two[1].value:
        four_card_value_hand_two = hand_two[0].value
        kicker_hand_two = hand_two[4].value
    else:
        four_card_value_hand_two = hand_two[1].value
        kicker_hand_two = hand_two[0].value

    if four_card_value_hand_one > four_card_value_hand_two:
        return 1
    elif four_card_value_hand_two > four_card_value_hand_one:
        return 2
    elif kicker_hand_one > kicker_hand_two:
        return 1
    elif kicker_hand_two > kicker_hand_one:
        return 2
    else:
        return 0


def break_tie_full_house(hand_one, hand_two):
    """
    Given two hands that both are full houses, determine which has greater value in poker.
    The hand with the greater value for its set of 3 (i.e. three 10s is greater than three 2s)
    is  greater.
    If both hands of the same value for their set of three, the hand with the greater value for 
    its set of two is greater.
    If both hands have the same value for their set of two and their set of three, the hands
    are equivalent.

    Params:
        hand_one: A tuple of five card objects, sorted in descending rank order.
        hand_two: A tuple of five card objects, sorted in descending rank order. 
    Returns:
        0 if the two hands have an exactly even poker value 
        1 if the first hand is greater
        2 if the second hand is greater  
    """
    if hand_one[0].value == hand_one[1].value and hand_one[0].value == hand_one[2].value:
        hand_one_trips = hand_one[0].value
        hand_one_pair = hand_one[3].value
    else:
        hand_one_trips = hand_one[2].value
        hand_one_pair = hand_one[0].value

    if hand_two[0].value == hand_two[1].value and hand_two[0].value == hand_two[2].value:
        hand_two_trips = hand_two[0].value
        hand_two_pair = hand_two[3].value
    else:
        hand_two_trips = hand_two[2].value
        hand_two_pair = hand_two[0].value

    if hand_one_trips > hand_two_trips:
        return 1
    elif hand_two_trips > hand_one_trips:
        return 2
    elif hand_one_pair > hand_two_pair:
        return 1
    elif  hand_two_pair > hand_one_pair: 
        return 2
    else:
        return 0


def break_tie_flush(hand_one, hand_two):
    """
    Given two hands that are both flushes, determine which has the greater poker value.
    The flush with the greatest valued card is more valuable. If both have  the same
    highest-valued card,  the  second highest-valued card is used -- and so forth as 
    necessary. It turns out that this is the same method for distinguishing high cards.
    
    Params:
        hand_one: A tuple of five card objects, sorted in descending rank order.
        hand_two: A tuple of five card objects, sorted in descending rank order. 
    Returns:
        0 if the two hands have an exactly even poker value 
        1 if the first hand is greater
        2 if the second hand is greater  
    """
    return break_tie_high_card(hand_one, hand_two)


def break_tie_three_of_a_kind(hand_one, hand_two):
    """
    Given two hands that both contain three of a kind, determine which is more valuable in poker.
    The hand with the larger value for its three of a kind is more valuable (i.e. three 10s is more 
    valuable than three 2s).
    If both hands have the same value for their three of a kind, we select the hand with the higher-valued
    first kicker card.
    If both hands have the same value for their first kicker card, we check the second kicker card.
    If, after checking the second kicker card, the hands still have the same value, they are 
    equivalent.
    
    Params:
        hand_one: A tuple of five card objects, sorted in descending rank order.
        hand_two: A tuple of five card objects, sorted in descending rank order. 
    Returns:
        0 if the two hands have an exactly even poker value 
        1 if the first hand is greater
        2 if the second hand is greater  
    """
    if hand_one[0].value == hand_one[1].value and hand_one[0].value == hand_one[2].value:
        hand_one_trips = hand_one[0].value
        hand_one_first_kicker = hand_one[3].value
        hand_one_second_kicker = hand_one[4].value
    elif hand_one[1].value == hand_one[2].value and hand_one[1].value == hand_one[3].value:
        hand_one_trips = hand_one[1].value
        hand_one_first_kicker = hand_one[0].value
        hand_one_second_kicker = hand_one[4].value
    else:
        hand_one_trips = hand_one[2].value
        hand_one_first_kicker = hand_one[0].value
        hand_one_second_kicker = hand_one[1].value

    if hand_two[0].value == hand_two[1].value and hand_two[0].value == hand_two[2].value:
        hand_two_trips = hand_two[0].value
        hand_two_first_kicker = hand_two[3].value
        hand_two_second_kicker = hand_two[4].value
    elif hand_two[1].value == hand_two[2].value and hand_two[1].value == hand_two[3].value:
        hand_two_trips = hand_two[1].value
        hand_two_first_kicker = hand_two[0].value
        hand_two_second_kicker = hand_two[4].value
    else:
        hand_two_trips = hand_two[2].value
        hand_two_first_kicker = hand_two[0].value
        hand_two_second_kicker = hand_two[1].value

    if hand_one_trips > hand_two_trips:
        return 1
    elif hand_two_trips > hand_one_trips:
        return 2
    elif hand_one_first_kicker > hand_two_first_kicker:
        return 1
    elif hand_two_first_kicker > hand_one_first_kicker:
        return 2
    elif hand_one_second_kicker > hand_two_second_kicker:
        return 1
    elif hand_two_second_kicker > hand_two_first_kicker:
        return 2
    else:
        return 0


def break_tie_two_pairs(hand_one, hand_two):
    """
    Given two hands that both contain two pairs, determine which has higher poker value.
    We first compare the higher-ranked two pair. 
    If both hands have the same higher-ranked two pair, w then compare the lower-ranked two pair. 
    If both hands have the same two pairs (by value), we compare the kicker cards. 
    If the hands have the same value after comparing their kicker cards, they are equivalent.

    Params:
        hand_one: A tuple of five card objects, sorted in descending rank order.
        hand_two: A tuple of five card objects, sorted in descending rank order. 
    Returns:
        0 if the two hands have an exactly even poker value 
        1 if the first hand is greater
        2 if the second hand is greater  
    """
    if hand_one[0].value == hand_one[1].value and hand_one[2].value == hand_one[3].value:
        hand_one_first_pair = hand_one[0].value
        hand_one_second_pair = hand_one[2].value
        hand_one_kicker = hand_one[4].value
    elif hand_one[0].value == hand_one[1].value:
        hand_one_first_pair = hand_one[0].value
        hand_one_second_pair = hand_one[3].value
        hand_one_kicker = hand_one[2].value
    else:
        hand_one_first_pair = hand_one[1].value
        hand_one_second_pair = hand_one[3].value
        hand_one_kicker = hand_one[0].value

    if hand_two[0].value == hand_two[1].value and hand_two[2].value == hand_two[3].value:
        hand_two_first_pair = hand_two[0].value
        hand_two_second_pair = hand_two[2].value
        hand_two_kicker = hand_two[4].value
    elif hand_two[0].value == hand_two[1].value:
        hand_two_first_pair = hand_two[0].value
        hand_two_second_pair = hand_two[3].value
        hand_two_kicker = hand_two[2].value
    else:
        hand_two_first_pair = hand_two[1].value
        hand_two_second_pair = hand_two[3].value
        hand_two_kicker = hand_two[0].value

    if hand_one_first_pair > hand_two_first_pair:
        return 1
    elif hand_two_first_pair > hand_one_first_pair:
        return 2
    elif hand_one_second_pair > hand_two_second_pair:
        return 1
    elif hand_two_second_pair > hand_one_second_pair:
        return 2
    elif hand_one_kicker > hand_two_kicker:
        return 1
    elif hand_two_kicker > hand_one_kicker:
        return 2
    else:
        return 0


def break_tie_one_pair(hand_one, hand_two):
    """
    Given two hands that both contain a single pair, determine which has a higher poker value.
    The hand with the higher-valued pair is more valuable (i.e. a pair of tens is more valuable than 
    a pair of twos). 
    If both hands have the same value for their pair, we then compare the kicker cards, in descending 
    order of value, until we one hand has a higher-valued card than the other.
    If we compare all of the kicker cards and the hands are still equivalent, they are tied.

    Params:
        hand_one: A tuple of five card objects, sorted in descending rank order.
        hand_two: A tuple of five card objects, sorted in descending rank order. 
    Returns:
        0 if the two hands have an exactly even poker value 
        1 if the first hand is greater
        2 if the second hand is greater  
    """
    if hand_one[0].value == hand_one[1].value:
        hand_one_pair = hand_one[0].value
        hand_one_first_kicker = hand_one[2].value
        hand_one_second_kicker = hand_one[3].value
        hand_one_third_kicker = hand_one[4].value
    elif hand_one[1].value == hand_one[2].value:
        hand_one_pair = hand_one[1].value
        hand_one_first_kicker = hand_one[0].value
        hand_one_second_kicker = hand_one[3].value
        hand_one_third_kicker = hand_one[4].value
    elif hand_one[2].value == hand_one[3].value:
        hand_one_pair = hand_one[2].value
        hand_one_first_kicker = hand_one[0].value
        hand_one_second_kicker = hand_one[1].value
        hand_one_third_kicker = hand_one[4].value
    else:
        hand_one_pair = hand_one[3].value
        hand_one_first_kicker = hand_one[0].value
        hand_one_second_kicker = hand_one[1].value
        hand_one_third_kicker = hand_one[2].value
    
    if hand_two[0].value == hand_two[1].value:
        hand_two_pair = hand_two[0].value
        hand_two_first_kicker = hand_two[2].value
        hand_two_second_kicker = hand_two[3].value
        hand_two_third_kicker = hand_two[4].value
    elif hand_two[1].value == hand_two[2].value:
        hand_two_pair = hand_two[1].value
        hand_two_first_kicker = hand_two[0].value
        hand_two_second_kicker = hand_two[3].value
        hand_two_third_kicker = hand_two[4].value
    elif hand_two[2].value == hand_two[3].value:
        hand_two_pair = hand_two[2].value
        hand_two_first_kicker = hand_two[0].value
        hand_two_second_kicker = hand_two[1].value
        hand_two_third_kicker = hand_two[4].value
    else:
        hand_two_pair = hand_two[3].value
        hand_two_first_kicker = hand_two[0].value
        hand_two_second_kicker = hand_two[1].value
        hand_two_third_kicker = hand_two[2].value

    if hand_one_pair > hand_two_pair:
        return 1
    elif hand_two_pair > hand_one_pair:
        return 2
    elif hand_one_first_kicker > hand_two_first_kicker:
        return 1
    elif hand_two_first_kicker > hand_one_first_kicker:
        return 2
    elif hand_one_second_kicker > hand_two_second_kicker:
        return 1
    elif hand_two_second_kicker > hand_one_second_kicker:
        return 2
    elif hand_one_third_kicker > hand_two_third_kicker:
        return 1
    elif hand_two_third_kicker > hand_one_third_kicker:
        return 2
    else:
        return 0


def break_tie_high_card(hand_one, hand_two):
    """
    Given two hands that do not contain any poker patterns (no pairs, no straights, no flushes),
    we determine which has a higher value.
    The hand with the highest valued card is more valuable. If both of their high cards have
    the same value, we examine their second-highest valued cards  -- and so forth as necessary.
    If both hands contain the same set of five values,  they are equivalent.

    Params:
        hand_one: A tuple of five card objects, sorted in descending rank order.
        hand_two: A tuple of five card objects, sorted in descending rank order. 
    Returns:
        0 if the two hands have an exactly even poker value 
        1 if the first hand is greater
        2 if the second hand is greater  
    """
    for i in range(5):
        if hand_one[i].value > hand_two[i].value:
            return 1
        elif hand_two[i].value < hand_one[i].value:
            return 2
    
    return 0
