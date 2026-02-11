template = "С днём рождения, {name}! С {age}-летием тебя!"
name_list_line = input("Список людей через запятую: ").split(", ")
age_list_line = input("Возраст людей через пробел: ").split()

for i_man in range(len(name_list_line)):
	print(template.format(name=name_list_line[i_man], age=age_list_line[i_man]))

people = [
	" ".join([name_list_line[i_man], age_list_line[i_man]])
	for i_man in range(len(name_list_line))
]

people_str = ", ".join(people)
print("Именинники: ", people_str)


