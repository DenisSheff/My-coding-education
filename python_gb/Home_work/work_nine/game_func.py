import os
import pickle


def check_desk(desk: list, symbol: str) -> bool:
    for i in range(3):
        if desk[i].count(symbol) == 3:
            return True
        elif [desk[0][i], desk[1][i], desk[2][i]].count(symbol) == 3:
            return True
        elif [desk[0][0], desk[1][1], desk[2][2]].count(symbol) == 3:
            return True
        elif [desk[0][2], desk[1][1], desk[2][0]].count(symbol) == 3:
            return True
    return False


def reset_board(board: list):
    for i in range(3):
        for j in range(3):
            board[i][j] = '\U0001F60E'


def init(db):
    if os.path.exists('db.dat'):
        with open('db.dat', 'rb') as f:
            db = pickle.load(f)