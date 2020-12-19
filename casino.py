import random

from tictactoe import run_tictactoe_game


class color:
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
        self.totalcards = 0

    def __str__(self):
        return f"Player's name:{self.name}\nBalance:{self.balance}"

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

    def draw_card(self):
        x = random.randint(1, 13)
        shape = random.randint(1, 4)
        colordict = {'Spade': 'Black', 'Club': 'Black', 'Heart': 'Red', 'Diamond': 'Red'}
        newcard = Card(x, shape_shift(shape), colordict[shape_shift(shape)])
        if newcard.number >= 11:
            newcard.number = 10
        self.cards.append(newcard)
        self.totalcards = self.cards_len()

    def new_bet(self):  # input by user of bet + remote check. the func will update the instance's balance.

        flag = False  # checking if bet is successful
        while not flag:
            print("How much would you like to bet?\n\n\t" + color.BOLD + f"Your balance is currently {self.balance}"
                  + color.END)
            bet_amount = int(input())
            check = check_bet(self.balance, bet_amount)
            if check > 0:
                flag = True
                self.balance -= bet_amount
                return bet_amount


def shape_shift(shape):
    """
    :param shape:
    :type shape:
    :return:
    :rtype:
    1 for Hearts , 2 Spades, 3 Diamonds, 4 Clubs
    """

    shapes = {
        1: 'Heart',
        2: 'Spade',
        3: 'Diamond',
        4: 'Club'
    }

    return shapes[shape]


def build_deck_n_shuffle():  # working
    deck = []
    colordict = {'Spade': 'Black', 'Club': 'Black', 'Heart': 'Red', 'Diamond': 'Red'}
    for shape in range(1, 5):
        for card in range(1, 14):
            newcard = Card(card, shape_shift(shape), colordict[shape_shift(shape)])
            deck.append(newcard)
            print(newcard)
    random.shuffle(deck)
    print("Successfuly shuffled new deck.")
    return deck


def sum_list(l):
    total = 0
    for val in l:
        total += val
    return total


def check_war(player, dealer):
    if player > dealer:
        return True
    else:
        return False


def sum_cards(cards):
    sum = 0
    for i in cards:
        sum += i.number
    return sum


def count_cards(cards):
    count = 0
    for _ in cards:
        count += 1
    return count


def draw_dealer(dealer, cards, sumofcards):
    print("Generating cards for dealer.......... (must hit at-least 17)")
    while sumofcards < 17:
        dealer.draw_card()
        sumofcards = sum_cards(dealer.cards)
    return


def check_bet(balance, bet):  # checks if the bet is legit (=not higher than balance, can be equal to)
    # and if so returns True
    if bet > balance:
        print(f"Bet can't exceed max balance.\n please re-enter your bet. Your current balance is {balance}")
    else:
        return bet
    return 0


def lose(player, betAmount):
    print(
        f"Im sorry :(\nYou lost {betAmount}, better luck next time!\n" + color.RED + "Your current balance:" + color.END,
        player.get_balance())


def win(player, chips_won):
    player.add_to_balance(chips_won)
    print(color.BOLD + color.GREEN + "Congratulations!" + color.END + f"\nYou have won {chips_won}.\n"
                                                                      f"And your balance is now {player.get_balance()}")


def tie(player, bet):
    player.add_to_balance(bet)
    print(color.BOLD + color.YELLOW + "Tied !" + color.END)


def game_pick():  # inputs what game player wants to play
    print(
        "Pick game:" + color.BOLD + "\n\t1. War\n\t2. Roullette\n\t3. BlackJack\n\n\t4.Tic Tac Toe (friendly game)\n\n\t9. Exit" + color.END)
    game = int(input())
    return game


def check_BJ(player, dealer):  # true for player win false for dealer's win
    if dealer > 21:
        return True
    if player > 21:
        return False
    if player > dealer:
        return True
    else:
        return False


def show_card(card):
    if card.color == 'Red':
        if card.get_card() == 10:
            print(
                color.RED + f" -----\n|\t{card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  |\n|{card.get_card()}\t  |\n -----" + color.END)
        else:
            print(
                color.RED + f" -----\n|\t {card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  |\n|{card.get_card()}\t  |\n -----" + color.END)
    else:
        if card.get_card() == 10:
            print(
                f" -----\n|\t{card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  |\n|{card.get_card()}\t  |\n -----")
        else:
            print(
                f" -----\n|\t {card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  |\n|{card.get_card()}\t  |\n -----")
    return card.shape


card = 0
oppcard = 0
name = input("Input your name")
newplayer = Player(name, 100)
opponent = Player("OP", 9999999)
game_picked_by_player = game_pick()

if __name__ == '__main__':
    while game_picked_by_player != 9:
        if game_picked_by_player == 18:
            deck = build_deck_n_shuffle()
            for i in range(len(deck)):
                show_card(deck[i])
                print("*" * 15)
            # print(deck[i], end=" , ")
            game_picked_by_player = game_pick()
        if game_picked_by_player == 4:
            run_tictactoe_game()
            game_picked_by_player = game_pick()
        if game_picked_by_player == 1:
            print("WELCOME TO WAR \nstart game? \n\t1=Yes \n\t2=No")
            startGame = int(input())
            while startGame == 1:
                bet = newplayer.new_bet()
                card = Card(random.randint(1, 13), shape_shift(random.randint(1, 4)))
                print(f"Your card: ", color.BOLD + show_card(card) + color.END)
                oppcard = Card(random.randint(1, 13), shape_shift(random.randint(1, 4)))
                print(f"Opponent's card: ", color.BOLD + show_card(oppcard) + color.END)
                if card.number < oppcard.number:
                    lose(newplayer, bet)
                    print("\nanother game?\n1=Yes\n2=No")
                    startGame = int(input())
                elif card.number == oppcard.number:
                    tie(newplayer, bet)
                    print("Another game?\n\t1=Yes\n\t2=No")
                    startGame = int(input())
                else:
                    win(newplayer, bet * 2)
                    print("\nanother game?\n1=Yes\n2=No")
                    startGame = int(input())
            game_picked_by_player = game_pick()
        if game_picked_by_player == 2:
            print(color.BOLD+"WELCOME TO ROULETTE"+color.END)
            randInt = random.randint(1, 36)
            print("Pick your choice \n\t1.(Numbers 1-36)\n\t2.(Colors)\n\n\t9.Exit")
            choice = int(input())
            if choice == 1:
                betAmount = [0]
                playerBet = [0]
                print("Enter the number to bet on (1-36):")
                playerBet[0] = int(input())
                if playerBet[0] == 99:  # for check. 99 for an array that will win.
                    playerBet = list(range(37))
                betAmount[0] = newplayer.new_bet()
                print("Another bet? \n\t", color.BOLD + color.GREEN + "1-Yes" + color.END,
                      color.BOLD + color.RED + "\n\t2-No" + color.END)
                anotherbet = int(input())
                while anotherbet == 1:
                    print("On what number? 1-36")
                    x = int(input())
                    playerBet.append(x)
                    x = newplayer.new_bet()
                    betAmount.append(x)
                    print("Another bet? \n\t", color.BOLD + color.GREEN + "1-Yes" + color.END,
                          color.BOLD + color.RED + "\n\t2-No" + color.END)
                    anotherbet = int(input())
                index_solution = 0
                betAmountSum = sum_list(betAmount)
                isItIn = randInt in playerBet
                if isItIn:
                    index_solution = playerBet.index(randInt)
                    if playerBet == list(range(37)):
                        betAmount = list([10] * 37)  # inputs 10 as a bet for all 'tries' - also, a check
                    print(color.BOLD + color.GREEN + f"the number is....{randInt}" + color.END)
                    win(newplayer, (betAmount[index_solution]) * 36)
                else:
                    print(color.BOLD + color.RED + f"the number is....{randInt}\n" + color.END)
                    lose(newplayer, betAmountSum)

            if choice == 2:
                print("What color would you like to bet on?\n\t1-Black\n\t2-Red")
                playerBet = int(input())
                betAmount = newplayer.new_bet()
                color_result = random.randint(1, 2)
                colordict= {
                    1: 'Black',
                    2: 'Red'
                }
                if playerBet == color_result:
                    win(newplayer, betAmount * 2)
                else:
                    lose(newplayer, betAmount)
            if choice == 9:
                game_picked_by_player = game_pick()
                continue
        if game_picked_by_player == 3:
            print(color.BOLD+"WELCOME TO BLACK JACK"+color.END)
            newplayer.draw_card()
            newplayer.draw_card()
            betAmount = newplayer.new_bet()
            cardsSum = sum_cards(newplayer.cards)  # player's total
            print(f"Your cards are: {newplayer.get_card(0)}, {newplayer.get_card(1)} \nSum of cards:\t {cardsSum}\n")
            opponent.draw_card()
            opponent.draw_card()
            oppSum = sum_cards(opponent.cards)  # dealer's total
            print(f"Dealer cards are:{opponent.get_card(0)}, {opponent.get_card(1)} \n"
                  f"And the sum of the dealer's cards are:{oppSum} \n\nAnother card?", color.BOLD + color.GREEN +
                  "\n\t1-Yes" + color.END, color.BOLD + color.RED + "\n\t2-No" + color.END)
            if oppSum < 17:
                draw_dealer(opponent, opponent.cards, oppSum)
                oppSum = sum_cards(opponent.cards)
                print("Dealer has drawn more cards. New total sum of dealer's cards is: ", oppSum)
            anotherCard = int(input())
            while anotherCard == 1 and cardsSum < 22:
                newplayer.draw_card()
                cardsSum = sum_cards(newplayer.cards)
                print(f"Next cards is: {newplayer.cards[len(newplayer.cards) - 1]} and the total sum is {cardsSum}\n"
                      f"Another card?\n\t", color.BOLD + color.GREEN + "1-Yes" + color.END, color.BOLD + color.RED +
                      "\n\t2-No" + color.END)
                anotherCard = int(input())
            if cardsSum > 21:
                print("BURNT!")
            win_check = check_BJ(cardsSum, oppSum)
            if win_check:
                if newplayer.cards_len() == 2 and cardsSum == 21:
                    betAmount = int(betAmount * 1.5)
                    print(color.BG_WHITE + color.RED + "BJ!!!" + color.END)
                win(newplayer, betAmount * 2)
            else:
                lose(newplayer, betAmount)
            print("Another game?", color.BOLD + color.GREEN + "\n\t1-Yes" + color.END,
                  color.BOLD + color.RED + "\n\t2-No" + color.END)
            anotherBJ = int(input())
            newplayer.reset_card_array()
            opponent.reset_card_array()
            if anotherBJ == 2:
                game_picked_by_player = game_pick()
    if game_picked_by_player == 9:
        print(color.BOLD + color.RED + f"Your end balance: {newplayer.get_balance()}\nGoodbye {newplayer.name}."
              + color.END)
