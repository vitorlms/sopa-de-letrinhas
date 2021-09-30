import socket


# endereço do servidor e socket do cliente
address = ('localhost', 12000)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


message = input('Entre seu nome: ')
client_socket.sendto(message.encode(), address)

client_socket.settimeout(10)
message = client_socket.recv(2048)
try:
    message = input(message.decode())
except socket.timeout:
    message = client_socket.recv(2048)
    message = input(message.decode())