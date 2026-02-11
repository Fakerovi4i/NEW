name_list = ['Артемий', 'Борис', "Влад", "Гоша", "Дима", 'Евгений', 'Женя', 'Захар']
name_list_2 = []
for i in range(0, len(name_list), 2):
	name_list_2.append(name_list[i])
print("Первый день:", name_list_2)