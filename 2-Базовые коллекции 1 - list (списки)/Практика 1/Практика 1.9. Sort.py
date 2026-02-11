def sort(num_list):
	for i in range(len(num_list)):
		for ii in range(i, len(num_list)):
			if num_list[ii] < num_list[i]:
				num_list[ii], num_list[i] = num_list[i], num_list[ii]

num_list = [1, 4, -3, 0, 10]

sort(num_list)

print(num_list)
