tel_dict = dict()

while True:
    text = input("Введите Фамилию имя и номер: ").split()

    if text:
        tel_dict[(text[0], text[1])] = text[2]

        for i_name, i_tel in tel_dict.items():
            print(f"{i_name[0]} {i_name[1]}: {i_tel}")
    else:
        break
