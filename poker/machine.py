# -*- coding: utf-8 -*-

from cards import CardUtils
import operator
import poker_hands


class PokerMachine(object):

    def __init__(self, hand, deck):
        self.hand = hand
        self.deck = deck

        self.hand_matrix = CardUtils.get_matrix(self.hand)
        self.full_matrix = CardUtils.get_matrix(self.hand + self.deck)

        self.win_hands = sorted([poker_hand() for poker_hand in poker_hands.poker_hands],
                                key=operator.methodcaller('rank'))

    def format_output(self, poker_hand_name):
        hand_repr = " ".join(str(card) for card in self.hand)
        deck_repr = " ".join(str(card) for card in self.deck)

        return "Hand: %s Deck: %s Best hand: %s" % (hand_repr, deck_repr, poker_hand_name)

    def play(self):
        for poker_hand in self.win_hands:
            if poker_hand.match(self.hand_matrix) or poker_hand.match(self.full_matrix):
                return self.format_output(str(poker_hand))

        return self.format_output("Game is lost")

