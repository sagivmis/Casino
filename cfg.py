##  IMPORTS
# MODULES:
import send2trash
import csv
import os

# CLASSES:
from casino import Player
from casino import Card
from casino import Deck
from casino import Hand

# UTILITIES:
import logging
import random
from casino import Color

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
    line_fields=line.strip().split(',')
    amount = int(line_fields[1])
    return amount

def show_high_score():
    # f = open('high_score.csv', mode='r', newline='')
    # csv_file = csv.reader(f)
    # data_lines = list(csv_file)
    # print(data_lines)
    # f.close()
    print("*"*50)
    print('██████████████████████████████████████████████████')
    print('█─█─█▄─▄█─▄▄▄▄█─█─███─▄▄▄▄█─▄▄▄─█─▄▄─█▄─▄▄▀█▄─▄▄─█')
    print('█─▄─██─██─██▄─█─▄─███▄▄▄▄─█─███▀█─██─██─▄─▄██─▄█▀█')
    print('▀▄▀▄▀▄▄▄▀▄▄▄▄▄▀▄▀▄▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀')
    print("*"*50)
    with open('high_score.csv','r') as fp:
        data = fp.readlines()
        data.sort(key=sorts, reverse=True)
        print(Color.BOLD+"Name\t\tBalance"+Color.END)
        for line in data:
            newline = line.split(',')
            print(f"{newline[0]}\t\t{newline[1]}")


def save_score():
    f = open('high_score.csv', mode='a', newline='')
    csv_file = csv.writer(f)
    csv_file.writerow([new_player.name, new_player.balance])
    f.close()
    print("Saved successfully.\n")


def main_menu():
    logging.debug("Starting Casino")
    name = input("Input your name")
    new_player.name = name

    game_picked_by_player = game_pick()
    playing_deck = Deck()

    while game_picked_by_player != 9:
        while game_picked_by_player in [1, 2, 3, 4, 7, 8]:
            if game_picked_by_player == 7:
                save_score()
                game_picked_by_player = game_pick()

            if game_picked_by_player == 8:
                show_high_score()
                game_picked_by_player = game_pick()

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

        else:

            if game_picked_by_player != 9:
                game_picked_by_player = wrong_input()
            else:
                break
    if game_picked_by_player == 9:
        print(
            Color.BOLD + Color.RED + f"Your end balance: {new_player.get_balance()}\nGoodbye {new_player.name}."
            + Color.END)


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
    #    colordict = {'Spade': 'Black', 'Club': 'Black', 'Heart': 'Red', 'Diamond': 'Red'}
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


def game_pick():  # inputs what game player wants to play
    print(
        "Pick game:" + Color.BOLD + "\n\t1. War\n\t2. Roullette\n\t3. BlackJack\n\t4. Tic Tac Toe (friendly game)\n\t\t7. Save Score\n\t\t8. Show high score\n\n\t\t\t9. Exit" + Color.END)
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
                Color.RED + f" -----\n|\t{card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  |\n|{card.get_card()}\t  |\n -----" + Color.END)
        else:
            print(
                Color.RED + f" -----\n|\t {card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  |\n|{card.get_card()}\t  |\n -----" + Color.END)
    else:
        if card.get_card() == 10:
            print(
                f" -----\n|\t{card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  |\n|{card.get_card()}\t  |\n -----")
        else:
            print(
                f" -----\n|\t {card.get_card()}|\n|\t {card.get_shape()}|\n|{card.get_shape()}\t  |\n|{card.get_card()}\t  |\n -----")
    return card.shape


def wrong_input():
    game_picked = 0
    if game_picked != 9:
        legit_input = False
        while not legit_input:
            print("WRONG INPUT")
            game_picked = game_pick()
            if game_picked in [1, 2, 3, 4, 9, 7, 8]:
                legit_input = True
    return game_picked
