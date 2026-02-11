def sum(*args, total=0):
	for i_data in args:
		if isinstance(i_data, int):
			total += i_data
		elif isinstance(i_data, (list, tuple)):
			total += sum(*i_data)
	return total

print(sum([[1, 2, [3]], [1], 3]))
#Ответ в консоли: 10
print(sum(1, 2, 3, 4, 5))
#Ответ в консоли: 15

print(sum(1, 2, 3))  # 6 - правильно
print(sum(4, 5))

# Решение без использования незнакомой *
# def my_sum(*args, num_total=0):
#     for i_val in args:
#         if isinstance(i_val, (int, float)):
#             num_total += i_val
#         else:
#             for i in i_val:
#                 num_total += my_sum(i)
#
#     return num_total
#
# print(my_sum([[1, 2, [3]], [1], 3]))
# print(my_sum(1, 2, 3, 4, 5))
# print(my_sum(4, 5))