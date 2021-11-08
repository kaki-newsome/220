"""
Name: Kaki Newsome
lab10.py
"""


def build_board():
    board_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board_list


def display_board(board):
    counter = 0
    print('_______')
    for num in range(3):
        print("|", end='')
        for i in range(3):
            print(board[counter], end='|')
            counter += 1
        print('\n_______')

def place_spot(board, spot, marker):
    board[spot - 1] = marker

def legal_spot(board, spot):
    if((board[spot - 1] == 'x' or board[spot - 1] == 'y' or board[spot - 1] == '0') or (spot < 1 or spot > 9)):
        return False
    else:
        return True

def game_won(board):
    winCon = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], \
              [1, 5, 9], [3, 5, 7]]
    for condition in winCon:
        counterx = 0
        countery = 0
        for spot in condition:
            if board[spot - 1] == 'x':
                counterx += 1
            if counterx == 3:
                return "xwins"
            if board[spot - 1] == 'y':
                countery += 1
            if countery == 3:
                return "ywins"


def game_over(board, turncount):
    if ((game_won(board) == 'xwins' or game_won(board) == 'ywins') or (turncount > 9)):
        return True
    else:
        return False

def play_game():
    board = build_board()
    display_board(board)
    turncount = 0
    while not game_over(board, turncount):
        spot, marker = eval(input("where do you want to place your mark and are you x or y? "))
        legal = legal_spot(board, spot)
        if legal:
            place_spot(board, spot, marker)
            turncount += 1
        display_board(board)
    print(game_won(board))


def main():
    play_game()


main()
