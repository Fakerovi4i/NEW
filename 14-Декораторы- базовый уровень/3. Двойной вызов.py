from typing import Callable, Any

def do_twice(func:Callable) -> Callable:
    """Декоратор, дублирует код переданной функции"""
    def wrapped_func(*args, **kwargs) -> None:
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapped_func

@do_twice
def greeting(name: str) -> None:
    '''Функция печатает переданный пользователем текст один раз'''
    print('Привет, {name}!'.format(name=name))


greeting('Tom')

