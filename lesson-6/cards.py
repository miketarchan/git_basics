import itertools
from enum import Enum
from collections import namedtuple


SuitView = namedtuple('SuitView',['symbol','color'])

_regular_ranks = [6, 7, 8, 9, 10, 'JACK', 'QUEEN', 'KING', 'ACE']
_additional_ranks = [ 2, 3, 4, 5]

_COLOR_RED = '\033[31m'
_COLOR_BLACK = '\033[30m'
_DEFAULT_COLOR = '\033[39m'

# or ranks = list(range(6, 10 + 1)) + list('JQKA')
_regular_suits = {
    'spades': SuitView(symbol='\u2660', color=_COLOR_RED),
    'hearts': SuitView(symbol='\u2665', color=_COLOR_RED),
    'diamonds': SuitView(symbol='\u2666', color=_COLOR_BLACK),
    'clubs': SuitView(symbol='\u2663', color=_COLOR_BLACK)
}

# class SuitEnum(Enum):
#     def __str__(cls):
#         return f'{cls.value}'
    
# Suit = SuitEnum('Suit', _regular_suits)


class Card:
    __slots__ = 'rank', 'suit' # consume less memory
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.suit.color} {self.rank} {self.suit.symbol}{_DEFAULT_COLOR}'

## ranks = [6, 7, 8, 9, 10]
## suits = ['clubs', 'spades', 'hearts', 'diamonds']
## itertools.product(ranks, suits)
# equivalent to:
##for r in ranks:
## for s in suits:
## print(f'{r} : {s}')

class CardDeckBase:

    def getCardList(self,ranks, suits):
        result=[]
        for r in range(len(ranks)):
            for s in suits:
                result.append(Card(ranks[r],suits[s]))

        return result

    # def __str__(self) -> str:
    #     pass
    


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