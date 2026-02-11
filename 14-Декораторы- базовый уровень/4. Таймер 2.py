from time import time
from typing import Callable, Any, Union

def timer(func: Callable) -> Callable:
    '''Декоратор. Выводит время работы переданной функции'''
    def wrapped_func(*args, **kwargs) -> Any:
        start_time = time()
        result = func(*args, **kwargs)
        stop_time = time()
        run_time = round(stop_time - start_time, 4)
        print(f"Время работы программы: {run_time} секунд.")
        return result
    return wrapped_func

@timer
def cubes_sum(number: int) -> int:
    """Считает сумму кубов от 1 до 10 000, number раз."""
    result = 0
    for _ in range(number):
        result += sum(i**3 for i in range(10000))
    return result

my_test = cubes_sum(200)
print(my_test)


