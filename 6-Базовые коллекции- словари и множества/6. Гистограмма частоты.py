text = "Здесь что-то написано"
text_dict = dict()

for i in text.lower():
	if i in text_dict:
		text_dict[i] += 1
	else:
		text_dict[i] = 1

for i in sorted(text_dict.keys()):
	print(i, ":", text_dict[i])
print("Максимальная частота:", max(text_dict.values()))