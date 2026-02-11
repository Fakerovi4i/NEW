# def isPalindrome(string):
# 	text_dict = dict()
# 	for i in string:
# 		text_dict[i] = text_dict.get(i, 0) + 1
#
# 	odd_count = 0
# 	for i in text_dict.values():
# 		if i % 2 != 0:
# 			odd_count += 1
#
# 	return odd_count <= 1
#
# text = input("Введите символы для проверки: ")
#
# if isPalindrome(text):
# 	print("Можно сделать палиндромом!")
# else:
# 	print("Нельзя сдeлать полиндромом!")


def isPalindrome(string):
	text_dict = dict()
	for i in string:
		text_dict[i] = text_dict.get(i, 0) + 1

	odd_count = 0
	for i in text_dict.values():
		if i % 2 != 0:
			odd_count += 1
		if odd_count > 1:
			return False
	return  True

text = input("Введите текст: ")

if isPalindrome(text):
	print("Можно сделать палиндром!")
else:
	print("Нельзя сделать палиндром.")
