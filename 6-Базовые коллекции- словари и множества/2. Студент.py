info_student = "Илья Иванов Москва МГУ 5 4 4 4 5".split()
info = dict()

info["Имя"] = info_student[0]
info["Фамилия"] = info_student[1]
info["Город"] = info_student[2]
info["ВУЗ"] = info_student[3]
info["Оценки"] = [int(i) for i in info_student[4:]]

# for i in info_student[4:]:
#     info["Оценки"].append(int(i))


for i in info:
    print(f"{i}: {info[i]}")