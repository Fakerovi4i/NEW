while True:
    ip_adress = input("Введите ип: ").split(".")

    if len(ip_adress) != 4:
        print("ip-адресс - это 4 числа роазделенных точкой")
        continue

    valid = True

    for i in ip_adress:
        if not i.isdigit():
            print(f"{i} - это не целое число!")
            valid = False
            break
        elif int(i) > 255:
            print(f"{i} - больше 255")
            valid = False
            break
    if valid:
        break

print("ip-адрес коректен:", ".".join(ip_adress))

