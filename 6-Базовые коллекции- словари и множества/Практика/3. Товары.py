goods = {
'Лампа': '12345',
'Стол': '23456',
'Диван': '34567',
'Стул': '45678',
}
store = {
'12345': [
{'quantity': 27, 'price': 42},
],
'23456': [
{'quantity': 22, 'price': 510},
{'quantity': 32, 'price': 520},
],
'34567': [
{'quantity': 2, 'price': 1200},
{'quantity': 1, 'price': 1150},
],
'45678': [
{'quantity': 50, 'price': 100},
{'quantity': 12, 'price': 95},
{'quantity': 43, 'price': 97},
],
}

for i_mebel in goods:
	summ_goods = 0
	summ_item = 0
	for i_cod in store[goods[i_mebel]]:
		summ_item += i_cod['quantity']
		summ_goods +=  i_cod['quantity'] * i_cod['price']
	print("{0} - {1} штук, общая стоимость: {2} рубля.".format(i_mebel, summ_item, summ_goods))




