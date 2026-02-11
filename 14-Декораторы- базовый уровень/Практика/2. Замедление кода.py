from typing import Callable, Any
import functools
import time


def delay(func: Callable) -> Callable:
    """Декоратор ожижания перед выполнением основной функции"""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        print('Ожидание....')
        time.sleep(2)
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@delay
def test():
    print('<Тут что-то происходит...>')

test()