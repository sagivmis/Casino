##  IMPORTS
# MODULES:
import csv

# CLASSES:
from casino import Player
from casino import Card
from casino import Deck
from casino import Hand

# UTILITIES:
import logging
import random

# MAIN MENU FUNCTIONS:
from black_jack import play_bj
from roulette import roulette
from tictactoe import run_tictactoe_game
from war import run_war

##GLOBAL VARIABLES:
new_player = Player("Player", 100)
opponent = Player("OP", 99999)
legit_input = False

##GLOBAL DICT. & LISTS:
colordict = {'Spade': 'Black', 'Club': 'Black', 'Heart': 'Red', 'Diamond': 'Red'}
suits = ('Heart', 'Diamond', 'Spade', 'Club')
ranks = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King')
values = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10}


def sorts(line):
    line_fields = line.strip().split(',')
    amount = int(line_fields[1])
    return amount


def save_game():
    # with open("save.csv","r") as f:
    #     csv_read=csv.reader(f)
    #     data = f.readlines()
    #     i=0
    #     saved_name = new_player.name
    #     for row in data:
    #         newdata=data[i].split(',')
    #         if newdata[0] == saved_name:
    #             data[i]=f"{saved_name},{new_player.balance}"
    #             print("SAVED GAME PROGRESS")
    #             return
    #         i+=1
    with open("save.csv", "a", newline='') as fp:
        csv_writer = csv.writer(fp)
        csv_writer.writerow([new_player.name, new_player.balance])


def load_game(load_name):
    with open("save.csv", "r") as fp:
        csv_reader = csv.reader(fp)
        data = fp.readlines()
        print(data)
        i=0
        for row in data:
            newdata = data[i].split(',')
            print(newdata)
            if newdata[0] == load_name:
                new_player.name = newdata[0]
                new_player.balance = int(newdata[1])
                print("LOADED")
                print(f"Welcome back {new_player.name}\nYour balance is: {new_player.balance}\nGOOD LUCK")
                return
            else:
                i += 1

        # new_player.name = newdata[0]
        # new_player.balance = int(newdata[1])
        print("Couldn't find save")



def show_high_score():
    print("*" * 50)
    print('██████████████████████████████████████████████████')
    print('█─█─█▄─▄█─▄▄▄▄█─█─███─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄▄▀█▄─▄▄─█')
    print('█─▄─██─██─██▄─█─▄─███▄▄▄▄─█─███▀█─██─██─▄─▄██─▄█▀█')
    print('▀▄▀▄▀▄▄▄▀▄▄▄▄▄▀▄▀▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀')
    print("*" * 50)
    with open('high_score.csv', 'r') as fp:
        data = fp.readlines()
        data.sort(key=sorts, reverse=True)
        print("   Name\t\t\tBalance")
        i = 1
        for line in data:
            newline = line.split(',')
            print(f"{i}. {newline[0]} {newline[1]}")
            i += 1


def save_score():
    f = open('high_score.csv', mode='a', newline='')
    csv_file = csv.writer(f)
    csv_file.writerow([new_player.name, new_player.balance])
    f.close()
    print("Saved successfully.\n")


def saving_loading_menu():
    while True:
        print(f"Enter desired action:\n")
        player_choice = input(f"\t-save - To save current game (will overwrite previous saved game.\n\t-load - "
                              f"To load previously saved game")
        while player_choice not in ['save', 'load']:
            player_choice = input(f"WRONG INPUT!\n\t-save - To save current game (will overwrite previous saved game."
                                  "\n\t-load - To load previously saved game")
        # while player_choice in ['save', 'load']:
        if player_choice == 'save':
            save_game()
        if player_choice == 'load':
            loading_name=input("what name of save?")
            new_loading_name=fix_name(loading_name)
            load_game(new_loading_name)
        break


def main_menu():
    logging.debug("Starting Casino")
    temp_name = input("Input your name:\n\tmax chars- 12.\n\tmin chars- 1.\n")
    name = fix_name(temp_name)
    new_player.name = name
    print(f"Hello {new_player.name}\nYour starting balance is 100.\nGood Luck!\n")
    game_picked_by_player = game_pick()
    playing_deck = Deck()
    while game_picked_by_player != 9:
        while game_picked_by_player in [1, 2, 3, 4, 6, 7, 8]:

            if game_picked_by_player == 1:
                run_war()
                game_picked_by_player = game_pick()

            if game_picked_by_player == 2:
                roulette()
                game_picked_by_player = game_pick()

            if game_picked_by_player == 3:
                play_bj()
                game_picked_by_player = game_pick()

            if game_picked_by_player == 4:
                run_tictactoe_game()
                game_picked_by_player = game_pick()

            if game_picked_by_player == 6:
                save_score()
                game_picked_by_player = game_pick()

            if game_picked_by_player == 7:
                show_high_score()
                game_picked_by_player = game_pick()

            if game_picked_by_player == 8:
                saving_loading_menu()
                game_picked_by_player = game_pick()
        else:

            if game_picked_by_player != 9:
                game_picked_by_player = wrong_input()
            else:
                break
    if game_picked_by_player == 9:
        print(f"Your end balance: {new_player.get_balance()}\nGoodbye {new_player.name}")  


def shape_shift_from_number(shape):
    shapes = {
        1: 'Heart',
        2: 'Spade',
        3: 'Diamond',
        4: 'Club'
    }

    return shapes[shape]


def build_deck_n_shuffle():  # working
    deck = []
    for shape in range(1, 5):
        for card in range(1, 14):
            newcard = Card(card, shape_shift_from_number(shape), colordict[shape_shift_from_number(shape)])
            deck.append(newcard)
            print(newcard)
    random.shuffle(deck)
    print("Successfuly shuffled new deck.")
    return deck


def sum_list(lst):
    total = 0
    for val in lst:
        total += val
    return total


def check_war(player, dealer):
    if player > dealer:
        return True
    elif player < dealer:
        return False


def sum_cards(cards):
    sum = 0
    for i in cards:
        sum += i.number
    return sum


def draw_dealer(dealer, cards, sumofcards):
    print("Generating cards for dealer.......... (must hit at-least 17)")
    while sumofcards < 17:
        dealer.draw_random_card()
        sumofcards = sum_cards(dealer.cards)
    return


def check_bet(balance, bet):  # checks if the bet is legit (=not higher than balance, can be equal to)
    # and if so returns True
    if bet > balance:
        print(f"Bet can't exceed max balance.\n please re-enter your bet. Your current balance is {balance}")
    else:
        return bet
    return 0


def game_pick():# inputs what game player wants to play
    game = 0
    try:
        print(f"MAIN MENU:\n\t1. War\n\t2. Roullette\n\t3. BlackJack\n\t4. Tic Tac Toe (friendly game)"
                                          "\n\t\t\t6. Save Score\n\t\t\t7. Show high score\n\n\t\t\t\t\t\t\t"
                                          "8. Save\Load menu\n\t\t\t\t\t\t\t9. Exit")
        game = int(input())
    except:
        print(f"WRONG INPUT\nPlease provide a choice by numbers 0-9 only.")
        game = game_pick()
    finally:
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
            print(f" -----\n|\t{card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  "
                  f"|\n|{card.get_card()}\t  |\n -----")
        else:
            print(f" -----\n|\t {card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  "
                  f"|\n|{card.get_card()}\t  |\n -----")
    else:
        if card.get_card() == 10:
            print(f" -----\n|\t{card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  "
                  f"|\n|{card.get_card()}\t  |\n -----")
        else:
            print(f" -----\n|\t {card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  "
                  f"|\n|{card.get_card()}\t  |\n -----")
    return card.shape


def wrong_input():
    game_picked = 0
    if game_picked != 9:
        legit_input = False
        while not legit_input:
            print("WRONG INPUT")
            game_picked = game_pick()
            if game_picked in [1, 2, 3, 4, 6, 7, 8]:
                legit_input = True
    return game_picked


def fix_name(name):
    length = len(name)
    if length > 12 or length < 1:
        while True:
            print(f"WRONG INPUT\n\tmax chars- 12.\n\tmin chars-1.")
            name_in = input(f"Input your name:")
            if len(name_in) > 1 and len(name_in) < 12:
                name = name_in
                length = len(name)
                break
    num_of_spaces = 12 - length
    new_name = name + (" " * num_of_spaces)
    return new_name
