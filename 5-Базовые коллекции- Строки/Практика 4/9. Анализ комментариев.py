def count_uppercase_lowercase(text):
	count_up = 0
	count_low = 0

	for i in text:
		if i.isupper():
			count_up += 1
		elif i.islower():
			count_low += 1

	return count_up, count_low

text = input("Введите строку для анализа: ")

uppercase, lowercase = count_uppercase_lowercase(text)

print("Количество заглавных букв:", uppercase)
print("Количество строчных букв:", lowercase)
