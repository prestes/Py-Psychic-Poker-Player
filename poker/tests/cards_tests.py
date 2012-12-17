# -*- coding: utf-8 -*-

from poker.cards import CardUtils, Card
import unittest

class TestCardUtils(unittest.TestCase):
    # SUITES = "CDHS"
    
    def test_valid_suites(self):
        self.assertEquals(CardUtils.getCard("2c"), Card("2", "C"))
        self.assertEquals(CardUtils.getCard("2C"), Card("2", "C"))
        
        self.assertEquals(CardUtils.getCard("2D"), Card("2", "D"))
        self.assertEquals(CardUtils.getCard("2d"), Card("2", "D"))

        self.assertEquals(CardUtils.getCard("2h"), Card("2", "H"))
        
        self.assertEquals(CardUtils.getCard("2S"), Card("2", "S"))

    
    def test_valid_cards(self):
        self.assertEquals(CardUtils.getCard("2s"), Card("2", "S"))
        self.assertEquals(CardUtils.getCard("ah"), Card("A", "H"))
        self.assertEquals(CardUtils.getCard("aH"), Card("A", "H"))
        self.assertEquals(CardUtils.getCard("AH"), Card("A", "H"))
        self.assertEquals(CardUtils.getCard("KD"), Card("K", "D"))
        
        
    def test_invalid_cards(self):
        self.assertRaises(AssertionError, CardUtils.getCard, "1s")
        self.assertRaises(AssertionError, CardUtils.getCard, "10s")
        self.assertRaises(AssertionError, CardUtils.getCard, "3g")
        self.assertRaises(AssertionError, CardUtils.getCard, "12h")
