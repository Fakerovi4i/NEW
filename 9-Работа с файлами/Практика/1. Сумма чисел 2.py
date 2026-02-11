import os

file = open(os.path.join('..', 'numbers.txt'), 'r', encoding='utf-8')
summ = 0
for i_num in file:
	summ += int(i_num)
file.close()

file_summ = open('file_summ.txt', 'w')
file_summ.write(str(summ))
file_summ.close()