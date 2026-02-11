user_string = input('Введите строку: ')
try:
    file_for_write = open('file_for_write.txt', 'w')
    file_for_write.write(user_string)
except FileNotFoundError:
    print('Неверно указан путь.')
except ZeroDivisionError:
    print('Делить на ноль нельзя.')
except SyntaxError:
    print('Что-то не так с синтаксисом кода.')
else:
    print("Все прошло без ошибок.")
finally:
    file_for_write.close()
    print(file_for_write.closed)