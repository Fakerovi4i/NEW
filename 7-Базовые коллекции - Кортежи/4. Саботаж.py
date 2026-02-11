text = "so~mec~od~e"
string_index = []

for i_sym, sym in enumerate(text):
	if sym == "~":
		string_index.append(i_sym)

string_index = " ".join([str(i) for i in string_index])
print("Ответ:", string_index)