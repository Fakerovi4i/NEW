import random

alphabet = "абвгдеёжзийклмнопрстуфхцчщъыьэюя"
first_list = [alphabet[random.randint(0, len(alphabet)-1)] for _ in range(10)]
second_list = [alphabet[random.randint(0, len(alphabet)-1)] for _ in range(10)]

first_list_dict = dict()
second_list_dict = dict()
for i_lit, lit in enumerate(first_list):
	first_list_dict[i_lit] = lit
for i_lit, lit in enumerate(second_list):
	second_list_dict[i_lit] = lit

print(first_list)
print(second_list)
print(first_list_dict)
print(second_list_dict)