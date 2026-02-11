import os

try:
    devide = ''.join(['\n\n', '*' * 40])  # Просто разделитель
    path_1 = os.path.abspath(os.path.join('..', '3-Методы для работы со списками', 'Задания'))
    new_file = open(os.path.join('..', 'new_file.txt'), 'w') #прописал путь в другую папку добавил os.path.join(..)
    for i_file in os.listdir(path_1):
        path_2 = open(os.path.join(path_1, i_file), 'r')
        path_2_read = path_2.read()
        new_file.write(str(path_2_read))
        new_file.write(devide)
        new_file.write('\n')
except TypeError:
    print('Где-то неверный тип данных.')
except:
    print('Что-то пошло не так.')
else:
    print('Все четко.')
finally:
    new_file.close()
    path_2.close()
    print(new_file.closed, path_2.closed)