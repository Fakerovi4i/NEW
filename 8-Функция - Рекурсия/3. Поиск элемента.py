site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def find_key(dict_1, key):
	if key in dict_1:
		return dict_1[key]

	for i_value in dict_1.values():
		if isinstance(i_value, dict):
			result = find_key(i_value, key)
			if result:
				break
	else:
		result = None

	return result

key_find = "h2"
value = find_key(site, key_find)

if value:
	print("Значение ключа:", value)
else:
	print("Такого ключа нет.")

