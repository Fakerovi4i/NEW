import os
str_list = []

file = open(os.path.join('..', 'zen.txt'), 'r')
for i_str in file:
	str_list.append(i_str)
str_back = str_list[::-1]

for i_str_list in str_back:
	print(i_str_list, end='')

#for i_str_list in range(len(str_list)-1, -1, -1): #Чуть сложнее
	# print(str_list[i_str_list], end='')



# def print_file_back(file_name):
#     zen_open = open(file_name)
#     zen_file = zen_open.read().split("\n")
#     for i in zen_file[::-1]:
#         print(i)
#     zen_open.close()
#
#
#
# print_file_back("zen.txt")
