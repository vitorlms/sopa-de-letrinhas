from ...sopa_de_letrinhas.words.models import Word

f = open("./todas_palavras", 'r')
all_words = f.readlines()
f.close()

words = []
for word in all_words:
  new_word = Word(text=word)
  words.append(new_word)

print(words)
