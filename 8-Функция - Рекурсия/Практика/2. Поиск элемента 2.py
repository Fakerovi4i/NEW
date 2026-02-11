site = {
'html': {
    'head': {
    'title': 'Мой сайт'
},
'body': {
    'h2': 'Здесь будет мой заголовок',
    'div': 'Тут, наверное, какой-то блок',
    'p': 'А вот здесь новый абзац',
    "new": {
        "create": "И вот новейший код!"
    }
}
}
}

def find_key(key, data, deep):
    deep -= 1
    if key in data:
        return data[key]

    for i_value in data.values():
        if deep == 0:
            result = None
            print("Закончился счетчик глубины")
            return result
        if isinstance(i_value, dict):
            result = find_key(key, i_value, deep)
            if result:
                break
    else:
        result = None
    return result


f_key = input("Введите искомый ключ: ")
deep_question = input("Задать глубину?: ")

if deep_question == "y":
    deep_f = int(input("Введите глубину: "))
else:
    deep_f = -1

key_find = find_key(f_key, site, deep_f)
print(key_find)