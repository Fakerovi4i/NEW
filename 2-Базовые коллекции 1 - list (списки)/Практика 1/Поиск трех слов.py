text_q = []
counter_text = [0, 0, 0]

for i in range(3):
	print(f'Введите искомое слово {i+1}: ', end = " ")
	text = input()
	text_q.append(text)
text = input("Введите слово: ")
while text != "end":
	for i in range(3):
		if text_q[i] == text:
			counter_text[i] += 1
	text = input("Введите слово: ")

for i in range(3):
	print(f"Подсчет слов ({text_q[i]}) в тексте: {counter_text[i]}")
	