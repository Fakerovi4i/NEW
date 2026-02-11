counter = 0
sum_name = 0
try:
    people_open = open('5.1. people.txt', 'r')
    for i_name in people_open:
        counter = len(i_name)
        if i_name.endswith('\n'):
            counter -= 1
        if len(i_name) < 3:
            raise BaseException("Длина одной из строк короче 3х символов")
        sum_name += counter
    print(sum_name)
except FileNotFoundError:
    print('Файл не найден.')
finally:
    people_open.close()
    print(people_open.closed)
