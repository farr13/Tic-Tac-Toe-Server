import socket
import threading

# Server details
HOST = '127.0.0.1'
PORT = 12345

# Ask user for nickname
nickname = input("Choose your nickname: ")

# Setup socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Receives messages from server
def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')# this just checks if they have provided a nickname yet
            if message == "NICKNAME":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occurred. Disconnected from server.")
            client.close()
            break

# Sends messages to server
def write():
    while True:
        message = input('')
        if message.lower() == 'exit':
            client.send(f"{nickname} has left the chat.".encode('utf-8'))
            client.close()
            break
        else:
            message = f"{nickname}: {message}"
            client.send(message.encode('utf-8'))

# Start threads
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
