import math
def is_integer(input):#Проверка на целочисленность заменить на проверку просто числа если будет float
    try:
        int_input = int(input)
        if str(int_input) == input:
            return True
    except ValueError:
        return False

def sqrt_num(num):
    return math.sqrt(num)

try:
    user_input = input('Введте число для поиска квадратного корня: ')
    if not is_integer(user_input):#Проверка на целые числа, заменить на проверку числа если использовать float
        raise ValueError('Введено не целое число!')

    user_num = int(user_input)

    if user_num < 0:
        raise ValueError("Невозможно найти корень отрицательного числа!")
    print(f'Квадратный корень числа {user_num}:', sqrt_num(user_num))
except ValueError as exc:#Обработка ошибок ввода отрицательных чисел и дробных
    print(exc)
except Exception as exc:
    print(f'Ошибка: {exc}')
