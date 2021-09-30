#input timeout: https://pt.stackoverflow.com/questions/297721/timeout-na-fun%C3%A7%C3%A3o-input-do-python

import threading

def check_players_lives():
  for player in players:
    if players[player] == 0:
      players.pop(player)
  if len(players) == 1:
    print(players + 'venceu')

def turn():
  try:
    sylable = choose_random_sylable()
    timer.start()
    text = input(sylable + ': ') + '\n'
    if sylable in text and search_word(text):
      timer.cancel()
      return True
  except Exception as exception:
    print('timeout!')
    return False

def timeout(): 
  raise Exception('timeout')

timer = threading.Timer(10, timeout)

players = {
  'vitor': 3,
  'luisa': 3,
  'joao': 3,
  'maria': 3
}

used_words = []

turn()

while (len(players) > 1):
  print(players)
  for player in players:
    if player in players:
      print(player)
      text = input('Insira uma palavra: ') + '\n'
      if not search_word(text):
        players[player] -= 1
    print(player, players[player])
  check_players_lives()
