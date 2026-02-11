def factorial(n):
	if n == 1:
		return 1
	fact_num = n * factorial(n - 1)
	return fact_num

num = factorial(5)
print(num)