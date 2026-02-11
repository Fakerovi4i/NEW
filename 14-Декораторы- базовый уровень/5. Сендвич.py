from typing import Callable

def ingridients(func:Callable) -> Callable:
    """Декоратор обертка для начинки"""
    def wrapped(*args, **kwargs) -> None:
        print("  #помидоры#")
        result = func(*args, **kwargs)
        print("    ~салат~")
        return result
    return wrapped

def bread(func:Callable) -> Callable:
    """Декоратор хлеб"""
    def wrapped(*args, **kwargs) -> None:
        print(r"</----------\>")
        result = func(*args, **kwargs)
        print(r"  <\______/>")
        return result
    return wrapped

@bread
@ingridients
def feeling(*args, **kwargs) -> None:
    """Функция начинка"""
    print("  --ветчина--")

feeling()