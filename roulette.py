
def roulette():
    # IMPORTS:
    import random
    from casino import color
    from casino import sum_list
    import cfg
    ##

    game_on=True
    while game_on:
        print(color.BOLD + "WELCOME TO ROULETTE" + color.END)
        randInt = random.randint(1, 36)
        print("Pick your choice \n\t1.(Numbers 1-36)\n\t2.(Colors)\n\n\t9.Exit")
        choice = int(input())
        if choice == 1:
            bet_amount = [0]
            playerBet = [0]
            print("Enter the number to bet on (1-36):")
            playerBet[0] = int(input())
            if playerBet[0] == 99:  # for check. 99 for an array that will win.
                playerBet = list(range(37))
            bet_amount[0] = cfg.new_player.new_bet()
            print("Another bet? \n\t", color.BOLD + color.GREEN + "1. Yes" + color.END,
                  color.BOLD + color.RED + "\n\t2. No" + color.END)
            anotherbet = int(input())
            while anotherbet == 1:
                print("On what number? 1-36")
                x = int(input())
                playerBet.append(x)
                x = cfg.new_player.new_bet()
                bet_amount.append(x)
                print("Another bet? \n\t", color.BOLD + color.GREEN + "1. Yes" + color.END,
                      color.BOLD + color.RED + "\n\t2. No" + color.END)
                anotherbet = int(input())
            index_solution = 0
            bet_amountSum = sum_list(bet_amount)
            isItIn = randInt in playerBet
            if isItIn:
                index_solution = playerBet.index(randInt)
                if playerBet == list(range(37)):
                    bet_amount = list([10] * 37)  # inputs 10 as a bet for all 'tries' - also, a check
                print(color.BOLD + color.GREEN + f"the number is....{randInt}" + color.END)
                cfg.new_player.win((bet_amount[index_solution]) * 36)
            else:
                print(color.BOLD + color.RED + f"the number is....{randInt}\n" + color.END)
                cfg.new_player.lose(bet_amountSum)

        if choice == 2:
            print("What color would you like to bet on?\n\t1. Black\n\t2. Red")
            playerBet = int(input())
            bet_amount = cfg.new_player.new_bet()
            color_result = random.randint(1, 2)
            color_diction={1:'Black', 2:'Red'}
            if playerBet == color_result:
                print(f"The color is... {color_diction[color_result]}")
                cfg.new_player.win(bet_amount * 2)
            else:
                print(f"The color is... {color_diction[color_result]}")
                cfg.new_player.lose(bet_amount)
        if choice == 9:
            game_on = False
            return
