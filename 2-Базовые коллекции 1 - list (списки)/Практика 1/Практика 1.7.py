original_list = [1, 4, -3, 0, 10]
new_list = []
move = int(input("Сдвиг: "))

for i in range(len(original_list)):
	new_list.append(original_list[i-move])

print("Изначальный список:", original_list)
print("Новый список:", new_list)

