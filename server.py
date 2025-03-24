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
        print(f"{self.board[0][0]} | {self.board[0][1]} | {self.board[0][2]}\n__________\n{self.board[1][0]} | {self.board[1][1]} | {self.board[1][2]}\n__________\n{self.board[2][0]} | {self.board[2][1]} | {self.board[2][2]}")
    
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
        #Vertical Win
        if (self.board[0][0] == self.player and self.board[0][1] == self.player and self.board[0][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[1][0] == self.player and self.board[1][1] == self.player and self.board[1][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[2][0] == self.player and self.board[2][1] == self.player and self.board[2][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        #Horizontal Win
        elif (self.board[0][0] == self.player and self.board[1][0] == self.player and self.board[2][0] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[0][1] == self.player and self.board[1][1] == self.player and self.board[2][1] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[0][2] == self.player and self.board[1][2] == self.player and self.board[2][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        #Diagonal Win
        elif (self.board[0][0] == self.player and self.board[1][1] == self.player and self.board[2][2] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        elif (self.board[0][2] == self.player and self.board[1][1] == self.player and self.board[2][0] == self.player):
            print(f"Congrats player {self.player}, You Won!")
            self.gameEnd = True
        #Tie Game
        elif self.game_end_tie():
            print("Tie Game!")
            self.gameEnd = True
        #No Win
        else:
            self.gameEnd = False
    
    def host_game(self, host, port):
        """
        Takes in a host(ip address) and a port to host the game on, 
        waits until the second player connects to the game
        """
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((host, port))
        server.listen(1)

        client, addr = server.accept()
        threading.Thread(target=self.handle_connection, args=(client,)).start()
        server.close()

    def handle_connection(self, client):
        """
        Handles game functionallity when the game starts and during the game until it ends. 
        On player turn will input move and print board with nerw move made,
        on oppenent turn will wait until move it input and receive board from oppenent"
        """

        while not self.gameEnd:
            if self.player == 2: #Host Turn
                move = input("Enter a move (row,column: )")
                if(not (move.split(',') in self.moves)):
                    self.input_move(move.split(','))
                    self.player = 1
                    client.send(move.encode('utf-8'))
                else:
                    print("Move already made!")
            else: #Client Turn
                data = client.recv(1024)
                if not data:
                    break
                else:
                    self.input_move(data.decode('utf-8').split(','))
                    self.player = 2
        client.close()

if __name__ == "__main__":
    game = tic_tac_toe()
    game.host_game("localhost", 9999)
