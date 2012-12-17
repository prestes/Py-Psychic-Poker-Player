# -*- coding: utf-8 -*-

from cards import CardUtils
from machine import PokerMachine


def main(poker_data):
    try:
        with open(poker_data, 'r') as f:
            data = f.readlines()
    except IOError:
        print "Error. File %s doesn't exist" % poker_data
    else:
        for line in data:
            cards = line.replace("\n", "").split(" ")

            if cards:
                hand = map(CardUtils.getCard, cards[0:5])
                deck = map(CardUtils.getCard, cards[5:10])

                print PokerMachine(hand=hand, deck=deck).play()

if __name__ == "__main__":
    main("../poker.in")
