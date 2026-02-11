text = input("Введите текст: ").split()
max_word = text[0]

for i in text:
    if len(i) > len(max_word):
        max_word = i

print("Самое длинное слово:", max_word)
print("Длина этого слова:", len(max_word), "сим.")