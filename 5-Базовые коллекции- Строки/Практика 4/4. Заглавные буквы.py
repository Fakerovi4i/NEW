text = "Кажется, я забыл выключить утюг"
text_list = text.split()
new_list = []
new_text = ''

for i in text_list:
	new_list.append(''.join([i[:1].upper(), i[1:]]))
new_text = " ".join(new_list)

print(new_text)
#print(text.title())