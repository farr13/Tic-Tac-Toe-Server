import socket
import threading


class tic_tac_toe:

    def __init__(self):
        self.player = 1
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.moves = []
        self.gameEnd = False

    def input_move(self, move):
        """
        Input the player smove into the tic-tac-toe board
        """
        self.board[int(move[0])][int(move[1])] = self.player
        self.moves.append(move)
        self.display()
        self.game_end()

    def display(self):
        """
        Print the tic tac toe board on the command line
        """
        return(
            f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}"
            f"\n__________\n{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}"
            f"\n__________\n{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")

    def game_end_tie(self):
        """
        Checks if all spaces on the board are filled
        """
        for row in self.board:
            for column in row:
                if column == 0:
                    return False
        return True

    def game_end(self):
        """
        Checks if the current player has won the game
        """
        # Vertical Win
        if (self.board[0][0] == self.player and self.board[0][1] == self.player and self.board[0][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[1][0] == self.player and self.board[1][1] == self.player and self.board[1][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[2][0] == self.player and self.board[2][1] == self.player and self.board[2][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        # Horizontal Win
        elif (self.board[0][0] == self.player and self.board[1][0] == self.player and self.board[2][0] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[0][1] == self.player and self.board[1][1] == self.player and self.board[2][1] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[0][2] == self.player and self.board[1][2] == self.player and self.board[2][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        # Diagonal Win
        elif (self.board[0][0] == self.player and self.board[1][1] == self.player and self.board[2][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[0][2] == self.player and self.board[1][1] == self.player and self.board[2][0] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        # Tie Game
        elif self.game_end_tie():
            print("Tie Game!")
            self.gameEnd = True
        # No Win
        else:
            self.gameEnd = False
