# -*- coding: utf-8 -*-

import numpy

class PokerHandsMatcher(object):
    
    def get_suits_mask(self, cards_matrix):
        return numpy.sum(cards_matrix, axis=1)
    
    def get_values_mask(self, cards_matrix):
        return numpy.sum(cards_matrix, axis=0)
    
    def match_by_values(self, cards_matrix, expected):
        expected = sorted(expected, reverse=True)
        sorted_cards_values = sorted(self.get_values_mask(cards_matrix), reverse=True)
        
        for expected_suit_size, suit_size in zip(expected, sorted_cards_values):
            if expected_suit_size > suit_size:
                return False                 
            
        return True
    
class SequenceMatcher(PokerHandsMatcher):
    def _extract_sequence(self, suit, without_breaks, sequence_size):
        sequence_block = None
        sequence = []
        
        for index, item in enumerate(suit):
            if item and not sequence_block:
                sequence_block = list()
                sequence.append(sequence_block)
                
            if item and sequence_block is not None:
                sequence_block.append(index)
                
            if item == 0 and sequence_block:
                sequence_block = None

        # if 'A' & 'K' => union A to royal sequence 
        if suit[0] and suit[-1]:
            sequence[-1].append(0)
            #sequence.pop(0)
        
        if without_breaks:
            return [sequence_item for sequence_item in sequence if len(sequence_item) >= sequence_size]
          
        return sequence

    def match_by_sequence(self, cards_matrix, without_breaks=True, sequence_size=5):
        cards_values_mask = self.get_values_mask(cards_matrix)
        if len([sum_per_suite for sum_per_suite in cards_values_mask if sum_per_suite != 0]) < sequence_size:
            return False
        
        sequence = self._extract_sequence(cards_values_mask, without_breaks, sequence_size)
        return True if sequence else False
    
class SuitSequenceMatcher(SequenceMatcher):
    def _get_sequence_suit_id(self, cards_matrix, sequence_size=5):
        """
        detect suit where's sequence can be located
        """
        
        suit_index = None
        
        for index, suit_size in enumerate(self.get_suits_mask(cards_matrix)):
            if suit_size >= sequence_size:
                suit_index = index
                break 
        
        return suit_index

    def match_by_sequence(self, cards_matrix, without_breaks=True, sequence_size=5):
        suit_id = self._get_sequence_suit_id(cards_matrix, sequence_size)
        
        if not suit_id:
            return False
        
        sequence = self._extract_sequence(cards_matrix[suit_id], without_breaks, sequence_size)        
        return True if sequence else False

class FactoryMatcher(object):
    @staticmethod
    def get_values_matcher():
        return PokerHandsMatcher()
    
    @staticmethod
    def get_sequence_matcher(same_suit=False):
        return SuitSequenceMatcher() if same_suit else SequenceMatcher()
