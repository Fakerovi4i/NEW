
first_m = input("Первое сообщение: ")
second_m = input("Второе сообщение: ")
first_list = list(first_m)
second_list = list(second_m)

if (first_list.count('!') + first_list.count('?')) > (second_list.count('!') + second_list.count('?')):
	print("Третье сообщение:", first_m, second_m)
elif (first_list.count('!') + first_list.count('?')) < (second_list.count('!') + second_list.count('?')):
	print("Третье сообщение:", second_m, first_m)
else:
	print('Ой')