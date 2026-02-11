from typing import Callable, Any

PLUGINS: dict[str, Callable] = dict()

def plug_register(func: Callable) -> Callable:
    '''Декоратор для добавления плагина в словарь'''
    PLUGINS[func.__name__] = func
    return func

@plug_register
def cubes_sum(number: int) -> int:
    """Считает сумму кубов от 1 до 10 000, number раз."""
    result = 0
    for _ in range(number):
        result += sum(i**3 for i in range(10000))
    return result

@plug_register
def feeling(*args, **kwargs) -> None:
    """Функция начинка"""
    print("  --ветчина--")


print(PLUGINS)