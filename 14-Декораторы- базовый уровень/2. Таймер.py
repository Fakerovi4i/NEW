from time import time
from typing import Callable, Any, Union

def timer(func: Callable, *args, **kwargs) -> Any:
    '''Функция таймер. Выводит время работы переданной функции'''
    start_time = time()
    result = func(*args, **kwargs)
    stop_time = time()
    run_time = round(stop_time - start_time, 4)
    print(f"Время работы программы: {run_time} секунд.")

    return result


def cubes_sum(number: int) -> int:
    """Считает сумму кубов от 1 до 10 000, number раз."""
    result = 0
    for _ in range(number):
        result += sum(i**3 for i in range(10000))

    return result

my_test = timer(cubes_sum, 10000)

print(my_test)


