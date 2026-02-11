import zipfile
import collections

def unzip(archive):
	zfile = zipfile.ZipFile(archive, 'r')
	for i_file_name in zfile.namelist():
		zfile.extract(i_file_name)
	zfile.close()

def collect_stats(file_name):
	result = {}
	if file_name.endswith('.zip'):
		unzip(file_name)
		file_name = ''.join((file_name[:-3], 'txt'))
	text_file = open(file_name, 'r')
	for i_line in text_file:
		for j_char in i_line.lower():
			if j_char.isalpha():
				if j_char not in result:
					result[j_char] = 0
				result[j_char] += 1
	text_file.close()
	return result

def print_stats(stats):
	print('+{:-^19}+'.format('+'))
	print('|{: ^9}|{: ^9}|'.format('Буква', 'Частота'))
	print('+{:-^19}+'.format('+'))
	for i_char, count in stats.items():
		print('|{: ^9}|{: ^9}|'.format(i_char, count))
	print('+{:-^19}+'.format('+'))

def sort_sequency(stats_dict):
	sort_values = sorted(stats_dict.values(), reverse=True)
	sorted_dict = collections.OrderedDict()
	for i_value in sort_values:
		for j_key in stats_dict.keys():
			if stats_dict[j_key] == i_value:
				sorted_dict[j_key]  = stats_dict[j_key]

	return sorted_dict


file_name = 'voina_i_mir.zip'
stats = collect_stats(file_name)
stats = sort_sequency(stats)
print_stats(stats)

# import os
# import zipfile
# os.chdir("C://")
#
# def sort_gist_list(dict_sym):
#     sort_list = [(value, key) for key, value in dict_sym.items()]
#     return sorted(sort_list)
#
# def gist_sym(big_text):
#     dict_sym_gist = dict()
#     for i_sym in big_text:
#         if i_sym.isalpha():
#             dict_sym_gist[i_sym] = dict_sym_gist.get(i_sym, 0) + 1
#     return sort_gist_list(dict_sym_gist)
#
#
# path = (os.path.abspath(os.path.join("Users", "Mohen-Tohen", "Desktop", "voina_i_mir.zip")))
# zip_file_open = zipfile.ZipFile(path, "r")
# text_open = zip_file_open.open("warandpeace.txt", "r")
# woinaimir_text = text_open.read().decode("utf-8")
# text_open.close()
# zip_file_open.close()
#
# gistogram_list = gist_sym(woinaimir_text)
#
# for i in gistogram_list:
#     print(f"{i[1]}: {i[0]}")
#

