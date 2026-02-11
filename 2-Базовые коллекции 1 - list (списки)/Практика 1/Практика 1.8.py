word = input("Введите слово: ")
word = list(word)

flag = True

for i in range(len(word)):
	if word[i] != word[-i-1]:
		print("Число не являтеся полиндромом!")
		flag = False
		break
	else:
		flag = True

if flag:
	print("Число явялется полиндромом!")