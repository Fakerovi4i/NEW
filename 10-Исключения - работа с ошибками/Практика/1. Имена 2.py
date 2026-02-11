sum_name = 0
counter_line = 0

with open('errors.log', 'a', encoding='utf-8') as log_open:
    with open('people.txt', 'r', encoding="utf-8") as people_open:
        for i_name in people_open:
            counter_line += 1
            counter_len = len(i_name.strip())
            sum_name += counter_len
            try:
                if counter_len < 3:
                    raise ValueError
            except ValueError:
                print("Ошибка: В строке {} менее 3-х символов.".format(counter_line))
                log_open.write("Ошибка в строке {}. Имя '{}' короче 3-х символов.\n".format(counter_line, i_name.strip()))
        print("Общее количество символов в файле: {}".format(sum_name))
