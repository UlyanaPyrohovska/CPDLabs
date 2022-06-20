"""
 Implements a simple socket server

"""

import socket

# Define socket host and port
import threading

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000


def handle_client(client_connection, connections):
    username = client_connection.recv(1024).decode()
    client_connection.sendall(('You are now connected, ' + username + '!').encode())
    print('New client:', username)
    for con in connections:
        if client_connection != con:
            con.sendall(("(" + username + ")" + " is now connected!").encode())
    while True:
        msg = client_connection.recv(1024).decode()
        print('Received:', msg)
        mensagem = "(" + username + ")" + " " + msg
        for con in connections:
            if client_connection != con:
                con.sendall(mensagem.encode())
        # Recebe mensagem do cliente
        if msg == 'exit':
            client_connection.sendall(('Goodbye ' + username + '!').encode())
            connections.remove(client_connection)
            for con in connections:
                con.sendall(("(" + username + ") has exited!").encode())

            break
    print('Client disconnected:', username)
    client_connection.close()


# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print('Listening on port %s ...' % SERVER_PORT)
client_connections = []

while True:
    # Wait for client connections
    client_con, client_address = server_socket.accept()
    client_connections.append(client_con)
    thread = threading.Thread(target=handle_client, args=[client_con, client_connections])
    thread.start()

# Close socket
server_socket.close()
