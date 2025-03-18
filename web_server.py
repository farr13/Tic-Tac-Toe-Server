import socket

class tic_tac_toe:
    
    def __init__(self):
        self.player = 1
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.moves = []
        self.gameEnd = False
    
    def reset_game(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.moves = []
    
    def input_move(self, row, column):
        if (([row, column] in self.moves)):
            print("Cannot make this move as it has already been made!")
            #Ensures same player goes again becasue swap is called in main function
            self.swap()
        else:
            self.board[row][column] = self.player
            self.moves.append([row, column])

    def swap(self):
        if(self.player == 1):
            self.player = 2
        else:
            self.player = 1
    
    def display(self):
        print(f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}\n__________\n{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}\n__________\n{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")
    
    def game_end_tie(self):
        for row in self.board:
            for column in row:
                if column == 0:
                    return False
        return True

    def game_end(self):
        #Vertical Win
        if (self.board[0][0] == self.player & self.board[0][1] == self.player & self.board[0][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            return True
        elif (self.board[1][0] == self.player & self.board[1][1] == self.player & self.board[1][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            return True
        elif (self.board[2][0] == self.player & self.board[2][1] == self.player & self.board[2][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            return True
        #Horizontal Win
        elif (self.board[0][0] == self.player & self.board[1][0] == self.player & self.board[2][0] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            return True
        elif (self.board[0][1] == self.player & self.board[1][1] == self.player & self.board[2][1] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            return True
        elif (self.board[0][2] == self.player & self.board[1][2] == self.player & self.board[2][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            return True
        #Diagonal Win
        elif (self.board[0][0] == self.player & self.board[1][1] == self.player & self.board[2][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            return True
        elif (self.board[0][2] == self.player & self.board[1][1] == self.player & self.board[2][0] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            return True
        #Tie Game
        elif self.game_end_tie():
            print("Tie Game!")
            return True
        #No Win
        else:
            return False
        
def main():
    main_game = tic_tac_toe()
    main_game.display()
    gameEnd = False
    while(not gameEnd):
        row = input("Input the row you want to play: ")
        column = input("Input the column you want to play: ")
        try:
            main_game.input_move(int(row), int(column))
        except:
            print("Input must be an Integer and within the board")
        gameEnd = main_game.game_end()
        main_game.swap()
        main_game.display()

main()





















