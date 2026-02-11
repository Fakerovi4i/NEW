count = 0
num_list = []
while count < 4:
	num = int(input("Введите число (до 255): "))
	if num <= 255:
		num_list.append(num)
		count += 1
	else:
		print("Ошибка! Число больше 255!")

ip_adress = "{0}.{1}.{2}.{3}".format(
	num_list[0],
	num_list[1],
	num_list[2],
	num_list[3]
)

print(ip_adress)