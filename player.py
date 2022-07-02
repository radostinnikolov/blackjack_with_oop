import random


class Player:
    __cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def __init__(self, has_bj=False):
        self.cards = []
        self.has_bj = has_bj

    def pick_a_card(self):
        card = random.choice(Player.__cards)
        if card == 11:
            self.cards.append(card)
            if self.current_score() > 21:
                self.cards.pop()
                self.cards.append(1)
        else:
            self.cards.append(card)
        print(f"Player picked {card}")

    def current_score(self):
        return sum(self.cards)

    def bj_checker(self):
        if sum(self.cards) == 21 and len(self.cards) == 2:
            self.has_bj = True