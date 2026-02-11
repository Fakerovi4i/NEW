def shift(first, second, start):
	new_str = ""
	for i in range(len(second)):
		new_str += second[(start + i) % len(second)]
	if new_str == first:
		return True
	else:
		return False

first_str = "abcd"
second_str = "cdab"
start = second_str.index(first_str[0])

if shift(first_str, second_str, start):
	print("Первая строка получается из второй со сдвигом", start)
else:
	print("Первую строку не получить из второй.")
