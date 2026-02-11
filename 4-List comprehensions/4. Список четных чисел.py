a = 1
b = 10

even_list = [x
			 for x in range(a, b+1)
			 if x % 2 == 0]
print(even_list)