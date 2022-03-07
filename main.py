import random

#https://geekflare.com/tic-tac-toe-python-code/

class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)

    def show_board(self):
        for row in self.board:
            print(*row)

    def get_random_first_player(self):
        return random.int(0,1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def checking_if_players_won(self, player):
#checking row
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

#checking columns
        for i in range(3):
            win = True
            for j in range(3):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
#checking diag
        win = True
        for i in range(3):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(2-i):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

    def checking_if_board_full(self):
        is_full = True
        for row in self.board:
            for i in range(3):
                if row[i] == '-':
                    is_full = False
        return is_full











game = TicTacToe()
game.create_board()
game.show_board()
