N = int(input("Количество контейнеров: "))
kont_list = []

for i in range(N):
	while True:
		kont = int(input(f"Введите вес {i+1}-го контейнера: "))
		if kont <= 200:
			kont_list.append(kont)
			break
		else:
			print("Ошибка! Число больше 200!")

new_kont = int(input("Введите вес нового контейнера: "))
while new_kont > 200:
	print("Ошибка! Число больше 200!")
	new_kont = int(input("Повторите ввод: "))
counter = 0
while counter < len(kont_list) and kont_list[counter] >= new_kont:
	counter += 1

print("Номер места нового контейнера:", counter + 1)

