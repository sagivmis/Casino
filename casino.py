import random

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


class Card():
    def __init__(self, number=0, shape='none'):
        self.number = number
        self.shape = shape

    def __str__(self):
        return f"{self.number} of {self.shape}s"

    def get_card(self):
        return self.number


class Player():

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.cards = []
        self.totalcards = 0

    def __str__(self):
        return f"Player's name:{self.name}\nBalance:{self.balance}"

    def cards_len(self):
        count =0
        for i in self.cards:
            count+=1
        return count

    def get_balance(self):
        return self.balance

    def get_card(self, position):
        return self.cards[position]

    def get_name(self):
        return self.name

    def set_balance(self, newbal):
        self.balance = newbal

    def reset_card_array(self):
        for i in range(self.cards_len()):
                self.cards.pop()

    def draw_card(self):
        x = random.randint(1, 13)
        shape = random.randint(1, 4)
        if shape == 1:
            shape = 'Heart'
        if shape == 2:
            shape = 'Spade'
        if shape == 3:
            shape = 'Diamond'
        if shape == 4:
            shape = 'Club'
        x = Card(x, shape)
        if x.number > 11:
            x.number = 10
        self.cards.append(x)
        self.totalcards+=1

    def new_bet(self):  # input by user of bet + remote check. the func will return legit bet,

        flag = False  # checking if bet is successful
        print("How much would you like to bet?\n\n\t" + color.BOLD + f"Your balance is currently {self.balance}" + color.END)
        betAmount = int(input())
        while flag == False:  # but doesnt add the bet to history.
            check = check_bet(self.balance, betAmount)
            if check > 0:
                flag = True
                self.balance -= betAmount
                return betAmount
            else:
                betAmount = new_bet(self.balance)


def build_deck_n_shuffle(self):
    deck = []
    for shape in range(4):
        for card in range(1, 14):
            deck.append(card)
            print(card)
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
    while sumofcards < 17:
        dealer.draw_card()
        sumofcards = sum_cards(dealer.cards)
    return


def deck_full(deck):
    count = 0
    for i in deck:
        if deck[i] != 0:
            count += 1
    if count == 52:
        return True
    else:
        return False


def new_bet(balance):  # input by user of bet + remote check. the func will return legit bet,

    flag = False  # checking if bet is successful
    print("How much would you like to bet?\n\n\t" + color.BOLD + f"Your balance is currently {balance}" + color.END)
    betAmount = int(input())
    while flag == False:  # but doesnt add the bet to history.
        check = check_bet(balance, betAmount)
        if check > 0:
            flag = True
            balance -= betAmount
            return betAmount
        else:
            betAmount = new_bet(balance)


def check_bet(balance, bet):  # checks if the bet is legit (=not higher than balance, can be equal to)
    # and if so returns True
    if bet > balance:
        print(f"Bet can't exceed max balance.\n please re-enter your bet. Your current balance is {balance}")
    else:
        return bet
    return 0


def draw_card(cards):
    x = random.randint(1, 13)
    shape = random.randint(1, 4)
    if shape == 1:
        shape = 'Heart'
    if shape == 2:
        shape = 'Spade'
    if shape == 3:
        shape = 'Diamond'
    if shape == 4:
        shape = 'Club'
    x = Card(x, shape)
    if x.number > 11:
        x.number = 10
    cards.append(x)


def game_pick():  # inputs what game player wants to play
    print("Pick game:" + color.BOLD + "\n\t1. War\n\t2. Roullette\n\t3. BlackJack\n\n\t4.Tic Tac Toe (friendly game)\n\n\t9. Exit" + color.END)
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




card = 0
oppcard = 0
name = input("Input your name")
newplayer = Player(name, 100)
opponent = Player("OP", 9999999)
gamePick = game_pick()

while gamePick != 9:
    if gamePick == 4:
        import tictactoe
        gamePick = game_pick()
    if gamePick == 1:
        #bet = new_bet(newplayer.get_balance())
        print("start game? \n1=Yes \n2=No")
        startGame = int(input())
        while startGame == 1:
            bet = newplayer.new_bet()
            print("Your card:")
            card = random.randint(1, 13)
            print(card)
            oppcard = random.randint(1, 13)
            print("Opponent's card:\n", oppcard)
            if card < oppcard:
                print(color.BOLD + color.RED + "You lost", bet, "from balance." + color.END)
               # newplayer.set_balance(newplayer.get_balance() - bet)
                print("New balance:", newplayer.get_balance())
                print("another game?\n1=Yes\n2=No")
                startGame = int(input())
            elif card == oppcard:
                print(color.BOLD + color.YELLOW + "Tied !" + color.END + "\n Another game?\n\t1=Yes\n\t2=No")
                newplayer.set_balance(newplayer.get_balance() + bet)
                startGame = int(input())
            else:
                newplayer.set_balance(newplayer.get_balance() + bet*2)
                print(color.BOLD + color.GREEN + "You win", bet, "!!" + color.END + "\nNew balance:",
                      newplayer.get_balance(),
                      "\nanother game?\n1=Yes\n2=No")
                startGame = int(input())
        gamePick = game_pick()
    if gamePick == 2:
        randInt = random.randint(1, 36)
        print("Pick your choice \n\t1.(Numbers 1-36)\n\t2.(Colors)\n\n\t9.Exit")
        choice = int(input())
        if choice == 1:
            betAmount = [0]
            playerBet = [0]
            print("Enter the number to bet on (1-36):")
            playerBet[0] = int(input())
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
            if isItIn == True:
                index_solution = playerBet.index(randInt)
                newplayer.set_balance(newplayer.get_balance() + (betAmount[index_solution] * 36))
                print(color.BOLD + color.GREEN + f"the number is....{randInt}\n" + color.END,
                      color.BOLD + color.GREEN + f"!!!!\nYou won!!! {betAmount[index_solution] * 36}"
                      + color.END, f"added to your balance.\nNew balance:\t{newplayer.get_balance()}")
            else:
                newplayer.set_balance(newplayer.get_balance() - betAmountSum)
                print(color.BOLD + color.RED + f"the number is....{randInt}\n" + color.END,
                      f"!!!!\nYou lost :(\n{betAmountSum}",
                      f"has been deducted from your balance.\nNew balance:\t{newplayer.get_balance()}")
        if choice == 2:
            print("What color would you like to bet on?\n\t1-Black\n\t2-Red")
            playerBet = int(input())
            betAmount = newplayer.new_bet()
            colorResult = random.randint(1, 2)
            if playerBet == colorResult:
                newplayer.set_balance(newplayer.get_balance() + betAmount)
                print(color.BOLD + color.GREEN + f"You won!!! {betAmount}" + color.END,
                      f"added to your balance.\nNew balance:\t{newplayer.get_balance()}")
            else:
                newplayer.set_balance(newplayer.get_balance() - betAmount)
                print(color.BOLD + color.RED + f"You lost :(\n{betAmount}" + color.END,
                      f"has been deducted from your balance.\nNew balance:\t{newplayer.get_balance()}")
        if choice == 9:
            gamePick = game_pick()
            continue
    if gamePick == 3:
        newplayer.draw_card()
        newplayer.draw_card()
        betAmount = newplayer.new_bet()
        cardsSum = sum_cards(newplayer.cards)  # player's total
        print(f"Your cards are: {newplayer.get_card(0)}, {newplayer.get_card(1)} \nSum of cards: {cardsSum}")
        opponent.draw_card()
        opponent.draw_card()
        oppSum = sum_cards(opponent.cards)  # dealer's total
        print(
            f"Dealer cards are:{opponent.get_card(0)}, {opponent.get_card(1)} \nAnd the sum of the dealer's cards are:{oppSum}",
            "\n\nAnother card?", color.BOLD + color.GREEN + "\n\t1-Yes" + color.END,
                                 color.BOLD + color.RED + "\n\t2-No" + color.END)
        if oppSum < 17:
            draw_dealer(opponent, opponent.cards, oppSum)
            oppSum = sum_cards(opponent.cards)
            print("Dealer has drawn more cards. New total sum of dealer's cards is: ", oppSum)
        anotherCard = int(input())
        while anotherCard == 1:
            newplayer.draw_card()
            cardsSum = sum_cards(newplayer.cards)
            print(
                f"Next cards is: {newplayer.cards[len(newplayer.cards) - 1]} and the total sum is {cardsSum}\nAnother card?\n\t",
                color.BOLD + color.GREEN + "1-Yes" + color.END, color.BOLD + color.RED + "\n\t2-No" + color.END)
            anotherCard = int(input())
        win = check_BJ(cardsSum, oppSum)
        if win:
            if count_cards(newplayer.cards) == 2 & cardsSum == 21:
                betAmount = int(betAmount * 1.5)
                print(color.BG_WHITE + color.RED + "BJ!!!" + color.END)
            newplayer.set_balance(newplayer.get_balance() + betAmount)
            print(color.BOLD + color.GREEN + "Congratulations!" + color.END + "\nYou have won ", betAmount,
                  ".\nAnd your balance is now ", newplayer.get_balance())
        else:
            newplayer.set_balance(newplayer.get_balance() - betAmount)
            print("Im sorry :(\nBetter Luck next time!\n" + color.RED + "Your current balance:" + color.END,
                  newplayer.get_balance())
        print("Another game?", color.BOLD + color.GREEN + "\n\t1-Yes" + color.END,
              color.BOLD + color.RED + "\n\t2-No" + color.END)
        anotherBJ = int(input())
        newplayer.reset_card_array()
        opponent.reset_card_array()
        if anotherBJ == 2:
            gamePick = game_pick()
if gamePick == 9:
    print(color.BOLD + color.RED + f"Your end balance: {newplayer.get_balance()}\nGoodbye {newplayer.name}." + color.END)