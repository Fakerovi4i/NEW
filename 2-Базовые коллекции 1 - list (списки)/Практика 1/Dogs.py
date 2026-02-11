Dogs = [33, 99, 1, 17, 14]
max = Dogs[0]
min = Dogs[0]
def max_min(max, min):
	for i in Dogs:
		if i > max:
			max = i
		if i < min:
			min = i
	return max, min

max, min = max_min(max, min)

def counter_i(max, min):
	counter = -1
	for i in Dogs:
		counter += 1
		if max == i:
			max_i = counter
		if min == i:
			min_i = counter
	return max_i, min_i

max_i, min_i = counter_i(max, min)
Dogs[max_i], Dogs[min_i] = Dogs[min_i], Dogs[max_i]

print(Dogs)