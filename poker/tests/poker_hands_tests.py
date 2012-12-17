# -*- coding: utf-8 -*-

from poker.cards import CardUtils
from poker.poker_hands import *
import unittest


class TestPokerHands(unittest.TestCase):
    def get_cards_matrix(self, str_cards):
        cards = str_cards.split(" ")
        cards = map(CardUtils.getCard, cards)
        return CardUtils.get_matrix(cards)

class TestStraightFlushHand(TestPokerHands):

    def test_exectly_match(self):
        cards = self.get_cards_matrix('QS JS TS 9S 8S')
        self.assertTrue(StraightFlushHand().match(cards))

        cards = self.get_cards_matrix('TS 9S 8S 7s 6s')
        self.assertTrue(StraightFlushHand().match(cards))

        cards = self.get_cards_matrix('5S 4S 3S 2s As')
        self.assertTrue(StraightFlushHand().match(cards))

    def test_match(self):
        cards = self.get_cards_matrix('3h QS JS 2d TS 9S 8S 7s')
        self.assertTrue(StraightFlushHand().match(cards))

        cards = self.get_cards_matrix('TS 9S Ad 5h 8S 7s 6s')
        self.assertTrue(StraightFlushHand().match(cards))

    def test_not_match(self):
        cards = self.get_cards_matrix('QS JC TS 9S 8S')
        self.assertFalse(StraightFlushHand().match(cards))

        cards = self.get_cards_matrix('TS 8S 7s 6s 5s')
        self.assertFalse(StraightFlushHand().match(cards))

        cards = self.get_cards_matrix('5S 4S 3S 2s Qs')
        self.assertFalse(StraightFlushHand().match(cards))

class TestFourOfKindHand(TestPokerHands):
    def test_exect_match(self):
        cards = self.get_cards_matrix('9s 9d 9h 9c Ah')
        self.assertTrue(FourOfKindHand().match(cards))

        cards = self.get_cards_matrix('3s 3d 9h 3c 3h')
        self.assertTrue(FourOfKindHand().match(cards))

    def test_match(self):
        cards = self.get_cards_matrix('9s 9d 9h 9c Ah 3d')
        self.assertTrue(FourOfKindHand().match(cards))

        cards = self.get_cards_matrix('3s 3d 9h 3c 3h 9c 9d')
        self.assertTrue(FourOfKindHand().match(cards))

    def test_not_match(self):
        cards = self.get_cards_matrix('9s 9c Ah 9d 8h')
        self.assertFalse(FourOfKindHand().match(cards))

class TestFullHouseHand(TestPokerHands):
    def test_exect_match(self):
        cards = self.get_cards_matrix('9s 9d 9h 7c 7h')
        self.assertTrue(FullHouseHand().match(cards))

        cards = self.get_cards_matrix('3s 3d 9h 3c 9c')
        self.assertTrue(FullHouseHand().match(cards))

    def test_match(self):
        cards = self.get_cards_matrix('9s 9d 9h 7c 7h 7d 7s')
        self.assertTrue(FullHouseHand().match(cards))

        cards = self.get_cards_matrix('3s 3d 9h 3c 9c kh kd ks ad as')
        self.assertTrue(FullHouseHand().match(cards))

    def test_not_match(self):
        cards = self.get_cards_matrix('9s 9c 9h 9d 8h')
        self.assertFalse(FullHouseHand().match(cards))

        cards = self.get_cards_matrix('Kh Qh Jh Th 9h')
        self.assertFalse(FullHouseHand().match(cards))

class TestFlushHand(TestPokerHands):
    def test_exectly_match(self):
        cards = self.get_cards_matrix('9s 2s As Qs Ts')
        self.assertTrue(FlushHand().match(cards))

        cards = self.get_cards_matrix('3h 4h Kh Qh Ah')
        self.assertTrue(FlushHand().match(cards))

    def test_match(self):
        cards = self.get_cards_matrix('Ad 9s 2h 2s As js Qh Qs Ts')
        self.assertTrue(FlushHand().match(cards))

    def test_not_match(self):
        cards = self.get_cards_matrix('3h 4h Kh Qh As')
        self.assertFalse(FlushHand().match(cards))

        cards = self.get_cards_matrix('3s 4h Kh Qh Ah')
        self.assertFalse(FlushHand().match(cards))

class TestStraightHand(TestPokerHands):
    def test_exectly_match(self):
        cards = self.get_cards_matrix('9s 6h 7d 8s 5h')
        self.assertTrue(StraightHand().match(cards))

        cards = self.get_cards_matrix('ah kd jh qs ts')
        self.assertTrue(StraightHand().match(cards))

        cards = self.get_cards_matrix('ah 2d 3h 4s 5s')
        self.assertTrue(StraightHand().match(cards))

    def test_match(self):
        cards = self.get_cards_matrix('9s 6h 6d 6s 7d 8s 5h')
        self.assertTrue(StraightHand().match(cards))

        cards = self.get_cards_matrix('ah kd jh qs ts 2d td')
        self.assertTrue(StraightHand().match(cards))

    def test_not_match(self):
        cards = self.get_cards_matrix('ah 2d jh qs ts')
        self.assertFalse(StraightHand().match(cards))

        cards = self.get_cards_matrix('ah 3d 4h 5s 6s')
        self.assertFalse(StraightHand().match(cards))


class TestThreeOfKindHand(TestPokerHands):
    def test_exect_match(self):
        cards = self.get_cards_matrix('9s 9h 9d Qs Tc')
        self.assertTrue(ThreeOfKindHand().match(cards))

        cards = self.get_cards_matrix('kh ks th 2h kd')
        self.assertTrue(ThreeOfKindHand().match(cards))

    def test_match(self):
        cards = self.get_cards_matrix('9s 9h 9d Qs Tc Qh Qd Th Ts')
        self.assertTrue(ThreeOfKindHand().match(cards))

        cards = self.get_cards_matrix('kh ks th 2h kd kc')
        self.assertTrue(ThreeOfKindHand().match(cards))

    def test_not_match(self):
        cards = self.get_cards_matrix('3h 3s Kh Qh As')
        self.assertFalse(ThreeOfKindHand().match(cards))

class TestTwoPairsHand(TestPokerHands):
    def test_exect_match(self):
        cards = self.get_cards_matrix('9s 9h Qd Qs Tc')
        self.assertTrue(TwoPairsHand().match(cards))

        cards = self.get_cards_matrix('kh Ks 2h 4h 2d')
        self.assertTrue(TwoPairsHand().match(cards))

    def test_match(self):
        cards = self.get_cards_matrix('9s 9h Qd Qs Tc Th jd js')
        self.assertTrue(TwoPairsHand().match(cards))

        cards = self.get_cards_matrix('kh Ks 2h 4h 2d As Ad Qh')
        self.assertTrue(TwoPairsHand().match(cards))

    def test_not_match(self):
        cards = self.get_cards_matrix('3h 3s Kh Qh As')
        self.assertFalse(TwoPairsHand().match(cards))

class TestOnePairHand(TestPokerHands):
    def test_exect_match(self):
        cards = self.get_cards_matrix('9s 9h Qd Ks Tc')
        self.assertTrue(OnePairHand().match(cards))

        cards = self.get_cards_matrix('kh Ks 2h 4h Ad')
        self.assertTrue(OnePairHand().match(cards))

    def test_match(self):
        cards = self.get_cards_matrix('9s 9h 9d Qd Ks Tc')
        self.assertTrue(OnePairHand().match(cards))

        cards = self.get_cards_matrix('kh Ks 2h 4h Ad Ah')
        self.assertTrue(OnePairHand().match(cards))

    def test_not_match(self):
        cards = self.get_cards_matrix('3h 2s Kh Qh As')
        self.assertFalse(OnePairHand().match(cards))

"""
class TestHighCardHand(TestPokerHands):
    def test_match(self):
        cards = self.get_cards_matrix('9s 6h Qd Ks Tc')
        self.assertTrue(HighCardHand().match(cards))

        cards = self.get_cards_matrix('kh js 2h 4h Ad')
        self.assertTrue(HighCardHand().match(cards))

    def test_not_match(self):
        cards = self.get_cards_matrix('3h 3s Kh Qh As')
        self.assertFalse(HighCardHand().match(cards))
"""