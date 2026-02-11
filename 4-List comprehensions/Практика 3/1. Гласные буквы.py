vowel_symbol = ['а', 'у', 'о', 'ы', 'э', 'я', 'ю', 'ё', 'и', 'е']
text = "Нужно отнести кольцо в Мордор!"
vowel_in = [i for i in text if i in vowel_symbol]


print("Список гласных букв:", vowel_in)
print("Длина списка:", len(vowel_in))