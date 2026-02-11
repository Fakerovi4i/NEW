flag = False
while flag == False:
    count_digit = 0
    passw = input("Введите пароль: ")
    if passw.isalpha() or passw.islower() or len(passw) < 8:
        print("Попробуйте еще раз!")
        continue
    for i in passw:
        if i.isdigit():
            count_digit += 1
        if count_digit >= 3:
            flag = True
            break
    if flag == False:
        print("Попробуй еще раз бро!")

print("Ну наконец-то!")