order_dict = dict()
quanty_pizza = 6

for i in range(quanty_pizza):
	print("Введите {0}-ый заказ через пробел\n(Имя, Пиццу, Количество): ".format(i+1))
	order_list = input().lower().split()

	if not order_list[0] in order_dict:
		order_dict[order_list[0]] = {order_list[1]: int(order_list[2])}
	elif not order_list[1] in order_dict.get(order_list[0], {}):
		order_dict[order_list[0]][order_list[1]] = int(order_list[2])
	else:
		order_dict[order_list[0]][order_list[1]] += int(order_list[2])

for i_man in order_dict:
	print("\n{0}:".format(i_man.title()))
	for i_ord in order_dict[i_man]:
		print("{0}: {1}".format(i_ord.title(), order_dict[i_man][i_ord]))

print(order_dict)