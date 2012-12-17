# -*- coding: utf-8 -*-

from abc import abstractmethod
from hands_matchers import FactoryMatcher


__all__ = ["StraightFlushHand",
           "FourOfKindHand",
           "FullHouseHand",
           "FlushHand",
           "StraightHand",
           "ThreeOfKindHand",
           "TwoPairsHand",
           "OnePairHand",
           "HighCardHand"]


class PokerHands(object):

    @abstractmethod
    def match(self, cards_matrix):
        pass

    @abstractmethod
    def rank(self):
        pass

    def match_by_sequence(self, cards_matrix, same_suit=False, without_breaks=True, sequence_size=5):
        return FactoryMatcher.get_sequence_matcher(same_suit).\
            match_by_sequence(cards_matrix, without_breaks, sequence_size)

    def match_by_values(self, cards_matrix, expected):
        return FactoryMatcher.get_values_matcher().match_by_values(cards_matrix, expected)


class AbstractExpectedHand(PokerHands):
    """
    self.expected - tuple with expected cards value
    """

    def match(self, cards_matrix):
        return self.match_by_values(cards_matrix, self.expected)


class StraightFlushHand(PokerHands):
    """
    straight flush
    contains five cards in sequence, all of the same suit
    Q♣ J♣ 10♣ 9♣ 8♣
    """

    def match(self, cards_matrix):
        return self.match_by_sequence(cards_matrix, same_suit=True, without_breaks=True)

    def __repr__(self):
        return "straight-flush"

    def rank(self):
        return 1


class FourOfKindHand(AbstractExpectedHand):
    """
    Four of a kind
    contains all four cards of one rank and any other (unmatched) card
    9♣ 9♠ 9♦ 9♥ J♥
    7♣ 7♠ 7♦ 7♥ 10♣
    """
    expected = (4, 1)

    def __repr__(self):
        return "four-of-a-kind"

    def rank(self):
        return 2


class FullHouseHand(AbstractExpectedHand):
    """
    Full house
    contains three matching cards of one rank and two matching cards of another rank
    7♠ 7♥ 7♦ 4♠ 4♣
    6♠ 6♥ 6♦ A♠ A♣
    """
    expected = (3, 2)

    def __repr__(self):
        return "full-house"

    def rank(self):
        return 3


class FlushHand(PokerHands):
    """
    Flush
    all five cards are of the same suit, but not in sequence
    Q♣ 10♣ 7♣ 6♣ 4♣
    """

    def match(self, cards_matrix):
        return self.match_by_sequence(cards_matrix, same_suit=True, without_breaks=False)

    def __repr__(self):
        return "flush"

    def rank(self):
        return 4


class StraightHand(PokerHands):
    """
    contains five cards of sequential rank in at least two different suits
    Q♣ J♠ 10♠ 9♥ 8♥
    A♣ K♣ Q♦ J♠ 10♠
    """

    def match(self, cards_matrix):
        return self.match_by_sequence(cards_matrix, same_suit=False, without_breaks=True)

    def __repr__(self):
        return "straight"

    def rank(self):
        return 5


class ThreeOfKindHand(AbstractExpectedHand):
    """
    Three of a kind
    contains three cards of the same rank, plus two cards
    which are not of this rank nor the same as each other
    2♦ 2♠ 2♣ K♠ 6♥
    J♠ J♣ J♦ A♦ K♣
    """
    expected = (3, 1, 1)

    def __repr__(self):
        return "three-of-a-kind"

    def rank(self):
        return 6


class TwoPairsHand(AbstractExpectedHand):
    """
    Two pairs
    contains two cards of the same rank, plus two cards of another rank
    (that match each other but not the first pair), plus any card not of either rank
    J♥ J♣ 4♣ 4♠ 9♥
    10♠ 10♣ 8♥ 8♣ 4♠
    """

    expected = (2, 2, 1)

    def __repr__(self):
        return "two-pairs"

    def rank(self):
        return 7


class OnePairHand(AbstractExpectedHand):
    """
    One pair
    contains two cards of one rank, plus three cards
    which are not of this rank nor the same as each other
    4♥ 4♠ K♠ 10♦ 5♠
    """

    expected = (2, 1, 1, 1)

    def __repr__(self):
        return "one-pair"

    def rank(self):
        return 8


class HighCardHand(PokerHands):
    """
    High card
    made of any five cards not meeting any of the above requirements.
    Essentially, no hand is made, and the only thing of any potential meaning in the hand is the highest card.
    K♥ J♥ 8♣ 7♦ 4♠
    7♠ 5♣ 4♦ 3♦ 2♣
    """

    def match(self, cards_matrix):
        return True # self.match_by_sequence(cards_matrix, same_suit=False, without_breaks=False)

    def __repr__(self):
        return "highest-card"

    def rank(self):
        return 9


poker_hands = (StraightFlushHand,
             FourOfKindHand,
             FullHouseHand,
             FlushHand,
             StraightHand,
             ThreeOfKindHand,
             TwoPairsHand,
             OnePairHand,
             HighCardHand)
