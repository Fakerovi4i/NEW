def is_palindrome(new_list):
	palindrome = new_list[:]
	palindrome.reverse()
	if palindrome == new_list:
		return True
	else:
		return False
num_list = [1, 2]
palindrome_list = []
answer_list = []

for i in range(len(num_list)-1):
	for j in range(i, len(num_list)):
		palindrome_list.append(num_list[j])
	if is_palindrome(palindrome_list):
		break
	answer_list.append(num_list[i])
	palindrome_list = []

answer_list.reverse()
print("Последовательность:", num_list)
print("Нужно приписать чисел;", len(answer_list))
print("Сами числа:", answer_list)
