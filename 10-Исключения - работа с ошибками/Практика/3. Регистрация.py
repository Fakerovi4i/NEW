def drop_exeption(lst):
    if len(lst) < 3:
        raise IndexError("Не присутствуют все три поля!")

    name, email, age = lst[0], lst[1], lst[2]
    if not name.isalpha():
        raise NameError("Поле «Имя» содержит НЕ только буквы")

    if "." not in email or "@" not in  email:
        raise SyntaxError("Поле «Имейл» НЕ содержит @ и точку")

    if age.isdigit():
        if not (9 < int(age) < 100):
            raise ValueError("Поле «Возраст» НЕ представляет число от 10 до 99")
    else:
        raise ValueError("Поле «Возраст» НЕ число!")


with open("registration.txt", 'r', encoding='utf-8') as open_registration:
    with open("registration_bad.log", "w", encoding='utf-8') as open_bad:
        with open("registration_good.log", "w", encoding='utf-8') as open_good:
            for i_line in open_registration:
                try:
                    data_list = i_line.split()
                    drop_exeption(data_list)
                    open_good.write(i_line)
                except (IndexError, NameError, SyntaxError, ValueError) as exc:
                    open_bad.write(f"{i_line.strip()}:   {exc}\n")


