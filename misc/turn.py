import signal
from random import randint
from import_words import all_words

def choose_random_sylable():
  return sylable_list[randint(0, len(sylable_list) - 1)]

def search_word(text):
  for word in all_words:
    if word == text:
      return True
  return False

def timeout(signum, frame):
    raise Exception('Seu tempo acabou!')

sylable_list = ['al', 'fa', 'mar', 'ta', 'er', 'ar', 'pa', 'ca']

signal.signal(signal.SIGALRM, timeout)
# signal.alarm(5)

sylable = choose_random_sylable()
print(sylable)
signal.alarm(5)
while True:
    try:
        text = input('Insira a palavra com a sílaba acima: ') + '\n'
        if sylable in text and search_word(text):
            signal.alarm(0)
            print('Acertou!', text)
            break
    except Exception as e:
        print(e)
        break
    