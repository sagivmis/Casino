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
    from casino import color
    ##

    # UTILITIES:
    #
    from casino import show_card
    ##

    deck = casino.Deck()
    print("WELCOME TO WAR \nstart game? \n\t1=Yes \n\t2=No")
    startGame = int(input())
    while startGame == 1:
        bet = cfg.new_player.new_bet()
        card = cfg.new_player.hand.draw_card_from_deck(deck)
        print(f"Your card: ", color.BOLD + show_card(card) + color.END)
        oppcard = cfg.opponent.hand.draw_card_from_deck(deck)
        print(f"Opponent's card: ", color.BOLD + show_card(oppcard) + color.END)
        if card.number < oppcard.number:
            cfg.new_player.lose(bet)
            print("\nanother game?\n1=Yes\n2=No")
            startGame = int(input())
        elif card.number == oppcard.number:
            cfg.new_player.tie(bet)
            print("Another game?\n\t1=Yes\n\t2=No")
            startGame = int(input())
        else:
            cfg.new_player.win(bet * 2)
            print("\nanother game?\n1=Yes\n2=No")
            startGame = int(input())

#
# if __name__ != '__main__':
#     deck = build_deck_n_shuffle()
#     for x in range(26):
#         player_one.draw_card_from_deck(deck)
#         opponent_ai.draw_card_from_deck(deck)
#     print(len(player_one.cards))
#     print(len(opponent_ai.cards))
#     start_game = True
#     player_bet = player_one.new_bet()
#     round_num = 0
#     while start_game:
#         round_num += 1
#         print(f'Round {round_num}')
#         if len(player_one.cards) == 0:
#             lose(player_one, player_bet)
#             start_game = False
#             break
#         if len(opponent_ai.cards) == 0:
#             win(player_one, player_bet)
#             start_game = False
#             break
#         player_one_in_game_cards = []
#         ai_in_game_cards = []
#         player_one_in_game_cards.append(player_one.draw_card_from_deck(player_one.cards))
#         ai_in_game_cards.append(opponent_ai.draw_card_from_deck(opponent_ai.cards))
#         print("your card")
#         show_card(player_one_in_game_cards[0])
#         print("AI card")
#         show_card(ai_in_game_cards[0])
#         print(player_one_in_game_cards[0].number, "                   ", ai_in_game_cards[0].number)
#         index = 0  # to show the cards, already shown 0
#         input()
#         if player_one_in_game_cards[0].number > ai_in_game_cards[0].number:
#             win(player_one, player_bet)
#             player_one.cards.append(ai_in_game_cards[0])
#             ai_in_game_cards.pop(0)
#         elif player_one_in_game_cards[0].number < ai_in_game_cards[0].number:
#             lose(player_one, player_bet)
#             opponent_ai.cards.append(player_one_in_game_cards[0])
#             player_one_in_game_cards.pop(0)
#         else:
#             at_war = True
#             while at_war:
#                 if player_one_in_game_cards[index].number > ai_in_game_cards[index].number:
#                     win(player_one, player_bet)
#                     at_war = False
#                     for i in range(index):
#                         player_one.cards.append(ai_in_game_cards[i])
#                         ai_in_game_cards.pop(i)
#                     index = 0
#                 elif player_one_in_game_cards[index].number < ai_in_game_cards[index].number:
#                     lose(player_one, player_bet)
#                     at_war = False
#                     for i in range(index):
#                         opponent_ai.cards.append(player_one_in_game_cards[i])
#                         player_one_in_game_cards.pop(i)
#                     index = 0
#                 else:
#                     if count_cards(player_one_in_game_cards) < 3:
#                         lose(player_one, player_bet)
#                         index = 0
#                     if count_cards(ai_in_game_cards) < 3:
#                         win(player_one, player_bet)
#                         index = 0
#                 print("*" * 15)
#                 print("TIE")
#                 print("Initiating war")
#                 print("*" * 15)
#                 print("\t\tLOST CARDS:")
#                 for i in range(3):
#                     player_one_in_game_cards.append(player_one.draw_card_from_deck(player_one.cards))
#                     print("your card")
#                     show_card(player_one_in_game_cards[index])
#                     ai_in_game_cards.append(opponent_ai.draw_card_from_deck(opponent_ai.cards))
#                     print("AI card")
#                     show_card(ai_in_game_cards[index])
#                     index += 1
#                 print(f"Drawn 3 more cards for both players")
