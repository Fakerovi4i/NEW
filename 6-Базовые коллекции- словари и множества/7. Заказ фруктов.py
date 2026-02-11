order = {'apple': 2,
         'banana': 3,
         'pear': 1,
         'watermelon': 10,
         'chocolate': 5}

incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}
summ = 0
no_item = []

for i_order in order:
    summ += incomes.get(i_order, 0) * order[i_order]
    if not i_order in incomes:
        no_item.append(i_order)

print("Итоговая сумма заказа:", summ)
print("В наличии нет:", no_item)


