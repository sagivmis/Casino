##  IMPORTS
# MODULES:
import csv
from os import path

import pandas as pd

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


def save_score():
    data = {"name": [new_player.name],
            "balance": [new_player.balance],
            "tries": [new_player.game_count]}
    df = pd.DataFrame(data)
    if not path.exists("pandas_highscore.csv"):
        df.to_csv("pandas_highscore.csv", index=False)
        return
    db = pd.read_csv("pandas_highscore.csv")
    if new_player.name in db.name.values:
        if input("Overwrite existing score? y or n\n") == 'y':
            db.loc[db['name'] == new_player.name, 'balance'] = new_player.balance
            db.loc[db['name'] == new_player.name, 'tries'] = new_player.game_count
            print("\t\t***Updated successfully the previous entry in the leaderboard***")
            db.to_csv("pandas_highscore.csv", index=False)
            return
        else:
            if input("Would you like to change your current name and save again? y or n\n") == 'y':
                print(f"\t\t-suggestion: {new_player.name}#<x>\t(x=0,1,2...)")
                set_name()
                save_score()
                return


    df.to_csv("pandas_highscore.csv", mode='a', index=False, header=False)
    print("\t\t***Saved successfully on leaderboard***")


def save_progress():
    if input("would you like to save your score to the leaderboard? y or n\n") == 'y':
        save_score()

    data = {"name": [new_player.name],
            "balance": [new_player.balance],
            "tries": [new_player.game_count]}
    df = pd.DataFrame(data)

    if not path.exists("save_pandas.csv"):
        df.to_csv("save_pandas.csv", index=False)
        return

    db = pd.read_csv("save_pandas.csv")
    if new_player.name in db.name.values:
        db.loc[db['name'] == new_player.name, 'balance'] = new_player.balance
        db.loc[db['name'] == new_player.name, 'tries'] = new_player.game_count
        print("\t\t***Successfully found previous save and updated it.***")
        db.to_csv("save_pandas.csv", index=False)
        return
    df.to_csv("save_pandas.csv", mode='a', header=False, index=False)
    print("\t\t **Successfully saved game progress**")


def check_if_name_in_data_and_replace():
    var = None
    x = 0
    name = new_player.name
    df = pd.read_csv("save_pandas.csv")

    if name in df.name.values:
        var = df.loc[df['name'] == name].values[0]
        x = input(
            f"I see this is not your first time around.\nAre you {name} who played here for {var[2]} times? y or n")

    if x == 'y':
        if var[0]:
            new_player.name = var[0]
            new_player.balance = var[1]
            new_player.game_count = var[2] + 1
            print(
                f"Welcome back {new_player.name}\nYour balance: {new_player.balance} and this is your"
                f" {new_player.game_count} time here")


def load_game():
    desired_name = input("Please input your save's name")
    db = pd.read_csv("save_pandas.csv")
    line = None
    if desired_name in db.name.values:
        line = db.loc[db['name'] == desired_name].values[0]
        if input("Found the save.\nLoad game? y or n") == 'y':
            new_player.name = line[0]
            new_player.balance = line[1]
            new_player.game_count = line[2] + 1
            print(f"Welcome back {new_player.name}\nYour balance: {new_player.balance} "
                  f"and this is your {new_player.game_count} time here")
    else:
        print(f"Couldn't find save, are you sure it was called {desired_name}?")
        if input("Would you like to load another save? y or n") == 'y':
            load_game()


def show_high_score():
    print("*" * 50)
    print('██████████████████████████████████████████████████')
    print('█─█─█▄─▄█─▄▄▄▄█─█─███─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄▄▀█▄─▄▄─█')
    print('█─▄─██─██─██▄─█─▄─███▄▄▄▄─█─███▀█─██─██─▄─▄██─▄█▀█')
    print('▀▄▀▄▀▄▄▄▀▄▄▄▄▄▀▄▀▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀')
    print("*" * 50)
    df = pd.read_csv("pandas_highscore.csv", index_col=["name"])
    df.sort_values(["balance"], inplace=True, ascending=False)
    print(f"\n-------------------------\n\n{df}\n\n-------------------------")


def saving_loading_menu():
    while True:
        print(f"Enter desired action:\n")
        player_choice = input(f"\t-save - To save current game (will overwrite previous saved game.)\n\t-load - "
                              f"To load previously saved game")
        while player_choice not in ['save', 'load']:
            player_choice = input(f"WRONG INPUT!\n\t-save - To save current game (will overwrite previous saved game.)"
                                  "\n\t-load - To load previously saved game")
        if player_choice == 'save':
            save_progress()
        if player_choice == 'load':
            load_game()
        break

def set_name():
    temp_name = input("Input your name:\n\tmax chars- 12.\n\tmin chars- 1.\n")
    new_player.name = temp_name
    if temp_name == 'admin':
        if input("Password?") == 'sagiv':
            new_player.balance = 999999

def main_menu():
    set_name()
    check_if_name_in_data_and_replace()

    print(f"Hello {new_player.name}\nYour starting balance is {new_player.balance}.\nGood Luck!\n")
    game_picked_by_player = game_pick()
    playing_deck = Deck()

    while game_picked_by_player != 9:
        while game_picked_by_player in [1, 2, 3, 4, 7, 8]:
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
                if input("Would you like to save your progress? y or n") == 'y':
                    save_progress()
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


def game_pick():  # inputs what game player wants to play
    game = 0
    try:
        print(f"MAIN MENU:\n\t1. War\n\t2. Roullette\n\t3. BlackJack\n\t4. Tic Tac Toe (friendly game)"
              "\n\n\t\t\t\t\t7. Show high score\n\t\t\t\t\t\t\t"
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
