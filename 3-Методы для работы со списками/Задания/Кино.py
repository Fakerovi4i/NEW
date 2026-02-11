def film_exist(films, add):
	for i_film in films:
		if i_film == add:
			return True
	return False

films = [
	'Крепкий орешек', 'Назад в будущее', 'Таксист',
	'Леон', 'Богемская рапсодия', 'Город грехов',
	'Мементо', 'Отступники', 'Деревня',
	'Проклятый остров', 'Начало', 'Матрица'
]
top_list = ['Отступники', 'Деревня',
	'Проклятый остров', 'Начало']

while True:
	print("Ваше изранное:", top_list)
	add_film = input("Введите название фильма?: ")
	command = input("Что сделать (добавить, поменять, удалить)?: ")
	if command == 'добавить':
		if film_exist(films, add_film) and (film_exist(top_list, add_film) == False):
			top_list.append(add_film)
		elif film_exist(films, add_film) == False:
			print("Такого фильма у нас нет!")
		elif film_exist(top_list, add_film):
			print("Фильм уже в избранном!")
	if command == "поменять":
		if film_exist(top_list, add_film):
			top_list.remove(add_film)
			que = int(input("На какое место: "))
			top_list.insert(que - 1, add_film)
		else:
			print("Такого фильма нет в избранном!")
	if command == "удалить":
		if film_exist(top_list, add_film):
			top_list.remove(add_film)
		else:
			print("Такого фильма нет в избранном!")


#Тут как по мне получился более изящный код и без isexist

# films = [
#     'Крепкий орешек', 'Назад в будущее', 'Таксист',
#     'Леон', 'Богемская рапсодия', 'Город грехов',
#     'Мементо', 'Отступники', 'Деревня',
#     'Проклятый остров', 'Начало', 'Матрица'
# ]
# my_top_list = []
#
# while True:
#     print('Мой топ фильмов:', my_top_list)
#     film_one = input('Введите название фильма: ')
#     if film_one in films:
#         print("Команды: добавить, вставить, удалить", end = ' ')
#         command = input()
#         if command == 'добавить':
#             if not film_one in my_top_list:
#                 my_top_list.append(film_one)
#             else:
#                 print('Такой фильм уже есть в вашем топе')
#
#         elif command == 'вставить':
#             if film_one in my_top_list:
#                 num_in_list = int(input("На какое место вставить: "))
#                 my_top_list.remove(film_one)
#                 my_top_list.insert(num_in_list-1, film_one)
#             else:
#                 print("Такого фильмы нет в топе")
#
#         elif command == 'удалить':
#             if film_one in my_top_list:
#                 my_top_list.remove(film_one)
#             else:
#                 print("Такого фильмы нет в топе")
#
#     else:
#         print('Такого фильма нет на сайте')


