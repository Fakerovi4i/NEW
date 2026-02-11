name = input('Введите имя: ')
while True:
    print('Введите 1 - написать сообщение, 2 - увидеть чат')
    choise = input('Введите 1 или 2: ')
    try:
        if choise == '1':
            message = input('Введите сообщение: ')
            with open('4.1. messages.txt', 'a') as file:
                file.write(f"{name}: {message}\n")
        elif choise == '2':
            with open('4.1. messages.txt', 'r') as file:
                for i_line in file: #Можно использовать readline
                    print(i_line[:-1])
        else:
            print('Введена неверная команда, введите 1 или 2')
    except FileNotFoundError:
        print("Системная ошибка: Пока ничего нет\n")


#   ТУТ ВСЕ КРУЧЕ РЕАЛИЗОВАННО!!
# def my_chat(choice_num_str, user):
#     if choice_num_str == "1":
#         try:
#             with open("chat.txt", "r", encoding="utf-8") as open_chat:
#                 print(open_chat.read())
#         except FileNotFoundError:
#             print("Чат пока Пуст!")
#
#     if choice_num_str == "2":
#         with open("chat.txt", "a", encoding="utf-8") as open_chat:
#             while True:
#                     try:
#                         message = input("Введите сообщение: ")
#                         if not message.strip():
#                             raise ValueError("Ошибка: Пустой ввод.")
#                         open_chat.write(f"{user}:\n"
#                                         f"    {message}\n")
#                         break
#                     except ValueError as exc:
#                         print(exc)
#
#
# while True:#Легкая и простая проверка на содержимое
#     user_name = input("Введите имя пользователя: ")
#     if user_name.strip():
#         break
#     else:
#         print("Введите хоть что-то.")
#
# while True:
#     print("1: Посмотреть текущий текст чата;\n"
#           "2: Отправить сообщение;\n"
#           "3: Завершить;")
#     try:
#         choice = input("Ваш выбор: ").strip().lower()
#         if choice not in ("1", "2", "3"):
#             print(choice)
#             raise ValueError("Ошибка: Неверное значение выбора.")
#         if choice == "3":
#             print("Закрытие чата!")
#             break
#         my_chat(choice, user_name)
#     except ValueError as exc:
#         print(exc)
#
#
#
# #

