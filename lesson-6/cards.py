from random import shuffle
from collections import namedtuple


SuitView = namedtuple('SuitView', ['symbol', 'color'])

_regular_ranks = [6, 7, 8, 9, 10, 'JACK', 'QUEEN', 'KING', 'ACE']
_additional_ranks = [2, 3, 4, 5]
_all_ranks = _additional_ranks + _regular_ranks

_COLOR_RED = '\033[31m'
_COLOR_BLACK = '\033[30m'
_DEFAULT_COLOR = '\033[39m'


_suits = {
    'spades': SuitView(symbol='\u2660', color=_COLOR_RED),
    'hearts': SuitView(symbol='\u2665', color=_COLOR_RED),
    'diamonds': SuitView(symbol='\u2666', color=_COLOR_BLACK),
    'clubs': SuitView(symbol='\u2663', color=_COLOR_BLACK)
}


class Card:
    __slots__ = 'rank', 'suit'  # consume less memory

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return (f'{self.suit.color} {self.rank} '
                f'{self.suit.symbol}{_DEFAULT_COLOR}')

    def __repr__(self) -> str:
        return (f'{self.__class__.__name__}'
                f'(rank={self.rank!r}, suit={self.suit!r})')

    def __eq__(self, value):
        return self.rank == value.rank and self.suit == value.suit

    def __hash__(self) -> int:
        return hash(str(self.rank) + self.suit.symbol)


class BaseCardDeck:
    """
    It's muttable object
    Represent base logic for card deck.
    Can contains unlimited amount of cards
    Make sure you are using its children
    """
    __slots__ = '_cards', '_shufled'

    def __init__(self, ranks) -> None:
        self._cards = []

        self._shufled = False
        for rank in ranks:
            for suit in _suits:
                self._cards.append(Card(rank, _suits[suit]))

    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        self._cards = shuffle(self._cards)
        self._shufled = True

    def index(self, value):
        return self._cards.index(value)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __contains__(self, value):
        return value in self._cards

    def __sub__(self, value):
        try:
            self._cards.remove(value)
        except ValueError:
            raise ValueError('Card is not in a Deck')

        return self

    def __add__(self, value):
        if value in self._cards:
            raise ValueError(f'{value} already in card deck')

        self._cards.insert(0, value)
        return self

    def __eq__(self, value):
        if not isinstance(value, BaseCardDeck):
            return super().__eq__(value)

        if len(self) != len(value):
            return False

        diff = list(set(self.cards) - set(value.cards))
        return len(diff) == 0

    def __bool__(self):
        return len(self._cards) > 0 and self._shufled

    def __gt__(self, value):
        if not isinstance(value, BaseCardDeck):
            return super().__gt__(value)
        diff = list(set(self._cards) - set(value.cards))
        return len(diff) > 0

    def __lt__(self, value):
        if not isinstance(value, BaseCardDeck):
            return super().__lt__(value)

        diff = list(set(value._cards) - set(self.cards))
        return len(diff) > 0


class SmallDeck(BaseCardDeck):
    def __init__(self) -> None:
        super().__init__(_regular_ranks)


class ClassicDeck(BaseCardDeck):
    def __init__(self) -> None:
        super().__init__(_all_ranks)


if __name__ == '__main__':
    smallDeck = SmallDeck()
    classicDeck = ClassicDeck()
    print('Small card deck length: ', len(smallDeck))
    print('Classic card deck length: ', len(classicDeck))

    print()
    print('small deck\'s item #2 is', smallDeck[2])

    print()

    def check_if_card_in_deck(card, deck):
        state = 'contains' if card in deck else 'doesn\'t contain'
        print(f'{deck.__class__.__name__} {state} {card}')

    def show_card_position(card, deck):
        print(f'position of {card} in {deck.__class__.__name__} '
              f'is {deck.index(card)}')

    def check_card_deck_equal(deck1, deck2):
        res = "equal" if deck1 == deck2 else "not equal"
        print(f'{deck1.__class__.__name__} is {res}'
              f' to {deck2.__class__.__name__}')

    def remove_cards_from_deck(ranks, deck):
        for rank in ranks:
            for s in _suits:
                card = Card(rank=rank, suit=_suits[s])
                print(f'\t{card} removed')
                deck -= card

    def add_cards_to_deck(ranks, deck):
        for rank in ranks:
            for s in _suits:
                card = Card(rank=rank, suit=_suits[s])
                print(f'\t{card} added')
                deck += card

    fiveClubsCard = Card(5, _suits['clubs'])

    check_if_card_in_deck(fiveClubsCard, smallDeck)
    check_if_card_in_deck(fiveClubsCard, classicDeck)

    show_card_position(fiveClubsCard, classicDeck)

    print()
    print(f'Remove {fiveClubsCard} from {classicDeck.__class__.__name__}')
    classicDeck -= fiveClubsCard
    check_if_card_in_deck(fiveClubsCard, classicDeck)

    print(f'Remove {fiveClubsCard} again '
          f'from {classicDeck.__class__.__name__}')
    try:
        classicDeck -= fiveClubsCard
    except ValueError as e:
        print('Exception caught:', e)

    check_if_card_in_deck(fiveClubsCard, classicDeck)

    print()
    print(f'Add {fiveClubsCard} back to the {classicDeck.__class__.__name__}')
    classicDeck += fiveClubsCard
    check_if_card_in_deck(fiveClubsCard, classicDeck)

    show_card_position(fiveClubsCard, classicDeck)

    print()
    check_card_deck_equal(smallDeck, classicDeck)
    print('Now remove some of the cards '
          f'from {classicDeck.__class__.__name__}')

    remove_cards_from_deck(_additional_ranks, classicDeck)

    check_card_deck_equal(smallDeck, classicDeck)

    add_cards_to_deck(_additional_ranks, classicDeck)
    check_card_deck_equal(smallDeck, classicDeck)

    print()
    print(f'{smallDeck.__class__.__name__} > {classicDeck.__class__.__name__}',
          smallDeck > classicDeck)

    print(f'{classicDeck.__class__.__name__} > {smallDeck.__class__.__name__}',
          classicDeck > smallDeck)

    print(f'{smallDeck.__class__.__name__} < {classicDeck.__class__.__name__}',
          smallDeck < classicDeck)

    print(f'{classicDeck.__class__.__name__} < {smallDeck.__class__.__name__}',
          classicDeck < smallDeck)
    
    print(f'{smallDeck.__class__.__name__} <= {classicDeck.__class__.__name__}',
          smallDeck <= classicDeck)
