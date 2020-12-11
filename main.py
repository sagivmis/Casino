import random


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


def count_cards(cards):
    count = 0
    for _ in cards:
        count += 1
    return count


def draw_dealer(cards, dealer):
    while dealer < 17:
        draw_card(cards)
        dealer = sum_list(cards)
    return


def build_deck_n_shuffle():
    deck = []
    for shape in range(4):
        for card in range(1, 14):
            deck.append(card)
            print(card)
    random.shuffle(deck)
    print("Successfuly shuffled new deck.")
    return deck


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
    x = random.randint(1, 14)
    if x > 11:
        x = 10
    cards.append(x)


def game_pick():  # inputs what game player wants to play
    print("Pick game:" + color.BOLD + "\n\t1. War\n\t2. Roullette\n\t3. BlackJack\n\n\t9. Exit" + color.END)
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


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    BLINK = '\033[5m'
    CONCEALED = '\033[7m'
    ALL_OFF = '\033[0m'
    # BG Colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


balance = 100
card = 0
oppcard = 0
gamePick = game_pick()
while gamePick != 9:
    if gamePick == 1:
        bet = new_bet(balance)
        print("start game? \n1=Yes \n2=No")
        startGame = int(input())
        while startGame == 1:
            print("Your card:")
            card = random.randint(1, 13)
            print(card)
            oppcard = random.randint(1, 13)
            print("Opponent's card:\n", oppcard)
            if card < oppcard:
                print(color.BOLD + color.RED + "You lost", bet, "from balance." + color.END)
                balance -= bet
                print("New balance:", balance)
                print("another game?\n1=Yes\n2=No")
                startGame = int(input())
            elif card == oppcard:
                print(color.BOLD + color.YELLOW + "Tied !" + color.END + "\n another game?\n\t1=Yes\n\t2=No")
                startGame = int(input())
            else:
                balance += bet
                print(color.BOLD + color.GREEN + "You win", bet, "!!" + color.END + "\nNew balance:", balance,
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
            betAmount[0] = new_bet(balance)
            # for multiple bets implement memory allocated array when learned which consists the bet amounts and checks each number with randInt (the number that played on roulette)
            print("Another bet? \n\t", color.BOLD + color.GREEN + "1-Yes" + color.END,
                  color.BOLD + color.RED + "\n\t2-No" + color.END)
            anotherbet = int(input())
            while anotherbet == 1:
                print("On what number? 1-36")
                x = int(input())
                playerBet.append(x)
                x = new_bet(balance)
                betAmount.append(x)
                print("Another bet? \n\t", color.BOLD + color.GREEN + "1-Yes" + color.END,
                      color.BOLD + color.RED + "\n\t2-No" + color.END)
                anotherbet = int(input())
            index_solution = 0
            betAmountSum = sum_list(betAmount)
            isItIn = randInt in playerBet
            if isItIn == True:
                index_solution = playerBet.index(randInt)
                if playerBet[index_solution] == randInt:
                    balance += betAmount[index_solution] * 36
                    print(color.BOLD + color.GREEN + f"the number is....{randInt}\n" + color.END,
                          color.BOLD + color.GREEN + f"!!!!\nYou won!!! {betAmount[index_solution] * 36}" + color.END,
                          f"added to your balance.\nNew balance:\t{balance}")
            else:
                balance -= betAmountSum
                print(color.BOLD + color.RED + f"the number is....{randInt}\n" + color.END,
                      f"!!!!\nYou lost :(\n{betAmountSum}",
                      f"has been deducted from your balance.\nNew balance:\t{balance}")
        if choice == 2:
            print("What color would you like to bet on?\n\t1-Black\n\t2-Red")
            playerBet = int(input())
            betAmount = new_bet(balance)
            colorResult = random.randint(1, 2)
            if playerBet == colorResult:
                balance += betAmount
                print(color.BOLD + color.GREEN + f"You won!!! {betAmount}" + color.END,
                      f"added to your balance.\nNew balance:\t{balance}")
            else:
                balance -= betAmount
                print(color.BOLD + color.RED + f"You lost :(\n{betAmount}" + color.END,
                      f"has been deducted from your balance.\nNew balance:\t{balance}")
        if choice == 9:
            gamePick = game_pick()
            continue
    if gamePick == 3:
        cards = []  # player cards
        draw_card(cards)
        draw_card(cards)
        # print("How much do you want to bet?\n\n\tYour balance is currently ", balance)
        betAmount = new_bet(balance)
        cardsSum = sum_list(cards)  # player's total
        print(f"Your cards are: {cards[0]}, {cards[1]} \nSum of cards: {cardsSum}")
        oppcards = []  # dealer's cards
        draw_card(oppcards)
        draw_card(oppcards)
        oppSum = sum_list(oppcards)  # dealer's total
        print(f"Dealer cards are:{oppcards[0]}, {oppcards[1]} \nAnd the sum of the dealer's cards are:{oppSum}",
              "\n\nAnother card?", color.BOLD + color.GREEN + "\n\t1-Yes" + color.END,
              color.BOLD + color.RED + "\n\t2-No" + color.END)
        if oppSum < 17:
            draw_dealer(oppcards, oppSum)
            oppSum = sum_list(oppcards)
            print("Dealer has drawn more cards. New total sum of dealer's cards is: ", oppSum)
        anotherCard = int(input())
        while anotherCard == 1:
            draw_card(cards)
            cardsSum = sum_list(cards)
            print(f"Next cards is: {cards[len(cards) - 1]} and the total sum is {cardsSum}\nAnother card?\n\t",
                  color.BOLD + color.GREEN + "1-Yes" + color.END, color.BOLD + color.RED + "\n\t2-No" + color.END)
            anotherCard = int(input())
        win = check_BJ(cardsSum, oppSum)
        if win:
            if count_cards(cards) == 2 & cardsSum == 21:
                betAmount = int(betAmount * 1.5)
                print(color.BG_WHITE + color.RED + "BJ!!!" + color.END)
            balance += betAmount
            print(color.BOLD + color.GREEN + "Congratulations!" + color.END + "\nYou have won ", betAmount,
                  ".\nAnd your balance is now ", balance)
        else:
            balance -= betAmount
            print("Im sorry :(\nBetter Luck next time!\n" + color.RED + "Your current balance:" + color.END, balance)
        print("Another game?", color.BOLD + color.GREEN + "\n\t1-Yes" + color.END,
              color.BOLD + color.RED + "\n\t2-No" + color.END)
        anotherBJ = int(input())
        if anotherBJ == 2:
            gamePick = game_pick()
if gamePick == 9:
    print(color.BOLD + color.RED + f"Your end balance: {balance}\nGoodbye." + color.END)
