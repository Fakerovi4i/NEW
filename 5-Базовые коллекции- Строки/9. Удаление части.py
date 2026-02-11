text = "ПитоН - ЭТО Хорошо"

counter_big = 0
counter_low = 0

for i in text:
    if i.isupper():
        counter_big += 1
    elif i.islower():
        counter_low += 1

# Крутой способ подсказал ИИ Вместо счетчика и цикла использовать генератор
# counter_big = sum(1 for i in text if i.isupper())
# counter_low = sum(1 for i in text if i.islower())

if counter_big > counter_low:
    text = text.upper()
else:
    text = text.lower()

print(text)