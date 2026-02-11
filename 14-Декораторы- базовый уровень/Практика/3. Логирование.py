from typing import Callable, Any
import functools
from datetime import datetime


def loging(func: Callable) -> Callable:
    """Декоратор логирования:
     1. Выводит функцию и документацию к ней.
     2. Записывает ошибки.
     """
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print(f"\nФункция: {func.__name__}")
        print(f"Документация: {func.__doc__}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as exc:
            with open("Ошибки.log", "a") as file:
                file.write(f'[{datetime.now().replace(microsecond=0)}] {func.__name__}: {type(exc).__name__}: {exc}\n\n')
            print("Ошибка записана в лог.")
            return None
    return wrapped_func


@loging
def test(num: int) -> int:
    """
    -Функция для теста, выводит число на экран
    ошибка с прибавлением числа и строки:
    :param num: int
    :return: int
    """
    print('Число функции:', num)
    return num + 'd'

@loging
def test_2():
    """
    Ничего не делает. Вызывает ошибку деления на ноль!
    :return: None
    """
    return 10 / 0

test(10)
test_2()