# -*- coding: utf-8 -*-

import numpy
import re


class CardUtils(object):
    
    SUITS_NUM = 4
    CARD_TYPES = 13
    
    VALUES = {'A' : 1 , 'T' : 10, 'J' : 11, 'Q' : 12 , 'K' : 13}
    SUITES = "CDHS"
    
    @staticmethod
    def toInternalValue(val):
        """
        '-1' - normalization to 0-index
        """
        return (CardUtils.VALUES.get(val) or int(val)) - 1
    
    @staticmethod
    def toInternalSuite(suite):
        return CardUtils.SUITES.index(suite)
    
    @staticmethod
    def getCard(value):
        assert len(value) == 2, "Wrong card format: '%s'" % value
        
        value = value.upper()        
        card_value, suit = value[0], value[1]
        
        assert re.match("^[CDHS]$", suit), "Wrong suit type: '%s'" % suit
        assert re.match("^[2-9ATJQK]$", card_value), "Wrong card value: '%s'" % card_value
        
        return Card(card_value, suit)
        
    @staticmethod
    def get_matrix(cards):
        cards_matrix = numpy.zeros((CardUtils.SUITS_NUM, CardUtils.CARD_TYPES), dtype=numpy.int)
        
        for card in cards:
            cards_matrix[card.suit()][card.value()] = 1
        
        return cards_matrix
    
class Card(object):
    def __init__(self, value, suit):
        self._value = value 
        self._internal_val = CardUtils.toInternalValue(value)
        
        self._suit = suit
        self._internal_suit = CardUtils.toInternalSuite(suit)
        
    def value(self):
        return self._internal_val
    
    def suit(self):
        return self._internal_suit
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return "%s%s" % (self._value, self._suit)
    
    def __eq__(self, obj): 
        return self.__dict__ == obj.__dict__
