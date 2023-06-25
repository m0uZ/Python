# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.

import string

text = input("Введите текст: ")

clean_text = text.lower().translate(str.maketrans('', '', string.punctuation)).split()

word_counts = {}

for word in clean_text:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

top_words = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10])

print(top_words)