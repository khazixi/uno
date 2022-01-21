import random
import enum
from typing import Union, Tuple, Optional


"""
This is a simple project that I have made to test my skills in python.
I have not made a completed project in python in a long time so this seemed like a good oppurtunity
The logic is simple and the game can be refactored to become extensible
"""

# TODO: Add Color Changer Cards
# TODO: Add Skip and Reverse Cards
# TODO: Add Draw Cards
# TODO: Create graphics for the game

class Color(enum.Enum):  # Enum is used to assign colors 
    RED = enum.auto()
    BLUE = enum.auto()
    GREEN = enum.auto()
    YELLOW = enum.auto()


class Card:
    def __init__(self, number, color) -> None:
        self._name = number
        self._color = color

    def get_color(self):
        return self._color

    def get_number(self) -> str:
        return self._number

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

    def add_card(self, cards: Tuple[Card] | Card) -> None:
        if type(cards) is tuple:
            self.hand.extend(card for card in cards)
        elif type(cards) is Card:
            self.hand.append(cards)

    def show_hand(self, card: Card) -> Tuple[Card, ...]:
        return tuple(card for card in self.hand)

    def use_card(self) -> Card:
        if len(self.hand) == 0:
            raise IndexError("Cannot Use Card if no card is in hand!")
        choice = int("Pick a number between 1~")
        return self.hand[choice]


class Game:
    def __init__(self):
        self.deck = Deck()
        self.stack = Stack()
        self.player_list: list[Player] = []
        # Initializer functions will be added to __init__
        self.create_players()
        self.initialize_stack()
        self.create_players()

    ###### GAME INITIALIZER FUNCTIONS ######

    def create_cards(self):
        for color in Color:
            for number in range(10):
                for _ in range(2):
                    self.deck.add_card(Card(number, color))

    def initialize_stack(self):
        random.shuffle(self.deck)
        card = random.choice(self.deck)
        self.stack.add_stack(card)

    def create_players(self):
        while True:
            choice = input("How many players would like to play?")
            if choice.isnumeric() and 0 < int(choice) < 8:
                self.player_list.extend(Player() for _ in range(int(choice)))
                for player in self.player_list:
                    player.add_card(self.deck.draw_card(5))
                break

    ###### GAME LOGIC FUNCTIONS ######
    def check_hand(self, player: Player, stack_card: Card) -> list[bool]:
        bool_chain = []
        for card in player.hand:
            if stack_card.get_color() == card.get_color():
                bool_chain.append(True)
            elif stack_card.get_number == card.get_number():
                bool_chain.append(True)
            else:
                bool_chain.append(False)

        return bool_chain

    
    def check_card(self, card: Card, stack_card: Card) -> bool:
        if card.get_color() == stack_card.get_color():
            return True
        elif card.get_color() == stack_card.get_color():
            return True
        else:
            return False
        
    ###### THE FUNCTION THAT RUNS THE ACTUAL GAME ######
    def run(self):  # This is where the game logic will occur!
        while True:
            for player in self.player_list:
                stack_card = self.stack.get_top()
                while True:
                    if any(self.check_hand(player, stack_card)):
                        player_card = player.use_card()
                        if self.check_card(player_card, stack_card):
                            self.stack.add_stack(player_card)
                            break
                        else:
                            # This returns the card to hand if it cannot be placed on the top stack card
                            player.add_card(player_card)
                        # This is meant to check if the player's hand is empty and then they win
                        if not player.show_hand():
                            winner = player
                            break
                    else:
                        player.add_card(self.deck.draw_card()) 


if __name__ == "__main__":
    uno = Game()
    uno.run()