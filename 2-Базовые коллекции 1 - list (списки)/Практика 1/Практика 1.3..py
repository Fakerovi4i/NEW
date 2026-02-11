N = int(input("Введите количество видеокарт: "))
old_list = []
new_list = []
max = 0
for i in range(N):
	print(f'Видеокарта {i+1}:', end = " ")
	kart = int(input())
	old_list.append(kart)
	if kart > max:
		max = kart
for i in old_list:
	if i != max:
		new_list.append(i)

print("Старый список:", old_list)
print("Новый список:", new_list )

