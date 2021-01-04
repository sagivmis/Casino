import random

import casino


def clear_screen():
    for i in range(250):
        print()


def player_input():
    choice = False  # not yet to choose correctly
    while not choice:
        x = input("Please insert 'X' or 'O'")
        if x == 'X' or x == 'O':
            choice = True


def place_marker(board, marker, position):
    board.pop(position)
    board.insert(position, marker)
    return board


def place_holder():
    print("----------------------------")


def win_check(board, mark):
    for i in range(1, 10, 3):
        if board[i] == board[i + 1] == board[i + 2] == mark:
            return True
    for i in [1, 2, 3]:
        if board[i] == board[i + 3] == board[i + 6] == mark:
            return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True

    return False


def choose_first():
    return random.randint(1, 2)


def space_check(board, position):
    return board[position] == " "


def full_board_check(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True


def player_choice(board):
    pos = int(input("What position you want to place?\n POS\nINDEX:\n1 2 3\n4 5 6\n7 8 9\n"))
    if space_check(board, pos):
        return pos
    else:
        while not space_check(board, pos):
            pos = int(input("What position you want to place?"))
        if space_check(board, pos):
            return pos


def replay():
    again = input("Another game? y or n")
    while again != "y" and again != "n":
        again = input("Another game?")
    if again == "y":
        return True
    else:
        return False


def display_board(board, switch, player=None):  # switch = 1 for win 0 for in-game
    if player:
        print(f"Current marker's turn: {player}")
    for i in range(1, 4):
        print(f"{board[i]}", end=" | ")
    print()
    print("___________")
    for i in range(4, 7):
        print(f"{board[i]}", end=" | ")
    print()
    print("___________")
    for i in range(7, 10):
        print(f"{board[i]}", end=" | ")
    print()
    print("___________")


def run_tictactoe_game():
    score = [0, 0]
    tie = 0
    print("Welcome to TIC TAC TOE")
    while True:
        print(f"The SCORE is:\n\tPLAYER 1: {score[0]}\n\tPLAYER 2: {score[1]}\n\t\tNumber of ties: {tie}")
        game_board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        display_board(game_board, 0)
        player2 = 'Z'
        player1 = input("Choose your marker: X or O")
        while player1 != 'X' and player1 != 'O':
            player1 = input("WRONG INPUT\nChoose your marker: X or O")
        if player1 == 'X':
            player2 = 'O'
        if player1 == 'O':
            player2 = 'X'

        turn = choose_first()
        print(f"Player {turn} will go first.")
        play_game = input("Play? y or n")
        while play_game != 'y' and play_game != 'n':
            play_game = input("WRONG INPUT\nPlay? y or n")
        if play_game == 'y':
            gamer_on = True
        else:
            gamer_on = False
        clear_screen()

        while gamer_on:
            if turn == 1:
                # player 1 turn
                display_board(game_board, 0, player1)
                position = player_choice(game_board)
                place_marker(game_board, player1, position)
                if win_check(game_board, player1):
                    clear_screen()
                    score[0] += 1
                    display_board(game_board, 0, player1)
                    print("Player 1 has won !")
                    gamer_on = False
                else:
                    if full_board_check(game_board):
                        tie += 1
                        clear_screen()
                        print("Tied")
                        display_board(game_board, 0)
                        gamer_on = False
                    else:
                        turn = 2
                        clear_screen()
                        print(f"Its Player {turn}'s turn")
            else:
                # player 2 turn
                display_board(game_board, 0, player2)
                position = player_choice(game_board)
                place_marker(game_board, player2, position)
                if win_check(game_board, player2):
                    clear_screen()
                    score[1] += 1
                    display_board(game_board, 0, player2)
                    print("Player 2 has won !")
                    gamer_on = False
                else:
                    if full_board_check(game_board):
                        tie += 1
                        clear_screen()
                        print(f"Tied")
                        display_board(game_board, 0)
                        gamer_on = False
                    else:
                        turn = 1
                        clear_screen()
                        print(f"Its Player {turn}'s turn")
        if not replay():
            print(f"The SCORE is:\n\tPLAYER 1: {score[0]}\n\tPLAYER 2: {score[1]}\n\t\tNumber of ties: {tie}")
            break
