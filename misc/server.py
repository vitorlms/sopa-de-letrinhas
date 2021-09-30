import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('localhost', 12000))

players = []

print('Server ready')

def lobby():
  while True:
    message, client_address = server_socket.recvfrom(2048)
    if len(players) == 8 and client_address not in players:
      server_socket.sendto('Sala cheia.'.encode(), client_address)
    elif client_address not in players:
      players.append(client_address)
    