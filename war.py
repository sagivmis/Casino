def replay():
    again = input("Another game? y or n")
    while again != "y" and again != "n":
        again = input("Another game?")
    if again == "y":
        return True
    else:
        return False


def count_cards(cards_list):
    count = 0
    for _ in cards_list:
        count += 1
    return count


def to_war(player, opp, playing_deck): #returns 1 for win , 0 for lose
    at_war = True
    index = 0

    while at_war:
        for i in range(3):
            index += 1
            player.hand.draw_card_from_deck(playing_deck)
            opp.hand.draw_card_from_deck(playing_deck)
        if (player.hand.cards[player.hand.total_cards]) > (opp.hand.cards[opp.hand.total_cards]):
            at_war = False
            for i in range(index):
                player.cards.append(opp.hand.cards[i])
            opp.hand.reset_hand_card_array()
            player.hand.reset_hand_card_array()
            return 1

        if (player.hand.cards[player.hand.total_cards]) > (opp.hand.cards[opp.hand.total_cards]):
            at_war = False
            for i in range(index):
                opp.cards.append(player.hand.cards[i])
            opp.hand.reset_hand_card_array()
            player.hand.reset_hand_card_array()
            return 0


def run_war():
    # CLASSES:
    #
    import cfg
    import casino
    from cfg import Color
    ##

    # UTILITIES:
    #
    from cfg import show_card
    ##

    deck = casino.Deck()
    print("WELCOME TO WAR \nstart game? \n\t1=Yes \n\t2=No")
    start_game = int(input())
    while start_game == 1:
        bet = cfg.new_player.new_bet()
        card = cfg.new_player.hand.draw_card_from_deck(deck)
        print(f"Your card: ", Color.BOLD + show_card(card) + Color.END)
        oppcard = cfg.opponent.hand.draw_card_from_deck(deck)
        print(f"Opponent's card: ", Color.BOLD + show_card(oppcard) + Color.END)
        if card.number < oppcard.number:
            cfg.new_player.lose(bet)
            print("\nanother game?\n1=Yes\n2=No")
            start_game = int(input())
        elif card.number == oppcard.number:
            cfg.new_player.tie(bet)
            print("Another game?\n\t1=Yes\n\t2=No")
            start_game = int(input())
        else:
            cfg.new_player.win(bet * 2)
            print("\nanother game?\n1=Yes\n2=No")
            start_game = int(input())
