quant_rol = int(input("Введите количество роликов: "))
roll_list = []

for i in range(quant_rol):
	print(f"Размер пары {i+1}:", end = " ")
	roll = int(input())
	roll_list.append(roll)

quant_people = int(input("Введите количество людей: "))
people = 0

for ii in range(quant_people):
	print(f"Размер ноги человека {ii+1}:", end=" ")
	people_leg = int(input())
	if people_leg in roll_list:
		people += 1
		roll_list.remove(people_leg)

print("Наибольшее количество людей, которые могут взять ролики:", people)