zoo_list = ['lion', 'kangaroo', 'elephant', 'monkey']

zoo_list.insert(2, "bear")
zoo_list.remove('elephant')

print("Зоопарк:", zoo_list)
print("Лев сидит в клетке:", zoo_list.index("lion")+1)
print("Обезьяна сидит в клетке:", zoo_list.index("monkey")+1)