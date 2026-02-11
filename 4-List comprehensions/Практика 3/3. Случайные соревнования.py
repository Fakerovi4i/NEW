import random
first = [round(random.uniform(5, 10), 2) for _ in range(20)]
second = [round(random.uniform(5, 10), 2) for _ in range(20)]
third = [first[i] if first[i] > second[i]
		else second[i]
		for i in range(20)]

print(first)
print()
print(second)
print()
print(third)