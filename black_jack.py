

def play_bj():
    # IMPORTS
    ## CLASSES:
    import cfg
    from cfg import Color

    ## UTILITIES:
    from cfg import sum_cards
    from cfg import draw_dealer
    from cfg import check_BJ

    another_bj = 1
    while another_bj == 1:
        print(Color.BOLD + "WELCOME TO BLACK JACK" + Color.END)
        cfg.new_player.draw_random_card()
        cfg.new_player.draw_random_card()
        bet_amount = cfg.new_player.new_bet()
        cardsSum = sum_cards(cfg.new_player.cards)  # player's total
        print(
            f"Your cards are: {cfg.new_player.get_card(0)}, {cfg.new_player.get_card(1)} \nSum of cards:\t {cardsSum}\n")
        cfg.opponent.draw_random_card()
        cfg.opponent.draw_random_card()
        oppSum = sum_cards(cfg.opponent.cards)  # dealer's total
        print(f"Dealer cards are:{cfg.opponent.get_card(0)}, {cfg.opponent.get_card(1)} \n"
              f"And the sum of the dealer's cards are:{oppSum} \n\nAnother card?", Color.BOLD + Color.GREEN +
              "\n\t1-Yes" + Color.END, Color.BOLD + Color.RED + "\n\t2-No" + Color.END)
        if oppSum < 17:
            draw_dealer(cfg.opponent, cfg.opponent.cards, oppSum)
            oppSum = sum_cards(cfg.opponent.cards)
            print("Dealer has drawn more cards. New total sum of dealer's cards is: ", oppSum)
        anotherCard = int(input())
        while anotherCard == 1 and cardsSum < 22:
            cfg.new_player.draw_random_card()
            cardsSum = sum_cards(cfg.new_player.cards)
            print(
                f"Next cards is: {cfg.new_player.cards[len(cfg.new_player.cards) - 1]} and the total sum is {cardsSum}\n"
                f"Another card?\n\t", Color.BOLD + Color.GREEN + "1-Yes" + Color.END, Color.BOLD + Color.RED +
                                      "\n\t2-No" + Color.END)
            anotherCard = int(input())
        if cardsSum > 21:
            print("BURNT!")
        win_check = check_BJ(cardsSum, oppSum)
        if win_check:
            if cfg.new_player.cards_len() == 2 and cardsSum == 21:
                bet_amount = int(bet_amount * 1.5)
                print(Color.BG_WHITE + Color.RED + "BJ!!!" + Color.END)
            cfg.new_player.win(bet_amount * 2)
        else:
            cfg.new_player.lose(bet_amount)
        print("Another game?", Color.BOLD + Color.GREEN + "\n\t1. Yes" + Color.END,
              Color.BOLD + Color.RED + "\n\t2. No" + Color.END)
        another_bj = int(input())
        cfg.new_player.reset_card_array()
        cfg.opponent.reset_card_array()
        if another_bj == 2:
            return