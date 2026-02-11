from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Callable:
    """Декоратор шутка."""
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        input("Привет как дела?: ")
        print("А у меня не очень! Ладно держи свою функцию!")
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')

test()