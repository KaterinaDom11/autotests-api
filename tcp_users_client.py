import socket
import sys

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

message = sys.argv[1] if len(sys.argv) > 1 else "Привет, сервер!" #Как дела?
client_socket.send(message.encode())

print(client_socket.recv(1024).decode())
client_socket.close()