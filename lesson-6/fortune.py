from cards import SmallDeck, ClassicDeck
from random import randrange


_attempts = 4


def _print_cards(cards):
    used_idx = []

    def attemp():
        rand_number = randrange(len(cards))
        if rand_number not in used_idx:
            print(f'{cards[rand_number]}', end=" ")
            used_idx.append(rand_number)
        else:
            attemp()

    for i in range(_attempts):
        attemp()

    print()


print("Your Franch's deck fortune:")
_print_cards(ClassicDeck().cards)

print("Your Russion's deck fortune:")
_print_cards(SmallDeck().cards)
