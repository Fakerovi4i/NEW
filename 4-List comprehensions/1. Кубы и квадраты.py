a = int(input("Введите начало диапазона: "))
b = int(input("Введите конец диапазона: "))

squer_list = [x ** 2  for x in range(a, b+1)]
cube_list = [x ** 3 for x in range(a, b+1)]

print("Список квадратов чисел:", squer_list)
print("Список кубов чисел:", cube_list)