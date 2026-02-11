kontacts_book = dict()
while True:
	print("Текущие контакты:")
	if not kontacts_book:
		print("Пусто")
	else:
		for i in kontacts_book:
			print(i, kontacts_book[i])
	name = input("\nВведите имя: ")
	if name in kontacts_book:
		print("Ошибка: такое имя существует.")
		print()
		continue
	elif name == "конец":
		for i in kontacts_book:
			print(i, kontacts_book[i])
			print("Завершение программы!")
		break
	kontacts_book[name] = input("Введите номер телефона: ")
	print()


# Чутка другое решение но в принципе одно и то же
# book_dict = dict()

# while True:
# 	print("\nТекущий список:")
#
# 	if book_dict:
# 		for i in book_dict:
# 			print(f"{i}: {book_dict[i]}")
# 	else:
# 		print("Пусто.")
#
# 	print()
#
# 	end_programm = input("Нажмите любую клавишу, чтоб продолжить. Или введите 'end': ")
#
# 	if end_programm == "end":
# 		print("Завершение прогарммы!")
# 		break
#
# 	while True:
# 		name = input("Введите имя: ")
#
# 		if name in book_dict:
# 			print('Ошибка! Такое имя уже существует!')
# 		else:
# 			phone = int(input("Введите номер телефона: "))
# 			book_dict[name] = phone
# 			break


