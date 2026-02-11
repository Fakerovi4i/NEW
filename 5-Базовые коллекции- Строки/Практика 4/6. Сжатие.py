text = "aaAAbbсaaaa"
count = 1
new_str = []

for i in range(len(text)):
    if i == len(text)-1 or text[i] != text[i+1]: #Если это не последняя буква и буква не равна следующей
        new_str.append(text[i] + str(count)) # то мы добавляем букву и значение счетчика
        count = 1 # И сбрасываем его
    else:
        count += 1 # Считаем пока следующаяя == i

new_text = "".join(new_str)
print(new_text)