text = "Здесь что-то написано"
text_dict = dict()

for i in text:
	if i in text_dict:
		text_dict[i] += 1
	else:
		text_dict[i] = 1
print("Оригинальный словарь частот:")
for i in sorted(text_dict.keys()):
	print(i, ":", text_dict[i])

def back_dict_func():
	back_dict = dict()
	for i in text_dict.values():
		back_dict[i] = []
		for i_sym in text:
			if text_dict[i_sym] == i and not i_sym in back_dict[i]:
				back_dict[i].append(i_sym)
	return back_dict

print("Инвертированный словарь частот:")
invert = back_dict_func()
for i in invert :
	print(i, invert[i])

