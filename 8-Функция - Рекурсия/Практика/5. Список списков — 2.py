def open_list(n_list, new_list=[]):
	for i in n_list:
		if isinstance(i, int):
			new_list.append(i)
		else:
			open_list(i)
	return new_list

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(open_list(nice_list))