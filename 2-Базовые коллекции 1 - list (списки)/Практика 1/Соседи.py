text = input("Введите текст: ")
text_list = list(text)
num_symb = int(input("Введите номер символа: "))
num_symb = num_symb - 1
count_sym = -1


print("Символ слева:", text_list[num_symb-1])
print("Символ справа:", text_list[num_symb+1])
for i_symb in text_list:
	if i_symb == text_list[num_symb]:
		count_sym += 1
if count_sym >= 1:
	print("Таких же символов:", count_sym)
else:
	print("Таких же символов нет.")



