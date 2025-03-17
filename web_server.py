import socket

class tic_tac_toe:
    
    def __init__(self):
        self.player = 1
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.moves = []
    
    def reset_game(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.moves = []
    
    def input_move(self, row, column):
        if ([row, column] in self.moves):
            print("Cannot make this move as it has already been made!")
        else:
            print(self.board[row][column])
            self.board[row][column] = self.player
            if(self.player == 1):
                self.player = 2
            else:
                self.player = 1
            self.moves.append([row, column])
    
    def display(self):
        print(f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}\n__________\n{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}\n__________\n{self.board[2][2]} | {self.board[2][1]} | {self.board[0][2]}")
    

    def game_end(self, player):
        for row in self.board:
            pass

def main():
    main_game = tic_tac_toe()
    main_game.display()

    while(main_game.game_end()):
        row = input("Input the row you want to play: ")
        column = input("Input the column you want to play: ")
        main_game.input_move(int(row), int(column))
        main_game.display()

main()
