small_storage = {
	'гвозди': 5000,
	'шурупы': 3040,
	'саморезы': 2000
}
big_storage = {
	'доски': 1000,
	'балки': 150,
	'рейки': 600
}
big_storage.update(small_storage)

while True:
    item = input("что ищем: ")
    item_found = big_storage.get(item)

    if not item_found:
        print("Такого нет")
    else:
        print(f'{item}: {item_found}')