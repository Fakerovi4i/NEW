data = {(5000, 123456): ('Иванов', 'Василий'),
		(6000, 111111): ('Иванов', 'Петр'),
		(7000, 222222): ('Медведев', 'Алексей'),
		(8000, 333333): ('Алексеев', 'Георгий'),
		(9000, 444444): ('Георгиева', 'Мария')}

while True:
    seria_number = input("Введите номер и серию паспорта: ").split()
    seria_number = tuple(int(i) for i in seria_number)

    for i_key_tuple, i_value_tuple in data.items():
        if i_key_tuple == seria_number:
            print(i_value_tuple[0], i_value_tuple[1])