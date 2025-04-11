
import socket
import threading
from game_class import tic_tac_toe

# host and port address
HOST = '127.0.0.1'
PORT = 12345

# list to track what clients are connected along with their nicknames
clients = []
nicknames = []
game = tic_tac_toe()
players = [] #tracks whos playing the game

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            remove_client(client)

def remove_client(client):# function so removing clients is reusable where nessacary
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[index]
        broadcast(f"{nickname} has left the chat.")
        clients.remove(client)
        nicknames.remove(nickname)
        client.close()

def handle_game_move(nickname, client, move):
    if game.gameEnd:
        broadcast("Game has already ended.")
        return
    try:
        row, col = map(int, move.split(','))
        if [row, col] in game.moves:
            client.send("Invalid move, already taken.".encode('utf-8'))
            return
        game.input_move([row, col])
        game.player = 2 if game.player == 1 else 1
        broadcast(f"{nickname} made move: {row},{col}")
        broadcast(game.display())
        if game.gameEnd:
            broadcast("Game Over!")
    except Exception as e:
        client.send(f"wrong format for the move".encode('utf-8'))

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message.strip().lower() == "/exit":
                players.clear()
                nickname = nicknames[clients.index(client)]
                broadcast(f"{nickname} has left the chat.")
                remove_client(client)
                break
            elif message.startswith("/move"):
                nickname = nicknames[clients.index(client)]
                move = message.split()[1]
                handle_game_move(nickname, client, move)

            elif message.startswith("/start"):
                if client not in players and len(players) < 2:
                    players.append(client)
                    nickname = nicknames[clients.index(client)]
                    broadcast(f"{nickname} wants to play tic tac toe.")
                    if len(players) == 2:
                        broadcast("tic tac toe started! Use /move row,column from 0-2")
                else:
                    client.send("can't join game at all or more than once".encode('utf-8'))

            elif message.strip().lower() == "/restart":
                if game.gameEnd:
                    game.__init__()  # Or use game.reset_game() if you made a separate reset method
                    players.clear()
                    broadcast("Game has been restarted! Type /start to join again.")
                else:
                    client.send("You can only restart after a game ends.".encode('utf-8'))

            else:
                nickname = nicknames[clients.index(client)]
                message = f"{nickname}: {message}"
                broadcast(message)

        except:
            remove_client(client)
            break

def receive_connections():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print("Server Started")

    while True:
        client, address = server.accept()

        client.send("NICKNAME".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        clients.append(client)# adds nickname and client to the list
        nicknames.append(nickname)

        print(f"{nickname}, connected to the server")
        broadcast(f"{nickname} joined the chat!")
        client.send("Connected /start for tic tac toe".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()