goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
print('Текущий асортимент:', goods)

new_good = input('Новый фрукт: ')
new_price = int(input('Цена: '))

goods.append([new_good, new_price])
for i_good in goods:
    i_good[1] += i_good[1] * 0.08

print('Новый асортимент с ув. ценой:', goods)