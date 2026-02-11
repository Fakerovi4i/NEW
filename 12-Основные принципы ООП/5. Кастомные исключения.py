class DivisionError(Exception):
    pass

with open("5.1. pairs.txt", "r") as file:
    counter = 0
    for line in file:
        try:
            counter += 1
            temp = line.split()
            if float(temp[0]) < float(temp[1]):
                raise DivisionError("нельзя делить меньшее на большее")
            print(f"\n{counter}. {temp[0]} / {temp[1]} =", round(float(temp[0]) / float(temp[1]), 2))
        except DivisionError:
            print(f"\n{counter}. Ошибка в {counter}-й строке (Делить меньшее на большее нельзя)")
    else:
        print("\nВсе строки обработаны успешно.")

