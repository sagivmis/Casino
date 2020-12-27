import random
import cfg

class Color:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    # BG Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_WHITE = '\033[47m'


class Deck:

    def __init__(self):
        self.deck = []

        for suit in cfg.suits:
            for rank in cfg.ranks:
                self.deck.append(Card(cfg.values[rank], suit, cfg.colordict[suit]))
        random.shuffle(self.deck)

    def __str__(self):
        i = 0
        string = ""
        for _ in cfg.suits:
            string+='\n'
            for _ in cfg.ranks:
                string += f"{self.deck[i]},\t"
                i += 1
        return string

    def deck_len(self):
        count = 0
        for _ in self.deck:
            count += 1
        return count


class Card:
    def __init__(self, number=0, shape='none', color='none'):
        self.number = number
        self.shape = shape
        self.color = color

    def __str__(self):
        num = self.number
        if num == 13:
            num = 'K'
        if num == 12:
            num = 'Q'
        if num == 11:
            num = 'J'
        if num == 1:
            num = 'A'
        return f"{num} of {self.shape}s"

    def get_shape(self):
        if self.shape == 'Spade':
            return '♠'
        if self.shape == 'Diamond':
            return '♦'
        if self.shape == 'Heart':
            return '♥'
        if self.shape == 'Club':
            return '♣'

    def get_card(self):
        num = self.number
        if self.number > 10:
            if num == 13:
                num = 'K'
            if num == 12:
                num = 'Q'
            if num == 11:
                num = 'J'
            return num
        if num == 1:
            num = 'A'
        return num


class Player:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.cards = []
        self.total_cards = 0
        self.hand = Hand()
        self.bet = 0

    def __str__(self):
        return f"Player's name:{self.name}\nBalance:{self.balance}"

    def draw_card_from_deck(self, deck):
        x = deck.pop()
        self.cards.append(x)
        return x

    def cards_len(self):
        count = 0
        for i in self.cards:
            count += 1
        return count

    def get_balance(self):
        return self.balance

    def get_card(self, position):
        return self.cards[position]

    def set_balance(self, newbal):
        self.balance = newbal

    def add_to_balance(self, addition):  # addition*-1 for reduction
        self.balance += addition

    def reset_card_array(self):
        for i in range(self.cards_len()):
            self.cards.pop()

    def draw_random_card(self):
        x = random.randint(1, 13)
        shape = random.randint(1, 4)
        # cfg.colordict = {'Spade': 'Black', 'Club': 'Black', 'Heart': 'Red', 'Diamond': 'Red'}
        newcard = Card(x, cfg.shape_shift_from_number(shape), cfg.colordict[cfg.shape_shift_from_number(shape)])
        if newcard.number >= 11:
            newcard.number = 10
        self.cards.append(newcard)
        self.total_cards = self.cards_len()

    def new_bet(self):  # input by user of bet + remote check. the func will update the instance's balance.

        flag = False  # checking if bet is successful
        while not flag:
            print("How much would you like to bet?\n\n\t" + Color.BOLD + f"Your balance is currently {self.balance}"
                  + Color.END)
            bet_amount = int(input())
            check = cfg.check_bet(self.balance, bet_amount)
            if check > 0:
                flag = True
                self.balance -= bet_amount
                return bet_amount

    def lose(self, bet_amount):
        print(
            f"Im sorry :(\nYou lost {bet_amount} $, better luck next time!\n" + Color.RED + "Your current balance:" + Color.END,
            self.get_balance())

    def win(self, chips_won):
        self.add_to_balance(chips_won)
        print(Color.BOLD + Color.GREEN + "Congratulations!" + Color.END + f"\nYou have won {chips_won} $!!\n"
                                                                          f"Your balance is now {self.get_balance()}")

    def tie(self, bet):
        self.add_to_balance(bet)
        print(Color.BOLD + Color.YELLOW + "Tied !" + Color.END)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        self.total_cards = 0

    def add_card(self, card):
        if card.number >= 11:
            card.number = 10
        self.cards.append(card)
        self.total_cards = self.cards_len()

    def cards_len(self):
        count = 0
        for i in self.cards:
            count += 1
        return count

    def adjust_for_ace(self):
        if self.aces > 0:
            if self.value > 21:
                self.value -= 10

    def draw_card_from_deck(self, played_deck):
        temp_card=0
        if played_deck.deck_len() > 0:
            temp_card = played_deck.deck.pop()
            self.cards.append(temp_card)
        else:
            print("No more cards in deck")
        return temp_card

    def reset_hand_card_array(self):
        for i in range(self.cards_len()):
            self.cards.pop()


if __name__ == '__main__':
    cfg.main_menu()
