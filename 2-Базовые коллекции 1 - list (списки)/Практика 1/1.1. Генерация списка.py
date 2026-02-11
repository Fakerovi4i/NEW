N = int(input("Введите число: "))
num_list = []
for num in range(1, N+1, 2):
	num_list.append(num)
print("Список нечетных чисел от 1 до N:", num_list)