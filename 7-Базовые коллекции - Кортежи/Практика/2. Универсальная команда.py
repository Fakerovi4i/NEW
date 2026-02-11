def IsPrime(num):
	for i in range(2, num):
		if num % i == 0:
			return False
	return True

def Crypto(list):
	return [i_value for i_index, i_value in enumerate(list)
			if IsPrime(i_index) and i_index > 1]
print(Crypto(("О Дивный Новый мир!")))
print(Crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))