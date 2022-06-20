"""
 Implements a simple socket client

"""

import socket

# Define socket host and port
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000


def listening_thread(client_socket):
    while True:
        res = client_socket.recv(1024).decode()
        print(res)
        if res.startswith('Goodbye'):
            break


# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect((SERVER_HOST, SERVER_PORT))

msg = input('Username? ')
client_socket.sendall(msg.encode())
res = client_socket.recv(1024).decode()
print(res)
thread = threading.Thread(target=listening_thread, args=[client_socket])
thread.start()

while True:
    # Send message

    msg = input()
    client_socket.sendall(msg.encode())

    # Check for exit
    if msg == 'exit':
        thread.join()
        # client_socket.close()
        # exit()
        break


    # Read response
# res = client_socket.recv(1024).decode()
# print(res)

# Close socket
client_socket.close()
