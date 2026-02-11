# sin_dict = {"Привет": "Здравствуйте", "Грустно": "Печально", "Весело": "Радостно" }
# Тут мы создаем словарь и заносим в него данные
sin_dict = dict()
N = int(input("Сколько слов добавим: "))
for i in range(1, N+1):
    print(f"{i}-ая пара: ", end="")
    pare_dict = input().title().split(" - ")
    sin_dict[pare_dict[0]] = pare_dict[1]
    print(sin_dict)
#Тут запускаем цикл до первого верного поиска
while True:
    sucsess = False
    word_find = input("Какое слово ищем: ").lower()
    for i_key in sin_dict:
        if word_find == i_key.lower():#Если слово == ключю
            print("Синоним:", sin_dict[i_key])
            sucsess = True
            break
        elif word_find == sin_dict[i_key].lower():#Если слово равно значению ключа
            print("Синоним:", i_key)
            sucsess = True
            break
    if sucsess:
        break
    else:
        print("Такого слова нет в словаре, введите другое слово.")
