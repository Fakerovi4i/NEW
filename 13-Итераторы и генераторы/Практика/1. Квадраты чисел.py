# Что нужно сделать
# Пользователь вводит число N. Напишите программу,
# которая генерирует последовательность из квадратов чисел
# от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так далее).
# Реализацию напишите тремя способами:
# класс-итератор,
# функция-генератор
# и генераторное выражение.

user_num = 5
# 1 СПОСОБ
class My_iter:
    def __init__(self, n):
        self.__n = n
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__counter < self.__n:
            self.__counter += 1
            return self.__counter ** 2
        raise StopIteration

iter = My_iter(user_num)

for i in iter:
    print(i, end=" ")

print()
# 2 СПОСОБ

def my_gen(num):
    for i in range(num):
        yield (i+1)**2

gen = my_gen(user_num)
for i in gen:
    print(i, end=" ")

print()
# 3 СПОСОБ
gen_2 = ((i+1)**2 for i in range(user_num))
for i in gen_2:
    print(i, end = " ")