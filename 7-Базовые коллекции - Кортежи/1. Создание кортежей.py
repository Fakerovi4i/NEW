import random
def random_nums(num_1, num_2):
	list = [random.randint(num_1, num_2) for _ in range(5)]
	return tuple(list)

first_tuple = random_nums(0, 5)
second_tuple = random_nums(-5, 0)
third_tuple = first_tuple + second_tuple

print(first_tuple)
print(second_tuple)
print(third_tuple)
print("Количество нулей в 3-м кортеже:", third_tuple.count(0))