import itertools
from enum import Enum
from collections import namedtuple


SuitView = namedtuple('SuitView',['symbol','color'])

_regular_ranks = [6, 7, 8, 9, 10, 'JACK', 'QUEEN', 'KING', 'ACE']
_additional_ranks = [ 2, 3, 4, 5]

_COLOR_RED = '\033[31m'
_COLOR_BLACK = '\033[30m'
_DEFAULT_COLOR = '\033[39m'


_regular_suits = {
    'spades': SuitView(symbol='\u2660', color=_COLOR_RED),
    'hearts': SuitView(symbol='\u2665', color=_COLOR_RED),
    'diamonds': SuitView(symbol='\u2666', color=_COLOR_BLACK),
    'clubs': SuitView(symbol='\u2663', color=_COLOR_BLACK)
}

class Card:
    __slots__ = 'rank', 'suit' # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.suit.color} {self.rank} {self.suit.symbol}{_DEFAULT_COLOR}'


class CardDeckBase:
    """Represent base logic for card deck"""
    
    def getCardList(self,ranks, suits):
        result=[]
        for r in range(len(ranks)):
            for s in suits:
                result.append(Card(ranks[r],suits[s]))

        return result


class RussianCardDeck(CardDeckBase):
    
    @property
    def cards(self):
        return super().getCardList(_regular_ranks,_regular_suits)

class FrenchCardDeck(CardDeckBase):

    @property
    def cards(self):
        return super().getCardList(_additional_ranks + _regular_ranks , _regular_suits)

if __name__ == '__main__':
    pass