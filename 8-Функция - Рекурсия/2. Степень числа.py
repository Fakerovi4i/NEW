def power(a, n):
	if n == 1:
		return a
	return a * power(a, n-1)

float_num = 1.5
int_num = 5
print(float_num, '**', int_num, '=', power(float_num, int_num))

# Правильный результат:
# Введите вещественное число: 1.5
# Введите степень числа: 5
# 1.5 ** 5 = 7.59375
