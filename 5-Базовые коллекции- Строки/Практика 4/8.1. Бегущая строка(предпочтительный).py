first_str = "abcd"
second_str = "cdab"
start = second_str.index(first_str[0])
if len(first_str) != len(second_str):
	print("Первую строку не получить из второй.")
elif second_str in first_str * 2:
	print("Первая строка получается из второй со сдвигом", start)
else:
	print("Первую строку не получить из второй.")