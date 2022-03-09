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
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def checking_if_players_won(self, player):
        win = None
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
        for i in range(3):
            win = True
            if self.board[i][2-i] != player:
                win = False
                break
        if win:
            return win
        return False

    def checking_if_board_full(self):
        is_full = True
        for row in self.board:
            for i in range(3):
                if row[i] == '-':
                    is_full = False
        return is_full

    def swap_player(self, player):
        return "X" if player == "o" else "o"

    def start(self):
        self.create_board()

        player = "X" if self.get_random_first_player()==1 else "o"
        while True:
            print(f"Player {player} turn")

#collectling users input

            self.show_board()
            row,col = list(map(int, input("Enter row and column number to fix the spot")))

#fixing a spot

            self.fix_spot(row -1, col - 1, player)

#checking if player has won

            if self.checking_if_players_won(player):
                print(f"Player {player} won!")
                break

#checking if is draw

            if self.checking_if_board_full():
                print(f"its a draw!")
                break

#swaping player
            player = self.swap_player(player)


game = TicTacToe()
game.start()

