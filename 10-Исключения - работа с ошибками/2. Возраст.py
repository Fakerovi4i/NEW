#Так и не решил проблему с PermissionError, не могу получить IsADirectoryError
import os
names_list = ["Ан", "Бн", "Зн", "Дн", "Жа", "Хо", "Ук", "Бм", "Эж", "Зр", "Го"]
count = 0

try:
	ages_1 = open("ages.txt", 'r')
	names_ages = open('result.txt', 'w', encoding='utf-8')
	for i_age in ages_1:
		count += 1
		name_age = ' '.join((names_list[count-1], i_age))
		names_ages.write(name_age)
	ages_1.close()
	names_ages.close()
except FileExistsError:
	print('Файл уже существет.')
except IsADirectoryError:
	print('Эта папка, не файл!')
except TypeError or ValueError:
    print('Неверный тип данных или некорректное значение!')







