def find_first_another():
    return ", ".join([str(i) for i in array_1 if i in array_2 and i in array_3])

def find_first_with():
    new_set = set(array_1).intersection(array_2, array_3)
    return ", ".join({str(i) for i in new_set})

def find_second_another():
    new_list_secnd = [
        str(i) for i in array_1
        if i not in array_2 and not i in array_3
    ]
    return ", ".join(new_list_secnd)

def find_second_with():
    new_set_with = set(array_1).difference(array_2, array_3)
    return ", ".join([str(i) for i in new_set_with])


array_1 = [1, 2, 3, 4]
array_2 = [2, 4]
array_3 = [2, 3]

print('Задача 1:')
print("Решение без множеств:", find_first_another())
print("Решение c множеством:", find_first_with())

print('\nЗадача 2:')
print("Решение без множеств:", find_second_another())
print("Решение c множеством:", find_second_with())

