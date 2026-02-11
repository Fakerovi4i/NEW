import random

counter_summ = 0
with open("out_file.txt", "w") as file_open:
    try:
        while counter_summ < 777:
            i_num = int(input("Введите число: "))
            if random.randint(1, 13) == 7:
                raise ValueError
            file_open.write(f"{i_num}\n")
            counter_summ += i_num
    except ValueError:
        print("Вас постигла неудача!")
    else:
        print("Вы успешно выполнили условие для выхода из порочного цикла!")
