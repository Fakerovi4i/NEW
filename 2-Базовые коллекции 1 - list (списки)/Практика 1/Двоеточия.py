s = input("Введите текст: ")

s_list = list(s)
count = -1
count2 = 0

for i in s_list:
	count += 1
	if i == ":":
		s_list[count] = ";"
		count2 += 1


print("Исправленная строка:", end = " " )
for i in s_list:
	print(i, end = "")
print('\nКоличество замен:', count2)

