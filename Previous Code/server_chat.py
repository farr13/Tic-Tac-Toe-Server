import socket
import threading

# host and port address
HOST = '127.0.0.1'
PORT = 12345

# list to track what clients are connected along with their nicknames
clients = []
nicknames = []

# Broadcasts message to all clients
def broadcast(message):
    for client in clients: #for each client connected
        try:
            client.send(message)
        except: # if client unreachable remove it so it's not tried again
            index = clients.index(client)
            clients.remove(client)
            nickname = nicknames[index]
            nicknames.remove(nickname)



def handle_client(client):#reveives message from client then sends it back out
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message)
        except ConnectionResetError:
            # Handle client disconnection
            print("client was closed")
            break
        except:
            print("error")
            break

    # Ensure the client is still in the list before attempting to remove it
    try:
        index = clients.index(client) # find the position of client in the client list which is the same as in the nickname list
        nickname = nicknames[index]
        broadcast(f"{nickname} left the chat".encode('utf-8')) #tells all client which client has disconnected and closes the connection
        clients.remove(client)
        nicknames.remove(nickname)
        client.close()
    except ValueError:
        #checks if the client was removed ealier in the broadcast function
        pass

# Accepts new clients
def receive_connections(server):
    server.listen()
    print(f"Server address {HOST}:{PORT}")
    while True:
        client, address = server.accept()

        client.send("NICKNAME".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        nicknames.append(nickname)# adds nickname and client to the list
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server.".encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Setup socket
print("Server is starting...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of socket
server.bind((HOST, PORT))

print("Server is running...")
receive_connections(server)
