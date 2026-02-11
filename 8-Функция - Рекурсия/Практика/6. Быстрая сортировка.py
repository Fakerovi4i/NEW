



def partition(list_part):
	less_l = []
	egal_s = []
	grater_s = []
	base = list_part[-1]
	for i in list_part:
		if i < base:
			less_l.append(i)
		elif i == base:
			egal_s.append(i)
		else:
			grater_s.append(i)

	return less_l, egal_s, grater_s


def fast_sort(li_st):
	if len(li_st) < 2:
		return li_st
	else:
		less_list, egal_list, grater_list = partition(li_st)

	return fast_sort(less_list) + egal_list + fast_sort(grater_list)


orig_list = [5, 8, 9, 4, 2, 9, 1, 8]

print(fast_sort(orig_list))