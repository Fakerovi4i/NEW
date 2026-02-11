#Тут функция принимает целую фразу и представление списка нагроможденно и плохо читается
def cezar_pass(text, shift):
	frase_list = [(alphabet[(alphabet.index(sym) + shift) % 33] if sym in alphabet else sym) for sym in text]
	frase_cezar = ''
	for i in frase_list:
		frase_cezar += i
	return frase_cezar

alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
text = "это питон"
K = 3

text_cezar = cezar_pass(text, K)

print(text_cezar)


# Вот это вариант по логике проще тут функция принимает только символ и конвертирет его
# def change(sym, move):
# 	index = (alphabet.index(sym) + move) % 33
# 	return alphabet[index]
#
# alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"  # 0 - 32 последний индекс - 1 - 33 буквы
# text = "это питон."
# K = 3
#
# new_text = [change(i, K) if i in alphabet else i for i in text]
#
# text_done = ""
#
# for i in new_text:
# 	text_done += i
#
# print(text_done)