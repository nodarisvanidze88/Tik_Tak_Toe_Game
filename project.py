from tabulate import tabulate
import numpy as np


def main(sc1=0, sc2=0):
    player1, player2, rounds, symbol1, symbol2 = info_for_starting()
    print("Let's Start!!!")
    for _ in range(rounds):
        try:
            winner, p = start_game(player1, player2, symbol1, symbol2)
            if winner == symbol1:
                sc1 += 1
                print(f"Hey, you {p} you winn and your score is {sc1}\nDear {player2}, your score is {sc2}")
            elif winner == symbol2:
                sc2 += 1
                print(f"Hey, you {p} you winn and your score is {sc2}\nDear {player1}, your score is {sc1}")
        except:
            print("Standoff")


def info_for_starting():    # function for initiate game and collect initiate data
    print("Welcome to Tic_Toc_Toe Game \nUse format like A1 or B1 \nPlease add Player Names")
    player1, player2, symbol1, symbol2 = check_player_names()
    rounds = check_rounds()
    return player1, player2, rounds, symbol1, symbol2


def check_player_names():   # get correct format of player names
    while True:
        player1 = input("Player 1: ").strip().upper()
        player2 = input("Player 2: ").strip().upper()
        if player1 == "" or player2 == "" or player1 == player2:
            print("Players name can't be empty or player names should be different")
        else:
            symbol1 = "X"
            symbol2 = "O"
            print(f"{player1} your symbol is {symbol1}")
            print(f"{player2} your symbol is {symbol2}")
            return player1, player2, symbol1, symbol2


def check_rounds():  # get correct numbers of rounds from 1 to 10
    while True:
        try:
            rounds = input("How many rounds do you what to play? ").strip()
            if 0 < int(rounds) <= 10:
                return int(rounds)
        except:
            print("Please add numbers from 1 to 10")


def win_checker(tbl):
    ans1 = []
    ans2 = []
    ans3 = []
    # check vertically
    for k in range(1, 4):
        temp_arr = []
        for i in range(3):
            if tbl[i][k] != "":
                temp_arr.append(tbl[i][k])
        if len(temp_arr) == 3:
            ans1.append(temp_arr)
    # check horizontally
    for k in range(3):
        temp_arr = []
        for i in range(1, 4):
            if tbl[k][i] != "":
                temp_arr.append(tbl[k][i])
        if len(temp_arr) == 3:
            ans2.append(temp_arr)
    # check diagonal left to right
    temp_arr = []
    for k in range(3):
        if tbl[k][k+1] != "":
            temp_arr.append(tbl[k][k+1])

    if len(temp_arr) ==3:
        ans3.append(temp_arr)
    # check diagonal right to left
    temp_arr = []
    for k in range(2, -1, -1):
        if tbl[k][k+1] != "":
            temp_arr.append(tbl[k][k+1])
    if len(temp_arr) ==3:
        ans3.append(temp_arr)
    for i in ans1:
        a = np.unique(np.array(i))
        if len(a) == 1 and len(ans1) > 0:
            return a
    for i in ans2:
        b = np.unique(np.array(i))
        if len(b) == 1 and len(ans2) > 0:
            return b
    for i in ans3:
        c = np.unique(np.array(i))
        if len(c) == 1 and len(ans3) > 0:
            return c


def start_game(p1, p2, s1, s2):
    table = [["1", "", "", ""], ["2", "", "", ""], ["3", "", "", ""]]
    columns = {
            "A": 1,
            "B": 2,
            "C": 3
        }
    counter = 0

    def possible_answers():  # possible correct format of answers
        header = ["A", "B", "C"]
        first_column = ["1", "2", "3"]
        answers = []
        for i in header:
            for k in first_column:
                answers.append(i+k)
        return answers

    def draw_table():   # draw Table
        header = [""]
        col = columns.keys()
        for i in col:
            header.append(i)
        return tabulate(table, headers=header, tablefmt="grid")

    def player_input(name, symb):
        answers = possible_answers()
        while True:
            user = input(f"{name} your turn: ").strip().upper()
            if user not in answers:
                print("Incorrect Answer format")
            else:
                return user[0], int(user[1]), symb

    def modify_table(user):
        column, row, symb = user
        if table[row-1][columns[column]] == "":
            table[row-1][columns[column]] = symb
        return table

    print(draw_table())
    while True:
        p = p1
        s = s1
        table = modify_table(player_input(p, s))
        counter += 1
        if ["X"] != win_checker(table) != ["O"] and counter < 9:
            print(draw_table())
        else:
            print(draw_table())
            try:
                return win_checker(table)[0], p
            except:
                return False
        p = p2
        s = s2
        table = modify_table(player_input(p, s))
        counter +=1
        if ["X"] != win_checker(table) != ["O"] and counter < 9:
            print(draw_table())
        else:
            print(draw_table())
            try:
                return win_checker(table)[0], p
            except:
                return False


if __name__ == "__main__":
    main()
