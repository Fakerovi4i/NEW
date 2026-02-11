

kont_list = [165, 163, 160, 160, 157, 157, 155, 154]

new_cont = 162

for i in range(len(kont_list)):
	if new_cont < kont_list[-i]:
		print("Новый контейнер будет лежать в ячейке:", kont_list[-i])

