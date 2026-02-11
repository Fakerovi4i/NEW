N = int(input("Введите количество человек: "))
K = int(input("Введите число в считалке: "))
print(f"Значит выбывает каждый {K}-й человек")
people = list(range(1, N+1))
index = 0

while len(people) > 1:
	print("\nТекущий круг людей:", people)
	#print(index)
	print("Начало счета с номера:", people[index])
	index = (K + index - 1) % len(people)
	#print(index)
	print("Выбывает человек под номером:", people[index])
	people.remove(people[index])
	if index >= len(people)-1:
		index = 0
print("\nОстался человек под номером:", people[index])










