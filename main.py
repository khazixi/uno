import random
import enum
from typing import Union, Tuple, Optional

class Color(enum.Enum):
    RED = enum.auto()
    BLUE = enum.auto()
    GREEN = enum.auto()
    YELLOW = enum.auto()


class Card:
    def __init__(self, name, color) -> None:
        self._name = name
        self._color = color

    def get_color(self):
        return self._color

    def get_number(self) -> str:
        return self._name

class Stack:
    def __init__(self):
        self.stack: list[Card] = []

    def get_top(self) -> Card:
        return self.stack[-1]

    def add_stack(self, card: Card) -> bool:
        top_card = self.get_top()
        if top_card.get_color() == card.get_color():
            self.stack.append(card)
            return True
        elif top_card.get_number == card.get_number():
            self.stack.append(card)
            return True
        else:
            return False

class Deck:
    def __init__(self) -> None:
        self.deck: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.deck.append(card)

    def draw_card(self, amount: Optional[int] = 1) -> Tuple[Card, ...]:
        return tuple(self.deck.pop() for _ in range(amount))

class Player:
    def __init__(self) -> None:
        self.hand: list[Card] = []

    def add_card(self, cards: Tuple[Card]) -> None:
        if len(cards) == 1:
            self.hand.append(cards)
        else: 
            self.hand.extend(card for card in cards)

    def show_hand(self, card: Card) -> Tuple[Card, ...]:
        return tuple(card for card in self.hand)

    def use_card(self) -> Card:
        if len(self.hand) == 0:
            raise IndexError("Cannot Use Card if no card is in hand!")
        choice = int("Pick a number between 1~")
        return self.hand[choice]